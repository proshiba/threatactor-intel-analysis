#!/usr/bin/env python3
"""日次のアクター更新チェック（読み取り専用）。

全673アクターを毎日見るのは現実的でないため、次の2観点に絞って
確認すべきものだけを抽出する。

  観点1: 直近に活動があったアクター（既定は過去365日）に新しい報告がないか
  観点2: tech-memo の daily-news で言及されたアクターの活動記載

このスクリプトはプロファイルを変更しない。採用可否の判断と反映は
AGENT.md の手順（validate_daily.py → apply_review_queue.py）に従うこと。

    # 既存の output/review-queue.json を使って報告だけ出す
    python3 parse-daily/daily_check.py

    # tech-memo の取得とキュー生成から通しで実行する
    python3 parse-daily/daily_check.py --run-scan
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
PROFILES_DIR = REPO_ROOT / "profiles"
STATE_PATH = BASE_DIR / "state.json"
QUEUE_PATH = BASE_DIR / "output" / "review-queue.json"
OUT_JSON = BASE_DIR / "output" / "daily-check.json"

# 自動採用してよい判定ではない。レビュー優先度の高い順に並べるためだけに使う。
CLAIM_PRIORITY = {
    "strong-subject": 0,
    "attributed-subject": 1,
    "structured-actor-field": 2,
    "scope-review-required": 3,
    "candidate": 4,
    "attribution-uncertain": 5,
    "name-collision": 6,
    "context-only": 7,
    "historical-reference": 8,
    "non-operational": 9,
    "forecast": 10,
}


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def parse_point(field) -> datetime | None:
    """{value, status, ...} 形式の時間から、判明している日時だけを返す。"""
    if not isinstance(field, dict) or field.get("status") != "known":
        return None
    value = field.get("value")
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def latest_activity(profile: dict) -> tuple[datetime | None, str]:
    """アクターの最終活動時期と、その根拠フィールドを返す。

    攻撃期間が不明でも reported_at は残っている（RULES.md 4.）ため、
    期間・報告日の両方を見て一番新しいものを採る。
    """
    best: datetime | None = None
    basis = ""
    for activity in profile.get("activities") or []:
        for key in ("last_observed", "first_observed", "reported_at"):
            point = parse_point(activity.get(key))
            if point and (best is None or point > best):
                best, basis = point, f"activity.{key}"
    seen = parse_point((profile.get("actor") or {}).get("last_seen"))
    if seen and (best is None or seen > best):
        best, basis = seen, "actor.last_seen"
    return best, basis


def collect_recent_actors(days: int) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    rows: list[dict] = []
    for profile_dir in sorted(PROFILES_DIR.iterdir()):
        path = profile_dir / "actor-profile.json"
        if path.exists():
            profile = load_json(path)
            point, basis = latest_activity(profile)
            if point and point >= cutoff:
                rows.append({
                    "slug": profile_dir.name,
                    "name": profile.get("name") or profile_dir.name,
                    "last_activity": point.date().isoformat(),
                    "basis": basis,
                    "days_since": (datetime.now(timezone.utc) - point).days,
                    "activities": len(profile.get("activities") or []),
                    "updated_at": (profile.get("updated_at") or "")[:10],
                })
    rows.sort(key=lambda row: row["last_activity"], reverse=True)
    return rows


def run_scan(since: str | None) -> list[str]:
    """tech-memo の取得とレビューキュー生成を実行する。"""
    log: list[str] = []
    for argv in (
        [sys.executable, str(BASE_DIR / "sync_daily.py")],
        [sys.executable, str(BASE_DIR / "build_review_queue.py")] + (["--since", since] if since else []),
    ):
        result = subprocess.run(argv, capture_output=True, text=True, cwd=REPO_ROOT)
        name = Path(argv[1]).name
        if result.returncode != 0:
            log.append(f"{name} が失敗しました (exit {result.returncode}): {result.stderr.strip()[:400]}")
            return log
        log.append(f"{name} 完了")
    return log


def build_report(days: int, since: str | None) -> dict:
    state = load_json(STATE_PATH) if STATE_PATH.exists() else {}
    queue = load_json(QUEUE_PATH) if QUEUE_PATH.exists() else {}
    records = queue.get("records") or []
    recent = collect_recent_actors(days)
    recent_slugs = {row["slug"]: row for row in recent}

    # 観点2: 新規ウィンドウでレビュー待ちのレコードをアクター単位へ畳む
    by_actor: dict[str, dict] = {}
    for record in records:
        if record.get("review_status") not in (None, "pending", "approved"):
            continue
        actor = record.get("actor") or {}
        slug = actor.get("slug")
        if not slug:
            continue
        activity = record.get("activity") or {}
        claim = (record.get("activity_claim") or {}).get("assessment") or "candidate"
        entry = by_actor.setdefault(slug, {
            "slug": slug,
            "name": actor.get("canonical_name") or slug,
            "in_recent_set": slug in recent_slugs,
            "last_activity": recent_slugs.get(slug, {}).get("last_activity"),
            "items": [],
        })
        entry["items"].append({
            "title": activity.get("title") or "",
            "news_date": activity.get("news_date") or "",
            "primary_url": activity.get("primary_url") or "",
            "claim": claim,
            "review_status": record.get("review_status") or "pending",
            "matched_term": actor.get("matched_term") or "",
            "scope": actor.get("scope") or "",
        })
    for entry in by_actor.values():
        entry["items"].sort(key=lambda item: (CLAIM_PRIORITY.get(item["claim"], 99), item["news_date"]))
        entry["priority"] = min(CLAIM_PRIORITY.get(item["claim"], 99) for item in entry["items"])

    mentioned = sorted(
        by_actor.values(),
        key=lambda entry: (not entry["in_recent_set"], entry["priority"], entry["name"]),
    )
    unmatched = queue.get("unmatched_actor_values") or []
    name_candidates = queue.get("unmatched_name_candidates") or []

    return {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "window": {
            "since": since or state.get("last_scanned_date"),
            "recent_days": days,
        },
        "source": {
            "last_scanned_commit": state.get("last_scanned_commit"),
            "last_scanned_date": state.get("last_scanned_date"),
            "queue_commit": (queue.get("source") or {}).get("commit"),
            "queue_generated_at": queue.get("generated_at"),
        },
        "statistics": {
            "recent_actors": len(recent),
            "mentioned_actors": len(mentioned),
            "mentioned_recent_actors": sum(1 for e in mentioned if e["in_recent_set"]),
            "records": len(records),
            "unmatched_actor_values": len(unmatched),
            "unmatched_name_candidates": len(name_candidates),
            **(queue.get("statistics") or {}),
        },
        "mentioned_actors": mentioned,
        "unmatched_actor_values": unmatched,
        "unmatched_name_candidates": name_candidates,
        "recent_actors": recent,
    }


def render_markdown(report: dict, top: int) -> str:
    stats = report["statistics"]
    window = report["window"]
    lines = [
        "# アクター更新チェック",
        "",
        f"生成: {report['generated_at']}　"
        f"対象ウィンドウ: {window['since'] or '(未設定)'} 以降　"
        f"直近活動の定義: 過去{window['recent_days']}日",
        "",
        f"- 直近に活動があったアクター: **{stats['recent_actors']}** 件",
        f"- 新規ウィンドウで言及されたアクター: **{stats['mentioned_actors']}** 件"
        f"（うち直近活動あり: {stats['mentioned_recent_actors']} 件）",
        f"- レビュー待ちレコード: **{stats.get('records', 0)}** 件",
        # unmatched_actor_values は queue 側で観測数の合計に上書きされるため、名称数と区別して表示する
        f"- 既存プロファイルに一致しないIOC actor値: **{stats['unmatched_actor_values']}** 観測"
        f"（{len(report['unmatched_actor_values'])} 名称）",
        f"- 本文から抽出した未登録のアクター名候補: "
        f"**{len(report['unmatched_name_candidates'])}** 件",
        "",
    ]

    lines += ["## 観点1・2の交差: 直近活動があり、かつ新たに言及されたアクター", ""]
    hits = [e for e in report["mentioned_actors"] if e["in_recent_set"]]
    if hits:
        lines += ["最優先で確認する対象です。", ""]
        for entry in hits:
            lines.append(f"### {entry['name']} (`{entry['slug']}`) — 既知の最終活動 {entry['last_activity']}")
            for item in entry["items"]:
                lines.append(
                    f"- [{item['claim']}] {item['news_date']} {item['title']}\n"
                    f"  - 一致語: {item['matched_term']} ({item['scope']}) / {item['primary_url']}"
                )
            lines.append("")
    else:
        lines += ["該当なし。直近活動のあるアクターについて、新しい報告はありません。", ""]

    others = [e for e in report["mentioned_actors"] if not e["in_recent_set"]]
    if others:
        lines += ["## 新たに言及されたその他のアクター（直近活動の記録なし）", ""]
        for entry in others[:top]:
            top_item = entry["items"][0]
            lines.append(
                f"- **{entry['name']}** (`{entry['slug']}`) "
                f"[{top_item['claim']}] {top_item['news_date']} {top_item['title']}"
            )
        if len(others) > top:
            lines.append(f"- ほか {len(others) - top} 件")
        lines.append("")

    if report["unmatched_actor_values"]:
        lines += ["## 既存プロファイルに一致しない名前（IOC CSVのactor列）", "",
                  "新規プロファイル作成の検討対象です（自動では作成しません）。", ""]
        for value in report["unmatched_actor_values"][:top]:
            if isinstance(value, dict):
                lines.append(f"- {value.get('value')}（観測 {value.get('observations', '?')} 件）")
            else:
                lines.append(f"- {value}")
        lines.append("")

    if report["unmatched_name_candidates"]:
        lines += ["## 本文から抽出した未登録のアクター名候補", "",
                  "IOCを伴わない記事はIOC CSVのactor列に現れないため、本文の実行主体表現からも"
                  "名前を抽出しています。発見用途であり、被害組織名・製品名・ベンダー名を含みます。"
                  "原文を確認したうえで、`parse-daily/unknown-clusters.json` との照合と"
                  "新規プロファイル作成の要否を判断してください（自動承認しません）。", ""]
        for candidate in report["unmatched_name_candidates"][:top]:
            sources = candidate.get("sources") or []
            lines.append(f"- **{candidate.get('value')}**（記事 {candidate.get('articles', '?')} 件）")
            for source in sources[:2]:
                lines.append(
                    f"  - {source.get('news_date')} {source.get('title')} / {source.get('primary_url')}"
                )
        if len(report["unmatched_name_candidates"]) > top:
            lines.append(f"- ほか {len(report['unmatched_name_candidates']) - top} 件")
        lines.append("")

    lines += [f"## 直近{window['recent_days']}日に活動があったアクター（上位{top}件）", "",
              "| アクター | 最終活動 | 経過日数 | 根拠 | プロファイル更新 |",
              "|---|---|---:|---|---|"]
    for row in report["recent_actors"][:top]:
        lines.append(
            f"| {row['name']} (`{row['slug']}`) | {row['last_activity']} | {row['days_since']} | "
            f"{row['basis']} | {row['updated_at'] or '不明'} |"
        )
    if len(report["recent_actors"]) > top:
        lines.append(f"| ほか {len(report['recent_actors']) - top} 件 | | | | |")
    lines.append("")
    lines += ["---", "",
              "採用可否の判断と反映は `parse-daily/AGENT.md` の手順に従ってください。",
              "このチェックはプロファイルを変更しません。"]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--days", type=int, default=365, help="直近活動とみなす日数（既定365）")
    parser.add_argument("--since", help="走査開始日。既定は state.json の last_scanned_date")
    parser.add_argument("--run-scan", action="store_true", help="sync_daily.py と build_review_queue.py を先に実行する")
    parser.add_argument("--top", type=int, default=20, help="一覧の表示件数（既定20）")
    parser.add_argument("--json", action="store_true", help="Markdownの代わりにJSONを標準出力へ出す")
    args = parser.parse_args()

    if not PROFILES_DIR.is_dir():
        print(f"profiles ディレクトリが見つかりません: {PROFILES_DIR}", file=sys.stderr)
        return 1

    since = args.since
    if since is None and STATE_PATH.exists():
        since = load_json(STATE_PATH).get("last_scanned_date")

    scan_log: list[str] = []
    if args.run_scan:
        scan_log = run_scan(since)
        if any("失敗" in line for line in scan_log):
            for line in scan_log:
                print(line, file=sys.stderr)
            return 1

    report = build_report(args.days, since)
    report["scan_log"] = scan_log

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(report, args.top))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
