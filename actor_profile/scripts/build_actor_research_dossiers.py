#!/usr/bin/env python3
"""Materialize evidence-linked research dossiers for every active actor.

The canonical layer is copied from ``actor-profile.json`` and never receives
facts from aggregation datasets.  ETDA, MISP, and TIDAL material is retained in
a separate research-lead layer so analysts can see potentially relevant past
activity without mistaking it for a verified actor-specific assertion.
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from common import load_json, stable_digest, unknown_time, utc_now, write_json_atomic


URL_RE = re.compile(r"https?://[^\s<>]+")
KNOWN_STATUSES = {"known", "inferred"}
TARGETING_LINE_PREFIX = "構造化ターゲット監査:"


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def known_time(point: dict[str, Any] | None) -> bool:
    return bool(point and point.get("value") and point.get("status") in KNOWN_STATUSES)


def explicit_time(
    value: str | None, basis: str, *, status: str = "known"
) -> dict[str, Any]:
    if not value:
        return unknown_time()
    raw = value.strip()
    if re.fullmatch(r"\d{4}", raw):
        timestamp, precision = f"{raw}-01-01T00:00:00Z", "year"
    elif re.fullmatch(r"\d{4}-\d{2}", raw):
        timestamp, precision = f"{raw}-01T00:00:00Z", "month"
    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        timestamp, precision = f"{raw}T00:00:00Z", "day"
    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}T.*Z", raw):
        timestamp, precision = raw, "second"
    else:
        return unknown_time()
    return {
        "value": timestamp,
        "precision": precision,
        "status": status,
        "basis": basis,
    }


def linked_period(
    observations: Iterable[dict[str, Any]],
    field: str,
    choose: str,
) -> dict[str, Any]:
    points = [item.get(field) for item in observations if known_time(item.get(field))]
    if not points:
        return unknown_time()
    point = min(points, key=lambda item: item["value"]) if choose == "min" else max(
        points, key=lambda item: item["value"]
    )
    result = dict(point)
    result["status"] = "inferred"
    result["basis"] = "explicit-linked-activity-period"
    return result


def claim_index(audit: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    for item in audit.get("claims", []):
        result.setdefault(str(item.get("subject", "")), []).append(
            {
                "claim_id": item.get("claim_id"),
                "category": item.get("category"),
                "verification_status": item.get("verification_status"),
                "confidence": item.get("confidence"),
                "statement": item.get("statement", ""),
                "evidence_refs": item.get("evidence_refs", []),
                "verification_rationale": item.get("verification_rationale", ""),
                "counterevidence": item.get("counterevidence", []),
            }
        )
    return result


def attach_claims(item: dict[str, Any], claims: dict[str, list[dict[str, Any]]], key: str) -> dict[str, Any]:
    result = dict(item)
    result["claim_assessments"] = claims.get(str(item.get(key, "")), [])
    return result


def target_records(profile: dict[str, Any], claims: dict[str, list[dict[str, Any]]]) -> tuple[list[dict[str, Any]], dict[str, str]]:
    activities = profile.get("activities", [])
    result: list[dict[str, Any]] = []
    names: dict[str, str] = {}
    for category in ("countries", "regions", "sectors", "roles"):
        for target in profile.get("targets", {}).get(category, []):
            target_id = target["id"]
            names[target_id] = target.get("name", target_id)
            record = attach_claims(target, claims, "id")
            record["category"] = category[:-1] if category.endswith("s") else category
            record["activity_refs"] = sorted(
                activity["activity_id"]
                for activity in activities
                if target_id in activity.get("target_refs", [])
            )
            result.append(record)
    return result, names


def activity_records(
    profile: dict[str, Any],
    claims: dict[str, list[dict[str, Any]]],
    target_names: dict[str, str],
) -> list[dict[str, Any]]:
    malware_names = {
        item["id"]: item.get("name", item["id"])
        for item in profile.get("capabilities", {}).get("malware", [])
    }
    tool_names = {
        item["id"]: item.get("name", item["id"])
        for item in profile.get("capabilities", {}).get("tools", [])
    }
    ttp_by_id = {item["ttp_id"]: item for item in profile.get("ttps", [])}
    victims = {
        item["victim_case_id"]: item.get("victim_name") or item.get("disclosure_status", "unknown")
        for item in profile.get("victim_cases", [])
    }
    result = []
    for activity in profile.get("activities", []):
        record = attach_claims(activity, claims, "activity_id")
        record["malware"] = [
            {"id": ref, "name": malware_names.get(ref, tool_names.get(ref, ref))}
            for ref in activity.get("malware_refs", [])
        ]
        if "tool_refs" in activity:
            record["tools"] = [
                {"id": ref, "name": tool_names.get(ref, ref)}
                for ref in activity.get("tool_refs", [])
            ]
        record["targets"] = [
            {"id": ref, "name": target_names.get(ref, ref)}
            for ref in activity.get("target_refs", [])
        ]
        record["victims"] = [
            {"id": ref, "name": victims.get(ref, ref)}
            for ref in activity.get("victim_refs", [])
        ]
        record["techniques"] = [
            {
                "id": ref,
                "technique_id": ttp_by_id.get(ref, {}).get("technique_id"),
                "name": ttp_by_id.get(ref, {}).get("technique_name", ref),
            }
            for ref in activity.get("ttp_refs", [])
        ]
        result.append(record)
    return sorted(
        result,
        key=lambda item: (
            item.get("first_observed", {}).get("value") is None,
            item.get("first_observed", {}).get("value") or "9999",
            item.get("name", "").casefold(),
        ),
    )


def malware_records(
    profile: dict[str, Any],
    claims: dict[str, list[dict[str, Any]]],
    capability_kind: str = "malware",
) -> list[dict[str, Any]]:
    activities = profile.get("activities", [])
    ttps = profile.get("ttps", [])
    result = []
    activity_ref_field = "tool_refs" if capability_kind == "tools" else "malware_refs"
    for malware in profile.get("capabilities", {}).get(capability_kind, []):
        malware_id = malware["id"]
        activity_ids = {
            activity["activity_id"]
            for activity in activities
            if malware_id in activity.get(activity_ref_field, [])
        }
        if capability_kind == "malware":
            for ttp in ttps:
                if malware_id in ttp.get("malware_refs", []):
                    activity_ids.update(ttp.get("activity_refs", []))
        observations = [
            {
                "activity_id": activity["activity_id"],
                "activity_name": activity.get("name", ""),
                "first_observed": activity.get("first_observed", unknown_time()),
                "last_observed": activity.get("last_observed", unknown_time()),
                "evidence_refs": activity.get("evidence_refs", []),
            }
            for activity in activities
            if activity["activity_id"] in activity_ids
        ]
        record = attach_claims(malware, claims, "id")
        record["activity_observations"] = observations
        record["derived_first_observed"] = linked_period(observations, "first_observed", "min")
        record["derived_last_observed"] = linked_period(observations, "last_observed", "max")
        record["temporal_assessment"] = (
            "activity-linked"
            if observations
            else "actor-level-only; no campaign-specific use date is asserted"
        )
        result.append(record)
    return sorted(result, key=lambda item: item.get("name", "").casefold())


def etda_activity_leads(matches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for match in matches:
        for operation in match.get("research_data", {}).get("operations", []):
            if not isinstance(operation, dict):
                continue
            raw = str(operation.get("activity", ""))
            urls = URL_RE.findall(raw)
            title = " ".join(
                line.strip()
                for line in raw.splitlines()
                if line.strip() and not line.strip().startswith(("http://", "https://"))
            )
            key = stable_digest(title, *urls, str(operation.get("date", "")))
            if key in seen:
                continue
            seen.add(key)
            result.append(
                {
                    "lead_id": f"activity-lead--etda--{key[:20]}",
                    "name": title or "ETDA indexed activity",
                    "first_observed": unknown_time(),
                    "last_observed": unknown_time(),
                    "reported_at": explicit_time(
                        str(operation.get("date") or ""),
                        "etda-operation-index-date; not an activity observation date",
                    ),
                    "source_urls": urls,
                    "dataset_entry": match.get("entry_value"),
                    "match_basis": match.get("match_basis"),
                    "match_confidence": match.get("match_confidence"),
                    "verification_status": "partially-supported",
                    "analyst_notes": (
                        "ETDA/ThaiCERT aggregation lead. The linked original report "
                        "must be reviewed before canonical integration."
                    ),
                }
            )
    return result


def field_leads(matches: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for match in matches:
        values = match.get("research_data", {}).get(key, [])
        if not isinstance(values, list):
            values = [values]
        for value in values:
            text = str(value).strip()
            normalized_value = normalized(text)
            if not normalized_value or normalized_value in seen:
                continue
            seen.add(normalized_value)
            result.append(
                {
                    "value": text,
                    "dataset_entry": match.get("entry_value"),
                    "source_urls": match.get("refs", []),
                    "match_basis": match.get("match_basis"),
                    "match_confidence": match.get("match_confidence"),
                    "verification_status": "partially-supported",
                }
            )
    return result


def merge_value_leads(*collections: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    by_key: dict[str, dict[str, Any]] = {}
    for collection in collections:
        for item in collection:
            key = normalized(str(item.get("value") or item.get("name") or ""))
            if not key:
                continue
            existing = by_key.get(key)
            if existing is None:
                existing = copy.deepcopy(item)
                by_key[key] = existing
                result.append(existing)
                continue
            if item == existing or item in existing.get("supporting_records", []):
                continue
            existing.setdefault("supporting_records", []).append(copy.deepcopy(item))
            for field in ("evidence_refs", "source_urls"):
                values = [
                    *existing.get(field, []),
                    *item.get(field, []),
                ]
                if values:
                    existing[field] = list(dict.fromkeys(values))
    return result


def tidal_leads(
    matches: list[dict[str, Any]],
    index: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    campaign_result: list[dict[str, Any]] = []
    software_result: list[dict[str, Any]] = []
    campaign_seen: set[str] = set()
    software_seen: set[str] = set()
    for match in matches:
        group_id = str(match.get("entry_uuid", "")).lower()
        group = index.get("groups", {}).get(group_id)
        if not group:
            continue
        for campaign_id in group.get("campaign_refs", []):
            campaign = index.get("campaigns", {}).get(campaign_id)
            if not campaign or campaign_id in campaign_seen:
                continue
            campaign_seen.add(campaign_id)
            campaign_result.append(
                {
                    **campaign,
                    "first_observed": explicit_time(
                        campaign.get("first_observed"),
                        "tidal-aggregation; original source not yet reviewed",
                        status="inferred",
                    ),
                    "last_observed": explicit_time(
                        campaign.get("last_observed"),
                        "tidal-aggregation; original source not yet reviewed",
                        status="inferred",
                    ),
                    "match_basis": match.get("match_basis"),
                    "match_confidence": match.get("match_confidence"),
                    "verification_status": "partially-supported",
                    "analyst_notes": (
                        "TIDAL/MISP aggregation lead. Review source_urls and actor "
                        "scope before canonical integration."
                    ),
                }
            )
        for software_id in group.get("software_refs", []):
            software = index.get("software", {}).get(software_id)
            if not software or software_id in software_seen:
                continue
            software_seen.add(software_id)
            software_result.append(
                {
                    **software,
                    "match_basis": match.get("match_basis"),
                    "match_confidence": match.get("match_confidence"),
                    "verification_status": "partially-supported",
                    "temporal_assessment": "unknown; actor-level aggregation lead",
                }
            )
    return campaign_result, software_result


def source_catalog(profile: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        source["source_id"]: source
        for source in profile.get("sources", [])
        if source.get("source_id")
    }


def evidence_refs_in(value: Any) -> set[str]:
    refs: set[str] = set()
    if isinstance(value, dict):
        refs.update(str(item) for item in value.get("evidence_refs", []) if item)
        for nested in value.values():
            refs.update(evidence_refs_in(nested))
    elif isinstance(value, list):
        for nested in value:
            refs.update(evidence_refs_in(nested))
    return refs


def resolve_target_actor(
    value: str,
    catalog_by_name: dict[str, dict[str, Any]],
    catalog_by_id: dict[str, dict[str, Any]],
) -> tuple[str | None, str]:
    target = catalog_by_id.get(value) or catalog_by_name.get(normalized(value))
    if target:
        return f"actor--{target['slug']}", "catalog-profile"
    return None, "external-name-only"


def workbook_target_leads(profile: dict[str, Any]) -> list[dict[str, Any]]:
    source_id = "source--actor-mapping-workbook"
    if not any(
        source.get("source_id") == source_id
        for source in profile.get("sources", [])
    ):
        return []
    text = "\n".join(
        line
        for line in profile.get("free_text", {})
        .get("targeting_details", "")
        .splitlines()
        if not line.startswith(TARGETING_LINE_PREFIX)
    ).strip()
    if not text:
        return []
    return [
        {
            "value": text,
            "evidence_refs": [source_id],
            "verification_status": "unresolved",
            "analyst_notes": (
                "Legacy workbook targeting prose. Original actor scope and cited "
                "reports must be reviewed before canonical integration."
            ),
        }
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument(
        "--tidal-index",
        type=Path,
        default=Path("actor_profile/reference/osint/tidal-activity-index.json"),
    )
    parser.add_argument(
        "--manual-leads",
        type=Path,
        default=Path("actor_profile/manual-research-leads.json"),
    )
    parser.add_argument(
        "--summary", type=Path, default=Path("profiles/research-summary.json")
    )
    parser.add_argument(
        "--csv", type=Path, default=Path("profiles/research-summary.csv")
    )
    args = parser.parse_args()

    catalog = load_json(args.catalog)
    tidal = load_json(args.tidal_index)
    manual_leads = (
        load_json(args.manual_leads).get("actors", {})
        if args.manual_leads.exists()
        else {}
    )
    catalog_by_name = {normalized(item["name"]): item for item in catalog["actors"]}
    catalog_by_id = {
        f"actor--{item['slug']}": item for item in catalog["actors"]
    }
    generated_at = utc_now()
    summary_rows: list[dict[str, Any]] = []
    coverage_counts: Counter[str] = Counter()

    for actor in catalog["actors"]:
        slug = actor["slug"]
        actor_root = args.profiles_root / slug
        profile = load_json(actor_root / "actor-profile.json")
        audit = load_json(actor_root / "claim-audit.json")
        crosscheck = load_json(actor_root / "osint-crosscheck.json")
        claims = claim_index(audit)
        curated_leads = manual_leads.get(slug, {})
        targets, target_names = target_records(profile, claims)
        activities = activity_records(profile, claims, target_names)
        malware = malware_records(profile, claims)
        tools = malware_records(profile, claims, "tools")
        associated_entities = [
            attach_claims(item, claims, "entity_id")
            for item in profile.get("associated_entities", [])
        ]
        entity_relationships = [
            attach_claims(item, claims, "relationship_id")
            for item in profile.get("entity_relationships", [])
        ]
        hunting_pivots = [
            attach_claims(item, claims, "pivot_id")
            for item in profile.get("hunting_pivots", [])
        ]
        relationships = []
        for relation in profile.get("relationships", []):
            record = attach_claims(relation, claims, "relationship_id")
            target_ref, resolution = resolve_target_actor(
                str(relation.get("target_actor", "")),
                catalog_by_name,
                catalog_by_id,
            )
            record["target_actor_ref"] = target_ref
            record["target_resolution"] = resolution
            relationships.append(record)

        etda_matches = crosscheck.get("actor_matches", {}).get(
            "etda-threat-group-cards", []
        )
        tidal_matches = crosscheck.get("actor_matches", {}).get(
            "misp-tidal-groups", []
        )
        aggregation_matches = [
            match
            for dataset_id, matches in crosscheck.get("actor_matches", {}).items()
            if dataset_id == "etda-threat-group-cards"
            or dataset_id.startswith("misp-")
            for match in matches
        ]
        external_campaigns, external_software = tidal_leads(tidal_matches, tidal)
        external_aliases = merge_value_leads(curated_leads.get("aliases", []))
        external_activities = merge_value_leads(
            curated_leads.get("activities", []),
            etda_activity_leads(etda_matches),
            external_campaigns,
        )
        external_relationships = [
            *crosscheck.get("relationship_candidates", []),
            *curated_leads.get("relationships", []),
        ]
        external_targets = {
            "countries": merge_value_leads(
                curated_leads.get("targets", {}).get("countries", []),
                field_leads(aggregation_matches, "observed-countries"),
            ),
            "victims_or_geographies": merge_value_leads(
                curated_leads.get("targets", {}).get("regions", []),
                field_leads(aggregation_matches, "cfr-suspected-victims"),
            ),
            "sectors": merge_value_leads(
                curated_leads.get("targets", {}).get("sectors", []),
                field_leads(aggregation_matches, "observed-sectors"),
                field_leads(aggregation_matches, "target_categories"),
                field_leads(aggregation_matches, "cfr-target-category"),
                field_leads(aggregation_matches, "targeted-sector"),
            ),
            "roles": merge_value_leads(
                curated_leads.get("targets", {}).get("roles", []),
            ),
            "legacy_workbook_text": workbook_target_leads(profile),
        }
        external_motivations = merge_value_leads(
            curated_leads.get("motivations", []),
            field_leads(aggregation_matches, "motivation"),
            field_leads(aggregation_matches, "observed_motivations"),
        )
        aggregated_software = field_leads(aggregation_matches, "tools")
        external_incident_types = field_leads(
            aggregation_matches, "cfr-type-of-incident"
        )
        external_malware = merge_value_leads(
            curated_leads.get("capabilities", {}).get("malware", []),
            aggregated_software,
            [
                item
                for item in external_software
                if "malware" in item.get("software_type", [])
            ],
        )
        external_tools = merge_value_leads(
            curated_leads.get("capabilities", {}).get("tools", []),
            [
                item
                for item in external_software
                if "tool" in item.get("software_type", [])
            ],
        )
        external_untyped_software = [
            item
            for item in external_software
            if not set(item.get("software_type", [])) & {"malware", "tool"}
        ]
        external_other_capabilities = {
            category: curated_leads.get("capabilities", {}).get(category, [])
            for category in (
                "infrastructure",
                "delivery_formats",
                "vulnerabilities",
                "operational_capabilities",
            )
        }
        external_assessments = curated_leads.get("assessment", [])
        external_attribution = [
            {
                "dataset": dataset_id,
                "entry_value": match.get("entry_value"),
                "countries": match.get("countries", []),
                "sponsor": match.get("research_data", {}).get("sponsor"),
                "source_urls": match.get("refs", []),
                "match_basis": match.get("match_basis"),
                "match_confidence": match.get("match_confidence"),
                "verification_status": "partially-supported",
            }
            for dataset_id, matches in crosscheck.get("actor_matches", {}).items()
            for match in matches
            if match.get("countries")
            or match.get("research_data", {}).get("sponsor")
        ] + curated_leads.get("attribution", [])

        gaps = []
        if not activities:
            gaps.append("No canonical actor-specific activity is structured.")
        if activities and not any(
            known_time(item.get("first_observed"))
            or known_time(item.get("last_observed"))
            for item in activities
        ):
            gaps.append("Canonical activities exist, but their observation periods are unknown.")
        if malware and not any(item["activity_observations"] for item in malware):
            gaps.append("Malware is actor-linked only; campaign-specific use periods are unknown.")
        if not relationships:
            gaps.append("No canonical cross-actor relationship is structured.")
        if not targets:
            gaps.append("No canonical target country, region, sector, or role is structured.")
        if not profile.get("motivations"):
            gaps.append("Motivation remains unknown or unstructured.")
        attribution = profile.get("attribution", {})
        if (
            not attribution.get("countries")
            and not attribution.get("organizations")
            and attribution.get("sponsor_type", "unknown") == "unknown"
        ):
            gaps.append("Attribution remains unknown or unstructured.")

        attribution_record = dict(attribution)
        attribution_record["claim_assessments"] = [
            *claims.get("countries", []),
            *claims.get("organizations", []),
            *claims.get("sponsor-type", []),
        ]
        canonical = {
            "attribution": attribution_record,
            "motivations": [
                attach_claims(item, claims, "type")
                for item in profile.get("motivations", [])
            ],
            "relationships": relationships,
            "associated_entities": associated_entities,
            "entity_relationships": entity_relationships,
            "hunting_pivots": hunting_pivots,
            "activity_timeline": activities,
            "malware_usage": malware,
            "tool_usage": tools,
            "targets": targets,
        }
        sources = source_catalog(profile)
        unresolved_refs = sorted(evidence_refs_in(canonical) - set(sources))
        if unresolved_refs:
            gaps.append(
                "Canonical evidence references missing from source catalog: "
                + ", ".join(unresolved_refs)
            )

        dimension_status = {
            "activities": "canonical-present" if activities else "lead-only" if external_activities else "unknown",
            "relationships": "canonical-present" if relationships else "lead-only" if external_relationships else "unknown",
            "associated_entities": "canonical-present" if associated_entities or entity_relationships else "unknown",
            "hunting_pivots": "canonical-present" if hunting_pivots else "unknown",
            "malware": "canonical-present" if malware else "lead-only" if external_malware else "unknown",
            "tools": "canonical-present" if tools else "lead-only" if external_tools else "unknown",
            "targets": "canonical-present" if targets else "lead-only" if any(external_targets.values()) else "unknown",
            "motivations": "canonical-present" if profile.get("motivations") else "lead-only" if external_motivations else "unknown",
            "attribution": "canonical-present" if attribution.get("evidence_refs") else "lead-only" if external_attribution else "unknown",
        }
        coverage_counts.update(dimension_status.values())
        dossier = {
            "schema_version": "1.0.0",
            "generated_at": generated_at,
            "actor_ref": profile["profile_id"],
            "actor_name": profile["name"],
            "profile_updated_at": profile.get("updated_at"),
            "scope_note": (
                "Canonical records come from actor-profile.json. External research "
                "leads are kept separate and are not proof of actor identity, use, "
                "targeting, motivation, or attribution until original sources are reviewed."
            ),
            "coverage": {
                "dimensions": dimension_status,
                "canonical_counts": {
                    "activities": len(activities),
                    "dated_activities": sum(
                        known_time(item.get("first_observed"))
                        or known_time(item.get("last_observed"))
                        for item in activities
                    ),
                    "relationships": len(relationships),
                    "associated_entities": len(associated_entities),
                    "entity_relationships": len(entity_relationships),
                    "hunting_pivots": len(hunting_pivots),
                    "hunting_pivot_observations": sum(
                        len(item.get("observations", []))
                        for item in hunting_pivots
                    ),
                    "malware": len(malware),
                    "activity_linked_malware": sum(
                        bool(item["activity_observations"]) for item in malware
                    ),
                    "tools": len(tools),
                    "targets": len(targets),
                    "motivations": len(profile.get("motivations", [])),
                },
                "external_lead_counts": {
                    "aliases": len(external_aliases),
                    "activities": len(external_activities),
                    "relationships": len(external_relationships),
                    "malware": len(external_malware),
                    "tools": len(external_tools),
                    "untyped_software": len(external_untyped_software),
                    "targets": sum(len(items) for items in external_targets.values()),
                    "motivations": len(external_motivations),
                    "other_capabilities": sum(
                        len(items) for items in external_other_capabilities.values()
                    ),
                    "assessments": len(external_assessments),
                },
            },
            "canonical": canonical,
            "external_research_leads": {
                "aliases": external_aliases,
                "activities": external_activities,
                "incident_types": external_incident_types,
                "relationships": external_relationships,
                "malware": external_malware,
                "tools": external_tools,
                "untyped_software": external_untyped_software,
                "other_capabilities": external_other_capabilities,
                "targets": external_targets,
                "motivations": external_motivations,
                "attribution": external_attribution,
                "assessments": external_assessments,
            },
            "claim_audit_counts": audit.get("counts", {}),
            "evidence_catalog": sources,
            "research_gaps": gaps,
        }
        output = actor_root / "generated" / "research-dossier.json"
        write_json_atomic(output, dossier)
        summary_rows.append(
            {
                "slug": slug,
                "name": profile["name"],
                **{f"{key}_status": value for key, value in dimension_status.items()},
                **dossier["coverage"]["canonical_counts"],
                "external_activity_leads": len(external_activities),
                "external_alias_leads": len(external_aliases),
                "external_relationship_leads": len(external_relationships),
                "external_malware_leads": len(external_malware),
                "external_tool_leads": len(external_tools),
                "gap_count": len(gaps),
            }
        )

    summary = {
        "schema_version": "1.0.0",
        "generated_at": generated_at,
        "actor_count": len(summary_rows),
        "dimension_status_counts": dict(coverage_counts),
        "totals": {
            key: sum(int(row.get(key, 0)) for row in summary_rows)
            for key in (
                "activities",
                "dated_activities",
                "relationships",
                "associated_entities",
                "entity_relationships",
                "hunting_pivots",
                "hunting_pivot_observations",
                "malware",
                "activity_linked_malware",
                "tools",
                "targets",
                "motivations",
                "external_activity_leads",
                "external_alias_leads",
                "external_relationship_leads",
                "external_malware_leads",
                "external_tool_leads",
            )
        },
        "actors": summary_rows,
    }
    write_json_atomic(args.summary.resolve(), summary)
    fieldnames = list(summary_rows[0]) if summary_rows else []
    with args.csv.resolve().open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(summary_rows)
    print(json.dumps({"actors": len(summary_rows), **summary["totals"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
