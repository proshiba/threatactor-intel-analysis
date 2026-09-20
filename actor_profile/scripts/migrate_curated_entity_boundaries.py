#!/usr/bin/env python3
"""Apply reviewed actor-identity merges and software exclusions to profiles.

The census curation file prevents future materialization.  This migration also
repairs profiles that were created before a rule existed.  Exact-name actor
merges retain unique activity-linked intelligence on the canonical profile;
the legacy profile is reduced to a stable-ID tombstone.
"""

from __future__ import annotations

import argparse
import copy
import json
import unicodedata
from pathlib import Path
from typing import Any, Callable

from activity_diamond import materialize_profile_diamonds
from common import load_json, utc_now, write_json_atomic


REPO_ROOT = Path(__file__).resolve().parents[2]
MERGES = {
    "peach-sandstorm": "apt33",
    "raspberry-typhoon": "lotus-blossom",
    "sangria-tempest": "fin7",
    "violet-typhoon": "zirconium",
}
EXCLUSIONS = {"zebrocy"}

EVIDENCE_URLS = {
    "peach-sandstorm": "https://attack.mitre.org/groups/G0064/",
    "raspberry-typhoon": "https://attack.mitre.org/groups/G0030/",
    "sangria-tempest": "https://attack.mitre.org/groups/G0046/",
    "violet-typhoon": "https://attack.mitre.org/groups/G0128/",
    "zebrocy": "https://attack.mitre.org/software/S0251/",
}


def normalized_name(value: str) -> str:
    """Normalize identifiers without collapsing every non-Latin name to empty."""
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return "".join(character for character in normalized if character.isalnum())


def _source_key(item: dict[str, Any]) -> tuple[str, str]:
    return (str(item.get("url") or ""), str(item.get("path") or ""))


def _merge_scalar_lists(left: list[Any], right: list[Any]) -> list[Any]:
    result = copy.deepcopy(left)
    for value in right:
        if value not in result:
            result.append(copy.deepcopy(value))
    return result


def merge_record(target: dict[str, Any], source: dict[str, Any]) -> None:
    """Conservatively merge lists and missing fields into an existing record."""
    for key, value in source.items():
        if key not in target or target[key] in (None, "", []):
            target[key] = copy.deepcopy(value)
        elif isinstance(target[key], list) and isinstance(value, list):
            target[key] = _merge_scalar_lists(target[key], value)
        elif (
            isinstance(target[key], dict)
            and isinstance(value, dict)
            and {"value", "precision", "status", "basis"} <= target[key].keys()
            and {"value", "precision", "status", "basis"} <= value.keys()
        ):
            # A time assertion is atomic.  Field-by-field merging can produce an
            # impossible hybrid such as status=unknown with a non-null value.
            if target[key].get("status") == "unknown" and value.get("status") != "unknown":
                target[key] = copy.deepcopy(value)
        elif isinstance(target[key], dict) and isinstance(value, dict):
            merge_record(target[key], value)


def _map_collection(
    target_items: list[dict[str, Any]],
    source_items: list[dict[str, Any]],
    id_key: str,
    natural_key: Callable[[dict[str, Any]], Any],
    ref_map: dict[str, str],
) -> None:
    by_id = {item[id_key]: item for item in target_items}
    by_natural = {natural_key(item): item for item in target_items}
    for item in source_items:
        existing = by_id.get(item[id_key]) or by_natural.get(natural_key(item))
        if existing is not None:
            ref_map[item[id_key]] = existing[id_key]
        else:
            ref_map[item[id_key]] = item[id_key]


def _rewrite_refs(value: Any, ref_map: dict[str, str]) -> Any:
    if isinstance(value, str):
        return ref_map.get(value, value)
    if isinstance(value, list):
        rewritten = [_rewrite_refs(item, ref_map) for item in value]
        result: list[Any] = []
        for item in rewritten:
            if item not in result:
                result.append(item)
        return result
    if isinstance(value, dict):
        return {key: _rewrite_refs(item, ref_map) for key, item in value.items()}
    return value


