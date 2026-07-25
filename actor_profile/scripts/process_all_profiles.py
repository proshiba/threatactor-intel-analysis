#!/usr/bin/env python3
"""Ingest, render, and validate every profile in corpus-catalog.json."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from common import load_json, utc_now, write_json_atomic


SCRIPT_DIR = Path(__file__).resolve().parent
FRAMEWORK_DIR = SCRIPT_DIR.parent


def run(command: list[str], root: Path) -> dict[str, Any]:
    started = time.monotonic()
    result = subprocess.run(
        command,
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "exit_code": result.returncode,
        "duration_seconds": round(time.monotonic() - started, 3),
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def parse_json_output(output: str) -> dict[str, Any]:
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {}


def process_actor(
    actor: dict[str, Any],
    root: Path,
    profiles_root: Path,
    *,
    skip_ingest: bool,
) -> dict[str, Any]:
    slug = actor["slug"]
    actor_dir = profiles_root / slug
    profile = actor_dir / "actor-profile.json"
    manifest = actor_dir / "ioc-sources.json"
    iocs = actor_dir / "iocs.json"
    artifacts = actor_dir / "artifacts.csv"
    markdown = actor_dir / "generated" / "profile-ja.md"
    stix = actor_dir / "generated" / "profile.stix2.json"
    result: dict[str, Any] = {
        "slug": slug,
        "name": actor["name"],
        "profile": str(profile.relative_to(root)),
        "steps": {},
    }
    if not profile.exists() or not manifest.exists():
        result["status"] = "missing-input"
        return result

    if not skip_ingest:
        ingest = run(
            [
                sys.executable,
                "-B",
                str(SCRIPT_DIR / "ingest_observables.py"),
                str(manifest),
                "--iocs-output",
                str(iocs),
                "--artifacts-output",
                str(artifacts),
            ],
            root,
        )
        result["steps"]["ingest"] = {
            **ingest,
            "summary": parse_json_output(ingest["stdout"]),
        }
    elif iocs.exists() and artifacts.exists():
        dataset = load_json(iocs)
        with artifacts.open("r", encoding="utf-8-sig", newline="") as stream:
            artifact_count = max(sum(1 for _ in stream) - 1, 0)
        ingestion = dataset.get("ingestion", {})
        result["steps"]["ingest"] = {
            "exit_code": 1 if ingestion.get("error_source_count", 0) else 0,
            "duration_seconds": 0,
            "stdout": "",
            "stderr": "",
            "summary": {
                "sources": ingestion.get("source_count", len(dataset.get("sources", []))),
                "processed": ingestion.get("processed_source_count", 0),
                "errors": ingestion.get("error_source_count", 0),
                "indicators": len(dataset.get("indicators", [])),
                "indicator_observations": sum(
                    item.get("observation_count", 0)
                    for item in dataset.get("indicators", [])
                ),
                "artifacts": artifact_count,
            },
        }

    if not iocs.exists() or not artifacts.exists():
        result["status"] = "ingestion-output-missing"
        return result

    render = run(
        [
            sys.executable,
            "-B",
            str(SCRIPT_DIR / "render_profile.py"),
            str(profile),
            "--iocs",
            str(iocs),
            "--artifacts",
            str(artifacts),
        ],
        root,
    )
    result["steps"]["render"] = {
        **render,
        "summary": parse_json_output(render["stdout"]),
    }
    validate = run(
        [
            sys.executable,
            "-B",
            str(SCRIPT_DIR / "validate_profile.py"),
            str(profile),
            "--iocs",
            str(iocs),
            "--artifacts",
            str(artifacts),
            "--stix",
            str(stix),
            "--json-output",
            "--max-findings",
            "20",
        ],
        root,
    )
    validation = parse_json_output(validate["stdout"])
    result["steps"]["validate"] = {
        **validate,
        "summary": {
            "valid": validation.get("valid", False),
            "counts": validation.get("counts", {}),
            "issues": validation.get("issues", []),
            "omitted_issue_count": validation.get("omitted_issue_count", 0),
        },
    }
    step_codes = [
        item["exit_code"]
        for item in result["steps"].values()
        if isinstance(item, dict) and "exit_code" in item
    ]
    validation_errors = validation.get("counts", {}).get("error", 1)
    result["status"] = (
        "complete"
        if render["exit_code"] == 0 and validation_errors == 0
        else "error"
    )
    result["has_ingestion_warnings"] = bool(
        result["steps"].get("ingest", {}).get("exit_code", 0)
    )
    result["outputs"] = {
        "iocs": str(iocs.relative_to(root)),
        "artifacts": str(artifacts.relative_to(root)),
        "markdown": str(markdown.relative_to(root)),
        "stix": str(stix.relative_to(root)),
    }
    return result


def write_csv_summary(path: Path, results: list[dict[str, Any]]) -> None:
    columns = [
        "slug", "name", "status", "source_count", "processed_source_count",
        "ingestion_error_count", "ioc_count", "ioc_observation_count",
        "artifact_count", "validation_errors", "validation_warnings",
        "ingest_seconds", "render_seconds", "validate_seconds",
    ]
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        for result in results:
            ingest = result.get("steps", {}).get("ingest", {})
            ingestion = ingest.get("summary", {})
            validation = (
                result.get("steps", {}).get("validate", {}).get("summary", {})
            )
            counts = validation.get("counts", {})
            writer.writerow(
                {
                    "slug": result["slug"],
                    "name": result["name"],
                    "status": result.get("status", ""),
                    "source_count": ingestion.get("sources", ""),
                    "processed_source_count": ingestion.get("processed", ""),
                    "ingestion_error_count": ingestion.get("errors", ""),
                    "ioc_count": ingestion.get("indicators", ""),
                    "ioc_observation_count": ingestion.get("indicator_observations", ""),
                    "artifact_count": ingestion.get("artifacts", ""),
                    "validation_errors": counts.get("error", ""),
                    "validation_warnings": counts.get("warning", ""),
                    "ingest_seconds": ingest.get("duration_seconds", ""),
                    "render_seconds": result.get("steps", {}).get("render", {}).get("duration_seconds", ""),
                    "validate_seconds": result.get("steps", {}).get("validate", {}).get("duration_seconds", ""),
                }
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog",
        type=Path,
        default=FRAMEWORK_DIR / "corpus-catalog.json",
    )
    parser.add_argument("--repository-root", type=Path, default=Path.cwd())
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument("--actor", action="append", help="only process this slug; repeatable")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--skip-ingest", action="store_true")
    parser.add_argument(
        "--missing-iocs-only",
        action="store_true",
        help="process only actors whose iocs.json or artifacts.csv is missing",
    )
    args = parser.parse_args()

    root = args.repository_root.resolve()
    profiles_root = args.profiles_root.resolve()
    catalog = load_json(args.catalog.resolve())
    wanted = set(args.actor or [])
    actors = [
        actor
        for actor in catalog["actors"]
        if not wanted or actor["slug"] in wanted
    ]
    if args.missing_iocs_only:
        actors = [
            actor
            for actor in actors
            if not (profiles_root / actor["slug"] / "iocs.json").exists()
            or not (profiles_root / actor["slug"] / "artifacts.csv").exists()
        ]
    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(
                process_actor,
                actor,
                root,
                profiles_root,
                skip_ingest=args.skip_ingest,
            ): actor
            for actor in actors
        }
        for future in as_completed(futures):
            actor = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {
                    "slug": actor["slug"],
                    "name": actor["name"],
                    "status": "exception",
                    "error": f"{type(exc).__name__}: {exc}",
                    "steps": {},
                }
            results.append(result)
            validation = (
                result.get("steps", {}).get("validate", {}).get("summary", {})
            )
            print(
                json.dumps(
                    {
                        "actor": result["slug"],
                        "status": result.get("status"),
                        "validation": validation.get("counts", {}),
                    },
                    ensure_ascii=False,
                ),
                flush=True,
            )
    results.sort(key=lambda item: item["slug"])
    summary = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "actor_count": len(results),
        "complete_count": sum(item.get("status") == "complete" for item in results),
        "error_count": sum(item.get("status") != "complete" for item in results),
        "ingestion_warning_actor_count": sum(
            item.get("has_ingestion_warnings", False) for item in results
        ),
        "results": results,
    }
    json_path = profiles_root / "processing-summary.json"
    csv_path = profiles_root / "processing-summary.csv"
    write_json_atomic(json_path, summary)
    write_csv_summary(csv_path, results)
    print(
        json.dumps(
            {
                "summary": str(json_path.relative_to(root)),
                "csv": str(csv_path.relative_to(root)),
                "actors": summary["actor_count"],
                "complete": summary["complete_count"],
                "errors": summary["error_count"],
                "ingestion_warning_actors": summary["ingestion_warning_actor_count"],
            },
            ensure_ascii=False,
        )
    )
    return 1 if summary["error_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
