#!/usr/bin/env python3
"""Materialize census identities as catalog entries and actor-scoped evidence.

Only evidence windows already associated with an identity are placed in that
identity's ingestion source.  This avoids assigning every IOC in a broad annual
report to every actor merely mentioned by that report.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import normalized_name
from common import load_json, slugify, stable_digest, utc_now, write_json_atomic


VALID_DISCOVERED_ID = re.compile(
    r"^(?:APT[- ]?\d{1,3}|UNC\d{3,4}|UNG\d{3,4}|UTG\d{3,4}|"
    r"FIN\d{1,4}|TA\d{3,4}|UAC-\d{4}|DEV-\d{4}|TAG-\d{2,4}|"
    r"Storm-\d{4}|CL-STA-\d{4})$",
    re.IGNORECASE,
)
COUNTRY_ORIGINS = {
    "china", "russia", "north korea", "iran", "israel", "vietnam",
    "india", "pakistan", "ukraine", "belarus", "turkey", "syria",
    "lebanon", "palestine",
}


def normalized_unique_names(names: list[str]) -> list[str]:
    """Deduplicate display variants while preserving the first sourced spelling."""
    result: list[str] = []
    seen: set[str] = set()
    for name in names:
        key = normalized_name(name)
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(name)
    return result


def merge_identity_group(items: list[dict[str, Any]]) -> dict[str, Any]:
    preferred = next((item for item in items if item.get("mitre_group_id")), items[0])
    result = {
        "actor_ids": [],
        "canonical_name": preferred["canonical_name"],
        "aliases": [],
        "mitre_group_id": preferred.get("mitre_group_id"),
        "origins": [],
        "reference_evidence": [],
        "mentions": [],
    }
    seen_mentions: set[str] = set()
    ordered_items = [preferred, *(item for item in items if item is not preferred)]
    for item in ordered_items:
        result["actor_ids"].append(item["actor_id"])
        result["aliases"].extend(item.get("aliases", []))
        result["origins"].extend(item.get("origins", []))
        result["reference_evidence"].extend(item.get("reference_evidence", []))
        for mention in item.get("mentions", []):
            key = json.dumps(mention, sort_keys=True, ensure_ascii=False)
            if key not in seen_mentions:
                seen_mentions.add(key)
                result["mentions"].append(mention)
    for key in ("actor_ids", "origins"):
        result[key] = list(dict.fromkeys(result[key]))
    result["aliases"] = normalized_unique_names(result["aliases"])
    result["reference_evidence"] = list(
        {
            json.dumps(item, sort_keys=True, ensure_ascii=False): item
            for item in result["reference_evidence"]
        }.values()
    )
    result["mentions"].sort(
        key=lambda item: (
            item["source_path"],
            json.dumps(item["source_location"], sort_keys=True),
            item["matched_name"],
        )
    )
    return result


def actor_types(origins: list[str]) -> list[str]:
    """Return evidence-neutral actor types for census-generated entries.

    ``origins`` may contain country or regional labels from source organization,
    workbook placement, or collection context. Those labels are useful leads,
    but they do not establish government sponsorship or control. Census
    materialization therefore keeps the generated entry neutral. Supported
    actor types are added later from actor-specific evidence.
    """
    _ = origins
    return ["threat-cluster"]


def unique_slug(name: str, mitre_id: str | None, used: set[str]) -> str:
    base = slugify(name) or "unnamed-actor"
    if base not in used:
        used.add(base)
        return base
    suffix = mitre_id.casefold() if mitre_id else stable_digest(name)[:8]
    candidate = f"{base}-{suffix}"
    counter = 2
    while candidate in used:
        candidate = f"{base}-{suffix}-{counter}"
        counter += 1
    used.add(candidate)
    return candidate


def identity_curation_rule(curation: dict[str, Any], canonical_name: str) -> dict[str, Any]:
    """Return an analyst curation rule for a census identity, if present."""
    return curation.get("identities", {}).get(normalized_name(canonical_name), {})


def has_trusted_attack_reference(item: dict[str, Any]) -> bool:
    """Return whether a reference-only identity has an official ATT&CK anchor."""
    return any(
        str(ref.get("source", "")).startswith("MITRE ") and ref.get("external_id")
        for ref in item.get("reference_evidence", [])
    )


def write_evidence_csv(
    path: Path,
    mentions: list[dict[str, Any]],
    *,
    lineterminator: str = "\n",
) -> None:
    """Write one deterministic actor-scoped evidence window."""
    with path.open("w", encoding="utf-8", newline="") as stream:
        options: dict[str, Any] = {
            "fieldnames": [
                "original_source_path",
                "original_source_location",
                "matched_name",
                "context_excerpt",
            ]
        }
        options["lineterminator"] = lineterminator
        writer = csv.DictWriter(stream, **options)
        writer.writeheader()
        for mention in mentions:
            writer.writerow(
                {
                    "original_source_path": mention["source_path"],
                    "original_source_location": json.dumps(
                        mention["source_location"],
                        ensure_ascii=False,
                        sort_keys=True,
                    ),
                    "matched_name": mention["matched_name"],
                    "context_excerpt": mention["context_excerpt"],
                }
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--census", type=Path, default=Path("actor_profile/actor-census.json")
    )
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
    )
    parser.add_argument(
        "--evidence-root", type=Path, default=Path("actor_profile/evidence")
    )
    parser.add_argument(
        "--decision-log",
        type=Path,
        default=Path("actor_profile/actor-census-decisions.json"),
    )
    parser.add_argument(
        "--curation",
        type=Path,
        default=Path("actor_profile/actor-census-curation.json"),
    )
    args = parser.parse_args()

    root = args.repository_root.resolve()
    census = load_json((root / args.census).resolve())
    curation_path = (root / args.curation).resolve()
    curation = load_json(curation_path) if curation_path.exists() else {"identities": {}}
    catalog_path = (root / args.catalog).resolve()
    catalog = load_json(catalog_path)
    # Rebuild generated census entries deterministically on repeated runs.
    catalog["actors"] = [
        item
        for item in catalog["actors"]
        if item.get("profile_basis")
        not in {"actor-scoped-census-evidence", "official-attack-reference"}
    ]
    existing_slugs = {item["slug"] for item in catalog["actors"]}
    used_slugs = set(existing_slugs)

    accepted_raw: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    represented: list[dict[str, Any]] = []
    curated_merges: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for item in census["actors"]:
        rule = identity_curation_rule(curation, item["canonical_name"])
        if rule.get("action") == "exclude":
            rejected.append(
                {
                    "actor_id": item["actor_id"],
                    "canonical_name": item["canonical_name"],
                    "reason": "curated-non-actor-entity",
                    "curation_reason": rule.get("reason", ""),
                    "evidence_urls": rule.get("evidence_urls", []),
                }
            )
            continue
        if rule.get("action") == "merge":
            curated_merges.append((item, rule))
            represented.append(
                {
                    "actor_id": item["actor_id"],
                    "canonical_name": item["canonical_name"],
                    "catalog_slugs": [rule["target_slug"]],
                    "reason": "curated-merge-into-existing-profile",
                    "curation_reason": rule.get("reason", ""),
                    "evidence_urls": rule.get("evidence_urls", []),
                }
            )
            continue
        if item.get("catalog_slugs"):
            represented.append(
                {
                    "actor_id": item["actor_id"],
                    "canonical_name": item["canonical_name"],
                    "catalog_slugs": item["catalog_slugs"],
                    "reason": "represented-by-existing-profile",
                }
            )
            continue
        if not item.get("mentions"):
            if not has_trusted_attack_reference(item):
                rejected.append(
                    {
                        "actor_id": item["actor_id"],
                        "canonical_name": item["canonical_name"],
                        "reason": "reference-only-no-corpus-mention",
                    }
                )
                continue
        sources = {ref["source"] for ref in item.get("reference_evidence", [])}
        if sources == {"corpus-pattern-discovery"} and not VALID_DISCOVERED_ID.fullmatch(
            item["canonical_name"]
        ):
            rejected.append(
                {
                    "actor_id": item["actor_id"],
                    "canonical_name": item["canonical_name"],
                    "reason": "malformed-or-implausible-discovered-id",
                }
            )
            continue
        accepted_raw.append(item)

    by_name: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in accepted_raw:
        by_name[normalized_name(item["canonical_name"])].append(item)
    accepted = [
        merge_identity_group(items)
        for _, items in sorted(by_name.items(), key=lambda pair: pair[0])
    ]

    evidence_root = (root / args.evidence_root).resolve()
    evidence_root.mkdir(parents=True, exist_ok=True)
    added_entries: list[dict[str, Any]] = []
    for item in accepted:
        rule = identity_curation_rule(curation, item["canonical_name"])
        original_canonical_name = item["canonical_name"]
        canonical_name = rule.get("canonical_name", original_canonical_name)
        if rule.get("slug"):
            slug = rule["slug"]
            if slug in used_slugs:
                raise ValueError(f"curated slug already exists: {slug}")
            used_slugs.add(slug)
        else:
            slug = unique_slug(canonical_name, item.get("mitre_group_id"), used_slugs)
        relative_evidence = (Path(args.evidence_root) / f"{slug}.csv").as_posix()
        source_dirs: list[str] = []
        if item["mentions"]:
            evidence_path = root / relative_evidence
            write_evidence_csv(evidence_path, item["mentions"])
            source_dirs.append(relative_evidence)
        original_sources = sorted(
            {mention["source_path"] for mention in item["mentions"]}
        )
        aliases = normalized_unique_names([
            alias
            for alias in item["aliases"]
            if normalized_name(alias) != normalized_name(original_canonical_name)
        ])
        if "aliases" in rule:
            aliases = normalized_unique_names(list(rule["aliases"]))
        elif canonical_name != original_canonical_name:
            aliases = list(dict.fromkeys([original_canonical_name, *aliases]))
        entry = {
            "slug": slug,
            "name": canonical_name,
            "aliases": aliases,
            "source_dirs": source_dirs,
            "reported_sources": original_sources,
            "census_actor_ids": item["actor_ids"],
            "actor_types": rule.get("actor_types", actor_types(item["origins"])),
            "profile_basis": (
                "actor-scoped-census-evidence"
                if item["mentions"]
                else "official-attack-reference"
            ),
        }
        if rule:
            entry["curation"] = {
                "reason": rule.get("reason", ""),
                "evidence_urls": rule.get("evidence_urls", []),
            }
        if item.get("mitre_group_id"):
            entry["mitre_group_id"] = item["mitre_group_id"]
        added_entries.append(entry)

    catalog["actors"].extend(added_entries)
    entries_by_slug = {entry["slug"]: entry for entry in catalog["actors"]}
    for item, rule in curated_merges:
        target_slug = rule["target_slug"]
        target = entries_by_slug.get(target_slug)
        if target is None:
            raise ValueError(
                f"curated merge target is not an active catalog entry: {target_slug}"
            )
        evidence_name = (
            f"{target_slug}--merged--"
            f"{stable_digest(normalized_name(item['canonical_name']))[:12]}.csv"
        )
        relative_evidence = (Path(args.evidence_root) / evidence_name).as_posix()
        write_evidence_csv(
            root / relative_evidence,
            item.get("mentions", []),
            lineterminator="\n",
        )
        target["source_dirs"] = list(
            dict.fromkeys([*target.get("source_dirs", []), relative_evidence])
        )
        target["reported_sources"] = sorted(
            set(target.get("reported_sources", []))
            | {mention["source_path"] for mention in item.get("mentions", [])}
        )
        target["census_actor_ids"] = list(
            dict.fromkeys(
                [*target.get("census_actor_ids", []), item["actor_id"]]
            )
        )
        # The census can contain aggregation aliases whose scope has not been
        # reviewed.  Do not promote those into the canonical catalog entry.
        # Start from the target profile's evidence-scoped aliases and add only
        # the curated merge identity itself.
        profile_path = root / "profiles" / target_slug / "actor-profile.json"
        reviewed_aliases = target.get("aliases", [])
        if profile_path.is_file():
            target_profile = load_json(profile_path)
            reviewed_aliases = [
                alias["name"] for alias in target_profile["actor"].get("aliases", [])
            ]
        merged_names = [item["canonical_name"]]
        target["aliases"] = list(
            dict.fromkeys(
                [
                    *reviewed_aliases,
                    *(
                        name
                        for name in merged_names
                        if normalized_name(name) != normalized_name(target["name"])
                    ),
                ]
            )
        )
    catalog["actors"].sort(key=lambda item: item["slug"])
    catalog["description"] = (
        "Corpus catalog covering every evidence-backed actor identity named in "
        "the report corpus plus current official ATT&CK Groups. Actor-scoped "
        "evidence files prevent broad multi-actor reports from contaminating "
        "IOC attribution; reference-only ATT&CK entries remain explicitly marked."
    )
    write_json_atomic(catalog_path, catalog)
    decisions = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "counts": {
            "census_identities": len(census["actors"]),
            "existing_profile_identities": len(represented),
            "new_profile_entries": len(added_entries),
            "rejected_candidates": len(rejected),
            "catalog_actor_count": len(catalog["actors"]),
        },
        "policy": {
            "exact_canonical_name_duplicates": "merged",
            "cross_vendor_alias_overlap": "kept as separate identities unless already represented",
            "pattern_only_ids": VALID_DISCOVERED_ID.pattern,
            "ioc_scope": "actor-associated context excerpts only",
            "curation_file": str(args.curation),
            "curation_precedence": "analyst curation overrides automatic census materialization",
        },
        "represented": represented,
        "rejected": rejected,
        "added": [
            {
                "slug": entry["slug"],
                "name": entry["name"],
                "census_actor_ids": entry["census_actor_ids"],
                "reported_source_count": len(entry["reported_sources"]),
                "evidence_path": (
                    entry["source_dirs"][0] if entry["source_dirs"] else None
                ),
                "profile_basis": entry["profile_basis"],
            }
            for entry in added_entries
        ],
    }
    write_json_atomic((root / args.decision_log).resolve(), decisions)
    print(json.dumps(decisions["counts"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