def _merge_collection(
    target_items: list[dict[str, Any]],
    source_items: list[dict[str, Any]],
    id_key: str,
    natural_key: Callable[[dict[str, Any]], Any],
    ref_map: dict[str, str],
) -> None:
    by_id = {item[id_key]: item for item in target_items}
    by_natural = {natural_key(item): item for item in target_items}
    for original in source_items:
        item = _rewrite_refs(copy.deepcopy(original), ref_map)
        existing = by_id.get(item[id_key]) or by_natural.get(natural_key(item))
        if existing is not None:
            merge_record(existing, item)
            continue
        target_items.append(item)
        by_id[item[id_key]] = item
        by_natural[natural_key(item)] = item


def merge_profiles(
    target: dict[str, Any], source: dict[str, Any], source_slug: str
) -> dict[str, Any]:
    """Merge unique structured intelligence into the canonical actor profile."""
    result = copy.deepcopy(target)
    ref_map = {
        source["profile_id"]: result["profile_id"],
    }

    source_by_key = {_source_key(item): item for item in result.get("sources", [])}
    source_ids = {item["source_id"]: item for item in result.get("sources", [])}
    for item in source.get("sources", []):
        existing = source_ids.get(item["source_id"]) or source_by_key.get(
            _source_key(item)
        )
        if existing is not None:
            ref_map[item["source_id"]] = existing["source_id"]
        else:
            ref_map[item["source_id"]] = item["source_id"]
            copied = copy.deepcopy(item)
            result["sources"].append(copied)
            source_ids[copied["source_id"]] = copied
            source_by_key[_source_key(copied)] = copied

    for category in result["capabilities"]:
        if not isinstance(result["capabilities"][category], list):
            continue
        _map_collection(
            result["capabilities"][category],
            source["capabilities"].get(category, []),
            "id",
            lambda item: normalized_name(item.get("name", item["id"])),
            ref_map,
        )
    for category in ("countries", "regions", "sectors", "roles"):
        _map_collection(
            result["targets"][category],
            source["targets"].get(category, []),
            "id",
            lambda item: normalized_name(item.get("name", item["id"])),
            ref_map,
        )
    _map_collection(
        result["activities"], source["activities"], "activity_id",
        lambda item: normalized_name(item.get("name", item["activity_id"])), ref_map,
    )
    _map_collection(
        result["victim_cases"], source["victim_cases"], "victim_case_id",
        lambda item: normalized_name(
            item.get("victim_name") or item.get("name", item["victim_case_id"])
        ), ref_map,
    )
    _map_collection(
        result["ttps"], source["ttps"], "ttp_id",
        lambda item: (
            item.get("technique_id", ""),
            normalized_name(item.get("observed_behavior", "")),
            tuple(sorted(ref_map.get(ref, ref) for ref in item.get("activity_refs", []))),
        ), ref_map,
    )

    for category in result["capabilities"]:
        if not isinstance(result["capabilities"][category], list):
            continue
        _merge_collection(
            result["capabilities"][category],
            source["capabilities"].get(category, []),
            "id",
            lambda item: normalized_name(item.get("name", item["id"])),
            ref_map,
        )
    for category in ("countries", "regions", "sectors", "roles"):
        _merge_collection(
            result["targets"][category],
            source["targets"].get(category, []),
            "id",
            lambda item: normalized_name(item.get("name", item["id"])),
            ref_map,
        )
    _merge_collection(
        result["activities"], source["activities"], "activity_id",
        lambda item: normalized_name(item.get("name", item["activity_id"])), ref_map,
    )
    _merge_collection(
        result["victim_cases"], source["victim_cases"], "victim_case_id",
        lambda item: normalized_name(
            item.get("victim_name") or item.get("name", item["victim_case_id"])
        ), ref_map,
    )
    _merge_collection(
        result["ttps"], source["ttps"], "ttp_id",
        lambda item: (
            item.get("technique_id", ""),
            normalized_name(item.get("observed_behavior", "")),
            tuple(sorted(item.get("activity_refs", []))),
        ), ref_map,
    )

    source_names = {
        normalized_name(source["name"]),
        normalized_name(source["actor"]["canonical_name"]),
    }
    kept_relationships = [
        item for item in result.get("relationships", [])
        if normalized_name(item.get("target_actor", "")) not in source_names
    ]
    source_relationships = [
        item for item in source.get("relationships", [])
        if normalized_name(item.get("target_actor", ""))
        not in source_names | {normalized_name(result["name"])}
    ]
    _merge_collection(
        kept_relationships, source_relationships, "relationship_id",
        lambda item: (
            normalized_name(item.get("target_actor", "")),
            item.get("relationship_type", ""),
        ), ref_map,
    )
    result["relationships"] = kept_relationships

    result["languages"] = _merge_scalar_lists(
        result.get("languages", []), source.get("languages", [])
    )
    result["motivations"] = _merge_scalar_lists(
        result.get("motivations", []),
        _rewrite_refs(source.get("motivations", []), ref_map),
    )
    merge_record(
        result["attribution"], _rewrite_refs(source.get("attribution", {}), ref_map)
    )
    for key in ("capability", "infrastructure", "victim", "socio_political"):
        old = source.get("diamond_model", {}).get(key, "")
        if old and old not in result["diamond_model"].get(key, ""):
            current = result["diamond_model"].get(key, "")
            result["diamond_model"][key] = "; ".join(x for x in (current, old) if x)

    alias_name = source["actor"]["canonical_name"]
    aliases = result["actor"].setdefault("aliases", [])
    alias = next(
        (item for item in aliases if normalized_name(item["name"]) == normalized_name(alias_name)),
        None,
    )
    if alias is None:
        aliases.append(
            {
                "name": alias_name,
                "vendor": "MITRE ATT&CK / Microsoft",
                "scope": "exact",
                "confidence": "high",
                "evidence_refs": ["source--mitre-attack-19-1"],
                "analyst_notes": "Curated merge into the canonical MITRE Group profile.",
            }
        )
    else:
        alias["scope"] = "exact"
        alias["confidence"] = "high"
        alias["vendor"] = "MITRE ATT&CK / Microsoft"
        alias["evidence_refs"] = _merge_scalar_lists(
            alias.get("evidence_refs", []), ["source--mitre-attack-19-1"]
        )
        alias["analyst_notes"] = "Curated merge into the canonical MITRE Group profile."

    note = (
        f"2026-09 entity-boundary migration: actor--{source_slug} was merged into "
        f"{result['profile_id']} after official same-Group alias verification."
    )
    existing_note = result["actor"].get("analyst_notes", "")
    if note not in existing_note:
        result["actor"]["analyst_notes"] = " ".join(
            part for part in (existing_note, note) if part
        )
    result["updated_at"] = utc_now()
    materialize_profile_diamonds(result)
    return result


