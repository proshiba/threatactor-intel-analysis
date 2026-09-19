#!/usr/bin/env python3
"""Migrate legacy geography-derived attribution without rebuilding profiles.

This migration only removes or re-scopes fields that can be identified as
outputs of the historical bootstrap rules. It preserves daily observations,
manual enrichments, IOC data, activities, TTPs, targets, and other analyst work.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import (
    derive_actor_types,
    derive_motivations,
)
from common import load_json, utc_now, write_json_atomic


WORKBOOK_SOURCE_ID = "source--actor-mapping-workbook"
MITRE_SOURCE_ID = "source--mitre-attack-19-1"
GENERATED_ESPIONAGE_DESCRIPTION = (
    "State-sponsored intelligence collection or strategic operations."
)
GENERATED_ATTRIBUTION_PREFIX = (
    "The repository mapping workbook places this actor in the "
)


def is_generated_state_attribution(attribution: dict[str, Any]) -> bool:
    return (
        attribution.get("sponsor_type") == "state"
        and attribution.get("confidence") == "medium"
        and attribution.get("evidence_refs") == [WORKBOOK_SOURCE_ID]
        and attribution.get("assessment", "").startswith(GENERATED_ATTRIBUTION_PREFIX)
    )


def is_generated_espionage_motivation(item: dict[str, Any]) -> bool:
    return (
        item.get("type") == "espionage"
        and item.get("description") == GENERATED_ESPIONAGE_DESCRIPTION
        and item.get("evidence_refs") == [WORKBOOK_SOURCE_ID]
    )


def rescope_aliases(
    aliases: list[dict[str, Any]], mitre_group: dict[str, Any] | None
) -> tuple[list[dict[str, Any]], int]:
    """Repair aliases that inherited MITRE evidence merely because a group existed."""
    mitre_aliases = set((mitre_group or {}).get("aliases", []))
    changed = 0
    output: list[dict[str, Any]] = []
    for item in aliases:
        alias = dict(item)
        name = alias.get("name", "")
        if name in mitre_aliases:
            desired = {
                "vendor": "MITRE ATT&CK",
                "confidence": "high",
                "evidence_refs": [MITRE_SOURCE_ID],
            }
        elif alias.get("vendor") == "catalog":
            desired = {
                "vendor": "catalog",
                "confidence": "medium",
                "evidence_refs": [WORKBOOK_SOURCE_ID],
            }
        else:
            output.append(alias)
            continue
        if any(alias.get(key) != value for key, value in desired.items()):
            alias.update(desired)
            changed += 1
        output.append(alias)
    return output, changed


def migrate_profile(
    profile: dict[str, Any],
    catalog_actor: dict[str, Any],
    mitre_group: dict[str, Any] | None,
) -> dict[str, Any]:
    """Apply the narrow migration and return a change report."""
    report = {
        "slug": catalog_actor["slug"],
        "changed": False,
        "actor_types_changed": False,
        "state_attribution_removed": False,
        "state_attribution_rescoped": False,
        "generated_espionage_removed": False,
        "derived_motivations_added": 0,
        "aliases_rescoped": 0,
    }

    desired_types = derive_actor_types(catalog_actor, mitre_group)
    if profile["actor"].get("actor_types", []) != desired_types:
        profile["actor"]["actor_types"] = desired_types
        report["actor_types_changed"] = True
        report["changed"] = True

    aliases, alias_changes = rescope_aliases(
        profile["actor"].get("aliases", []), mitre_group
    )
    if alias_changes:
        profile["actor"]["aliases"] = aliases
        report["aliases_rescoped"] = alias_changes
        report["changed"] = True

    attribution = profile.get("attribution", {})
    old_countries = list(attribution.get("countries", []))
    if is_generated_state_attribution(attribution):
        if "state-sponsored" in desired_types:
            attribution.update(
                {
                    "sponsor_type": "state",
                    "assessment": (
                        "Actor-specific MITRE ATT&CK reporting supports state "
                        "sponsorship; the community workbook country placement "
                        "is retained only as a geographic lead."
                    ),
                    "confidence": "medium",
                    "evidence_refs": [MITRE_SOURCE_ID, WORKBOOK_SOURCE_ID],
                    "analyst_notes": (
                        "Migrated from a legacy rule that treated workbook "
                        "geography as sponsorship. State sponsorship is now "
                        "anchored to actor-specific MITRE text."
                    ),
                }
            )
            report["state_attribution_rescoped"] = True
        else:
            profile["attribution"] = {
                "countries": [],
                "sponsor_type": "unknown",
                "organizations": attribution.get("organizations", []),
                "assessment": "",
                "confidence": "unknown",
                "evidence_refs": [],
                "analyst_notes": (
                    "Removed legacy state attribution generated solely from "
                    "community-workbook geography. Country/origin is not "
                    "sponsorship evidence."
                ),
            }
            if (
                profile.get("diamond_model", {}).get("socio_political")
                in old_countries
            ):
                profile["diamond_model"]["socio_political"] = ""
            report["state_attribution_removed"] = True
        report["changed"] = True

    motivations = profile.get("motivations", [])
    retained = [
        item for item in motivations if not is_generated_espionage_motivation(item)
    ]
    if len(retained) != len(motivations):
        report["generated_espionage_removed"] = True
        report["changed"] = True

    derived = derive_motivations(
        desired_types,
        mitre_group,
        MITRE_SOURCE_ID,
        WORKBOOK_SOURCE_ID,
    )
    existing_types = {item.get("type") for item in retained}
    for item in derived:
        if item.get("type") not in existing_types:
            retained.append(item)
            existing_types.add(item.get("type"))
            report["derived_motivations_added"] += 1
            report["changed"] = True
    profile["motivations"] = retained

    if report["changed"]:
        profile["updated_at"] = utc_now()
        note = (
            "2026-09 migration: removed or re-scoped legacy geography-derived "
            "state sponsorship, generated espionage motivation, and alias "
            "evidence that was not source-specific."
        )
        existing = profile["actor"].get("analyst_notes", "").strip()
        if note not in existing:
            profile["actor"]["analyst_notes"] = f"{existing} {note}".strip()

    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog",
        type=Path,
        default=Path("actor_profile/corpus-catalog.json"),
    )
    parser.add_argument(
        "--attack",
        type=Path,
        default=Path("actor_profile/reference/attack-index.json"),
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("actor_profile/generated-attribution-migration-report.json"),
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    catalog = load_json(args.catalog)
    attack = load_json(args.attack)
    results: list[dict[str, Any]] = []

    for actor in catalog["actors"]:
        profile_path = args.profiles_root / actor["slug"] / "actor-profile.json"
        if not profile_path.exists():
            continue
        profile = load_json(profile_path)
        mitre_group = attack["groups"].get(actor.get("mitre_group_id", ""))
        result = migrate_profile(profile, actor, mitre_group)
        results.append(result)
        if args.apply and result["changed"]:
            write_json_atomic(profile_path, profile)

    summary = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "apply": args.apply,
        "actor_count": len(results),
        "changed_actor_count": sum(item["changed"] for item in results),
        "actor_types_changed": sum(item["actor_types_changed"] for item in results),
        "state_attribution_removed": sum(
            item["state_attribution_removed"] for item in results
        ),
        "state_attribution_rescoped": sum(
            item["state_attribution_rescoped"] for item in results
        ),
        "generated_espionage_removed": sum(
            item["generated_espionage_removed"] for item in results
        ),
        "aliases_rescoped": sum(item["aliases_rescoped"] for item in results),
        "derived_motivations_added": sum(
            item["derived_motivations_added"] for item in results
        ),
        "results": results,
    }
    write_json_atomic(args.report, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
