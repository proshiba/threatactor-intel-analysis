#!/usr/bin/env python3
"""Replace legacy workbook-derived aliases using explicit name columns only."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import normalized_name
from common import load_json, utc_now, write_json_atomic


WORKBOOK_VENDOR = "actor-mapping-workbook"
WORKBOOK_SOURCE_ID = "source--actor-mapping-workbook"


def migrate_aliases(
    profile: dict[str, Any],
    actor: dict[str, Any],
) -> dict[str, Any]:
    """Drop workbook-only aliases from existing profiles.

    The original workbook is intentionally not stored in this repository, so
    existing workbook-only aliases cannot be safely re-read during CI. We keep
    aliases already backed by MITRE, catalog, or actor-specific sources and
    remove only aliases whose sole provenance is the mapping workbook.
    """
    aliases = profile.get("actor", {}).get("aliases", [])
    retained = [
        item for item in aliases
        if not (isinstance(item, dict) and item.get("vendor") == WORKBOOK_VENDOR)
    ]
    removed = [
        item.get("name", "") for item in aliases
        if isinstance(item, dict) and item.get("vendor") == WORKBOOK_VENDOR
    ]

    old_names = [
        item.get("name", "") if isinstance(item, dict) else str(item)
        for item in aliases
    ]
    new_names = [
        item.get("name", "") if isinstance(item, dict) else str(item)
        for item in retained
    ]
    changed = old_names != new_names
    if changed:
        profile["actor"]["aliases"] = retained
        profile["updated_at"] = utc_now()
        note = (
            "2026-09 workbook-alias migration: workbook-only aliases were "
            "removed because the source workbook is not retained in this "
            "repository. MITRE, catalog, and actor-specific aliases were kept. "
            "Future workbook ingestion uses explicit actor-name columns only."
        )
        existing_note = profile["actor"].get("analyst_notes", "").strip()
        if note not in existing_note:
            profile["actor"]["analyst_notes"] = f"{existing_note} {note}".strip()

    return {
        "slug": actor["slug"],
        "changed": changed,
        "removed": removed,
        "added": [],
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
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
    results: list[dict[str, Any]] = []

    for actor in catalog["actors"]:
        profile_path = args.profiles_root / actor["slug"] / "actor-profile.json"
        if not profile_path.exists():
            continue
        profile = load_json(profile_path)
        result = migrate_aliases(profile, actor)
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
