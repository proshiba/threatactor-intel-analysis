from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROFILE_PATH = ROOT / "profiles/gunra/actor-profile.json"
IOCS_PATH = ROOT / "profiles/gunra/iocs.json"
ARTIFACTS_PATH = ROOT / "profiles/gunra/artifacts.csv"
MANIFEST_PATH = ROOT / "profiles/gunra/ioc-sources.json"

SOURCE_ID = "source--ahnlab-operation-double-barrel-2026"
INCIDENT_ID = "activity--gunra-operation-double-barrel-incident-2026-03"
GROUPING_ID = "activity--operation-double-barrel-technical-overlap-2026"
INFRA_ID = "infrastructure--gunra-operation-double-barrel-network"


class GunraOperationDoubleBarrelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
        cls.iocs = json.loads(IOCS_PATH.read_text(encoding="utf-8"))
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        with ARTIFACTS_PATH.open(encoding="utf-8", newline="") as stream:
            cls.artifacts = list(csv.DictReader(stream))

    def test_source_date_hash_and_version_boundary_are_preserved(self) -> None:
        source = next(
            item for item in self.profile["sources"] if item["source_id"] == SOURCE_ID
        )
        self.assertEqual(source["published_at"]["value"], "2026-07-30T00:00:00Z")
        self.assertEqual(
            source["sha256"],
            "21615fcb3c88ffde1b6ce0527f8a8232943bc265d3a88f1ecf20cde1a14da1ab",
        )
        self.assertIn("Operation%20Double%20Barrel", source["url"])
        self.assertIn("v1.2", source["analyst_notes"])
        self.assertIn("2026-08-11", source["analyst_notes"])
        self.assertIn("publication date", source["analyst_notes"])

        manifest_source = self.manifest["sources"][0]
        self.assertEqual(manifest_source["source_id"], SOURCE_ID)
        self.assertEqual(
            manifest_source["published_at"]["value"], "2026-07-30T00:00:00Z"
        )
        self.assertEqual(
            manifest_source["default_observed_at"]["status"], "unknown"
        )

    def test_gunra_incident_and_cross_cluster_grouping_are_separated(self) -> None:
        activities = {
            item["activity_id"]: item for item in self.profile["activities"]
        }
        incident = activities[INCIDENT_ID]
        grouping = activities[GROUPING_ID]

        self.assertEqual(incident["stix_object_type"], "incident")
        self.assertEqual(incident["first_observed"]["value"], "2026-03-01T00:00:00Z")
        self.assertEqual(incident["last_observed"]["value"], "2026-03-01T00:00:00Z")
        self.assertEqual(incident["reported_at"]["value"], "2026-07-30T00:00:00Z")
        self.assertEqual(incident["reported_at"]["basis"], "source-publication")
        self.assertIn("malware--gunra-ransomware", incident["malware_refs"])
        self.assertIn("target--gunra--sector--pharmaceuticals", incident["target_refs"])
        self.assertIn(INFRA_ID, incident["infrastructure_refs"])

        self.assertEqual(grouping["stix_object_type"], "grouping")
        self.assertEqual(grouping["grouping_context"], "suspicious-activity")
        self.assertEqual(grouping["activity_refs"], [INCIDENT_ID])
        self.assertEqual(grouping["first_observed"]["value"], "2026-01-01T00:00:00Z")
        self.assertEqual(grouping["last_observed"]["value"], "2026-03-01T00:00:00Z")
        self.assertEqual(grouping["confidence"], "medium")
        self.assertIn("same actor", grouping["description"])
        self.assertIn("確定せず", grouping["description"])
        self.assertIn("Actor/Intrusion Setへ昇格せず", grouping["analyst_notes"])

    def test_anonymous_cluster_is_not_promoted_or_merged(self) -> None:
        self.assertEqual(self.profile["attribution"]["countries"], [])
        self.assertEqual(self.profile["attribution"]["sponsor_type"], "criminal")
        self.assertEqual(self.profile["relationships"], [])
        aliases = {item["name"].casefold() for item in self.profile["actor"]["aliases"]}
        self.assertNotIn("lazarus", aliases)
        malware_names = {
            item["name"].casefold() for item in self.profile["capabilities"]["malware"]
        }
        self.assertNotIn("brandoor", malware_names)
        self.assertNotIn("copperhedge", malware_names)

    def test_ahnlab_evidence_does_not_leak_into_older_cisa_activities(self) -> None:
        activities = {
            item["activity_id"]: item for item in self.profile["activities"]
        }
        for activity_id in (
            "activity--gunra-raas-2025-2026",
            "activity--gunra-knpa-vdi-intrusion-2025",
        ):
            diamond = activities[activity_id]["diamond_model"]
            self.assertNotIn(SOURCE_ID, diamond["evidence_refs"])
            self.assertNotIn(INFRA_ID, diamond["infrastructure"]["infrastructure_refs"])

        legacy_tool_ids = {"tool--gunra-openssh", "tool--gunra-filezilla"}
        legacy_tools = [
            item
            for item in self.profile["capabilities"]["tools"]
            if item["id"] in legacy_tool_ids
        ]
        self.assertEqual(len(legacy_tools), 2)
        for tool in legacy_tools:
            self.assertEqual(tool["evidence_refs"], ["source--cisa-aa26-222a-gunra"])

        legacy_ttp_ids = {
            "ttp--gunra-t1003",
            "ttp--gunra-t1021-001",
            "ttp--gunra-t1105",
            "ttp--gunra-t1486",
            "ttp--gunra-t1572",
        }
        legacy_ttps = [
            item for item in self.profile["ttps"] if item["ttp_id"] in legacy_ttp_ids
        ]
        self.assertEqual(len(legacy_ttps), 5)
        for ttp in legacy_ttps:
            self.assertNotIn(SOURCE_ID, ttp["evidence_refs"])
            self.assertNotIn(INCIDENT_ID, ttp["activity_refs"])
            self.assertNotIn(GROUPING_ID, ttp["activity_refs"])

    def test_exact_iocs_are_source_scoped_and_not_timestamped_by_publication(self) -> None:
        indicators = self.iocs["indicators"]
        expected = {
            ("md5", "6512bc560bc2199c24f946b67c5bf1d5"),
            ("md5", "b3c4a6abd9c39ccae8a628f2ce2513b5"),
            ("url", "https://anyonecdn.com/"),
            ("domain", "anyonecdn.com"),
            ("url", "https://jshosting.me/_common/_view/?id=2021043321"),
            ("domain", "jshosting.me"),
            ("ipv4", "141.164.44.139"),
            ("ipv4", "158.247.212.35"),
            ("ipv4", "158.247.240.44"),
            ("ipv4", "176.65.128.26"),
            ("ipv4", "45.32.25.205"),
        }
        actual = {(item["type"], item["normalized_value"]) for item in indicators}
        self.assertEqual(actual, expected)
        self.assertEqual(len(indicators), 11)

        for indicator in indicators:
            self.assertEqual(indicator["campaign_refs"], [GROUPING_ID])
            self.assertEqual(indicator["first_observed"]["status"], "unknown")
            self.assertEqual(indicator["last_observed"]["status"], "unknown")
            observation = indicator["observations"][0]
            self.assertEqual(observation["observed_at"]["status"], "unknown")
            self.assertEqual(
                observation["source_published_at"]["value"],
                "2026-07-30T00:00:00Z",
            )
            self.assertEqual(observation["source_id"], SOURCE_ID)

        shared_ip = next(
            item for item in indicators if item["normalized_value"] == "176.65.128.26"
        )
        self.assertEqual(shared_ip["infrastructure_refs"], [INFRA_ID])
        self.assertTrue(
            {"c2", "reverse-tunnel", "payload-download", "shared-infrastructure"}
            <= set(shared_ip["roles"])
        )

    def test_hunting_artifacts_preserve_exact_context_and_time_precision(self) -> None:
        self.assertEqual(len(self.artifacts), 17)
        artifacts = {(item["artifact_type"], item["value"]): item for item in self.artifacts}

        sync_host = artifacts[("process-name", "SyncHost.exe")]
        self.assertEqual(sync_host["observed_at"], "2026-03-01T00:00:00Z")
        self.assertEqual(sync_host["observed_at_precision"], "month")
        self.assertIn("legitimate-process", json.loads(sync_host["roles"]))

        fingerprint = artifacts[
            ("sample-string", "Qr1to32lQHxEu6phzNyrTZrU0iElrOfVWMBLnqoen24")
        ]
        self.assertIn("ssh-key-fingerprint", json.loads(fingerprint["roles"]))
        self.assertEqual(fingerprint["observed_at"], "2026-03-01T00:00:00Z")

        hotfix = artifacts[("file-name", "hotfix.exe")]
        self.assertEqual(hotfix["observed_at"], "")
        self.assertEqual(hotfix["observed_at_status"], "unknown")
        self.assertIn("renamed-psexec", json.loads(hotfix["roles"]))

        for artifact in self.artifacts:
            self.assertEqual(artifact["source_published_at"], "2026-07-30T00:00:00Z")
            self.assertEqual(artifact["source_id"], SOURCE_ID)


if __name__ == "__main__":
    unittest.main()
