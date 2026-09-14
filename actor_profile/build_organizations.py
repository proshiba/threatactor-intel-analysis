#!/usr/bin/env python3
"""関与組織レジストリ actor_profile/organizations.json を生成・更新する。

profiles/<slug>/actor-profile.json の attribution.organizations を機械的に集約し、
組織側から関与アクターを逆引きできる形へ変換する。既存の記述は要約せず原文のまま
relationship / analyst_notes へ転記する。

レジストリに固有の情報（organization_type、country、legal_entity、profile_slug、
手入力の組織）は curated_organizations.json 側に持ち、生成のたびに失われないようにする。

    python3 actor_profile/build_organizations.py            # 差分を表示
    python3 actor_profile/build_organizations.py --apply    # 書き出す
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILES = ROOT / "profiles"
CURATED = ROOT / "actor_profile" / "curated-organizations.json"
OUT = ROOT / "actor_profile" / "organizations.json"

SCHEMA_VERSION = "1.0.0"


def normalize_id(raw: str) -> str:
    """org--x と organization--x の表記揺れを organization--x へ寄せる。"""
    if raw.startswith("organization--"):
        return raw
    if raw.startswith("org--"):
        return "organization--" + raw[len("org--") :]
    return "organization--" + raw.lstrip("-")


def collect_from_profiles() -> dict[str, dict]:
    """profiles/ の attribution.organizations を組織IDで集約する。"""
    found: dict[str, dict] = {}
    for path in sorted(PROFILES.glob("*/actor-profile.json")):
        slug = path.parent.name
        data = json.loads(path.read_text(encoding="utf-8"))
        orgs = (data.get("attribution") or {}).get("organizations") or []
        for org in orgs:
            raw_id = org.get("id") or ""
            oid = normalize_id(raw_id)
            entry = found.setdefault(
                oid,
                {
                    "organization_id": oid,
                    "primary_name": org.get("name", ""),
                    "legacy_ids": set(),
                    "related_actors": [],
                },
            )
            entry["legacy_ids"].add(raw_id)
            # 同一組織が複数プロファイルから異なる表記で参照されることがある。
            # 最初に現れた表記を primary_name とし、差異は related_actors 側へ残す。
            entry["related_actors"].append(
                {
                    "slug": slug,
                    "relation": org.get("relationship", ""),
                    "confidence": org.get("confidence", "unknown"),
                    "name_as_written": org.get("name", ""),
                    "evidence_refs": org.get("evidence_refs") or [],
                    "analyst_notes": org.get("analyst_notes") or "",
                }
            )
    for entry in found.values():
        entry["legacy_ids"] = sorted(entry["legacy_ids"])
        entry["related_actors"].sort(key=lambda r: r["slug"])
    return found


def build() -> dict:
    curated_doc = json.loads(CURATED.read_text(encoding="utf-8"))
    curated = {c["organization_id"]: c for c in curated_doc["organizations"]}
    derived = collect_from_profiles()

    organizations = []
    for oid in sorted(set(curated) | set(derived)):
        c = curated.get(oid, {})
        d = derived.get(oid, {})
        entry = {
            "organization_id": oid,
            "primary_name": c.get("primary_name") or d.get("primary_name", ""),
            "also_known_as": c.get("also_known_as", []),
            "organization_type": c.get("organization_type", "unknown"),
            "country": c.get("country"),
            "status": c.get("status", "tracking"),
            "profile_slug": c.get("profile_slug"),
            "legacy_ids": d.get("legacy_ids", []),
            "related_actors": d.get("related_actors", []),
            "related_clusters": c.get("related_clusters", []),
            "sources": c.get("sources", []),
            "unresolved_questions": c.get("unresolved_questions", []),
            "analyst_notes": c.get("analyst_notes", ""),
        }
        organizations.append(entry)

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": curated_doc["generated_at"],
        "purpose": curated_doc["purpose"],
        "id_policy": curated_doc["id_policy"],
        "organization_type_vocabulary": curated_doc["organization_type_vocabulary"],
        "status_vocabulary": curated_doc["status_vocabulary"],
        "counts": {
            "organizations": len(organizations),
            "from_profiles": len(derived),
            "curated_only": len(set(curated) - set(derived)),
            "with_profile": sum(1 for o in organizations if o["profile_slug"]),
        },
        "organizations": organizations,
        "analyst_notes": curated_doc["analyst_notes"],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="organizations.json を書き出す")
    args = ap.parse_args()

    doc = build()
    rendered = json.dumps(doc, ensure_ascii=False, indent=2) + "\n"

    if args.apply:
        OUT.write_text(rendered, encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)}")
    else:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        print("差分なし" if current == rendered else "差分あり (--apply で書き出す)")

    print(json.dumps(doc["counts"], ensure_ascii=False))
    multi = [o for o in doc["organizations"] if len(o["related_actors"]) > 1]
    if multi:
        print("複数アクターに関与する組織:")
        for o in multi:
            print(f"  {o['organization_id']}: {[r['slug'] for r in o['related_actors']]}")
    drift = [o for o in doc["organizations"] if len(o["legacy_ids"]) > 1]
    if drift:
        print("ID表記が割れている組織:")
        for o in drift:
            print(f"  {o['organization_id']}: {o['legacy_ids']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
