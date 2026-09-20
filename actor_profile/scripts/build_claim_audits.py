#!/usr/bin/env python3
"""Build per-profile claim verification ledgers and a collection summary."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import (
    STATE_SPONSORSHIP_MARKERS,
    normalized_name,
    text_contains_any,
)
from common import load_json, stable_digest, utc_now, write_json_atomic


NON_NATION_STATE_CATEGORIES = {
    "covert network",
    "financially motivated",
    "group in development",
    "influence operations",
    "private sector offensive actor",
}


def claim(
    slug: str,
    category: str,
    subject: str,
    statement: str,
    status: str,
    confidence: str,
    evidence_refs: list[str],
    rationale: str,
    *,
    counterevidence: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "claim_id": "claim--" + stable_digest(slug, category, subject)[:24],
        "category": category,
        "subject": subject,
        "statement": statement,
        "verification_status": status,
        "confidence": confidence,
        "evidence_refs": sorted(set(evidence_refs)),
        "verification_rationale": rationale,
        "counterevidence": counterevidence or [],
        "reviewed_at": utc_now(),
    }


def evidence_tier(refs: list[str], source_by_id: dict[str, dict[str, Any]]) -> str:
    if not refs:
        return "none"

    def source_tier(source: dict[str, Any]) -> str:
        source_type = source.get("source_type", "")
        publisher = source.get("publisher", "")
        # Aggregations stay leads even when a government body publishes them
        # or their publisher string mentions an upstream knowledge base.
        if any(
            marker in source_type
            for marker in ("aggregation", "mapping", "encyclopedia")
        ):
            return "aggregation"
        if any(
            marker in source_type
            for marker in ("government", "legal", "law-enforcement", "cert")
        ):
            return "authoritative"
        if "knowledge-base" in source_type or publisher in {
            "MITRE",
            "MITRE ATT&CK",
        }:
            return "knowledge-base"
        if (
            source_type == "report"
            or source_type
            in {"actor-specific-investigation", "primary-report", "technical-report"}
            or any(
                marker in source_type for marker in ("vendor-", "-research")
            )
        ):
            return "research"
        return "repository"

    rank = {
        "repository": 0,
        "aggregation": 1,
        "research": 2,
        "knowledge-base": 3,
        "authoritative": 4,
    }
    tiers = [source_tier(source_by_id.get(ref, {})) for ref in refs]
    return max(tiers, key=rank.__getitem__)


def verification_from_refs(
    refs: list[str], source_by_id: dict[str, dict[str, Any]]
) -> tuple[str, str]:
    tier = evidence_tier(refs, source_by_id)
    if tier in {"authoritative", "knowledge-base", "research"}:
        return "supported", tier
    if refs:
        return "partially-supported", tier
    return "unresolved", tier


def microsoft_nation_state_match(
    profile: dict[str, Any], mapping: list[dict[str, Any]]
) -> dict[str, Any] | None:
    """Return an exact-name Microsoft nation-state taxonomy match.

    The mapping's country field is usable here only because Microsoft's source
    explicitly defines country-labelled entries as the nation-state actor
    category. Generic country/origin fields remain insufficient evidence.
    """
    exact_names = {
        normalized_name(profile["name"]),
        normalized_name(profile["actor"]["canonical_name"]),
        *(
            normalized_name(alias["name"])
            for alias in profile["actor"].get("aliases", [])
            if alias.get("scope") == "exact"
        ),
    }
    for row in mapping:
        row_names = [row.get("Threat actor name", "")]
        row_names.extend(
            item.strip()
            for item in re.split(r"[,;]", row.get("Other names", ""))
            if item.strip()
        )
        if not exact_names.intersection(
            normalized_name(name) for name in row_names if name
        ):
            continue
        category = row.get("Origin/Threat", "").strip()
        category_folded = category.casefold()
        if not category or any(
            marker in category_folded for marker in NON_NATION_STATE_CATEGORIES
        ):
            continue
        return row
    return None


def actor_type_support(
    actor_type: str,
    profile: dict[str, Any],
    catalog_actor: dict[str, Any],
    source_by_id: dict[str, dict[str, Any]],
    attack_groups: dict[str, dict[str, Any]],
    microsoft_mapping: list[dict[str, Any]],
) -> tuple[str, str, list[str], str]:
    """Return verification metadata for a profile-level actor type."""
    attribution = profile.get("attribution", {})
    attribution_refs = attribution.get("evidence_refs", [])
    mitre_refs = [
        source_id
        for source_id, source in source_by_id.items()
        if source.get("publisher") in {"MITRE", "MITRE ATT&CK"}
        or "attack-index.json" in (source.get("path") or "")
    ]
    mitre_group = attack_groups.get(catalog_actor.get("mitre_group_id", ""), {})

    if actor_type == "state-sponsored":
        if attribution.get("sponsor_type") == "state" and attribution_refs:
            status, tier = verification_from_refs(attribution_refs, source_by_id)
            return status, attribution.get("confidence", "unknown"), attribution_refs, (
                f"Structured sponsor_type=state; evidence tier={tier}."
            )
        if text_contains_any(
            mitre_group.get("description", ""), STATE_SPONSORSHIP_MARKERS
        ):
            return (
                "supported",
                "high",
                mitre_refs,
                "The actor-specific MITRE ATT&CK description explicitly states state sponsorship.",
            )
        microsoft_match = microsoft_nation_state_match(profile, microsoft_mapping)
        microsoft_ref = "source--osint-microsoft-threat-actor-mapping"
        if microsoft_match and microsoft_ref in source_by_id:
            return (
                "supported",
                "high",
                [microsoft_ref],
                "Microsoft places the exact actor name in its nation-state taxonomy "
                f"(category={microsoft_match['Origin/Threat']}); this is not inferred "
                "from generic geography.",
            )
        if attribution.get("sponsor_type") == "state-aligned" and attribution_refs:
            return (
                "partially-supported",
                attribution.get("confidence", "unknown"),
                attribution_refs,
                "The structured assessment supports state alignment but not the stronger state-sponsored label.",
            )
        return (
            "unresolved",
            "unknown",
            [],
            "No actor-specific sponsorship evidence was linked to this actor type.",
        )

    motivation_type = {
        "financially-motivated": "financial-gain",
        "espionage": "espionage",
        "hacktivist": "ideological",
        "hacktivist-collective": "ideological",
    }.get(actor_type)
    refs: list[str] = []
    confidences: list[str] = []
    if motivation_type:
        for item in profile.get("motivations", []):
            if item.get("type") == motivation_type:
                refs.extend(item.get("evidence_refs", []))
                confidences.append(item.get("confidence", "unknown"))
    if actor_type == "private-sector-offensive" and attribution.get(
        "sponsor_type"
    ) == "private-sector-offensive":
        refs.extend(attribution_refs)
        confidences.append(attribution.get("confidence", "unknown"))
    if actor_type in {"cybercrime", "business-email-compromise"} and attribution.get(
        "sponsor_type"
    ) == "criminal":
        refs.extend(attribution_refs)
        confidences.append(attribution.get("confidence", "unknown"))
    if actor_type in {"threat-cluster", "threat-group"} and catalog_actor.get(
        "mitre_group_id"
    ):
        refs.extend(mitre_refs)
        confidences.append("high")
    refs = sorted(set(refs))
    if not refs and actor_type in {"threat-cluster", "threat-group"}:
        for section in (
            profile.get("motivations", []),
            profile.get("activities", []),
            profile.get("assessment", {}).get("key_judgments", []),
        ):
            for item in section:
                candidate_refs = item.get("evidence_refs", [])
                if evidence_tier(candidate_refs, source_by_id) in {
                    "authoritative",
                    "knowledge-base",
                    "research",
                }:
                    refs.extend(candidate_refs)
            if refs:
                break
        refs = sorted(set(refs))[:5]
    status, tier = verification_from_refs(refs, source_by_id)
    confidence = "high" if "high" in confidences else "medium" if refs else "unknown"
    return status, confidence, refs, f"Evidence tier={tier}; actor type is audited independently of geography."


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument(
        "--output", type=Path, default=Path("profiles/claim-audit-summary.json")
    )
    parser.add_argument(
        "--attack-index",
        type=Path,
        default=Path("actor_profile/reference/attack-index.json"),
    )
    parser.add_argument(
        "--microsoft-mapping",
        type=Path,
        default=Path(
            "actor_profile/reference/osint/microsoft-threat-actor-mapping.json"
        ),
    )
    parser.add_argument(
        "--actor",
        action="append",
        default=[],
        help="limit regeneration to an actor slug; repeat for multiple actors",
    )
    args = parser.parse_args()
    catalog = load_json(args.catalog)
    attack_groups = load_json(args.attack_index).get("groups", {})
    microsoft_mapping = load_json(args.microsoft_mapping)
    profiles_root = args.profiles_root.resolve()
    collection_counts: Counter[str] = Counter()
    actors: list[dict[str, Any]] = []
    selected_slugs = set(args.actor)
    catalog_actors = catalog["actors"]
    if selected_slugs:
        known_slugs = {actor["slug"] for actor in catalog_actors}
        unknown_slugs = sorted(selected_slugs - known_slugs)
        if unknown_slugs:
            parser.error(f"unknown actor slug(s): {', '.join(unknown_slugs)}")
        catalog_actors = [
            actor for actor in catalog_actors if actor["slug"] in selected_slugs
        ]

    for actor in catalog_actors:
        slug = actor["slug"]
        profile_path = profiles_root / slug / "actor-profile.json"
        profile = load_json(profile_path)
        source_by_id = {
            item["source_id"]: item for item in profile.get("sources", [])
        }
        claims: list[dict[str, Any]] = []
        crosscheck_path = profiles_root / slug / "osint-crosscheck.json"
        crosscheck = (
            load_json(crosscheck_path) if crosscheck_path.exists() else None
        )
        mitre_refs = [
            source_id
            for source_id, source in source_by_id.items()
            if source.get("publisher") in {"MITRE", "MITRE ATT&CK"}
            or "attack-index.json" in (source.get("path") or "")
        ]
        canonical_status = "supported" if actor.get("mitre_group_id") else "unresolved"
        claims.append(
            claim(
                slug,
                "identity",
                "canonical-name",
                f"Canonical profile name is {profile['name']}.",
                canonical_status,
                "high" if mitre_refs else "medium",
                mitre_refs,
                (
                    "The canonical name is mapped to a MITRE ATT&CK group ID."
                    if mitre_refs
                    else "The name is corpus-backed but lacks an independent canonical authority."
                ),
            )
        )
        for actor_type in profile["actor"].get("actor_types", []):
            status, confidence, refs, rationale = actor_type_support(
                actor_type,
                profile,
                actor,
                source_by_id,
                attack_groups,
                microsoft_mapping,
            )
            claims.append(
                claim(
                    slug,
                    "actor-type",
                    actor_type,
                    f"{profile['name']} is classified as {actor_type}.",
                    status,
                    confidence,
                    refs,
                    rationale,
                )
            )
        if crosscheck:
            assessment = crosscheck.get("overall_assessment", "no-match")
            matched_dataset_ids = sorted(
                dataset_id
                for dataset_id, matches in crosscheck.get(
                    "actor_matches", {}
                ).items()
                if matches
            )
            matched_refs = [
                f"source--osint-{dataset_id}"
                for dataset_id in matched_dataset_ids
                if f"source--osint-{dataset_id}" in source_by_id
            ]
            if assessment == "matched":
                crosscheck_status = "supported"
                crosscheck_confidence = "high"
            elif assessment == "possible-match":
                crosscheck_status = "partially-supported"
                crosscheck_confidence = "medium"
            else:
                crosscheck_status = "unresolved"
                crosscheck_confidence = "unknown"
            claims.append(
                claim(
                    slug,
                    "identity-crosscheck",
                    "fixed-public-datasets",
                    (
                        f"{profile['name']} was cross-checked against all fixed "
                        f"public datasets; result={assessment}."
                    ),
                    crosscheck_status,
                    crosscheck_confidence,
                    matched_refs,
                    (
                        f"Matched datasets: {', '.join(matched_dataset_ids) or 'none'}. "
                        "Exact normalized-name matching and aggregation aliases do "
                        "not prove one-to-one vendor cluster identity. A no-match "
                        "result records completed searches, not actor nonexistence."
                    ),
                )
            )
        for alias in profile["actor"].get("aliases", []):
            refs = alias.get("evidence_refs", [])
            tier = evidence_tier(refs, source_by_id)
            status = (
                "supported"
                if tier in {"authoritative", "knowledge-base", "research"}
                and alias.get("scope") != "unknown"
                else "partially-supported"
                if refs
                else "unresolved"
            )
            claims.append(
                claim(
                    slug,
                    "alias",
                    normalized_name(alias["name"]),
                    f"{alias['name']} is associated with {profile['name']} with scope {alias.get('scope', 'unknown')}.",
                    status,
                    alias.get("confidence", "unknown"),
                    refs,
                    f"Evidence tier={tier}; vendor scope must be preserved.",
                )
            )
        attribution = profile.get("attribution", {})
        refs = attribution.get("evidence_refs", [])
        if attribution.get("countries"):
            tier = evidence_tier(refs, source_by_id)
            attribution_status, _ = verification_from_refs(refs, source_by_id)
            claims.append(
                claim(
                    slug,
                    "attribution",
                    "countries",
                    f"Attributed country or countries: {', '.join(attribution['countries'])}.",
                    attribution_status,
                    attribution.get("confidence", "unknown"),
                    refs,
                    f"Evidence tier={tier}. Community workbook-only attribution requires independent corroboration.",
                )
            )
        if attribution.get("sponsor_type") != "unknown":
            sponsor_status, sponsor_tier = verification_from_refs(
                attribution.get("evidence_refs", []), source_by_id
            )
            claims.append(
                claim(
                    slug,
                    "attribution",
                    "sponsor-type",
                    f"Sponsor classification: {attribution['sponsor_type']}.",
                    sponsor_status,
                    attribution.get("confidence", "unknown"),
                    attribution.get("evidence_refs", []),
                    f"Evidence tier={sponsor_tier}; sponsor classification is audited separately from country labels.",
                )
            )
        for organization in attribution.get("organizations", []):
            organization_refs = organization.get("evidence_refs", [])
            organization_status, organization_tier = verification_from_refs(
                organization_refs, source_by_id
            )
            claims.append(
                claim(
                    slug,
                    "attribution-organization",
                    organization["id"],
                    f"{profile['name']} has relationship {organization['relationship']} with {organization['name']}.",
                    organization_status,
                    organization.get("confidence", "unknown"),
                    organization_refs,
                    f"Evidence tier={organization_tier}; organization relationship is distinct from country attribution.",
                )
            )
        if "Supersedes the workbook-only China attribution" in attribution.get(
            "analyst_notes", ""
        ):
            claims.append(
                claim(
                    slug,
                    "attribution-counterevidence",
                    "workbook-china-attribution",
                    (
                        f"The former workbook-only China attribution for "
                        f"{profile['name']} is superseded."
                    ),
                    "superseded",
                    "high" if profile["name"] in {"APT-C-27", "APT-C-37"} else "medium",
                    attribution.get("evidence_refs", []),
                    attribution.get("analyst_notes", ""),
                    counterevidence=[
                        "The former assessment was inferred from workbook worksheet placement."
                    ],
                )
            )
        for motivation in profile.get("motivations", []):
            motivation_refs = motivation.get("evidence_refs", [])
            motivation_status, motivation_tier = verification_from_refs(
                motivation_refs, source_by_id
            )
            claims.append(
                claim(
                    slug,
                    "motivation",
                    motivation["type"],
                    f"{profile['name']} has motivation {motivation['type']}: {motivation['description']}",
                    motivation_status,
                    motivation.get("confidence", "unknown"),
                    motivation_refs,
                    f"Evidence tier={motivation_tier}; motivation is not inferred from sponsorship.",
                )
            )
        for relationship in profile.get("relationships", []):
            refs = relationship.get("evidence_refs", [])
            notes = relationship.get("analyst_notes", "")
            if notes.startswith("Verified OSINT relationship:"):
                status = (
                    "partially-supported"
                    if "status=partially-supported" in notes
                    else "supported"
                )
            elif notes.startswith("MITRE relationship extraction:"):
                status = (
                    "supported"
                    if "status=supported" in notes
                    else "partially-supported"
                )
            elif relationship.get("confidence") == "low":
                status = "unresolved"
            else:
                status = "partially-supported"
            claims.append(
                claim(
                    slug,
                    "relationship",
                    relationship["relationship_id"],
                    f"{profile['name']} {relationship['relationship_type']} {relationship['target_actor']}: {relationship['description']}",
                    status,
                    relationship.get("confidence", "unknown"),
                    refs,
                    notes or "Relationship requires source-scope review.",
                    counterevidence=[notes] if "counterevidence=" in notes else [],
                )
            )
        for field in (
            "malware",
            "tools",
            "infrastructure",
            "delivery_formats",
            "vulnerabilities",
            "operational_capabilities",
        ):
            for item in profile.get("capabilities", {}).get(field, []):
                refs = item.get("evidence_refs", [])
                tier = evidence_tier(refs, source_by_id)
                capability_status, _ = verification_from_refs(refs, source_by_id)
                claims.append(
                    claim(
                        slug,
                        f"capability-{field}",
                        item["id"],
                        f"{profile['name']} uses or has used {item['name']}.",
                        capability_status,
                        item.get("confidence", "unknown"),
                        refs,
                        f"Evidence tier={tier}.",
                    )
                )
        for activity in profile.get("activities", []):
            activity_refs = activity.get("evidence_refs", [])
            activity_status, activity_tier = verification_from_refs(
                activity_refs, source_by_id
            )
            claims.append(
                claim(
                    slug,
                    "activity",
                    activity["activity_id"],
                    f"{profile['name']} conducted or is associated with {activity['name']}: {activity['description']}",
                    activity_status,
                    activity.get("confidence", "unknown"),
                    activity_refs,
                    f"Evidence tier={activity_tier}; observation dates remain separate from report dates.",
                )
            )
        for victim_case in profile.get("victim_cases", []):
            victim_refs = victim_case.get("evidence_refs", [])
            victim_status, victim_tier = verification_from_refs(
                victim_refs, source_by_id
            )
            claims.append(
                claim(
                    slug,
                    "victim-case",
                    victim_case["victim_case_id"],
                    f"{profile['name']} victim case {victim_case['victim_name']} has status {victim_case['case_status']}.",
                    victim_status,
                    victim_case.get("confidence", "unknown"),
                    victim_refs,
                    f"Evidence tier={victim_tier}; allegation and confirmation status are preserved.",
                )
            )
        target_labels = {
            "countries": "country",
            "regions": "region",
            "sectors": "sector",
            "roles": "role",
        }
        for target_kind, target_label in target_labels.items():
            for target in profile.get("targets", {}).get(target_kind, []):
                target_refs = target.get("evidence_refs", [])
                target_status, target_tier = verification_from_refs(
                    target_refs, source_by_id
                )
                claims.append(
                    claim(
                        slug,
                        f"target-{target_label}",
                        target["id"],
                        f"{profile['name']} targets {target_label} {target['name']}.",
                        target_status,
                        target.get("confidence", "unknown"),
                        target_refs,
                        f"Evidence tier={target_tier}; attribution and infrastructure geography are not targeting evidence.",
                    )
                )
        for item in profile.get("ttps", []):
            refs = item.get("evidence_refs", [])
            tier = evidence_tier(refs, source_by_id)
            ttp_status, _ = verification_from_refs(refs, source_by_id)
            claims.append(
                claim(
                    slug,
                    "ttp",
                    item["ttp_id"],
                    f"{profile['name']} exhibits {item['technique_id']} {item['technique_name']}.",
                    ttp_status,
                    item.get("confidence", "unknown"),
                    refs,
                    f"Evidence tier={tier}; activity-level context may still be incomplete.",
                )
            )
        for judgment in profile.get("assessment", {}).get("key_judgments", []):
            judgment_refs = judgment.get("evidence_refs", [])
            judgment_status, judgment_tier = verification_from_refs(
                judgment_refs, source_by_id
            )
            claims.append(
                claim(
                    slug,
                    "assessment",
                    stable_digest(judgment.get("statement", ""))[:16],
                    judgment.get("statement", ""),
                    judgment_status,
                    judgment.get("confidence", "unknown"),
                    judgment_refs,
                    f"Evidence tier={judgment_tier}; analyst judgment remains distinct from source wording.",
                )
            )
        status_counts = Counter(item["verification_status"] for item in claims)
        collection_counts.update(status_counts)
        audit = {
            "schema_version": "1.0.0",
            "actor_ref": profile["profile_id"],
            "generated_at": utc_now(),
            "status_values": [
                "supported",
                "partially-supported",
                "contradicted",
                "unresolved",
                "superseded",
            ],
            "counts": dict(status_counts),
            "claims": claims,
        }
        write_json_atomic(profiles_root / slug / "claim-audit.json", audit)
        actors.append(
            {
                "slug": slug,
                "name": profile["name"],
                "claim_count": len(claims),
                "counts": dict(status_counts),
            }
        )
    if not selected_slugs:
        active_slugs = {actor["slug"] for actor in catalog_actors}
        for profile_path in sorted(profiles_root.glob("*/actor-profile.json")):
            slug = profile_path.parent.name
            if slug in active_slugs:
                continue
            profile = load_json(profile_path)
            if profile.get("status") != "deprecated":
                continue
            tombstone_claim = claim(
                slug,
                "lifecycle",
                "deprecated-profile",
                f"Legacy profile {profile['name']} is deprecated and must not be used as an active canonical actor.",
                "superseded",
                "high",
                [],
                profile.get("actor", {}).get("analyst_notes")
                or "The profile is retained only as a stable legacy tombstone.",
            )
            write_json_atomic(
                profile_path.parent / "claim-audit.json",
                {
                    "schema_version": "1.0.0",
                    "actor_ref": profile["profile_id"],
                    "generated_at": utc_now(),
                    "status_values": [
                        "supported",
                        "partially-supported",
                        "contradicted",
                        "unresolved",
                        "superseded",
                    ],
                    "counts": {"superseded": 1},
                    "claims": [tombstone_claim],
                },
            )
    summary = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "actor_count": len(actors),
        "claim_count": sum(item["claim_count"] for item in actors),
        "counts": dict(collection_counts),
        "actors": actors,
    }
    # A filtered run intentionally leaves the full collection summary untouched;
    # otherwise it would be replaced by a misleading partial collection.
    if not selected_slugs:
        write_json_atomic(args.output.resolve(), summary)
    print(json.dumps({key: summary[key] for key in ("actor_count", "claim_count", "counts")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
