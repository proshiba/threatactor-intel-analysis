#!/usr/bin/env python3
"""IOCに混入した非指標値を検出し、必要なら除去する。

出典レポート自身の参考リンク（ベンダーブログ、CERT、報道、リファレンス）や、
抽出に失敗した壊れた値がIOCとして保存されている場合がある。いずれも脅威と
無関係な値であり、横断検索で無関係な資料同士を誤って結び付ける。

判定は値ごとに行う。出典単位では判定しない。同じ資料の同じ抜粋から、
参考URLと実在の指標（C2ドメイン等）が同時に出てくるためである。

    # 検出のみ（既定）。レポートを出力して終了する
    python3 actor_profile/scripts/audit_reference_iocs.py

    # 判定内訳を確認する
    python3 actor_profile/scripts/audit_reference_iocs.py --list malformed

    # profiles/<slug>/iocs.json から除去する
    python3 actor_profile/scripts/audit_reference_iocs.py --apply

除去後は生成物の再生成が必要である。
    python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest
"""
from __future__ import annotations

import argparse
import ipaddress
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PROFILES_DIR = REPO_ROOT / "profiles"
REFERENCE_DIR = REPO_ROOT / "actor_profile" / "reference"
HOSTS_PATH = REFERENCE_DIR / "reference-hosts.json"
TLDS_PATH = REFERENCE_DIR / "iana-tlds.json"
REPORT_PATH = REPO_ROOT / "actor_profile" / "reference" / "reference-ioc-audit.json"

CHECKED_TYPES = {"url", "domain", "email"}
URL_HOST_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*://([^/?#:]+)")
HOSTNAME_RE = re.compile(r"^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?(\.[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?)*$")
# ベンダー名の短縮形を拾うための最小長。これより短いと実在ドメインと衝突しうる。
TRUNCATION_MIN = 5
# IANAの委任TLDではないが、指標として正当な名前空間。
SPECIAL_USE_TLDS = {"onion", "i2p", "bit", "exit"}


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_reference() -> tuple[frozenset[str], frozenset[str], frozenset[str]]:
    data = load_json(HOSTS_PATH)
    hosts = frozenset(h.strip().lower() for h in data.get("hosts", []) if h.strip())
    suffixes = frozenset(s.strip().lower() for s in data.get("public_suffixes", []) if s.strip())
    tlds = frozenset(load_json(TLDS_PATH).get("tlds", []))
    return hosts, suffixes, tlds


def host_of(value: str) -> str:
    match = URL_HOST_RE.match(value)
    host = (match.group(1) if match else value).strip().lower().rstrip(".")
    if "@" in host:
        host = host.rsplit("@", 1)[-1]
    return host[4:] if host.startswith("www.") else host


class Classifier:
    def __init__(self) -> None:
        self.hosts, self.suffixes, self.tlds = load_reference()

    def reference_host(self, host: str) -> bool:
        if host in self.hosts:
            return True
        labels = host.split(".")
        return any(".".join(labels[i:]) in self.hosts for i in range(1, len(labels) - 1))

    def classify(self, ioc_type: str, value: str) -> tuple[str, str] | None:
        """(判定, 理由) を返す。指標として残す場合は None。"""
        host = host_of(value)
        if not host:
            return ("malformed", "ホストを取り出せない")

        # IPアドレスはホスト名の規則に従わないが指標としては正当。
        # type が domain のままなのは分類の誤りであり、値そのものは残す。
        literal = host.strip("[]").split("%", 1)[0]
        try:
            ipaddress.ip_address(literal)
        except ValueError:
            pass
        else:
            if ioc_type == "domain":
                return ("mistyped-ip", f"IPアドレスがdomain型で保存されている: {host}")
            return None

        # 1) 形式の妥当性。TLDが実在しない値はファイル名や抽出失敗である。
        if "." not in host:
            return ("malformed", f"ドットがなくホストとして成立しない: {host}")
        if not HOSTNAME_RE.match(host):
            return ("malformed", f"ホスト名として不正な文字を含む: {host}")
        tld = host.rsplit(".", 1)[-1]
        if tld not in self.tlds and tld not in SPECIAL_USE_TLDS:
            return ("malformed", f"実在しないTLD: .{tld}")

        # 2) 出典レポート自身の参考リンク
        if self.reference_host(host):
            return ("reference-host", f"参考ホスト一覧に一致: {host}")

        # 3) 抽出途中で切れたベンダーURL（securelist.co, fireeye.co 等）
        if len(host) >= TRUNCATION_MIN:
            for known in self.hosts:
                if known != host and known.startswith(host):
                    return ("reference-truncated", f"参考ホストの途中で切れた値: {host} → {known}")

        # 4) 公開サフィックス単体
        if ioc_type == "domain" and host in self.suffixes:
            return ("public-suffix", f"公開サフィックス単体: {host}")

        return None


