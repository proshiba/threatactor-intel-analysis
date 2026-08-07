#!/usr/bin/env python3
"""Regression tests for observable classification and normalization."""

from __future__ import annotations

import sys
import unittest
import json
from itertools import groupby
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from common import normalize_observable, normalize_time, refang  # noqa: E402
from ingest_observables import (  # noqa: E402
    NON_HASH_WORD_RE,
    analyst_marked_indicator,
    classified_record_values,
    classify_hash,
    extract_artifacts,
    extract_iocs,
    looks_like_hash,
)


class ObservableBoundaryTests(unittest.TestCase):
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
        for actor in catalog["actors"]:
            profile_path = root / "profiles" / actor["slug"] / "actor-profile.json"
            self.assertTrue(profile_path.is_file(), actor["slug"])
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            self.assertEqual(profile["profile_id"], f"actor--{actor['slug']}")
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
