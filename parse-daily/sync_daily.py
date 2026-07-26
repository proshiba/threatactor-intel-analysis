#!/usr/bin/env python3
"""Clone or fast-forward the configured tech-memo daily-news sparse checkout."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from daily_common import load_json, utc_now, write_json_atomic


HERE = Path(__file__).resolve().parent


def run(command: list[str], *, cwd: Path | None = None) -> str:
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)
    if result.returncode:
        raise RuntimeError(f"{' '.join(command)}\n{result.stderr.strip()}")
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=HERE / "config.json")
    parser.add_argument("--cache", type=Path, default=HERE / ".cache" / "tech-memo")
    parser.add_argument("--manifest", type=Path, default=HERE / "output" / "sync-manifest.json")
    args = parser.parse_args()

    config = load_json(args.config)
    source = config["source"]
    cache = args.cache.resolve()
    if not (cache / ".git").exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        run([
            "git", "clone", "--depth", "1", "--filter=blob:none", "--sparse",
            "--branch", source["branch"], source["repository"], str(cache),
        ])
    else:
        if run(["git", "status", "--porcelain"], cwd=cache):
            raise RuntimeError(f"Cache has local changes; refusing to update: {cache}")
        configured_remote = run(["git", "remote", "get-url", "origin"], cwd=cache)
        if configured_remote.rstrip("/") != source["repository"].rstrip("/"):
            raise RuntimeError(f"Unexpected origin in cache: {configured_remote}")

    run(
        ["git", "sparse-checkout", "set", source["news_path"], source["iocs_path"]],
        cwd=cache,
    )
    run(["git", "pull", "--ff-only", "origin", source["branch"]], cwd=cache)
    manifest = {
        "schema_version": "1.0.0",
        "synced_at": utc_now(),
        "repository": source["repository"],
        "branch": source["branch"],
        "commit": run(["git", "rev-parse", "HEAD"], cwd=cache),
        "cache": str(cache),
        "news_files": len(list((cache / source["news_path"]).rglob("*.md"))),
        "ioc_csv_files": len(list((cache / source["iocs_path"]).rglob("*.csv"))),
    }
    write_json_atomic(args.manifest, manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
