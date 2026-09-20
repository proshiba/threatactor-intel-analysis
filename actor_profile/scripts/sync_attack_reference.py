#!/usr/bin/env python3
"""Synchronize current Enterprise ATT&CK facts without erasing other evidence.

Profiles mapped to a Group that remains in the current ATT&CK release are
updated from that release.  Facts supported only by the previous ATT&CK
release are removed before current aliases, software, campaigns, and general
techniques are added.  Profiles whose Group is no longer current retain their
historical source and are pointed at the frozen historical index instead of
the current file.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import (
    capability,
    derive_motivations,
    normalized_name,
    time_point,
)
from common import load_json, unknown_time, utc_now, write_json_atomic


OLD_SOURCE_ID = "source--mitre-attack-19-1"
CURRENT_SOURCE_ID = "source--mitre-attack-19-2"


def source_record(source_id: str, *, historical: bool = False) -> dict[str, Any]:
    version = "19.1" if historical else "19.2"
    published = "2026-05-12" if historical else "2026-08-05"
    path = (
        "actor_profile/reference/attack-enterprise-19.1.json"
        if historical
        else "actor_profile/reference/attack-index.json"
    )
    return {
        "source_id": source_id,
        "path": path,
        "title": f"MITRE Enterprise ATT&CK {version} compact local index",
        "publisher": "MITRE",
        "published_at": time_point(published, "upstream-release"),
        "language": "en",
        "source_type": "structured-knowledge-base",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "exact",
        "claims_supported": [
            "identity",
            "alias",
            "relationship",
            "activity",
            "malware",
            "targeting",
            "ttp",
        ],
        "analyst_notes": (
            "Frozen historical ATT&CK release retained for Groups that are no "
            "longer current. Deprecated status is not interpreted as proof "
            "that the real-world actor ceased to exist."
            if historical
            else "Derived from the official MITRE attack-stix-data release. "
            "ATT&CK modification dates are not activity observation dates."
        ),
    }


def sync_aliases(profile: dict[str, Any], group: dict[str, Any]) -> None:
    current = {
        normalized_name(name): name
        for name in group.get("aliases", [])
        if normalized_name(name)
        and normalized_name(name)
        != normalized_name(profile["actor"].get("canonical_name", ""))
    }
    aliases = []
    for item in profile["actor"].get("aliases", []):
        key = normalized_name(item.get("name", ""))
        refs = set(item.get("evidence_refs", []))
        if key in current:
            refs.discard(OLD_SOURCE_ID)
            refs.add(CURRENT_SOURCE_ID)
        elif refs & {OLD_SOURCE_ID, CURRENT_SOURCE_ID}:
            refs -= {OLD_SOURCE_ID, CURRENT_SOURCE_ID}
            if not refs:
                continue
        item["evidence_refs"] = sorted(refs)
        aliases.append(item)
    by_name = {normalized_name(item.get("name", "")): item for item in aliases}
    for key, name in current.items():
        item = by_name.get(key)
        if item is None:
            item = {
                "name": name,
                "vendor": "MITRE ATT&CK",
                "scope": "overlapping",
                "confidence": "high",
                "evidence_refs": [CURRENT_SOURCE_ID],
                "analyst_notes": (
                    "Official ATT&CK associated-group name. Vendor collection "
                    "boundaries may differ, so exactness is not inferred."
                ),
            }
            aliases.append(item)
            by_name[key] = item
        else:
            item["evidence_refs"] = sorted(
                set(item.get("evidence_refs", [])) | {CURRENT_SOURCE_ID}
            )
            if "MITRE ATT&CK" not in item.get("vendor", ""):
                item["vendor"] = " / ".join(
                    part for part in (item.get("vendor", ""), "MITRE ATT&CK") if part
                )
    profile["actor"]["aliases"] = sorted(
        aliases, key=lambda item: normalized_name(item.get("name", ""))
    )


def sync_capabilities(
    profile: dict[str, Any], group: dict[str, Any], attack: dict[str, Any]
) -> None:
    software = [
        attack["software"][ref]
        for ref in group.get("software_refs", [])
        if ref in attack.get("software", {})
    ]
    by_kind: dict[str, dict[str, dict[str, Any]]] = {"malware": {}, "tools": {}}
    for item in software:
        bucket = "malware" if item.get("software_type") == "malware" else "tools"
        by_kind[bucket][normalized_name(item.get("name", ""))] = item

    for bucket, current in by_kind.items():
        retained = []
        for item in profile.get("capabilities", {}).get(bucket, []):
            key = normalized_name(item.get("name", ""))
            refs = set(item.get("evidence_refs", []))
            if key in current:
                refs.discard(OLD_SOURCE_ID)
                refs.add(CURRENT_SOURCE_ID)
            elif refs & {OLD_SOURCE_ID, CURRENT_SOURCE_ID}:
                refs -= {OLD_SOURCE_ID, CURRENT_SOURCE_ID}
                if not refs:
                    continue
            item["evidence_refs"] = sorted(refs)
            retained.append(item)
        existing = {normalized_name(item.get("name", "")): item for item in retained}
        for key, software_item in current.items():
            item = existing.get(key)
            if item is None:
                item = capability(
                    "malware" if bucket == "malware" else "tool",
                    software_item["name"],
                    software_item.get("description", ""),
                    [CURRENT_SOURCE_ID],
                    aliases=software_item.get("aliases", []),
                    types=software_item.get("platforms", []),
                    confidence="high",
                )
                retained.append(item)
                existing[key] = item
            else:
                item.update(
                    {
                        "name": software_item["name"],
                        "aliases": software_item.get("aliases", []),
                        "types": software_item.get("platforms", []),
                        "description": software_item.get("description", ""),
                        "confidence": "high",
                    }
                )
                item["evidence_refs"] = sorted(
                    set(item.get("evidence_refs", [])) | {CURRENT_SOURCE_ID}
                )
        profile["capabilities"][bucket] = sorted(
            retained, key=lambda item: normalized_name(item.get("name", ""))
        )


def sync_general_ttps(
    profile: dict[str, Any], group: dict[str, Any], attack: dict[str, Any]
) -> None:
    current_uses = {
        item.get("target_external_id"): item
        for item in group.get("technique_uses", [])
        if item.get("target_external_id")
    }
    retained: list[dict[str, Any]] = []
    existing: dict[str, dict[str, Any]] = {}
    for item in profile.get("ttps", []):
        technique_id = item.get("technique_id", "")
        refs = set(item.get("evidence_refs", []))
        general = not item.get("activity_refs")
        if general and technique_id in current_uses:
            refs.discard(OLD_SOURCE_ID)
            refs.add(CURRENT_SOURCE_ID)
        elif general and refs & {OLD_SOURCE_ID, CURRENT_SOURCE_ID}:
            refs -= {OLD_SOURCE_ID, CURRENT_SOURCE_ID}
            if not refs:
                continue
        item["evidence_refs"] = sorted(refs)
        retained.append(item)
        if general and technique_id:
            existing[technique_id] = item

    for technique_id, use in current_uses.items():
        technique = attack.get("techniques", {}).get(technique_id, {})
        item = existing.get(technique_id)
        if item is None:
            item = {
                "ttp_id": f"ttp--{technique_id.casefold().replace('.', '-')}--general",
                "tactic": ", ".join(technique.get("tactics", []) or ["Uncategorized"]),
                "technique_id": technique_id,
                "technique_name": technique.get("name", f"MITRE ATT&CK {technique_id}"),
                "observed_behavior": use.get("description", ""),
                "activity_refs": [],
                "malware_refs": [],
                "infrastructure_refs": [],
                "first_observed": unknown_time(),
                "last_observed": unknown_time(),
                "confidence": "high",
                "evidence_refs": [CURRENT_SOURCE_ID],
                "analyst_notes": (
                    "Current ATT&CK actor-level procedure example. No activity "
                    "date is inferred from relationship modification time."
                ),
            }
            retained.append(item)
            existing[technique_id] = item
        else:
            item["technique_name"] = technique.get("name", item.get("technique_name"))
            item["tactic"] = ", ".join(technique.get("tactics", [])) or item.get(
                "tactic", "Uncategorized"
            )
            if use.get("description"):
                item["observed_behavior"] = use["description"]
            item["evidence_refs"] = sorted(
                set(item.get("evidence_refs", [])) | {CURRENT_SOURCE_ID}
            )
    profile["ttps"] = sorted(retained, key=lambda item: item.get("ttp_id", ""))


def sync_campaigns(
    profile: dict[str, Any], group: dict[str, Any], attack: dict[str, Any]
) -> None:
    current = {
        normalized_name(attack["campaigns"][ref].get("name", "")): attack["campaigns"][ref]
        for ref in group.get("campaign_refs", [])
        if ref in attack.get("campaigns", {})
    }
    before = profile.get("activities", [])
    retained_activities = []
    for item in before:
        key = normalized_name(item.get("name", ""))
        refs = set(item.get("evidence_refs", []))
        if key in current:
            refs.discard(OLD_SOURCE_ID)
            refs.add(CURRENT_SOURCE_ID)
        elif refs & {OLD_SOURCE_ID, CURRENT_SOURCE_ID}:
            refs -= {OLD_SOURCE_ID, CURRENT_SOURCE_ID}
            if not refs:
                continue
        item["evidence_refs"] = sorted(refs)
        retained_activities.append(item)
    profile["activities"] = retained_activities
    retained_ids = {item.get("activity_id") for item in profile["activities"]}
    removed_ids = {
        item.get("activity_id")
        for item in before
        if item.get("activity_id") not in retained_ids
    }
    if removed_ids:
        retained_ttps = []
        for item in profile.get("ttps", []):
            item["activity_refs"] = [
                ref for ref in item.get("activity_refs", []) if ref not in removed_ids
            ]
            if (
                item.get("ttp_id", "").startswith("ttp--mitre-campaign--")
                and not item["activity_refs"]
                and set(item.get("evidence_refs", [])) <= {CURRENT_SOURCE_ID}
            ):
                continue
            retained_ttps.append(item)
        profile["ttps"] = retained_ttps
        for victim in profile.get("victim_cases", []):
            victim["activity_refs"] = [
                ref for ref in victim.get("activity_refs", []) if ref not in removed_ids
            ]
    for activity in profile["activities"]:
        campaign = current.get(normalized_name(activity.get("name", "")))
        if not campaign:
            continue
        activity["description"] = campaign.get("description", "")
        activity["first_observed"] = time_point(
            campaign.get("first_seen"), "mitre-attack-campaign"
        )
        activity["last_observed"] = time_point(
            campaign.get("last_seen"), "mitre-attack-campaign"
        )
        activity["evidence_refs"] = sorted(
            set(activity.get("evidence_refs", [])) | {CURRENT_SOURCE_ID}
        )


def sync_current_profile(
    profile: dict[str, Any], actor: dict[str, Any], group: dict[str, Any], attack: dict[str, Any]
) -> None:
    had_old_source = any(
        item.get("source_id") == OLD_SOURCE_ID for item in profile.get("sources", [])
    )
    profile["sources"] = [
        item
        for item in profile.get("sources", [])
        if item.get("source_id") not in {OLD_SOURCE_ID, CURRENT_SOURCE_ID}
    ]
    if had_old_source:
        profile["sources"].append(source_record(OLD_SOURCE_ID, historical=True))
    profile["sources"].append(source_record(CURRENT_SOURCE_ID))
    profile["actor"]["description"] = group.get("description", "")
    profile["actor"]["first_seen"] = time_point(group.get("first_seen"), "mitre-attack")
    profile["actor"]["last_seen"] = time_point(group.get("last_seen"), "mitre-attack")
    sync_aliases(profile, group)
    sync_capabilities(profile, group, attack)
    sync_general_ttps(profile, group, attack)
    sync_campaigns(profile, group, attack)

    retained_motivations = profile.get("motivations", [])
    by_type = {item.get("type"): item for item in retained_motivations}
    workbook_source = "source--actor-mapping-workbook"
    for item in derive_motivations(
        profile["actor"].get("actor_types", []),
        group,
        CURRENT_SOURCE_ID,
        workbook_source,
    ):
        existing = by_type.get(item["type"])
        if existing is None:
            by_type[item["type"]] = item
        else:
            existing["evidence_refs"] = sorted(
                set(existing.get("evidence_refs", []))
                | set(item.get("evidence_refs", []))
            )
    profile["motivations"] = sorted(by_type.values(), key=lambda item: item.get("type", ""))
    profile["updated_at"] = utc_now()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json"))
    parser.add_argument("--attack", type=Path, default=Path("actor_profile/reference/attack-index.json"))
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    args = parser.parse_args()

    catalog = load_json(args.catalog)
    attack = load_json(args.attack)
    stats = {"current": 0, "historical": 0, "unmapped": 0}
    for actor in catalog.get("actors", []):
        path = args.profiles_root / actor["slug"] / "actor-profile.json"
        if not path.exists():
            continue
        profile = load_json(path)
        group_id = actor.get("mitre_group_id", "")
        group = attack.get("groups", {}).get(group_id)
        if group:
            sync_current_profile(profile, actor, group, attack)
            stats["current"] += 1
        elif any(
            item.get("source_id") == OLD_SOURCE_ID for item in profile.get("sources", [])
        ):
            profile["sources"] = [
                source_record(OLD_SOURCE_ID, historical=True)
                if item.get("source_id") == OLD_SOURCE_ID
                else item
                for item in profile.get("sources", [])
            ]
            profile["updated_at"] = utc_now()
            stats["historical"] += 1
        else:
            stats["unmapped"] += 1
        write_json_atomic(path, profile)

    print(stats)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
