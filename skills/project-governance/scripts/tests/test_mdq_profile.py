#!/usr/bin/env python3
"""Tests for the versioned shared Markdown query profile asset."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


SKILL_ROOT = Path(__file__).resolve().parents[2]
PROFILE_ROOT = SKILL_ROOT / "assets" / "mdq-profiles"
PROFILE = PROFILE_ROOT / "governed-document-v1.yaml"
PROFILE_REFERENCE = "project-governance/governed-document-v1"


class SharedMdqProfileTest(unittest.TestCase):
    def test_governed_document_profile_is_versioned_and_self_identifying(self) -> None:
        self.assertTrue(PROFILE.is_file())
        document = yaml.safe_load(PROFILE.read_text(encoding="utf-8"))
        self.assertEqual(document["x-profile-id"], PROFILE_REFERENCE)
        self.assertEqual(document["x-profile-version"], 1)
        self.assertEqual(document["version"], 1)
        self.assertEqual(document["records"]["boundary"]["levels"], [2])

    def test_profile_key_pattern_covers_standard_governance_headings(self) -> None:
        pattern = re.compile(document_pattern())
        for heading, identifier, title in (
            ("Q-001 — Open question", "Q-001", "Open question"),
            ("REQ-001: Requirement", "REQ-001", "Requirement"),
            ("PLAN-001 - Delivery plan", "PLAN-001", "Delivery plan"),
        ):
            match = pattern.fullmatch(heading)
            self.assertIsNotNone(match, heading)
            assert match is not None
            self.assertEqual(match.group("id"), identifier)
            self.assertEqual(match.group("title"), title)

    def test_profile_catalog_is_self_identifying_and_versioned(self) -> None:
        expected = {
            "governed-document-v1": 1,
            "defect-profile-v1": 1,
            "domain-profile-v2": 2,
            "marketing-profile-v2": 2,
            "evaluation-profile-v1": 1,
            "evaluation-profile-v2": 2,
        }
        for name, family_version in expected.items():
            path = PROFILE_ROOT / f"{name}.yaml"
            self.assertTrue(path.is_file(), name)
            document = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertEqual(
                document["x-profile-id"], f"project-governance/{name}"
            )
            self.assertEqual(document["x-profile-version"], family_version)
            self.assertIn(document["version"], (1, 2))
            self.assertIn("records", document)
            self.assertIn("fields", document)

    def test_named_query_families_use_mdq_v2(self) -> None:
        for name in (
            "defect-profile-v1",
            "domain-profile-v2",
            "marketing-profile-v2",
            "evaluation-profile-v2",
        ):
            document = yaml.safe_load(
                (PROFILE_ROOT / f"{name}.yaml").read_text(encoding="utf-8")
            )
            self.assertEqual(document["version"], 2, name)
            self.assertTrue(document.get("queries"), name)


def document_pattern() -> str:
    document = yaml.safe_load(PROFILE.read_text(encoding="utf-8"))
    return document["records"]["key"]["pattern"]


if __name__ == "__main__":
    unittest.main()
