#!/usr/bin/env python3
"""Regression tests for observable classification and normalization."""

from __future__ import annotations

import sys
import unittest
import json
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from common import normalize_observable, normalize_time  # noqa: E402
from ingest_observables import extract_artifacts, extract_iocs  # noqa: E402


class ObservableBoundaryTests(unittest.TestCase):
    def test_ioc_types_are_kept_out_of_artifacts(self) -> None:
        text = (
            "IOC: hxxps://c2[.]example/path, 192.0.2.10, "
            "44d88612fea8a8f36de82e1278abb02f"
        )
        iocs = extract_iocs(
            text, allow_plain_domains=True, explicit_structured=False
        )
        self.assertIn(("ipv4", "192.0.2.10", "confirmed"), iocs)
        self.assertTrue(any(kind == "url" for kind, _, _ in iocs))
        self.assertTrue(any(kind == "md5" for kind, _, _ in iocs))
        self.assertFalse(extract_artifacts(text, explicit_structured=False))

    def test_non_ioc_artifacts_are_classified(self) -> None:
        text = (
            r"powershell.exe -enc AAA; C:\ProgramData\stage.dll; "
            r"HKCU\SOFTWARE\Example\Run"
        )
        kinds = {
            kind for kind, _, _ in extract_artifacts(text, explicit_structured=True)
        }
        self.assertIn("command", kinds)
        self.assertIn("file-path", kinds)
        self.assertIn("registry-key", kinds)

    def test_file_names_are_not_domains(self) -> None:
        values = extract_iocs(
            "IOC table: loader.exe report.pdf c2.example.org",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {normalize_observable(kind, value) for kind, value, _ in values}
        self.assertEqual(domains, {"c2.example.org"})


class TimeTests(unittest.TestCase):
    def test_invalid_calendar_date_becomes_unknown(self) -> None:
        point = normalize_time("2020-46", basis="same-record")
        self.assertEqual(point["status"], "unknown")
        self.assertIsNone(point["value"])
        self.assertEqual(point["basis"], "invalid-calendar-date:same-record")


class CollectionTests(unittest.TestCase):
    def test_catalog_and_generated_profiles_are_complete(self) -> None:
        root = Path(__file__).resolve().parents[2]
        catalog = json.loads(
            (root / "actor_profile" / "corpus-catalog.json").read_text(
                encoding="utf-8"
            )
        )
        slugs = [actor["slug"] for actor in catalog["actors"]]
        self.assertEqual(len(slugs), len(set(slugs)))
        for actor in catalog["actors"]:
            profile_path = root / "profiles" / actor["slug"] / "actor-profile.json"
            self.assertTrue(profile_path.is_file(), actor["slug"])
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            self.assertEqual(profile["profile_id"], f"actor--{actor['slug']}")
            self.assertFalse(
                any(
                    alias["name"].lower().startswith(("http://", "https://"))
                    for alias in profile["actor"]["aliases"]
                ),
                actor["slug"],
            )

    def test_collection_validation_has_no_errors(self) -> None:
        root = Path(__file__).resolve().parents[2]
        summary = json.loads(
            (root / "profiles" / "processing-summary.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(summary["actor_count"], len(summary["results"]))
        self.assertEqual(summary["error_count"], 0)
        self.assertTrue(all(item["status"] == "complete" for item in summary["results"]))


if __name__ == "__main__":
    unittest.main()
