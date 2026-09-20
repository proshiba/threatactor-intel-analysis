#!/usr/bin/env python3
"""Build a compact actor/technique/software index from MITRE ATT&CK STIX."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from common import utc_now, write_json_atomic


def external_id(obj: dict[str, Any]) -> str:
    for reference in obj.get("external_references", []):
        if reference.get("source_name") == "mitre-attack":
            return str(reference.get("external_id", ""))
    return ""


def active_object(obj: dict[str, Any]) -> bool:
    """Return whether an ATT&CK object is current and safe to materialize.

    ATT&CK keeps deprecated objects in its STIX bundles for compatibility.
    ``revoked`` and ``x_mitre_deprecated`` are independent flags, so checking
    only the former can silently resurrect retired Groups or relationships.
    """
    return not obj.get("revoked") and not obj.get("x_mitre_deprecated")


def relationship_record(
    relationship: dict[str, Any],
    target: dict[str, Any],
) -> dict[str, Any]:
    return {
        "relationship_id": relationship.get("relationship_id", ""),
        "target_ref": relationship.get("target_ref", ""),
        "target_type": target.get("type", ""),
        "target_external_id": external_id(target),
        "target_name": target.get("name", ""),
        "description": relationship.get("description", ""),
        "external_references": [
            {
                key: reference[key]
                for key in ("source_name", "url", "description")
                if reference.get(key)
            }
            for reference in relationship.get("external_references", [])
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    bundle = json.loads(args.input.read_text(encoding="utf-8"))
    objects = bundle.get("objects", [])
    by_id = {obj["id"]: obj for obj in objects if obj.get("id")}
    relationships: dict[str, list[dict[str, str]]] = defaultdict(list)
    for obj in objects:
        if obj.get("type") != "relationship" or not active_object(obj):
            continue
        relationships[obj.get("source_ref", "")].append(
            {
                "relationship_id": obj.get("id", ""),
                "relationship_type": obj.get("relationship_type", ""),
                "target_ref": obj.get("target_ref", ""),
                "description": obj.get("description", ""),
                "external_references": obj.get("external_references", []),
            }
        )

    techniques: dict[str, Any] = {}
    for obj in objects:
        if obj.get("type") != "attack-pattern" or not active_object(obj):
            continue
        technique_id = external_id(obj)
        if not technique_id.startswith("T"):
            continue
        techniques[technique_id] = {
            "stix_id": obj["id"],
            "name": obj.get("name", technique_id),
            "tactics": sorted(
                {
                    phase.get("phase_name", "").replace("-", " ").title()
                    for phase in obj.get("kill_chain_phases", [])
                    if phase.get("phase_name")
                }
            ),
            "platforms": sorted(obj.get("x_mitre_platforms", [])),
            "deprecated": bool(obj.get("x_mitre_deprecated", False)),
        }

    software: dict[str, Any] = {}
    for obj in objects:
        if obj.get("type") not in {"malware", "tool"} or not active_object(obj):
            continue
        software[obj["id"]] = {
            "stix_id": obj["id"],
            "external_id": external_id(obj),
            "name": obj.get("name", ""),
            "aliases": sorted(set(obj.get("x_mitre_aliases", []))),
            "software_type": obj["type"],
            "description": obj.get("description", ""),
            "platforms": sorted(obj.get("x_mitre_platforms", [])),
        }

    campaigns: dict[str, Any] = {}
    for obj in objects:
        if obj.get("type") != "campaign" or not active_object(obj):
            continue
        campaign_relationships = relationships.get(obj["id"], [])
        campaigns[obj["id"]] = {
            "stix_id": obj["id"],
            "external_id": external_id(obj),
            "name": obj.get("name", ""),
            "aliases": sorted(set(obj.get("aliases", []))),
            "description": obj.get("description", ""),
            "first_seen": obj.get("first_seen"),
            "last_seen": obj.get("last_seen"),
            "technique_uses": sorted(
                [
                    relationship_record(item, by_id[item["target_ref"]])
                    for item in campaign_relationships
                    if item["relationship_type"] == "uses"
                    and item["target_ref"] in by_id
                    and by_id[item["target_ref"]].get("type") == "attack-pattern"
                ],
                key=lambda item: item["target_external_id"],
            ),
            "software_uses": sorted(
                [
                    relationship_record(item, by_id[item["target_ref"]])
                    for item in campaign_relationships
                    if item["relationship_type"] == "uses"
                    and item["target_ref"] in by_id
                    and by_id[item["target_ref"]].get("type") in {"malware", "tool"}
                ],
                key=lambda item: (item["target_type"], item["target_name"]),
            ),
            "group_refs": sorted(
                {
                    item["target_ref"]
                    for item in campaign_relationships
                    if item["relationship_type"] == "attributed-to"
                    and item["target_ref"] in by_id
                    and by_id[item["target_ref"]].get("type") == "intrusion-set"
                }
            ),
        }

    groups: dict[str, Any] = {}
    for obj in objects:
        if obj.get("type") != "intrusion-set" or not active_object(obj):
            continue
        group_id = external_id(obj) or obj["id"]
        group_relationships = relationships.get(obj["id"], [])
        groups[group_id] = {
            "stix_id": obj["id"],
            "external_id": external_id(obj),
            "name": obj.get("name", ""),
            "aliases": sorted(set(obj.get("aliases", []))),
            "description": obj.get("description", ""),
            "first_seen": obj.get("first_seen"),
            "last_seen": obj.get("last_seen"),
            "technique_uses": sorted(
                [
                    relationship_record(item, by_id[item["target_ref"]])
                    for item in group_relationships
                    if item["relationship_type"] == "uses"
                    and item["target_ref"] in by_id
                    and by_id[item["target_ref"]].get("type") == "attack-pattern"
                ],
                key=lambda item: item["target_external_id"],
            ),
            "technique_ids": sorted(
                {
                    external_id(by_id[item["target_ref"]])
                    for item in group_relationships
                    if item["relationship_type"] == "uses"
                    and item["target_ref"] in by_id
                    and by_id[item["target_ref"]].get("type") == "attack-pattern"
                    and external_id(by_id[item["target_ref"]])
                }
            ),
            "software_refs": sorted(
                {
                    item["target_ref"]
                    for item in group_relationships
                    if item["relationship_type"] == "uses"
                    and item["target_ref"] in software
                }
            ),
            "software_uses": sorted(
                [
                    relationship_record(item, by_id[item["target_ref"]])
                    for item in group_relationships
                    if item["relationship_type"] == "uses"
                    and item["target_ref"] in software
                ],
                key=lambda item: (item["target_type"], item["target_name"]),
            ),
            "campaign_refs": [],
        }

    # Campaigns point to groups through attributed-to relationships.
    for campaign_ref, campaign in campaigns.items():
        for item in relationships.get(campaign_ref, []):
            if item["relationship_type"] != "attributed-to":
                continue
            for group in groups.values():
                if group["stix_id"] == item["target_ref"]:
                    group["campaign_refs"].append(campaign_ref)
                    group["campaign_refs"] = sorted(set(group["campaign_refs"]))

    collection = next(
        (obj for obj in objects if obj.get("type") == "x-mitre-collection"),
        {},
    )
    result = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "source": {
            "name": collection.get("name", "Enterprise ATT&CK"),
            "version": collection.get("x_mitre_version", "unknown"),
            "modified": collection.get("modified"),
            "url": "https://github.com/mitre-attack/attack-stix-data",
        },
        "techniques": dict(sorted(techniques.items())),
        "software": dict(sorted(software.items())),
        "campaigns": dict(sorted(campaigns.items())),
        "groups": dict(sorted(groups.items())),
    }
    write_json_atomic(args.output, result)
    print(
        json.dumps(
            {
                "output": str(args.output.resolve()),
                "techniques": len(techniques),
                "software": len(software),
                "campaigns": len(campaigns),
                "groups": len(groups),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
