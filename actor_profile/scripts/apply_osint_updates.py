#!/usr/bin/env python3
"""Merge a reviewed OSINT update file into an actor profile."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from common import load_json, utc_now, write_json_atomic


KEYS = {
    "aliases": lambda item: item["name"].casefold(),
    "motivations": lambda item: item["type"].casefold(),
    "relationships": lambda item: item["relationship_id"],
    "malware": lambda item: item["id"],
    "tools": lambda item: item["id"],
    "infrastructure": lambda item: item["id"],
    "delivery_formats": lambda item: item["id"],
    "vulnerabilities": lambda item: item["id"],
    "operational_capabilities": lambda item: item["id"],
    "activities": lambda item: item["activity_id"],
    "countries": lambda item: item["id"],
    "regions": lambda item: item["id"],
    "sectors": lambda item: item["id"],
    "roles": lambda item: item["id"],
    "ttps": lambda item: item["ttp_id"],
    "sources": lambda item: item["source_id"],
}


def merge_records(
    existing: list[dict[str, Any]],
    updates: list[dict[str, Any]],
    key_name: str,
) -> list[dict[str, Any]]:
    key = KEYS[key_name]
    positions = {key(item): index for index, item in enumerate(existing)}
    result = list(existing)
    for item in updates:
        item_key = key(item)
        if item_key in positions:
            result[positions[item_key]] = item
        else:
            positions[item_key] = len(result)
            result.append(item)
    return result


def append_unique(existing: list[Any], updates: list[Any]) -> list[Any]:
    result = list(existing)
    seen = {json.dumps(item, sort_keys=True, ensure_ascii=False) for item in result}
    for item in updates:
        marker = json.dumps(item, sort_keys=True, ensure_ascii=False)
        if marker not in seen:
            result.append(item)
            seen.add(marker)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    parser.add_argument("update", type=Path)
    args = parser.parse_args()

    profile = load_json(args.profile)
    update = load_json(args.update)
    if update["actor_ref"] != profile["profile_id"]:
        raise ValueError("OSINT update actor_ref does not match profile_id")

    profile["sources"] = merge_records(
        profile["sources"], update.get("sources", []), "sources"
    )
    profile["actor"]["aliases"] = merge_records(
        profile["actor"]["aliases"],
        update.get("actor", {}).get("aliases", []),
        "aliases",
    )
    for field in ("description", "first_seen", "last_seen", "active", "analyst_notes"):
        if field in update.get("actor", {}):
            profile["actor"][field] = update["actor"][field]
    if "attribution" in update:
        for field, value in update["attribution"].items():
            profile["attribution"][field] = value
    profile["motivations"] = merge_records(
        profile["motivations"], update.get("motivations", []), "motivations"
    )
    profile["relationships"] = merge_records(
        profile["relationships"], update.get("relationships", []), "relationships"
    )
    for field in (
        "malware", "tools", "infrastructure", "delivery_formats",
        "vulnerabilities", "operational_capabilities",
    ):
        profile["capabilities"][field] = merge_records(
            profile["capabilities"][field],
            update.get("capabilities", {}).get(field, []),
            field,
        )
    profile["activities"] = merge_records(
        profile["activities"], update.get("activities", []), "activities"
    )
    for field in ("countries", "regions", "sectors", "roles"):
        profile["targets"][field] = merge_records(
            profile["targets"][field],
            update.get("targets", {}).get(field, []),
            field,
        )
    for field in ("selection_logic", "analyst_notes"):
        if field in update.get("targets", {}):
            profile["targets"][field] = update["targets"][field]
    profile["ttps"] = merge_records(
        profile["ttps"], update.get("ttps", []), "ttps"
    )
    for field in ("key_judgments", "gaps", "uncertainties"):
        profile["assessment"][field] = append_unique(
            profile["assessment"][field],
            update.get("assessment", {}).get(field, []),
        )
    for field in ("collection_notes", "analyst_notes"):
        if field in update.get("assessment", {}):
            addition = update["assessment"][field]
            if addition and addition not in profile["assessment"][field]:
                profile["assessment"][field] = (
                    profile["assessment"][field].rstrip() + "\n" + addition
                ).strip()
    for field, addition in update.get("free_text_append", {}).items():
        if addition and addition not in profile["free_text"].get(field, ""):
            profile["free_text"][field] = (
                profile["free_text"].get(field, "").rstrip() + "\n\n" + addition
            ).strip()
    profile["updated_at"] = utc_now()
    profile["status"] = update.get("resulting_status", "review")
    write_json_atomic(args.profile, profile)
    print(
        json.dumps(
            {
                "profile": str(args.profile.resolve()),
                "sources_added": len(update.get("sources", [])),
                "activities_added": len(update.get("activities", [])),
                "ttps_added": len(update.get("ttps", [])),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
