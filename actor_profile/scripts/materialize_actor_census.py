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
    for item in items:
        result["actor_ids"].append(item["actor_id"])
        result["aliases"].extend(item.get("aliases", []))
        result["origins"].extend(item.get("origins", []))
        result["reference_evidence"].extend(item.get("reference_evidence", []))
        for mention in item.get("mentions", []):
            key = json.dumps(mention, sort_keys=True, ensure_ascii=False)
            if key not in seen_mentions:
                seen_mentions.add(key)
                result["mentions"].append(mention)
    for key in ("actor_ids", "aliases", "origins"):
        result[key] = list(dict.fromkeys(result[key]))
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
    if any(origin.casefold() in COUNTRY_ORIGINS for origin in origins):
        return ["state-sponsored", "threat-cluster"]
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
    args = parser.parse_args()

    root = args.repository_root.resolve()
    census = load_json((root / args.census).resolve())
    catalog_path = (root / args.catalog).resolve()
    catalog = load_json(catalog_path)
    # Rebuild generated census entries deterministically on repeated runs.
    catalog["actors"] = [
        item
        for item in catalog["actors"]
        if item.get("profile_basis") != "actor-scoped-census-evidence"
    ]
    existing_slugs = {item["slug"] for item in catalog["actors"]}
    used_slugs = set(existing_slugs)

    accepted_raw: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    represented: list[dict[str, Any]] = []
    for item in census["actors"]:
        if not item.get("mentions"):
            rejected.append(
                {
                    "actor_id": item["actor_id"],
                    "canonical_name": item["canonical_name"],
                    "reason": "reference-only-no-corpus-mention",
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
        slug = unique_slug(item["canonical_name"], item.get("mitre_group_id"), used_slugs)
        relative_evidence = (Path(args.evidence_root) / f"{slug}.csv").as_posix()
        evidence_path = root / relative_evidence
        with evidence_path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(
                stream,
                fieldnames=[
                    "original_source_path",
                    "original_source_location",
                    "matched_name",
                    "context_excerpt",
                ],
            )
            writer.writeheader()
            for mention in item["mentions"]:
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
        original_sources = sorted(
            {mention["source_path"] for mention in item["mentions"]}
        )
        aliases = [
            alias
            for alias in item["aliases"]
            if normalized_name(alias) != normalized_name(item["canonical_name"])
        ]
        entry = {
            "slug": slug,
            "name": item["canonical_name"],
            "aliases": aliases,
            "source_dirs": [relative_evidence],
            "reported_sources": original_sources,
            "census_actor_ids": item["actor_ids"],
            "actor_types": actor_types(item["origins"]),
            "profile_basis": "actor-scoped-census-evidence",
        }
        if item.get("mitre_group_id"):
            entry["mitre_group_id"] = item["mitre_group_id"]
        added_entries.append(entry)

    catalog["actors"].extend(added_entries)
    catalog["actors"].sort(key=lambda item: item["slug"])
    catalog["description"] = (
        "Corpus catalog covering every evidence-backed actor identity named in "
        "the original report corpus. Actor-scoped evidence files prevent broad "
        "multi-actor reports from contaminating IOC attribution."
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
        },
        "represented": represented,
        "rejected": rejected,
        "added": [
            {
                "slug": entry["slug"],
                "name": entry["name"],
                "census_actor_ids": entry["census_actor_ids"],
                "reported_source_count": len(entry["reported_sources"]),
                "evidence_path": entry["source_dirs"][0],
            }
            for entry in added_entries
        ],
    }
    write_json_atomic((root / args.decision_log).resolve(), decisions)
    print(json.dumps(decisions["counts"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
