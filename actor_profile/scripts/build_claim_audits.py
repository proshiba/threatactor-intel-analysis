#!/usr/bin/env python3
"""Build per-profile claim verification ledgers and a collection summary."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import normalized_name
from common import load_json, stable_digest, utc_now, write_json_atomic


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
    types = {
        source_by_id[ref].get("source_type", "")
        for ref in refs
        if ref in source_by_id
    }
    publishers = {
        source_by_id[ref].get("publisher", "")
        for ref in refs
        if ref in source_by_id
    }
    if any("government" in item or "legal" in item for item in types):
        return "authoritative"
    if "MITRE" in publishers or "MITRE ATT&CK" in publishers:
        return "knowledge-base"
    if any(item in {"vendor-research", "report"} for item in types):
        return "research"
    if refs:
        return "repository"
    return "none"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument(
        "--output", type=Path, default=Path("profiles/claim-audit-summary.json")
    )
    args = parser.parse_args()
    catalog = load_json(args.catalog)
    profiles_root = args.profiles_root.resolve()
    collection_counts: Counter[str] = Counter()
    actors: list[dict[str, Any]] = []

    for actor in catalog["actors"]:
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
            or "attack-index.json" in source.get("path", "")
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
            claims.append(
                claim(
                    slug,
                    "attribution",
                    "countries",
                    f"Attributed country or countries: {', '.join(attribution['countries'])}.",
                    (
                        "supported"
                        if tier in {"authoritative", "knowledge-base", "research"}
                        else "partially-supported"
                    ),
                    attribution.get("confidence", "unknown"),
                    refs,
                    f"Evidence tier={tier}. Community workbook-only attribution requires independent corroboration.",
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
        for field in ("malware", "tools", "infrastructure"):
            for item in profile.get("capabilities", {}).get(field, []):
                refs = item.get("evidence_refs", [])
                tier = evidence_tier(refs, source_by_id)
                claims.append(
                    claim(
                        slug,
                        f"capability-{field}",
                        item["id"],
                        f"{profile['name']} uses or has used {item['name']}.",
                        "supported" if tier in {"authoritative", "knowledge-base", "research"} else "partially-supported",
                        item.get("confidence", "unknown"),
                        refs,
                        f"Evidence tier={tier}.",
                    )
                )
        for item in profile.get("ttps", []):
            refs = item.get("evidence_refs", [])
            tier = evidence_tier(refs, source_by_id)
            claims.append(
                claim(
                    slug,
                    "ttp",
                    item["ttp_id"],
                    f"{profile['name']} exhibits {item['technique_id']} {item['technique_name']}.",
                    "supported" if tier in {"authoritative", "knowledge-base", "research"} else "partially-supported",
                    item.get("confidence", "unknown"),
                    refs,
                    f"Evidence tier={tier}; activity-level context may still be incomplete.",
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
    summary = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "actor_count": len(actors),
        "claim_count": sum(item["claim_count"] for item in actors),
        "counts": dict(collection_counts),
        "actors": actors,
    }
    write_json_atomic(args.output.resolve(), summary)
    print(json.dumps({key: summary[key] for key in ("actor_count", "claim_count", "counts")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
