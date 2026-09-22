from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROFILE_DIR = ROOT / "profiles" / "teampcp"
OPENCTI_OSS_CAMPAIGN = (
    ROOT
    / "opencti"
    / "campaigns"
    / "teampcp"
    / "activity--teampcp-oss-supply-chain-2026.stix2.json"
)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class TeamPCPOligoIOCCompletenessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profile = load_json(PROFILE_DIR / "actor-profile.json")
        cls.iocs = load_json(PROFILE_DIR / "iocs.json")
        cls.manifest = load_json(PROFILE_DIR / "ioc-sources.json")
        cls.generated_stix = load_json(
            PROFILE_DIR / "generated" / "profile.stix2.json"
        )
        cls.opencti_oss_campaign = load_json(OPENCTI_OSS_CAMPAIGN)
        with (PROFILE_DIR / "artifacts.csv").open(
            newline="", encoding="utf-8"
        ) as stream:
            cls.artifacts = list(csv.DictReader(stream))

    def test_exact_oligo_observables_are_complete(self) -> None:
        indicators = {
            (item["type"], item["value"]): item
            for item in self.iocs["indicators"]
        }
        domains = {
            "masscan.cloud",
            "matrix.masscan.cloud",
            "natalstatus.org",
            "auth.masscan.cloud",
            "checkout.masscan.cloud",
            "pay.masscan.cloud",
            "mail.masscan.cloud",
            "test.masscan.cloud",
            "pcp.masscan.cloud",
            "scan.aquasecurity.org",
            "checkmarx.zone",
        }
        addresses = {
            "103.79.77.16",
            "104.164.55.217",
            "213.139.205.74",
            "67.217.57.240",
            "44.252.85.168",
            "103.127.134.124",
        }
        self.assertTrue(
            {("domain", value) for value in domains}.issubset(indicators)
        )
        self.assertTrue(
            {("ipv4", value) for value in addresses}.issubset(indicators)
        )
        self.assertIn(
            ("url", "https://matrix.masscan.cloud/ep9TS2/ndt.sh"),
            indicators,
        )
        self.assertEqual(len(indicators), 18)
        self.assertEqual(
            sum(item["observation_count"] for item in indicators.values()),
            28,
        )

    def test_wildcards_and_unproven_resolution_are_not_exact_iocs(self) -> None:
        values = {item["value"] for item in self.iocs["indicators"]}
        for wildcard in (
            "*.bank-phish.masscan.cloud",
            "*.test-phish.masscan.cloud",
            "*.zendesk.masscan.cloud",
        ):
            self.assertNotIn(wildcard, values)
            self.assertTrue(
                any(row["value"] == wildcard for row in self.artifacts)
            )
        self.assertFalse(any(value.startswith("*.") for value in values))
        self.assertNotIn("6.6.6.6", values)

    def test_observation_times_preserve_source_scope(self) -> None:
        indicators = {item["value"]: item for item in self.iocs["indicators"]}
        self.assertIsNone(
            indicators["scan.aquasecurity.org"]["first_observed"]["value"]
        )
        self.assertIsNone(
            indicators["checkmarx.zone"]["first_observed"]["value"]
        )
        for value in ("scan.aquasecurity.org", "checkmarx.zone"):
            observation = indicators[value]["observations"][0]
            self.assertIsNone(observation["observed_at"]["value"])
            self.assertIn(
                "certificate-transparency-first-seen-not-activity-time",
                observation["context_excerpt"],
            )
            self.assertEqual(
                observation["infrastructure_refs"],
                ["infra--teampcp-oss-staging-2026"],
            )
        for value in ("masscan.cloud", "matrix.masscan.cloud"):
            indicator = indicators[value]
            self.assertEqual(
                indicator["first_observed"]["value"],
                "2025-07-26T00:00:00Z",
            )
            ct_observation = next(
                item
                for item in indicator["observations"]
                if "certificate-transparency-first-seen-not-activity-time"
                in item["context_excerpt"]
            )
            self.assertIsNone(ct_observation["observed_at"]["value"])
            self.assertIn("2025-05-11", ct_observation["context_excerpt"])
        self.assertIsNone(
            indicators["natalstatus.org"]["first_observed"]["value"]
        )
        self.assertIsNone(
            indicators["213.139.205.74"]["first_observed"]["value"]
        )
        self.assertEqual(
            indicators["67.217.57.240"]["observation_count"], 6
        )
        address_103 = indicators["103.127.134.124"]["observations"]
        roles_by_date = {
            item["observed_at"]["value"]: set(item["roles"])
            for item in address_103
        }
        self.assertEqual(
            roles_by_date["2025-11-02T00:00:00Z"], {"account-management"}
        )
        self.assertEqual(roles_by_date["2025-11-16T00:00:00Z"], {"c2"})

        dates_by_artifact: dict[str, list[str]] = {}
        for row in self.artifacts:
            dates_by_artifact.setdefault(row["value"], []).append(
                row["observed_at"]
            )
        self.assertEqual(
            dates_by_artifact["/files/netsh"],
            [
                "2025-09-21T00:00:00Z",
                "2025-09-26T00:00:00Z",
                "2025-09-28T00:00:00Z",
            ],
        )
        self.assertEqual(
            dates_by_artifact["/files/keyen.sh"],
            ["2025-10-02T00:00:00Z"],
        )
        self.assertEqual(
            dates_by_artifact["/ep9TS2/ndt.sh"],
            ["2025-06-01T00:00:00Z", "2025-07-26T00:00:00Z"],
        )
        for value in ("ndt.sh", "nnt.sh", "is.sh", "rs.sh"):
            row = next(item for item in self.artifacts if item["value"] == value)
            self.assertEqual(row["artifact_type"], "file-name")
            self.assertEqual(row["observed_at"], "")
            self.assertEqual(row["infrastructure_refs"], '["infra--masscan-cloud"]')

    def test_infrastructure_scope_is_not_collapsed(self) -> None:
        infrastructure = {
            item["id"]: item
            for item in self.profile["capabilities"]["infrastructure"]
        }
        self.assertIn("infra--masscan-cloud", infrastructure)
        self.assertIn(
            "infra--teampcp-shadowray-ironern-control", infrastructure
        )
        self.assertIn("infra--teampcp-oss-staging-2026", infrastructure)

        indicators = {item["value"]: item for item in self.iocs["indicators"]}
        self.assertEqual(
            indicators["103.127.134.124"]["infrastructure_refs"],
            ["infra--teampcp-shadowray-ironern-control"],
        )
        for value in ("scan.aquasecurity.org", "checkmarx.zone"):
            self.assertEqual(
                indicators[value]["infrastructure_refs"],
                ["infra--teampcp-oss-staging-2026"],
            )

        oss_activity = next(
            item
            for item in self.profile["activities"]
            if item["activity_id"]
            == "activity--teampcp-oss-supply-chain-2026"
        )
        self.assertEqual(
            oss_activity["infrastructure_refs"],
            ["infra--teampcp-oss-staging-2026"],
        )
        self.assertIn("source--oligo-teampcp-2026", oss_activity["evidence_refs"])
        lineage = next(
            item
            for item in self.profile["activities"]
            if item["activity_id"]
            == "activity--teampcp-oligo-lineage-2020-2026"
        )
        self.assertEqual(
            set(lineage["infrastructure_refs"]),
            {
                "infra--masscan-cloud",
                "infra--teampcp-shadowray-ironern-control",
                "infra--teampcp-oss-staging-2026",
            },
        )

    def test_ct_record_ids_are_artifacts_and_a_non_digest_pivot(self) -> None:
        record_ids = {
            "18348750576",
            "18348751301",
            "18349037873",
            "18349038225",
        }
        ct_rows = [
            row
            for row in self.artifacts
            if row["value"].startswith("crt.sh certificate record ")
        ]
        self.assertEqual(
            {row["value"].rsplit(" ", 1)[-1] for row in ct_rows},
            record_ids,
        )
        self.assertTrue(all(not row["observed_at"] for row in ct_rows))
        self.assertTrue(
            all("not a certificate fingerprint" in row["context_excerpt"] for row in ct_rows)
        )
        self.assertFalse(
            any(
                item["type"] == "certificate-fingerprint"
                for item in self.iocs["indicators"]
            )
        )

        pivots = {
            item["pivot_id"]: item for item in self.profile["hunting_pivots"]
        }
        ct_pivot = pivots["hunting-pivot--teampcp-masscan-ct-records"]
        self.assertIsNone(ct_pivot["stix_pattern"])
        self.assertIn("issuer Let's Encrypt E6", ct_pivot["value"])
        self.assertIn("2025-05-11", ct_pivot["value"])
        self.assertIsNone(ct_pivot["first_observed"]["value"])
        self.assertEqual(ct_pivot["observation_count"], 4)
        self.assertFalse(ct_pivot["continuity"]["passive_scan_performed"])
        self.assertEqual(ct_pivot["continuity"]["active_status"], "unknown")

    def test_indicator_valid_from_fallback_is_not_time_correlation(self) -> None:
        def by_pattern(bundle, pattern):
            return next(
                item
                for item in bundle["objects"]
                if item.get("type") == "indicator"
                and item.get("pattern") == pattern
            )

        pattern = "[domain-name:value = 'scan.aquasecurity.org']"
        for bundle in (self.generated_stix, self.opencti_oss_campaign):
            indicator = by_pattern(bundle, pattern)
            self.assertEqual(
                indicator["valid_from"], self.profile["created_at"]
            )
            self.assertEqual(
                indicator["x_valid_from_basis"],
                "stix-required-created-fallback",
            )
            self.assertFalse(indicator["x_time_correlation_eligible"])
            self.assertIsNone(indicator["x_first_observed"]["value"])
            self.assertEqual(
                indicator["x_report_published_fallback"][0]["value"],
                "2026-08-05T00:00:00Z",
            )

        observed = by_pattern(
            self.generated_stix,
            "[domain-name:value = 'masscan.cloud']",
        )
        self.assertEqual(observed["x_valid_from_basis"], "first-observed")
        self.assertTrue(observed["x_time_correlation_eligible"])
        self.assertEqual(
            observed["x_first_observed"]["value"],
            "2025-07-26T00:00:00Z",
        )

    def test_hunt_pivots_reference_only_canonical_indicators(self) -> None:
        pivots = {
            item["pivot_id"]: item for item in self.profile["hunting_pivots"]
        }
        wildcard = pivots[
            "hunting-pivot--teampcp-masscan-wildcard-phishing"
        ]
        self.assertEqual(wildcard["indicator_refs"], [])
        self.assertIn("MATCHES", wildcard["stix_pattern"])
        self.assertEqual(wildcard["continuity"]["active_status"], "unknown")

        paths = pivots["hunting-pivot--teampcp-deployment-path-lineage"]
        self.assertEqual(paths["observation_count"], 6)
        self.assertEqual(paths["continuity"]["assessment"], "reused")
        indicator_ids = {
            item["indicator_id"] for item in self.iocs["indicators"]
        }
        for pivot in pivots.values():
            self.assertTrue(set(pivot["indicator_refs"]).issubset(indicator_ids))

    def test_manifest_reproduces_reviewed_split(self) -> None:
        source = self.manifest["sources"][0]
        self.assertEqual(source["source_id"], "source--oligo-teampcp-2026")
        self.assertEqual(
            source["path"],
            "actor_profile/evidence/teampcp-oligo-2026-08-05.csv",
        )
        self.assertEqual(source["field_map"]["observed_at"], "observed_at")
        self.assertIn("wildcard", source["analyst_notes"])
        self.assertIn("証明書fingerprintではない", source["analyst_notes"])
        self.assertIn("live passive scanは実施しておらず", self.profile["assessment"]["collection_notes"])


if __name__ == "__main__":
    unittest.main()
