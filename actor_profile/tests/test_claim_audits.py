import json
import sys
import unittest
from collections import Counter
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from build_claim_audits import (  # noqa: E402
    actor_type_support,
    evidence_tier,
    microsoft_nation_state_match,
    verification_from_refs,
)


def profile(
    *,
    name: str = "Example",
    aliases: list[dict] | None = None,
    sponsor_type: str = "unknown",
    evidence_refs: list[str] | None = None,
) -> dict:
    return {
        "name": name,
        "actor": {
            "canonical_name": name,
            "aliases": aliases or [],
        },
        "attribution": {
            "sponsor_type": sponsor_type,
            "confidence": "medium",
            "evidence_refs": evidence_refs or [],
        },
        "motivations": [],
        "activities": [],
        "assessment": {"key_judgments": []},
    }


class ClaimAuditTests(unittest.TestCase):
    def test_evidence_tier_recognizes_source_families(self) -> None:
        sources = {
            "gov": {"source_type": "government-joint-advisory"},
            "vendor": {"source_type": "vendor-technical-report"},
            "official-mapping": {
                "source_type": "official-vendor-actor-mapping"
            },
            "aggregation": {"source_type": "structured-osint-aggregation"},
            "gov-encyclopedia": {
                "source_type": "government-threat-actor-encyclopedia",
                "publisher": "MITRE",
            },
        }
        self.assertEqual(evidence_tier(["gov"], sources), "authoritative")
        self.assertEqual(evidence_tier(["vendor"], sources), "research")
        self.assertEqual(
            evidence_tier(["official-mapping"], sources), "research"
        )
        self.assertEqual(evidence_tier(["aggregation"], sources), "aggregation")
        self.assertEqual(
            evidence_tier(["gov-encyclopedia"], sources), "aggregation"
        )
        self.assertEqual(
            evidence_tier(["aggregation", "vendor"], sources), "research"
        )

    def test_missing_evidence_is_unresolved(self) -> None:
        self.assertEqual(verification_from_refs([], {})[0], "unresolved")

    def test_microsoft_match_requires_exact_profile_identity(self) -> None:
        mapping = [
            {
                "Threat actor name": "Example Typhoon",
                "Origin/Threat": "China",
                "Other names": "Overlap Name",
            }
        ]
        overlapping = profile(
            aliases=[{"name": "Overlap Name", "scope": "overlapping"}]
        )
        exact = profile(aliases=[{"name": "Overlap Name", "scope": "exact"}])
        self.assertIsNone(microsoft_nation_state_match(overlapping, mapping))
        self.assertIsNotNone(microsoft_nation_state_match(exact, mapping))

    def test_microsoft_non_state_category_does_not_support_state_type(self) -> None:
        mapping = [
            {
                "Threat actor name": "Example",
                "Origin/Threat": "Financially motivated",
                "Other names": "",
            }
        ]
        self.assertIsNone(microsoft_nation_state_match(profile(), mapping))

    def test_state_aligned_evidence_only_partially_supports_state_sponsored(self) -> None:
        item = profile(sponsor_type="state-aligned", evidence_refs=["source--vendor"])
        sources = {
            "source--vendor": {"source_type": "vendor-threat-research"}
        }
        status, confidence, refs, rationale = actor_type_support(
            "state-sponsored", item, {}, sources, {}, []
        )
        self.assertEqual(status, "partially-supported")
        self.assertEqual(confidence, "medium")
        self.assertEqual(refs, ["source--vendor"])
        self.assertIn("state alignment", rationale)

    def test_country_label_alone_does_not_support_state_sponsored(self) -> None:
        item = profile()
        item["attribution"]["countries"] = ["Exampleland"]
        status, _, refs, _ = actor_type_support(
            "state-sponsored", item, {}, {}, {}, []
        )
        self.assertEqual(status, "unresolved")
        self.assertEqual(refs, [])


class ClaimAuditCollectionTests(unittest.TestCase):
    def test_claim_ids_are_unique_and_evidence_refs_resolve(self) -> None:
        root = Path(__file__).resolve().parents[2]
        claim_ids: list[str] = []
        for audit_path in (root / "profiles").glob("*/claim-audit.json"):
            profile = json.loads(
                (audit_path.parent / "actor-profile.json").read_text(encoding="utf-8")
            )
            source_ids = {item["source_id"] for item in profile.get("sources", [])}
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
            for item in audit["claims"]:
                claim_ids.append(item["claim_id"])
                self.assertFalse(
                    set(item.get("evidence_refs", [])) - source_ids,
                    f"unresolved evidence ref: {audit_path.parent.name}",
                )
        duplicates = {
            claim_id: count
            for claim_id, count in Counter(claim_ids).items()
            if count > 1
        }
        self.assertEqual(duplicates, {})


if __name__ == "__main__":
    unittest.main()
