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
    activity_id_override_issue,
    activity_reported_at,
    activity_identity_migration_issues,
    artifact_columns,
    build_ledger,
    canonical_source_url,
    daily_rebuild_dependency_issues,
    ensure_malware_capabilities,
    finalize_dataset,
    generated_activity_id_for,
    load_artifact_rows,
    merge_materialized_source,
    merge_artifacts,
    migrate_cross_file_source_identities,
    migrate_profile_source_identities,
    migrate_source_manifest,
    merge_ioc_record,
    merge_materialized_activity,
    migrate_activity_identities,
    primary_source,
    profile_source,
    profile_source_identity_migration_issues,
    reconcile_profile_source_identity,
    reviewed_reported_at_issue,
    remove_daily_materialization,
    source_id_for_value,
    source_id_for_url,
    source_identity_migration_issues,
    source_manifest_migration_issues,
    source_items,
)


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
sys.path.insert(0, str(REPO_ROOT / "actor_profile" / "scripts"))
import common as profile_common  # noqa: E402
from activity_diamond import materialize_profile_diamonds  # noqa: E402


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


def rebuild_actor_slugs(
    queue: dict[str, Any], profiles_root: Path
) -> set[str]:
    """Return every actor whose prior daily slice belongs to a full rebuild."""
    slugs = {
        record["actor"]["slug"]
        for record in queue.get("records", [])
        if record.get("actor", {}).get("slug")
    }
    if profiles_root.exists():
        slugs.update(
            ledger.parent.name
            for ledger in profiles_root.glob("*/daily-observations.json")
        )
    return slugs


def planned_source_identity_migrations(
    profile: dict[str, Any],
    dataset: dict[str, Any],
    records: list[dict[str, Any]],
    queue: dict[str, Any],
) -> dict[str, str]:
    """Model Source reconciliation without changing the caller's profile."""
    simulated = copy.deepcopy(profile)
    migrations: dict[str, str] = {}
    for record in sorted(records, key=lambda item: item["record_id"]):
        # This must run against the progressively simulated Source set: two
        # queue rows for one canonical Source may otherwise each pass against
        # an initially unknown date and then conflict during the real apply.
        activity_reported_at(record, simulated.get("sources", []))
        for source in source_items(record, queue):
            selected_source_id = source_id_for_url(
                source, simulated.get("sources", [])
            )
            old_ids = reconcile_profile_source_identity(
                simulated, source, selected_source_id
            )
            canonical_url = canonical_source_url(source.get("url", ""))
            old_ids.update(
                item["source_id"]
                for item in dataset.get("sources", [])
                if canonical_url
                and canonical_source_url(
                    item.get("url") or item.get("path") or ""
                )
                == canonical_url
                and item.get("source_id") != selected_source_id
                and item.get("source_id", "").startswith("source--daily-")
            )
            for old_id in old_ids:
                prior = migrations.get(old_id)
                if prior and prior != selected_source_id:
                    raise ValueError(
                        f"Source {old_id} maps to both {prior} and {selected_source_id}"
                    )
                migrations[old_id] = selected_source_id
            modeled = profile_source(record, source, queue)
            modeled["source_id"] = selected_source_id
            indexes = {
                item["source_id"]: index
                for index, item in enumerate(simulated.get("sources", []))
            }
            if selected_source_id in indexes:
                existing = simulated["sources"][indexes[selected_source_id]]
                simulated["sources"][indexes[selected_source_id]] = (
                    modeled
                    if selected_source_id.startswith("source--daily-")
                    else merge_materialized_source(existing, modeled)
                )
            else:
                simulated.setdefault("sources", []).append(modeled)
    return migrations