def deprecated_profile(
    profile: dict[str, Any], *, target: dict[str, Any] | None = None
) -> dict[str, Any]:
    result = copy.deepcopy(profile)
    is_software = target is None
    target_text = (
        "APT28/Sednit; Zebrocy remains a malware entity (MITRE Software S0251)"
        if is_software
        else f"{target['actor']['canonical_name']} ({target['profile_id']})"
    )
    result["status"] = "deprecated"
    result["updated_at"] = utc_now()
    result["actor"]["aliases"] = []
    result["actor"]["description"] = (
        f"Deprecated legacy profile. {result['actor']['canonical_name']} is "
        f"represented by {target_text}. Retained only for stable legacy references."
    )
    result["actor"]["analyst_notes"] = (
        "Removed from the active corpus catalog by actor-census-curation.json."
    )
    result["attribution"] = {
        "countries": [], "sponsor_type": "unknown", "organizations": [],
        "assessment": "", "confidence": "unknown", "evidence_refs": [],
        "analyst_notes": "",
    }
    result["motivations"] = []
    result["relationships"] = []
    result["diamond_model"] = {
        "adversary": "", "capability": "", "infrastructure": "", "victim": "",
        "socio_political": "", "analyst_notes": "Deprecated legacy profile.",
    }
    for key, value in result["capabilities"].items():
        if isinstance(value, list):
            result["capabilities"][key] = []
    result["activities"] = []
    for category in ("countries", "regions", "sectors", "roles"):
        result["targets"][category] = []
    result["targets"]["selection_logic"] = ""
    result["targets"]["analyst_notes"] = ""
    result["ttps"] = []
    result["victim_cases"] = []
    evidence_refs = ["source--mitre-attack-19-1"]
    if is_software:
        mitre_source = {
            "source_id": "source--mitre-zebrocy-s0251",
            "path": EVIDENCE_URLS["zebrocy"],
            "url": EVIDENCE_URLS["zebrocy"],
            "title": "Zebrocy, Software S0251",
            "publisher": "MITRE ATT&CK",
            "published_at": {
                "value": None,
                "precision": "unknown",
                "status": "unknown",
                "basis": "not-stated",
            },
            "language": "en",
            "source_type": "structured-knowledge-base",
            "tlp": "TLP:CLEAR",
            "reliability": "high",
            "sha256": None,
            "analyst_notes": (
                "Primary entity-type evidence: MITRE classifies Zebrocy as "
                "software used by APT28."
            ),
        }
        eset_source = {
            "source_id": "source--eset-zebrocy-2018",
            "path": (
                "https://www.welivesecurity.com/2018/11/20/"
                "sednit-whats-going-zebrocy/"
            ),
            "url": (
                "https://www.welivesecurity.com/2018/11/20/"
                "sednit-whats-going-zebrocy/"
            ),
            "title": "Sednit: What's going on with Zebrocy?",
            "publisher": "ESET",
            "published_at": {
                "value": "2018-11-20T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-publication",
            },
            "language": "en",
            "source_type": "vendor-threat-research",
            "tlp": "TLP:CLEAR",
            "reliability": "high",
            "sha256": None,
            "analyst_notes": (
                "Primary actor-scoping evidence: ESET describes Zebrocy as a "
                "toolset operated by the Sednit group."
            ),
        }
        existing_source_ids = {item["source_id"] for item in result["sources"]}
        for item in (mitre_source, eset_source):
            if item["source_id"] not in existing_source_ids:
                result["sources"].append(item)
        evidence_refs = [mitre_source["source_id"], eset_source["source_id"]]
    statement = (
        "Zebrocy is malware used by APT28/Sednit, not a canonical threat actor."
        if is_software
        else f"This profile is an exact-identity duplicate of {target_text}."
    )
    result["assessment"] = {
        "key_judgments": [
            {
                "statement": statement,
                "confidence": "high",
                "evidence_refs": evidence_refs,
                "analyst_notes": "Entity-boundary correction.",
            }
        ],
        "gaps": [],
        "uncertainties": [],
        "collection_notes": "Legacy evidence remains on disk for provenance.",
        "analyst_notes": "",
    }
    return result


