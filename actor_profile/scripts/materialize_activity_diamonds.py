#!/usr/bin/env python3
"""Materialize a Diamond Model for every activity in every actor profile."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from activity_diamond import SCHEMA_VERSION, materialize_profile_diamonds
from common import load_json, write_json_atomic


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profiles_root", nargs="?", type=Path, default=Path("profiles"))
    parser.add_argument("--actor", action="append", default=[])
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    selected = set(args.actor)
    scanned = changed_profiles = changed_activities = activity_count = 0
    for path in sorted(args.profiles_root.glob("*/actor-profile.json")):
        if selected and path.parent.name not in selected:
            continue
        profile = load_json(path)
        before_version = profile.get("schema_version")
        changed = materialize_profile_diamonds(profile)
        activities = len(profile.get("activities", []))
        version_changed = before_version != SCHEMA_VERSION
        scanned += 1
        activity_count += activities
        changed_activities += changed
        if changed or version_changed:
            changed_profiles += 1
            if args.apply:
                write_json_atomic(path, profile)

    print(
        json.dumps(
            {
                "mode": "apply" if args.apply else "dry-run",
                "schema_version": SCHEMA_VERSION,
                "profiles_scanned": scanned,
                "profiles_changed": changed_profiles,
                "activities_scanned": activity_count,
                "activity_diamonds_changed": changed_activities,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
