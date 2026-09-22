#!/usr/bin/env python3
"""Validate and reproducibly package the OpenCTI STIX distribution."""

from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import shutil
import tarfile
import tempfile
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


SECTIONS = ("actors", "campaigns", "activities")
COUNT_FIELDS = {
    "actors": "actor_bundle_count",
    "campaigns": "campaign_bundle_count",
    "activities": "activity_bundle_count",
}
COMMON_FILES = ("README.md", "manifest.json")
MAX_BUNDLE_BYTES = 45 * 1024 * 1024
MANIFEST_SCHEMA_VERSION = "1.1.0"
MANIFEST_FORMAT = "STIX 2.1 bundles for OpenCTI ImportFileStix"
OBJECT_MARKING = "TLP:CLEAR"


def profile_stix_id(kind: str, key: str) -> str:
    """Return the deterministic STIX ID used by the profile renderer."""

    raw = bytearray(
        hashlib.sha256(f"actor-profile:{kind}:{key}".encode("utf-8")).digest()[:16]
    )
    raw[6] = (raw[6] & 0x0F) | 0x40
    raw[8] = (raw[8] & 0x3F) | 0x80
    value = raw.hex()
    uuid = (
        f"{value[:8]}-{value[8:12]}-{value[12:16]}-"
        f"{value[16:20]}-{value[20:]}"
    )
    return f"{kind}--{uuid}"


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest_count(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"manifest {field} must be a non-negative integer")
    return value


def manifest_relative_path(value: Any) -> Path:
    """Map one repository-relative manifest path below the opencti root."""

    raw = PurePosixPath(str(value or ""))
    if raw.is_absolute() or not raw.parts or raw.parts[0] != "opencti":
        raise ValueError(f"invalid OpenCTI manifest path: {value!r}")
    relative = PurePosixPath(*raw.parts[1:])
    if not relative.parts or ".." in relative.parts:
        raise ValueError(f"unsafe OpenCTI manifest path: {value!r}")
    return Path(*relative.parts)


def _section_entries(
    manifest: dict[str, Any], section: str
) -> list[dict[str, Any]]:
    entries = manifest.get(section)
    if not isinstance(entries, list) or not all(
        isinstance(item, dict) for item in entries
    ):
        raise ValueError(f"manifest.{section} must be an array of objects")
    count_field = COUNT_FIELDS[section]
    expected_count = manifest_count(manifest.get(count_field), count_field)
    if expected_count != len(entries):
        raise ValueError(
            f"manifest {section} count mismatch: "
            f"declared={expected_count!r} actual={len(entries)}"
        )
    return entries


