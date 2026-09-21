#!/usr/bin/env python3
"""Ensure exact file-hash pivots remain in the reproducible IOC datasets."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "actor_profile" / "osint" / "hunting-entity-research.json"
FILE_HASH_PATTERN = re.compile(
    r"file:hashes\.'(MD5|SHA-1|SHA-256|SHA-512)'\s*=\s*'([0-9A-Fa-f]+)'"
)
IOC_TYPE = {
    "MD5": "md5",
    "SHA-1": "sha1",
    "SHA-256": "sha256",
    "SHA-512": "sha512",
}


class HuntingPivotIOCTests(unittest.TestCase):
    def test_exact_file_hash_pivots_are_in_actor_ioc_datasets(self) -> None:
        research = json.loads(RESEARCH.read_text(encoding="utf-8"))
        checked = 0

        for slug, update in research["profiles"].items():
            pivots = update.get("hunting_pivots", [])
            hash_pivots = [
                (pivot, FILE_HASH_PATTERN.findall(pivot.get("stix_pattern") or ""))
                for pivot in pivots
            ]
            hash_pivots = [item for item in hash_pivots if item[1]]
            if not hash_pivots:
                continue

            dataset = json.loads(
                (ROOT / "profiles" / slug / "iocs.json").read_text(
                    encoding="utf-8"
                )
            )
            indicators = {
                (item["type"], item["normalized_value"].lower()): item
                for item in dataset["indicators"]
            }
            indicators_by_id = {
                item["indicator_id"]: item for item in dataset["indicators"]
            }

            for pivot in pivots:
                for indicator_ref in pivot.get("indicator_refs", []):
                    with self.subTest(
                        slug=slug,
                        pivot=pivot["pivot_id"],
                        indicator_ref=indicator_ref,
                    ):
                        self.assertIn(indicator_ref, indicators_by_id)
                        source_refs = {
                            observation["source_id"]
                            for observation in indicators_by_id[indicator_ref][
                                "observations"
                            ]
                        }
                        self.assertTrue(
                            source_refs.intersection(pivot["evidence_refs"])
                        )

            for pivot, matches in hash_pivots:
                for algorithm, value in matches:
                    checked += 1
                    key = (IOC_TYPE[algorithm], value.lower())
                    with self.subTest(slug=slug, pivot=pivot["pivot_id"], hash=value):
                        self.assertIn(key, indicators)
                        indicator = indicators[key]
                        self.assertIn(
                            indicator["indicator_id"],
                            pivot.get("indicator_refs", []),
                        )
                        self.assertEqual(indicator["disposition"], "confirmed")
                        source_refs = {
                            observation["source_id"]
                            for observation in indicator["observations"]
                        }
                        self.assertTrue(
                            source_refs.intersection(pivot["evidence_refs"])
                        )
                        for observation in indicator["observations"]:
                            observed = observation["observed_at"].get("value")
                            published = observation["source_published_at"].get(
                                "value"
                            )
                            if observed and published:
                                self.assertNotEqual(observed, published)

        self.assertGreaterEqual(checked, 11)


if __name__ == "__main__":
    unittest.main()
