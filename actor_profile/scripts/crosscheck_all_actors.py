#!/usr/bin/env python3
"""Cross-check every actor against versioned public OSINT datasets.

This script deliberately separates three concepts:

* an actor/profile identity match;
* a candidate alias or relationship found in an aggregation dataset; and
* a malware name existing in Malpedia.

The latter two are leads, not proof of exact identity or actor use.  Every
profile receives an ``osint-crosscheck.json`` file, including profiles for
which no external match is found.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import normalized_name
from common import load_json, normalize_time, stable_id, utc_now, write_json_atomic


DATASETS = {
    "etda-threat-group-cards": {
        "path": "actor_profile/reference/osint/etda-threat-group-cards.json",
        "title": "Threat Group Cards: A Threat Actor Encyclopedia",
        "publisher": "ETDA / ThaiCERT",
        "url": "https://apt.etda.or.th/cgi-bin/listgroups.cgi",
        "reliability": "medium",
        "kind": "actor",
        "format": "etda-cards",
    },
    "cert-ua-uac-index": {
        "path": "actor_profile/reference/osint/cert-ua-uac-index.json",
        "title": "CERT-UA UAC Article Index",
        "publisher": "CERT-UA",
        "url": "https://cert.gov.ua/articles",
        "reliability": "high",
        "kind": "actor",
    },
    "microsoft-threat-actor-mapping": {
        "path": "actor_profile/reference/osint/microsoft-threat-actor-mapping.json",
        "title": "Microsoft Threat Actor Naming Mapping",
        "publisher": "Microsoft",
        "url": "https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json",
        "reliability": "high",
        "kind": "actor",
        "format": "microsoft-mapping",
    },
    "misp-threat-actor": {
        "path": "actor_profile/reference/osint/misp-threat-actor.json",
        "title": "MISP Galaxy Threat Actor",
        "publisher": "MISP Project",
        "url": "https://github.com/MISP/misp-galaxy/blob/main/clusters/threat-actor.json",
        "reliability": "medium",
        "kind": "actor",
    },
    "misp-microsoft-activity-group": {
        "path": "actor_profile/reference/osint/misp-microsoft-activity-group.json",
        "title": "MISP Galaxy Microsoft Activity Group",
        "publisher": "MISP Project / Microsoft",
        "url": "https://github.com/MISP/misp-galaxy/blob/main/clusters/microsoft-activity-group.json",
        "reliability": "high",
        "kind": "actor",
    },
    "misp-mitre-enterprise-intrusion-set": {
        "path": "actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json",
        "title": "MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set",
        "publisher": "MISP Project / MITRE ATT&CK",
        "url": "https://github.com/MISP/misp-galaxy/blob/main/clusters/mitre-enterprise-attack-intrusion-set.json",
        "reliability": "high",
        "kind": "actor",
    },
    "misp-mitre-intrusion-set": {
        "path": "actor_profile/reference/osint/misp-mitre-intrusion-set.json",
        "title": "MISP Galaxy MITRE Intrusion Set",
        "publisher": "MISP Project / MITRE ATT&CK",
        "url": "https://github.com/MISP/misp-galaxy/blob/main/clusters/mitre-intrusion-set.json",
        "reliability": "high",
        "kind": "actor",
    },
    "misp-360net": {
        "path": "actor_profile/reference/osint/misp-360net.json",
        "title": "MISP Galaxy 360.net Threat Actors",
        "publisher": "MISP Project / 360 Netlab",
        "url": "https://github.com/MISP/misp-galaxy/blob/main/clusters/360net.json",
        "reliability": "medium",
        "kind": "actor",
    },
    "misp-malpedia": {
        "path": "actor_profile/reference/osint/misp-malpedia.json",
        "title": "MISP Galaxy Malpedia",
        "publisher": "MISP Project / Fraunhofer FKIE",
        "url": "https://github.com/MISP/misp-galaxy/blob/main/clusters/malpedia.json",
        "reliability": "medium",
        "kind": "malware",
    },
}


COUNTRY_EQUIVALENTS = {
    "cn": "china",
    "china": "china",
    "prc": "china",
    "ru": "russia",
    "russia": "russia",
    "russianfederation": "russia",
    "kp": "northkorea",
    "northkorea": "northkorea",
    "dprk": "northkorea",
    "ir": "iran",
    "iran": "iran",
    "islamicrepublicofiran": "iran",
    "vn": "vietnam",
    "vietnam": "vietnam",
    "in": "india",
    "india": "india",
    "pk": "pakistan",
    "pakistan": "pakistan",
    "us": "unitedstates",
    "usa": "unitedstates",
    "unitedstates": "unitedstates",
    "unitedstatesofamerica": "unitedstates",
    "tr": "turkey",
    "turkiye": "turkey",
    "turkey": "turkey",
    "lb": "lebanon",
    "lebanon": "lebanon",
    "ps": "palestine",
    "palestine": "palestine",
    "il": "israel",
    "israel": "israel",
    "kr": "southkorea",
    "southkorea": "southkorea",
    "tw": "taiwan",
    "taiwan": "taiwan",
    "sy": "syria",
    "syria": "syria",
    "by": "belarus",
    "belarus": "belarus",
    "ua": "ukraine",
    "ukraine": "ukraine",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean_actor_value(value: str) -> str:
    """Remove the MITRE suffix used by some MISP cluster values."""
    return re.sub(r"\s*-\s*G\d{4,5}\s*$", "", value).strip()


def names_for_entry(entry: dict[str, Any]) -> list[str]:
    values = [clean_actor_value(str(entry.get("value", "")))]
    meta = entry.get("meta", {})
    values.extend(str(item) for item in meta.get("synonyms", []) if item)
    return list(dict.fromkeys(item.strip() for item in values if item.strip()))


def country_key(value: str) -> str:
    normalized = normalized_name(value)
    return COUNTRY_EQUIVALENTS.get(normalized, normalized)


def entry_countries(entry: dict[str, Any]) -> list[str]:
    meta = entry.get("meta", {})
    raw: list[str] = []
    for key in ("country", "cfr-suspected-state-sponsor"):
        value = meta.get(key)
        if isinstance(value, list):
            raw.extend(str(item) for item in value)
        elif value:
            raw.append(str(value))
    microsoft_origin = meta.get("microsoft-origin-threat")
    if microsoft_origin:
        values = (
            microsoft_origin
            if isinstance(microsoft_origin, list)
            else [microsoft_origin]
        )
        for value in values:
            # This Microsoft field also contains classifications such as
            # "Financially motivated" and "Group in development".
            if country_key(str(value)) in set(COUNTRY_EQUIVALENTS.values()):
                raw.append(str(value))
    return list(
        dict.fromkeys(
            item
            for item in raw
            if item and normalized_name(item) not in {"mideast", "middleeast"}
        )
    )


def source_object(
    dataset_id: str, descriptor: dict[str, Any], manifest: dict[str, Any]
) -> dict[str, Any]:
    return {
        "source_id": f"source--osint-{dataset_id}",
        "path": descriptor["path"],
        "url": descriptor["url"],
        "title": descriptor["title"],
        "publisher": descriptor["publisher"],
        "published_at": normalize_time(None),
        "accessed_at": manifest["retrieved_at"],
        "language": "en",
        "source_type": (
            "official-vendor-actor-mapping"
            if dataset_id == "microsoft-threat-actor-mapping"
            else "government-cert-article-index"
            if dataset_id == "cert-ua-uac-index"
            else "government-threat-actor-encyclopedia"
            if dataset_id == "etda-threat-group-cards"
            else "structured-osint-aggregation"
        ),
        "tlp": "TLP:CLEAR",
        "reliability": descriptor["reliability"],
        "sha256": manifest["sha256"],
        "actor_scope": "unknown",
        "claims_supported": ["identity-crosscheck", "alias-lead", "relationship-lead"],
        "analyst_notes": (
            f"Dataset version={manifest['version']}. "
            + (
                "This is Microsoft's published mapping; other vendors' "
                "collection boundaries may differ."
                if dataset_id == "microsoft-threat-actor-mapping"
                else "This index is derived from CERT-UA's official article "
                "titles and summaries; open the linked article before extending "
                "the claim beyond the indexed text."
                if dataset_id == "cert-ua-uac-index"
                else "ETDA/ThaiCERT aggregates the cited vendor and government "
                "reporting. Actor scope and attribution must be checked against "
                "the card's original references."
                if dataset_id == "etda-threat-group-cards"
                else "Aggregation match is a cross-check lead; vendor collection "
                "boundaries and original references must be reviewed before "
                "asserting exact identity."
            )
        ),
    }


def normalize_dataset(
    dataset_id: str, descriptor: dict[str, Any], data: Any
) -> dict[str, Any]:
    if descriptor.get("format") == "etda-cards":
        if not isinstance(data, dict):
            raise ValueError(f"{dataset_id}: expected ETDA card object")
        values = []
        for row in data.get("values", []):
            canonical = str(row.get("actor", "")).strip()
            if not canonical:
                continue
            names = [
                str(item.get("name", "")).strip()
                for item in row.get("names", [])
                if isinstance(item, dict) and item.get("name")
            ]
            synonyms = [
                item for item in names if normalized_name(item) != normalized_name(canonical)
            ]
            refs = [
                *[str(item) for item in row.get("information", []) if item],
                *([row["_card_url"]] if row.get("_card_url") else []),
            ]
            values.append(
                {
                    "uuid": row.get("uuid") or stable_id("etda-actor", canonical),
                    "value": canonical,
                    "description": row.get("description", ""),
                    "meta": {
                        "synonyms": list(dict.fromkeys(synonyms)),
                        "country": [
                            item
                            for item in row.get("country", [])
                            if item and item != "[Unknown]"
                        ],
                        "refs": refs,
                        "motivation": row.get("motivation", []),
                        "first-seen": row.get("first-seen"),
                        "observed-sectors": row.get("observed-sectors", []),
                        "observed-countries": row.get("observed-countries", []),
                        "last-card-change": row.get("last-card-change"),
                    },
                }
            )
        return {
            "version": data.get("last-db-change"),
            "values": values,
        }
    if descriptor.get("format") != "microsoft-mapping":
        if not isinstance(data, dict):
            raise ValueError(f"{dataset_id}: expected object dataset")
        return data
    if not isinstance(data, list):
        raise ValueError(f"{dataset_id}: expected Microsoft mapping array")
    values = []
    for index, row in enumerate(data):
        canonical = str(row.get("Threat actor name", "")).strip()
        if not canonical:
            continue
        synonyms = [
            item.strip()
            for item in str(row.get("Other names", "")).split(",")
            if item.strip()
        ]
        values.append(
            {
                "uuid": stable_id("microsoft-actor", canonical),
                "value": canonical,
                "description": (
                    "Microsoft threat actor mapping. Origin/Threat: "
                    + str(row.get("Origin/Threat", ""))
                ),
                "meta": {
                    "synonyms": synonyms,
                    "microsoft-origin-threat": row.get("Origin/Threat", ""),
                    "refs": [descriptor["url"]],
                },
            }
        )
    return {"version": None, "values": values}


def match_actor(
    actor: dict[str, Any],
    profile: dict[str, Any],
    dataset: dict[str, Any],
) -> list[dict[str, Any]]:
    query_names = [actor["name"], *actor.get("aliases", [])]
    query_names.extend(
        item["name"] for item in profile.get("actor", {}).get("aliases", [])
    )
    query_index = {
        normalized_name(item): item
        for item in query_names
        if len(normalized_name(item)) >= 3
    }
    mitre_group_id = actor.get("mitre_group_id")
    matches: list[dict[str, Any]] = []
    for entry in dataset.get("values", []):
        entry_names = names_for_entry(entry)
        entry_index = {
            normalized_name(item): item
            for item in entry_names
            if len(normalized_name(item)) >= 3
        }
        shared = sorted(set(query_index) & set(entry_index))
        external_id = str(entry.get("meta", {}).get("external_id", ""))
        mitre_match = bool(mitre_group_id and external_id == mitre_group_id)
        if not shared and not mitre_match:
            continue
        canonical_key = normalized_name(actor["name"])
        canonical_match = canonical_key in entry_index
        if mitre_match:
            confidence, basis = "high", "mitre-external-id"
        elif canonical_match:
            confidence, basis = "high", "canonical-name"
        elif len(shared) >= 2:
            confidence, basis = "high", "multiple-name-intersection"
        else:
            confidence, basis = "medium", "single-alias-intersection"
        matches.append(
            {
                "entry_uuid": entry.get("uuid"),
                "entry_value": entry.get("value"),
                "external_id": external_id or None,
                "matched_names": [
                    {
                        "normalized": key,
                        "profile_value": query_index[key],
                        "dataset_value": entry_index[key],
                    }
                    for key in shared
                ],
                "match_basis": basis,
                "match_confidence": confidence,
                "candidate_names": entry_names,
                "countries": entry_countries(entry),
                "description": entry.get("description", ""),
                "refs": entry.get("meta", {}).get("refs", []),
                "related": entry.get("related", []),
            }
        )
    return matches


def malware_catalog_matches(
    profile: dict[str, Any], dataset: dict[str, Any]
) -> list[dict[str, Any]]:
    by_name: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in dataset.get("values", []):
        for name in names_for_entry(entry):
            key = normalized_name(name)
            if len(key) >= 4:
                by_name[key].append(entry)
    result: list[dict[str, Any]] = []
    for malware in profile.get("capabilities", {}).get("malware", []):
        names = [malware["name"], *malware.get("aliases", [])]
        found: dict[str, dict[str, Any]] = {}
        for name in names:
            for entry in by_name.get(normalized_name(name), []):
                found[entry["uuid"]] = entry
        for entry in found.values():
            result.append(
                {
                    "profile_malware_id": malware["id"],
                    "profile_name": malware["name"],
                    "entry_uuid": entry["uuid"],
                    "entry_value": entry["value"],
                    "refs": entry.get("meta", {}).get("refs", []),
                    "assessment": (
                        "Name exists in Malpedia; this does not independently "
                        "verify that the actor used the malware."
                    ),
                }
            )
    return result


def relationship_candidates(
    matches_by_dataset: dict[str, list[dict[str, Any]]],
    datasets: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for dataset_id, matches in matches_by_dataset.items():
        by_uuid = {
            str(entry.get("uuid")): entry for entry in datasets[dataset_id]["values"]
        }
        for match in matches:
            for relation in match.get("related", []):
                destination = by_uuid.get(str(relation.get("dest-uuid")))
                if not destination:
                    continue
                relation_type = str(relation.get("type", "related-to"))
                if relation_type not in {"similar", "related-to", "part-of"}:
                    continue
                result.append(
                    {
                        "dataset_id": dataset_id,
                        "source_entry_uuid": match["entry_uuid"],
                        "relationship_type": relation_type,
                        "target_entry_uuid": destination.get("uuid"),
                        "target_actor": clean_actor_value(
                            str(destination.get("value", ""))
                        ),
                        "estimative_tags": relation.get("tags", []),
                        "confidence": "low",
                        "assessment": (
                            "MISP Galaxy relationship candidate. Review the "
                            "original references and actor scopes before integration."
                        ),
                    }
                )
    unique: dict[tuple[str, str, str], dict[str, Any]] = {}
    for item in result:
        key = (
            item["dataset_id"],
            item["relationship_type"],
            normalized_name(item["target_actor"]),
        )
        unique[key] = item
    return sorted(
        unique.values(),
        key=lambda item: (
            item["dataset_id"],
            item["relationship_type"],
            item["target_actor"],
        ),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument(
        "--tracker", type=Path, default=Path("profiles/osint-progress.json")
    )
    parser.add_argument(
        "--summary", type=Path, default=Path("profiles/osint-crosscheck-summary.json")
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("actor_profile/reference/osint/dataset-manifest.json"),
    )
    parser.add_argument(
        "--no-profile-sources",
        action="store_true",
        help="Do not add matched dataset sources to actor-profile.json.",
    )
    args = parser.parse_args()

    retrieved_at = utc_now()
    datasets: dict[str, dict[str, Any]] = {}
    manifests: dict[str, dict[str, Any]] = {}
    for dataset_id, descriptor in DATASETS.items():
        path = Path(descriptor["path"]).resolve()
        data = normalize_dataset(dataset_id, descriptor, load_json(path))
        datasets[dataset_id] = data
        manifests[dataset_id] = {
            "dataset_id": dataset_id,
            "title": descriptor["title"],
            "publisher": descriptor["publisher"],
            "url": descriptor["url"],
            "local_path": descriptor["path"],
            "kind": descriptor["kind"],
            "version": data.get("version"),
            "entry_count": len(data.get("values", [])),
            "sha256": sha256_file(path),
            "retrieved_at": retrieved_at,
        }
    write_json_atomic(
        args.manifest.resolve(),
        {
            "schema_version": "1.0.0",
            "generated_at": retrieved_at,
            "datasets": list(manifests.values()),
        },
    )

    catalog = load_json(args.catalog)
    tracker = load_json(args.tracker)
    tracker_by_slug = {item["slug"]: item for item in tracker["actors"]}
    actors_summary: list[dict[str, Any]] = []
    status_counts: Counter[str] = Counter()
    dataset_match_counts: Counter[str] = Counter()

    for actor in catalog["actors"]:
        slug = actor["slug"]
        profile_path = args.profiles_root / slug / "actor-profile.json"
        profile = load_json(profile_path)
        matches_by_dataset: dict[str, list[dict[str, Any]]] = {}
        for dataset_id, descriptor in DATASETS.items():
            if descriptor["kind"] != "actor":
                continue
            matches = match_actor(actor, profile, datasets[dataset_id])
            matches_by_dataset[dataset_id] = matches
            if matches:
                dataset_match_counts[dataset_id] += 1

        malware_matches = malware_catalog_matches(
            profile, datasets["misp-malpedia"]
        )
        all_actor_matches = [
            (dataset_id, match)
            for dataset_id, matches in matches_by_dataset.items()
            for match in matches
        ]
        ambiguous_datasets = sorted(
            dataset_id
            for dataset_id, matches in matches_by_dataset.items()
            if len(matches) > 1
        )
        profile_countries = {
            country_key(item)
            for item in profile.get("attribution", {}).get("countries", [])
            if item
        }
        external_countries = {
            country_key(country)
            for _, match in all_actor_matches
            for country in match.get("countries", [])
            if country
        }
        country_conflict = bool(
            profile_countries
            and external_countries
            and profile_countries.isdisjoint(external_countries)
        )
        high_confidence = any(
            match["match_confidence"] == "high"
            for _, match in all_actor_matches
        )
        anchored_match = any(
            match["match_basis"] in {"mitre-external-id", "canonical-name"}
            for _, match in all_actor_matches
        )
        unresolved_ambiguity = bool(ambiguous_datasets and not anchored_match)
        if unresolved_ambiguity or country_conflict:
            overall = "needs-review"
        elif high_confidence:
            overall = "matched"
        elif all_actor_matches:
            overall = "possible-match"
        else:
            overall = "no-match"
        status_counts[overall] += 1

        crosscheck = {
            "schema_version": "1.0.0",
            "actor_ref": profile["profile_id"],
            "actor_name": profile["name"],
            "searched_at": retrieved_at,
            "search_scope": {
                "datasets": list(DATASETS),
                "name_inputs": list(
                    dict.fromkeys(
                        [
                            actor["name"],
                            *actor.get("aliases", []),
                            *[
                                item["name"]
                                for item in profile.get("actor", {}).get(
                                    "aliases", []
                                )
                            ],
                        ]
                    )
                ),
                "mitre_group_id": actor.get("mitre_group_id"),
            },
            "overall_assessment": overall,
            "actor_matches": matches_by_dataset,
            "malware_catalog_matches": malware_matches,
            "relationship_candidates": relationship_candidates(
                matches_by_dataset, datasets
            ),
            "country_comparison": {
                "profile_values": sorted(profile_countries),
                "external_values": sorted(external_countries),
                "conflict": country_conflict,
                "assessment": (
                    "External country metadata conflicts with the profile; "
                    "retain both and review original sources."
                    if country_conflict
                    else "No disjoint country conflict detected."
                ),
            },
            "ambiguities": {
                "datasets_with_multiple_matches": ambiguous_datasets,
                "scope_divergence_detected": bool(ambiguous_datasets),
                "requires_review": bool(unresolved_ambiguity or country_conflict),
                "assessment": (
                    "Multiple taxonomy entries share names or aliases. A canonical "
                    "name or MITRE ID anchors this profile, so the additional "
                    "entries are retained as scope-divergence leads."
                    if ambiguous_datasets and anchored_match
                    else "No anchored resolution is available for multiple matches."
                    if unresolved_ambiguity
                    else "No multiple-match ambiguity detected."
                ),
            },
            "limitations": [
                "Exact normalized-name matching does not prove one-to-one actor identity.",
                "MISP Galaxy is an aggregation layer; original references remain authoritative.",
                "A no-match result means no exact match in the fixed datasets, not that the actor does not exist.",
                "A Malpedia name match confirms catalogue presence only, not actor use.",
            ],
        }
        write_json_atomic(
            args.profiles_root / slug / "osint-crosscheck.json", crosscheck
        )

        if not args.no_profile_sources and all_actor_matches:
            source_ids = {item["source_id"] for item in profile.get("sources", [])}
            matched_dataset_ids = sorted(
                dataset_id
                for dataset_id, matches in matches_by_dataset.items()
                if matches
            )
            for dataset_id in matched_dataset_ids:
                source = source_object(
                    dataset_id, DATASETS[dataset_id], manifests[dataset_id]
                )
                if source["source_id"] not in source_ids:
                    profile["sources"].append(source)
                    source_ids.add(source["source_id"])
            note = (
                "Structured OSINT cross-check completed against MISP Galaxy "
                f"datasets at {retrieved_at}; result={overall}."
            )
            collection_notes = profile["assessment"].get("collection_notes", "")
            prefix = "Structured OSINT cross-check completed against MISP Galaxy "
            retained_notes = [
                line
                for line in collection_notes.splitlines()
                if not line.startswith(prefix)
            ]
            profile["assessment"]["collection_notes"] = "\n".join(
                [*retained_notes, note]
            ).strip()
            if country_conflict:
                uncertainty = (
                    "Structured OSINT country metadata is disjoint from the "
                    "profile attribution; see osint-crosscheck.json and retain "
                    "both assessments pending original-source review."
                )
                if uncertainty not in profile["assessment"]["uncertainties"]:
                    profile["assessment"]["uncertainties"].append(uncertainty)
            profile["updated_at"] = retrieved_at
            write_json_atomic(profile_path, profile)

        progress = tracker_by_slug[slug]
        query = (
            f"{profile['name']} exact-name and alias cross-check in fixed "
            "MISP/MITRE/Microsoft/360 datasets"
        )
        if query not in progress["queries"]:
            progress["queries"].append(query)
        if progress.get("claims_integrated"):
            next_status = "integrated"
        elif overall == "needs-review":
            next_status = "needs_review"
        elif all_actor_matches:
            next_status = (
                "integrated"
                if progress["status"] == "integrated"
                else "source_verified"
            )
        else:
            next_status = (
                progress["status"]
                if progress["status"] in {"integrated", "source_verified"}
                else "searched"
            )
        progress["status"] = next_status
        progress["last_searched_at"] = retrieved_at
        note = (
            f"Fixed-dataset cross-check={overall}; actor datasets matched="
            f"{sum(bool(items) for items in matches_by_dataset.values())}; "
            f"Malpedia capability-name matches={len(malware_matches)}. "
            "See osint-crosscheck.json for ambiguity and no-match semantics."
        )
        tracker_prefix = "Fixed-dataset cross-check="
        retained_tracker_notes = [
            line
            for line in progress.get("analyst_notes", "").splitlines()
            if not line.startswith(tracker_prefix)
            and not line.startswith("Malpedia capability-name matches=")
        ]
        progress["analyst_notes"] = "\n".join(
            [*retained_tracker_notes, note]
        ).strip()
        actors_summary.append(
            {
                "slug": slug,
                "name": profile["name"],
                "overall_assessment": overall,
                "matched_dataset_count": sum(
                    bool(items) for items in matches_by_dataset.values()
                ),
                "actor_match_count": len(all_actor_matches),
                "malware_catalog_match_count": len(malware_matches),
                "relationship_candidate_count": len(
                    crosscheck["relationship_candidates"]
                ),
                "country_conflict": country_conflict,
                "ambiguous_datasets": ambiguous_datasets,
            }
        )

    tracker["updated_at"] = retrieved_at
    write_json_atomic(args.tracker.resolve(), tracker)
    summary = {
        "schema_version": "1.0.0",
        "generated_at": retrieved_at,
        "actor_count": len(actors_summary),
        "status_counts": dict(status_counts),
        "dataset_actor_match_counts": dict(dataset_match_counts),
        "actors_with_any_match": sum(
            item["actor_match_count"] > 0 for item in actors_summary
        ),
        "actors_with_no_match": sum(
            item["overall_assessment"] == "no-match" for item in actors_summary
        ),
        "actors_needing_review": sum(
            item["overall_assessment"] == "needs-review"
            for item in actors_summary
        ),
        "actors": actors_summary,
    }
    write_json_atomic(args.summary.resolve(), summary)
    print(
        json.dumps(
            {
                "actor_count": summary["actor_count"],
                "status_counts": summary["status_counts"],
                "actors_with_any_match": summary["actors_with_any_match"],
                "actors_needing_review": summary["actors_needing_review"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
