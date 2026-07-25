#!/usr/bin/env python3
"""Update one actor in the OSINT progress tracker."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import load_json, utc_now, write_json_atomic


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tracker", type=Path)
    parser.add_argument("--slug", required=True)
    parser.add_argument(
        "--status",
        required=True,
        choices=[
            "not_started", "searched", "source_verified", "integrated",
            "needs_review",
        ],
    )
    parser.add_argument("--query", action="append", default=[])
    parser.add_argument(
        "--source-json",
        action="append",
        default=[],
        help="verified source as a JSON object",
    )
    parser.add_argument("--note")
    args = parser.parse_args()

    tracker = load_json(args.tracker)
    actor = next(
        (item for item in tracker["actors"] if item["slug"] == args.slug),
        None,
    )
    if actor is None:
        raise ValueError(f"unknown actor slug: {args.slug}")
    actor["status"] = args.status
    actor["queries"] = list(dict.fromkeys([*actor["queries"], *args.query]))
    known_urls = {item["url"] for item in actor["verified_sources"]}
    for raw in args.source_json:
        source = json.loads(raw)
        if source["url"] not in known_urls:
            actor["verified_sources"].append(source)
            known_urls.add(source["url"])
    actor["last_searched_at"] = utc_now()
    if args.note is not None:
        actor["analyst_notes"] = args.note
    tracker["updated_at"] = utc_now()
    write_json_atomic(args.tracker, tracker)
    print(
        json.dumps(
            {
                "slug": actor["slug"],
                "status": actor["status"],
                "verified_sources": len(actor["verified_sources"]),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
