#!/usr/bin/env python3
"""Regression tests for actor-free standalone Activity export."""

from __future__ import annotations

import json
import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "actor_profile/scripts"
sys.path.insert(0, str(SCRIPTS))

from build_opencti_bundles import producer_identity, validate_bundle  # noqa: E402
from standalone_activity_stix import (  # noqa: E402
    build_standalone_activity_bundle,
    validate_curation,
)


class StandaloneActivityStixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.curation = json.loads(
            (ROOT / "actor_profile/standalone-activity-curation.json").read_text(
                encoding="utf-8"
            )
        )
        ledger = json.loads(
            (ROOT / "parse-daily/unknown-clusters.json").read_text(encoding="utf-8")
        )
        cls.clusters = {
            item["cluster_id"]: item for item in ledger["clusters"]
        }
        records = validate_curation(cls.curation, ledger)
        producer = producer_identity(
            "2025-01-01T00:00:00Z", cls.curation["updated_at"]
        )
        cls.bundles = {}
        cls.metadata = {}
        for record in records:
            bundle, metadata = build_standalone_activity_bundle(
                record=record,
                updated_at=cls.curation["updated_at"],
                producer=producer,
            )
            cls.bundles[metadata["activity_id"]] = bundle
            cls.metadata[metadata["activity_id"]] = metadata

    def test_curation_is_explicit_and_covers_only_reviewed_scope(self) -> None:
        expected = {
            "activity--unattributed-bigbear-2-0",
            "activity--unattributed-secflow-ai-agent-campaign",
            "activity--unattributed-operation-quicsilver",
            "activity--unattributed-operation-cameraswarm",
            "activity--unattributed-xentry-mexico-bitlocker-incident",
            "activity--unattributed-project-cav3rn-technical-cluster",
            "activity--unattributed-knaithe-knyuan-evidence",
            "activity--unattributed-cavern-manticore-evidence",
            "activity--unattributed-heartlesssoul-evidence",
            "activity--unattributed-ted-curlrat-toolkit-evidence",
            "activity--unattributed-thehatman-self-claim",
        }
        self.assertEqual(set(self.bundles), expected)
        self.assertEqual(self.curation["held"], [])

    def test_bundles_are_actor_free_reference_complete_and_valid(self) -> None:
        for activity_id, bundle in self.bundles.items():
            with self.subTest(activity_id=activity_id):
                object_type = self.metadata[activity_id]["stix_object_type"]
                self.assertEqual(
                    validate_bundle(bundle, expected_scope=object_type), []
                )
                objects = bundle["objects"]
                self.assertFalse(
                    any(obj["type"] in {"intrusion-set", "threat-actor"} for obj in objects)
                )
                actor_types = {"intrusion-set", "threat-actor"}
                by_id = {obj["id"]: obj for obj in objects}
                for relationship in (
                    obj for obj in objects if obj["type"] == "relationship"
                ):
                    self.assertNotIn(by_id[relationship["source_ref"]]["type"], actor_types)
                    self.assertNotIn(by_id[relationship["target_ref"]]["type"], actor_types)

    def test_grouping_containment_does_not_generate_relationships(self) -> None:
        for activity_id, metadata in self.metadata.items():
            if metadata["stix_object_type"] != "grouping":
                continue
            objects = self.bundles[activity_id]["objects"]
            self.assertFalse(any(obj["type"] == "relationship" for obj in objects))
            grouping = next(obj for obj in objects if obj["type"] == "grouping")
            self.assertTrue(grouping["object_refs"])

    def test_non_normalized_ledger_facts_are_explicitly_note_only(self) -> None:
        for activity_id, metadata in self.metadata.items():
            bundle = self.bundles[activity_id]
            primary = next(
                obj
                for obj in bundle["objects"]
                if obj.get("x_profile_object_id") == activity_id
            )
            self.assertFalse(primary["x_unstructured_observables_promoted"])
            if metadata["structured_ioc_indicator_count"] == 0:
                self.assertEqual(primary["x_ioc_promotion_policy"], "none")
                self.assertFalse(
                    any(obj["type"] == "indicator" for obj in bundle["objects"])
                )

    def test_source_publication_is_not_activity_or_relationship_time(self) -> None:
        for activity_id, bundle in self.bundles.items():
            with self.subTest(activity_id=activity_id):
                source_reports = [
                    obj
                    for obj in bundle["objects"]
                    if obj.get("x_opencti_source_report")
                ]
                self.assertTrue(source_reports)
                self.assertTrue(
                    all(obj["x_temporal_role"] == "publication-only" for obj in source_reports)
                )
                container = next(
                    obj for obj in bundle["objects"] if obj.get("x_opencti_bundle_scope")
                )
                self.assertEqual(
                    container["x_temporal_role"], "bundle-generation-time"
                )
                for relationship in (
                    obj for obj in bundle["objects"] if obj["type"] == "relationship"
                ):
                    self.assertNotIn("start_time", relationship)
                    self.assertNotIn("stop_time", relationship)

    def test_time_precision_and_source_publication_are_strictly_validated(self) -> None:
        ledger = json.loads(
            (ROOT / "parse-daily/unknown-clusters.json").read_text(encoding="utf-8")
        )
        invalid_precision = copy.deepcopy(self.curation)
        invalid_precision["activities"][0]["first_observed"]["precision"] = "quarter"
        with self.assertRaisesRegex(ValueError, "precision is invalid"):
            validate_curation(invalid_precision, ledger)

        invalid_publication = copy.deepcopy(ledger)
        cluster_id = self.curation["activities"][0]["ledger_cluster_id"]
        cluster = next(
            item for item in invalid_publication["clusters"] if item["cluster_id"] == cluster_id
        )
        cluster["observations"][0]["published_at"] = "2026-99-99"
        with self.assertRaisesRegex(ValueError, "not valid ISO 8601"):
            validate_curation(self.curation, invalid_publication)

    def test_unverified_thehatman_dates_remain_note_only(self) -> None:
        bundle = self.bundles["activity--unattributed-thehatman-self-claim"]
        grouping = next(obj for obj in bundle["objects"] if obj["type"] == "grouping")
        self.assertIsNone(grouping["x_first_observed"]["value"])
        self.assertIsNone(grouping["x_last_observed"]["value"])
        self.assertFalse(any(obj["type"] in {"campaign", "incident"} for obj in bundle["objects"]))
        note = next(obj for obj in bundle["objects"] if obj["type"] == "note")
        self.assertIn("未検証", json.dumps(note["x_ledger_observation"], ensure_ascii=False))

    def test_collection_and_publication_dates_are_not_observations(self) -> None:
        bigbear = self.clusters["unknown-cluster--bigbear-2-0"]
        secflow = self.clusters["unknown-cluster--secflow-ai-operator"]
        ted = self.clusters["unknown-cluster--ted-curlrat"]
        self.assertIsNone(bigbear["observations"][0]["observed_on"])
        self.assertIn("収集日", bigbear["observations"][0]["observed_on_basis"])
        self.assertIsNone(secflow["observations"][0]["observed_on"])
        self.assertIn("収集日", secflow["observations"][0]["observed_on_basis"])
        self.assertEqual(ted["entity_type"], "grouping")
        self.assertEqual((ted["first_seen"], ted["last_seen"]), ("2025", "2026"))
        self.assertEqual(ted["tracking_detected_on"], "2026-09-08")
        self.assertIsNone(ted["observations"][0]["observed_on"])
        self.assertNotEqual(
            ted["observations"][0]["published_at"], ted["first_seen"]
        )

        ted_curation = next(
            item
            for item in self.curation["activities"]
            if item["ledger_cluster_id"] == "unknown-cluster--ted-curlrat"
        )
        self.assertEqual(ted_curation["first_observed"]["precision"], "year")
        self.assertEqual(ted_curation["last_observed"]["precision"], "year")
        self.assertEqual(
            ted_curation["first_observed"]["basis"], "source-relative-period"
        )
        self.assertNotEqual(
            ted_curation["first_observed"]["value"],
            f"{ted['observations'][0]['published_at']}T00:00:00Z",
        )

    def test_bigbear_exact_primary_table_counts(self) -> None:
        activity_id = "activity--unattributed-bigbear-2-0"
        bundle = self.bundles[activity_id]
        indicators = [obj for obj in bundle["objects"] if obj["type"] == "indicator"]
        self.assertEqual(len(indicators), 48)
        self.assertEqual(self.metadata[activity_id]["structured_ioc_indicator_count"], 48)
        self.assertEqual(
            self.metadata[activity_id]["structured_ioc_source_observation_count"], 48
        )
        self.assertEqual(len({obj["pattern"] for obj in indicators}), 48)

    def test_structured_iocs_have_direct_based_on_observables(self) -> None:
        supported_observable_types = {
            "domain-name",
            "file",
            "ipv4-addr",
            "url",
        }
        for activity_id in (
            "activity--unattributed-bigbear-2-0",
            "activity--unattributed-secflow-ai-agent-campaign",
        ):
            with self.subTest(activity_id=activity_id):
                bundle = self.bundles[activity_id]
                by_id = {obj["id"]: obj for obj in bundle["objects"]}
                indicators = [
                    obj for obj in bundle["objects"] if obj["type"] == "indicator"
                ]
                relationships = [
                    obj
                    for obj in bundle["objects"]
                    if obj.get("relationship_type") == "based-on"
                ]
                self.assertEqual(len(relationships), len(indicators))
                self.assertEqual(
                    self.metadata[activity_id][
                        "structured_ioc_observable_count"
                    ],
                    len(indicators),
                )
                self.assertEqual(
                    self.metadata[activity_id][
                        "structured_ioc_based_on_count"
                    ],
                    len(indicators),
                )
                for indicator in indicators:
                    matches = [
                        relation
                        for relation in relationships
                        if relation["source_ref"] == indicator["id"]
                    ]
                    self.assertEqual(len(matches), 1)
                    target = by_id[matches[0]["target_ref"]]
                    self.assertIn(target["type"], supported_observable_types)
                    self.assertTrue(indicator["labels"])
                    self.assertEqual(
                        target["x_opencti_labels"], indicator["labels"]
                    )
                    self.assertEqual(
                        target["x_ioc_roles"], indicator["x_ioc_roles"]
                    )
                    self.assertEqual(
                        matches[0]["x_ioc_roles"], indicator["x_ioc_roles"]
                    )
                    self.assertEqual(
                        matches[0]["x_ioc_role_source_refs"],
                        [indicator["x_source_id"]],
                    )
                    self.assertIn(
                        indicator["x_opencti_main_observable_type"],
                        {"Domain-Name", "IPv4-Addr", "StixFile", "Url"},
                    )

    def test_secflow_exact_values_and_wildcard_boundary(self) -> None:
        activity_id = "activity--unattributed-secflow-ai-agent-campaign"
        bundle = self.bundles[activity_id]
        indicators = [obj for obj in bundle["objects"] if obj["type"] == "indicator"]
        # 15 exact infrastructure rows become 13 unique atomic observables;
        # 25 unique SHA-256 values yield 38 unique Indicators. The wildcard
        # niestools.com family remains in the source Note and is not promoted.
        self.assertEqual(len(indicators), 38)
        self.assertEqual(
            sum(obj["x_source_scoped_observation_count"] for obj in indicators), 40
        )
        self.assertEqual(self.metadata[activity_id]["non_promoted_feature_count"], 1)
        self.assertFalse(any("*.niestools" in obj["pattern"] for obj in indicators))
        note_text = json.dumps(
            [obj for obj in bundle["objects"] if obj["type"] == "note"],
            ensure_ascii=False,
        )
        self.assertIn("*.niestools", note_text)

if __name__ == "__main__":
    unittest.main()
