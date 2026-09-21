#!/usr/bin/env python3
"""Migrate canonical profiles to explicit Campaign/Incident/Grouping modeling."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from activity_diamond import SCHEMA_VERSION
from common import load_json, write_json_atomic
from stix_modeling import apply_activity_modeling_defaults


DEFAULT_CURATION = Path("actor_profile/activity-stix-model-curation.json")


def migrate(
    profile: dict[str, object],
    decisions: dict[tuple[str, str], dict[str, str]] | None = None,
) -> tuple[dict[str, object], bool]:
    changed = False
    if profile.get("schema_version") != SCHEMA_VERSION:
        profile["schema_version"] = SCHEMA_VERSION
        changed = True
    for activity in profile.get("activities", []):
        changed = apply_activity_modeling_defaults(activity) or changed
        decision = (decisions or {}).get(
            (str(profile.get("profile_id", "")), activity.get("activity_id", ""))
        )
        if decision and activity.get("stix_object_type") != decision["stix_object_type"]:
            activity["stix_object_type"] = decision["stix_object_type"]
            activity["grouping_context"] = (
                "suspicious-activity"
                if decision["stix_object_type"] == "grouping"
                else None
            )
            changed = True
    return profile, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "profiles_root", nargs="?", type=Path, default=Path("profiles")
    )
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--curation", type=Path, default=DEFAULT_CURATION)
    args = parser.parse_args()

    curation = load_json(args.curation)
    decisions = {
        (item["profile_id"], item["activity_id"]): item
        for item in curation.get("decisions", [])
    }
    if len(decisions) != len(curation.get("decisions", [])):
        raise ValueError("duplicate profile/activity decision in STIX curation")
    invalid = sorted(
        key
        for key, item in decisions.items()
        if item.get("stix_object_type") not in {"campaign", "incident", "grouping"}
    )
    if invalid:
        raise ValueError(f"invalid curated STIX object types: {invalid[:5]}")

    scanned = changed_count = 0
    distribution: Counter[str] = Counter()
    observed_activity_keys: set[tuple[str, str]] = set()
    for path in sorted(args.profiles_root.glob("*/actor-profile.json")):
        profile = load_json(path)
        profile, changed = migrate(profile, decisions)
        scanned += 1
        distribution.update(
            item["stix_object_type"] for item in profile.get("activities", [])
        )
        observed_activity_keys.update(
            (profile["profile_id"], item["activity_id"])
            for item in profile.get("activities", [])
        )
        if changed:
            changed_count += 1
            if args.apply:
                write_json_atomic(path, profile)
    missing_decisions = sorted(set(decisions) - observed_activity_keys)
    if missing_decisions:
        raise ValueError(
            "curated STIX modeling decisions do not resolve: "
            f"{missing_decisions[:5]}"
        )
    print(
        json.dumps(
            {
                "mode": "apply" if args.apply else "dry-run",
                "profiles_scanned": scanned,
                "profiles_changed": changed_count,
                "schema_version": SCHEMA_VERSION,
                "activity_stix_types": dict(sorted(distribution.items())),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
