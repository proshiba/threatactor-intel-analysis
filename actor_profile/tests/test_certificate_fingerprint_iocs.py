#!/usr/bin/env python3
"""Regression checks for typed certificate-fingerprint IOC ingestion."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class CertificateFingerprintIOCTests(unittest.TestCase):
    def pivot(self, actor: str, pivot_id: str) -> dict:
        profile = json.loads(
            (ROOT / "profiles" / actor / "actor-profile.json").read_text()
        )
        return next(
            item for item in profile["hunting_pivots"] if item["pivot_id"] == pivot_id
        )

    def test_manifest_schema_models_algorithm_and_reviewed_exclusions(self) -> None:
        schema = json.loads(
            (ROOT / "actor_profile" / "schemas" / "ioc-sources.schema.json").read_text()
        )
        source_properties = schema["properties"]["sources"]["items"]["properties"]
        self.assertEqual(
            source_properties["field_map"]["$ref"], "#/$defs/fieldMap"
        )
        self.assertIn(
            "hash_algorithm", schema["$defs"]["fieldMap"]["properties"]
        )
        excluded_item = schema["$defs"]["excludedIocs"]["items"]
        self.assertEqual(
            excluded_item["required"], ["type", "value", "reason"]
        )

    def indicator(self, actor: str, value: str) -> dict:
        dataset = json.loads((ROOT / "profiles" / actor / "iocs.json").read_text())
        return next(
            item
            for item in dataset["indicators"]
            if item["normalized_value"] == value.lower()
        )

    def assert_certificate(
        self, actor: str, value: str, algorithm: str, stix_name: str, source_id: str
    ) -> dict:
        indicator = self.indicator(actor, value)
        self.assertEqual(indicator["type"], "certificate-fingerprint")
        self.assertEqual(indicator["hash_algorithm"], algorithm)
        self.assertIn(
            f"x509-certificate:hashes.'{stix_name}'", indicator["stix_pattern"]
        )
        self.assertEqual(
            {item["source_id"] for item in indicator["observations"]},
            {source_id},
        )
        self.assertTrue(
            all(
                item["source_published_at"] != item["observed_at"]
                for item in indicator["observations"]
            )
        )
        return indicator

    def test_confucius_asyncrat_thumbprint_is_x509_sha1(self) -> None:
        indicator = self.assert_certificate(
            "confucius",
            "dee2b1e9f3fd0fd8171648a3b528a85577c49ffa",
            "sha1",
            "SHA-1",
            "source--qianxin-confucius-operation-tibbar-2020",
        )
        self.assertNotIn("file:hashes", indicator["stix_pattern"])
        dataset = json.loads(
            (ROOT / "profiles" / "confucius" / "iocs.json").read_text()
        )
        self.assertFalse(
            any(
                item["normalized_value"]
                == "dee2b1e9f3fd0fd8171648a3b528a85577c49ffa"
                and item["type"] != "certificate-fingerprint"
                for item in dataset["indicators"]
            )
        )
        pivot = self.pivot(
            "confucius", "hunting-pivot--confucius-asyncrat-tls-certificate"
        )
        self.assertEqual(pivot["indicator_refs"], [indicator["indicator_id"]])

    def test_lazarus_lamera_fingerprints_keep_both_algorithms(self) -> None:
        sha256 = self.assert_certificate(
            "lazarus",
            "cd27daa4bed5c1cfd02b43c1322829dc5396d545f3912b9694fc5a2499d5089e",
            "sha256",
            "SHA-256",
            "source--withsecure-lazarus-no-pineapple-2023",
        )
        sha1 = self.assert_certificate(
            "lazarus",
            "6d0bffe68bc8992b60dc294ec68dd2b44a5fc6f4",
            "sha1",
            "SHA-1",
            "source--withsecure-lazarus-no-pineapple-2023",
        )
        pivot = self.pivot(
            "lazarus", "hunting-pivot--lazarus-lamera-code-signing-cert"
        )
        self.assertEqual(
            set(pivot["indicator_refs"]),
            {sha256["indicator_id"], sha1["indicator_id"]},
        )

    def test_driver_and_protocol_pivots_link_known_malware(self) -> None:
        earth = self.pivot(
            "earth-lusca", "hunting-pivot--earth-lusca-bthcam-driver"
        )
        self.assertEqual(
            earth["malware_refs"], ["malware--daily-f196d446e69f62aacb40"]
        )
        bthcam = self.indicator(
            "earth-lusca", "44dc4a08c5eb0972c8e18b0e01284e06f09006bb"
        )
        self.assertEqual(
            bthcam["malware_refs"], ["malware--daily-f196d446e69f62aacb40"]
        )
        wellmess = self.pivot(
            "apt29", "hunting-pivot--apt29-wellmess-tunis-tls-dn"
        )
        self.assertEqual(wellmess["malware_refs"], ["malware--wellmess"])


if __name__ == "__main__":
    unittest.main()
