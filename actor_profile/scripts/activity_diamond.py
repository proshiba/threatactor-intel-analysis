#!/usr/bin/env python3
"""Build evidence-linked Diamond Model records for profile activities.

The activity model intentionally stores references instead of copying names and
descriptions.  This keeps the four Diamond Model vertices synchronized with the
canonical capability, target, victim-case, and TTP records in the same profile.
"""

from __future__ import annotations

import copy
from typing import Any


SCHEMA_VERSION = "1.2.0"
DERIVATION_NOTE = "[activity-diamond-v1]"


def _unique(values: list[str]) -> list[str]:
    return sorted({value for value in values if isinstance(value, str) and value})


def _by_id(items: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    return {
        item[key]: item
        for item in items
        if isinstance(item, dict) and isinstance(item.get(key), str)
    }


def build_activity_diamond(
    profile: dict[str, Any], activity: dict[str, Any]
) -> dict[str, Any]:
    """Return a deterministic activity-level Diamond Model.

    Only records explicitly linked to the activity are included.  Actor-level
    capability or targeting history is never used to fill an activity gap.
    Victim-case links may contribute their target, malware, TTP, impact, and
    evidence references because those cases are explicitly tied to the same
    activity.
    """

    activity_id = activity.get("activity_id", "")
    victims = profile.get("victim_cases", []) or []
    linked_victims = [
        victim
        for victim in victims
        if victim.get("victim_case_id") in set(activity.get("victim_refs", []))
        or activity_id in victim.get("activity_refs", [])
    ]

    ttps = profile.get("ttps", []) or []
    ttp_by_id = _by_id(ttps, "ttp_id")
    ttp_refs = _unique(
        list(activity.get("ttp_refs", []))
        + [ref for victim in linked_victims for ref in victim.get("ttp_refs", [])]
    )
    linked_ttps = [ttp_by_id[ref] for ref in ttp_refs if ref in ttp_by_id]

    malware_refs = _unique(
        list(activity.get("malware_refs", []))
        + [ref for victim in linked_victims for ref in victim.get("malware_refs", [])]
        + [ref for ttp in linked_ttps for ref in ttp.get("malware_refs", [])]
    )
    infrastructure_refs = _unique(
        list(activity.get("infrastructure_refs", []))
        + [
            ref
            for ttp in linked_ttps
            for ref in ttp.get("infrastructure_refs", [])
        ]
    )
    target_refs = _unique(
        list(activity.get("target_refs", []))
        + [ref for victim in linked_victims for ref in victim.get("target_refs", [])]
    )
    victim_refs = _unique(
        list(activity.get("victim_refs", []))
        + [victim.get("victim_case_id", "") for victim in linked_victims]
    )

    targets = profile.get("targets", {}) or {}
    country_ids = {
        item.get("id") for item in targets.get("countries", []) if item.get("id")
    }
    region_ids = {
        item.get("id") for item in targets.get("regions", []) if item.get("id")
    }
    phases = _unique(
        [
            phase.strip()
            for ttp in linked_ttps
            for phase in str(ttp.get("tactic", "")).split(",")
        ]
    )
    results = _unique(
        [
            impact.get("impact_type", "")
            for victim in linked_victims
            for impact in victim.get("impacts", [])
            if isinstance(impact, dict)
        ]
    )

    evidence_refs = _unique(
        list(activity.get("evidence_refs", []))
        + [ref for victim in linked_victims for ref in victim.get("evidence_refs", [])]
        + [ref for ttp in linked_ttps for ref in ttp.get("evidence_refs", [])]
    )
    attribution = profile.get("attribution", {}) or {}
    actor = profile.get("actor", {}) or {}
    actor_ref = profile.get("profile_id") or ""
    actor_name = (
        actor.get("canonical_name")
        or profile.get("name")
        or actor_ref.removeprefix("actor--")
    )
    organizations = attribution.get("organizations", []) or []

    note = (
        f"{DERIVATION_NOTE} 活動、被害事例、TTPに明示された参照だけから生成。"
        "空配列は活動単位の根拠が確認できないことを示し、"
        "アクター全体の実績では補完しない。"
    )
    return {
        "adversary": {
            "actor_ref": actor_ref,
            "name": actor_name,
            "attribution_countries": _unique(
                list(attribution.get("countries", []))
            ),
            "organization_refs": _unique(
                [item.get("id", "") for item in organizations]
            ),
        },
        "capability": {
            "malware_refs": malware_refs,
            "ttp_refs": ttp_refs,
        },
        "infrastructure": {
            "infrastructure_refs": infrastructure_refs,
        },
        "victim": {
            "target_refs": target_refs,
            "victim_refs": victim_refs,
        },
        "meta_features": {
            "first_observed": copy.deepcopy(activity.get("first_observed")),
            "last_observed": copy.deepcopy(activity.get("last_observed")),
            "reported_at": copy.deepcopy(activity.get("reported_at")),
            "activity_type": activity.get("activity_type", ""),
            "phases": phases,
            "results": results,
            "direction": {
                "source_countries": _unique(
                    list(attribution.get("countries", []))
                ),
                "target_country_refs": [
                    ref for ref in target_refs if ref in country_ids
                ],
                "target_region_refs": [
                    ref for ref in target_refs if ref in region_ids
                ],
            },
        },
        "confidence": activity.get("confidence", "unknown"),
        "evidence_refs": evidence_refs,
        "analyst_notes": note,
    }


def materialize_profile_diamonds(profile: dict[str, Any]) -> int:
    """Refresh every activity Diamond Model and return the changed count."""

    profile["schema_version"] = SCHEMA_VERSION
    changed = 0
    for activity in profile.get("activities", []):
        modeled = build_activity_diamond(profile, activity)
        if activity.get("diamond_model") != modeled:
            activity["diamond_model"] = modeled
            changed += 1
    return changed