def planned_activity_identity_migrations(
    records: list[dict[str, Any]],
) -> dict[str, str]:
    """Return reviewed daily→stable Activity migrations for one actor."""
    migrations: dict[str, str] = {}
    target_sources: dict[str, str] = {}
    for record in sorted(records, key=lambda item: item["record_id"]):
        override = record.get("activity_id_override")
        if override is None:
            continue
        actor_slug = record.get("actor", {}).get("slug", "")
        issue = activity_id_override_issue(override, actor_slug)
        if issue:
            raise ValueError(
                f"{record.get('record_id', '<unknown>')}: {issue}"
            )
        old_id = generated_activity_id_for(record)
        prior_target = migrations.get(old_id)
        if prior_target and prior_target != override:
            raise ValueError(
                f"Activity {old_id} maps to both {prior_target} and {override}"
            )
        prior_source = target_sources.get(override)
        if prior_source and prior_source != old_id:
            raise ValueError(
                f"Activity override {override} is shared by {prior_source} and {old_id}"
            )
        migrations[old_id] = override
        target_sources[override] = old_id
    return migrations


def activity_override_ownership_issues(
    grouped: dict[str, list[dict[str, Any]]], profiles_root: Path
) -> list[str]:
    """Reject cross-actor reuse of an explicitly scoped stable Activity ID."""
    requested: dict[str, str] = {}
    legacy_ids: set[str] = set()
    issues: list[str] = []
    for slug, records in sorted(grouped.items()):
        try:
            migrations = planned_activity_identity_migrations(records)
        except ValueError as exc:
            issues.append(f"{slug}: {exc}")
            continue
        for activity_id in migrations.values():
            prior = requested.get(activity_id)
            if prior and prior != slug:
                issues.append(
                    f"Activity override {activity_id} is requested by both "
                    f"{prior} and {slug}"
                )
            requested[activity_id] = slug
        legacy_ids.update(migrations)
    if not requested:
        return issues

    for profile_path in sorted(profiles_root.glob("*/actor-profile.json")):
        try:
            profile = load_json(profile_path)
        except (OSError, json.JSONDecodeError) as exc:
            issues.append(
                f"cannot audit Activity override ownership in {profile_path}: {exc}"
            )
            continue
        owner_slug = profile_path.parent.name
        for activity in profile.get("activities", []):
            activity_id = activity.get("activity_id")
            requested_slug = requested.get(activity_id)
            if requested_slug and requested_slug != owner_slug:
                issues.append(
                    f"Activity override {activity_id} for {requested_slug} is "
                    f"already owned by {owner_slug}"
                )

    def exact_legacy_refs(value: Any, path: str) -> list[str]:
        found: list[str] = []
        if isinstance(value, dict):
            for key, item in value.items():
                found.extend(exact_legacy_refs(item, f"{path}.{key}"))
        elif isinstance(value, list):
            for index, item in enumerate(value):
                found.extend(exact_legacy_refs(item, f"{path}[{index}]"))
        elif isinstance(value, str) and value in legacy_ids:
            found.append(f"{path} -> {value}")
        return found

    actor_profile_root = REPO_ROOT / "actor_profile"
    curated_input_paths = [
        actor_profile_root / "activity-stix-model-curation.json",
        actor_profile_root / "activity-observation-rules.json",
        actor_profile_root / "manual-research-leads.json",
        actor_profile_root / "standalone-activity-curation.json",
        *sorted((actor_profile_root / "osint").rglob("*.json")),
    ]
    for path in curated_input_paths:
        if not path.exists():
            continue
        try:
            value = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            issues.append(f"cannot audit Activity refs in {path}: {exc}")
            continue
        issues.extend(
            f"global Activity curation must be migrated explicitly: {item}"
            for item in exact_legacy_refs(
                value, str(path.relative_to(REPO_ROOT))
            )
        )
    return issues


def activity_override_rerun_issues(
    profile: dict[str, Any],
    records: list[dict[str, Any]],
    ledger: dict[str, Any] | None,
) -> list[str]:
    """Distinguish an idempotent override rerun from an in-actor ID collision."""
    issues: list[str] = []
    activities = {
        item.get("activity_id"): item for item in profile.get("activities", [])
    }
    ledger_records = {
        item.get("record_id"): item for item in (ledger or {}).get("records", [])
    }
    for record in records:
        override = record.get("activity_id_override")
        if not override:
            continue
        old_id = generated_activity_id_for(record)
        if old_id in activities or override not in activities:
            continue
        prior = ledger_records.get(record.get("record_id")) or {}
        marker = f"日次収集レコード {record.get('record_id', '')} から取込。"
        proven_rerun = (
            prior.get("activity_id_override") == override
            or marker in activities[override].get("analyst_notes", "")
        )
        if not proven_rerun:
            issues.append(
                f"Activity override {override} already exists in actor scope "
                "without ownership proof from this daily record"
            )
    return issues


