#!/usr/bin/env python3
"""Prioritize remaining actor OSINT work using corpus exposure and claim gaps."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from bootstrap_all_profiles import normalized_name
from common import load_json, utc_now, write_json_atomic


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
    )
    parser.add_argument(
        "--census", type=Path, default=Path("actor_profile/actor-census.json")
    )
    parser.add_argument(
        "--claims", type=Path, default=Path("profiles/claim-audit-summary.json")
    )
    parser.add_argument(
        "--tracker", type=Path, default=Path("profiles/osint-progress.json")
    )
    parser.add_argument(
        "--output", type=Path, default=Path("profiles/osint-research-queue.json")
    )
    parser.add_argument(
        "--csv-output", type=Path, default=Path("profiles/osint-research-queue.csv")
    )
    args = parser.parse_args()
    catalog = load_json(args.catalog)
    census = load_json(args.census)
    claims = {item["slug"]: item for item in load_json(args.claims)["actors"]}
    tracker = {item["slug"]: item for item in load_json(args.tracker)["actors"]}
    mentions: dict[str, tuple[int, int]] = {}
    census_by_id = {item["actor_id"]: item for item in census["actors"]}
    for actor in census["actors"]:
        for slug in actor.get("catalog_slugs", []):
            old = mentions.get(slug, (0, 0))
            mentions[slug] = (
                max(old[0], actor.get("mention_source_count", 0)),
                max(old[1], actor.get("mention_count", 0)),
            )
    rows = []
    for actor in catalog["actors"]:
        slug = actor["slug"]
        for actor_id in actor.get("census_actor_ids", []):
            census_actor = census_by_id.get(actor_id, {})
            old = mentions.get(slug, (0, 0))
            mentions[slug] = (
                max(old[0], census_actor.get("mention_source_count", 0)),
                max(old[1], census_actor.get("mention_count", 0)),
            )
        progress = tracker[slug]
        if progress["status"] in {"integrated", "source_verified"}:
            continue
        source_count, mention_count = mentions.get(slug, (0, 0))
        audit = claims[slug]["counts"]
        unresolved = audit.get("unresolved", 0)
        partial = audit.get("partially-supported", 0)
        score = source_count * 10 + mention_count + unresolved * 8 + partial * 2
        priority = "high" if score >= 300 else "medium" if score >= 60 else "low"
        rows.append(
            {
                "slug": slug,
                "name": actor["name"],
                "priority": priority,
                "priority_score": score,
                "tracker_status": progress["status"],
                "corpus_source_count": source_count,
                "corpus_mention_count": mention_count,
                "unresolved_claim_count": unresolved,
                "partially_supported_claim_count": partial,
                "mitre_group_id": actor.get("mitre_group_id", ""),
                "recommended_queries": [
                    f'"{actor["name"]}" threat actor official advisory',
                    f'"{actor["name"]}" attribution relationship malware',
                    f'"{actor["name"]}" contradiction disputed attribution',
                ],
            }
        )
    rows.sort(key=lambda item: (-item["priority_score"], item["slug"]))
    result = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "research_complete_actor_count": sum(
            item["status"] != "not_started" for item in tracker.values()
        ),
        "followup_actor_count": len(rows),
        "remaining_actor_count": len(rows),
        "priority_counts": {
            level: sum(item["priority"] == level for item in rows)
            for level in ("high", "medium", "low")
        },
        "actors": rows,
    }
    write_json_atomic(args.output.resolve(), result)
    with args.csv_output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=[
                "slug", "name", "priority", "priority_score",
                "tracker_status", "corpus_source_count", "corpus_mention_count",
                "unresolved_claim_count", "partially_supported_claim_count",
                "mitre_group_id", "recommended_queries",
            ],
        )
        writer.writeheader()
        for row in rows:
            output = dict(row)
            output["recommended_queries"] = json.dumps(
                output["recommended_queries"], ensure_ascii=False
            )
            writer.writerow(output)
    print(
        json.dumps(
            {
                "remaining": len(rows),
                "priority_counts": result["priority_counts"],
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
