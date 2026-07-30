#!/usr/bin/env python3
"""ハッシュとして保存された「ハッシュでない16進列」を検出し、必要なら除去する。

``ingest_observables.py`` は資料本文から16進の連なりを拾う。マルウェア解析の資料には
逆アセンブル結果・PEヘッダのダンプ・シェルコード・スクリプトの16進表現が普通に載る
ため、これらがちょうど32/40/64/128桁で切り出されるとファイルハッシュとして
取り込まれてしまう。値そのものが指標でないため、``disposition`` が ``confirmed``
でも除去してよい。

判定は ``ingest_observables.looks_like_hash()` をそのまま使う。取込側と監査側で
規則が食い違わないよう、実装は一箇所に置く。

資料本体(``sources/``)はこのリポジトリに含まれないため再取り込みができない。
既存データの掃除はこのスクリプトで行う。

    # 検出のみ（既定）。レポートを出力して終了する
    python3 actor_profile/scripts/audit_hash_iocs.py

    # 復号結果を含めて一覧表示する
    python3 actor_profile/scripts/audit_hash_iocs.py --list

    # profiles/<slug>/iocs.json から除去する
    python3 actor_profile/scripts/audit_hash_iocs.py --apply

除去後は生成物と索引の再生成が必要である。
    python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest
    python3 ui/build_data.py && python3 ui/build_portal_index.py
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ingest_observables import NON_HASH_WORD_RE, looks_like_hash  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
PROFILES_DIR = REPO_ROOT / "profiles"
REPORT_PATH = REPO_ROOT / "actor_profile" / "reference" / "hash-ioc-audit.json"

HASH_TYPES = {"md5", "sha1", "sha256", "sha512"}
HEX_RE = re.compile(r"[0-9a-f]+")


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def reject_reason(compact: str) -> str | None:
    """``looks_like_hash()`` が偽になる理由を人間向けに言い直す。

    判定そのものは ``looks_like_hash()`` が持つ。ここは同じ順序で条件をたどり、
    レポートに載せる理由を組み立てるだけである。
    """
    raw = bytes.fromhex(compact)
    zeros = raw.count(0) / len(raw)
    if zeros >= 0.20:
        return f"ゼロバイト {round(zeros * 100)}%"
    run = longest = 1
    for prev, cur in zip(raw, raw[1:]):
        run = run + 1 if cur == prev else 1
        longest = max(longest, run)
    if longest >= 4:
        return f"同一バイト {longest} 連"
    grams = Counter(bytes(raw[index : index + 3]) for index in range(len(raw) - 2))
    gram, count = grams.most_common(1)[0]
    if count >= 3:
        return f"3バイトの並び {gram.hex()} が {count} 回"
    match = NON_HASH_WORD_RE.search(raw)
    if match:
        return f"可読 {match.group(0)!r}"
    return None


def decoded(compact: str) -> str:
    """16進を復号して、印字できないバイトをドットに置き換えた表示を返す。"""
    return "".join(
        chr(byte) if 32 <= byte < 127 else "." for byte in bytes.fromhex(compact)
    )


def audit() -> tuple[list[dict], int]:
    findings: list[dict] = []
    checked = 0

    for profile_dir in sorted(PROFILES_DIR.iterdir()):
        path = profile_dir / "iocs.json"
        if not path.exists():
            continue
        for indicator in load_json(path).get("indicators") or []:
            if (indicator.get("type") or "") not in HASH_TYPES:
                continue
            value = (
                indicator.get("normalized_value") or indicator.get("value") or ""
            ).lower()
            # 16進でない値は型の付け間違いであり、この監査の対象ではない。
            if not HEX_RE.fullmatch(value):
                continue
            checked += 1
            if looks_like_hash(value):
                continue
            findings.append({
                "slug": profile_dir.name,
                "indicator_id": indicator.get("indicator_id"),
                "type": indicator.get("type"),
                "value": value,
                "decoded": decoded(value),
                "reason": reject_reason(value) or "",
                "disposition": indicator.get("disposition"),
                "observation_count": indicator.get("observation_count", 0),
            })
    return findings, checked


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
    parser.add_argument("--list", action="store_true", help="値と復号結果を一覧表示する")
    parser.add_argument("--markdown", action="store_true", help="一覧をMarkdownの表で出す")
    args = parser.parse_args()

    if not PROFILES_DIR.is_dir():
        print(f"profiles ディレクトリが見つかりません: {PROFILES_DIR}", file=sys.stderr)
        return 1

    findings, checked = audit()
    print(f"全 {checked} 件 / 疑わしい {len(findings)} 件")
    print("型:", dict(Counter(item["type"] for item in findings)))
    print("disposition:", dict(Counter(item["disposition"] for item in findings)))
    print("プロファイル:", sorted({item["slug"] for item in findings}))

    if args.markdown:
        print("\n| プロファイル | 型 | disposition | 値 | 復号 | 却下理由 |")
        print("| --- | --- | --- | --- | --- | --- |")
        for item in findings:
            print(
                f"| {item['slug']} | {item['type']} | {item['disposition']} | "
                f"`{item['value']}` | `{item['decoded']}` | {item['reason']} |"
            )
    elif args.list:
        print()
        for item in findings:
            print(f"  [{item['slug']:16s}] {item['type']:6s} {item['disposition']:9s} {item['value']}")
            print(f"      復号: {item['decoded']}")
            print(f"      理由: {item['reason']}")

    REPORT_PATH.write_text(
        json.dumps(
            {
                "schema_version": "1.0.0",
                "description": "ハッシュとして保存されていた非ハッシュ16進列の監査結果。",
                "checked": checked,
                "type_counts": dict(Counter(item["type"] for item in findings)),
                "disposition_counts": dict(
                    Counter(item["disposition"] for item in findings)
                ),
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
        print("生成物と索引の再生成が必要です:")
        print("  python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest")
        print("  python3 ui/build_data.py && python3 ui/build_portal_index.py")
    else:
        print("（検出のみ。除去するには --apply を付けてください）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
