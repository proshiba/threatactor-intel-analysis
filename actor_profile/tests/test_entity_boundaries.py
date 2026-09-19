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
        self.assertIn("spacecobra", slugs)
        self.assertIn("famous-chollima", slugs)

    def test_legacy_software_actor_profiles_are_deprecated(self) -> None:
        gravity = self.load_profile("gravityrat")
        shamoon = self.load_profile("shamoon")
        self.assertEqual(gravity["status"], "deprecated")
        self.assertEqual(shamoon["status"], "deprecated")
        self.assertEqual(gravity["activities"], [])
        self.assertEqual(shamoon["activities"], [])

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


if __name__ == "__main__":
    unittest.main()
