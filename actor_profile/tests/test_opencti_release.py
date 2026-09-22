#!/usr/bin/env python3
"""Tests for reproducible OpenCTI release packaging."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import tarfile
import tempfile
import unittest
import zipfile
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from package_opencti_release import (  # noqa: E402
    package_distribution,
    profile_stix_id,
    validate_distribution,
)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


class OpenCtiReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.workspace = Path(temporary.name)
        self.opencti = self.workspace / "opencti"
        self.opencti.mkdir()
        (self.opencti / "README.md").write_text(
            "# OpenCTI fixture\n", encoding="utf-8"
        )
        self.manifest = self._build_fixture()

    def _bundle_entry(
        self,
        relative: str,
        object_type: str,
        *,
        standalone: bool = False,
    ) -> dict[str, object]:
        path = self.opencti / relative
        bundle = {
            "type": "bundle",
            "id": f"bundle--{relative.replace('/', '-')}",
            "objects": [
                {
                    "type": object_type,
                    "spec_version": "2.1",
                    "id": f"{object_type}--11111111-1111-4111-8111-111111111111",
                    "created": "2026-01-01T00:00:00Z",
                    "modified": "2026-01-01T00:00:00Z",
                    "name": relative,
                    "x_profile_object_id": f"activity--{path.stem}",
                }
            ],
        }
        write_json(path, bundle)
        entry: dict[str, object] = {
            "slug": "unattributed" if standalone else "example",
            "profile_id": None if standalone else "actor--example",
            "activity_id": f"activity--{path.stem}",
            "name": relative,
            "stix_object_type": object_type,
            "path": f"opencti/{relative}",
            "object_count": 1,
            "size_bytes": path.stat().st_size,
        }
        if standalone:
            entry["standalone_activity"] = True
        return entry

    def _build_fixture(self) -> dict[str, object]:
        actor_path = self.opencti / "actors/example.stix2.json"
        write_json(
            actor_path,
            {
                "type": "bundle",
                "id": "bundle--actor",
                "objects": [
                    {
                        "type": "intrusion-set",
                        "spec_version": "2.1",
                        "id": profile_stix_id("intrusion-set", "actor--example"),
                        "created": "2026-01-01T00:00:00Z",
                        "modified": "2026-01-01T00:00:00Z",
                        "name": "Example",
                    }
                ],
            },
        )
        actor_entry = {
            "slug": "example",
            "profile_id": "actor--example",
            "name": "Example",
            "path": "opencti/actors/example.stix2.json",
            "object_count": 1,
            "campaign_bundle_count": 1,
            "activity_bundle_count": 2,
            "size_bytes": actor_path.stat().st_size,
        }
        campaign_entry = self._bundle_entry(
            "campaigns/example/campaign.stix2.json", "campaign"
        )
        grouping_entry = self._bundle_entry(
            "activities/example/grouping.stix2.json", "grouping"
        )
        standalone_entry = self._bundle_entry(
            "activities/unattributed/incident.stix2.json",
            "incident",
            standalone=True,
        )
        sizes = [
            actor_entry["size_bytes"],
            campaign_entry["size_bytes"],
            grouping_entry["size_bytes"],
            standalone_entry["size_bytes"],
        ]
        manifest: dict[str, object] = {
            "schema_version": "1.1.0",
            "format": "STIX 2.1 bundles for OpenCTI ImportFileStix",
            "generated_at": "2026-09-22T00:00:00Z",
            "producer_identity": "identity--11111111-1111-4111-8111-111111111111",
            "object_marking": "TLP:CLEAR",
            "import_order": ["actors", "campaigns", "activities"],
            "actor_bundle_count": 1,
            "campaign_bundle_count": 1,
            "activity_bundle_count": 2,
            "standalone_activity_bundle_count": 1,
            "activity_type_counts": {"grouping": 1, "incident": 1},
            "max_bundle_size_bytes": max(sizes),
            "unresolved_actor_relationships": [],
            "actors": [actor_entry],
            "campaigns": [campaign_entry],
            "activities": [grouping_entry, standalone_entry],
            "standalone_activities": [copy.deepcopy(standalone_entry)],
        }
        write_json(self.opencti / "manifest.json", manifest)
        return manifest

    def _rewrite_manifest(self) -> None:
        write_json(self.opencti / "manifest.json", self.manifest)

    def test_packages_are_reproducible_and_scoped(self) -> None:
        first = self.workspace / "first"
        second = self.workspace / "second"
        result = package_distribution(self.opencti, first)
        package_distribution(self.opencti, second)

        expected_assets = {
            "opencti-stix-all.tar.gz",
            "opencti-stix-all.zip",
            "opencti-stix-actors.tar.gz",
            "opencti-stix-campaigns.tar.gz",
            "opencti-stix-activities.tar.gz",
            "opencti-manifest.json",
            "SHA256SUMS",
        }
        self.assertEqual({path.name for path in first.iterdir()}, expected_assets)
        self.assertTrue(
            all(path.stat().st_mode & 0o777 == 0o644 for path in first.iterdir())
        )
        self.assertEqual(result["bundle_counts"], {
            "actors": 1,
            "campaigns": 1,
            "activities": 2,
        })
        for name in expected_assets:
            self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())

        all_members = {
            "opencti/README.md",
            "opencti/manifest.json",
            "opencti/actors/example.stix2.json",
            "opencti/campaigns/example/campaign.stix2.json",
            "opencti/activities/example/grouping.stix2.json",
            "opencti/activities/unattributed/incident.stix2.json",
        }
        with tarfile.open(first / "opencti-stix-all.tar.gz", "r:gz") as archive:
            members = archive.getmembers()
            self.assertEqual([item.name for item in members], sorted(all_members))
            self.assertTrue(all(item.mtime == 0 for item in members))
            self.assertTrue(all(item.mode == 0o644 for item in members))
            self.assertTrue(all(item.uid == item.gid == 0 for item in members))
        with tarfile.open(first / "opencti-stix-actors.tar.gz", "r:gz") as archive:
            self.assertEqual(
                {item.name for item in archive.getmembers()},
                {
                    "opencti/README.md",
                    "opencti/manifest.json",
                    "opencti/actors/example.stix2.json",
                },
            )
        with zipfile.ZipFile(first / "opencti-stix-all.zip") as archive:
            self.assertEqual(set(archive.namelist()), all_members)
            self.assertTrue(
                all(
                    item.date_time == (1980, 1, 1, 0, 0, 0)
                    for item in archive.infolist()
                )
            )

        self.assertEqual(
            (first / "opencti-manifest.json").read_bytes(),
            (self.opencti / "manifest.json").read_bytes(),
        )
        checksum_lines = (first / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
        checksum_names = [line.split("  ", 1)[1] for line in checksum_lines]
        self.assertEqual(checksum_names, sorted(expected_assets - {"SHA256SUMS"}))
        for line in checksum_lines:
            digest, name = line.split("  ", 1)
            self.assertEqual(
                digest, hashlib.sha256((first / name).read_bytes()).hexdigest()
            )

    def test_rejects_missing_bundle(self) -> None:
        (self.opencti / "actors/example.stix2.json").unlink()
        with self.assertRaisesRegex(ValueError, "bundle is missing"):
            validate_distribution(self.opencti)

    def test_rejects_unlisted_bundle(self) -> None:
        write_json(
            self.opencti / "actors/unlisted.stix2.json",
            {"type": "bundle", "objects": []},
        )
        with self.assertRaisesRegex(ValueError, "coverage mismatch"):
            validate_distribution(self.opencti)

    def test_rejects_manifest_drift_and_unsafe_paths(self) -> None:
        self.manifest["actors"][0]["size_bytes"] = 1  # type: ignore[index]
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "size mismatch"):
            validate_distribution(self.opencti)

        self.manifest = self._build_fixture()
        self.manifest["actors"][0][  # type: ignore[index]
            "path"
        ] = "opencti/actors/../README.md"
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "unsafe OpenCTI manifest path"):
            validate_distribution(self.opencti)

    def test_rejects_type_and_standalone_boundary_drift(self) -> None:
        self.manifest["campaigns"][0][  # type: ignore[index]
            "stix_object_type"
        ] = "grouping"
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "campaign manifest/type mismatch"):
            validate_distribution(self.opencti)

        self.manifest = self._build_fixture()
        self.manifest["standalone_activities"][0][  # type: ignore[index]
            "slug"
        ] = "named-actor"
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "differs from its activity entry"):
            validate_distribution(self.opencti)

    def test_rejects_actor_without_canonical_intrusion_set(self) -> None:
        actor_path = self.opencti / "actors/example.stix2.json"
        bundle = json.loads(actor_path.read_text(encoding="utf-8"))
        bundle["objects"][0]["id"] = (
            "intrusion-set--22222222-2222-4222-8222-222222222222"
        )
        write_json(actor_path, bundle)
        self.manifest["actors"][0][  # type: ignore[index]
            "size_bytes"
        ] = actor_path.stat().st_size
        self.manifest["max_bundle_size_bytes"] = max(
            item["size_bytes"]  # type: ignore[index]
            for section in ("actors", "campaigns", "activities")
            for item in self.manifest[section]  # type: ignore[index]
        )
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "canonical intrusion-set"):
            validate_distribution(self.opencti)

    def test_rejects_activity_id_without_matching_primary_object(self) -> None:
        self.manifest["campaigns"][0][  # type: ignore[index]
            "activity_id"
        ] = "activity--not-the-primary"
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "matching primary object"):
            validate_distribution(self.opencti)

    def test_rejects_omitted_flagged_standalone_activity(self) -> None:
        self.manifest["standalone_activities"] = []
        self.manifest["standalone_activity_bundle_count"] = 0
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "does not exactly match"):
            validate_distribution(self.opencti)

    def test_rejects_actor_activity_counts_and_import_order_drift(self) -> None:
        self.manifest["actors"][0]["campaign_bundle_count"] = 999  # type: ignore[index]
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "actor campaign bundle count mismatch"):
            validate_distribution(self.opencti)

        self.manifest = self._build_fixture()
        self.manifest["actors"][0]["activity_bundle_count"] = 999  # type: ignore[index]
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "actor activity bundle count mismatch"):
            validate_distribution(self.opencti)

        self.manifest = self._build_fixture()
        self.manifest["import_order"] = ["campaigns", "actors", "activities"]
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "manifest import_order mismatch"):
            validate_distribution(self.opencti)

    def test_rejects_boolean_manifest_count(self) -> None:
        self.manifest["campaigns"][0]["object_count"] = True  # type: ignore[index]
        self._rewrite_manifest()
        with self.assertRaisesRegex(ValueError, "must be a non-negative integer"):
            validate_distribution(self.opencti)

    def test_rejects_bundle_over_configured_limit(self) -> None:
        with self.assertRaisesRegex(ValueError, "exceeds"):
            validate_distribution(self.opencti, max_bundle_bytes=1)

    def test_rejects_unexpected_release_output_entries(self) -> None:
        output = self.workspace / "release"
        output.mkdir()
        (output / "do-not-upload.txt").write_text("unexpected", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unexpected entries"):
            package_distribution(self.opencti, output)


if __name__ == "__main__":
    unittest.main()
