import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class EntityBoundaryTests(unittest.TestCase):
    def load_profile(self, slug: str) -> dict:
        return json.loads(
            (ROOT / "profiles" / slug / "actor-profile.json").read_text(encoding="utf-8")
        )

    def test_software_names_are_not_active_actor_catalog_entries(self) -> None:
        catalog = json.loads(
            (ROOT / "actor_profile" / "corpus-catalog.json").read_text(encoding="utf-8")
        )
        slugs = {item["slug"] for item in catalog["actors"]}
        self.assertNotIn("gravityrat", slugs)
        self.assertNotIn("shamoon", slugs)
        self.assertNotIn("zebrocy", slugs)
        self.assertIn("spacecobra", slugs)
        self.assertIn("famous-chollima", slugs)

    def test_vendor_renames_do_not_create_duplicate_active_actors(self) -> None:
        catalog = json.loads(
            (ROOT / "actor_profile" / "corpus-catalog.json").read_text(
                encoding="utf-8"
            )
        )
        by_slug = {item["slug"]: item for item in catalog["actors"]}
        merges = {
            "peach-sandstorm": ("apt33", "Peach Sandstorm"),
            "raspberry-typhoon": ("lotus-blossom", "Raspberry Typhoon"),
            "sangria-tempest": ("fin7", "Sangria Tempest"),
            "violet-typhoon": ("zirconium", "Violet Typhoon"),
        }
        for duplicate, (canonical, alias) in merges.items():
            self.assertNotIn(duplicate, by_slug)
            self.assertIn(canonical, by_slug)
            self.assertIn(alias, by_slug[canonical].get("aliases", []))
            self.assertTrue(
                any(
                    "--merged--" in path
                    for path in by_slug[canonical].get("source_dirs", [])
                )
            )
        self.assertNotIn("APT30", by_slug["lotus-blossom"]["aliases"])

    def test_legacy_software_actor_profiles_are_deprecated(self) -> None:
        gravity = self.load_profile("gravityrat")
        shamoon = self.load_profile("shamoon")
        self.assertEqual(gravity["status"], "deprecated")
        self.assertEqual(shamoon["status"], "deprecated")
        self.assertEqual(gravity["activities"], [])
        self.assertEqual(shamoon["activities"], [])

        zebrocy = self.load_profile("zebrocy")
        self.assertEqual(zebrocy["status"], "deprecated")
        self.assertEqual(zebrocy["activities"], [])
        self.assertEqual(zebrocy["ttps"], [])

    def test_merged_legacy_profiles_are_deprecated_and_data_is_preserved(self) -> None:
        merges = {
            "peach-sandstorm": "apt33",
            "raspberry-typhoon": "lotus-blossom",
            "sangria-tempest": "fin7",
            "violet-typhoon": "zirconium",
        }
        for duplicate, canonical in merges.items():
            legacy = self.load_profile(duplicate)
            current = self.load_profile(canonical)
            self.assertEqual(legacy["status"], "deprecated")
            self.assertEqual(legacy["activities"], [])
            aliases = {
                item["name"]: item for item in current["actor"]["aliases"]
            }
            self.assertIn(legacy["actor"]["canonical_name"], aliases)
            self.assertEqual(
                aliases[legacy["actor"]["canonical_name"]]["scope"], "exact"
            )

        zirconium = self.load_profile("zirconium")
        activity_names = {item["name"] for item in zirconium["activities"]}
        self.assertIn(
            "新たな「BlueMoon」キットがWindowsとChromeのゼロデイ脆弱性を悪用",
            activity_names,
        )
        self.assertIn(
            "米国国家核安全保障局、Microsoft SharePoint攻撃で侵害",
            activity_names,
        )
        sector_names = {
            item["name"] for item in zirconium["targets"]["sectors"]
        }
        self.assertIn("非営利・市民社会", sector_names)
        victim_names = {item["name"] for item in zirconium["victim_cases"]}
        self.assertIn(
            "被害事例: 米国国家核安全保障局、Microsoft SharePoint攻撃で侵害",
            victim_names,
        )

    def test_deprecated_profiles_are_revoked_in_generated_stix(self) -> None:
        for directory in (ROOT / "profiles").iterdir():
            profile_path = directory / "actor-profile.json"
            stix_path = directory / "generated" / "profile.stix2.json"
            if not profile_path.is_file() or not stix_path.is_file():
                continue
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            if profile.get("status") != "deprecated":
                continue
            bundle = json.loads(stix_path.read_text(encoding="utf-8"))
            intrusion_sets = [
                item for item in bundle["objects"] if item["type"] == "intrusion-set"
            ]
            self.assertEqual(len(intrusion_sets), 1, directory.name)
            self.assertTrue(intrusion_sets[0].get("revoked"), directory.name)
            self.assertEqual(
                intrusion_sets[0].get("x_profile_status"),
                "deprecated",
                directory.name,
            )

    def test_deprecated_profiles_have_only_superseded_claims(self) -> None:
        for directory in (ROOT / "profiles").iterdir():
            profile_path = directory / "actor-profile.json"
            audit_path = directory / "claim-audit.json"
            if not profile_path.is_file():
                continue
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            if profile.get("status") != "deprecated":
                continue
            self.assertTrue(audit_path.is_file(), directory.name)
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
            self.assertEqual(audit["counts"], {"superseded": 1}, directory.name)
            self.assertEqual(len(audit["claims"]), 1, directory.name)
            self.assertEqual(
                audit["claims"][0]["verification_status"],
                "superseded",
                directory.name,
            )

    def test_active_relationships_do_not_target_deprecated_profiles(self) -> None:
        deprecated_names = set()
        for directory in (ROOT / "profiles").iterdir():
            profile_path = directory / "actor-profile.json"
            if not profile_path.is_file():
                continue
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            if profile.get("status") == "deprecated":
                deprecated_names.add(profile["actor"]["canonical_name"])

        catalog = json.loads(
            (ROOT / "actor_profile" / "corpus-catalog.json").read_text(
                encoding="utf-8"
            )
        )
        for actor in catalog["actors"]:
            profile = self.load_profile(actor["slug"])
            targets = {
                relationship["target_actor"]
                for relationship in profile.get("relationships", [])
            }
            self.assertFalse(targets & deprecated_names, actor["slug"])

    def test_spacecobra_uses_gravityrat_as_malware(self) -> None:
        profile = self.load_profile("spacecobra")
        self.assertEqual(profile["actor"]["canonical_name"], "SpaceCobra")
        self.assertIn(
            "GravityRAT",
            {item["name"] for item in profile["capabilities"]["malware"]},
        )

    def test_greenbug_volatile_kitten_and_calypso_aliases_are_scoped(self) -> None:
        greenbug = self.load_profile("greenbug")
        self.assertEqual(
            {item["name"] for item in greenbug["actor"]["aliases"]},
            {"Volatile Kitten"},
        )
        calypso = self.load_profile("calypso")
        names = {item["name"] for item in calypso["actor"]["aliases"]}
        self.assertEqual(names, {"Bronze Medley", "Red Lamassu"})
        self.assertNotIn("Comment Crew", names)
        self.assertNotIn("Mirage", names)
        self.assertNotIn("Pitty Tiger", names)

    def test_famous_chollima_is_not_exact_alias_of_broad_profiles(self) -> None:
        workers = self.load_profile("dprk-it-workers")
        interview = self.load_profile("contagious-interview")
        self.assertNotIn(
            "Famous Chollima",
            {item["name"] for item in workers["actor"]["aliases"]},
        )
        self.assertNotIn(
            "Famous Chollima",
            {item["name"] for item in interview["actor"]["aliases"]},
        )
        famous = self.load_profile("famous-chollima")
        targets = {item["target_actor"] for item in famous["relationships"]}
        self.assertIn("DPRK IT Worker Schemes", targets)
        self.assertIn("Contagious Interview", targets)

    def test_operation_names_and_normalized_duplicates_are_not_actor_aliases(self) -> None:
        fox_kitten = self.load_profile("fox-kitten")
        self.assertNotIn(
            "Pay2key",
            {item["name"] for item in fox_kitten["actor"]["aliases"]},
        )
        earth_berberoka_aliases = {
            item["name"]
            for item in self.load_profile("earth-berberoka")["actor"]["aliases"]
        }
        self.assertEqual(
            earth_berberoka_aliases,
            {"GamblingPuppet"},
        )
        ke3chang_aliases = {
            item["name"] for item in self.load_profile("ke3chang")["actor"]["aliases"]
        }
        self.assertIn("RoyalAPT", ke3chang_aliases)
        self.assertNotIn("Royal APT", ke3chang_aliases)


if __name__ == "__main__":
    unittest.main()
