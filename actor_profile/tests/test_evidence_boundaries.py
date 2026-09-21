from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WEAK_PREFIXES = (
    "source--actor-mapping-workbook",
    "source--osint-etda",
    "source--osint-misp",
    "source--target-audit-",
)
LEGACY_DIAMOND_FIELDS = (
    "adversary",
    "capability",
    "infrastructure",
    "victim",
    "socio_political",
)
class EvidenceBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profiles = {
            path.parent.name: json.loads(
                path.read_text(encoding="utf-8")
            )
            for path in sorted((ROOT / "profiles").glob("*/actor-profile.json"))
        }

    def test_aggregation_and_workbook_claims_are_not_canonical(self) -> None:
        def assert_no_weak_refs(value, location: str) -> None:
            if isinstance(value, dict):
                refs = value.get("evidence_refs", [])
                self.assertFalse(
                    any(ref.startswith(WEAK_PREFIXES) for ref in refs),
                    location,
                )
                for key, nested in value.items():
                    if key != "evidence_refs":
                        assert_no_weak_refs(nested, f"{location}.{key}")
            elif isinstance(value, list):
                for index, nested in enumerate(value):
                    assert_no_weak_refs(nested, f"{location}[{index}]")

        for slug, profile in self.profiles.items():
            assert_no_weak_refs(profile, slug)

    def test_legacy_top_level_diamond_prose_is_empty(self) -> None:
        for slug, profile in self.profiles.items():
            diamond = profile.get("diamond_model", {})
            for field in LEGACY_DIAMOND_FIELDS:
                self.assertEqual(diamond.get(field, ""), "", f"{slug}:{field}")

    def test_targeting_policy_text_matches_the_current_evidence_boundary(self) -> None:
        old_logic = "高確度でアクター照合できた構造化OSINTの被害地理フィールド"
        old_note = "OSINT集約値は中確度とし、ベンダー間のアクター集合境界差を保持する"
        current_logic = "external research leadに隔離する"
        current_note = "原典確認前にcanonicalへ昇格しない"
        generic_workbook_notes = (
            "Structured targets are extracted from workbook prose and require review.",
            "No structured target statement was available in the mapping workbook.",
        )
        for slug, profile in self.profiles.items():
            targets = profile.get("targets", {})
            selection_logic = targets.get("selection_logic", "")
            analyst_notes = targets.get("analyst_notes", "")
            self.assertNotIn(old_logic, selection_logic, slug)
            self.assertEqual(selection_logic.count(current_logic), 1, slug)
            self.assertNotIn(old_note, analyst_notes, slug)
            self.assertEqual(analyst_notes.count(current_note), 1, slug)
            for note in generic_workbook_notes:
                self.assertNotIn(note, analyst_notes, slug)

    def test_web_sources_have_explicit_scope_and_claim_metadata(self) -> None:
        for slug, profile in self.profiles.items():
            for source in profile.get("sources", []):
                value = source.get("url") or source.get("path", "")
                if not isinstance(value, str) or not value.startswith(("http://", "https://")):
                    continue
                self.assertIn("accessed_at", source, slug)
                self.assertIn("actor_scope", source, slug)
                self.assertIn("claims_supported", source, slug)
                self.assertIsInstance(source["claims_supported"], list, slug)

    def test_alias_scopes_are_reviewed(self) -> None:
        for slug, profile in self.profiles.items():
            for alias in profile.get("actor", {}).get("aliases", []):
                self.assertNotEqual(
                    alias.get("scope"),
                    "unknown",
                    f"{slug}:{alias.get('name')}",
                )

    def test_manual_research_lead_evidence_resolves(self) -> None:
        manual_path = ROOT / "actor_profile" / "manual-research-leads.json"
        manual = json.loads(manual_path.read_text(encoding="utf-8"))

        def refs_in(value):
            if isinstance(value, dict):
                yield from value.get("evidence_refs", [])
                for key, nested in value.items():
                    if key != "evidence_refs":
                        yield from refs_in(nested)
            elif isinstance(value, list):
                for nested in value:
                    yield from refs_in(nested)

        for slug, leads in manual.get("actors", {}).items():
            source_ids = {
                source["source_id"]
                for source in self.profiles[slug].get("sources", [])
            }
            self.assertFalse(set(refs_in(leads)) - source_ids, slug)

    def test_known_contradictions_and_relationship_cycles_are_removed(self) -> None:
        apt28 = self.profiles["apt28"]
        corrected = next(
            item
            for item in apt28.get("activities", [])
            if item["activity_id"] == "activity--daily-7f3a9417fcc5fd34f701"
        )
        self.assertIn("CVE-2026-21510", corrected["name"])
        self.assertNotIn("CVE-2026-32202", corrected["name"])
        self.assertIn("CVE-2026-32202", corrected["description"])
        self.assertIn("関連証拠を確認していない", corrected["description"])
        apt29 = self.profiles["apt29"]
        self.assertFalse(
            {
                "relationship--apt29-unc6293-subcluster",
                "relationship--apt29-unc7005-subcluster",
            }
            & {item["relationship_id"] for item in apt29.get("relationships", [])}
        )

    def test_part_of_relationship_graph_is_acyclic(self) -> None:
        profile_ids = {
            profile["profile_id"] for profile in self.profiles.values()
        }
        graph = {profile_id: set() for profile_id in profile_ids}
        for profile in self.profiles.values():
            for relationship in profile.get("relationships", []):
                target = relationship.get("target_actor")
                if (
                    relationship.get("relationship_type") == "part-of"
                    and target in profile_ids
                ):
                    graph[profile["profile_id"]].add(target)

        def visit(node, active, complete):
            self.assertNotIn(node, active, f"part-of cycle at {node}")
            if node in complete:
                return
            active.add(node)
            for target in graph[node]:
                visit(target, active, complete)
            active.remove(node)
            complete.add(node)

        complete = set()
        for profile_id in graph:
            visit(profile_id, set(), complete)

    def test_internal_dossier_relationship_targets_resolve(self) -> None:
        for slug in self.profiles:
            path = ROOT / "profiles" / slug / "generated" / "research-dossier.json"
            if not path.exists():
                continue
            dossier = json.loads(path.read_text(encoding="utf-8"))
            for relationship in dossier.get("canonical", {}).get(
                "relationships", []
            ):
                if str(relationship.get("target_actor", "")).startswith("actor--"):
                    self.assertIsNotNone(
                        relationship.get("target_actor_ref"),
                        f"{slug}:{relationship.get('relationship_id')}",
                    )

    def test_calypso_uses_actor_specific_primary_source(self) -> None:
        calypso = self.profiles["calypso"]
        self.assertNotIn("APT1", json.dumps(calypso["diamond_model"]))
        self.assertEqual(
            calypso["attribution"]["evidence_refs"],
            ["source--pwc-red-lamassu-jfmbackdoor-2026"],
        )
        malware = {item["name"] for item in calypso["capabilities"]["malware"]}
        self.assertEqual(malware, {"Showboat", "JFMBackdoor"})


if __name__ == "__main__":
    unittest.main()
