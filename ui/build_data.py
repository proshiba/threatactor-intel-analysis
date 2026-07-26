#!/usr/bin/env python3
"""Build the compact actor index consumed by the GitHub Pages UI.

Reads every profiles/<slug>/actor-profile.json (plus iocs.json / artifacts.csv
for counts) and writes ui/data/actors.json. Run from anywhere:

    python3 ui/build_data.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = REPO_ROOT / "profiles"
OUT_PATH = Path(__file__).resolve().parent / "data" / "actors.json"

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
CITATION_RE = re.compile(r"\(Citation:[^)]*\)")
SNIPPET_LEN = 240


def plain_snippet(text: str | None) -> str:
    if not text:
        return ""
    text = MD_LINK_RE.sub(r"\1", text)
    text = CITATION_RE.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > SNIPPET_LEN:
        text = text[: SNIPPET_LEN - 1].rstrip() + "…"
    return text


def date_value(field) -> str | None:
    if isinstance(field, dict) and field.get("status") == "known" and field.get("value"):
        return str(field["value"])[:10]
    return None


def load_json(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def count_csv_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh)
        try:
            next(reader)
        except StopIteration:
            return 0
        return sum(1 for _ in reader)


def build_record(slug: str, profile_dir: Path) -> dict | None:
    profile_path = profile_dir / "actor-profile.json"
    if not profile_path.exists():
        return None
    profile = load_json(profile_path)
    actor = profile.get("actor", {})
    attribution = profile.get("attribution", {})
    capabilities = profile.get("capabilities", {})
    targets = profile.get("targets", {})

    aliases = []
    seen = set()
    for alias in actor.get("aliases", []):
        name = alias.get("name") if isinstance(alias, dict) else alias
        if name and name.lower() not in seen:
            seen.add(name.lower())
            aliases.append(name)

    ioc_count = 0
    ioc_types: dict[str, int] = {}
    iocs_path = profile_dir / "iocs.json"
    if iocs_path.exists():
        indicators = load_json(iocs_path).get("indicators", [])
        ioc_count = len(indicators)
        for ind in indicators:
            t = ind.get("type") or "unknown"
            ioc_types[t] = ioc_types.get(t, 0) + 1

    record = {
        "slug": slug,
        "name": profile.get("name") or actor.get("canonical_name") or slug,
        "aliases": aliases,
        "actor_types": actor.get("actor_types", []),
        "active": actor.get("active", "unknown"),
        "first_seen": date_value(actor.get("first_seen")),
        "last_seen": date_value(actor.get("last_seen")),
        "description": plain_snippet(actor.get("description")),
        "attribution": {
            "countries": attribution.get("countries", []),
            "sponsor_type": attribution.get("sponsor_type", "unknown"),
            "confidence": attribution.get("confidence", "unknown"),
        },
        "motivations": sorted({m.get("type") for m in profile.get("motivations", []) if m.get("type")}),
        "target_countries": [t.get("name") for t in targets.get("countries", []) if t.get("name")],
        "target_sectors": [t.get("name") for t in targets.get("sectors", []) if t.get("name")],
        "counts": {
            "aliases": len(aliases),
            "malware": len(capabilities.get("malware", [])),
            "tools": len(capabilities.get("tools", [])),
            "ttps": len(profile.get("ttps", [])),
            "activities": len(profile.get("activities", [])),
            "relationships": len(profile.get("relationships", [])),
            "sources": len(profile.get("sources", [])),
            "iocs": ioc_count,
            "artifacts": count_csv_rows(profile_dir / "artifacts.csv"),
        },
        "ioc_types": ioc_types,
        "updated_at": (profile.get("updated_at") or "")[:10] or None,
    }
    return record


def main() -> int:
    if not PROFILES_DIR.is_dir():
        print(f"profiles directory not found: {PROFILES_DIR}", file=sys.stderr)
        return 1

    records = []
    errors = []
    for profile_dir in sorted(PROFILES_DIR.iterdir()):
        if not profile_dir.is_dir():
            continue
        try:
            record = build_record(profile_dir.name, profile_dir)
        except Exception as exc:  # noqa: BLE001 - report and continue
            errors.append(f"{profile_dir.name}: {exc}")
            continue
        if record:
            records.append(record)

    stats = {
        "actors": len(records),
        "aliases": sum(r["counts"]["aliases"] for r in records),
        "malware_tools": sum(r["counts"]["malware"] + r["counts"]["tools"] for r in records),
        "ttps": sum(r["counts"]["ttps"] for r in records),
        "iocs": sum(r["counts"]["iocs"] for r in records),
        "artifacts": sum(r["counts"]["artifacts"] for r in records),
        "sources": sum(r["counts"]["sources"] for r in records),
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stats": stats,
        "actors": records,
    }
    with OUT_PATH.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write("\n")

    size_kb = OUT_PATH.stat().st_size / 1024
    print(f"wrote {OUT_PATH} ({len(records)} actors, {size_kb:.0f} KiB)")
    if errors:
        print("errors:", file=sys.stderr)
        for line in errors:
            print(f"  {line}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
