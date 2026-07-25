#!/usr/bin/env python3
"""Render a collection-level index for all generated actor profiles."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import load_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("summary", type=Path)
    parser.add_argument("catalog", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    summary = load_json(args.summary)
    catalog = load_json(args.catalog)
    profiles_root = args.summary.resolve().parent
    rows = []
    totals = {
        "sources": 0,
        "iocs": 0,
        "observations": 0,
        "artifacts": 0,
        "aliases": 0,
        "software": 0,
        "ttps": 0,
        "errors": 0,
        "warnings": 0,
    }
    for result in summary["results"]:
        slug = result["slug"]
        profile = load_json(profiles_root / slug / "actor-profile.json")
        ingest = result["steps"]["ingest"]["summary"]
        validation = result["steps"]["validate"]["summary"]["counts"]
        aliases = len(profile["actor"]["aliases"])
        software = len(profile["capabilities"]["malware"]) + len(
            profile["capabilities"]["tools"]
        )
        ttps = len(profile["ttps"])
        values = {
            "sources": int(ingest.get("processed", 0) or 0),
            "iocs": int(ingest.get("indicators", 0) or 0),
            "observations": int(ingest.get("indicator_observations", 0) or 0),
            "artifacts": int(ingest.get("artifacts", 0) or 0),
            "aliases": aliases,
            "software": software,
            "ttps": ttps,
            "errors": int(validation.get("error", 0) or 0),
            "warnings": int(validation.get("warning", 0) or 0),
        }
        for key, value in values.items():
            totals[key] += value
        rows.append((result, values))

    lines = [
        "# Threat Actor Profile Collection",
        "",
        f"Generated: {summary['generated_at']}",
        "",
        "同一スキーマで作成したアクター／脅威クラスターの一覧です。"
        "各ディレクトリの`actor-profile.json`が正規データで、MarkdownとSTIXは生成物です。",
        "",
        "## 集計",
        "",
        f"- プロファイル: {len(rows)}",
        f"- 処理資料: {totals['sources']}",
        f"- IOC: {totals['iocs']}（観測イベント: {totals['observations']}）",
        f"- 非IOC artifact観測: {totals['artifacts']}",
        f"- Alias: {totals['aliases']}",
        f"- マルウェア／ツール: {totals['software']}",
        f"- TTP: {totals['ttps']}",
        f"- 検証エラー: {totals['errors']}",
        "",
        "警告は主に、資料に観測日がない、または自動抽出値がcandidateであることを示します。"
        "不明値を推測で埋めず、レビュー対象として保持しています。",
        "",
        "## プロファイル一覧",
        "",
        "| Actor | Sources | Alias | Software | TTP | IOC | IOC observations | Artifacts | Errors | Warnings |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for result, values in rows:
        slug = result["slug"]
        actor_link = f"[{result['name']}]({slug}/generated/profile-ja.md)"
        lines.append(
            f"| {actor_link} | {values['sources']} | {values['aliases']} | "
            f"{values['software']} | {values['ttps']} | {values['iocs']} | "
            f"{values['observations']} | {values['artifacts']} | "
            f"{values['errors']} | {values['warnings']} |"
        )

    lines.extend(
        [
            "",
            "## アクターとして扱わない資料群",
            "",
            "横断資料やツール／脆弱性コレクションを誤ってアクター化しないため、"
            "次のルートはカタログ上で除外しています。",
            "",
            "| Path | Reason |",
            "|---|---|",
        ]
    )
    for item in catalog["excluded_roots"]:
        lines.append(f"| `{item['path']}` | {item['reason']} |")
    lines.append("")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