def audit(classifier: Classifier) -> tuple[list[dict], Counter, dict[str, Counter]]:
    findings: list[dict] = []
    verdicts: Counter = Counter()
    by_verdict_host: dict[str, Counter] = defaultdict(Counter)

    for profile_dir in sorted(PROFILES_DIR.iterdir()):
        path = profile_dir / "iocs.json"
        if not path.exists():
            continue
        for indicator in load_json(path).get("indicators") or []:
            ioc_type = indicator.get("type") or ""
            if ioc_type not in CHECKED_TYPES:
                continue
            value = indicator.get("normalized_value") or indicator.get("value") or ""
            result = classifier.classify(ioc_type, value)
            if not result:
                continue
            verdict, reason = result
            verdicts[verdict] += 1
            by_verdict_host[verdict][host_of(value)] += 1
            findings.append({
                "slug": profile_dir.name,
                "indicator_id": indicator.get("indicator_id"),
                "type": ioc_type,
                "value": value,
                "verdict": verdict,
                "reason": reason,
                "disposition": indicator.get("disposition"),
                "observation_count": indicator.get("observation_count", 0),
            })
    return findings, verdicts, by_verdict_host


def apply_removals(findings: list[dict]) -> tuple[int, int]:
    """判定された指標を iocs.json から取り除く。集計値も更新する。"""
    by_slug: dict[str, set[str]] = defaultdict(set)
    for item in findings:
        by_slug[item["slug"]].add(item["indicator_id"])

    changed_files = 0
    removed = 0
    for slug, ids in sorted(by_slug.items()):
        path = PROFILES_DIR / slug / "iocs.json"
        data = load_json(path)
        before = len(data.get("indicators") or [])
        data["indicators"] = [
            ind for ind in data.get("indicators") or []
            if ind.get("indicator_id") not in ids
        ]
        after = len(data["indicators"])
        if after == before:
            continue
        removed += before - after
        ingestion = data.get("ingestion")
        if isinstance(ingestion, dict):
            # 取込サマリの件数を実データへ合わせる
            if "indicator_count" in ingestion:
                ingestion["indicator_count"] = after
            if "observation_count" in ingestion:
                ingestion["observation_count"] = sum(
                    len(ind.get("observations") or []) for ind in data["indicators"]
                )
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        changed_files += 1
    return changed_files, removed


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--apply", action="store_true", help="検出した値を iocs.json から除去する")
    parser.add_argument("--list", metavar="VERDICT", help="指定した判定の値を一覧表示する")
    parser.add_argument("--limit", type=int, default=40, help="--list の表示件数")
    args = parser.parse_args()

    if not PROFILES_DIR.is_dir():
        print(f"profiles ディレクトリが見つかりません: {PROFILES_DIR}", file=sys.stderr)
        return 1

    classifier = Classifier()
    findings, verdicts, by_verdict_host = audit(classifier)

    print(f"検査対象の判定: {sum(verdicts.values())} 件 / {len(findings)} レコード")
    for verdict, count in verdicts.most_common():
        top = "、".join(f"{h}({c})" for h, c in by_verdict_host[verdict].most_common(5))
        print(f"  {verdict:22s} {count:5d}  上位: {top}")

    if args.list:
        print(f"\n=== {args.list} の一覧（先頭 {args.limit} 件）===")
        for item in [f for f in findings if f["verdict"] == args.list][: args.limit]:
            print(f"  [{item['slug']:22s}] {item['type']:6s} {item['value'][:90]}")
            print(f"      理由: {item['reason']}")

    REPORT_PATH.write_text(
        json.dumps(
            {
                "schema_version": "1.0.0",
                "description": "IOCとして保存されていた非指標値の監査結果。",
                "verdict_counts": dict(verdicts),
                "findings": findings,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"\n監査結果: {REPORT_PATH.relative_to(REPO_ROOT)}")

    if args.apply:
        changed, removed = apply_removals(findings)
        print(f"除去: {removed} 件 / 更新ファイル {changed} 件")
        print("生成物の再生成が必要です:")
        print("  python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest")
    else:
        print("（検出のみ。除去するには --apply を付けてください）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
