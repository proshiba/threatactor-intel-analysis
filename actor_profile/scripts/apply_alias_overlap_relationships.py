#!/usr/bin/env python3
"""Store shared-alias taxonomy overlaps globally and in actor profiles."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import normalized_name
from common import load_json, stable_digest, unknown_time, utc_now, write_json_atomic


GENERATED_NOTE = (
    "共有aliasに基づくtaxonomy overlap候補。同一主体であることを断定せず、"
    "ベンダーごとの追跡スコープ差を個別に確認する。"
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json")
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("actor_profile/actor-alias-overlaps.json"),
    )
    args = parser.parse_args()

    root = args.repository_root.resolve()
    catalog = load_json((root / args.catalog).resolve())
    actors = {item["slug"]: item for item in catalog["actors"]}
    name_index: dict[str, dict[str, set[str]]] = defaultdict(
        lambda: defaultdict(set)
    )
    for actor in catalog["actors"]:
        for surface in [actor["name"], *actor.get("aliases", [])]:
            key = normalized_name(surface)
            if key:
                name_index[key][actor["slug"]].add(surface)

    pair_aliases: dict[tuple[str, str], set[str]] = defaultdict(set)
    for by_actor in name_index.values():
        if not 1 < len(by_actor) <= 10:
            continue
        for left, right in itertools.combinations(sorted(by_actor), 2):
            pair_aliases[(left, right)].update(by_actor[left])
            pair_aliases[(left, right)].update(by_actor[right])

    relationships: list[dict[str, Any]] = []
    per_actor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for (left, right), aliases in sorted(pair_aliases.items()):
        relation_id = (
            "relationship--alias-overlap--"
            + stable_digest(left, right)[:20]
        )
        relation = {
            "relationship_id": relation_id,
            "source_actor_slug": left,
            "target_actor_slug": right,
            "relationship_type": "taxonomy-overlaps-with",
            "shared_aliases": sorted(aliases, key=str.casefold),
            "confidence": "low",
            "status": "candidate",
            "analyst_notes": GENERATED_NOTE,
        }
        relationships.append(relation)
        for source, target in ((left, right), (right, left)):
            per_actor[source].append(
                {
                    "relationship_id": (
                        "relationship--"
                        + source
                        + "--alias-overlap--"
                        + stable_digest(source, target)[:16]
                    ),
                    "target_actor": actors[target]["name"],
                    "relationship_type": "overlaps-with",
                    "description": (
                        "共有alias: "
                        + ", ".join(sorted(aliases, key=str.casefold))
                    ),
                    "confidence": "low",
                    "first_observed": unknown_time(),
                    "last_observed": unknown_time(),
                    "evidence_refs": [
                        "source--mitre-attack-19-1",
                        "source--actor-mapping-workbook",
                    ],
                    "analyst_notes": GENERATED_NOTE,
                }
            )

    updated = 0
    profiles_root = (root / args.profiles_root).resolve()
    for slug, additions in per_actor.items():
        path = profiles_root / slug / "actor-profile.json"
        profile = load_json(path)
        available_source_ids = [
            item["source_id"] for item in profile.get("sources", [])
        ]
        preferred_evidence = [
            source_id
            for source_id in (
                "source--mitre-attack-19-1",
                "source--actor-mapping-workbook",
            )
            if source_id in available_source_ids
        ]
        evidence_refs = preferred_evidence or available_source_ids[:1]
        for addition in additions:
            addition["evidence_refs"] = evidence_refs
        retained = [
            item
            for item in profile.get("relationships", [])
            if item.get("analyst_notes") != GENERATED_NOTE
        ]
        profile["relationships"] = retained + additions
        profile["updated_at"] = utc_now()
        write_json_atomic(path, profile)
        updated += 1

    output = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "relationship_count": len(relationships),
        "actor_count": len(per_actor),
        "semantics": (
            "Candidate overlap caused by a shared alias. It does not assert "
            "one-to-one actor identity."
        ),
        "relationships": relationships,
    }
    write_json_atomic((root / args.output).resolve(), output)
    print(
        json.dumps(
            {
                "relationships": len(relationships),
                "profiles_updated": updated,
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
