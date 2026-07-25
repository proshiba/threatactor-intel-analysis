#!/usr/bin/env python3
"""Extract cross-group relationships explicitly described by MITRE ATT&CK."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from common import load_json, stable_digest, unknown_time, utc_now, write_json_atomic


GROUP_LINK_RE = re.compile(
    r"\[([^\]]+)\]\(https://attack\.mitre\.org/groups/(G\d{4})\)"
)
NOTE_PREFIX = "MITRE relationship extraction:"


def relation_type(text: str) -> tuple[str, str, str]:
    lower = text.casefold()
    if any(marker in lower for marker in ("sub-set of", "subset of", "subgroup of")):
        return "part-of", "high", "supported"
    if "assist" in lower or "collaborat" in lower or "cooperat" in lower:
        return "cooperates-with", "high", "supported"
    if "overlap" in lower:
        return "overlaps-with", "high", "supported"
    if "shared" in lower or "similar" in lower or "linked" in lower:
        return "related-to", "medium", "partially-supported"
    return "related-to", "medium", "partially-supported"


def context(text: str, start: int, end: int) -> str:
    left_candidates = [text.rfind(marker, 0, start) for marker in (". ", "\n")]
    left = max(left_candidates)
    left = 0 if left < 0 else left + 1
    right_candidates = [
        value for value in (text.find(". ", end), text.find("\n", end)) if value >= 0
    ]
    right = min(right_candidates) + 1 if right_candidates else min(len(text), end + 500)
    return " ".join(text[left:right].split())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--attack", type=Path, default=Path("actor_profile/reference/attack-index.json")
    )
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("actor_profile/osint/mitre-described-relationships.json"),
    )
    parser.add_argument(
        "--tracker", type=Path, default=Path("profiles/osint-progress.json")
    )
    args = parser.parse_args()
    attack = load_json(args.attack)
    catalog = load_json(args.catalog)
    by_mitre = {
        item["mitre_group_id"]: item
        for item in catalog["actors"]
        if item.get("mitre_group_id")
    }
    profiles_root = args.profiles_root.resolve()
    candidates: dict[tuple[str, str], dict[str, Any]] = {}
    for source_id, group in attack["groups"].items():
        if source_id not in by_mitre:
            continue
        for match in GROUP_LINK_RE.finditer(group.get("description", "")):
            target_id = match.group(2)
            if target_id == source_id or target_id not in by_mitre:
                continue
            excerpt = context(group["description"], match.start(), match.end())
            kind, confidence, status = relation_type(excerpt)
            source_slug = by_mitre[source_id]["slug"]
            target_slug = by_mitre[target_id]["slug"]
            key = (source_slug, target_slug)
            candidate = {
                "source_actor_slug": source_slug,
                "target_actor_slug": target_slug,
                "source_mitre_id": source_id,
                "target_mitre_id": target_id,
                "relationship_type": kind,
                "confidence": confidence,
                "verification_status": status,
                "description": excerpt,
                "evidence_refs": ["source--mitre-attack-19-1"],
                "limitations": (
                    "A narrative cross-reference establishes a relationship but "
                    "does not by itself prove exact actor identity or identical scope."
                ),
            }
            existing = candidates.get(key)
            if existing is None or (
                existing["verification_status"] == "partially-supported"
                and status == "supported"
            ):
                candidates[key] = candidate

    updated: set[str] = set()
    integrated_claims: dict[str, set[str]] = {}
    source_group_for_slug: dict[str, str] = {}
    for relation in candidates.values():
        for source_slug, target_slug, kind in (
            (
                relation["source_actor_slug"],
                relation["target_actor_slug"],
                relation["relationship_type"],
            ),
            (
                relation["target_actor_slug"],
                relation["source_actor_slug"],
                "related-to"
                if relation["relationship_type"] == "part-of"
                else relation["relationship_type"],
            ),
        ):
            path = profiles_root / source_slug / "actor-profile.json"
            profile = load_json(path)
            target = load_json(profiles_root / target_slug / "actor-profile.json")
            available_source_ids = {
                item["source_id"] for item in profile.get("sources", [])
            }
            profile_evidence_refs = [
                source_id
                for source_id in relation["evidence_refs"]
                if source_id in available_source_ids
            ]
            if not profile_evidence_refs:
                profile_evidence_refs = [
                    item["source_id"]
                    for item in profile.get("sources", [])
                    if item.get("publisher") in {"MITRE", "MITRE ATT&CK"}
                ][:1]
            # A manually reviewed relationship between the same actors wins.
            if any(
                item.get("target_actor") == target["name"]
                and item.get("analyst_notes", "").startswith(
                    "Verified OSINT relationship:"
                )
                for item in profile.get("relationships", [])
            ):
                continue
            relation_id = (
                "relationship--"
                + source_slug
                + "--mitre--"
                + stable_digest(source_slug, target_slug, kind)[:16]
            )
            record = {
                "relationship_id": relation_id,
                "target_actor": target["name"],
                "relationship_type": kind,
                "description": relation["description"],
                "confidence": relation["confidence"],
                "first_observed": unknown_time(),
                "last_observed": unknown_time(),
                "evidence_refs": profile_evidence_refs,
                "analyst_notes": (
                    f"{NOTE_PREFIX} status={relation['verification_status']}; "
                    f"{relation['limitations']}"
                ),
            }
            retained = [
                item
                for item in profile.get("relationships", [])
                if item["relationship_id"] != relation_id
            ]
            profile["relationships"] = retained + [record]
            profile["updated_at"] = utc_now()
            write_json_atomic(path, profile)
            updated.add(source_slug)
            integrated_claims.setdefault(source_slug, set()).add(relation_id)
            source_group_for_slug[source_slug] = relation["source_mitre_id"]
    if args.tracker.exists():
        tracker = load_json(args.tracker)
        by_slug = {item["slug"]: item for item in tracker["actors"]}
        for slug in updated:
            item = by_slug[slug]
            item["status"] = "integrated"
            item["last_searched_at"] = utc_now()
            group_id = source_group_for_slug[slug]
            url = f"https://attack.mitre.org/groups/{group_id}/"
            item["queries"] = list(
                dict.fromkeys(
                    [
                        *item["queries"],
                        f"MITRE ATT&CK {group_id} cross-group relationships",
                    ]
                )
            )
            if url not in {
                source.get("url") for source in item["verified_sources"]
            }:
                item["verified_sources"].append(
                    {
                        "url": url,
                        "title": f"MITRE ATT&CK group {group_id}",
                        "publisher": "MITRE ATT&CK",
                        "source_id": "source--mitre-attack-19-1",
                    }
                )
            item["claims_integrated"] = list(
                dict.fromkeys(
                    [
                        *item["claims_integrated"],
                        *sorted(integrated_claims.get(slug, set())),
                    ]
                )
            )
        tracker["updated_at"] = utc_now()
        write_json_atomic(args.tracker, tracker)
    output = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "source": "MITRE Enterprise ATT&CK 19.1 compact local index",
        "relationship_count": len(candidates),
        "relationships": sorted(
            candidates.values(),
            key=lambda item: (
                item["source_actor_slug"],
                item["target_actor_slug"],
            ),
        ),
    }
    write_json_atomic(args.output.resolve(), output)
    print(
        json.dumps(
            {
                "relationships": len(candidates),
                "profiles_updated": len(updated),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
