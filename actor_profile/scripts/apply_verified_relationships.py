#!/usr/bin/env python3
"""Apply reviewed OSINT relationship research to both actor profiles."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from common import load_json, stable_digest, unknown_time, utc_now, write_json_atomic


NOTE_PREFIX = "Verified OSINT relationship:"


def merge_source(profile: dict[str, Any], source: dict[str, Any]) -> None:
    positions = {
        item["source_id"]: index for index, item in enumerate(profile["sources"])
    }
    if source["source_id"] in positions:
        profile["sources"][positions[source["source_id"]]] = source
    else:
        profile["sources"].append(source)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "research",
        type=Path,
        default=Path("actor_profile/osint/verified-relationships.json"),
        nargs="?",
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument(
        "--tracker", type=Path, default=Path("profiles/osint-progress.json")
    )
    args = parser.parse_args()
    research = load_json(args.research)
    sources = {item["source_id"]: item for item in research["sources"]}
    profiles_root = args.profiles_root.resolve()
    updated: set[str] = set()
    integrated_claims: dict[str, set[str]] = {}
    verified_source_ids: dict[str, set[str]] = {}

    for relation in research["relationships"]:
        for source_slug, target_slug, reciprocal in (
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
            target = load_json(profiles_root / target_slug / "actor-profile.json")
            profile = load_json(path)
            for source_id in relation["evidence_refs"]:
                merge_source(profile, sources[source_id])
            relationship_id = (
                "relationship--"
                + source_slug
                + "--"
                + reciprocal
                + "--"
                + stable_digest(source_slug, target_slug, reciprocal)[:16]
            )
            record = {
                "relationship_id": relationship_id,
                "target_actor": target["name"],
                "relationship_type": reciprocal,
                "description": relation["description"],
                "confidence": relation["confidence"],
                "first_observed": unknown_time(),
                "last_observed": unknown_time(),
                "evidence_refs": relation["evidence_refs"],
                "analyst_notes": (
                    f"{NOTE_PREFIX} status={relation['verification_status']}; "
                    f"limitation={relation['limitations']} "
                    f"counterevidence={relation['counterevidence']}"
                ),
            }
            retained = [
                item
                for item in profile.get("relationships", [])
                if item["relationship_id"] != relationship_id
            ]
            profile["relationships"] = retained + [record]
            judgment = {
                "statement": relation["description"],
                "confidence": relation["confidence"],
                "evidence_refs": relation["evidence_refs"],
                "analyst_notes": (
                    f"verification_status={relation['verification_status']}; "
                    f"{relation['limitations']} {relation['counterevidence']}"
                ),
            }
            if judgment not in profile["assessment"]["key_judgments"]:
                profile["assessment"]["key_judgments"].append(judgment)
            profile["updated_at"] = utc_now()
            write_json_atomic(path, profile)
            updated.add(source_slug)
            integrated_claims.setdefault(source_slug, set()).add(relationship_id)
            verified_source_ids.setdefault(source_slug, set()).update(
                relation["evidence_refs"]
            )
    if args.tracker.exists():
        tracker = load_json(args.tracker)
        by_slug = {item["slug"]: item for item in tracker["actors"]}
        for slug in updated:
            item = by_slug[slug]
            item["status"] = "integrated"
            item["last_searched_at"] = utc_now()
            item["queries"] = list(
                dict.fromkeys(
                    [
                        *item["queries"],
                        f"{slug} threat actor relationship official sources",
                    ]
                )
            )
            known_urls = {
                source.get("url") for source in item["verified_sources"]
            }
            for source_id in sorted(verified_source_ids.get(slug, set())):
                source = sources[source_id]
                if source.get("url") not in known_urls:
                    item["verified_sources"].append(
                        {
                            "url": source["url"],
                            "title": source["title"],
                            "publisher": source["publisher"],
                            "published_at": source["published_at"],
                            "source_id": source_id,
                        }
                    )
                    known_urls.add(source.get("url"))
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
    print(
        json.dumps(
            {
                "relationships": len(research["relationships"]),
                "profiles_updated": len(updated),
                "profiles": sorted(updated),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