def validate_distribution(
    opencti_root: Path,
    *,
    max_bundle_bytes: int = MAX_BUNDLE_BYTES,
) -> tuple[dict[str, Any], dict[str, list[Path]]]:
    """Validate manifest coverage and every Bundle's recorded size/count."""

    if opencti_root.is_symlink():
        raise ValueError("opencti root must not be a symlink")
    opencti_root = opencti_root.resolve()
    manifest_path = opencti_root / "manifest.json"
    readme_path = opencti_root / "README.md"
    if not manifest_path.is_file() or not readme_path.is_file():
        raise ValueError("opencti/README.md and opencti/manifest.json are required")

    for path in opencti_root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"symlinks are not allowed in the release tree: {path}")

    manifest = load_json(manifest_path)
    expected_metadata = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "format": MANIFEST_FORMAT,
        "object_marking": OBJECT_MARKING,
        "import_order": list(SECTIONS),
    }
    for field, expected in expected_metadata.items():
        if manifest.get(field) != expected:
            raise ValueError(
                f"manifest {field} mismatch: "
                f"declared={manifest.get(field)!r} expected={expected!r}"
            )

    files_by_section: dict[str, list[Path]] = {}
    expected_bundle_paths: set[Path] = set()
    actual_max_size = 0
    actor_by_profile_id: dict[str, dict[str, Any]] = {}
    actor_by_slug: dict[str, dict[str, Any]] = {}
    entries_by_section: dict[str, list[dict[str, Any]]] = {}

    for section in SECTIONS:
        section_files: list[Path] = []
        entries = _section_entries(manifest, section)
        entries_by_section[section] = entries
        for entry in entries:
            relative = manifest_relative_path(entry.get("path"))
            if relative.suffixes[-2:] != [".stix2", ".json"]:
                raise ValueError(f"manifest path is not STIX JSON: opencti/{relative}")
            if not relative.parts or relative.parts[0] != section:
                raise ValueError(
                    f"manifest path is outside its {section} section: "
                    f"opencti/{relative}"
                )
            if relative in expected_bundle_paths:
                raise ValueError(f"duplicate manifest bundle path: opencti/{relative}")
            expected_bundle_paths.add(relative)
            section_files.append(relative)

            path = opencti_root / relative
            if not path.is_file():
                raise ValueError(f"manifest bundle is missing: {path}")
            actual_size = path.stat().st_size
            if actual_size > max_bundle_bytes:
                raise ValueError(
                    f"bundle exceeds the {max_bundle_bytes}-byte release limit: {path}"
                )
            declared_size = manifest_count(
                entry.get("size_bytes"), f"{section}[].size_bytes"
            )
            if declared_size != actual_size:
                raise ValueError(
                    f"bundle size mismatch for {path}: "
                    f"declared={declared_size!r} actual={actual_size}"
                )
            bundle = load_json(path)
            objects = bundle.get("objects")
            if bundle.get("type") != "bundle" or not isinstance(objects, list):
                raise ValueError(f"not a STIX Bundle with an objects array: {path}")
            if not all(isinstance(item, dict) for item in objects):
                raise ValueError(f"STIX Bundle objects must all be objects: {path}")
            declared_object_count = manifest_count(
                entry.get("object_count"), f"{section}[].object_count"
            )
            if declared_object_count != len(objects):
                raise ValueError(
                    f"object count mismatch for {path}: "
                    f"declared={declared_object_count!r} actual={len(objects)}"
                )
            if section == "actors":
                profile_id = entry.get("profile_id")
                slug = entry.get("slug")
                if not isinstance(profile_id, str) or not profile_id.startswith(
                    "actor--"
                ):
                    raise ValueError(f"invalid actor profile_id: {path}")
                if not isinstance(slug, str) or not slug or slug == "unattributed":
                    raise ValueError(f"invalid actor slug: {path}")
                if profile_id in actor_by_profile_id or slug in actor_by_slug:
                    raise ValueError(f"duplicate actor identity in manifest: {path}")
                expected_path = Path("actors") / f"{slug}.stix2.json"
                if relative != expected_path:
                    raise ValueError(
                        f"actor path/slug mismatch: opencti/{relative}"
                    )
                expected_actor_id = profile_stix_id("intrusion-set", profile_id)
                primary = [
                    item
                    for item in objects
                    if item.get("type") == "intrusion-set"
                    and item.get("id") == expected_actor_id
                ]
                if len(primary) != 1:
                    raise ValueError(
                        "actor bundle lacks exactly one canonical "
                        f"intrusion-set: {path}"
                    )
                actor_by_profile_id[profile_id] = entry
                actor_by_slug[slug] = entry
            elif section in {"campaigns", "activities"}:
                activity_id = entry.get("activity_id")
                if not isinstance(activity_id, str) or not activity_id:
                    raise ValueError(f"invalid activity_id: {path}")
                if "standalone_activity" in entry and entry.get(
                    "standalone_activity"
                ) is not True:
                    raise ValueError(f"invalid standalone activity flag: {path}")
                is_standalone = entry.get("standalone_activity") is True
                profile_id = entry.get("profile_id")
                slug = entry.get("slug")
                if is_standalone:
                    if slug != "unattributed" or profile_id is not None:
                        raise ValueError(
                            f"invalid standalone activity boundary: {path}"
                        )
                else:
                    actor_entry = actor_by_profile_id.get(profile_id)
                    if actor_entry is None or actor_entry.get("slug") != slug:
                        raise ValueError(
                            f"activity actor identity does not match manifest: {path}"
                        )

                if section == "campaigns":
                    primary_type = "campaign"
                    if entry.get("stix_object_type") != primary_type:
                        raise ValueError(f"campaign manifest/type mismatch: {path}")
                else:
                    primary_type = entry.get("stix_object_type")
                    if primary_type not in {"incident", "grouping"}:
                        raise ValueError(f"activity manifest/type mismatch: {path}")
                primary = [
                    item
                    for item in objects
                    if item.get("type") == primary_type
                    and item.get("x_profile_object_id") == activity_id
                ]
                if len(primary) != 1:
                    raise ValueError(
                        "activity bundle lacks exactly one matching primary "
                        f"object: {path}"
                    )
            actual_max_size = max(actual_max_size, actual_size)
        files_by_section[section] = sorted(
            section_files, key=lambda item: item.as_posix()
        )

    actual_bundle_paths = {
        path.relative_to(opencti_root)
        for path in opencti_root.rglob("*.stix2.json")
        if path.is_file()
    }
    missing = expected_bundle_paths - actual_bundle_paths
    extra = actual_bundle_paths - expected_bundle_paths
    if missing or extra:
        raise ValueError(
            "manifest/file coverage mismatch: "
            f"missing={sorted(item.as_posix() for item in missing)} "
            f"extra={sorted(item.as_posix() for item in extra)}"
        )

    allowed_files = expected_bundle_paths | {Path(item) for item in COMMON_FILES}
    actual_files = {
        path.relative_to(opencti_root)
        for path in opencti_root.rglob("*")
        if path.is_file()
    }
    unexpected_files = actual_files - allowed_files
    if unexpected_files:
        raise ValueError(
            "unexpected files in OpenCTI release tree: "
            f"{sorted(item.as_posix() for item in unexpected_files)}"
        )

    campaign_counts = Counter(
        item["profile_id"]
        for item in entries_by_section["campaigns"]
        if item.get("standalone_activity") is not True
    )
    activity_counts = Counter(
        item["profile_id"]
        for section in ("campaigns", "activities")
        for item in entries_by_section[section]
        if item.get("standalone_activity") is not True
    )
    for actor in entries_by_section["actors"]:
        profile_id = actor["profile_id"]
        declared_campaign_count = manifest_count(
            actor.get("campaign_bundle_count"),
            "actors[].campaign_bundle_count",
        )
        if declared_campaign_count != campaign_counts[profile_id]:
            raise ValueError(
                f"actor campaign bundle count mismatch: {profile_id}"
            )
        declared_activity_count = manifest_count(
            actor.get("activity_bundle_count"),
            "actors[].activity_bundle_count",
        )
        if declared_activity_count != activity_counts[profile_id]:
            raise ValueError(
                f"actor activity bundle count mismatch: {profile_id}"
            )

    standalone = manifest.get("standalone_activities")
    if not isinstance(standalone, list):
        raise ValueError("manifest.standalone_activities must be an array")
    standalone_count = manifest_count(
        manifest.get("standalone_activity_bundle_count"),
        "standalone_activity_bundle_count",
    )
    if standalone_count != len(standalone):
        raise ValueError("manifest standalone activity count mismatch")
    activity_paths = set(files_by_section["campaigns"]) | set(
        files_by_section["activities"]
    )
    standalone_by_path: dict[Path, dict[str, Any]] = {}
    for item in standalone:
        if not isinstance(item, dict):
            raise ValueError("manifest standalone activity entry must be an object")
        path = manifest_relative_path(item.get("path"))
        if path in standalone_by_path:
            raise ValueError(f"duplicate standalone activity path: opencti/{path}")
        standalone_by_path[path] = item
    if not set(standalone_by_path) <= activity_paths:
        raise ValueError(
            "standalone activity paths must be unique members of campaigns/activities"
        )
    activity_entry_by_path = {
        manifest_relative_path(item["path"]): item
        for section in ("campaigns", "activities")
        for item in manifest[section]
    }
    flagged_standalone_by_path = {
        path: item
        for path, item in activity_entry_by_path.items()
        if item.get("standalone_activity") is True
    }
    if set(standalone_by_path) != set(flagged_standalone_by_path):
        raise ValueError(
            "manifest standalone activity list does not exactly match flagged entries"
        )
    for path, item in standalone_by_path.items():
        if item != flagged_standalone_by_path[path]:
            raise ValueError(
                f"standalone entry differs from its activity entry: opencti/{path}"
            )
        if (
            item.get("standalone_activity") is not True
            or item.get("slug") != "unattributed"
            or item.get("profile_id") is not None
        ):
            raise ValueError(f"invalid standalone activity boundary: opencti/{path}")

    actual_activity_type_counts: dict[str, int] = {}
    for item in manifest["activities"]:
        key = str(item.get("stix_object_type", ""))
        actual_activity_type_counts[key] = actual_activity_type_counts.get(key, 0) + 1
    declared_activity_type_counts = manifest.get("activity_type_counts")
    if not isinstance(declared_activity_type_counts, dict):
        raise ValueError("manifest activity_type_counts must contain counts")
    for key, value in declared_activity_type_counts.items():
        manifest_count(value, f"activity_type_counts.{key}")
    if declared_activity_type_counts != dict(
        sorted(actual_activity_type_counts.items())
    ):
        raise ValueError("manifest activity_type_counts mismatch")

    declared_max_size = manifest_count(
        manifest.get("max_bundle_size_bytes"), "max_bundle_size_bytes"
    )
    if declared_max_size != actual_max_size:
        raise ValueError(
            "manifest maximum bundle size mismatch: "
            f"declared={declared_max_size!r} "
            f"actual={actual_max_size}"
        )
    return manifest, files_by_section


