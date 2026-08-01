#!/usr/bin/env python3
"""Migrate actor profiles to the activity-linked victim/TTP model."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from common import load_json, unknown_time, write_json_atomic
from activity_diamond import SCHEMA_VERSION, materialize_profile_diamonds


PUBLICATION_BASIS = re.compile(
    r"(?:publication|published|report(?:ed)?[-_ ]?date|daily-news-file-date)",
    re.IGNORECASE,
)
OBSERVATION_AUDIT_NOTE = "[observation-time-audit-v1]"


def clear_publication_observation_dates(value: Any) -> bool:
    """Remove publication-only dates from semantic observation fields.

    The original value and basis remain in the containing object's analyst
    note. The report date itself belongs in ``reported_at`` or source metadata.
    """
    changed = False
    if isinstance(value, dict):
        notes: list[str] = []
        for field in ("first_observed", "last_observed"):
            point = value.get(field)
            if not isinstance(point, dict) or not point.get("value"):
                continue
            basis = str(point.get("basis", ""))
            if not PUBLICATION_BASIS.search(basis):
                continue
            notes.append(
                f"{field}={point['value']} (basis={basis or 'not-stated'})"
            )
            value[field] = unknown_time()
            changed = True
        if notes:
            marker = (
                f"{OBSERVATION_AUDIT_NOTE} 資料公開日のみを根拠とする観測日時を"
                f"unknownへ戻した: {'; '.join(notes)}。公開日はreported_atまたは"
                "source metadataで保持する。"
            )
            current = value.get("analyst_notes")
            if isinstance(current, str) and marker not in current:
                value["analyst_notes"] = f"{current.rstrip()} {marker}".strip()
            elif current is None:
                value["analyst_notes"] = marker
        for child in value.values():
            changed = clear_publication_observation_dates(child) or changed
    elif isinstance(value, list):
        for child in value:
            changed = clear_publication_observation_dates(child) or changed
    return changed


def migrate(profile: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    changed = False
    if profile.get("schema_version") != SCHEMA_VERSION:
        profile["schema_version"] = SCHEMA_VERSION
        changed = True
    if "victim_cases" not in profile:
        # Keep targets and victim cases separate. Empty is better than manufacturing
        # a victim from broad actor-level targeting prose.
        profile["victim_cases"] = []
        changed = True

    activities = profile.get("activities", [])
    activity_by_id = {
        item.get("activity_id"): item
        for item in activities
        if item.get("activity_id")
    }
    for activity in activities:
        for field in ("ttp_refs", "victim_refs"):
            if field not in activity:
                activity[field] = []
                changed = True

    for ttp in profile.get("ttps", []):
        ttp_id = ttp.get("ttp_id")
        if not ttp_id:
            continue
        for activity_ref in ttp.get("activity_refs", []):
            activity = activity_by_id.get(activity_ref)
            if activity is None:
                continue
            if ttp_id not in activity["ttp_refs"]:
                activity["ttp_refs"].append(ttp_id)
                activity["ttp_refs"].sort()
                changed = True

    for victim in profile.get("victim_cases", []):
        if "case_status" not in victim:
            victim["case_status"] = "unknown"
            changed = True
        victim_id = victim.get("victim_case_id")
        if not victim_id:
            continue
        for activity_ref in victim.get("activity_refs", []):
            activity = activity_by_id.get(activity_ref)
            if activity is None:
                continue
            if victim_id not in activity["victim_refs"]:
                activity["victim_refs"].append(victim_id)
                activity["victim_refs"].sort()
                changed = True
    changed = clear_publication_observation_dates(profile) or changed
    changed = bool(materialize_profile_diamonds(profile)) or changed
    return profile, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "profiles_root",
        nargs="?",
        type=Path,
        default=Path("profiles"),
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    scanned = changed_count = 0
    for path in sorted(args.profiles_root.glob("*/actor-profile.json")):
        profile = load_json(path)
        profile, changed = migrate(profile)
        scanned += 1
        if changed:
            changed_count += 1
            if args.apply:
                write_json_atomic(path, profile)
    print(
        json.dumps(
            {
                "mode": "apply" if args.apply else "dry-run",
                "profiles_scanned": scanned,
                "profiles_changed": changed_count,
                "schema_version": SCHEMA_VERSION,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
