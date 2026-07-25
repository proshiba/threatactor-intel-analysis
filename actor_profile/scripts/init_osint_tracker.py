#!/usr/bin/env python3
"""Create or refresh the per-actor OSINT research progress tracker."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import load_json, utc_now, write_json_atomic


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    catalog = load_json(args.catalog)
    previous = load_json(args.output) if args.output.exists() else {}
    previous_by_slug = {
        item["slug"]: item for item in previous.get("actors", [])
    }
    actors = []
    for actor in catalog["actors"]:
        item = previous_by_slug.get(actor["slug"], {})
        actors.append(
            {
                "slug": actor["slug"],
                "name": actor["name"],
                "status": item.get("status", "not_started"),
                "queries": item.get("queries", []),
                "verified_sources": item.get("verified_sources", []),
                "rejected_sources": item.get("rejected_sources", []),
                "claims_integrated": item.get("claims_integrated", []),
                "last_searched_at": item.get("last_searched_at"),
                "analyst_notes": item.get("analyst_notes", ""),
            }
        )
    result = {
        "schema_version": "1.0.0",
        "updated_at": utc_now(),
        "status_values": [
            "not_started",
            "searched",
            "source_verified",
            "integrated",
            "needs_review",
        ],
        "actors": actors,
    }
    write_json_atomic(args.output, result)
    print(f"actors={len(actors)} output={args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
