#!/usr/bin/env python3
"""Apply approved daily review records deterministically."""

from __future__ import annotations

import argparse
import copy
import csv
import json
import subprocess
import sys
from collections import defaultdict
from io import StringIO
from pathlib import Path
from typing import Any

from daily_common import (
    load_json,
    utc_now,
    write_json_if_changed,
    write_text_atomic,
)
from daily_materializer import (
    activity_entry,
    artifact_columns,
    build_ledger,
    ensure_malware_capabilities,
    finalize_dataset,
    load_artifact_rows,
    merge_artifacts,
    merge_ioc_record,
    profile_source,
    remove_daily_materialization,
    source_id_for_value,
    source_items,
)


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
sys.path.insert(0, str(REPO_ROOT / "actor_profile" / "scripts"))
import common as profile_common  # noqa: E402


def semantic_copy(value: dict[str, Any], volatile_key: str) -> dict[str, Any]:
    result = copy.deepcopy(value)
    result.pop(volatile_key, None)
    return result


def write_artifacts_if_changed(
    path: Path, rows: list[dict[str, str]]
) -> bool:
    columns = artifact_columns()
    stream = StringIO()
    writer = csv.DictWriter(stream, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    content = stream.getvalue()
    if path.exists() and path.read_text(encoding="utf-8-sig") == content:
        return False
    write_text_atomic(path, content)
    return True


def process_profile(profile_dir: Path) -> dict[str, Any]:
    profile = profile_dir / "actor-profile.json"
    iocs = profile_dir / "iocs.json"
    artifacts = profile_dir / "artifacts.csv"
    commands = [
        [
            sys.executable,
            str(REPO_ROOT / "actor_profile" / "scripts" / "render_profile.py"),
            str(profile),
            "--iocs",
            str(iocs),
            "--artifacts",
            str(artifacts),
        ],
        [
            sys.executable,
            str(REPO_ROOT / "actor_profile" / "scripts" / "validate_profile.py"),
            str(profile),
            "--iocs",
            str(iocs),
            "--artifacts",
            str(artifacts),
            "--stix",
            str(profile_dir / "generated" / "profile.stix2.json"),
            "--json-output",
        ],
    ]
    result: dict[str, Any] = {"render": 0, "validate": 0, "validation": {}}
    for index, command in enumerate(commands):
        completed = subprocess.run(
            command,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        key = "render" if index == 0 else "validate"
        result[key] = completed.returncode
        if index == 1:
            try:
                validation = json.loads(completed.stdout)
                result["validation"] = {
                    "valid": validation.get("valid", False),
                    "counts": validation.get("counts", {}),
                    "errors": [
                        item
                        for item in validation.get("issues", [])
                        if item.get("severity") == "error"
                    ][:20],
                }
            except json.JSONDecodeError:
                result["validation"] = {
                    "stdout": completed.stdout,
                    "stderr": completed.stderr,
                }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queue", type=Path)
    parser.add_argument("--profiles-root", type=Path, default=REPO_ROOT / "profiles")
    parser.add_argument("--apply", action="store_true", help="write changes; default is dry-run")
    parser.add_argument("--actor", action="append", help="limit to actor slug; repeatable")
    parser.add_argument(
        "--rebuild-daily",
        action="store_true",
        help="remove the previously materialized daily slice before applying the queue",
    )
    parser.add_argument(
        "--no-render",
        action="store_true",
        help="skip Markdown/STIX regeneration; derived files may then be stale",
    )
    args = parser.parse_args()

    queue = load_json(args.queue.resolve())
    if args.rebuild_daily and (
        queue.get("source", {}).get("since")
        or queue.get("source", {}).get("until")
    ):
        raise SystemExit(
            "--rebuild-daily requires a full-history queue without --since/--until"
        )
    wanted = set(args.actor or [])
    approved = [
        item
        for item in queue["records"]
        if item.get("review_status") == "approved"
        and (not wanted or item["actor"]["slug"] in wanted)
    ]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in approved:
        grouped[record["actor"]["slug"]].append(record)
    summary: dict[str, Any] = {
        "mode": "apply" if args.apply else "dry-run",
        "rebuild_daily": args.rebuild_daily,
        "approved_records": len(approved),
        "actors": {},
    }
    if not args.apply:
        for slug, records in sorted(grouped.items()):
            summary["actors"][slug] = {
                "records": len(records),
                "ioc_observations": sum(len(item.get("iocs", [])) for item in records),
                "approved_artifacts": sum(
                    artifact.get("review_status") == "approved"
                    for item in records
                    for artifact in item.get("artifacts", [])
                ),
                "approved_capabilities": sum(
                    capability.get("status") == "approved"
                    for item in records
                    for capability in item.get("capability_decisions", [])
                ),
            }
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    failures = 0
    for slug, records in sorted(grouped.items()):
        profile_dir = args.profiles_root.resolve() / slug
        profile_path = profile_dir / "actor-profile.json"
        iocs_path = profile_dir / "iocs.json"
        artifacts_path = profile_dir / "artifacts.csv"
        if not all(path.exists() for path in (profile_path, iocs_path, artifacts_path)):
            summary["actors"][slug] = {"error": "required profile outputs are missing"}
            failures += 1
            continue

        profile = load_json(profile_path)
        dataset = load_json(iocs_path)
        artifact_rows = load_artifact_rows(artifacts_path)
        profile_before = semantic_copy(profile, "updated_at")
        dataset_before = semantic_copy(dataset, "generated_at")
        artifacts_before = copy.deepcopy(artifact_rows)

        if args.rebuild_daily:
            artifact_rows = remove_daily_materialization(
                profile, dataset, artifact_rows
            )

        for record in sorted(records, key=lambda item: item["record_id"]):
            sources = source_items(record, queue)
            evidence_refs = [source_id_for_value(item["url"]) for item in sources]
            source_indexes = {
                item["source_id"]: index
                for index, item in enumerate(profile.get("sources", []))
            }
            for source in sources:
                modeled = profile_source(record, source, queue)
                if modeled["source_id"] in source_indexes:
                    profile["sources"][source_indexes[modeled["source_id"]]] = modeled
                else:
                    profile["sources"].append(modeled)
                    source_indexes[modeled["source_id"]] = len(profile["sources"]) - 1
            ensure_malware_capabilities(profile, record, evidence_refs)
            activity = activity_entry(record, evidence_refs)
            activities = {
                item["activity_id"]: index
                for index, item in enumerate(profile["activities"])
            }
            if activity["activity_id"] in activities:
                profile["activities"][activities[activity["activity_id"]]] = activity
            else:
                profile["activities"].append(activity)
            merge_ioc_record(dataset, record, queue, profile_common)
            artifact_rows = merge_artifacts(
                artifact_rows,
                record,
                queue,
                profile["profile_id"],
                profile_common,
            )

        profile["sources"].sort(key=lambda item: item["source_id"])
        profile["activities"].sort(
            key=lambda item: (
                item.get("first_observed", {}).get("value") or "",
                item["activity_id"],
            )
        )
        profile["capabilities"]["malware"].sort(key=lambda item: item["id"])
        finalize_dataset(dataset)

        profile_changed = semantic_copy(profile, "updated_at") != profile_before
        dataset_changed = semantic_copy(dataset, "generated_at") != dataset_before
        artifacts_changed = artifact_rows != artifacts_before
        now = utc_now()
        if profile_changed:
            profile["updated_at"] = now
        if dataset_changed:
            dataset["generated_at"] = now

        ledger_path = profile_dir / "daily-observations.json"
        existing_ledger = load_json(ledger_path) if ledger_path.exists() else None
        ledger = build_ledger(
            existing_ledger,
            profile["profile_id"],
            records,
            queue["source"]["commit"],
            now,
            rebuild=args.rebuild_daily,
        )
        if existing_ledger:
            comparable = semantic_copy(ledger, "updated_at")
            if comparable == semantic_copy(existing_ledger, "updated_at"):
                ledger["updated_at"] = existing_ledger.get("updated_at", now)

        written = {
            "profile": write_json_if_changed(profile_path, profile),
            "iocs": write_json_if_changed(iocs_path, dataset),
            "artifacts": (
                write_artifacts_if_changed(artifacts_path, artifact_rows)
                if artifacts_changed
                else False
            ),
            "ledger": write_json_if_changed(ledger_path, ledger),
        }
        result: dict[str, Any] = {"written": written}
        changed_primary = any(written.values())
        if not args.no_render and changed_primary:
            result["processing"] = process_profile(profile_dir)
            counts = result["processing"].get("validation", {}).get("counts", {})
            if result["processing"]["render"] or counts.get("error", 1):
                failures += 1
        elif not args.no_render:
            result["processing"] = {"skipped": "no semantic changes"}
        else:
            result["derived_outputs_stale"] = changed_primary
        summary["actors"][slug] = result

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
