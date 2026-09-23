from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from validate_profile import Issue, validate_actor_aliases  # noqa: E402


class ActorAliasValidationTests(unittest.TestCase):
    source_id = "source--example"

    def valid_alias(self) -> dict:
        return {
            "name": "Vendor Name",
            "vendor": "Example Vendor",
            "scope": "exact",
            "confidence": "high",
            "evidence_refs": [self.source_id],
            "analyst_notes": "The source identifies this as a rename.",
        }

    def validate(self, aliases: object, canonical_name: object = "Example Actor") -> list[Issue]:
        issues: list[Issue] = []
        validate_actor_aliases(
            {"canonical_name": canonical_name, "aliases": aliases},
            {self.source_id},
            issues,
        )
        return issues

    def assert_has_error(self, issues: list[Issue], message: str) -> None:
        self.assertTrue(
            any(item.severity == "error" and item.message == message for item in issues),
            [item.__dict__ for item in issues],
        )

    def test_schema_complete_alias_is_valid(self) -> None:
        self.assertEqual(self.validate([self.valid_alias()]), [])

    def test_required_fields_and_additional_properties_are_rejected(self) -> None:
        for field in self.valid_alias():
            with self.subTest(missing=field):
                alias = self.valid_alias()
                alias.pop(field)
                self.assert_has_error(
                    self.validate([alias]),
                    f"missing alias field: {field}",
                )

        alias = self.valid_alias()
        alias["source"] = "legacy-field"
        self.assert_has_error(
            self.validate([alias]),
            "unexpected alias field: source",
        )

    def test_field_types_scope_and_evidence_reference_schema_are_enforced(self) -> None:
        invalid_values = {
            "name": (7, "alias name must be a string"),
            "vendor": (7, "alias vendor must be a string"),
            "scope": (7, "alias scope must be a string"),
            "confidence": (7, "alias confidence must be a string"),
            "evidence_refs": (self.source_id, "alias evidence_refs must be an array"),
            "analyst_notes": (7, "alias analyst_notes must be a string"),
        }
        for field, (value, message) in invalid_values.items():
            with self.subTest(field=field):
                alias = self.valid_alias()
                alias[field] = value
                self.assert_has_error(self.validate([alias]), message)

        alias = self.valid_alias()
        alias["scope"] = "vendor"
        self.assert_has_error(self.validate([alias]), "invalid alias scope")

        alias = self.valid_alias()
        alias["name"] = "   "
        self.assert_has_error(
            self.validate([alias]),
            "alias name must not be empty",
        )

        alias = self.valid_alias()
        alias["evidence_refs"] = []
        self.assert_has_error(
            self.validate([alias]),
            "alias evidence_refs must not be empty",
        )

        alias = self.valid_alias()
        alias["evidence_refs"] = [7, "example", self.source_id, self.source_id]
        issues = self.validate([alias])
        for message in (
            "evidence reference must be a string",
            "evidence reference must start with source--",
            "duplicate evidence reference",
        ):
            self.assert_has_error(issues, message)

    def test_normalized_self_alias_and_duplicate_alias_are_rejected(self) -> None:
        self_alias = self.valid_alias()
        self_alias["name"] = "apt-41"
        first = self.valid_alias()
        first["name"] = "Royal APT"
        duplicate = copy.deepcopy(first)
        duplicate["name"] = "ＲＯＹＡＬ_apt!"

        issues = self.validate(
            [self_alias, first, duplicate],
            canonical_name="ＡＰＴ ４１",
        )
        self.assert_has_error(
            issues,
            "alias duplicates the canonical actor name after normalization",
        )
        self.assert_has_error(issues, "duplicate alias after normalization")


if __name__ == "__main__":
    unittest.main()