def preflight_grouped_records(
    grouped: dict[str, list[dict[str, Any]]],
    profiles_root: Path,
    queue: dict[str, Any],
    *,
    rebuild_daily: bool = False,
) -> list[str]:
    """Validate every selected actor before the first output is written."""
    issues = activity_override_ownership_issues(grouped, profiles_root)
    for slug, records in sorted(grouped.items()):
        profile_dir = profiles_root / slug
        profile_path = profile_dir / "actor-profile.json"
        iocs_path = profile_dir / "iocs.json"
        artifacts_path = profile_dir / "artifacts.csv"
        manifest_path = profile_dir / "ioc-sources.json"
        ledger_path = profile_dir / "daily-observations.json"
        missing = [
            str(path)
            for path in (profile_path, iocs_path, artifacts_path)
            if not path.exists()
        ]
        if missing:
            issues.append(f"{slug}: required profile outputs are missing: {', '.join(missing)}")
            continue
        profile = load_json(profile_path)
        dataset = load_json(iocs_path)
        artifact_rows = load_artifact_rows(artifacts_path)
        manifest: Any = None
        if manifest_path.exists():
            try:
                manifest = load_json(manifest_path)
            except (OSError, json.JSONDecodeError) as exc:
                issues.append(f"{slug}: invalid ioc-sources.json: {exc}")
                continue
        ledger: Any = None
        if ledger_path.exists():
            try:
                ledger = load_json(ledger_path)
            except (OSError, json.JSONDecodeError) as exc:
                issues.append(f"{slug}: invalid daily-observations.json: {exc}")
                continue
        issues.extend(
            f"{slug}: {issue}"
            for issue in activity_override_rerun_issues(
                profile, records, ledger
            )
        )
        for record in sorted(records, key=lambda item: item["record_id"]):
            try:
                activity_reported_at(record, profile.get("sources", []))
            except ValueError as exc:
                issues.append(f"{slug}/{record.get('record_id', '')}: {exc}")
        try:
            source_id_map = planned_source_identity_migrations(
                profile, dataset, records, queue
            )
        except ValueError as exc:
            issues.append(f"{slug}: {exc}")
            continue
        try:
            activity_id_map = planned_activity_identity_migrations(records)
        except ValueError as exc:
            issues.append(f"{slug}: {exc}")
            continue
        source_migration_issues = [
            *profile_source_identity_migration_issues(profile, source_id_map),
            *source_identity_migration_issues(
                dataset, artifact_rows, source_id_map, profile_common
            ),
        ]
        issues.extend(
            f"{slug}: {issue}" for issue in source_migration_issues
        )
        manifest_issues = (
            source_manifest_migration_issues(manifest, source_id_map)
            if manifest is not None
            else []
        )
        issues.extend(f"{slug}: {issue}" for issue in manifest_issues)
        activity_issues = activity_identity_migration_issues(
            profile,
            dataset,
            artifact_rows,
            manifest,
            activity_id_map,
        )
        issues.extend(f"{slug}: {issue}" for issue in activity_issues)
        if rebuild_daily:
            retained_profile = copy.deepcopy(profile)
            retained_dataset = copy.deepcopy(dataset)
            retained_artifacts = copy.deepcopy(artifact_rows)
            retained_manifest = copy.deepcopy(manifest)
            if retained_manifest is not None and not manifest_issues:
                migrate_source_manifest(retained_manifest, source_id_map)
            if not source_migration_issues:
                migrate_profile_source_identities(
                    retained_profile, source_id_map
                )
                retained_artifacts = migrate_cross_file_source_identities(
                    retained_dataset,
                    retained_artifacts,
                    source_id_map,
                    retained_profile.get("sources", []),
                    profile_common,
                )
            if not activity_issues:
                retained_artifacts = migrate_activity_identities(
                    retained_profile,
                    retained_dataset,
                    retained_artifacts,
                    retained_manifest,
                    activity_id_map,
                    profile_common,
                )
            issues.extend(
                f"{slug}: rebuild dependency: {issue}"
                for issue in daily_rebuild_dependency_issues(
                    retained_profile,
                    retained_dataset,
                    retained_artifacts,
                    retained_manifest,
                )
            )
    return issues


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
    queue_issues = list(queue.get("decision_issues", []))
    queue_issues.extend(
        message
        for record in queue.get("records", [])
        for message in record.get("decision_issues", [])
    )
    for record in queue.get("records", []):
        if "reported_at" in record:
            issue = reviewed_reported_at_issue(record["reported_at"])
            if issue:
                queue_issues.append(f"{record.get('record_id', '')}: {issue}")
        if "activity_id_override" in record:
            issue = activity_id_override_issue(
                record["activity_id_override"],
                record.get("actor", {}).get("slug", ""),
            )
            if issue:
                queue_issues.append(f"{record.get('record_id', '')}: {issue}")
    if queue_issues:
        raise SystemExit(
            "review queue contains unresolved validation issues; "
            "run validate_daily.py before applying"
        )
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
    if args.rebuild_daily:
        for slug in rebuild_actor_slugs(queue, args.profiles_root.resolve()):
            if not wanted or slug in wanted:
                grouped.setdefault(slug, [])
    preflight_issues = preflight_grouped_records(
        grouped,
        args.profiles_root.resolve(),
        queue,
        rebuild_daily=args.rebuild_daily,
    )
    if preflight_issues:
        raise SystemExit(
            "review queue preflight failed before writes:\n"
            + "\n".join(preflight_issues)
        )
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
        manifest_path = profile_dir / "ioc-sources.json"
        if not all(path.exists() for path in (profile_path, iocs_path, artifacts_path)):
            summary["actors"][slug] = {"error": "required profile outputs are missing"}
            failures += 1
            continue

        profile = load_json(profile_path)
        dataset = load_json(iocs_path)
        artifact_rows = load_artifact_rows(artifacts_path)
        manifest = load_json(manifest_path) if manifest_path.exists() else None
        profile_before = semantic_copy(profile, "updated_at")
        dataset_before = semantic_copy(dataset, "generated_at")
        artifacts_before = copy.deepcopy(artifact_rows)
        manifest_before = copy.deepcopy(manifest)

        activity_id_map = planned_activity_identity_migrations(records)
        if args.rebuild_daily:
            # Rebuild removes legacy daily Sources before the record loop can
            # discover their old IDs. Preserve the preflight-equivalent map so
            # the generator manifest cannot reintroduce those identities.
            rebuild_source_id_map = planned_source_identity_migrations(
                profile, dataset, records, queue
            )
            if manifest is not None:
                migrate_source_manifest(manifest, rebuild_source_id_map)
            migrate_profile_source_identities(profile, rebuild_source_id_map)
            artifact_rows = migrate_cross_file_source_identities(
                dataset,
                artifact_rows,
                rebuild_source_id_map,
                profile.get("sources", []),
                profile_common,
            )
        artifact_rows = migrate_activity_identities(
            profile,
            dataset,
            artifact_rows,
            manifest,
            activity_id_map,
            profile_common,
        )
        if args.rebuild_daily:
            artifact_rows = remove_daily_materialization(
                profile, dataset, artifact_rows, manifest
            )

        source_id_map: dict[str, str] = {}
        for record in sorted(records, key=lambda item: item["record_id"]):
            sources = source_items(record, queue)
            source_indexes = {
                item["source_id"]: index
                for index, item in enumerate(profile.get("sources", []))
            }
            evidence_refs = []
            for source in sources:
                modeled = profile_source(record, source, queue)
                resolved_source_id = source_id_for_url(source, profile["sources"])
                old_source_ids = reconcile_profile_source_identity(
                    profile, source, resolved_source_id
                )
                canonical_url = canonical_source_url(source.get("url", ""))
                old_source_ids.update(
                    item["source_id"]
                    for item in dataset.get("sources", [])
                    if canonical_url
                    and canonical_source_url(
                        item.get("url") or item.get("path") or ""
                    )
                    == canonical_url
                    and item.get("source_id") != resolved_source_id
                    and item.get("source_id", "").startswith("source--daily-")
                )
                for old_source_id in old_source_ids:
                    prior = source_id_map.get(old_source_id)
                    if prior and prior != resolved_source_id:
                        raise ValueError(
                            f"Source {old_source_id} maps to both {prior} and "
                            f"{resolved_source_id}"
                        )
                    source_id_map[old_source_id] = resolved_source_id
                source_indexes = {
                    item["source_id"]: index
                    for index, item in enumerate(profile.get("sources", []))
                }
                modeled["source_id"] = resolved_source_id
                evidence_refs.append(resolved_source_id)
                if resolved_source_id in source_indexes:
                    existing_source = profile["sources"][source_indexes[resolved_source_id]]
                    if resolved_source_id.startswith("source--daily-"):
                        profile["sources"][source_indexes[resolved_source_id]] = modeled
                    else:
                        # A curated Source with the same canonical URL owns identity and
                        # richer metadata. A reviewed publication date may still fill
                        # an unknown curated date.
                        profile["sources"][source_indexes[resolved_source_id]] = (
                            merge_materialized_source(existing_source, modeled)
                        )
                else:
                    profile["sources"].append(modeled)
                    source_indexes[resolved_source_id] = len(profile["sources"]) - 1
            artifact_rows = migrate_cross_file_source_identities(
                dataset,
                artifact_rows,
                source_id_map,
                profile["sources"],
                profile_common,
            )
            if manifest is not None:
                migrate_source_manifest(manifest, source_id_map)
            source_id_map.clear()
            evidence_refs = sorted(set(evidence_refs))
            ensure_malware_capabilities(profile, record, evidence_refs)
            activity = activity_entry(record, evidence_refs, profile)
            activities = {
                item["activity_id"]: index
                for index, item in enumerate(profile["activities"])
            }
            if activity["activity_id"] in activities:
                index = activities[activity["activity_id"]]
                profile["activities"][index] = (
                    merge_materialized_activity(
                        profile["activities"][index], activity
                    )
                    if record.get("activity_id_override")
                    else activity
                )
            else:
                profile["activities"].append(activity)
            merge_ioc_record(
                dataset,
                record,
                queue,
                profile_common,
                preferred_sources=profile["sources"],
            )
            artifact_source_id = source_id_for_url(
                primary_source(record, queue), profile["sources"]
            )
            artifact_source_published_at = next(
                (
                    item.get("published_at")
                    for item in profile["sources"]
                    if item.get("source_id") == artifact_source_id
                ),
                None,
            )
            artifact_rows = merge_artifacts(
                artifact_rows,
                record,
                queue,
                profile["profile_id"],
                profile_common,
                source_id=artifact_source_id,
                source_published_at=artifact_source_published_at,
            )

        profile["sources"].sort(key=lambda item: item["source_id"])
        profile["activities"].sort(
            key=lambda item: (
                item.get("first_observed", {}).get("value") or "",
                item["activity_id"],
            )
        )
        profile["capabilities"]["malware"].sort(key=lambda item: item["id"])
        materialize_profile_diamonds(profile)
        finalize_dataset(dataset)

        profile_changed = semantic_copy(profile, "updated_at") != profile_before
        dataset_changed = semantic_copy(dataset, "generated_at") != dataset_before
        artifacts_changed = artifact_rows != artifacts_before
        manifest_changed = manifest != manifest_before
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
            "manifest": (
                write_json_if_changed(manifest_path, manifest)
                if manifest_changed and manifest is not None
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