def source_date_epoch(manifest: dict[str, Any]) -> int:
    value = manifest.get("generated_at")
    if not isinstance(value, str) or not value:
        raise ValueError("manifest.generated_at must be an ISO-8601 timestamp")
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("manifest.generated_at must be an ISO-8601 timestamp") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return int(parsed.timestamp())


def archive_members(files: Iterable[Path]) -> list[Path]:
    members = {Path(name) for name in COMMON_FILES}
    members.update(Path(item) for item in files)
    return sorted(members, key=lambda item: item.as_posix())


def write_reproducible_tar_gz(
    output: Path,
    opencti_root: Path,
    members: Iterable[Path],
    epoch: int,
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_tar = tempfile.NamedTemporaryFile(
        prefix=f".{output.name}.", suffix=".tar", dir=output.parent, delete=False
    )
    temporary_tar_path = Path(temporary_tar.name)
    temporary_tar.close()
    temporary_gzip = tempfile.NamedTemporaryFile(
        prefix=f".{output.name}.", suffix=".tmp", dir=output.parent, delete=False
    )
    temporary_gzip_path = Path(temporary_gzip.name)
    temporary_gzip.close()
    try:
        with tarfile.open(
            temporary_tar_path, "w", format=tarfile.PAX_FORMAT
        ) as archive:
            for relative in members:
                source = opencti_root / relative
                info = tarfile.TarInfo(f"opencti/{relative.as_posix()}")
                info.size = source.stat().st_size
                info.mtime = epoch
                info.mode = 0o644
                info.uid = 0
                info.gid = 0
                info.uname = ""
                info.gname = ""
                info.pax_headers = {}
                with source.open("rb") as handle:
                    archive.addfile(info, handle)
        with temporary_tar_path.open("rb") as source, temporary_gzip_path.open(
            "wb"
        ) as raw_output:
            with gzip.GzipFile(
                filename="",
                mode="wb",
                compresslevel=9,
                fileobj=raw_output,
                mtime=epoch,
            ) as compressed:
                shutil.copyfileobj(source, compressed, length=1024 * 1024)
        temporary_gzip_path.replace(output)
        output.chmod(0o644)
    finally:
        temporary_tar_path.unlink(missing_ok=True)
        temporary_gzip_path.unlink(missing_ok=True)


def write_reproducible_zip(
    output: Path,
    opencti_root: Path,
    members: Iterable[Path],
    epoch: int,
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.fromtimestamp(epoch, tz=dt.timezone.utc)
    zip_timestamp = max(timestamp, dt.datetime(1980, 1, 1, tzinfo=dt.timezone.utc))
    date_time = (
        zip_timestamp.year,
        zip_timestamp.month,
        zip_timestamp.day,
        zip_timestamp.hour,
        zip_timestamp.minute,
        zip_timestamp.second,
    )
    temporary = tempfile.NamedTemporaryFile(
        prefix=f".{output.name}.", suffix=".tmp", dir=output.parent, delete=False
    )
    temporary_path = Path(temporary.name)
    temporary.close()
    try:
        with zipfile.ZipFile(
            temporary_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for relative in members:
                source = opencti_root / relative
                info = zipfile.ZipInfo(
                    filename=f"opencti/{relative.as_posix()}", date_time=date_time
                )
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = (0o100644 & 0xFFFF) << 16
                archive.writestr(info, source.read_bytes(), compresslevel=9)
        temporary_path.replace(output)
        output.chmod(0o644)
    finally:
        temporary_path.unlink(missing_ok=True)


def atomic_copy(source: Path, output: Path) -> None:
    temporary = tempfile.NamedTemporaryFile(
        prefix=f".{output.name}.", suffix=".tmp", dir=output.parent, delete=False
    )
    temporary_path = Path(temporary.name)
    temporary.close()
    try:
        shutil.copyfile(source, temporary_path)
        temporary_path.replace(output)
        output.chmod(0o644)
    finally:
        temporary_path.unlink(missing_ok=True)


def atomic_write_text(output: Path, value: str) -> None:
    temporary = tempfile.NamedTemporaryFile(
        prefix=f".{output.name}.", suffix=".tmp", dir=output.parent, delete=False
    )
    temporary_path = Path(temporary.name)
    temporary.close()
    try:
        temporary_path.write_text(value, encoding="utf-8")
        temporary_path.replace(output)
        output.chmod(0o644)
    finally:
        temporary_path.unlink(missing_ok=True)


def package_distribution(opencti_root: Path, output_dir: Path) -> dict[str, Any]:
    if opencti_root.is_symlink():
        raise ValueError("opencti root must not be a symlink")
    if output_dir.is_symlink():
        raise ValueError("release output directory must not be a symlink")
    opencti_root = opencti_root.resolve()
    output_dir = output_dir.resolve()
    try:
        output_dir.relative_to(opencti_root)
    except ValueError:
        pass
    else:
        raise ValueError("release output directory must be outside opencti root")
    manifest, files_by_section = validate_distribution(opencti_root)
    source_date_epoch(manifest)
    epoch = 0

    all_files = [
        item for section in SECTIONS for item in files_by_section[section]
    ]
    layouts = {
        "opencti-stix-all.tar.gz": archive_members(all_files),
        "opencti-stix-actors.tar.gz": archive_members(files_by_section["actors"]),
        "opencti-stix-campaigns.tar.gz": archive_members(
            files_by_section["campaigns"]
        ),
        "opencti-stix-activities.tar.gz": archive_members(
            files_by_section["activities"]
        ),
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    allowed_output_names = {
        *layouts,
        "opencti-stix-all.zip",
        "opencti-manifest.json",
        "SHA256SUMS",
    }
    unexpected_outputs = [
        item for item in output_dir.iterdir() if item.name not in allowed_output_names
    ]
    if unexpected_outputs:
        raise ValueError(
            "release output contains unexpected entries: "
            f"{sorted(item.name for item in unexpected_outputs)}"
        )
    for existing in output_dir.iterdir():
        if not existing.is_file():
            raise ValueError(f"release output entry is not a file: {existing}")

    assets: list[Path] = []
    for name, members in layouts.items():
        output = output_dir / name
        write_reproducible_tar_gz(output, opencti_root, members, epoch)
        assets.append(output)

    zip_output = output_dir / "opencti-stix-all.zip"
    write_reproducible_zip(
        zip_output, opencti_root, archive_members(all_files), epoch
    )
    assets.append(zip_output)

    manifest_output = output_dir / "opencti-manifest.json"
    atomic_copy(opencti_root / "manifest.json", manifest_output)
    assets.append(manifest_output)

    checksums = {path.name: sha256_file(path) for path in sorted(assets)}
    checksum_path = output_dir / "SHA256SUMS"
    atomic_write_text(
        checksum_path,
        "".join(f"{digest}  {name}\n" for name, digest in checksums.items()),
    )
    reported_checksums = {**checksums, checksum_path.name: sha256_file(checksum_path)}

    return {
        "bundle_counts": {
            section: len(files_by_section[section]) for section in SECTIONS
        },
        "standalone_activity_bundles": manifest[
            "standalone_activity_bundle_count"
        ],
        "assets": [
            {
                "name": path.name,
                "size_bytes": path.stat().st_size,
                "sha256": reported_checksums[path.name],
            }
            for path in [*sorted(assets), checksum_path]
        ],
        "output_dir": str(output_dir),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--opencti-root", type=Path, default=Path("opencti")
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("dist/opencti-release")
    )
    args = parser.parse_args()
    result = package_distribution(args.opencti_root, args.output_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