def merge_daily_observations(target_path: Path, source_path: Path, ref_map: dict[str, str]) -> None:
    if not source_path.exists():
        return
    source = load_json(source_path)
    target = load_json(target_path) if target_path.exists() else {
        "schema_version": source["schema_version"],
        "actor_ref": ref_map[source["actor_ref"]],
        "updated_at": utc_now(),
        "records": [],
    }
    titles = {
        normalized_name(item.get("activity", {}).get("title", ""))
        for item in target["records"]
    }
    for record in source["records"]:
        title = normalized_name(record.get("activity", {}).get("title", ""))
        if title and title in titles:
            continue
        target["records"].append(_rewrite_refs(record, ref_map))
        titles.add(title)
    target["actor_ref"] = ref_map.get(target["actor_ref"], target["actor_ref"])
    target["updated_at"] = utc_now()
    write_json_atomic(target_path, target)


def migrate_review_decisions(path: Path) -> int:
    data = load_json(path)
    changed = 0
    for source_slug, target_slug in MERGES.items():
        for key in list(data):
            prefix = f"{source_slug}|"
            if not key.startswith(prefix):
                continue
            replacement = f"{target_slug}|{key[len(prefix):]}"
            if replacement not in data:
                data[replacement] = data[key]
            del data[key]
            changed += 1
    if changed:
        write_json_atomic(path, data)
    return changed


