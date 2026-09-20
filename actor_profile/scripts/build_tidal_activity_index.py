#!/usr/bin/env python3
"""Build a compact, evidence-linked TIDAL group/campaign/software index.

TIDAL data is an aggregation and is therefore retained as a research lead.  It
must not overwrite canonical actor-profile claims without original-source
review.  This index resolves the reference UUIDs embedded in descriptions so
each lead still points analysts to the cited report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from common import load_json, utc_now, write_json_atomic


TIDAL_LINK_RE = re.compile(
    r"(?:https://app\.tidalcyber\.com)?/(groups|software|references)/"
    r"([0-9a-f]{8}-[0-9a-f-]{27,36})",
    re.IGNORECASE,
)


def linked_uuids(description: str, kind: str) -> list[str]:
    return list(
        dict.fromkeys(
            match.group(2).lower()
            for match in TIDAL_LINK_RE.finditer(description or "")
            if match.group(1).casefold() == kind.casefold()
        )
    )


def reference_urls(
    description: str,
    references: dict[str, dict[str, Any]],
) -> list[str]:
    result: list[str] = []
    for reference_id in linked_uuids(description, "references"):
        reference = references.get(reference_id, {})
        result.extend(
            str(value)
            for value in reference.get("meta", {}).get("refs", [])
            if value
        )
    return list(dict.fromkeys(result))


def source_file(path: Path, dataset: dict[str, Any]) -> dict[str, Any]:
    """Describe an exact local aggregation snapshot used for this index."""

    return {
        "path": path.as_posix(),
        "version": dataset.get("version"),
        "entry_count": len(dataset.get("values", [])),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--groups",
        type=Path,
        default=Path("actor_profile/reference/osint/misp-tidal-groups.json"),
    )
    parser.add_argument(
        "--campaigns",
        type=Path,
        default=Path("actor_profile/reference/osint/misp-tidal-campaigns.json"),
    )
    parser.add_argument(
        "--software",
        type=Path,
        default=Path("actor_profile/reference/osint/misp-tidal-software.json"),
    )
    parser.add_argument(
        "--references",
        type=Path,
        default=Path("actor_profile/reference/osint/misp-tidal-references.json"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("actor_profile/reference/osint/tidal-activity-index.json"),
    )
    args = parser.parse_args()

    raw_groups = load_json(args.groups)
    raw_campaigns = load_json(args.campaigns)
    raw_software = load_json(args.software)
    raw_references = load_json(args.references)
    references = {
        str(item.get("uuid", "")).lower(): item
        for item in raw_references.get("values", [])
        if item.get("uuid")
    }
    group_values = {
        str(item.get("uuid", "")).lower(): item
        for item in raw_groups.get("values", [])
        if item.get("uuid")
    }
    software_values = {
        str(item.get("uuid", "")).lower(): item
        for item in raw_software.get("values", [])
        if item.get("uuid")
    }

    software_by_group: dict[str, list[str]] = defaultdict(list)
    software: dict[str, dict[str, Any]] = {}
    for software_id, item in software_values.items():
        description = str(item.get("description", ""))
        group_refs = list(
            dict.fromkeys(
                [
                    *linked_uuids(description, "groups"),
                    *[
                        str(relation.get("dest-uuid", "")).lower()
                        for relation in item.get("related", [])
                        if relation.get("type") == "used-by"
                        and relation.get("dest-uuid")
                    ],
                ]
            )
        )
        for group_ref in group_refs:
            if group_ref in group_values:
                software_by_group[group_ref].append(software_id)
        software[software_id] = {
            "software_id": software_id,
            "name": item.get("value", ""),
            "description": description,
            "software_type": item.get("meta", {}).get("type", []),
            "platforms": item.get("meta", {}).get("platforms", []),
            "attack_id": item.get("meta", {}).get("software_attack_id"),
            "group_refs": sorted(ref for ref in group_refs if ref in group_values),
            "source_urls": reference_urls(description, references),
        }

    campaigns_by_group: dict[str, list[str]] = defaultdict(list)
    campaigns: dict[str, dict[str, Any]] = {}
    for item in raw_campaigns.get("values", []):
        campaign_id = str(item.get("uuid", "")).lower()
        if not campaign_id:
            continue
        description = str(item.get("description", ""))
        group_refs = [
            ref for ref in linked_uuids(description, "groups") if ref in group_values
        ]
        software_refs = [
            ref
            for ref in linked_uuids(description, "software")
            if ref in software_values
        ]
        for group_ref in group_refs:
            campaigns_by_group[group_ref].append(campaign_id)
        campaigns[campaign_id] = {
            "campaign_id": campaign_id,
            "name": item.get("value", ""),
            "description": description,
            "first_observed": item.get("meta", {}).get("first_seen"),
            "last_observed": item.get("meta", {}).get("last_seen"),
            "group_refs": list(dict.fromkeys(group_refs)),
            "software_refs": list(dict.fromkeys(software_refs)),
            "source_urls": reference_urls(description, references),
            "upstream_source": item.get("meta", {}).get("source"),
        }

    groups: dict[str, dict[str, Any]] = {}
    for group_id, item in group_values.items():
        meta = item.get("meta", {})
        description = str(item.get("description", ""))
        groups[group_id] = {
            "group_id": group_id,
            "name": item.get("value", ""),
            "description": description,
            "country": meta.get("country", []),
            "motivations": meta.get("observed_motivations", []),
            "target_categories": meta.get("target_categories", []),
            "observed_countries": meta.get("observed_countries", []),
            "campaign_refs": sorted(set(campaigns_by_group.get(group_id, []))),
            "software_refs": sorted(set(software_by_group.get(group_id, []))),
            "source_urls": reference_urls(description, references),
        }

    result = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "source": {
            "name": "TIDAL Groups, Campaigns, Software, and References via MISP Galaxy",
            "url": "https://github.com/MISP/misp-galaxy",
            "files": {
                "groups": source_file(args.groups, raw_groups),
                "campaigns": source_file(args.campaigns, raw_campaigns),
                "software": source_file(args.software, raw_software),
                "references": source_file(args.references, raw_references),
            },
            "assessment": (
                "Aggregation-derived research leads; original source URLs must be "
                "reviewed before canonical integration."
            ),
        },
        "counts": {
            "groups": len(groups),
            "campaigns": len(campaigns),
            "campaigns_with_group": sum(
                bool(item["group_refs"]) for item in campaigns.values()
            ),
            "software": len(software),
            "software_with_group": sum(
                bool(item["group_refs"]) for item in software.values()
            ),
            "references": len(references),
        },
        "groups": dict(sorted(groups.items())),
        "campaigns": dict(sorted(campaigns.items())),
        "software": dict(sorted(software.items())),
    }
    write_json_atomic(args.output.resolve(), result)
    print(json.dumps(result["counts"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
