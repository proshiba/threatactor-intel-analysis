#!/usr/bin/env python3
"""Create a new actor profile directory from canonical templates."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import slugify, utc_now


SCRIPT_DIR = Path(__file__).resolve().parent
FRAMEWORK_DIR = SCRIPT_DIR.parent


def materialize(template: Path, replacements: dict[str, str]) -> str:
    content = template.read_text(encoding="utf-8")
    for key, value in replacements.items():
        content = content.replace(key, value)
    return content


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("actor_name")
    parser.add_argument("--slug")
    parser.add_argument("--output-root", default="profiles")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite framework-owned template files if they already exist.",
    )
    args = parser.parse_args()

    actor_slug = args.slug or slugify(args.actor_name)
    output_dir = Path(args.output_root).resolve() / actor_slug
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "generated").mkdir(exist_ok=True)

    replacements = {
        "__ACTOR_NAME__": args.actor_name,
        "__ACTOR_SLUG__": actor_slug,
        "__NOW__": utc_now(),
    }
    files = [
        (
            FRAMEWORK_DIR / "templates" / "actor-profile.template.json",
            output_dir / "actor-profile.json",
        ),
        (
            FRAMEWORK_DIR / "templates" / "ioc-sources.template.json",
            output_dir / "ioc-sources.json",
        ),
    ]
    created = []
    skipped = []
    for template, destination in files:
        if destination.exists() and not args.force:
            skipped.append(str(destination))
            continue
        destination.write_text(
            materialize(template, replacements), encoding="utf-8"
        )
        created.append(str(destination))

    print(f"actor_dir={output_dir}")
    for path in created:
        print(f"created={path}")
    for path in skipped:
        print(f"skipped_existing={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