def migrate_inbound_relationships(root: Path) -> int:
    """Retarget relationships that still name a merged legacy identity."""
    canonical_names = {
        source_slug: load_json(
            root / "profiles" / target_slug / "actor-profile.json"
        )["actor"]["canonical_name"]
        for source_slug, target_slug in MERGES.items()
    }
    legacy_names = {
        load_json(root / "profiles" / source_slug / "actor-profile.json")["actor"][
            "canonical_name"
        ]: (source_slug, canonical_names[source_slug])
        for source_slug in MERGES
    }
    changed = 0
    for path in sorted((root / "profiles").glob("*/actor-profile.json")):
        profile = load_json(path)
        if profile.get("status") == "deprecated":
            continue
        profile_changed = False
        for relationship in profile.get("relationships", []):
            legacy_name = relationship.get("target_actor", "")
            match = legacy_names.get(legacy_name)
            if match is None:
                continue
            source_slug, canonical_name = match
            relationship["target_actor"] = canonical_name
            legacy_ref = f"actor--{source_slug}"
            if relationship.get("target_actor_ref") == legacy_ref:
                relationship["target_actor_ref"] = f"actor--{MERGES[source_slug]}"
            # Keep the migration note specific and idempotent without changing
            # the original overlap assessment or confidence.
            note = (
                f"Entity-boundary migration: target renamed from {legacy_name} "
                f"to {canonical_name}."
            )
            existing_note = relationship.get("analyst_notes", "")
            if note not in existing_note:
                relationship["analyst_notes"] = " ".join(
                    part for part in (existing_note, note) if part
                )
            profile_changed = True
        if profile_changed:
            profile["updated_at"] = utc_now()
            write_json_atomic(path, profile)
            changed += 1
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.repository_root.resolve()
    changed: list[str] = []

    for source_slug, target_slug in MERGES.items():
        source_path = root / "profiles" / source_slug / "actor-profile.json"
        target_path = root / "profiles" / target_slug / "actor-profile.json"
        source = load_json(source_path)
        target = load_json(target_path)
        if source.get("status") == "deprecated":
            continue
        merged = merge_profiles(target, source, source_slug)
        deprecated = deprecated_profile(source, target=merged)
        if merged != target or deprecated != source:
            changed.extend([source_slug, target_slug])
            if args.apply:
                write_json_atomic(target_path, merged)
                write_json_atomic(source_path, deprecated)
                merge_daily_observations(
                    target_path.parent / "daily-observations.json",
                    source_path.parent / "daily-observations.json",
                    {
                        source["profile_id"]: merged["profile_id"],
                        source_slug: target_slug,
                        source["actor"]["canonical_name"]: merged["actor"]["canonical_name"],
                    },
                )

    for slug in EXCLUSIONS:
        path = root / "profiles" / slug / "actor-profile.json"
        profile = load_json(path)
        if profile.get("status") == "deprecated":
            continue
        deprecated = deprecated_profile(profile)
        if deprecated != profile:
            changed.append(slug)
            if args.apply:
                write_json_atomic(path, deprecated)

    decision_changes = 0
    inbound_relationship_changes = 0
    if args.apply:
        decision_changes = migrate_review_decisions(
            root / "parse-daily" / "review-decisions.json"
        )
        inbound_relationship_changes = migrate_inbound_relationships(root)
    print(
        json.dumps(
            {
                "mode": "apply" if args.apply else "dry-run",
                "profiles_changed": sorted(set(changed)),
                "review_decisions_rekeyed": decision_changes,
                "inbound_relationship_profiles_changed": inbound_relationship_changes,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
