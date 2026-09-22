#!/usr/bin/env python3
"""Regression tests for observable classification and normalization."""

from __future__ import annotations

import sys
import tempfile
import unittest
import json
from collections import defaultdict
from itertools import groupby
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from common import normalize_observable, normalize_time, refang, stix_pattern  # noqa: E402
from bootstrap_all_profiles import (  # noqa: E402
    alias_source_metadata,
    derive_actor_types,
    derive_motivations,
    normalized_name,
)
from materialize_actor_census import (  # noqa: E402
    actor_types as census_actor_types,
    has_trusted_attack_reference,
    identity_curation_rule,
    normalized_unique_names,
)
from build_actor_census import add_identity, resolve_mention_identities  # noqa: E402
from build_attack_reference import active_object  # noqa: E402
from extract_mitre_relationships import relation_type  # noqa: E402
from ingest_observables import (  # noqa: E402
    NON_HASH_WORD_RE,
    analyst_marked_indicator,
    canonical_reference_sets,
    certificate_hash_algorithm,
    classified_record_values,
    classify_hash,
    coalesce_dataset_sources,
    extract_artifacts,
    extract_iocs,
    explicitly_excluded_ioc,
    filter_canonical_refs,
    looks_like_hash,
    time_from_record,
    validate_certificate_fingerprint,
)


class ActorCensusIdentityTests(unittest.TestCase):
    def test_distinct_attack_group_ids_do_not_merge_on_shared_alias(self) -> None:
        identities = {}
        alias_index = defaultdict(set)
        first = add_identity(
            identities,
            alias_index,
            name="Ember Bear",
            aliases=["UAC-0056"],
            mitre_id="G1003",
        )
        second = add_identity(
            identities,
            alias_index,
            name="Saint Bear",
            aliases=["UAC-0056"],
            mitre_id="G1031",
        )
        self.assertNotEqual(first, second)
        self.assertEqual(len(identities), 2)

    def test_ambiguous_workbook_row_does_not_create_or_merge_identity(self) -> None:
        identities = {}
        alias_index = defaultdict(set)
        add_identity(identities, alias_index, name="Windshift", mitre_id="G0112")
        add_identity(
            identities, alias_index, name="The White Company", mitre_id="G0089"
        )
        actor_id = add_identity(
            identities,
            alias_index,
            name="Broad workbook row",
            aliases=["Windshift", "The White Company"],
        )
        self.assertEqual(actor_id, "")
        self.assertEqual(len(identities), 2)

    def test_curated_identity_can_survive_ambiguous_aliases(self) -> None:
        identities = {}
        alias_index = defaultdict(set)
        add_identity(identities, alias_index, name="One", aliases=["Shared One"])
        add_identity(identities, alias_index, name="Two", aliases=["Shared Two"])
        actor_id = add_identity(
            identities,
            alias_index,
            name="Curated Three",
            aliases=["Shared One", "Shared Two"],
            preserve_on_ambiguous=True,
        )
        self.assertTrue(actor_id)
        self.assertEqual(len(identities), 3)

    def test_reference_only_official_attack_group_is_materializable(self) -> None:
        self.assertTrue(
            has_trusted_attack_reference(
                {
                    "reference_evidence": [
                        {
                            "source": "MITRE Enterprise ATT&CK 19.2",
                            "external_id": "G0076",
                        }
                    ]
                }
            )
        )
        self.assertFalse(
            has_trusted_attack_reference(
                {
                    "reference_evidence": [
                        {"source": "MISP threat-actor galaxy", "external_id": "x"}
                    ]
                }
            )
        )

    def test_short_official_attack_group_name_is_retained(self) -> None:
        identities = {}
        actor_id = add_identity(
            identities,
            defaultdict(set),
            name="RTM",
            mitre_id="G0048",
        )
        self.assertEqual(actor_id, "actor-census--mitre:G0048")
        self.assertEqual(identities[actor_id]["canonical_name"], "RTM")

    def test_canonical_name_wins_over_ambiguous_alias(self) -> None:
        identities = {
            "actor--canonical": {"canonical_name": "Thrip"},
            "actor--overlap": {"canonical_name": "Lotus Blossom"},
        }
        self.assertEqual(
            resolve_mention_identities(
                "Thrip", identities, identities
            ),
            {"actor--canonical"},
        )

    def test_ambiguous_noncanonical_alias_is_not_duplicated(self) -> None:
        identities = {
            "actor--one": {"canonical_name": "Saint Bear"},
            "actor--two": {"canonical_name": "Ember Bear"},
        }
        self.assertEqual(
            resolve_mention_identities(
                "UAC-0056", identities, identities
            ),
            set(),
        )


