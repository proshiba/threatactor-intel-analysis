import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from crosscheck_all_actors import ensure_progress_entry  # noqa: E402


class OsintProgressTests(unittest.TestCase):
    def test_new_actor_gets_default_progress_entry(self) -> None:
        tracker = {"actors": []}
        by_slug = {}
        progress = ensure_progress_entry(
            tracker, by_slug, slug="new-actor", name="New Actor"
        )
        self.assertEqual(progress["status"], "not_started")
        self.assertEqual(progress["queries"], [])
        self.assertEqual(progress["verified_sources"], [])
        self.assertIsNone(progress["last_searched_at"])
        self.assertIs(by_slug["new-actor"], progress)
        self.assertEqual(tracker["actors"], [progress])

    def test_existing_progress_is_preserved(self) -> None:
        existing = {
            "slug": "existing",
            "name": "Existing",
            "status": "integrated",
            "queries": ["q"],
        }
        tracker = {"actors": [existing]}
        by_slug = {"existing": existing}
        progress = ensure_progress_entry(
            tracker, by_slug, slug="existing", name="Replacement"
        )
        self.assertIs(progress, existing)
        self.assertEqual(progress["status"], "integrated")
        self.assertEqual(progress["name"], "Existing")


if __name__ == "__main__":
    unittest.main()
