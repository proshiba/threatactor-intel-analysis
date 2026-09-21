#!/usr/bin/env python3
"""Regression tests for the manually curated CoolClient observable source."""

from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROFILE_DIR = ROOT / "profiles" / "mustang-panda"
SOURCE_ID = "source--daily-9232cff77ce0ef8f62b1"
ACTIVITY_ID = "activity--daily-b8b3301d837c22e89850"
MALWARE_ID = "malware--coolclient"
DRIVER_HASHES = {
    "2d7c8780e97409770a9d4f31c66c9d63",
    "9460e150e1981d5c165043520c5c12fe",
}
CERTIFICATE_SERIAL_AS_HEX = "3e62dc5d8d612a2633e76bdfd60719dd"


class MustangPandaCoolClientObservableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.iocs = json.loads((PROFILE_DIR / "iocs.json").read_text())
        with (PROFILE_DIR / "artifacts.csv").open(newline="", encoding="utf-8") as handle:
            cls.artifacts = list(csv.DictReader(handle))

    def test_msagent_driver_hashes_are_activity_scoped_iocs(self) -> None:
        indicators = {
            item["normalized_value"]: item
            for item in self.iocs["indicators"]
            if item["type"] == "md5"
        }
        self.assertTrue(DRIVER_HASHES.issubset(indicators))
        for value in DRIVER_HASHES:
            indicator = indicators[value]
            self.assertEqual(indicator["disposition"], "confirmed")
            self.assertEqual(indicator["campaign_refs"], [ACTIVITY_ID])
            self.assertEqual(indicator["malware_refs"], [MALWARE_ID])
            self.assertEqual(indicator["roles"], ["malware-sample"])
            self.assertIsNone(indicator["first_observed"]["value"])
            self.assertIsNone(indicator["last_observed"]["value"])
            observation = next(
                item
                for item in indicator["observations"]
                if item["source_id"] == SOURCE_ID
            )
            self.assertIsNone(observation["observed_at"]["value"])
            self.assertEqual(
                observation["source_published_at"]["value"],
                "2026-08-14T00:00:00Z",
            )

    def test_msagent_file_name_is_preserved_as_artifact(self) -> None:
        artifact = next(
            item
            for item in self.artifacts
            if item["artifact_type"] == "file-name"
            and item["normalized_value"] == "msagent.sys"
            and item["source_id"] == SOURCE_ID
        )
        self.assertEqual(json.loads(artifact["campaign_refs"]), [ACTIVITY_ID])
        self.assertEqual(json.loads(artifact["malware_refs"]), [MALWARE_ID])
        self.assertEqual(json.loads(artifact["roles"]), ["malware-sample"])
        self.assertEqual(artifact["observed_at"], "")
        self.assertEqual(artifact["source_published_at"], "2026-08-14T00:00:00Z")

    def test_certificate_serial_is_not_misclassified_as_md5(self) -> None:
        md5_values = {
            item["normalized_value"]
            for item in self.iocs["indicators"]
            if item["type"] == "md5"
        }
        self.assertNotIn(CERTIFICATE_SERIAL_AS_HEX, md5_values)


if __name__ == "__main__":
    unittest.main()
