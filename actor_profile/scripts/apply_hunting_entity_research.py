#!/usr/bin/env python3
"""Apply reviewed entity relationships and hunting pivots to actor profiles.

The JSON research file is a reproducible input.  It contains only claims that
have an explicit source record; this script does not infer relationships from
names, employment, geography, certificate ownership, or shared infrastructure.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from common import load_json, write_json_atomic


SCHEMA_VERSION = "1.4.0"
UPDATED_AT = "2026-09-21T13:20:00Z"
COLLECTION_FIELDS = (
    "associated_entities",
    "entity_relationships",
    "hunting_pivots",
)
MERGE_FIELDS = (*COLLECTION_FIELDS, "sources")
ID_FIELDS = {
    "associated_entities": "entity_id",
    "entity_relationships": "relationship_id",
    "hunting_pivots": "pivot_id",
    "sources": "source_id",
}


def unknown_time(basis: str = "not-stated") -> dict[str, Any]:
    return {
        "value": None,
        "precision": "unknown",
        "status": "unknown",
        "basis": basis,
    }


def canonical_time(
    value: dict[str, Any] | None,
    *,
    default_basis: str = "source-stated",
) -> dict[str, Any]:
    if not value or not value.get("value"):
        return unknown_time((value or {}).get("basis", "not-stated"))
    return {
        "value": value["value"],
        "precision": value.get("precision", "day"),
        "status": value.get("status", "known"),
        "basis": value.get("basis", default_basis),
    }


def canonical_source(item: dict[str, Any]) -> dict[str, Any]:
    path = item.get("path") or item.get("url") or ""
    accessed_at = item.get("accessed_at")
    analyst_notes = item.get("analyst_notes", "")
    if "accessed_at" not in item:
        missing_access_note = (
            "The original access timestamp was not preserved; accessed_at "
            "is null rather than inferred from a later audit."
        )
        analyst_notes = " ".join(
            part for part in (analyst_notes, missing_access_note) if part
        )
    result = {
        "source_id": item["source_id"],
        "path": path,
        "title": item["title"],
        "publisher": item.get("publisher", ""),
        "published_at": canonical_time(
            item.get("published_at"), default_basis="source-publication"
        ),
        "language": item.get("language", "en"),
        "source_type": item.get("source_type", "osint-report"),
        "tlp": item.get("tlp", "TLP:CLEAR"),
        "reliability": item.get("reliability", "high"),
        "sha256": item.get("sha256"),
        "accessed_at": accessed_at,
        "actor_scope": item.get("actor_scope", "direct"),
        "claims_supported": item.get("claims_supported", []),
        "analyst_notes": analyst_notes,
    }
    if item.get("url"):
        result["url"] = item["url"]
    if "archive_url" in item:
        result["archive_url"] = item["archive_url"]
    return result


def canonical_entity(item: dict[str, Any]) -> dict[str, Any]:
    legal_actions = []
    for action in item.get("legal_actions", []):
        legal_actions.append(
            {
                "action_id": action["action_id"],
                "action_type": action["action_type"],
                "authority": action.get("authority", ""),
                "action_date": canonical_time(action.get("action_date")),
                "status": action.get("status", "alleged"),
                "description": action.get("description", ""),
                "evidence_refs": action.get("evidence_refs", []),
                "analyst_notes": action.get("analyst_notes", ""),
            }
        )
    return {
        "entity_id": item["entity_id"],
        "name": item["name"],
        "entity_type": item["entity_type"],
        "aliases": item.get("aliases", []),
        "description": item.get("description", ""),
        "countries": item.get("countries", []),
        "roles": item.get("roles", []),
        "threat_actor_types": item.get("threat_actor_types", []),
        "first_observed": canonical_time(item.get("first_observed")),
        "last_observed": canonical_time(item.get("last_observed")),
        "legal_actions": legal_actions,
        "confidence": item.get("confidence", "unknown"),
        "evidence_refs": item.get("evidence_refs", []),
        "analyst_notes": item.get("analyst_notes", ""),
    }


def canonical_entity_relationship(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "relationship_id": item["relationship_id"],
        "source_ref": item["source_ref"],
        "target_ref": item["target_ref"],
        "relationship_type": item["relationship_type"],
        "description": item.get("description", ""),
        "first_observed": canonical_time(item.get("first_observed")),
        "last_observed": canonical_time(item.get("last_observed")),
        "confidence": item.get("confidence", "unknown"),
        "evidence_refs": item.get("evidence_refs", []),
        "analyst_notes": item.get("analyst_notes", ""),
    }


def canonical_hunting_pivot(item: dict[str, Any]) -> dict[str, Any]:
    observations = []
    for observation in item.get("observations", []):
        observations.append(
            {
                "observation_id": observation["observation_id"],
                "observed_at": canonical_time(observation.get("observed_at")),
                "source_ref": observation["source_ref"],
                "activity_ref": observation.get("activity_ref"),
                "context": observation.get("context", ""),
                "count": observation.get("count", 1),
                # Absence of a stated unit must never be promoted to a count
                # of attack events.  It represents one evidence record only.
                "count_basis": observation.get("count_basis", "unknown"),
            }
        )
    observed_values = [
        observation["observed_at"]
        for observation in observations
        if observation["observed_at"].get("value")
    ]
    first_is_explicit = "first_observed" in item
    last_is_explicit = "last_observed" in item
    first_observed = canonical_time(item.get("first_observed"))
    last_observed = canonical_time(item.get("last_observed"))
    if observed_values and not first_is_explicit:
        first_observed = min(observed_values, key=lambda point: point["value"])
    if observed_values and not last_is_explicit:
        last_observed = max(observed_values, key=lambda point: point["value"])
    source_refs = {observation["source_ref"] for observation in observations}
    activity_refs = {
        observation["activity_ref"]
        for observation in observations
        if observation.get("activity_ref")
    }
    continuity = item.get("continuity", {})
    return {
        "pivot_id": item["pivot_id"],
        "category": item["category"],
        "pivot_type": item["pivot_type"],
        "value": item["value"],
        "description": item.get("description", ""),
        "stix_pattern": item.get("stix_pattern"),
        "attribution_scope": item.get("attribution_scope", "unknown"),
        "malware_refs": item.get("malware_refs", []),
        "infrastructure_refs": item.get("infrastructure_refs", []),
        "activity_refs": item.get("activity_refs", []),
        "indicator_refs": item.get("indicator_refs", []),
        "observations": observations,
        "first_observed": first_observed,
        "last_observed": last_observed,
        "observation_count": sum(item["count"] for item in observations),
        "source_count": len(source_refs),
        "activity_count": len(activity_refs),
        "continuity": {
            "assessment": continuity.get("assessment", "unknown"),
            "active_status": continuity.get("active_status", "unknown"),
            "evaluated_at": continuity.get("evaluated_at", UPDATED_AT),
            "basis": continuity.get("basis", ""),
            "passive_scan_performed": continuity.get(
                "passive_scan_performed", False
            ),
            "checks": [
                {
                    "check_id": check["check_id"],
                    "evaluated_at": check["evaluated_at"],
                    "platform": check["platform"],
                    "query": check["query"],
                    "index_or_time_window": check.get(
                        "index_or_time_window", ""
                    ),
                    "result_count": check.get("result_count"),
                    "result_summary": check.get("result_summary", ""),
                    "analyst_validated": check.get(
                        "analyst_validated", False
                    ),
                    "evidence_refs": check.get("evidence_refs", []),
                    "limitations": check.get("limitations", ""),
                }
                for check in continuity.get("checks", [])
            ],
        },
        "hunt_queries": [
            {
                "platform": query["platform"],
                "query": query["query"],
                "purpose": query.get("purpose", ""),
                "requires_validation": query.get("requires_validation", True),
                "false_positive_notes": query.get("false_positive_notes", ""),
            }
            for query in item.get("hunt_queries", [])
        ],
        "confidence": item.get("confidence", "unknown"),
        "evidence_refs": item.get("evidence_refs", sorted(source_refs)),
        "analyst_notes": item.get("analyst_notes", ""),
    }


def canonical_update(update: dict[str, Any]) -> dict[str, Any]:
    claims_by_source: dict[str, set[str]] = {}

    def add_claims(refs: list[str], *claims: str) -> None:
        for source_ref in refs:
            claims_by_source.setdefault(source_ref, set()).update(claims)

    for entity in update.get("associated_entities", []):
        add_claims(entity.get("evidence_refs", []), "identity")
        for action in entity.get("legal_actions", []):
            add_claims(action.get("evidence_refs", []), "legal-action")
    for relationship in update.get("entity_relationships", []):
        add_claims(relationship.get("evidence_refs", []), "relationship")
    for pivot in update.get("hunting_pivots", []):
        category_claim = {
            "infrastructure": "infrastructure",
            "malware": "malware",
            "identity": "identity",
            "behavior": "artifact",
        }.get(pivot.get("category"), "artifact")
        add_claims(
            pivot.get("evidence_refs", []),
            "hunting-pivot",
            category_claim,
        )
        for observation in pivot.get("observations", []):
            add_claims(
                [observation["source_ref"]],
                "hunting-pivot",
                category_claim,
            )

    sources = []
    for item in update.get("sources", []):
        item = dict(item)
        if not item.get("claims_supported"):
            item["claims_supported"] = sorted(
                claims_by_source.get(item["source_id"], {"assessment"})
            )
        sources.append(canonical_source(item))
    return {
        "remove_ids": {
            field: list(update.get("remove_ids", {}).get(field, []))
            for field in MERGE_FIELDS
        },
        "sources": sources,
        "associated_entities": [
            canonical_entity(item)
            for item in update.get("associated_entities", [])
        ],
        "entity_relationships": [
            canonical_entity_relationship(item)
            for item in update.get("entity_relationships", [])
        ],
        "hunting_pivots": [
            canonical_hunting_pivot(item)
            for item in update.get("hunting_pivots", [])
        ],
    }


def merge_by_id(
    existing: list[dict[str, Any]],
    additions: list[dict[str, Any]],
    id_field: str,
) -> list[dict[str, Any]]:
    """Replace matching records without reordering the existing corpus.

    Source arrays can contain thousands of reviewed records.  Sorting the
    complete array while adding one record creates a noisy, hard-to-review
    diff, so existing order is retained and genuinely new IDs are appended in
    research-file order.
    """
    merged = {item[id_field]: item for item in existing}
    ordered_ids = [item[id_field] for item in existing]
    for item in additions:
        if item[id_field] not in merged:
            ordered_ids.append(item[id_field])
        merged[item[id_field]] = item
    return [merged[key] for key in ordered_ids]


def migrate_profile(profile: dict[str, Any]) -> bool:
    changed = False
    if profile.get("schema_version") != SCHEMA_VERSION:
        profile["schema_version"] = SCHEMA_VERSION
        changed = True
    for field in COLLECTION_FIELDS:
        if field not in profile:
            profile[field] = []
            changed = True
    if profile.get("updated_at", "") < UPDATED_AT:
        profile["updated_at"] = UPDATED_AT
        changed = True
    return changed


def apply_update(profile: dict[str, Any], update: dict[str, Any]) -> bool:
    update = canonical_update(update)
    before = {
        field: profile.get(field, [])
        for field in (*COLLECTION_FIELDS, "sources")
    }
    for field in MERGE_FIELDS:
        remove_ids = set(update["remove_ids"].get(field, []))
        retained = [
            item
            for item in profile.get(field, [])
            if item.get(ID_FIELDS[field]) not in remove_ids
        ]
        profile[field] = merge_by_id(
            retained,
            update.get(field, []),
            ID_FIELDS[field],
        )
    return any(profile[field] != before[field] for field in before)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--research",
        type=Path,
        default=Path("actor_profile/osint/hunting-entity-research.json"),
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    research_path = (
        args.research
        if args.research.is_absolute()
        else root / args.research
    )
    research = load_json(research_path)
    updates = research.get("profiles", {})
    changed_paths: list[str] = []

    for profile_path in sorted((root / "profiles").glob("*/actor-profile.json")):
        profile = load_json(profile_path)
        changed = migrate_profile(profile)
        slug = profile_path.parent.name
        if slug in updates:
            changed = apply_update(profile, updates[slug]) or changed
        if changed:
            changed_paths.append(str(profile_path.relative_to(root)))
            if args.apply:
                write_json_atomic(profile_path, profile)

    missing = sorted(set(updates) - {Path(path).parent.name for path in changed_paths})
    if missing:
        # An update that already matched byte-for-byte is not in changed_paths;
        # check the filesystem before treating it as a missing target.
        missing = [
            slug
            for slug in missing
            if not (root / "profiles" / slug / "actor-profile.json").exists()
        ]
    if missing:
        raise SystemExit(f"research targets missing profiles: {', '.join(missing)}")

    verb = "updated" if args.apply else "would update"
    print(f"{verb} {len(changed_paths)} profiles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
