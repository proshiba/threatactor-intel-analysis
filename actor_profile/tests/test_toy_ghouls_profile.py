#!/usr/bin/env python3
"""Regression checks for the evidence-scoped Toy Ghouls draft profile."""

from __future__ import annotations

import copy
import csv
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROFILE_DIR = ROOT / "profiles" / "toy-ghouls"
SCRIPTS = ROOT / "actor_profile" / "scripts"
sys.path.insert(0, str(SCRIPTS))

from validate_profile import (  # noqa: E402
    validate_artifacts,
    validate_iocs,
    validate_profile,
)


F6_2025 = "source--f6-bearlyfy-2025-09-23"
KASPERSKY_MARCH = "source--kaspersky-toy-ghouls-2026-03-12"
F6_2026 = "source--f6-bearlyfy-2026-03-25"
KASPERSKY_GENIE = "source--kaspersky-genielocker-2026-07-30"
KASPERSKY_BIRD = "source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04"


class ToyGhoulsProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profile = json.loads(
            (PROFILE_DIR / "actor-profile.json").read_text(encoding="utf-8")
        )
        cls.iocs = json.loads(
            (PROFILE_DIR / "iocs.json").read_text(encoding="utf-8")
        )
        cls.manifest = json.loads(
            (PROFILE_DIR / "ioc-sources.json").read_text(encoding="utf-8")
        )
        with (PROFILE_DIR / "artifacts.csv").open(
            encoding="utf-8", newline=""
        ) as stream:
            cls.artifacts = list(csv.DictReader(stream))

    def observations_for(self, source_id: str, observable_type: str | None = None):
        result = []
        for indicator in self.iocs["indicators"]:
            if observable_type and indicator["type"] != observable_type:
                continue
            for observation in indicator["observations"]:
                if observation["source_id"] == source_id:
                    result.append((indicator, observation))
        return result

    def test_profile_is_draft_intrusion_set_without_geographic_inference(self) -> None:
        self.assertEqual(self.profile["profile_id"], "actor--toy-ghouls")
        self.assertEqual(self.profile["status"], "draft")
        self.assertEqual(self.profile["attribution"]["countries"], [])
        self.assertEqual(self.profile["actor"]["active"], "unknown")
        self.assertEqual(
            self.profile["actor"]["first_seen"]["value"],
            "2025-01-01T00:00:00Z",
        )
        self.assertEqual(
            self.profile["actor"]["last_seen"]["value"],
            "2026-07-01T00:00:00Z",
        )
        self.assertIn("source-scoped", self.profile["attribution"]["analyst_notes"])
        self.assertIn("origin", self.profile["attribution"]["analyst_notes"])

    def test_aliases_are_correct_and_never_exact(self) -> None:
        aliases = {item["name"]: item for item in self.profile["actor"]["aliases"]}
        self.assertEqual(
            set(aliases), {"Bearlyfy", "Labubu", "Laboo.boo", "Feral Wolf"}
        )
        self.assertNotIn("Labuib", aliases)
        self.assertTrue(all(item["scope"] != "exact" for item in aliases.values()))
        self.assertEqual(aliases["Feral Wolf"]["confidence"], "medium")
        self.assertEqual(aliases["Feral Wolf"]["evidence_refs"], [KASPERSKY_BIRD])

    def test_head_mare_and_phantomcore_boundaries_are_preserved(self) -> None:
        relationships = {
            item["relationship_id"]: item for item in self.profile["relationships"]
        }
        self.assertEqual(
            relationships[
                "relationship--toy-ghouls--head-mare--shares-infrastructure"
            ]["evidence_refs"],
            [KASPERSKY_MARCH],
        )
        self.assertEqual(
            relationships["relationship--toy-ghouls--head-mare--shares-tools"][
                "evidence_refs"
            ],
            [KASPERSKY_MARCH],
        )
        self.assertEqual(
            relationships["relationship--toy-ghouls--head-mare--cooperates"][
                "evidence_refs"
            ],
            [F6_2026],
        )
        phantomcore = relationships[
            "relationship--toy-ghouls--phantomcore--shares-infrastructure"
        ]
        self.assertEqual(phantomcore["evidence_refs"], [F6_2025])
        self.assertIn("自律的", phantomcore["analyst_notes"])
        self.assertEqual(phantomcore["first_observed"]["status"], "unknown")
        self.assertEqual(phantomcore["last_observed"]["status"], "unknown")
        self.assertIn("同時利用ではない", phantomcore["analyst_notes"])
        forbidden = {"part-of", "subgroup-of", "exact", "same-as"}
        self.assertFalse(
            forbidden
            & {item["relationship_type"] for item in relationships.values()}
        )

    def test_f6_2025_uses_a_directly_verified_archive(self) -> None:
        source = next(
            item for item in self.profile["sources"] if item["source_id"] == F6_2025
        )
        self.assertEqual(source["url"], "https://www.f6.ru/blog/bearlyfy/")
        self.assertEqual(
            source["archive_url"],
            "https://web.archive.org/web/20251006200710id_/https://www.f6.ru/blog/bearlyfy/",
        )
        self.assertEqual(
            source["sha256"],
            "baca14b555e6dbcc26516f079c9dee019185772a5938c5e67bac65fc143e5fc1",
        )
        self.assertIn("現行URL", source["analyst_notes"])
        self.assertIn("Internet Archive", source["analyst_notes"])
        self.assertIn("63/63", source["analyst_notes"])
        self.assertNotIn("検索インデックス", source["analyst_notes"])

        manifest_source = next(
            item for item in self.manifest["sources"] if item["source_id"] == F6_2025
        )
        self.assertIn("保存版本文", manifest_source["analyst_notes"])
        self.assertIn("63/63", manifest_source["analyst_notes"])

        f6_2026 = next(
            item for item in self.profile["sources"] if item["source_id"] == F6_2026
        )
        self.assertIn("一次URL本文を直接取得", f6_2026["analyst_notes"])
        self.assertNotIn("検索インデックス", f6_2026["analyst_notes"])

    def test_public_file_hashes_are_complete_for_the_reviewed_tables(self) -> None:
        f6_expected = {
            "7d5a7965fe464b391daf0d36dfb862d7f53c7728",
            "bdf776d83aaf85931d2cf2bc53ae5606fcac8f81",
            "2d66caeb7d4fd81ea47b3286fce1ad66a939d0d4",
            "ade71388dc2fbcb33e69406e88e26d67cd43fa67",
            "4268bfee48695e1625d96e9eb904bb14d2eac6dd",
            "6c0b7a83ce46e6ffa34ac3fb04cd574bc02ae11d",
            "5c7a612482a7af27b11f17e2e793c6f3dd856248",
            "a60d6d6e1745220b143bbfb6b214594cbd1ce8d8",
            "6feaac36d6c9175bd7bbba1279cc6430976e12bd",
            "b8fd7845c0bb56ab786ab9801da4531b81dd12cc",
            "9f8f60e2c3c33ede923be622dd60f623a064e6dd",
            "835bd6a13ad025a34b85d51ecfd38c1d06f177ea",
            "ca7321d8e778310d2b14d6082ac055df7f8c75c2",
            "4ed37e27932f0db5ff98c8a6f5ea1b3ce078ab7a",
            "e23d1c937c5e4b1d116010d5c9b1412a59c67b88",
            "8c7b5a3e82791123b9810b065244ad1f95a3fc6c",
            "8836d741b13d192b70acdc684ad3fb28b52149ea",
            "48fc0f8fe7f8cf20b4db9bd525798e48e5972bce",
            "59a97f9d7c1d6e10fa41ea9339568fb25ec55e27",
            "e132d57ee2afbb0a1c479631fd70e7df85623642",
            "0049580250a7b8e65311acb7995450c750afc4c3",
            "2e75c65977975110c8f7288801eb212f4557d6e0",
            "e838d6ddf4da432de631d0f0120fb94f696150c0",
            "f16f3c7dd300bb403135c0daf38bb163e4707a18",
            "ce36d71fbfd9d989a409f8a42a817996d53332d2",
        }
        f6_actual = {
            indicator["normalized_value"]
            for indicator, _ in self.observations_for(F6_2025, "sha1")
        }
        self.assertEqual(f6_actual, f6_expected)

        self.assertEqual(len(self.observations_for(KASPERSKY_MARCH, "md5")), 22)
        self.assertEqual(len(self.observations_for(KASPERSKY_GENIE, "md5")), 24)
        self.assertEqual(len(self.observations_for(KASPERSKY_BIRD, "md5")), 2)
        self.assertEqual(len(self.iocs["indicators"]), 101)
        self.assertEqual(
            sum(len(item["observations"]) for item in self.iocs["indicators"]),
            104,
        )

    def test_f6_network_iocs_and_time_semantics_are_preserved(self) -> None:
        network = {
            indicator["normalized_value"]
            for indicator, _ in self.observations_for(F6_2025)
            if indicator["type"] in {"ipv4", "domain"}
        }
        self.assertEqual(len(network), 16)
        self.assertTrue(
            {
                "195.133.32.213",
                "45.158.169.131",
                "185.158.248.107",
                "nextcloud.soft-trust.com",
                "nextcloud.1cbit.dev",
                "213.232.204.110",
                "softline-solutions.cloud",
                "pvec.ufolab.ovh",
            }
            <= network
        )

        first_sample = next(
            observation
            for indicator, observation in self.observations_for(F6_2025, "sha1")
            if indicator["normalized_value"]
            == "7d5a7965fe464b391daf0d36dfb862d7f53c7728"
        )
        self.assertEqual(
            first_sample["observed_at"]["value"], "2025-01-15T00:00:00Z"
        )
        kaspersky_hash = self.observations_for(KASPERSKY_MARCH, "md5")[0][1]
        self.assertEqual(kaspersky_hash["observed_at"]["status"], "unknown")
        self.assertIsNone(kaspersky_hash["observed_at"]["value"])

    def test_shared_values_are_nonexclusive_and_legitimate_services_are_excluded(self) -> None:
        by_value = {
            item["normalized_value"]: item for item in self.iocs["indicators"]
        }
        for value in {
            "195.133.32.213",
            "31.56.27.60",
            "185.158.248.107",
            "nextcloud.soft-trust.com",
        }:
            roles = {
                role
                for observation in by_value[value]["observations"]
                for role in observation["roles"]
            }
            self.assertIn("non-exclusive", roles, value)

        self.assertNotIn("broker.hivemq.com", by_value)
        self.assertNotIn("ip-api.com", by_value)
        self.assertNotIn("1cbit-dev.com", by_value)
        exclusions = {
            item["value"]
            for source in self.manifest["sources"]
            for item in source.get("excluded_iocs", [])
        }
        self.assertEqual(exclusions, {"broker.hivemq.com", "ip-api.com"})

    def test_activity_model_uses_incident_grouping_campaign_and_tool_refs(self) -> None:
        activities = {
            item["activity_id"]: item for item in self.profile["activities"]
        }
        self.assertEqual(len(activities), 6)
        self.assertEqual(
            activities["activity--toy-ghouls-ransomware-2025-2026"][
                "stix_object_type"
            ],
            "campaign",
        )
        self.assertEqual(
            activities["activity--toy-ghouls-ransomware-2025-2026"][
                "activity_refs"
            ],
            [],
        )
        self.assertEqual(
            activities["activity--toy-ghouls-april-2025-oil-incident"][
                "stix_object_type"
            ],
            "incident",
        )
        self.assertEqual(
            activities["activity--toy-ghouls-june-2025-attacks"][
                "stix_object_type"
            ],
            "grouping",
        )
        self.assertEqual(
            activities["activity--toy-ghouls-bird-backdoors-july-2026"][
                "grouping_context"
            ],
            "malware-analysis",
        )
        self.assertEqual(
            activities["activity--toy-ghouls-bird-backdoors-july-2026"][
                "tool_refs"
            ],
            ["tool--evil-winrm-winrm-fs"],
        )
        june_tools = set(
            activities["activity--toy-ghouls-june-2025-attacks"]["tool_refs"]
        )
        self.assertEqual(
            june_tools,
            {
                "tool--cloudflared",
                "tool--gost",
                "tool--psmapexec",
                "tool--modified-shinysocks",
            },
        )
        self.assertEqual(
            activities["activity--toy-ghouls-april-2025-oil-incident"][
                "diamond_model"
            ]["capability"]["malware_refs"],
            ["malware--babuk", "malware--lockbit-3-black"],
        )
        self.assertEqual(
            activities["activity--toy-ghouls-july-2025-construction-incident"][
                "diamond_model"
            ]["capability"]["malware_refs"],
            [],
        )

    def test_non_grouping_activity_cannot_act_as_a_containment_container(self) -> None:
        invalid = copy.deepcopy(self.profile)
        invalid["activities"][0]["activity_refs"] = [
            "activity--toy-ghouls-april-2025-oil-incident"
        ]
        issues = []
        validate_profile(invalid, issues)
        self.assertTrue(
            any(
                item.severity == "error"
                and item.location == "$.activities[0].activity_refs"
                and "only Grouping" in item.message
                for item in issues
            )
        )

    def test_hunting_artifacts_are_structured(self) -> None:
        values = {row["value"]: row for row in self.artifacts}
        self.assertTrue(
            {
                "config.toml",
                "cplsupport",
                "wtas",
                "panel-bot",
                "m.bird.cmd_response",
                "WinScHost",
                "Cloudflared agent",
                "DriverInitService",
            }
            <= set(values)
        )
        self.assertEqual(
            json.loads(values["panel-bot"]["malware_refs"]),
            ["malware--matrix-bird-agent"],
        )
        self.assertIn(
            "infrastructure--toy-ghouls-phantomcore-overlap",
            json.loads(values["dnsclient64.exe"]["infrastructure_refs"]),
        )

    def test_repository_validator_reports_no_errors(self) -> None:
        issues = []
        refs = validate_profile(self.profile, issues)
        validate_iocs(self.iocs, self.profile, refs, issues)
        artifact_refs = dict(refs)
        artifact_refs["source_ids"] = set(refs["source_ids"])
        artifact_refs["source_ids"].update(
            item["source_id"] for item in self.iocs["sources"]
        )
        validate_artifacts(
            PROFILE_DIR / "artifacts.csv", self.profile, artifact_refs, issues
        )
        errors = [item for item in issues if item.severity == "error"]
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
