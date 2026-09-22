from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class ToyBigBearSecFlowCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ledger = json.loads(
            (ROOT / "parse-daily/unknown-clusters.json").read_text(encoding="utf-8")
        )
        cls.clusters = {item["cluster_id"]: item for item in ledger["clusters"]}

    def test_bigbear_primary_ioc_table_has_all_48_source_scoped_values(self) -> None:
        cluster = self.clusters["unknown-cluster--bigbear-2-0"]
        observation = cluster["observations"][0]
        indicators = observation["indicators"]
        groups = (
            indicators["vps_nodes"],
            indicators["historical_vps_nodes"],
            indicators["phishing_domains"],
            indicators["historical_phishing_domains"],
        )
        self.assertEqual([len(group) for group in groups], [15, 10, 15, 8])
        values = [value for group in groups for value in group]
        self.assertEqual(len(values), 48)
        self.assertEqual(len(values), len(set(values)))
        self.assertIn("source-scoped", indicators["context"])
        self.assertIn("専有資産として扱わない", indicators["context"])
        self.assertEqual(cluster["first_seen"], "2026-06")
        self.assertEqual(cluster["last_seen"], "unknown")
        self.assertIn("461組織", observation["targets"])
        self.assertIn("258", observation["targets"])
        self.assertIn("母集団の異なる指標", observation["targets"])

    def test_secflow_primary_tables_are_complete_and_do_not_flag_provider_root(self) -> None:
        cluster = self.clusters["unknown-cluster--secflow-ai-operator"]
        observation = cluster["observations"][0]
        indicators = observation["indicators"]
        infrastructure = indicators["operator_and_support_infrastructure"]
        hashes = indicators["payload_sha256"]
        self.assertEqual(len(infrastructure), 16)
        self.assertEqual(len(hashes), 25)
        sha_values = [item.split(" ", 1)[0] for item in hashes]
        self.assertEqual(len(sha_values), len(set(sha_values)))
        self.assertTrue(all(re.fullmatch(r"[0-9a-f]{64}", value) for value in sha_values))
        self.assertEqual(
            sum("trycloudflare[.]com" in item for item in infrastructure), 3
        )
        self.assertFalse(any(item.startswith("*.trycloudflare") for item in infrastructure))
        self.assertIn("source-scoped", indicators["context"])
        self.assertEqual(cluster["first_seen"], "2026-05-15")
        self.assertEqual(cluster["last_seen"], "2026-08-04")
        self.assertIn("AttackCapture", cluster["time_basis"])
        self.assertEqual(cluster["attribution"]["state"], "unattributed")
        self.assertEqual(cluster["attribution"]["actor_type"], "unknown")
        self.assertIn("espionageを推定しない", cluster["attribution"]["notes"])

    def test_toy_ledger_is_merged_into_the_draft_profile(self) -> None:
        cluster = self.clusters["unknown-cluster--toy-ghouls"]
        self.assertEqual(cluster["status"], "merged")
        self.assertEqual(cluster["merged_into"], "toy-ghouls")
        self.assertEqual(cluster["merged_on"], "2026-09-22")
        self.assertEqual(cluster["last_seen"], "2026-07")
        self.assertIn("公開日", cluster["time_basis"])
        reviewed = {
            item["url"]: item for item in cluster["observations"]
        }
        for url in {
            "https://www.f6.ru/media-center/press-releases/bearlyfy-research/",
            "https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/",
            "https://securelist.com/toy-ghouls-new-hivemq-and-element-backdoors/121270/",
        }:
            self.assertIsNone(reviewed[url]["observed_on"])
            self.assertIn("公開日", reviewed[url]["observed_on_basis"])

        catalog = json.loads(
            (ROOT / "actor_profile/corpus-catalog.json").read_text(encoding="utf-8")
        )
        entries = [item for item in catalog["actors"] if item["slug"] == "toy-ghouls"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["profile_basis"], "analyst-curated-external-evidence")


if __name__ == "__main__":
    unittest.main()
