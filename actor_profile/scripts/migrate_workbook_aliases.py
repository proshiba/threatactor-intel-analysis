#!/usr/bin/env python3
"""Replace legacy workbook-derived aliases using explicit name columns only."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import (
    actor_name_cells,
    find_workbook_record,
    load_workbook_rows,
    normalized_name,
)
from common import load_json, utc_now, write_json_atomic


WORKBOOK_VENDOR = "actor-mapping-workbook"
WORKBOOK_SOURCE_ID = "source--actor-mapping-workbook"


def migrate_aliases(
    profile: dict[str, Any],
    actor: dict[str, Any],
    workbook_record: dict[str, Any] | None,
) -> dict[str, Any]:
    aliases = profile.get("actor", {}).get("aliases", [])
    retained = [
        item for item in aliases
        if not (isinstance(item, dict) and item.get("vendor") == WORKBOOK_VENDOR)
    ]
    removed = [
        item.get("name", "") for item in aliases
        if isinstance(item, dict) and item.get("vendor") == WORKBOOK_VENDOR
    ]

    existing = {
        normalized_name(item.get("name", ""))
        for item in retained
        if isinstance(item, dict)
    }
    canonical = normalized_name(profile.get("actor", {}).get("canonical_name", actor["name"]))
    added: list[str] = []

    if workbook_record:
        for name in actor_name_cells(workbook_record):
            key = normalized_name(name)
            if not key or key == canonical or key in existing:
                continue
            retained.append(
                {
                    "name": name,
                    "vendor": WORKBOOK_VENDOR,
                    "scope": "unknown",
                    "confidence": "medium",
                    "evidence_refs": [WORKBOOK_SOURCE_ID],
                    "analyst_notes": (
                        f"Workbook {workbook_record['sheet']} row "
                        f"{workbook_record['row']}; explicit actor-name column only. "
                        "Mapping requires review."
                    ),
                }
            )
            existing.add(key)
            added.append(name)

    old_names = [
        item.get("name", "") if isinstance(item, dict) else str(item)
        for item in aliases
    ]
    new_names = [item.get("name", "") for item in retained]
    changed = old_names != new_names or removed != added
    if changed:
        profile["actor"]["aliases"] = retained
        profile["updated_at"] = utc_now()
        note = (
            "2026-09 workbook-alias migration: aliases were rebuilt from "
            "explicit Common Name / Other Names / Alias columns only; country, "
            "origin, sponsor, descriptive prose, and other metadata are not aliases."
        )
        existing_note = profile["actor"].get("analyst_notes", "").strip()
        if note not in existing_note:
            profile["actor"]["analyst_notes"] = f"{existing_note} {note}".strip()

    return {
        "slug": actor["slug"],
        "changed": changed,
        "removed": removed,
        "added": added,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
    )
    parser.add_argument(
        "--workbook", type=Path, default=Path("APT Groups and Operations.xlsx")
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("actor_profile/workbook-alias-migration-report.json"),
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    catalog = load_json(args.catalog)
    records = load_workbook_rows(args.workbook)
    results: list[dict[str, Any]] = []

    for actor in catalog["actors"]:
        profile_path = args.profiles_root / actor["slug"] / "actor-profile.json"
        if not profile_path.exists():
            continue
        profile = load_json(profile_path)
        record = find_workbook_record(actor, records)
        result = migrate_aliases(profile, actor, record)
        results.append(result)
        if args.apply and result["changed"]:
            write_json_atomic(profile_path, profile)

    summary = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "apply": args.apply,
        "actor_count": len(results),
        "changed_actor_count": sum(item["changed"] for item in results),
        "removed_alias_count": sum(len(item["removed"]) for item in results),
        "added_alias_count": sum(len(item["added"]) for item in results),
        "results": results,
    }
    write_json_atomic(args.report, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