class AttackReferenceTests(unittest.TestCase):
    def test_deprecated_and_revoked_objects_are_not_active(self) -> None:
        self.assertFalse(active_object({"x_mitre_deprecated": True}))
        self.assertFalse(active_object({"revoked": True}))
        self.assertTrue(active_object({"revoked": False, "x_mitre_deprecated": False}))

    def test_explicit_distinct_cluster_language_is_not_generic_overlap(self) -> None:
        self.assertEqual(
            relation_type(
                "Analysis of behaviors, tools, and targeting indicates these are distinct clusters."
            ),
            ("distinct-from", "high", "supported"),
        )


class ObservableBoundaryTests(unittest.TestCase):
    def test_shared_source_identity_keeps_all_evidence_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "first.csv"
            second = root / "second.csv"
            known_publication = {
                "value": "2026-08-12T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-publication",
            }
            items = [
                {
                    "source_id": "source--shared",
                    "resolved_path": first,
                    "published_at": {
                        "value": None,
                        "precision": "unknown",
                        "status": "unknown",
                        "basis": "not-stated",
                    },
                    "confidence": None,
                    "tlp": "TLP:CLEAR",
                    "analyst_notes": "first note",
                    "field_map": {"value": "value"},
                },
                {
                    "source_id": "source--shared",
                    "resolved_path": second,
                    "published_at": known_publication,
                    "confidence": "high",
                    "tlp": "TLP:CLEAR",
                    "analyst_notes": "second note",
                    "field_map": {"value": "indicator"},
                },
            ]

            rows = coalesce_dataset_sources(items, root)

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["path"], "first.csv")
            self.assertEqual(
                rows[0]["evidence_paths"], ["first.csv", "second.csv"]
            )
            self.assertIn("first note", rows[0]["analyst_notes"])
            self.assertIn("second.csv", rows[0]["analyst_notes"])
            self.assertEqual(rows[0]["published_at"], known_publication)
            self.assertEqual(rows[0]["confidence"], "high")
            self.assertEqual(items[0]["confidence"], "high")
            self.assertEqual(items[0]["published_at"], known_publication)
            self.assertEqual(items[0]["field_map"], {"value": "value"})
            self.assertEqual(items[1]["field_map"], {"value": "indicator"})

    def test_distinct_manifest_sources_remain_distinct(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            items = [
                {
                    "source_id": "source--one",
                    "resolved_path": root / "one.csv",
                    "confidence": "medium",
                    "tlp": "TLP:CLEAR",
                },
                {
                    "source_id": "source--two",
                    "resolved_path": root / "two.csv",
                    "confidence": "high",
                    "tlp": "TLP:AMBER",
                },
            ]

            rows = coalesce_dataset_sources(items, root)

            self.assertEqual(
                [item["source_id"] for item in rows],
                ["source--one", "source--two"],
            )
            self.assertTrue(
                all("evidence_paths" not in item for item in rows)
            )

    def test_shared_source_semantic_conflict_fails_before_ingest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            items = [
                {
                    "source_id": "source--shared",
                    "resolved_path": root / "one.csv",
                    "confidence": "high",
                    "tlp": "TLP:CLEAR",
                },
                {
                    "source_id": "source--shared",
                    "resolved_path": root / "two.csv",
                    "confidence": "low",
                    "tlp": "TLP:CLEAR",
                },
            ]

            with self.assertRaisesRegex(ValueError, "conflicting confidence"):
                coalesce_dataset_sources(items, root)

    def test_certificate_fingerprint_algorithm_controls_x509_pattern(self) -> None:
        cases = {
            "md5": ("MD5", "aa" * 16),
            "sha1": ("SHA-1", "aa" * 20),
            "sha256": ("SHA-256", "aa" * 32),
            "sha512": ("SHA-512", "aa" * 64),
        }
        for algorithm, (stix_name, value) in cases.items():
            with self.subTest(algorithm=algorithm):
                self.assertEqual(
                    stix_pattern("certificate-fingerprint", value, algorithm),
                    f"[x509-certificate:hashes.'{stix_name}' = '{value}']",
                )
                validate_certificate_fingerprint(
                    "certificate-fingerprint", value, algorithm
                )

    def test_structured_certificate_hash_algorithm_is_normalized(self) -> None:
        record = {
            "fields": {"digest_algorithm": "SHA-1"},
        }
        metadata = {"field_map": {"hash_algorithm": "digest_algorithm"}}
        self.assertEqual(
            certificate_hash_algorithm(
                record, metadata, "certificate-fingerprint"
            ),
            "sha1",
        )
        self.assertIsNone(certificate_hash_algorithm(record, metadata, "sha1"))

    def test_unsupported_certificate_hash_algorithm_is_rejected(self) -> None:
        record = {"fields": {"digest_algorithm": "SHA-3"}}
        metadata = {"field_map": {"hash_algorithm": "digest_algorithm"}}
        with self.assertRaisesRegex(ValueError, "Unsupported certificate"):
            certificate_hash_algorithm(
                record, metadata, "certificate-fingerprint"
            )

    def test_certificate_algorithm_length_mismatch_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "requires 40 hex characters"):
            validate_certificate_fingerprint(
                "certificate-fingerprint", "aa" * 32, "sha1"
            )

    def test_reviewed_source_can_exclude_a_misclassified_hash(self) -> None:
        metadata = {
            "excluded_iocs": [
                {
                    "type": "sha1",
                    "value": "DE:E2:B1:E9",
                    "reason": "Reviewed as a certificate thumbprint.",
                }
            ]
        }
        self.assertTrue(
            explicitly_excluded_ioc(metadata, "sha1", "dee2b1e9")
        )
        self.assertFalse(
            explicitly_excluded_ioc(
                metadata, "certificate-fingerprint", "dee2b1e9"
            )
        )

    def test_observable_links_only_reference_canonical_entities(self) -> None:
        profile = {
            "activities": [{"activity_id": "activity--kept"}],
            "capabilities": {
                "malware": [{"id": "malware--kept"}],
                "infrastructure": [{"id": "infra--kept"}],
            },
        }
        related = {
            "campaign_refs": ["activity--kept", "activity--lead-only"],
            "malware_refs": ["malware--kept", "malware--lead-only"],
            "infrastructure_refs": ["infra--kept", "infra--lead-only"],
            "roles": ["c2"],
        }

        filtered = filter_canonical_refs(
            related, canonical_reference_sets(profile)
        )

        self.assertEqual(filtered["campaign_refs"], ["activity--kept"])
        self.assertEqual(filtered["malware_refs"], ["malware--kept"])
        self.assertEqual(filtered["infrastructure_refs"], ["infra--kept"])
        self.assertEqual(filtered["roles"], ["c2"])

    def test_ioc_types_are_kept_out_of_artifacts(self) -> None:
        # 192.0.2.0/24 などのドキュメント用レンジは伏字であって指標ではないため、
        # ここでは実際に到達し得るアドレスを使う。
        text = (
            "IOC: hxxps://c2[.]evil-actor.net/path, 45.61.136.56, "
            "44d88612fea8a8f36de82e1278abb02f"
        )
        iocs = extract_iocs(
            text, allow_plain_domains=True, explicit_structured=False
        )
        self.assertIn(("ipv4", "45.61.136.56", "confirmed"), iocs)
        self.assertTrue(any(kind == "url" for kind, _, _ in iocs))
        self.assertTrue(any(kind == "md5" for kind, _, _ in iocs))
        self.assertFalse(extract_artifacts(text, explicit_structured=False))

    def test_non_ioc_artifacts_are_classified(self) -> None:
        text = (
            r"powershell.exe -enc AAA; C:\ProgramData\stage.dll; "
            r"HKCU\SOFTWARE\Example\Run"
        )
        kinds = {
            kind for kind, _, _ in extract_artifacts(text, explicit_structured=True)
        }
        self.assertIn("command", kinds)
        self.assertIn("file-path", kinds)
        self.assertIn("registry-key", kinds)

    def test_explicit_artifact_type_prevents_uuid_hash_misclassification(self) -> None:
        value = "A8215357-F99A-44FE-BC65-D8F0434B0C03"
        record = {
            "text": f"artifact\t{value}\tmutex",
            "location": {"row": 2},
            "fields": {
                "type": "artifact",
                "value": value,
                "artifact_type": "mutex",
            },
            "method": "csv-row",
        }
        metadata = {
            "field_map": {
                "type": "type",
                "value": "value",
                "artifact_type": "artifact_type",
            }
        }
        iocs, artifacts = classified_record_values(record, metadata)
        self.assertEqual(iocs, [])
        self.assertEqual(artifacts, [("mutex", value, "confirmed")])

    def test_file_names_are_not_domains(self) -> None:
        values = extract_iocs(
            "IOC table: loader.exe report.pdf c2.example-actor.org",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {normalize_observable(kind, value) for kind, value, _ in values}
        self.assertEqual(domains, {"c2.example-actor.org"})

    def test_repository_instruction_file_is_not_a_domain(self) -> None:
        values = extract_iocs(
            "IOC review follows AGENT.md; actual C2 is malicious-c2.com",
            allow_plain_domains=False,
            explicit_structured=False,
        )
        domains = {value for kind, value, _ in values if kind == "domain"}
        self.assertEqual(domains, {"malicious-c2.com"})

    def test_evidence_map_provenance_is_not_an_actor_artifact(self) -> None:
        record = {
            "text": (
                "APT Groups and Operations.xlsx row 85 Calypso "
                "malware was 1.bat https://example.org/report.pdf"
            ),
            "location": {"row": 2},
            "fields": {
                "original_source_path": "APT Groups and Operations.xlsx",
                "original_source_location": '{"row": 85}',
                "matched_name": "Calypso",
                "context_excerpt": "malware was 1.bat https://example.org/report.pdf",
            },
            "method": "csv-row",
        }
        _, artifacts = classified_record_values(record, {})
        self.assertEqual(artifacts, [("file-name", "1.bat", "candidate")])

    def test_non_tld_file_names_are_not_domains(self) -> None:
        """実在しないTLDを持つ値はファイル名や文の断片であり domain にしない。"""
        values = extract_iocs(
            "IOC: files readme.txt config.json index.html dbconn.asp "
            "safe.headquartered plus c2.example-actor.org",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {value for kind, value, _ in values if kind == "domain"}
        self.assertEqual(domains, {"c2.example-actor.org"})

    def test_com_domains_are_not_rejected_as_executables(self) -> None:
        """.comはCOM実行ファイルの拡張子でもあるが、TLDとして実在するため落とさない。"""
        values = extract_iocs(
            "IOC: c2 is malicious-c2.com",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {value for kind, value, _ in values if kind == "domain"}
        self.assertIn("malicious-c2.com", domains)

    def test_special_use_tlds_are_kept(self) -> None:
        """.onion は委任TLDではないが指標として正当。"""
        values = extract_iocs(
            "IOC: hidden service at fckilfkscwusoopguhi7i6yg3l6tknaz7lrumvlhg5mvtxzxbbxlimid.onion",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {value for kind, value, _ in values if kind == "domain"}
        self.assertEqual(len(domains), 1)
        self.assertTrue(next(iter(domains)).endswith(".onion"))

    def test_truncated_url_hosts_are_dropped(self) -> None:
        """https://www/ のように抽出途中で切れたURLはIOCにしない。"""
        values = extract_iocs(
            "IOC: see https://www/ and https://unit42/ but c2 was https://evil-c2.net/gate",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        urls = {value for kind, value, _ in values if kind == "url"}
        self.assertEqual(urls, {"https://evil-c2.net/gate"})

    def test_ocr_concatenated_emails_are_dropped(self) -> None:
        """PDF抽出で本文が連結されたメール値をIOCにしない。"""
        values = extract_iocs(
            "IOC: zeg888@gmail[.]comisnamed; valid zeg888@gmail[.]com",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        emails = {normalize_observable(kind, value) for kind, value, _ in values if kind == "email"}
        self.assertEqual(emails, {"zeg888@gmail.com"})

    def test_www_plus_public_suffix_fragments_are_dropped(self) -> None:
        """www[.]ru のような登録可能名を含まないOCR断片をIOCにしない。"""
        values = extract_iocs(
            "IOC: www[.]ru www[.]gmail www[.]malicious-c2.com",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {normalize_observable(kind, value) for kind, value, _ in values if kind == "domain"}
        self.assertEqual(domains, {"malicious-c2.com"})


class HashClassificationTests(unittest.TestCase):
    """長さがハッシュと一致するだけの16進列を取り込まないこと。"""

    REAL_HASHES = {
        "md5": "44d88612fea8a8f36de82e1278abb02f",
        "sha1": "3395856ce81f2b7382dee72602f798b642f14140",
        "sha256": (
            "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
        ),
        # sha512("abc")。実在の値を使い、統計判定が本物を弾かないことを確かめる。
        "sha512": (
            "ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a"
            "2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f"
        ),
    }

    # 依頼文の実例。復号すると正体が分かるものだけを並べている。
    NON_HASHES = {
        "PEのDOSスタブ": "2072756e20696e20444f53206d6f6465",
        "PowerShellの断片": "203d204765742d4368696c644974656d",
        "User-Agentの断片": "3935312e3534205361666172692f3533372e3336",
        "シェルコード": "6a04680020000068000040006a00ffd5",
        ".NET IL": (
            "0228030000067d120000040202fe0623000006735b00000a14208813000015"
            "735c00000a7d130000040202fe0624000006735b00000a14208813000015735c00"
        ),
        "ゼロ埋め": "11200000000000000000000000000000",
        "4バイトの繰り返し": "0412da510412da510412da511f8f4451",
        # 3バイトの並びの条件でしか弾けない2件。この条件を外すと両方通る。
        "RLOによるファイル名偽装": "e280ade280aee280aee280ae6664702e",
        "x86機械語": (
            "c744243c256c6f63508d442440c7442444616c617050b9bd881775c744244c"
            "70646174c744245061255c6cc74424546f675f67c74424586f6c6432c744245c2e"
        ),
    }

    def test_real_hashes_of_every_length_are_classified(self) -> None:
        for kind, value in self.REAL_HASHES.items():
            with self.subTest(kind=kind):
                self.assertEqual(classify_hash(value), (kind, value))

    def test_uppercase_hashes_are_normalized(self) -> None:
        value = self.REAL_HASHES["md5"]
        self.assertEqual(classify_hash(value.upper()), ("md5", value))

    def test_hex_encoded_content_is_not_a_hash(self) -> None:
        for label, value in self.NON_HASHES.items():
            with self.subTest(label=label):
                self.assertIsNone(classify_hash(value))

    def test_trigram_repetition_alone_catches_machine_code(self) -> None:
        """3バイトの並びの条件を落とさないための番人。

        x86の``c74424XX``とRLOの制御文字は、ゼロ埋めでも同一バイトの連続でも
        可読文字列でもないため、この条件を外すと他のどれにも掛からない。
        """
        for label in ("x86機械語", "RLOによるファイル名偽装"):
            compact = self.NON_HASHES[label]
            raw = bytes.fromhex(compact)
            longest = max(len(list(group)) for _, group in groupby(raw))
            with self.subTest(label=label):
                self.assertLess(raw.count(0) / len(raw), 0.20)
                self.assertLess(longest, 4)
                self.assertIsNone(NON_HASH_WORD_RE.search(raw))
                self.assertFalse(looks_like_hash(compact))

    def test_non_hash_hex_is_not_extracted_as_an_ioc(self) -> None:
        text = (
            "The stub contains 2072756e20696e20444f53206d6f6465 and the sample "
            "hash is 44d88612fea8a8f36de82e1278abb02f."
        )
        values = extract_iocs(
            text, allow_plain_domains=True, explicit_structured=True
        )
        hashes = {value for kind, value, _ in values if kind == "md5"}
        self.assertEqual(hashes, {"44d88612fea8a8f36de82e1278abb02f"})


class AnalystMarkedIndicatorTests(unittest.TestCase):
    """保存済みIndicatorへのRULES.md 8.0例外の適用判定。

    攻撃者が正規サービス(raw.githubusercontent.com等)をペイロード置き場に使う場合、
    構造化IOC表由来の観測を持つIndicatorは参考ホスト判定から除外される。
    """

    def test_structured_csv_observation_is_analyst_marked(self) -> None:
        indicator = {"observations": [{"extraction_method": "tech-memo-structured-csv"}]}
        self.assertTrue(analyst_marked_indicator(indicator))

    def test_defanged_raw_value_is_analyst_marked(self) -> None:
        indicator = {
            "observations": [
                {"extraction_method": "pdf-text", "raw_value": "hxxps://evil[.]example"}
            ]
        }
        self.assertTrue(analyst_marked_indicator(indicator))

    def test_plain_document_extraction_is_not_analyst_marked(self) -> None:
        indicator = {
            "observations": [
                {"extraction_method": "pdf-text", "raw_value": "https://securelist.com/x/"}
            ]
        }
        self.assertFalse(analyst_marked_indicator(indicator))


class ReferenceHostTests(unittest.TestCase):
    """出典レポート自身の参考リンクを IOC として取り込まないこと。"""

    def test_citation_urls_are_not_iocs(self) -> None:
        text = (
            "IOC report. See https://securelist.com/some-analysis/12345/ and "
            "https://www.microsoft.com/security/blog/post for background. "
            "The C2 was https://evil-c2.net/gate.php"
        )
        urls = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "url"
        }
        self.assertEqual(urls, {"https://evil-c2.net/gate.php"})

    def test_citation_subdomains_are_not_iocs(self) -> None:
        text = "IOC: https://blog.securelist.com/x and https://unit42.paloaltonetworks.com/y"
        urls = [
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "url"
        ]
        self.assertEqual(urls, [])

    def test_bare_reference_domains_are_not_iocs(self) -> None:
        text = "IOC list: securelist.com attack.mitre.org bad-domain.net"
        domains = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "domain"
        }
        self.assertEqual(domains, {"bad-domain.net"})

    def test_defanged_reference_host_is_kept(self) -> None:
        """難読化はアナリストが悪性と判断した印なので、参考ホストでも残す。"""
        text = "IOC: attacker abused hxxps://github[.]com/evil/repo for payload delivery"
        urls = [
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "url"
        ]
        self.assertEqual(len(urls), 1)
        self.assertEqual(refang(urls[0]), "https://github.com/evil/repo")

    def test_vendor_contact_emails_are_not_iocs(self) -> None:
        text = "IOC: contact ti_support@qianxin.com or phish@bad-domain.net"
        emails = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "email"
        }
        self.assertEqual(emails, {"phish@bad-domain.net"})

    def test_bare_public_suffix_is_not_a_domain(self) -> None:
        """co.kr や ddns.net 単体は指標にならないが、サブドメインは残す。"""
        text = "IOC list: co.kr ddns.net mfahost.ddns.net"
        domains = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "domain"
        }
        self.assertEqual(domains, {"mfahost.ddns.net"})

    def test_non_routable_and_resolver_ips_are_not_iocs(self) -> None:
        text = "IOC: 127.0.0.1 10.1.2.3 192.168.1.1 8.8.8.8 203.0.113.10 45.61.136.56"
        ips = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "ipv4"
        }
        self.assertEqual(ips, {"45.61.136.56"})

    def test_structured_source_reference_host_is_kept(self) -> None:
        """構造化IOC表からの取り込みはアナリストが指標として並べたものとみなす。"""
        text = "https://github.com/evil/repo"
        urls = [
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=False, explicit_structured=True)
            if kind == "url"
        ]
        self.assertEqual(urls, ["https://github.com/evil/repo"])


class RefangTests(unittest.TestCase):
    def test_bracketed_scheme_leaves_no_residue(self) -> None:
        """[:] を先に解決しないと hxxp が残る(旧実装の不具合)。"""
        self.assertEqual(refang("hxxps[:]//evil-actor.net/a"), "https://evil-actor.net/a")
        self.assertEqual(refang("hxxp[:]//evil-actor.net"), "http://evil-actor.net")

    def test_scheme_is_case_insensitive(self) -> None:
        self.assertEqual(refang("HXXPS://Evil.example"), "https://Evil.example")
        self.assertEqual(refang("hXXps://Evil.example"), "https://Evil.example")

    def test_bracketed_at_and_dot_words(self) -> None:
        self.assertEqual(refang("user[@]evil.example"), "user@evil.example")
        self.assertEqual(refang("evil[dot]example"), "evil.example")
        self.assertEqual(refang("user[at]evil[dot]example"), "user@evil.example")


class TimeTests(unittest.TestCase):
    def test_invalid_calendar_date_becomes_unknown(self) -> None:
        point = normalize_time("2020-46", basis="same-record")
        self.assertEqual(point["status"], "unknown")
        self.assertIsNone(point["value"])
        self.assertEqual(point["basis"], "invalid-calendar-date:same-record")

    def test_blank_mapped_observed_at_does_not_scrape_campaign_year(self) -> None:
        record = {
            "text": (
                "hepog.org,domain,activity--goffee-q2-container-campaign-2026,"
                "source--kaspersky-goffee-q2-2026,"
            ),
            "fields": {
                "value": "hepog.org",
                "observed_at": "",
                "campaign_refs": "activity--goffee-q2-container-campaign-2026",
            },
        }
        point = time_from_record(
            record,
            {
                "field_map": {"observed_at": "observed_at"},
            },
        )
        self.assertEqual(point["status"], "unknown")
        self.assertIsNone(point["value"])


class GenerationGuardrailTests(unittest.TestCase):
    def test_country_origin_does_not_imply_state_sponsorship(self) -> None:
        self.assertEqual(census_actor_types(["Russia"]), ["threat-cluster"])
        self.assertEqual(census_actor_types(["China"]), ["threat-cluster"])
    def test_identity_curation_rule_uses_normalized_name(self) -> None:
        curation = {
            "identities": {
                "whitecompany": {"action": "merge", "target_slug": "white-company"},
                "revil": {"action": "exclude"},
            }
        }
        self.assertEqual(
            identity_curation_rule(curation, "The White Company").get("action"),
            None,
        )
        self.assertEqual(
            identity_curation_rule(curation, "White Company")["target_slug"],
            "white-company",
        )
        self.assertEqual(identity_curation_rule(curation, "REvil")["action"], "exclude")

    def test_census_aliases_are_deduplicated_after_normalization(self) -> None:
        self.assertEqual(
            normalized_unique_names(
                ["DNSCALC", "DNSCalc", "RoyalAPT", "Royal APT", "GREF"]
            ),
            ["DNSCALC", "RoyalAPT", "GREF"],
        )

    def test_catalog_alias_does_not_inherit_mitre_evidence(self) -> None:
        group = {"aliases": ["Hecamede"]}
        self.assertEqual(
            alias_source_metadata(
                "Hecamede", group, "source--mitre", "source--workbook"
            ),
            ("MITRE ATT&CK", "high", "source--mitre"),
        )
        self.assertEqual(
            alias_source_metadata(
                "Black Basta", group, "source--mitre", "source--workbook"
            ),
            ("catalog", "medium", "source--workbook"),
        )

    def test_generated_state_flag_is_stripped_without_actor_specific_evidence(self) -> None:
        actor = {
            "actor_types": ["state-sponsored", "threat-cluster"],
            "profile_basis": "actor-scoped-census-evidence",
        }
        self.assertEqual(derive_actor_types(actor, None), ["threat-cluster"])

    def test_explicit_state_sponsorship_can_restore_state_type(self) -> None:
        actor = {
            "actor_types": ["state-sponsored", "threat-cluster"],
            "profile_basis": "actor-scoped-census-evidence",
        }
        group = {"description": "Example is a state-sponsored threat group."}
        self.assertIn("state-sponsored", derive_actor_types(actor, group))

    def test_explicit_financial_description_does_not_become_state_sponsored(self) -> None:
        actor = {
            "actor_types": ["state-sponsored", "threat-cluster"],
            "profile_basis": "actor-scoped-census-evidence",
        }
        group = {"description": "Example is a financially motivated threat group."}
        derived = derive_actor_types(actor, group)
        self.assertIn("financially-motivated", derived)
        self.assertNotIn("state-sponsored", derived)

    def test_state_sponsorship_does_not_imply_espionage(self) -> None:
        group = {"description": "Example is a state-sponsored group known for disruptive attacks."}
        motivations = derive_motivations(
            ["state-sponsored", "threat-cluster"],
            group,
            "source--mitre",
            "source--workbook",
        )
        self.assertNotIn("espionage", {item["type"] for item in motivations})

    def test_espionage_requires_explicit_actor_text(self) -> None:
        group = {"description": "Example conducts cyber espionage and intelligence collection."}
        motivations = derive_motivations(
            ["threat-cluster"],
            group,
            "source--mitre",
            "source--workbook",
        )
        self.assertIn("espionage", {item["type"] for item in motivations})


class CollectionTests(unittest.TestCase):
    def test_catalog_and_generated_profiles_are_complete(self) -> None:
        root = Path(__file__).resolve().parents[2]
        catalog = json.loads(
            (root / "actor_profile" / "corpus-catalog.json").read_text(
                encoding="utf-8"
            )
        )
        slugs = [actor["slug"] for actor in catalog["actors"]]
        self.assertEqual(len(slugs), len(set(slugs)))
        active_profile_slugs = {
            path.parent.name
            for path in (root / "profiles").glob("*/actor-profile.json")
            if json.loads(path.read_text(encoding="utf-8"))["status"]
            != "deprecated"
        }
        self.assertEqual(
            set(slugs),
            active_profile_slugs,
            "The catalog must include every active profile and exclude deprecated tombstones.",
        )
        for actor in catalog["actors"]:
            normalized_catalog_aliases = [
                normalized_name(alias) for alias in actor.get("aliases", [])
            ]
            self.assertEqual(
                len(normalized_catalog_aliases),
                len(set(normalized_catalog_aliases)),
                f"normalized duplicate catalog alias: {actor['slug']}",
            )
            profile_path = root / "profiles" / actor["slug"] / "actor-profile.json"
            self.assertTrue(profile_path.is_file(), actor["slug"])
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            self.assertEqual(profile["profile_id"], f"actor--{actor['slug']}")
            normalized_profile_aliases = [
                normalized_name(alias["name"])
                for alias in profile["actor"]["aliases"]
            ]
            self.assertEqual(
                len(normalized_profile_aliases),
                len(set(normalized_profile_aliases)),
                f"normalized duplicate profile alias: {actor['slug']}",
            )
            self.assertFalse(
                any(
                    alias["name"].lower().startswith(("http://", "https://"))
                    for alias in profile["actor"]["aliases"]
                ),
                actor["slug"],
            )

    def test_collection_validation_has_no_errors(self) -> None:
        root = Path(__file__).resolve().parents[2]
        summary = json.loads(
            (root / "profiles" / "processing-summary.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(summary["actor_count"], len(summary["results"]))
        self.assertEqual(summary["error_count"], 0)
        self.assertTrue(all(item["status"] == "complete" for item in summary["results"]))


if __name__ == "__main__":
    unittest.main()
