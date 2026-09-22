from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class PrimarySourceCorrectionTests(unittest.TestCase):
    def load_profile(self, slug: str) -> dict:
        return json.loads(
            (ROOT / "profiles" / slug / "actor-profile.json").read_text(
                encoding="utf-8"
            )
        )

    def test_unc6384_activity_does_not_assert_silk_typhoon(self) -> None:
        profile = self.load_profile("mustang-panda")
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--daily-421f30dbc45ea8e51ecf"
        )
        self.assertIn("UNC6384", activity["name"])
        self.assertNotIn("Silk Typhoon", activity["name"])
        self.assertIn("source--gtig-unc6384-captive-portal-2025", activity["evidence_refs"])
        self.assertIn("Silk Typhoonとは記載していない", activity["description"])

    def test_fox_tempest_is_a_relationship_not_false_vanilla_activity(self) -> None:
        profile = self.load_profile("vanilla-tempest")
        activity_ids = {item["activity_id"] for item in profile["activities"]}
        self.assertNotIn("activity--daily-c535922b3c89d69acd5c", activity_ids)
        relationship = next(
            item
            for item in profile["relationships"]
            if item["target_actor"] == "Fox Tempest"
        )
        self.assertEqual(relationship["relationship_type"], "uses-service-of")
        self.assertIn("source--daily-1f90e973408c7fac0a86", relationship["evidence_refs"])

    def test_vanilla_identity_and_historical_malware_are_preserved(self) -> None:
        profile = self.load_profile("vanilla-tempest")
        aliases = {item["name"]: item for item in profile["actor"]["aliases"]}
        for name in ("DEV-0832", "VICE SPIDER", "Vice Society"):
            self.assertEqual(aliases[name]["scope"], "exact")
        historical = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--microsoft-dev0832-education-2022"
        )
        malware = {item["name"] for item in profile["capabilities"]["malware"]}
        self.assertTrue(
            {"BlackCat", "QuantumLocker", "Zeppelin", "RedAlert", "SystemBC", "PortStarter"}
            <= malware
        )
        self.assertEqual(len(historical["malware_refs"]), 6)
        for victim_ref in historical["victim_refs"]:
            victim = next(
                item for item in profile["victim_cases"]
                if item["victim_case_id"] == victim_ref
            )
            self.assertIn(historical["activity_id"], victim["activity_refs"])

    def test_ta444_has_primary_alias_boundary_and_malware(self) -> None:
        profile = self.load_profile("ta444")
        aliases = {item["name"]: item for item in profile["actor"]["aliases"]}
        self.assertEqual(aliases["BlueNoroff"]["scope"], "overlapping")
        relationship = next(
            item for item in profile["relationships"] if item["target_actor"] == "APT38"
        )
        self.assertEqual(relationship["relationship_type"], "overlaps-with")
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--daily-e034301964da7955795d"
        )
        self.assertEqual(activity["confidence"], "high")
        self.assertEqual(len(activity["malware_refs"]), 7)
        malware = {item["name"] for item in profile["capabilities"]["malware"]}
        self.assertTrue({"Telegram 2", "Root Troy V4", "XScreen", "CryptoBot"} <= malware)

    def test_false_daily_candidate_is_rejected(self) -> None:
        ledger = json.loads(
            (ROOT / "profiles" / "vanilla-tempest" / "daily-observations.json").read_text(
                encoding="utf-8"
            )
        )
        record = next(
            item
            for item in ledger["records"]
            if item["record_id"] == "daily-record--c535922b3c89d69acd5cd17a"
        )
        self.assertEqual(record["review_status"], "rejected")
        self.assertEqual(record["activity_claim"]["actor_role"], "service-customer")

    def test_apt37_multi_topic_article_is_limited_to_rokrat_activity(self) -> None:
        profile = self.load_profile("apt37")
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--daily-c093c6edea29f9fcc0ac"
        )
        self.assertIn("APT37", activity["name"])
        self.assertIn("RoKRAT", activity["description"])
        self.assertNotIn("FERRET", activity["name"] + activity["description"])
        self.assertEqual(activity["first_observed"]["value"], "2024-11-13T00:00:00Z")
        self.assertIn("malware--rokrat", activity["malware_refs"])
        self.assertIn("source--genians-apt37-k-messenger-2025", activity["evidence_refs"])

    def test_aws_supply_chain_activity_keeps_vendor_scope_and_dates(self) -> None:
        profile = self.load_profile("apt38")
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--daily-e7e43253a3ee354a7560"
        )
        self.assertIn("Sapphire Sleet", activity["name"])
        self.assertEqual(activity["confidence"], "medium")
        self.assertEqual(activity["first_observed"]["value"], "2025-03-01T00:00:00Z")
        self.assertEqual(activity["last_observed"]["value"], "2026-03-01T00:00:00Z")
        source = next(
            item
            for item in profile["sources"]
            if item["source_id"] == "source--daily-a7e2c22924a222a6eb0f"
        )
        self.assertEqual(source["published_at"]["value"], "2026-07-29T00:00:00Z")
        self.assertEqual(source["actor_scope"], "overlapping")

    def test_water_galura_operator_is_distinct_from_qilin_software(self) -> None:
        profile = self.load_profile("water-galura")
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--daily-e30bc3c3abfd77cddd94"
        )
        self.assertIn("Water Galuraが運営するQilin", activity["name"])
        self.assertIn("無条件な別名としては扱わない", activity["description"])
        self.assertIn("malware--qilin", activity["malware_refs"])
        aliases = {item["name"] for item in profile["actor"]["aliases"]}
        self.assertNotIn("Qilin", aliases)
        self.assertEqual(activity["last_observed"]["value"], "2025-05-01T00:00:00Z")

    def test_apt45_and_andariel_are_linked_as_cross_vendor_overlap(self) -> None:
        for source_slug, target in (("apt45", "Andariel"), ("andariel", "APT45")):
            profile = self.load_profile(source_slug)
            matches = [
                item
                for item in profile["relationships"]
                if item["target_actor"] == target
                and item["relationship_type"] == "overlaps-with"
            ]
            self.assertEqual(len(matches), 1)
            self.assertEqual(
                matches[0]["evidence_refs"], ["source--mandiant-apt45-2024"]
            )

    def test_unc5342_contagious_interview_boundary_is_preserved(self) -> None:
        for source_slug, target in (
            ("unc5342", "Contagious Interview"),
            ("contagious-interview", "UNC5342"),
        ):
            profile = self.load_profile(source_slug)
            matches = [
                item
                for item in profile["relationships"]
                if item["target_actor"] == target
                and item["relationship_type"] == "taxonomy-overlaps-with"
            ]
            self.assertEqual(len(matches), 1)
            self.assertEqual(
                matches[0]["evidence_refs"],
                ["source--gtig-unc5342-etherhiding-2025"],
            )

    def test_kimsuky_apt43_overlap_is_not_duplicated(self) -> None:
        profile = self.load_profile("kimsuky")
        matches = [
            item
            for item in profile["relationships"]
            if item["target_actor"] == "APT43"
            and item["relationship_type"] == "overlaps-with"
        ]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["confidence"], "high")

    def test_unc6040_is_separated_from_unc6240_extortion(self) -> None:
        profile = self.load_profile("unc6040")
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--daily-dcc1e326e606705f98d4"
        )
        self.assertTrue(activity["name"].startswith("UNC6040"))
        self.assertIn("UNC6240", activity["description"])
        self.assertNotIn("ShinyHunters(UNC6040)", activity["description"])
        self.assertEqual(
            activity["evidence_refs"],
            ["source--gtig-unc6040-salesforce-vishing-2025"],
        )
        relationship = next(
            item
            for item in profile["relationships"]
            if item["target_actor"] == "UNC6240"
        )
        self.assertEqual(relationship["relationship_type"], "related-to")

    def test_unc6671_keeps_separate_cluster_boundary(self) -> None:
        profile = self.load_profile("unc6671")
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--daily-0697f946d4469dc9883a"
        )
        self.assertTrue(activity["name"].startswith("UNC6671"))
        self.assertEqual(activity["first_observed"]["value"], "2026-01-01T00:00:00Z")
        self.assertIsNone(activity["last_observed"]["value"])
        self.assertEqual(
            activity["evidence_refs"],
            ["source--gtig-shinyhunters-saas-clusters-2026"],
        )
        relationships = {
            (item["target_actor"], item["relationship_type"])
            for item in profile["relationships"]
        }
        self.assertIn(("UNC6240", "taxonomy-overlaps-with"), relationships)
        self.assertIn(("UNC6661", "taxonomy-overlaps-with"), relationships)

    def test_unc2286_does_not_duplicate_salt_typhoon_activity(self) -> None:
        profile = self.load_profile("unc2286")
        self.assertNotIn(
            "activity--daily-2c3e99f982af03e6e5ab",
            {item["activity_id"] for item in profile["activities"]},
        )
        relationships = [
            item
            for item in profile["relationships"]
            if item["target_actor"] == "Salt Typhoon"
            and item["relationship_type"] == "taxonomy-overlaps-with"
        ]
        self.assertEqual(len(relationships), 1)
        self.assertEqual(relationships[0]["confidence"], "medium")

    def test_salt_typhoon_jumbledpath_activity_uses_cisco_primary(self) -> None:
        profile = self.load_profile("salt-typhoon")
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--daily-4e15138dd5323d6e8406"
        )
        self.assertEqual(activity["first_observed"]["status"], "unknown")
        self.assertEqual(activity["last_observed"]["status"], "unknown")
        self.assertEqual(activity["evidence_refs"], ["source--cisco-talos-salt-typhoon-jumbledpath-2025"])
        self.assertIn("JumbledPath", activity["description"])

    def test_unc2286_daily_candidate_is_rejected(self) -> None:
        ledger = json.loads(
            (ROOT / "profiles" / "unc2286" / "daily-observations.json").read_text(
                encoding="utf-8"
            )
        )
        record = next(
            item
            for item in ledger["records"]
            if item["record_id"] == "daily-record--2c3e99f982af03e6e5abbb47"
        )
        self.assertEqual(record["review_status"], "rejected")
        self.assertEqual(record["activity_claim"]["actor_role"], "taxonomy-reference")

    def test_ta406_konni_activity_uses_primary_and_preserves_overlap(self) -> None:
        for slug, activity_id, target, confidence in (
            ("ta406", "activity--daily-ed16c556a166870fdeb2", "Konni", "medium"),
            ("konni", "activity--daily-647f622408c58cbd428c", "TA406", "high"),
        ):
            profile = self.load_profile(slug)
            activity = next(
                item
                for item in profile["activities"]
                if item["activity_id"] == activity_id
            )
            self.assertTrue(activity["name"].startswith("KONNI"))
            self.assertEqual(
                activity["first_observed"]["value"], "2025-10-01T00:00:00Z"
            )
            self.assertEqual(activity["confidence"], confidence)
            self.assertIn(
                "source--checkpoint-konni-ai-backdoor-2026",
                activity["evidence_refs"],
            )
            relationship = next(
                item
                for item in profile["relationships"]
                if item["target_actor"] == target
            )
            self.assertEqual(relationship["relationship_type"], "overlaps-with")
            self.assertEqual(relationship["confidence"], "medium")

    def test_kimsuky_quishing_is_canonicalized_once_and_not_copied_to_apt43(self) -> None:
        apt43 = self.load_profile("apt43")
        self.assertNotIn(
            "activity--daily-47a3435a13311fff4bdb",
            {item["activity_id"] for item in apt43["activities"]},
        )
        kimsuky = self.load_profile("kimsuky")
        activity_ids = {item["activity_id"] for item in kimsuky["activities"]}
        self.assertIn("activity--kimsuky-quishing-2025", activity_ids)
        self.assertNotIn("activity--daily-7fba10858bc6d43d600f", activity_ids)
        canonical = next(
            item
            for item in kimsuky["activities"]
            if item["activity_id"] == "activity--kimsuky-quishing-2025"
        )
        self.assertEqual(
            canonical["evidence_refs"], ["source--fbi-kimsuky-quishing-2026"]
        )

    def test_quishing_daily_candidates_are_rejected(self) -> None:
        for slug, record_id in (
            ("apt43", "daily-record--47a3435a13311fff4bdba862"),
            ("kimsuky", "daily-record--7fba10858bc6d43d600f7b78"),
        ):
            ledger = json.loads(
                (ROOT / "profiles" / slug / "daily-observations.json").read_text(
                    encoding="utf-8"
                )
            )
            record = next(
                item for item in ledger["records"] if item["record_id"] == record_id
            )
            self.assertEqual(record["review_status"], "rejected")

    def test_clickfix_beavertail_is_not_copied_from_contagious_interview(self) -> None:
        rejected = (
            ("apt43", "activity--daily-ad2a0b8acf43d0efef90"),
            ("kimsuky", "activity--daily-f1c379b17bba17ff7692"),
        )
        for slug, activity_id in rejected:
            profile = self.load_profile(slug)
            self.assertNotIn(
                activity_id,
                {item["activity_id"] for item in profile["activities"]},
            )
        contagious = self.load_profile("contagious-interview")
        canonical = next(
            item
            for item in contagious["activities"]
            if item["activity_id"] == "activity--daily-ad821db17bd56b3397be"
        )
        self.assertEqual(
            set(canonical["malware_refs"]),
            {"malware--beavertail", "malware--invisibleferret"},
        )
        self.assertEqual(
            canonical["evidence_refs"],
            ["source--gitlab-contagious-interview-clickfix-2025"],
        )
        self.assertEqual(
            canonical["first_observed"]["value"], "2025-05-01T00:00:00Z"
        )

    def test_clickfix_multitopic_daily_candidates_are_rejected(self) -> None:
        for slug, record_id in (
            ("apt43", "daily-record--ad2a0b8acf43d0efef90675b"),
            ("kimsuky", "daily-record--f1c379b17bba17ff76922589"),
        ):
            ledger = json.loads(
                (ROOT / "profiles" / slug / "daily-observations.json").read_text(
                    encoding="utf-8"
                )
            )
            record = next(
                item for item in ledger["records"] if item["record_id"] == record_id
            )
            self.assertEqual(record["review_status"], "rejected")
            self.assertEqual(record["activity_claim"]["actor_role"], "separate-news-item")

    def test_meta_syrian_clusters_have_distinct_activity_ids(self) -> None:
        ids = set()
        victim_ids = set()
        for slug in ("apt-c-27", "apt-c-37"):
            profile = self.load_profile(slug)
            expected = f"activity--meta-{slug}-disruption-2021"
            activity = next(
                item for item in profile["activities"] if item["activity_id"] == expected
            )
            self.assertIn(profile["actor"]["canonical_name"], activity["name"])
            self.assertNotIn(
                "activity--meta-syria-disruption-2021",
                {item["activity_id"] for item in profile["activities"]},
            )
            ids.add(expected)
            victim_ids.update(activity["victim_refs"])
        self.assertEqual(len(ids), 2)
        self.assertEqual(len(victim_ids), 2)

    def test_scattered_spider_unconfirmed_victims_are_groupings(self) -> None:
        profile = self.load_profile("scattered-spider")
        activities = {item["activity_id"]: item for item in profile["activities"]}
        retail = activities["activity--daily-3614985905a497f6500b"]
        qantas = activities["activity--daily-bd819e551e72e0636426"]
        self.assertEqual(retail["stix_object_type"], "grouping")
        self.assertEqual(qantas["stix_object_type"], "grouping")
        self.assertIn("source--ncsc-uk-retail-incidents-2025", retail["evidence_refs"])
        self.assertIn("source--qantas-call-centre-incident-2025", qantas["evidence_refs"])
        self.assertNotIn(
            "activity--daily-a97d2692a7a3198fb7f6", activities
        )
        self.assertNotIn(
            "activity--daily-ed14eeec16626d49c2e3", activities
        )
        self.assertIn("帰属していない", qantas["description"])

    def test_react2shell_counts_are_not_assigned_to_unc5174(self) -> None:
        profile = self.load_profile("unc5174")
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--daily-cdb2b24b57d09645a48d"
        )
        self.assertEqual(activity["stix_object_type"], "grouping")
        self.assertEqual(activity["victim_refs"], [])
        self.assertEqual(
            set(activity["malware_refs"]),
            {"malware--snowlight", "malware--vshell"},
        )
        relationship = next(
            item
            for item in profile["relationships"]
            if item["target_actor"] == "CL-STA-1015"
        )
        self.assertEqual(relationship["relationship_type"], "taxonomy-overlaps-with")
        self.assertEqual(relationship["confidence"], "medium")

    def test_moonstone_sleet_keeps_diamond_sleet_distinct(self) -> None:
        profile = self.load_profile("moonstone-sleet")
        aliases = {item["name"]: item for item in profile["actor"]["aliases"]}
        self.assertEqual(aliases["Storm-1789"]["scope"], "exact")
        relationship = next(
            item
            for item in profile["relationships"]
            if item["target_actor"] == "Diamond Sleet"
        )
        self.assertEqual(relationship["relationship_type"], "overlaps-with")
        self.assertIn("distinct actor", relationship["analyst_notes"])
        malware = {item["name"] for item in profile["capabilities"]["malware"]}
        self.assertTrue({"FakePenny", "SplitLoader", "YouieLoad"} <= malware)

    def test_storm1849_has_primary_arcanedoor_and_firestarter_activity(self) -> None:
        profile = self.load_profile("storm-1849")
        aliases = {item["name"]: item for item in profile["actor"]["aliases"]}
        self.assertEqual(aliases["UAT4356"]["scope"], "exact")
        activities = {item["activity_id"]: item for item in profile["activities"]}
        firestarter = activities["activity--storm-1849--firestarter-2026"]
        self.assertEqual(firestarter["stix_object_type"], "campaign")
        self.assertEqual(firestarter["first_observed"]["status"], "unknown")
        self.assertEqual(
            firestarter["evidence_refs"],
            ["source--cisco-talos-uat4356-firestarter-2026"],
        )
        self.assertIn("malware--firestarter", firestarter["malware_refs"])

    def test_toolshell_actor_boundaries_remove_nNSA_conflation(self) -> None:
        storm = self.load_profile("storm-2603")
        storm_activities = {
            item["activity_id"]: item for item in storm["activities"]
        }
        self.assertNotIn("activity--daily-e8fd6208405a17b2c79d", storm_activities)
        self.assertNotIn("activity--daily-aacbe5410f1223b930a5", storm_activities)
        self.assertNotIn("activity--daily-b80b607914fb7f62f988", storm_activities)
        toolshell = storm_activities[
            "activity--storm-2603--toolshell-warlock-2025"
        ]
        self.assertEqual(toolshell["victim_refs"], [])
        self.assertEqual(
            set(toolshell["infrastructure_refs"]),
            {
                "infrastructure--storm-2603-post-exploitation-c2",
                "infrastructure--storm-2603-updatemicfosoft-c2",
            },
        )
        self.assertNotIn("NNSA", toolshell["description"])
        malware = {
            item["id"]: item for item in storm["capabilities"]["malware"]
        }
        lockbit = malware["malware--storm-2603-lockbit-ransomware"]
        self.assertEqual(lockbit["first_observed"]["status"], "unknown")
        self.assertNotIn(lockbit["id"], toolshell["malware_refs"])
        infrastructure = {
            item["id"]: item
            for item in storm["capabilities"]["infrastructure"]
        }
        self.assertIn(
            "update.updatemicfosoft.com",
            infrastructure["infrastructure--storm-2603-updatemicfosoft-c2"][
                "description"
            ],
        )
        source_ids = {item["source_id"] for item in storm["sources"]}
        self.assertFalse(
            {
                "source--daily-0e75e392e2685f601677",
                "source--daily-5c143f1d91377b49cfcc",
                "source--daily-c9fa26bbe8d21f50b441",
            }
            & source_ids
        )
        microsoft_source = next(
            item
            for item in storm["sources"]
            if item["source_id"] == "source--microsoft-toolshell-2025"
        )
        self.assertIn("hunting", microsoft_source["claims_supported"])
        self.assertIn("19 exact indicators", microsoft_source["analyst_notes"])
        pivots = {item["value"]: item for item in storm["hunting_pivots"]}
        self.assertIn("update.updatemicfosoft.com", pivots)
        ledger = json.loads(
            (
                ROOT
                / "profiles"
                / "storm-2603"
                / "daily-observations.json"
            ).read_text(encoding="utf-8")
        )
        superseded_records = {
            "daily-record--aacbe5410f1223b930a5ab56",
            "daily-record--b80b607914fb7f62f9889fd0",
            "daily-record--e8fd6208405a17b2c79dc068",
        }
        self.assertEqual(
            {
                item["record_id"]: item["review_status"]
                for item in ledger["records"]
                if item["record_id"] in superseded_records
            },
            {record_id: "rejected" for record_id in superseded_records},
        )
        self.assertIn("activity--storm-2603--parallel-intrusion-2026", storm_activities)
        zirconium = self.load_profile("zirconium")
        zirconium_ids = {item["activity_id"] for item in zirconium["activities"]}
        self.assertNotIn("activity--daily-f8164c2182ec1f2d8e79", zirconium_ids)

    def test_reviewed_campaigns_have_primary_source_dates(self) -> None:
        checks = (
            (
                "apt41",
                "activity--daily-207ba8f2eb504435e5e4",
                "source--mandiant-apt41-arisen-from-dust-2024",
                "2023-01-01T00:00:00Z",
            ),
            (
                "unc5820",
                "activity--daily-6531aa0646bd2b399aec",
                "source--mandiant-unc5820-fortimanager-2024",
                "2024-06-27T00:00:00Z",
            ),
            (
                "unc6395",
                "activity--daily-75ed648ec068d5993ef2",
                "source--gtig-unc6395-salesloft-drift-2025",
                "2025-03-22T00:00:00Z",
            ),
        )
        for slug, activity_id, source_id, first_observed in checks:
            profile = self.load_profile(slug)
            activity = next(
                item for item in profile["activities"] if item["activity_id"] == activity_id
            )
            self.assertIn(source_id, activity["evidence_refs"])
            self.assertEqual(activity["first_observed"]["value"], first_observed)


if __name__ == "__main__":
    unittest.main()
