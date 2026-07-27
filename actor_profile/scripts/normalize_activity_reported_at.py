#!/usr/bin/env python3
"""Ensure every activity has a separate report-publication time point."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from common import load_json, write_json_atomic


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
UNKNOWN_TIME = {
    "value": None,
    "precision": "unknown",
    "status": "unknown",
    "basis": "not-stated",
}


def reported_at_for(
    activity: dict[str, Any],
    sources: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    known = [
        source["published_at"]
        for ref in activity.get("evidence_refs", [])
        if (source := sources.get(ref))
        and source.get("published_at", {}).get("value")
    ]
    if not known:
        return dict(UNKNOWN_TIME)
    earliest = min(known, key=lambda item: item["value"])
    return {
        **earliest,
        "basis": "earliest-evidence-source-published-at",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profiles-root",
        type=Path,
        default=REPO_ROOT / "profiles",
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    changed_profiles = 0
    changed_activities = 0
    for path in sorted(args.profiles_root.glob("*/actor-profile.json")):
        profile = load_json(path)
        sources = {
            item["source_id"]: item
            for item in profile.get("sources", [])
        }
        changed = False
        for activity in profile.get("activities", []):
            if "reported_at" in activity:
                continue
            activity["reported_at"] = reported_at_for(activity, sources)
            changed = True
            changed_activities += 1
        if changed:
            changed_profiles += 1
            if args.apply:
                write_json_atomic(path, profile)
    print(
        json.dumps(
            {
                "mode": "apply" if args.apply else "dry-run",
                "changed_profiles": changed_profiles,
                "changed_activities": changed_activities,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
