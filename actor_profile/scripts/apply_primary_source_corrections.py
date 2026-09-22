#!/usr/bin/env python3
"""Apply reviewed activity, alias, capability, and relationship corrections.

The corrections in this migration are intentionally limited to claims checked
against the named vendors' original reports.  It is idempotent and keeps
publisher dates separate from activity observation dates.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from activity_diamond import materialize_profile_diamonds
from bootstrap_all_profiles import normalized_name
from common import load_json, stable_digest, utc_now, write_json_atomic


ROOT = Path(__file__).resolve().parents[2]
PROFILES = ROOT / "profiles"
CATALOG = ROOT / "actor_profile" / "corpus-catalog.json"
REVIEW_DECISIONS = ROOT / "parse-daily" / "review-decisions.json"

GOOGLE_UNC6384_SOURCE_ID = "source--gtig-unc6384-captive-portal-2025"
MICROSOFT_FOX_SOURCE_ID = "source--daily-1f90e973408c7fac0a86"
MICROSOFT_DEV0832_SOURCE_ID = "source--microsoft-dev0832-vice-society-2022"
HUNTRESS_TA444_SOURCE_ID = "source--huntress-bluenoroff-macos-2025"
PROOFPOINT_TA444_SOURCE_ID = "source--proofpoint-ta444-2023"
GENIANS_APT37_SOURCE_ID = "source--genians-apt37-k-messenger-2025"
MANDIANT_APT45_SOURCE_ID = "source--mandiant-apt45-2024"
GTIG_UNC5342_SOURCE_ID = "source--gtig-unc5342-etherhiding-2025"
GTIG_UNC6040_SOURCE_ID = "source--gtig-unc6040-salesforce-vishing-2025"
GTIG_UNC6671_SOURCE_ID = "source--gtig-shinyhunters-saas-clusters-2026"
CISCO_SALT_SOURCE_ID = "source--cisco-talos-salt-typhoon-jumbledpath-2025"
CISA_SALT_BOUNDARY_SOURCE_ID = "source--cisa-aa25-239a-salt-typhoon-boundary"
CHECKPOINT_KONNI_SOURCE_ID = "source--checkpoint-konni-ai-backdoor-2026"
PROOFPOINT_TA406_SOURCE_ID = "source--proofpoint-ta406-konni-boundary-2025"
GITLAB_CLICKFIX_SOURCE_ID = "source--gitlab-contagious-interview-clickfix-2025"

MUSTANG_ACTIVITY_ID = "activity--daily-421f30dbc45ea8e51ecf"
VANILLA_FALSE_ACTIVITY_ID = "activity--daily-c535922b3c89d69acd5c"
VANILLA_TEAMS_ACTIVITY_ID = "activity--daily-cdd28b7e4efb97edb05f"
TA444_ACTIVITY_ID = "activity--daily-e034301964da7955795d"
APT37_FALSE_TITLE_ACTIVITY_ID = "activity--daily-c093c6edea29f9fcc0ac"
APT38_AWS_SUPPLY_CHAIN_ACTIVITY_ID = "activity--daily-e7e43253a3ee354a7560"
WATER_GALURA_QILIN_ACTIVITY_ID = "activity--daily-e30bc3c3abfd77cddd94"
CLICKFIX_BEAVERTAIL_SOURCE_ID = "source--daily-dddef70e68c0dc59a5d3"
STORM2603_TOOLSHELL_LEGACY_ACTIVITY_ID = "activity--daily-b80b607914fb7f62f988"
STORM2603_TOOLSHELL_ACTIVITY_ID = "activity--storm-2603--toolshell-warlock-2025"
STORM2603_SUPERSEDED_SOURCE_IDS = {
    "source--daily-0e75e392e2685f601677",
    "source--daily-5c143f1d91377b49cfcc",
    "source--daily-c9fa26bbe8d21f50b441",
}


def time_point(
    value: str | None,
    precision: str = "unknown",
    status: str = "unknown",
    basis: str = "not-stated",
) -> dict[str, Any]:
    return {
        "value": value,
        "precision": precision,
        "status": status,
        "basis": basis,
    }


def source_record(
    *,
    source_id: str,
    url: str,
    title: str,
    publisher: str,
    published: str,
    claims: list[str],
    actor_scope: str,
    note: str,
    accessed: str = "2026-09-21",
    language: str = "en",
    source_type: str = "vendor-threat-research",
    reliability: str = "high",
) -> dict[str, Any]:
    return {
        "source_id": source_id,
        "path": url,
        "url": url,
        "title": title,
        "publisher": publisher,
        "published_at": time_point(
            f"{published}T00:00:00Z", "day", "known", "source-publication"
        ),
        "accessed_at": f"{accessed}T00:00:00Z",
        "language": language,
        "source_type": source_type,
        "tlp": "TLP:CLEAR",
        "reliability": reliability,
        "sha256": None,
        "actor_scope": actor_scope,
        "claims_supported": claims,
        "analyst_notes": note,
    }


GOOGLE_UNC6384_SOURCE = source_record(
    source_id=GOOGLE_UNC6384_SOURCE_ID,
    url="https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats",
    title="Deception in Depth: PRC-Nexus Espionage Campaign Hijacks Web Traffic to Target Diplomats",
    publisher="Google Threat Intelligence Group",
    published="2025-08-25",
    claims=["activity", "attribution", "relationship", "capability", "targeting", "ttp", "ioc"],
    actor_scope="overlapping",
    note=(
        "GTIG attributes the campaign to UNC6384 and assesses that UNC6384 is "
        "associated with TEMP.Hex/Mustang Panda. GTIG does not call this Silk "
        "Typhoon and does not assert exact actor identity."
    ),
)

MICROSOFT_DEV0832_SOURCE = source_record(
    source_id=MICROSOFT_DEV0832_SOURCE_ID,
    url="https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-opportunistic-ransomware-campaigns-impacting-us-education-sector/",
    title="DEV-0832 (Vice Society) opportunistic ransomware campaigns impacting US education sector",
    publisher="Microsoft Threat Intelligence",
    published="2022-10-25",
    claims=["identity", "alias", "activity", "capability", "targeting", "ttp"],
    actor_scope="exact",
    note=(
        "Microsoft states that DEV-0832 is also known as Vice Society and is now "
        "tracked as Vanilla Tempest; the report documents its 2022 campaigns."
    ),
)

HUNTRESS_TA444_SOURCE = source_record(
    source_id=HUNTRESS_TA444_SOURCE_ID,
    url="https://www.huntress.com/blog/inside-bluenoroff-web3-intrusion-analysis",
    title="Inside the BlueNoroff Web3 macOS Intrusion Analysis",
    publisher="Huntress",
    published="2025-06-18",
    claims=["identity", "alias", "activity", "attribution", "capability", "targeting", "ttp", "ioc", "victim-case"],
    actor_scope="direct",
    note=(
        "Huntress attributes the June 2025 intrusion to TA444/BlueNoroff with high "
        "confidence and enumerates the recovered macOS implants."
    ),
)

PROOFPOINT_TA444_SOURCE = source_record(
    source_id=PROOFPOINT_TA444_SOURCE_ID,
    url="https://www.proofpoint.com/uk/blog/threat-insight/ta444-apt-startup-aimed-at-your-funds",
    title="TA444: The APT Startup Aimed at Acquisition (of Your Funds)",
    publisher="Proofpoint Threat Research",
    published="2023-01-25",
    claims=["identity", "activity", "attribution", "relationship", "capability", "targeting"],
    actor_scope="direct",
    note=(
        "Proofpoint defines TA444 as its own cluster and explicitly says APT38 "
        "heavily overlaps with TA444; this supports overlap, not exact identity."
    ),
)

GENIANS_APT37_SOURCE = source_record(
    source_id=GENIANS_APT37_SOURCE_ID,
    url="https://www.genians.co.kr/blog/threat_intelligence/k-messenger",
    title="K 메신저로 유포된 'APT37' 그룹의 악성 HWP 사례 분석",
    publisher="Genians Security Center",
    published="2025-02-03",
    claims=["activity", "attribution", "capability", "targeting", "ttp"],
    actor_scope="direct",
    note=(
        "Genians directly attributes the analyzed HWP/LNK campaign to APT37, "
        "documents the 13 November 2024 K-messenger delivery, and identifies "
        "the in-memory payload as RoKRAT."
    ),
    language="ko",
)

MANDIANT_APT45_SOURCE = source_record(
    source_id=MANDIANT_APT45_SOURCE_ID,
    url="https://cloud.google.com/blog/topics/threat-intelligence/apt45-north-korea-digital-military-machine",
    title="APT45: North Korea's Digital Military Machine",
    publisher="Mandiant",
    published="2024-07-25",
    claims=["identity", "activity", "attribution", "relationship", "capability", "targeting"],
    actor_scope="overlapping",
    note=(
        "Mandiant states that activity it attributes to APT45 has been publicly "
        "reported as Andariel, Onyx Sleet, Stonefly, and Silent Chollima. This "
        "supports a cross-vendor overlap, not an unqualified exact alias."
    ),
)

GTIG_UNC5342_SOURCE = source_record(
    source_id=GTIG_UNC5342_SOURCE_ID,
    url="https://cloud.google.com/blog/topics/threat-intelligence/dprk-adopts-etherhiding",
    title="DPRK Adopts EtherHiding: Nation-State Malware Hiding on Blockchains",
    publisher="Google Threat Intelligence Group",
    published="2025-10-16",
    claims=["activity", "attribution", "relationship", "capability", "targeting", "ttp", "ioc"],
    actor_scope="overlapping",
    note=(
        "GTIG tracks UNC5342 as the threat actor incorporating EtherHiding into "
        "the social-engineering campaign Palo Alto Networks named Contagious "
        "Interview. MITRE separately models Contagious Interview as Group G1052, "
        "so the repository preserves both records with a taxonomy relationship."
    ),
)

GTIG_UNC6040_SOURCE = source_record(
    source_id=GTIG_UNC6040_SOURCE_ID,
    url="https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion",
    title="The Cost of a Call: From Voice Phishing to Data Extortion",
    publisher="Google Threat Intelligence Group",
    published="2025-06-04",
    claims=["activity", "relationship", "capability", "targeting", "ttp"],
    actor_scope="direct",
    note=(
        "GTIG attributes Salesforce vishing and initial data theft to UNC6040, "
        "but separately tracks the subsequent ShinyHunters-branded extortion as "
        "UNC6240. The report says a partnership is possible, not proven."
    ),
)

GTIG_UNC6671_SOURCE = source_record(
    source_id=GTIG_UNC6671_SOURCE_ID,
    url="https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft",
    title="Vishing for Access: Tracking the Expansion of ShinyHunters-Branded SaaS Data Theft",
    publisher="Mandiant / Google Threat Intelligence Group",
    published="2026-01-30",
    claims=["activity", "relationship", "capability", "targeting", "ttp", "ioc"],
    actor_scope="overlapping",
    note=(
        "GTIG deliberately tracks UNC6661, UNC6671, and UNC6240 separately to "
        "represent evolving partnerships and possible impersonation. UNC6671 "
        "used an unbranded extortion email and a different Tox ID."
    ),
)

CISCO_SALT_SOURCE = source_record(
    source_id=CISCO_SALT_SOURCE_ID,
    url="https://blog.talosintelligence.com/salt-typhoon-analysis/",
    title="Weathering the storm: In the midst of a Typhoon",
    publisher="Cisco Talos",
    published="2025-02-20",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "Cisco Talos attributes the investigated telecommunications campaign to "
        "Salt Typhoon and documents JumbledPath. It does not identify UNC2286."
    ),
)

CISA_SALT_BOUNDARY_SOURCE = source_record(
    source_id=CISA_SALT_BOUNDARY_SOURCE_ID,
    url="https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a",
    title="Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System",
    publisher="CISA and international partners",
    published="2025-08-27",
    claims=["activity", "attribution", "relationship", "capability", "targeting", "ttp", "ioc"],
    actor_scope="overlapping",
    note=(
        "The joint advisory says the activity partially overlaps with several "
        "industry names, including Salt Typhoon, and explicitly warns that vendor "
        "groupings may not correlate one-to-one. It does not list UNC2286."
    ),
)
CISA_SALT_BOUNDARY_SOURCE["source_type"] = "government-advisory"

CHECKPOINT_KONNI_SOURCE = source_record(
    source_id=CHECKPOINT_KONNI_SOURCE_ID,
    url="https://research.checkpoint.com/2026/konni-targets-developers-with-ai-malware/",
    title="KONNI Adopts AI to Generate PowerShell Backdoors",
    publisher="Check Point Research",
    published="2026-01-22",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "Check Point attributes the analyzed campaign directly to the KONNI APT "
        "cluster and documents the blockchain-themed lures, October 2025 samples, "
        "and AI-assisted PowerShell backdoor."
    ),
)

PROOFPOINT_TA406_SOURCE = source_record(
    source_id=PROOFPOINT_TA406_SOURCE_ID,
    url="https://www.proofpoint.com/us/blog/threat-insight/ta406-pivots-front",
    title="TA406 Pivots to the Front",
    publisher="Proofpoint Threat Research",
    published="2025-05-13",
    claims=["identity", "relationship", "activity", "attribution", "targeting", "ttp"],
    actor_scope="overlapping",
    note=(
        "Proofpoint states that TA406 overlaps activity publicly tracked as Opal "
        "Sleet and Konni. This supports a cross-vendor overlap, not exact identity."
    ),
)

GITLAB_CLICKFIX_SOURCE = source_record(
    source_id=GITLAB_CLICKFIX_SOURCE_ID,
    url=(
        "https://gitlab-com.gitlab.io/gl-security/security-tech-notes/"
        "threat-intelligence-tech-notes/north-korean-malware-sept-2025/"
    ),
    title="Tech Note - BeaverTail variant distributed via malicious repositories and ClickFix lure",
    publisher="GitLab Threat Intelligence",
    published="2025-09-17",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "GitLab directly observed the ClickFix infrastructure and BeaverTail/"
        "InvisibleFerret samples from May 2025 and associates their operators "
        "with identifiers including Contagious Interview and Famous Chollima."
    ),
)

SEC_SOLARWINDS_SOURCE = source_record(
    source_id="source--sec-solarwinds-disclosure-enforcement-2024",
    url="https://www.sec.gov/newsroom/press-releases/2024-174",
    title="SEC Charges Four Companies With Misleading Cyber Disclosures",
    publisher="U.S. Securities and Exchange Commission",
    published="2024-10-22",
    claims=["activity", "victim-case", "attribution-context"],
    actor_scope="overlapping",
    note=(
        "The SEC names Unisys, Avaya, Check Point, and Mimecast and describes the "
        "intruder only as the threat actor likely behind the SolarWinds Orion hack. "
        "It supports the enforcement aftermath, not a fresh APT29 intrusion or a "
        "standalone exact-attribution claim."
    ),
    source_type="government-press-release",
)

MANDIANT_APT41_SOURCE = source_record(
    source_id="source--mandiant-apt41-arisen-from-dust-2024",
    url="https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust",
    title="APT41 Has Arisen From the DUST",
    publisher="Mandiant",
    published="2024-07-18",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "Mandiant directly attributes the sustained campaign observed since 2023 "
        "to APT41 and enumerates the affected countries, sectors, and toolchain."
    ),
)

CISCO_APT41_TAIWAN_SOURCE = source_record(
    source_id="source--cisco-talos-apt41-taiwan-institute-2024",
    url=(
        "https://blog.talosintelligence.com/chinese-hacking-group-apt41-compromised-"
        "taiwanese-government-affiliated-research-institute-with-shadowpad-and-cobaltstrike-2/"
    ),
    title=(
        "Chinese hacking group APT41 compromised Taiwanese government-affiliated "
        "research institute with ShadowPad and Cobalt Strike"
    ),
    publisher="Cisco Talos",
    published="2024-08-01",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc", "victim-case"],
    actor_scope="direct",
    note=(
        "Cisco Talos attributes the single-institute intrusion to APT41 with "
        "medium confidence and dates the initial compromise to mid-July 2023."
    ),
)

ZSCALER_TRANSLATEXT_SOURCE = source_record(
    source_id="source--zscaler-kimsuky-translatext-2024",
    url=(
        "https://www.zscaler.com/blogs/security-research/"
        "kimsuky-deploys-translatext-target-south-korean-academia"
    ),
    title="Kimsuky Deploys TRANSLATEXT to Target South Korean Academia",
    publisher="Zscaler ThreatLabz",
    published="2024-06-27",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "Zscaler observed the campaign in March 2024 and documents the malicious "
        "Chrome extension's credential, cookie, and screenshot collection."
    ),
)

CHECKMARX_MOONSTONE_SOURCE = source_record(
    source_id="source--checkmarx-moonstone-npm-2024",
    url=(
        "https://checkmarx.com/blog/"
        "a-new-north-korean-group-emerges-disrupting-the-open-source-ecosystem/"
    ),
    title="A New North Korean Group Emerges, Disrupting the Open-Source Ecosystem",
    publisher="Checkmarx",
    published="2024-06-13",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "Checkmarx documents Moonstone Sleet malicious npm packages in the first "
        "and second quarters of 2024, including added obfuscation and Linux support."
    ),
)

MICROSOFT_MOONSTONE_SOURCE = source_record(
    source_id="source--microsoft-moonstone-sleet-2024",
    url=(
        "https://www.microsoft.com/en-us/security/blog/2024/05/28/"
        "moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/"
    ),
    title="Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks",
    publisher="Microsoft Threat Intelligence",
    published="2024-05-28",
    claims=["identity", "alias", "activity", "attribution", "relationship", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "Microsoft says Moonstone Sleet was formerly Storm-1789, initially reused "
        "Diamond Sleet code and techniques, then moved to its own infrastructure "
        "and conducted concurrent operations as a distinct actor."
    ),
)

NCSC_UK_RETAIL_SOURCE = source_record(
    source_id="source--ncsc-uk-retail-incidents-2025",
    url="https://www.ncsc.gov.uk/blog-post/incidents-impacting-retailers",
    title="Incidents impacting retailers",
    publisher="UK National Cyber Security Centre",
    published="2025-05-04",
    claims=["activity", "victim-case", "attribution-boundary"],
    actor_scope="unconfirmed",
    note=(
        "NCSC explicitly said it was not yet in a position to determine whether "
        "the retailer incidents were linked or whether one actor was responsible."
    ),
    source_type="government-advisory",
)

MANDIANT_UNC3944_VSPHERE_SOURCE = source_record(
    source_id="source--mandiant-unc3944-vsphere-2025",
    url="https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944",
    title="From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944",
    publisher="Google Threat Intelligence Group / Mandiant",
    published="2025-07-23",
    claims=["identity", "activity", "attribution", "capability", "targeting", "ttp"],
    actor_scope="overlapping",
    note=(
        "Mandiant describes a mid-2025 UNC3944 campaign against retail, airline, "
        "and insurance organizations and states that UNC3944 overlaps Scattered Spider."
    ),
)

QANTAS_INCIDENT_SOURCE = source_record(
    source_id="source--qantas-call-centre-incident-2025",
    url="https://investor.qantas.com/DownloadFile.axd?file=/Report/ComNews/20250702/02963135.pdf",
    title="Qantas provides update on customer data cyber incident",
    publisher="Qantas Airways Limited",
    published="2025-07-02",
    claims=["activity", "victim-case", "impact", "attribution-boundary"],
    actor_scope="unconfirmed",
    note=(
        "Qantas confirms the third-party customer-platform incident and affected "
        "record categories but does not attribute the intrusion to Scattered Spider."
    ),
    source_type="first-party-incident-disclosure",
)

FBI_SCATTERED_SPIDER_SOURCE = source_record(
    source_id="source--fbi-cisa-scattered-spider-2025",
    url="https://www.fbi.gov/file-repository/cyber-alerts/scattered-spider-072925.pdf",
    title="Scattered Spider Joint Cybersecurity Advisory",
    publisher="FBI, CISA, and international partners",
    published="2025-07-29",
    claims=["identity", "alias", "activity", "capability", "targeting", "ttp", "ioc"],
    actor_scope="overlapping",
    note=(
        "The joint advisory lists cross-industry tracking names and updated TTPs. "
        "The names are retained as overlaps because vendor cluster boundaries need "
        "not be globally one-to-one."
    ),
    source_type="government-advisory",
)

MICROSOFT_TOOLSHELL_SOURCE = source_record(
    source_id="source--microsoft-toolshell-2025",
    url=(
        "https://www.microsoft.com/en-us/security/blog/2025/07/22/"
        "disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/"
    ),
    title="Disrupting active exploitation of on-premises SharePoint vulnerabilities",
    publisher="Microsoft Threat Intelligence",
    published="2025-07-22",
    claims=[
        "activity",
        "attribution",
        "capability",
        "targeting",
        "ttp",
        "ioc",
        "hunting",
    ],
    actor_scope="direct",
    accessed="2026-09-22",
    note=(
        "Microsoft separately attributes exploitation to Linen Typhoon, Violet "
        "Typhoon, and Storm-2603. It does not uniquely attribute the reported NNSA "
        "victim event to any one of those clusters. The IOC table and actor-specific "
        "hunting query were directly rechecked on 2026-09-22: only four web-shell "
        "hashes tied to a named Storm-2603 C2, twelve IIS_Server_dll.dll hashes "
        "explicitly labeled as the Storm-2603 IIS Backdoor, "
        "update.updatemicfosoft.com, msupdate.updatemicfosoft.com, and "
        "65.38.121.198 are retained as 19 exact indicators. The generic "
        "spinstall0.aspx hash, unattributed exploitation IPs, and other "
        "actor-unspecific rows are excluded."
    ),
)

UNIT42_REACT2SHELL_SOURCE = source_record(
    source_id="source--unit42-react2shell-cl-sta-1015-2025",
    url=(
        "https://unit42.paloaltonetworks.com/"
        "cve-2025-55182-react-and-cve-2025-66478-next/"
    ),
    title="Exploitation of Critical Vulnerability in React Server Components",
    publisher="Palo Alto Networks Unit 42",
    published="2025-12-12",
    claims=["identity", "alias", "activity", "attribution", "capability", "ttp", "ioc"],
    actor_scope="overlapping",
    note=(
        "Unit 42 assesses the observed sequence with high confidence as consistent "
        "with CL-STA-1015 and calls that cluster aka UNC5174. The cross-vendor "
        "mapping is preserved as overlap rather than a universal exact alias."
    ),
)

GTIG_REACT2SHELL_SOURCE = source_record(
    source_id="source--gtig-react2shell-multiple-actors-2025",
    url=(
        "https://cloud.google.com/blog/topics/threat-intelligence/"
        "threat-actors-exploit-react2shell-cve-2025-55182"
    ),
    title="Multiple Threat Actors Exploit React2Shell (CVE-2025-55182)",
    publisher="Google Threat Intelligence Group",
    published="2025-12-12",
    claims=["activity", "attribution-boundary", "capability", "ttp", "ioc"],
    actor_scope="boundary",
    note=(
        "GTIG describes multiple React2Shell clusters and separately tracks a "
        "SNOWLIGHT-using cluster as UNC6586. Shared malware in this exploitation "
        "window is not sufficient to collapse all activity into UNC5174."
    ),
)

ECLECTICIQ_UNC5221_SOURCE = source_record(
    source_id="source--eclecticiq-unc5221-epmm-2025",
    url=(
        "https://blog.eclecticiq.com/china-nexus-threat-actor-actively-exploiting-"
        "ivanti-endpoint-manager-mobile-cve-2025-4428-vulnerability"
    ),
    title=(
        "China-Nexus Threat Actor Actively Exploiting Ivanti Endpoint Manager "
        "Mobile (CVE-2025-4428) Vulnerability"
    ),
    publisher="EclecticIQ",
    published="2025-05-21",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "EclecticIQ attributes the exploitation observed from May 15 with high "
        "confidence to UNC5221 and documents KrustyLoader, Sliver, and AWS S3 use."
    ),
)

MANDIANT_UNC5820_SOURCE = source_record(
    source_id="source--mandiant-unc5820-fortimanager-2024",
    url=(
        "https://cloud.google.com/blog/topics/threat-intelligence/"
        "fortimanager-zero-day-exploitation-cve-2024-47575"
    ),
    title="Investigating FortiManager Zero-Day Exploitation (CVE-2024-47575)",
    publisher="Mandiant",
    published="2024-10-23",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "Mandiant observed UNC5820 exploitation from June 27 through at least "
        "September 23, 2024, across more than 50 potentially compromised devices; "
        "motivation and actor location remained unknown."
    ),
)

GTIG_UNC6395_SOURCE = source_record(
    source_id="source--gtig-unc6395-salesloft-drift-2025",
    url=(
        "https://cloud.google.com/blog/topics/threat-intelligence/"
        "data-theft-salesforce-instances-via-salesloft-drift"
    ),
    title="Widespread Data Theft Targets Salesforce Instances via Salesloft Drift",
    publisher="Google Threat Intelligence Group / Mandiant",
    published="2025-08-26",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "GTIG tracks the August 8-18 data-theft campaign as UNC6395 and warns that "
        "all Drift-connected tokens may have been exposed."
    ),
)

SALESLOFT_INCIDENT_SOURCE = source_record(
    source_id="source--salesloft-drift-incident-2025",
    url="https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Update",
    title="Update on Mandiant Drift and Salesloft Application Investigations",
    publisher="Salesloft",
    published="2025-09-06",
    claims=["activity", "victim-case", "impact", "ttp"],
    actor_scope="unattributed",
    note=(
        "Salesloft's first-party timeline covers GitHub access and reconnaissance "
        "from March through June 2025, followed by theft and use of Drift OAuth tokens."
    ),
    source_type="first-party-incident-disclosure",
)

CISCO_ARCANEDOOR_SOURCE = source_record(
    source_id="source--cisco-talos-arcanedoor-2024",
    url=(
        "https://blog.talosintelligence.com/"
        "arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/"
    ),
    title="ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices",
    publisher="Cisco Talos",
    published="2024-04-24",
    claims=["identity", "alias", "activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="exact",
    note=(
        "Cisco identifies the actor as UAT4356 and states that Microsoft tracks the "
        "same actor as Storm-1849; it documents Line Runner and Line Dancer."
    ),
)

CISCO_FIRESTARTER_SOURCE = source_record(
    source_id="source--cisco-talos-uat4356-firestarter-2026",
    url="https://blog.talosintelligence.com/uat-4356-firestarter/",
    title="UAT-4356's Targeting of Cisco Firepower Devices",
    publisher="Cisco Talos",
    published="2026-04-23",
    claims=["activity", "attribution", "capability", "targeting", "ttp", "ioc"],
    actor_scope="direct",
    note=(
        "Cisco reports continued UAT4356 targeting of Firepower/FXOS devices, "
        "n-day exploitation, and deployment of the custom FIRESTARTER backdoor."
    ),
)

MICROSOFT_STORM2603_PARALLEL_SOURCE = source_record(
    source_id="source--microsoft-storm2603-parallel-intrusion-2026",
    url=(
        "https://www.microsoft.com/en-us/security/blog/2026/06/22/"
        "one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/"
    ),
    title="One intrusion, two cyberattackers: Uncovering parallel threat activity",
    publisher="Microsoft Defender Experts Cybersecurity Incident Response",
    published="2026-06-22",
    claims=["activity", "attribution", "capability", "ttp", "victim-case"],
    actor_scope="direct",
    note=(
        "Microsoft separates Storm-2603 activity from a second unrelated actor in "
        "the same environment; shared victim presence is not an actor relationship."
    ),
)


def merge_source(profile: dict[str, Any], source: dict[str, Any]) -> None:
    profile["sources"] = [
        item
        for item in profile.get("sources", [])
        if item.get("source_id") != source["source_id"]
    ] + [source]


def add_evidence(record: dict[str, Any], source_id: str) -> None:
    record["evidence_refs"] = sorted(
        set(record.get("evidence_refs", [])) | {source_id}
    )


def find_activity(profile: dict[str, Any], activity_id: str) -> dict[str, Any]:
    return next(
        item
        for item in profile.get("activities", [])
        if item.get("activity_id") == activity_id
    )


def migrate_profile_activity_id(
    profile: dict[str, Any], old_id: str, new_id: str
) -> dict[str, Any] | None:
    """Rename one Activity and every exact structured reference idempotently."""
    old_matches = [
        item
        for item in profile.get("activities", [])
        if item.get("activity_id") == old_id
    ]
    new_matches = [
        item
        for item in profile.get("activities", [])
        if item.get("activity_id") == new_id
    ]
    if len(old_matches) > 1 or len(new_matches) > 1 or (old_matches and new_matches):
        raise ValueError(f"unsafe Activity ID collision: {old_id} -> {new_id}")

    def replace(value: Any) -> Any:
        if isinstance(value, dict):
            for key, item in list(value.items()):
                value[key] = replace(item)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                value[index] = replace(item)
        elif value == old_id:
            return new_id
        return value

    if old_matches:
        replace(profile)
        return old_matches[0]
    return new_matches[0] if new_matches else None


def remove_activity(profile: dict[str, Any], activity_id: str) -> None:
    """Remove a superseded activity and dependent victim/activity references."""

    profile["activities"] = [
        item
        for item in profile.get("activities", [])
        if item.get("activity_id") != activity_id
    ]
    retained_victims = []
    for victim in profile.get("victim_cases", []):
        original_refs = victim.get("activity_refs", [])
        if activity_id not in original_refs:
            retained_victims.append(victim)
            continue
        victim["activity_refs"] = [
            ref for ref in original_refs if ref != activity_id
        ]
        if victim["activity_refs"]:
            retained_victims.append(victim)
    profile["victim_cases"] = retained_victims
    for ttp in profile.get("ttps", []):
        ttp["activity_refs"] = [
            ref for ref in ttp.get("activity_refs", []) if ref != activity_id
        ]


def upsert_activity(profile: dict[str, Any], activity: dict[str, Any]) -> None:
    profile["activities"] = [
        item
        for item in profile.get("activities", [])
        if item.get("activity_id") != activity["activity_id"]
    ] + [activity]


def add_source_to_linked_victims(
    profile: dict[str, Any], activity: dict[str, Any], source_id: str
) -> None:
    victim_ids = set(activity.get("victim_refs", []))
    for victim in profile.get("victim_cases", []):
        if victim.get("victim_case_id") in victim_ids:
            add_evidence(victim, source_id)


def merge_alias(
    profile: dict[str, Any],
    *,
    name: str,
    vendor: str,
    source_ids: list[str],
    scope: str,
    note: str,
) -> None:
    aliases = profile["actor"].setdefault("aliases", [])
    existing = next(
        (
            item
            for item in aliases
            if normalized_name(item.get("name", "")) == normalized_name(name)
        ),
        None,
    )
    record = {
        "name": name,
        "vendor": vendor,
        "scope": scope,
        "confidence": "high",
        "evidence_refs": source_ids,
        "analyst_notes": note,
    }
    if existing is None:
        aliases.append(record)
    else:
        existing.update(record)


def add_relationship(
    profile: dict[str, Any],
    *,
    source_slug: str,
    target_actor: str,
    relationship_type: str,
    description: str,
    evidence_refs: list[str],
    note: str,
    confidence: str = "high",
) -> None:
    relationship_id = (
        f"relationship--{source_slug}--verified--"
        + stable_digest(source_slug, target_actor, relationship_type, *evidence_refs)[:16]
    )
    record = {
        "relationship_id": relationship_id,
        "target_actor": target_actor,
        "relationship_type": relationship_type,
        "description": description,
        "confidence": confidence,
        "first_observed": time_point(None),
        "last_observed": time_point(None),
        "evidence_refs": evidence_refs,
        "analyst_notes": note,
    }
    profile["relationships"] = [
        item
        for item in profile.get("relationships", [])
        if not (
            item.get("relationship_id") == relationship_id
            or (
                normalized_name(item.get("target_actor", ""))
                == normalized_name(target_actor)
                and item.get("relationship_type") == relationship_type
            )
        )
    ] + [record]


def merge_malware(
    profile: dict[str, Any],
    *,
    malware_id: str,
    name: str,
    aliases: list[str],
    platforms: list[str],
    description: str,
    first_observed: dict[str, Any],
    last_observed: dict[str, Any],
    evidence_refs: list[str],
) -> None:
    records = profile["capabilities"]["malware"]
    record = {
        "id": malware_id,
        "name": name,
        "aliases": aliases,
        "types": platforms,
        "description": description,
        "first_observed": first_observed,
        "last_observed": last_observed,
        "confidence": "high",
        "evidence_refs": evidence_refs,
        "analyst_notes": "Primary-source-verified capability used in the linked activity.",
    }
    existing = next(
        (
            item
            for item in records
            if item.get("id") == malware_id
            or normalized_name(item.get("name", "")) == normalized_name(name)
        ),
        None,
    )
    if existing is None:
        records.append(record)
    else:
        existing.update(record)


def fix_mustang_panda(profile: dict[str, Any]) -> None:
    merge_source(profile, GOOGLE_UNC6384_SOURCE)
    activity = find_activity(profile, MUSTANG_ACTIVITY_ID)
    activity["name"] = (
        "UNC6384、キャプティブポータルを乗っ取り東南アジアの外交官へマルウェアを配布"
    )
    activity["description"] = (
        "GTIGは、PRC-nexusのUNC6384がキャプティブポータルの通信を中間者攻撃で"
        "乗っ取り、東南アジアの外交官と世界各地の組織を標的にした2025年の諜報"
        "キャンペーンを報告した。偽Adobe更新から署名済みSTATICPLUGINを配布し、"
        "CANONSTAGERをDLLサイドロードしてSOGU.SEC（PlugX）をメモリ内展開した。"
        "GTIGはツール、TTP、標的、C2重複からUNC6384をTEMP.Hex（Mustang Panda）"
        "に関連すると評価するが、Silk Typhoonとは記載していない。"
    )
    add_evidence(activity, GOOGLE_UNC6384_SOURCE_ID)
    activity["confidence"] = "medium"
    activity["analyst_notes"] = (
        "一次資料照合済み。GTIGは活動主体をUNC6384、関連クラスタをTEMP.Hex/"
        "Mustang Pandaとする。二次記事見出しのSilk Typhoon表記は活動名・alias根拠"
        "として採用しない。活動期間は一次資料から安全に確定できないためunknown。"
    )
    for source in profile["sources"]:
        if source.get("source_id") == "source--daily-902e3900ab433af5ea5f":
            source["actor_scope"] = "overlapping"
            caveat = (
                "Source-title caveat: the secondary headline says Silk Typhoon, "
                "but the underlying GTIG report attributes the campaign to UNC6384 "
                "associated with TEMP.Hex/Mustang Panda; the headline is not alias evidence."
            )
            if caveat not in source.get("analyst_notes", ""):
                source["analyst_notes"] = (
                    source.get("analyst_notes", "").rstrip() + " " + caveat
                ).strip()


def fix_apt37(profile: dict[str, Any]) -> None:
    """Replace a multi-topic article headline with the APT37-specific campaign."""

    merge_source(profile, GENIANS_APT37_SOURCE)
    activity = find_activity(profile, APT37_FALSE_TITLE_ACTIVITY_ID)
    activity["name"] = (
        "APT37、侵害端末のKメッセンジャーからHWP／LNKとRoKRATを拡散"
    )
    activity["description"] = (
        "Genians Security Centerは、APT37が2024年11月13日に韓国のKメッセンジャー"
        "団体チャットへ悪性HWP文書とZIP内のLNKを時間差で配布した活動を分析した。"
        "初期スピアフィッシング後に侵害端末で偵察・探索を行い、ログイン中の"
        "メッセンジャーを追加配布経路として悪用した。HWPのOLEとLNK内PowerShellから"
        "ファイルレスで実行されるペイロードは、APT37のRoKRAT系列と特定された。"
    )
    activity["first_observed"] = time_point(
        "2024-11-13T00:00:00Z", "day", "known", "source-stated"
    )
    activity["last_observed"] = time_point(
        "2024-11-13T00:00:00Z", "day", "known", "source-stated"
    )
    activity["reported_at"] = time_point(
        "2025-02-03T00:00:00Z", "day", "known", "source-publication"
    )
    activity["malware_refs"] = sorted(
        set(activity.get("malware_refs", [])) | {"malware--rokrat"}
    )
    activity["confidence"] = "high"
    add_evidence(activity, GENIANS_APT37_SOURCE_ID)
    activity["analyst_notes"] = (
        "一次資料再検証済み。元の日次記事はContagious InterviewのFERRET活動を見出しと"
        "本文の主題にし、末尾で別件のAPT37活動へ言及していた。APT37プロファイルでは"
        "Genians一次分析が裏付けるKメッセンジャー／RoKRAT活動だけへ表示内容を限定した。"
    )

    for source in profile.get("sources", []):
        if source.get("source_id") == "source--daily-5be59ed011b127efaaf3":
            source["publisher"] = "The Hacker News"
            source["published_at"] = time_point(
                "2025-02-04T00:00:00Z", "day", "known", "source-publication"
            )
            source["source_type"] = "news-report"
            source["actor_scope"] = "indirect"
            source["claims_supported"] = ["activity"]
            caveat = (
                "The headline and main article concern Contagious Interview/FERRET; "
                "APT37 appears only in a separate closing item about a RoKRAT campaign."
            )
            if caveat not in source.get("analyst_notes", ""):
                source["analyst_notes"] = (
                    source.get("analyst_notes", "").rstrip() + " " + caveat
                ).strip()


def fix_apt38_aws_supply_chain(profile: dict[str, Any]) -> None:
    """Correct AWS publication dates and preserve its vendor-cluster boundary."""

    activity = find_activity(profile, APT38_AWS_SUPPLY_CHAIN_ACTIVITY_ID)
    activity["name"] = (
        "Sapphire Sleet系クラスタ、npmパッケージのサプライチェーンを侵害"
    )
    activity["first_observed"] = time_point(
        "2025-03-01T00:00:00Z", "month", "known", "source-stated"
    )
    activity["last_observed"] = time_point(
        "2026-03-01T00:00:00Z", "month", "known", "source-stated"
    )
    activity["reported_at"] = time_point(
        "2026-07-29T00:00:00Z", "day", "known", "source-publication"
    )
    activity["confidence"] = "medium"
    add_evidence(activity, "source--mitre-attack-19-2")
    activity["analyst_notes"] = (
        "AWS一次資料は同一DPRK系アクターをSAPPHIRE SLEET、STARDUST CHOLLIMA、"
        "BlueNoroff、CageyChameleon、Alluring Piscesとして記載し、中程度の確度で"
        "帰属した。APT38という名称は本文にないため、MITRE G0082のAssociated Groups"
        "を介したoverlappingスコープの活動として保持し、完全同一とは断定しない。"
    )

    for source in profile.get("sources", []):
        if source.get("source_id") == "source--daily-a7e2c22924a222a6eb0f":
            canonical_url = (
                "https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-"
                "hacker-group-behind-open-source-supply-chain-attacks/"
            )
            source.update(
                {
                    "path": canonical_url,
                    "url": canonical_url,
                    "publisher": "AWS Security Blog",
                    "published_at": time_point(
                        "2026-07-29T00:00:00Z",
                        "day",
                        "known",
                        "source-publication",
                    ),
                    "accessed_at": "2026-09-21T00:00:00Z",
                    "language": "en",
                    "source_type": "vendor-threat-research",
                    "reliability": "high",
                    "actor_scope": "overlapping",
                    "claims_supported": [
                        "activity",
                        "attribution",
                        "capability",
                        "targeting",
                        "ttp",
                        "ioc",
                    ],
                }
            )
            source["analyst_notes"] = (
                "AWS attributes the package compromises with medium confidence to a "
                "DPRK-linked cluster tracked under several vendor names. APT38 mapping "
                "uses MITRE G0082 and remains scoped as overlapping."
            )


def fix_water_galura(profile: dict[str, Any]) -> None:
    """Keep the Qilin software/RaaS distinct from its Water Galura operators."""

    activity = find_activity(profile, WATER_GALURA_QILIN_ACTIVITY_ID)
    activity["name"] = (
        "Water Galuraが運営するQilin RaaS、被害者への法的圧力機能を追加"
    )
    activity["description"] = (
        "Water Galuraが運営するQilin RaaSは、アフィリエイト向けパネルへ被害者に"
        "支払い圧力をかける「Call Lawyer」機能を追加した。公開集計ではQilinの被害"
        "主張が2025年4月に72件、5月に55件確認され、Rust/C製ペイロード、ネットワーク"
        "拡散、ログ消去、交渉自動化、DDoS、スパム、データ保管などを提供するサービス"
        "として報告された。QilinはRaaS／ランサムウェア名であり、Water Galuraの"
        "無条件な別名としては扱わない。"
    )
    activity["first_observed"] = time_point(
        "2025-04-01T00:00:00Z", "month", "known", "source-stated"
    )
    activity["last_observed"] = time_point(
        "2025-05-01T00:00:00Z", "month", "known", "source-stated"
    )
    activity["reported_at"] = time_point(
        "2025-06-20T00:00:00Z", "day", "known", "source-publication"
    )
    activity["malware_refs"] = sorted(
        set(activity.get("malware_refs", [])) | {"malware--qilin"}
    )
    add_evidence(activity, "source--mitre-attack-19-2")
    activity["analyst_notes"] = (
        "The Hacker NewsはQilinグループをGold Feather／Water Galuraとも表記する一方、"
        "MITRE ATT&CK G1050/S1242はWater Galura（GOLD FEATHER）をQilin RaaSの運営者、"
        "QilinをSoftwareとして分離する。本プロファイルは後者のentity境界を採用した。"
    )

    for source in profile.get("sources", []):
        if source.get("source_id") == "source--daily-3c55cd8958f6103f4eaf":
            source["publisher"] = "The Hacker News"
            source["published_at"] = time_point(
                "2025-06-20T00:00:00Z", "day", "known", "source-publication"
            )
            source["source_type"] = "news-report"
            source["actor_scope"] = "direct"
            caveat = (
                "Entity-boundary caveat: MITRE models Water Galura/GOLD FEATHER "
                "as the operators and Qilin as the RaaS software."
            )
            if caveat not in source.get("analyst_notes", ""):
                source["analyst_notes"] = (
                    source.get("analyst_notes", "").rstrip() + " " + caveat
                ).strip()


def fix_actor_relationships(
    apt45: dict[str, Any],
    andariel: dict[str, Any],
    unc5342: dict[str, Any],
    contagious_interview: dict[str, Any],
    kimsuky: dict[str, Any],
) -> None:
    """Record verified cross-taxonomy links without collapsing actor scopes."""

    for profile in (apt45, andariel):
        merge_source(profile, MANDIANT_APT45_SOURCE)
    apt45_description = (
        "Mandiant states that activity it attributes to APT45 has been publicly "
        "reported as Andariel, while treating vendor cluster boundaries as an "
        "attribution complication rather than asserting universal alias identity."
    )
    apt45_note = (
        "Cross-vendor overlap only; preserve separate APT45 and Andariel profiles "
        "until a primary source defines the identity boundary more precisely."
    )
    add_relationship(
        apt45,
        source_slug="apt45",
        target_actor="Andariel",
        relationship_type="overlaps-with",
        description=apt45_description,
        evidence_refs=[MANDIANT_APT45_SOURCE_ID],
        note=apt45_note,
    )
    add_relationship(
        andariel,
        source_slug="andariel",
        target_actor="APT45",
        relationship_type="overlaps-with",
        description=apt45_description,
        evidence_refs=[MANDIANT_APT45_SOURCE_ID],
        note=apt45_note,
    )

    for profile in (unc5342, contagious_interview):
        merge_source(profile, GTIG_UNC5342_SOURCE)
    unc_description = (
        "GTIG tracks UNC5342 as the threat actor using EtherHiding in the campaign "
        "Palo Alto Networks named Contagious Interview; MITRE models Contagious "
        "Interview as a threat group rather than a campaign."
    )
    unc_note = (
        "Taxonomy boundary retained: the source links actor activity to the named "
        "campaign but does not establish a universal exact alias."
    )
    add_relationship(
        unc5342,
        source_slug="unc5342",
        target_actor="Contagious Interview",
        relationship_type="taxonomy-overlaps-with",
        description=unc_description,
        evidence_refs=[GTIG_UNC5342_SOURCE_ID],
        note=unc_note,
    )
    add_relationship(
        contagious_interview,
        source_slug="contagious-interview",
        target_actor="UNC5342",
        relationship_type="taxonomy-overlaps-with",
        description=unc_description,
        evidence_refs=[GTIG_UNC5342_SOURCE_ID],
        note=unc_note,
    )

    # A prior enrichment pass emitted the same Kimsuky-to-APT43 overlap twice at
    # different confidence levels. Keep the reviewed two-primary-source record.
    candidates = [
        item
        for item in kimsuky.get("relationships", [])
        if item.get("target_actor") == "APT43"
        and item.get("relationship_type") == "overlaps-with"
    ]
    if candidates:
        preferred = max(
            candidates,
            key=lambda item: (
                item.get("confidence") == "high",
                len(item.get("evidence_refs", [])),
            ),
        )
        kimsuky["relationships"] = [
            item
            for item in kimsuky.get("relationships", [])
            if not (
                item.get("target_actor") == "APT43"
                and item.get("relationship_type") == "overlaps-with"
            )
        ] + [preferred]


def fix_vendor_cluster_boundaries(
    unc6040: dict[str, Any],
    unc6240: dict[str, Any],
    unc6661: dict[str, Any],
    unc6671: dict[str, Any],
    unc2286: dict[str, Any],
    salt_typhoon: dict[str, Any],
) -> None:
    """Repair umbrella-brand and vendor-cluster conflation in daily reports."""

    for profile in (unc6040, unc6240):
        merge_source(profile, GTIG_UNC6040_SOURCE)
    unc6040_activity = find_activity(
        unc6040, "activity--daily-dcc1e326e606705f98d4"
    )
    unc6040_activity.update(
        {
            "name": "UNC6040、vishingでSalesforce接続アプリを承認させデータを窃取",
            "description": (
                "GTIGは、UNC6040がITサポートを装った音声フィッシングで従業員を誘導し、"
                "攻撃者管理のSalesforce接続アプリ（Data Loaderまたは同等のカスタム"
                "アプリ）を承認させ、大量のCRMデータを窃取したと報告した。GTIGは"
                "初期侵入・窃取をUNC6040、後続のShinyHunters名義の恐喝をUNC6240として"
                "分けて追跡しており、両者の提携可能性は示すが同一主体とは断定していない。"
            ),
            "reported_at": time_point(
                "2025-06-04T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "evidence_refs": [GTIG_UNC6040_SOURCE_ID],
            "analyst_notes": (
                "一次資料に合わせ、ShinyHuntersをUNC6040の無条件な別名とする二次記事の"
                "表現を除去。侵入・データ窃取と後続恐喝のクラスタ境界を保持する。"
            ),
        }
    )
    for victim in unc6040.get("victim_cases", []):
        if unc6040_activity["activity_id"] not in victim.get("activity_refs", []):
            continue
        victim["name"] = "被害事例: UNC6040によるSalesforceデータ窃取"
        victim["description"] = unc6040_activity["description"]
        victim["reported_at"] = unc6040_activity["reported_at"]
        victim["confidence"] = "high"
        victim["evidence_refs"] = [GTIG_UNC6040_SOURCE_ID]
        victim["analyst_notes"] = unc6040_activity["analyst_notes"]
    relationship_description = (
        "GTIG tracks the initial Salesforce vishing and data theft as UNC6040 "
        "and the subsequent ShinyHunters-branded extortion as UNC6240; a "
        "partnership is possible but not established as exact identity."
    )
    relationship_note = (
        "Sequential operational link with distinct tracking boundaries; do not "
        "treat ShinyHunters as an exact UNC6040 alias."
    )
    add_relationship(
        unc6040,
        source_slug="unc6040",
        target_actor="UNC6240",
        relationship_type="related-to",
        description=relationship_description,
        evidence_refs=[GTIG_UNC6040_SOURCE_ID],
        note=relationship_note,
    )
    add_relationship(
        unc6240,
        source_slug="unc6240",
        target_actor="UNC6040",
        relationship_type="related-to",
        description=relationship_description,
        evidence_refs=[GTIG_UNC6040_SOURCE_ID],
        note=relationship_note,
    )

    for profile in (unc6240, unc6661, unc6671):
        merge_source(profile, GTIG_UNC6671_SOURCE)
    unc6671_activity = find_activity(
        unc6671, "activity--daily-0697f946d4469dc9883a"
    )
    unc6671_activity.update(
        {
            "name": "UNC6671、vishingでSSO資格情報を窃取しSaaSデータを流出",
            "description": (
                "Mandiantは、UNC6671が2026年1月初旬からIT担当者を装って電話し、"
                "被害組織を偽の認証サイトへ誘導してSSO資格情報とMFAコードを窃取したと"
                "報告した。侵入後はOktaアカウントへアクセスし、PowerShellを用いて"
                "SharePointとOneDriveの機密データを取得した。手口はUNC6661と類似する"
                "一方、UNC6671に続く恐喝メールはShinyHunters名義ではなく、異なるTox ID"
                "を使用しており、Mandiantは別の人物が関与する可能性を示している。"
            ),
            "first_observed": time_point(
                "2026-01-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2026-01-30T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "evidence_refs": [GTIG_UNC6671_SOURCE_ID],
            "analyst_notes": (
                "ShinyHunters-branded activity is an umbrella description. GTIG's "
                "separate UNC6671 cluster boundary and unbranded extortion detailを採用。"
            ),
        }
    )
    for victim in unc6671.get("victim_cases", []):
        if unc6671_activity["activity_id"] not in victim.get("activity_refs", []):
            continue
        victim["name"] = "被害事例: UNC6671によるSSO・SaaSデータ窃取"
        victim["description"] = unc6671_activity["description"]
        victim["first_observed"] = unc6671_activity["first_observed"]
        victim["last_observed"] = unc6671_activity["last_observed"]
        victim["reported_at"] = unc6671_activity["reported_at"]
        victim["confidence"] = "high"
        victim["evidence_refs"] = [GTIG_UNC6671_SOURCE_ID]
        victim["analyst_notes"] = unc6671_activity["analyst_notes"]

    boundary_description = (
        "GTIG tracks UNC6661, UNC6671, and UNC6240 separately within recent "
        "ShinyHunters-branded SaaS theft reporting to preserve possible "
        "partnership and impersonation boundaries."
    )
    boundary_note = (
        "Shared umbrella branding and TTPs do not establish exact identity; "
        "Mandiant notes indicators that separate individuals may be involved."
    )
    for left, left_slug, right, right_name in (
        (unc6671, "unc6671", unc6240, "UNC6240"),
        (unc6240, "unc6240", unc6671, "UNC6671"),
        (unc6671, "unc6671", unc6661, "UNC6661"),
        (unc6661, "unc6661", unc6671, "UNC6671"),
    ):
        add_relationship(
            left,
            source_slug=left_slug,
            target_actor=right_name,
            relationship_type="taxonomy-overlaps-with",
            description=boundary_description,
            evidence_refs=[GTIG_UNC6671_SOURCE_ID],
            note=boundary_note,
        )
    # UNC6661 intrusions are explicitly followed by UNC6240 extortion.
    for left, left_slug, right_name in (
        (unc6661, "unc6661", "UNC6240"),
        (unc6240, "unc6240", "UNC6661"),
    ):
        add_relationship(
            left,
            source_slug=left_slug,
            target_actor=right_name,
            relationship_type="related-to",
            description=(
                "GTIG attributes extortion following UNC6661 intrusions to UNC6240, "
                "based on negotiation-account and extortion-artifact overlaps."
            ),
            evidence_refs=[GTIG_UNC6671_SOURCE_ID],
            note="Linked stages, retained as distinct GTIG threat clusters.",
        )

    for profile in (unc2286, salt_typhoon):
        merge_source(profile, CISA_SALT_BOUNDARY_SOURCE)
    merge_source(salt_typhoon, CISCO_SALT_SOURCE)
    unc2286_activity_id = "activity--daily-2c3e99f982af03e6e5ab"
    unc2286["activities"] = [
        item
        for item in unc2286.get("activities", [])
        if item.get("activity_id") != unc2286_activity_id
    ]
    unc2286["victim_cases"] = [
        item
        for item in unc2286.get("victim_cases", [])
        if unc2286_activity_id not in item.get("activity_refs", [])
    ]
    for ttp in unc2286.get("ttps", []):
        ttp["activity_refs"] = [
            ref for ref in ttp.get("activity_refs", []) if ref != unc2286_activity_id
        ]
    daily_source_id = "source--daily-976395d39cbe624f587e"
    for category in ("countries", "regions", "sectors", "roles"):
        unc2286["targets"][category] = [
            item
            for item in unc2286["targets"][category]
            if not (
                set(item.get("evidence_refs", [])) == {daily_source_id}
                and "Salt Typhoon" in item.get("description", "")
            )
        ]
    for source in unc2286.get("sources", []):
        if source.get("source_id") == daily_source_id:
            source["actor_scope"] = "overlapping"
            source["claims_supported"] = ["relationship-lead"]
            source["analyst_notes"] = (
                source.get("analyst_notes", "").rstrip()
                + " The secondary article lists UNC2286 as an alias, but Cisco Talos "
                "does not use that designation and the joint CISA advisory warns that "
                "industry groupings are not necessarily one-to-one."
            ).strip()
    uncertainty = (
        "A secondary report maps UNC2286 to Salt Typhoon, but available primary "
        "Cisco and joint-government reporting does not confirm a one-to-one identity."
    )
    if uncertainty not in unc2286["assessment"].setdefault("uncertainties", []):
        unc2286["assessment"]["uncertainties"].append(uncertainty)
    salt_boundary_description = (
        "A secondary report maps UNC2286 to Salt Typhoon; primary Cisco reporting "
        "documents Salt Typhoon without UNC2286, and the joint CISA advisory warns "
        "that industry tracking names may not correlate one-to-one."
    )
    salt_boundary_note = (
        "Provisional taxonomy overlap only. Do not duplicate Salt Typhoon activity "
        "under UNC2286 or promote the mapping to an exact alias without primary evidence."
    )
    add_relationship(
        unc2286,
        source_slug="unc2286",
        target_actor="Salt Typhoon",
        relationship_type="taxonomy-overlaps-with",
        description=salt_boundary_description,
        evidence_refs=[daily_source_id, CISA_SALT_BOUNDARY_SOURCE_ID],
        note=salt_boundary_note,
        confidence="medium",
    )
    add_relationship(
        salt_typhoon,
        source_slug="salt-typhoon",
        target_actor="UNC2286",
        relationship_type="taxonomy-overlaps-with",
        description=salt_boundary_description,
        evidence_refs=[daily_source_id, CISA_SALT_BOUNDARY_SOURCE_ID],
        note=salt_boundary_note,
        confidence="medium",
    )

    salt_activity = find_activity(
        salt_typhoon, "activity--daily-4e15138dd5323d6e8406"
    )
    salt_activity.update(
        {
            "name": "Salt Typhoon、通信事業者のネットワーク機器でJumbledPathを使用",
            "description": (
                "Cisco Talosは、Salt Typhoonが米国の大手通信事業者を侵害し、盗取した"
                "正規資格情報で複数ベンダーのネットワーク機器へ長期間アクセスしたと"
                "報告した。攻撃者は設定情報や認証トラフィックを収集し、侵害機器を"
                "踏み台として横展開した。Go製ELFユーティリティJumbledPathは、離れた"
                "Cisco機器でパケットキャプチャを実行し、経路上のログを消去・阻害して"
                "暗号化済み取得データを返送するために使われた。"
            ),
            "first_observed": time_point(None),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2025-02-20T00:00:00Z", "day", "known", "source-publication"
            ),
            "target_refs": [
                "target--mitre-group--country--41795735fc0e57933c4e",
                "target--activity-rule--sector--97fa6f38a056d42117be",
            ],
            "confidence": "high",
            "evidence_refs": [CISCO_SALT_SOURCE_ID],
            "analyst_notes": (
                "Cisco Talos一次資料に限定。二次記事が混在させたRedMikeの別キャンペーン"
                "期間・地域と、未確認のUNC2286 exact-alias主張を除去した。"
            ),
        }
    )
    for malware in salt_typhoon["capabilities"]["malware"]:
        if normalized_name(malware.get("name", "")) == normalized_name("JumbledPath"):
            malware["evidence_refs"] = sorted(
                set(malware.get("evidence_refs", [])) | {CISCO_SALT_SOURCE_ID}
            )
            malware["first_observed"] = time_point(None)
            malware["last_observed"] = time_point(None)
    for target in [
        item
        for category in ("countries", "sectors")
        for item in salt_typhoon["targets"][category]
        if item["id"] in salt_activity["target_refs"]
    ]:
        add_evidence(target, CISCO_SALT_SOURCE_ID)
    for victim in salt_typhoon.get("victim_cases", []):
        if salt_activity["activity_id"] not in victim.get("activity_refs", []):
            continue
        victim["name"] = "被害事例: Salt Typhoonによる通信事業者ネットワーク侵害"
        victim["description"] = salt_activity["description"]
        victim["target_refs"] = salt_activity["target_refs"]
        victim["first_observed"] = time_point(None)
        victim["last_observed"] = time_point(None)
        victim["reported_at"] = salt_activity["reported_at"]
        victim["confidence"] = "high"
        victim["evidence_refs"] = [CISCO_SALT_SOURCE_ID]
        victim["analyst_notes"] = salt_activity["analyst_notes"]


def fix_ta406_konni_boundary(ta406: dict[str, Any], konni: dict[str, Any]) -> None:
    """Ground the shared KONNI activity while preserving vendor scope."""

    checkpoint_for_ta406 = dict(CHECKPOINT_KONNI_SOURCE)
    checkpoint_for_ta406["actor_scope"] = "overlapping"
    checkpoint_for_ta406["analyst_notes"] = (
        CHECKPOINT_KONNI_SOURCE["analyst_notes"]
        + " TA406 linkage is supported separately by Proofpoint's overlap statement."
    )
    proofpoint_for_ta406 = dict(PROOFPOINT_TA406_SOURCE)
    proofpoint_for_ta406["actor_scope"] = "direct"
    for profile, checkpoint, proofpoint in (
        (ta406, checkpoint_for_ta406, proofpoint_for_ta406),
        (konni, CHECKPOINT_KONNI_SOURCE, PROOFPOINT_TA406_SOURCE),
    ):
        merge_source(profile, checkpoint)
        merge_source(profile, proofpoint)

    first_observed = time_point(
        "2025-10-01T00:00:00Z", "month", "known", "source-stated-sample-upload"
    )
    reported_at = time_point(
        "2026-01-22T00:00:00Z", "day", "known", "source-publication"
    )
    name = "KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布"
    description = (
        "Check Point Researchは、KONNIに関連付けたフィッシング活動で、ブロック"
        "チェーン関連の開発者・エンジニアを狙うおとり文書と悪性LNKを確認した。"
        "LNKはPowerShellローダから永続化・UAC回避・分析回避・C2タスク実行機能を持つ"
        "PowerShellバックドアを展開する。2025年10月にアップロードされた初期亜種も"
        "確認され、検体投稿元は日本・豪州・インドを含むが、投稿元を被害国の確定値とは"
        "しない。Check PointはKONNIへ直接帰属し、ProofpointはTA406をKonni/Opal Sleet"
        "活動との重複として扱うため、TA406との完全同一性は断定しない。"
    )
    note = (
        "Check Point一次分析で活動・期間・TTPを確認。TA406への対応はProofpointの"
        "cross-vendor overlapに基づき、exact aliasには昇格しない。"
    )
    for profile, activity_id, confidence in (
        (ta406, "activity--daily-ed16c556a166870fdeb2", "medium"),
        (konni, "activity--daily-647f622408c58cbd428c", "high"),
    ):
        activity = find_activity(profile, activity_id)
        activity.update(
            {
                "name": name,
                "description": description,
                "first_observed": first_observed,
                "last_observed": time_point(None),
                "reported_at": reported_at,
                "confidence": confidence,
                "evidence_refs": [CHECKPOINT_KONNI_SOURCE_ID, PROOFPOINT_TA406_SOURCE_ID],
                "analyst_notes": note,
            }
        )
        for victim in profile.get("victim_cases", []):
            if activity_id not in victim.get("activity_refs", []):
                continue
            victim["name"] = "被害事例: KONNIによるブロックチェーン技術者標的化"
            victim["description"] = description
            victim["first_observed"] = first_observed
            victim["last_observed"] = time_point(None)
            victim["reported_at"] = reported_at
            victim["confidence"] = confidence
            victim["evidence_refs"] = [
                CHECKPOINT_KONNI_SOURCE_ID,
                PROOFPOINT_TA406_SOURCE_ID,
            ]
            victim["analyst_notes"] = note

    relationship_description = (
        "Proofpoint states that TA406 overlaps activity publicly tracked as Konni "
        "and Opal Sleet; Check Point directly attributes the January 2026 report's "
        "campaign to the KONNI cluster."
    )
    relationship_note = (
        "Cross-vendor overlap retained; neither source establishes universal "
        "one-to-one identity between every TA406 and Konni observation."
    )
    add_relationship(
        ta406,
        source_slug="ta406",
        target_actor="Konni",
        relationship_type="overlaps-with",
        description=relationship_description,
        evidence_refs=[PROOFPOINT_TA406_SOURCE_ID, CHECKPOINT_KONNI_SOURCE_ID],
        note=relationship_note,
        confidence="medium",
    )
    add_relationship(
        konni,
        source_slug="konni",
        target_actor="TA406",
        relationship_type="overlaps-with",
        description=relationship_description,
        evidence_refs=[PROOFPOINT_TA406_SOURCE_ID, CHECKPOINT_KONNI_SOURCE_ID],
        note=relationship_note,
        confidence="medium",
    )


def remove_activity_and_exclusive_derivatives(
    profile: dict[str, Any], activity_id: str, source_id: str
) -> None:
    """Remove a rejected activity and generated records supported only by it."""

    removed = [
        item
        for item in profile.get("activities", [])
        if item.get("activity_id") == activity_id
    ]
    target_refs = {
        ref for item in removed for ref in item.get("target_refs", [])
    }
    profile["activities"] = [
        item
        for item in profile.get("activities", [])
        if item.get("activity_id") != activity_id
    ]
    profile["victim_cases"] = [
        item
        for item in profile.get("victim_cases", [])
        if activity_id not in item.get("activity_refs", [])
    ]
    retained_ttps = []
    for ttp in profile.get("ttps", []):
        ttp["activity_refs"] = [
            ref for ref in ttp.get("activity_refs", []) if ref != activity_id
        ]
        generated_only = (
            not ttp.get("activity_refs")
            and ttp.get("ttp_id", "").startswith("ttp--activity-rule--")
            and set(ttp.get("evidence_refs", [])) <= {source_id}
        )
        if not generated_only:
            retained_ttps.append(ttp)
    profile["ttps"] = retained_ttps

    remaining_target_refs = {
        ref
        for item in profile.get("activities", [])
        for ref in item.get("target_refs", [])
    }
    for category in ("countries", "regions", "sectors", "roles"):
        profile["targets"][category] = [
            item
            for item in profile["targets"].get(category, [])
            if not (
                item.get("id") in target_refs - remaining_target_refs
                and set(item.get("evidence_refs", [])) <= {source_id}
            )
        ]


def fix_kimsuky_quishing_duplicates(
    apt43: dict[str, Any], kimsuky: dict[str, Any]
) -> None:
    """Keep the FBI Kimsuky activity once and out of the APT43 boundary."""

    daily_source_id = "source--daily-4c3098e731ae81f16008"
    remove_activity_and_exclusive_derivatives(
        apt43, "activity--daily-47a3435a13311fff4bdb", daily_source_id
    )
    remove_activity_and_exclusive_derivatives(
        kimsuky, "activity--daily-7fba10858bc6d43d600f", daily_source_id
    )
    note = (
        "The January 2026 FBI FLASH attributes the May-June 2025 QR-code "
        "spearphishing only to Kimsuky and does not name APT43. The activity is "
        "already represented once as activity--kimsuky-quishing-2025 with the "
        "official FBI source; the two secondary daily records are not canonicalized."
    )
    uncertainty = (
        "The FBI's January 2026 Kimsuky Quishing FLASH does not itself attribute "
        "that specific activity to APT43; cross-vendor overlap is recorded only "
        "as a relationship."
    )
    if uncertainty not in apt43["assessment"].setdefault("uncertainties", []):
        apt43["assessment"]["uncertainties"].append(uncertainty)
    for profile in (apt43, kimsuky):
        for source in profile.get("sources", []):
            if source.get("source_id") != daily_source_id:
                continue
            source["actor_scope"] = (
                "overlapping" if profile is apt43 else "direct"
            )
            source["claims_supported"] = ["corroboration"]
            source["analyst_notes"] = (
                source.get("analyst_notes", "").rstrip() + " " + note
            ).strip()


def fix_clickfix_beavertail_multitopic_boundary(
    apt43: dict[str, Any],
    kimsuky: dict[str, Any],
    contagious_interview: dict[str, Any],
) -> None:
    """Keep the BeaverTail campaign with the article's actual subject cluster."""

    rejected = (
        (apt43, "activity--daily-ad2a0b8acf43d0efef90"),
        (kimsuky, "activity--daily-f1c379b17bba17ff7692"),
    )
    for profile, activity_id in rejected:
        remove_activity_and_exclusive_derivatives(
            profile, activity_id, CLICKFIX_BEAVERTAIL_SOURCE_ID
        )
        for source in profile.get("sources", []):
            if source.get("source_id") != CLICKFIX_BEAVERTAIL_SOURCE_ID:
                continue
            source["actor_scope"] = "indirect"
            source["claims_supported"] = ["context"]
            note = (
                "The article's BeaverTail/InvisibleFerret ClickFix campaign is "
                "attributed to Contagious Interview. Kimsuky/APT43 appears only "
                "in a separate later news item, so the main campaign is not "
                "copied across that actor boundary."
            )
            if note not in source.get("analyst_notes", ""):
                source["analyst_notes"] = (
                    source.get("analyst_notes", "").rstrip() + " " + note
                ).strip()

    canonical = next(
        (
            item
            for item in contagious_interview.get("activities", [])
            if item.get("activity_id") == "activity--daily-ad821db17bd56b3397be"
        ),
        None,
    )
    if canonical is None:
        raise ValueError(
            "Contagious Interview ClickFix/BeaverTail canonical activity is missing"
        )
    merge_source(contagious_interview, GITLAB_CLICKFIX_SOURCE)
    canonical["first_observed"] = time_point(
        "2025-05-01T00:00:00Z", "month", "known", "source-observed"
    )
    canonical["last_observed"] = time_point(None)
    canonical["reported_at"] = time_point(
        "2025-09-17T00:00:00Z", "day", "known", "source-publication"
    )
    canonical["confidence"] = "high"
    canonical["evidence_refs"] = [GITLAB_CLICKFIX_SOURCE_ID]
    canonical["analyst_notes"] = (
        "GitLab一次分析に基づき、2025年5月から試験展開されたClickFix経由の"
        "BeaverTail/InvisibleFerret活動をContagious Interviewの活動として保持する。"
        "同じ二次記事の後半にあるKimsuky/APT43の別キャンペーンとは分離した。"
    )


def fix_vanilla_tempest(profile: dict[str, Any]) -> None:
    merge_source(profile, MICROSOFT_DEV0832_SOURCE)
    fox_source = source_record(
        source_id=MICROSOFT_FOX_SOURCE_ID,
        url="https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/",
        title="Exposing Fox Tempest: A malware-signing service operation",
        publisher="Microsoft Threat Intelligence",
        published="2026-05-19",
        claims=["activity", "relationship", "capability", "targeting", "infrastructure"],
        actor_scope="direct",
        note=(
            "The report concerns Fox Tempest, but its Vanilla Tempest case study "
            "directly documents Vanilla Tempest's use of the signing service."
        ),
    )
    merge_source(profile, fox_source)

    profile["activities"] = [
        item
        for item in profile.get("activities", [])
        if item.get("activity_id") != VANILLA_FALSE_ACTIVITY_ID
    ]
    for ttp in profile.get("ttps", []):
        ttp["activity_refs"] = [
            ref
            for ref in ttp.get("activity_refs", [])
            if ref != VANILLA_FALSE_ACTIVITY_ID
        ]
    profile["victim_cases"] = [
        item
        for item in profile.get("victim_cases", [])
        if VANILLA_FALSE_ACTIVITY_ID not in item.get("activity_refs", [])
    ]

    activity = find_activity(profile, VANILLA_TEAMS_ACTIVITY_ID)
    activity["name"] = (
        "Vanilla Tempest、Fox Tempest署名済みの偽TeamsインストーラでOysterを配布"
    )
    activity["description"] = (
        "Vanilla Tempestは遅くとも2025年6月からFox TempestのMSaaSへトロイ化した"
        "Microsoft Teamsインストーラを持ち込み、不正署名済みバイナリを正規広告、"
        "マルバタイジング、SEOポイズニング経由で配布した。偽MSTeamsSetup.exeは"
        "Oyster（Broomstick）バックドアを展開し、観測事例の一部ではRhysida"
        "ランサムウェアも配備された。Microsoftは2025年10月に関連する200超の"
        "証明書を失効させた。"
    )
    activity["first_observed"] = time_point(
        "2025-06-01T00:00:00Z", "month", "known", "source-stated"
    )
    activity["last_observed"] = time_point(
        "2025-10-01T00:00:00Z", "month", "known", "source-stated"
    )
    activity["confidence"] = "high"
    add_evidence(activity, MICROSOFT_FOX_SOURCE_ID)
    activity["analyst_notes"] = (
        "MicrosoftのFox Tempest一次報告にあるVanilla Tempest事例へ主体を限定して"
        "統合。Fox Tempest自体のサービス運営・妨害はVanilla Tempestの活動として"
        "扱わず、uses-service-of関係として分離した。"
    )

    oyster_id = "malware--oyster"
    rhysida_id = "malware--rhysida"
    teams_first = time_point(
        "2025-06-01T00:00:00Z", "month", "known", "source-stated"
    )
    teams_last = time_point(
        "2025-10-01T00:00:00Z", "month", "known", "source-stated"
    )
    merge_malware(
        profile,
        malware_id=oyster_id,
        name="Oyster",
        aliases=["Broomstick"],
        platforms=["Windows"],
        description=(
            "Modular multistage backdoor deployed from trojanized Teams installers; "
            "it provides persistence, C2, host discovery, and follow-on delivery."
        ),
        first_observed=teams_first,
        last_observed=teams_last,
        evidence_refs=[MICROSOFT_FOX_SOURCE_ID],
    )
    merge_malware(
        profile,
        malware_id=rhysida_id,
        name="Rhysida",
        aliases=[],
        platforms=["Windows"],
        description=(
            "Ransomware deployed by Vanilla Tempest in some intrusions using the "
            "same Fox Tempest-signed Teams-installer process."
        ),
        first_observed=teams_first,
        last_observed=teams_last,
        evidence_refs=[MICROSOFT_FOX_SOURCE_ID],
    )
    activity["malware_refs"] = sorted(
        set(activity.get("malware_refs", [])) | {oyster_id, rhysida_id}
    )

    historical_id = "activity--microsoft-dev0832-education-2022"
    historical = {
        "activity_id": historical_id,
        "name": "DEV-0832／Vanilla Tempestによる2022年の教育機関向け恐喝活動",
        "activity_type": "ransomware-extortion",
        "stix_object_type": "campaign",
        "grouping_context": None,
        "activity_refs": [],
        "first_observed": time_point(
            "2022-07-01T00:00:00Z", "month", "known", "source-stated"
        ),
        "last_observed": time_point(
            "2022-10-01T00:00:00Z", "month", "known", "source-stated"
        ),
        "reported_at": time_point(
            "2022-10-25T00:00:00Z", "day", "known", "source-publication"
        ),
        "description": (
            "MicrosoftはDEV-0832（現Vanilla Tempest、Vice Society）が2022年7月から"
            "10月に米国を中心とする教育機関へランサムウェアと恐喝活動を実施したと"
            "報告した。同集団はBlackCat、QuantumLocker、Zeppelin、Vice Society"
            "固有Zeppelin亜種、RedAlertを切り替え、SystemBCとPortStarterも使用した。"
            "過去の機会的攻撃には地方政府と小売も含まれる。"
        ),
        "target_refs": [],
        "malware_refs": [],
        "infrastructure_refs": [],
        "ttp_refs": [],
        "victim_refs": sorted(
            item["victim_case_id"]
            for item in profile.get("victim_cases", [])
            if historical_id in item.get("activity_refs", [])
        ),
        "confidence": "high",
        "evidence_refs": [MICROSOFT_DEV0832_SOURCE_ID],
        "analyst_notes": (
            "活動期間はMicrosoftが明記する2022年7月〜10月に限定。アクターの"
            "最古活動時期（2021年6月頃）とは分離した。"
        ),
    }
    profile["activities"] = [
        item
        for item in profile.get("activities", [])
        if item.get("activity_id") != historical_id
    ] + [historical]

    malware_specs = [
        ("malware--blackcat", "BlackCat", [], ["Windows", "Linux"], "Ransomware payload used by DEV-0832."),
        ("malware--quantumlocker", "QuantumLocker", [], ["Windows"], "Ransomware payload used by DEV-0832."),
        ("malware--zeppelin", "Zeppelin", [], ["Windows"], "Ransomware family and basis of a Vice Society-branded variant used by DEV-0832."),
        ("malware--redalert", "RedAlert", [], ["Windows"], "Ransomware variant used by DEV-0832 in late September 2022."),
        ("malware--systembc", "SystemBC", [], ["Windows"], "Commodity backdoor and proxy used in DEV-0832 intrusions."),
        ("malware--portstarter", "PortStarter", [], ["Windows"], "Go backdoor used by DEV-0832 to alter firewall settings and open ports for C2."),
    ]
    historic_first = historical["first_observed"]
    historic_last = historical["last_observed"]
    for malware_id, name, aliases, platforms, description in malware_specs:
        merge_malware(
            profile,
            malware_id=malware_id,
            name=name,
            aliases=aliases,
            platforms=platforms,
            description=description,
            first_observed=historic_first,
            last_observed=historic_last,
            evidence_refs=[MICROSOFT_DEV0832_SOURCE_ID],
        )
        historical["malware_refs"].append(malware_id)
    historical["malware_refs"].sort()

    add_relationship(
        profile,
        source_slug="vanilla-tempest",
        target_actor="Fox Tempest",
        relationship_type="uses-service-of",
        description=(
            "Vanilla Tempest used Fox Tempest's malware-signing-as-a-service to "
            "obtain fraudulently signed Teams installers carrying Oyster and, in "
            "some intrusions, Rhysida ransomware."
        ),
        evidence_refs=[MICROSOFT_FOX_SOURCE_ID],
        note=(
            "The actors remain separate: Fox Tempest provided the signing service; "
            "Vanilla Tempest conducted downstream intrusions."
        ),
    )


def fix_ta444(profile: dict[str, Any], apt38: dict[str, Any]) -> None:
    for source in (HUNTRESS_TA444_SOURCE, PROOFPOINT_TA444_SOURCE):
        merge_source(profile, source)
        merge_source(apt38, source)

    alias_note = (
        "Huntress uses these names interchangeably for the June 2025 intrusion, "
        "while Proofpoint states that APT38 heavily overlaps TA444. The alias is "
        "therefore scoped as overlapping across vendor taxonomies, not globally exact."
    )
    for name in (
        "BlueNoroff",
        "Sapphire Sleet",
        "COPERNICIUM",
        "STARDUST CHOLLIMA",
        "CageyChameleon",
    ):
        merge_alias(
            profile,
            name=name,
            vendor="Huntress / Proofpoint",
            source_ids=[HUNTRESS_TA444_SOURCE_ID, PROOFPOINT_TA444_SOURCE_ID],
            scope="overlapping",
            note=alias_note,
        )

    relationship_description = (
        "Proofpoint tracks TA444 as a distinct cluster and states that APT38 "
        "heavily overlaps with it; Huntress also uses TA444/BlueNoroff naming for "
        "the June 2025 intrusion."
    )
    relationship_note = (
        "Cross-vendor cluster overlap; do not collapse TA444 and APT38 into an "
        "unqualified exact identity."
    )
    add_relationship(
        profile,
        source_slug="ta444",
        target_actor="APT38",
        relationship_type="overlaps-with",
        description=relationship_description,
        evidence_refs=[PROOFPOINT_TA444_SOURCE_ID, HUNTRESS_TA444_SOURCE_ID],
        note=relationship_note,
    )
    add_relationship(
        apt38,
        source_slug="apt38",
        target_actor="TA444",
        relationship_type="overlaps-with",
        description=relationship_description,
        evidence_refs=[PROOFPOINT_TA444_SOURCE_ID, HUNTRESS_TA444_SOURCE_ID],
        note=relationship_note,
    )

    activity = find_activity(profile, TA444_ACTIVITY_ID)
    activity["name"] = (
        "TA444／BlueNoroff、ディープフェイクZoom会議からWeb3組織のmacOSを侵害"
    )
    activity["description"] = (
        "2025年6月11日、TA444／BlueNoroffは暗号資産財団の従業員を幹部らの"
        "ディープフェイクを使った偽Zoom会議へ誘導し、偽拡張機能のAppleScriptを"
        "実行させた。Huntressは侵害端末から、永続化を担うTelegram 2、バックドア"
        "Root Troy V4、ローダーInjectWithDyld、Nim Implant、キーロガー兼画面・"
        "クリップボード収集機XScreen、暗号資産情報窃取型CryptoBot、NetChkを回収"
        "した。Huntressはこの侵入をTA444にhigh confidenceで帰属した。"
    )
    activity["confidence"] = "high"
    add_evidence(activity, HUNTRESS_TA444_SOURCE_ID)
    activity["analyst_notes"] = (
        "Huntress一次分析で活動日、被害組織種別、帰属、回収マルウェアを確認。"
        "記事公開日とは分離して2025-06-11を観測日とする。"
    )

    observed = time_point(
        "2025-06-11T00:00:00Z", "day", "known", "source-stated"
    )
    specs = [
        ("malware--telegram-2", "Telegram 2", [], "Nim persistence implant that starts the primary backdoor."),
        ("malware--root-troy-v4", "Root Troy V4", ["RTV", "remoted"], "Go backdoor used to download and execute additional implants."),
        ("malware--injectwithdyld", "InjectWithDyld", ["a"], "C++ loader that decrypts and injects additional payloads."),
        ("malware--ta444-nim-implant", "Nim Implant", ["Trojan 1"], "Injected implant with asynchronous command-execution capability."),
        ("malware--xscreen", "XScreen", ["keyboardd"], "Objective-C keylogger with clipboard and screen-capture capability."),
        ("malware--cryptobot-ta444", "CryptoBot", ["airmond"], "Go infostealer focused on cryptocurrency wallet and browser-extension data."),
        ("malware--netchk", "NetChk", [], "Recovered malicious component that continuously generated random numbers."),
    ]
    for malware_id, name, aliases, description in specs:
        merge_malware(
            profile,
            malware_id=malware_id,
            name=name,
            aliases=aliases,
            platforms=["macOS"],
            description=description,
            first_observed=observed,
            last_observed=observed,
            evidence_refs=[HUNTRESS_TA444_SOURCE_ID],
        )
        activity.setdefault("malware_refs", []).append(malware_id)
    activity["malware_refs"] = sorted(set(activity["malware_refs"]))


def fix_reviewed_primary_activity_evidence(
    apt29: dict[str, Any],
    apt41: dict[str, Any],
    kimsuky: dict[str, Any],
    moonstone: dict[str, Any],
    unc5221: dict[str, Any],
    unc5820: dict[str, Any],
    unc6395: dict[str, Any],
) -> None:
    """Replace secondary-only activity claims with checked original reporting."""

    merge_source(apt29, SEC_SOLARWINDS_SOURCE)
    sec_activity = find_activity(apt29, "activity--daily-1f4283bbe40d968dcd5d")
    sec_activity.update(
        {
            "name": "SEC、SolarWinds関連開示を巡り技術企業4社を処分",
            "description": (
                "米SECは、SolarWinds Orion侵害に関連するサイバーリスクと影響の"
                "開示が投資家を誤解させたとして、Unisys、Avaya、Check Point、"
                "Mimecastを処分した。SEC原文は侵入者を『SolarWinds Orion攻撃の"
                "背後にいる可能性が高い脅威アクター』と記すにとどまり、APT29を"
                "名指ししていない。このレコードは2020年の侵害そのものではなく、"
                "2024年の法執行・開示上の後続事象を整理するGroupingである。"
            ),
            "reported_at": time_point(
                "2024-10-22T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "medium",
            "stix_object_type": "grouping",
            "grouping_context": "suspicious-activity",
            "analyst_notes": (
                "SEC一次資料は企業名と処分理由を裏づけるがAPT29という名称は使わない。"
                "既知のSolarWinds帰属との文脈的関連として保持し、新規侵入を表す"
                "Campaign/Incident関係は生成しない。"
            ),
        }
    )
    add_evidence(sec_activity, SEC_SOLARWINDS_SOURCE["source_id"])
    add_source_to_linked_victims(
        apt29, sec_activity, SEC_SOLARWINDS_SOURCE["source_id"]
    )

    for source in (MANDIANT_APT41_SOURCE, CISCO_APT41_TAIWAN_SOURCE):
        merge_source(apt41, source)
    dust = find_activity(apt41, "activity--daily-207ba8f2eb504435e5e4")
    dust.update(
        {
            "name": "APT41、2023年以降に複数国・複数業種へ継続侵入",
            "description": (
                "Mandiantは、APT41が2023年以降、イタリア、スペイン、台湾、タイ、"
                "トルコ、英国の海運・物流、メディア・娯楽、技術、自動車組織へ"
                "継続的に侵入したと報告した。攻撃ではANTSword、BLUEBEAM、"
                "DUSTPAN、Cobalt Strike Beacon、DUSTTRAP、SQLULDR2、PINEGROVEを"
                "組み合わせ、長期アクセスとデータ窃取を行った。"
            ),
            "first_observed": time_point(
                "2023-01-01T00:00:00Z", "year", "known", "source-stated"
            ),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2024-07-18T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "analyst_notes": (
                "開始年のみ一次資料が明示するためyear精度とし、公開日を活動終期には"
                "使用していない。国・業種はMandiantが列挙した範囲に限定した。"
            ),
        }
    )
    add_evidence(dust, MANDIANT_APT41_SOURCE["source_id"])
    apt41_specs = (
        ("malware--antsword", "ANTSword", "Web shell used in the sustained APT41 campaign."),
        ("malware--bluebeam", "BLUEBEAM", "Backdoor used in the sustained APT41 campaign."),
        ("malware--dustpan", "DUSTPAN", "In-memory dropper used by APT41."),
        ("malware--dusttrap", "DUSTTRAP", "Modular multi-stage plugin framework used by APT41."),
        ("malware--sqluldr2", "SQLULDR2", "Utility used to export Oracle database content."),
        ("malware--pinegrove", "PINEGROVE", "Command-line OneDrive uploader used for exfiltration."),
    )
    for malware_id, name, description in apt41_specs:
        merge_malware(
            apt41,
            malware_id=malware_id,
            name=name,
            aliases=[],
            platforms=["Windows"],
            description=description,
            first_observed=dust["first_observed"],
            last_observed=dust["last_observed"],
            evidence_refs=[MANDIANT_APT41_SOURCE["source_id"]],
        )
        dust.setdefault("malware_refs", []).append(malware_id)
    dust["malware_refs"] = sorted(set(dust["malware_refs"]))
    add_source_to_linked_victims(apt41, dust, MANDIANT_APT41_SOURCE["source_id"])

    taiwan = find_activity(apt41, "activity--daily-7e72b05415dea6793880")
    taiwan.update(
        {
            "name": "APT41、台湾の政府系研究機関1組織を侵害",
            "description": (
                "Cisco Talosは、2023年7月中旬から台湾の政府関連研究機関1組織で"
                "観測された侵入を、中程度の確度でAPT41へ帰属した。攻撃者は"
                "ShadowPadとCobalt Strikeに加え、Webシェルと独自ツールを使用した。"
                "単一組織の事例であるためIncidentとして保持する。"
            ),
            "first_observed": time_point(
                "2023-07-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2024-08-01T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "medium",
            "stix_object_type": "incident",
            "grouping_context": None,
            "analyst_notes": (
                "Cisco Talosの帰属確度（medium confidence）をそのまま反映。"
                "公開日を侵入終期として扱っていない。"
            ),
        }
    )
    add_evidence(taiwan, CISCO_APT41_TAIWAN_SOURCE["source_id"])
    add_source_to_linked_victims(
        apt41, taiwan, CISCO_APT41_TAIWAN_SOURCE["source_id"]
    )

    merge_source(kimsuky, ZSCALER_TRANSLATEXT_SOURCE)
    translatext = find_activity(kimsuky, "activity--daily-a75732bcf0cbd93ba89d")
    translatext.update(
        {
            "first_observed": time_point(
                "2024-03-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2024-03-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "reported_at": time_point(
                "2024-06-27T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "analyst_notes": (
                "Zscaler一次分析で2024年3月の観測、標的範囲、TRANSLATEXTの"
                "情報窃取機能を確認。3月内の厳密な開始・終了日は未確定。"
            ),
        }
    )
    add_evidence(translatext, ZSCALER_TRANSLATEXT_SOURCE["source_id"])

    for source in (CHECKMARX_MOONSTONE_SOURCE, MICROSOFT_MOONSTONE_SOURCE):
        merge_source(moonstone, source)
    merge_alias(
        moonstone,
        name="Storm-1789",
        vendor="Microsoft Threat Intelligence",
        source_ids=[MICROSOFT_MOONSTONE_SOURCE["source_id"]],
        scope="exact",
        note="Microsoft explicitly states that Moonstone Sleet was formerly Storm-1789.",
    )
    add_relationship(
        moonstone,
        source_slug="moonstone-sleet",
        target_actor="Diamond Sleet",
        relationship_type="overlaps-with",
        description=(
            "Microsoft observed strong initial code and tradecraft overlap with "
            "Diamond Sleet, followed by Moonstone Sleet's shift to its own "
            "infrastructure and concurrent, distinct operations."
        ),
        evidence_refs=[MICROSOFT_MOONSTONE_SOURCE["source_id"]],
        note=(
            "Historical operational overlap only; the source explicitly treats "
            "Moonstone Sleet as a distinct actor, so this is not an exact alias."
        ),
    )
    npm = find_activity(moonstone, "activity--daily-7319b51d47c031c67b7d")
    npm.update(
        {
            "name": "Moonstone Sleet、悪性npmパッケージをLinux対応へ拡張",
            "description": (
                "Checkmarxは、Moonstone Sleetが2024年第1・第2四半期に公開npm"
                "レジストリへ悪性パッケージを継続投入し、第2四半期には難読化と"
                "Linux対応を追加したと報告した。Microsoftも、偽の技術課題として"
                "悪性npmプロジェクトを配布し、SplitLoaderや資格情報窃取へつなげる"
                "活動を観測している。"
            ),
            "first_observed": time_point(
                "2024-01-01T00:00:00Z", "year", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2024-01-01T00:00:00Z", "year", "known", "source-stated"
            ),
            "reported_at": time_point(
                "2024-06-13T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "analyst_notes": (
                "四半期単位の記述を日付へ過剰変換せず、2024年内の活動としてyear精度"
                "で保持。Jade Sleet等の別DPRKクラスタと同一主体とは扱わない。"
            ),
        }
    )
    for source_id in (
        CHECKMARX_MOONSTONE_SOURCE["source_id"],
        MICROSOFT_MOONSTONE_SOURCE["source_id"],
    ):
        add_evidence(npm, source_id)
    fakepenny = find_activity(moonstone, "activity--daily-bf96dfd17fad7ae3914b")
    fakepenny.update(
        {
            "name": "Moonstone Sleet、侵害済み企業へFakePennyランサムウェアを展開",
            "description": (
                "Microsoftは、Moonstone Sleetが2024年2月に侵害した企業へ同年4月、"
                "独自のFakePennyランサムウェアを展開し660万米ドル相当のBitcoinを"
                "要求したと報告した。FakePennyはローダーと暗号化機能で構成され、"
                "Microsoftは金銭目的と評価している。"
            ),
            "first_observed": time_point(
                "2024-04-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2024-04-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "reported_at": time_point(
                "2024-05-28T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "analyst_notes": (
                "ランサムウェア展開月を活動期間とし、先行侵害月はdescriptionへ分離。"
            ),
        }
    )
    add_evidence(fakepenny, MICROSOFT_MOONSTONE_SOURCE["source_id"])
    moonstone_malware = (
        (
            "malware--splitloader",
            "SplitLoader",
            "Multi-stage loader delivered by trojanized PuTTY and malicious npm projects.",
            time_point("2023-08-01T00:00:00Z", "month", "known", "source-stated"),
            time_point(None),
        ),
        (
            "malware--youieload",
            "YouieLoad",
            "Custom in-memory loader delivered with the DeTankWar game.",
            time_point("2024-02-01T00:00:00Z", "month", "known", "source-stated"),
            time_point("2024-05-01T00:00:00Z", "month", "known", "source-stated"),
        ),
        (
            "malware--fakepenny",
            "FakePenny",
            "Custom Moonstone Sleet ransomware composed of a loader and encryptor.",
            fakepenny["first_observed"],
            fakepenny["last_observed"],
        ),
    )
    for malware_id, name, description, first, last in moonstone_malware:
        merge_malware(
            moonstone,
            malware_id=malware_id,
            name=name,
            aliases=[],
            platforms=["Windows"],
            description=description,
            first_observed=first,
            last_observed=last,
            evidence_refs=[MICROSOFT_MOONSTONE_SOURCE["source_id"]],
        )
    npm["malware_refs"] = sorted(set(npm.get("malware_refs", [])) | {"malware--splitloader"})
    fakepenny["malware_refs"] = sorted(
        set(fakepenny.get("malware_refs", [])) | {"malware--fakepenny"}
    )

    merge_source(unc5221, ECLECTICIQ_UNC5221_SOURCE)
    epmm = find_activity(unc5221, "activity--daily-fd8d76592cb438a30641")
    epmm.update(
        {
            "name": "UNC5221、Ivanti EPMM脆弱性チェーンを広域悪用",
            "description": (
                "EclecticIQは、2025年5月15日以降にCVE-2025-4427/4428を連鎖させた"
                "Ivanti EPMM悪用を観測し、高い確度でUNC5221へ帰属した。標的は欧州、"
                "北米、APACの医療、通信、航空、政府、金融に及び、KrustyLoaderを"
                "介してSliverを展開し、AWS S3を配布基盤に使用した。"
            ),
            "first_observed": time_point(
                "2025-05-15T00:00:00Z", "day", "known", "source-stated"
            ),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2025-05-21T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "analyst_notes": (
                "EclecticIQ一次分析の帰属確度と開始日を採用。公開日を活動終期にしない。"
            ),
        }
    )
    add_evidence(epmm, ECLECTICIQ_UNC5221_SOURCE["source_id"])
    for malware_id, name, description in (
        ("malware--krustyloader", "KrustyLoader", "Rust-based loader used to deploy Sliver."),
        ("malware--sliver", "Sliver", "Open-source command-and-control framework deployed after EPMM exploitation."),
    ):
        merge_malware(
            unc5221,
            malware_id=malware_id,
            name=name,
            aliases=[],
            platforms=["Linux"],
            description=description,
            first_observed=epmm["first_observed"],
            last_observed=epmm["last_observed"],
            evidence_refs=[ECLECTICIQ_UNC5221_SOURCE["source_id"]],
        )
        epmm.setdefault("malware_refs", []).append(malware_id)
    epmm["malware_refs"] = sorted(set(epmm["malware_refs"]))
    add_source_to_linked_victims(unc5221, epmm, ECLECTICIQ_UNC5221_SOURCE["source_id"])

    merge_source(unc5820, MANDIANT_UNC5820_SOURCE)
    fortimanager = find_activity(unc5820, "activity--daily-6531aa0646bd2b399aec")
    fortimanager.update(
        {
            "name": "UNC5820、FortiManager 50台超から構成情報を窃取",
            "description": (
                "Mandiantは、UNC5820がCVE-2024-47575を悪用し、50台超のFortiManager"
                "機器を潜在的に侵害したと報告した。2024年6月27日と9月23日に同一"
                "指標の悪用を観測し、管理対象FortiGateの構成とユーザー情報を"
                "圧縮・流出させた。公開時点で横展開の証拠はなく、動機と所在も不明。"
            ),
            "first_observed": time_point(
                "2024-06-27T00:00:00Z", "day", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2024-09-23T00:00:00Z", "day", "known", "source-stated"
            ),
            "reported_at": time_point(
                "2024-10-23T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "analyst_notes": (
                "Mandiantの直接観測日を期間に採用。構成情報の潜在的悪用と、未観測の"
                "横展開を区別し、国家帰属や動機を補完していない。"
            ),
        }
    )
    add_evidence(fortimanager, MANDIANT_UNC5820_SOURCE["source_id"])
    add_source_to_linked_victims(
        unc5820, fortimanager, MANDIANT_UNC5820_SOURCE["source_id"]
    )

    for source in (GTIG_UNC6395_SOURCE, SALESLOFT_INCIDENT_SOURCE):
        merge_source(unc6395, source)
    drift = find_activity(unc6395, "activity--daily-75ed648ec068d5993ef2")
    drift.update(
        {
            "name": "UNC6395、Salesloft Drift侵害から顧客SaaSデータ窃取へ展開",
            "description": (
                "SalesloftとMandiantの調査では、攻撃者が2025年3月22日から9月5日まで"
                "Drift環境へ侵入し、GitHub PATによる偵察・リポジトリ取得、AWS環境への"
                "アクセス、OAuthトークン窃取を行った。GTIGは8月8～18日に盗まれた"
                "トークンでSalesforce顧客データを大量取得した活動をUNC6395として"
                "追跡する。ShinyHuntersやScattered Spiderとの同一性は一次資料が"
                "確定していないため本活動の帰属根拠には用いない。"
            ),
            "first_observed": time_point(
                "2025-03-22T00:00:00Z", "day", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2025-09-05T00:00:00Z", "day", "known", "source-stated"
            ),
            "reported_at": time_point(
                "2025-09-06T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "analyst_notes": (
                "供給元の侵入期間はSalesloft、下流の大量窃取とUNC6395帰属はGTIGを"
                "根拠とする。両資料の観測範囲を分けて記録した。"
            ),
        }
    )
    for source_id in (
        GTIG_UNC6395_SOURCE["source_id"],
        SALESLOFT_INCIDENT_SOURCE["source_id"],
    ):
        add_evidence(drift, source_id)
        add_source_to_linked_victims(unc6395, drift, source_id)
    theft = find_activity(unc6395, "activity--daily-8c3751b2994642569734")
    theft.update(
        {
            "name": "UNC6395、盗難Drift OAuthトークンでSalesforceデータを大量窃取",
            "first_observed": time_point(
                "2025-08-08T00:00:00Z", "day", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2025-08-18T00:00:00Z", "day", "known", "source-stated"
            ),
            "reported_at": time_point(
                "2025-08-26T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "analyst_notes": (
                "GTIGがUNC6395として明示した8月8～18日の下流窃取期間に限定。"
            ),
        }
    )
    add_evidence(theft, GTIG_UNC6395_SOURCE["source_id"])
    add_source_to_linked_victims(unc6395, theft, GTIG_UNC6395_SOURCE["source_id"])


def fix_scattered_spider_primary_boundaries(profile: dict[str, Any]) -> None:
    """Keep confirmed sector activity separate from unconfirmed victim attribution."""

    for source in (
        NCSC_UK_RETAIL_SOURCE,
        MANDIANT_UNC3944_VSPHERE_SOURCE,
        QANTAS_INCIDENT_SOURCE,
        FBI_SCATTERED_SPIDER_SOURCE,
    ):
        merge_source(profile, source)

    alias_note = (
        "The joint advisory and Mandiant describe cross-vendor overlap; retain "
        "separate collection boundaries instead of asserting universal identity."
    )
    for name, vendor in (
        ("UNC3944", "Mandiant / FBI-CISA joint advisory"),
        ("0ktapus", "FBI-CISA joint advisory"),
        ("Scatter Swine", "FBI-CISA joint advisory"),
        ("Muddled Libra", "FBI-CISA joint advisory"),
    ):
        merge_alias(
            profile,
            name=name,
            vendor=vendor,
            source_ids=[
                FBI_SCATTERED_SPIDER_SOURCE["source_id"],
                MANDIANT_UNC3944_VSPHERE_SOURCE["source_id"],
            ],
            scope="overlapping",
            note=alias_note,
        )

    retail = find_activity(profile, "activity--daily-3614985905a497f6500b")
    retail.update(
        {
            "name": "英国小売インシデント群とScattered Spider帰属の未確認関連",
            "description": (
                "2025年4～5月にMarks & Spencer、Co-op、Harrodsなど英国小売業で"
                "インシデントが相次ぎ、報道ではScattered Spiderとの関連が論じられた。"
                "しかし英国NCSCは2025年5月4日時点で、各事案が関連するか、単一の"
                "攻撃者によるものかを判断できないと明記した。従って直接のCampaign"
                "帰属ではなく、後続分析用のGroupingとして保持する。"
            ),
            "reported_at": time_point(
                "2025-05-04T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "low",
            "stix_object_type": "grouping",
            "grouping_context": "suspicious-activity",
            "analyst_notes": (
                "NCSCの否定的境界を優先。企業間の時期・手口の近さは調査リードであり、"
                "Scattered Spiderへの確定帰属または単一キャンペーンの根拠ではない。"
            ),
        }
    )
    add_evidence(retail, NCSC_UK_RETAIL_SOURCE["source_id"])

    aviation = find_activity(profile, "activity--daily-483a8ab1bd549ba753ad")
    profile["victim_cases"] = [
        item
        for item in profile.get("victim_cases", [])
        if aviation["activity_id"] not in item.get("activity_refs", [])
    ]
    aviation.update(
        {
            "name": "UNC3944／Scattered Spider、航空・小売・保険を狙うvSphere侵入",
            "description": (
                "Mandiantは2025年半ば、UNC3944が小売、航空、保険組織を狙った"
                "キャンペーンを実施したと報告した。攻撃者はヘルプデスクへの"
                "ソーシャルエンジニアリングからActive Directory権限を取得し、"
                "VMware vCenter／ESXiへ到達して防御を回避した。MandiantはUNC3944を"
                "Scattered Spider等と重なるクラスタとして扱う。一次資料がこの"
                "キャンペーンの被害者として明示しない企業名は関連づけない。"
            ),
            "first_observed": time_point(
                "2025-01-01T00:00:00Z", "year", "known", "source-stated"
            ),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2025-07-23T00:00:00Z", "day", "known", "source-publication"
            ),
            "victim_refs": [],
            "confidence": "high",
            "analyst_notes": (
                "Mandiantが明示したsector-level campaignのみを採用。WestJet、Hawaiian"
                "等の個別帰属は本一次資料から確定できないため除外した。"
            ),
        }
    )
    add_evidence(aviation, MANDIANT_UNC3944_VSPHERE_SOURCE["source_id"])

    canonical_qantas_id = "activity--daily-bd819e551e72e0636426"
    for duplicate_id in (
        "activity--daily-a97d2692a7a3198fb7f6",
        "activity--daily-ed14eeec16626d49c2e3",
    ):
        remove_activity(profile, duplicate_id)
    qantas = find_activity(profile, canonical_qantas_id)
    qantas.update(
        {
            "name": "Qantas顧客プラットフォーム侵害とScattered Spider帰属の未確認関連",
            "description": (
                "Qantasは2025年7月2日、コールセンターで使用する第三者顧客サービス"
                "基盤への侵入を公表し、約600万件の顧客サービスレコードが存在する"
                "システムへのアクセスを確認した。氏名、メール、電話番号、生年月日、"
                "会員番号等が含まれ得る一方、カード情報、金融情報、パスポート情報、"
                "パスワード、PIN、ログイン情報は含まれないとした。Qantasの一次発表は"
                "攻撃者をScattered Spiderへ帰属していないため、関連候補をGroupingで"
                "保持し、直接のactor-victim関係は作らない。"
            ),
            "first_observed": time_point(None),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2025-07-02T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "low",
            "stix_object_type": "grouping",
            "grouping_context": "suspicious-activity",
            "analyst_notes": (
                "Qantas一次発表はインシデントと影響範囲のみを裏づける。アクター帰属は"
                "二次報道上の調査リードとして残し、確定Incidentとして出力しない。"
            ),
        }
    )
    add_evidence(qantas, QANTAS_INCIDENT_SOURCE["source_id"])
    qantas_victims = [
        item
        for item in profile.get("victim_cases", [])
        if canonical_qantas_id in item.get("activity_refs", [])
    ]
    if qantas_victims:
        victim = qantas_victims[0]
        victim.update(
            {
                "name": "被害事例: Qantas第三者顧客サービス基盤侵害",
                "victim_name": "Qantas",
                "disclosure_status": "named",
                "victim_type": "organization",
                "description": qantas["description"],
                "reported_at": qantas["reported_at"],
                "confidence": "high",
                "evidence_refs": [QANTAS_INCIDENT_SOURCE["source_id"]],
                "analyst_notes": (
                    "被害事象はQantas一次発表で確認。Scattered Spiderへの帰属は"
                    "確認されていないため、被害者オブジェクト自体に帰属を含めない。"
                ),
            }
        )


def fix_react2shell_cluster_boundary(
    unc5174: dict[str, Any], cl_sta_1015: dict[str, Any]
) -> None:
    for profile in (unc5174, cl_sta_1015):
        merge_source(profile, UNIT42_REACT2SHELL_SOURCE)
        merge_source(profile, GTIG_REACT2SHELL_SOURCE)
    alias_note = (
        "Unit 42 writes CL-STA-1015 (aka UNC5174), but this is a cross-vendor "
        "cluster mapping. It is retained as overlapping until scope stability is "
        "independently confirmed."
    )
    merge_alias(
        unc5174,
        name="CL-STA-1015",
        vendor="Palo Alto Networks Unit 42",
        source_ids=[UNIT42_REACT2SHELL_SOURCE["source_id"]],
        scope="overlapping",
        note=alias_note,
    )
    merge_alias(
        cl_sta_1015,
        name="UNC5174",
        vendor="Palo Alto Networks Unit 42 / Google Threat Intelligence Group",
        source_ids=[UNIT42_REACT2SHELL_SOURCE["source_id"]],
        scope="overlapping",
        note=alias_note,
    )
    relationship_description = (
        "Unit 42 maps its CL-STA-1015 activity cluster to UNC5174; the mapping is "
        "preserved as a cross-taxonomy overlap rather than a global exact identity."
    )
    for profile, slug, target in (
        (unc5174, "unc5174", "CL-STA-1015"),
        (cl_sta_1015, "cl-sta-1015", "UNC5174"),
    ):
        add_relationship(
            profile,
            source_slug=slug,
            target_actor=target,
            relationship_type="taxonomy-overlaps-with",
            description=relationship_description,
            evidence_refs=[UNIT42_REACT2SHELL_SOURCE["source_id"]],
            note=alias_note,
            confidence="medium",
        )
        boundary = (
            "React2Shell reporting contains multiple actor clusters. Unit 42 maps "
            "CL-STA-1015 to UNC5174, while GTIG separately tracks a SNOWLIGHT-using "
            "cluster as UNC6586; malware reuse alone must not merge those clusters."
        )
        if boundary not in profile["assessment"].setdefault("uncertainties", []):
            profile["assessment"]["uncertainties"].append(boundary)

    react = find_activity(unc5174, "activity--daily-cdb2b24b57d09645a48d")
    unc5174["victim_cases"] = [
        item
        for item in unc5174.get("victim_cases", [])
        if react["activity_id"] not in item.get("activity_refs", [])
    ]
    react.update(
        {
            "name": "CL-STA-1015／UNC5174と整合するReact2Shell後続活動",
            "description": (
                "Unit 42はReact2Shell（CVE-2025-55182）悪用後、CL-STA-1015と"
                "高い確度で整合する活動を観測した。攻撃者はcurl/wgetでsltシェル"
                "スクリプトをファイルレス実行し、SNOWLIGHTとVShellを展開した。"
                "React2Shell全体の侵害数や脆弱ホスト数は複数主体を含むため、この"
                "クラスタ固有の被害数・標的としては記録しない。"
            ),
            "first_observed": time_point(None),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2025-12-12T00:00:00Z", "day", "known", "source-publication"
            ),
            "target_refs": [],
            "victim_refs": [],
            "confidence": "medium",
            "stix_object_type": "grouping",
            "grouping_context": "suspicious-activity",
            "analyst_notes": (
                "Unit 42の直接観測は強いが、広域スキャン・30組織侵害・7.7万IP等を"
                "UNC5174単独へ割り当てる根拠はない。GTIGの別クラスタUNC6586も考慮。"
            ),
        }
    )
    for source_id in (
        UNIT42_REACT2SHELL_SOURCE["source_id"],
        GTIG_REACT2SHELL_SOURCE["source_id"],
    ):
        add_evidence(react, source_id)
    for malware_id, name, description in (
        ("malware--snowlight", "SNOWLIGHT", "Linux dropper used to retrieve follow-on malware including VShell."),
        ("malware--vshell", "VShell", "Remote access trojan deployed after SNOWLIGHT."),
    ):
        merge_malware(
            unc5174,
            malware_id=malware_id,
            name=name,
            aliases=[],
            platforms=["Linux"],
            description=description,
            first_observed=time_point(None),
            last_observed=time_point(None),
            evidence_refs=[UNIT42_REACT2SHELL_SOURCE["source_id"]],
        )
        react.setdefault("malware_refs", []).append(malware_id)
    react["malware_refs"] = sorted(set(react["malware_refs"]))


def fix_new_actor_links_and_activity(
    breeze: dict[str, Any],
    storm1849: dict[str, Any],
    storm2603: dict[str, Any],
    zirconium: dict[str, Any],
) -> None:
    """Add current primary-source activity and explicit cross-taxonomy links."""

    breeze_source_id = "source--breeze-comet--gtig-brazil-2026"
    for target in ("Plump Spider", "SHADOW-AETHER-064"):
        add_relationship(
            breeze,
            source_slug="breeze-comet",
            target_actor=target,
            relationship_type="overlaps-with",
            description=(
                "GTIG states that BREEZE COMET activity overlaps operations "
                f"publicly reported as {target}."
            ),
            evidence_refs=[breeze_source_id],
            note=(
                "Operational overlap only; the cited primary source does not "
                "establish exact actor identity and the original external report "
                "has not been independently verified."
            ),
            confidence="medium",
        )
    for source in breeze.get("sources", []):
        if source.get("source_id") == breeze_source_id:
            source["actor_scope"] = "direct"
            source["claims_supported"] = sorted(
                set(source.get("claims_supported", []))
                | {"activity", "identity", "alias", "relationship", "capability", "targeting", "ttp", "ioc"}
            )

    for source in (CISCO_ARCANEDOOR_SOURCE, CISCO_FIRESTARTER_SOURCE):
        merge_source(storm1849, source)
    merge_alias(
        storm1849,
        name="UAT4356",
        vendor="Cisco Talos / Microsoft Threat Intelligence",
        source_ids=[CISCO_ARCANEDOOR_SOURCE["source_id"]],
        scope="exact",
        note=(
            "Cisco states that the actor it tracks as UAT4356 is tracked by "
            "Microsoft as Storm-1849. Exactness is scoped to that explicit mapping."
        ),
    )
    arcanedoor = find_activity(storm1849, "activity--daily-1baaec4e789e123f6605")
    arcanedoor.update(
        {
            "name": "UAT4356／Storm-1849によるArcaneDoor作戦",
            "description": (
                "Cisco Talosは、UAT4356（Microsoft: Storm-1849）が世界各地の政府"
                "ネットワークにあるCisco ASAを狙った諜報作戦ArcaneDoorを報告した。"
                "主活動は2023年12月～2024年1月で、Line DancerとLine Runnerを用いて"
                "設定変更、偵察、通信取得・流出、永続化を行った。"
            ),
            "first_observed": time_point(
                "2023-12-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2024-01-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "reported_at": time_point(
                "2024-04-24T00:00:00Z", "day", "known", "source-publication"
            ),
            "confidence": "high",
            "analyst_notes": (
                "Cisco一次分析が明示する主活動期間と高確度の国家支援評価を採用。"
            ),
        }
    )
    add_evidence(arcanedoor, CISCO_ARCANEDOOR_SOURCE["source_id"])
    for malware_id, name, description in (
        ("malware--line-dancer", "Line Dancer", "Memory-resident shellcode interpreter used on Cisco ASA devices."),
        ("malware--line-runner", "Line Runner", "Persistent Lua-based backdoor used on Cisco ASA devices."),
    ):
        merge_malware(
            storm1849,
            malware_id=malware_id,
            name=name,
            aliases=[],
            platforms=["Network Device"],
            description=description,
            first_observed=arcanedoor["first_observed"],
            last_observed=arcanedoor["last_observed"],
            evidence_refs=[CISCO_ARCANEDOOR_SOURCE["source_id"]],
        )
        arcanedoor.setdefault("malware_refs", []).append(malware_id)
    arcanedoor["malware_refs"] = sorted(set(arcanedoor["malware_refs"]))

    firestarter_id = "activity--storm-1849--firestarter-2026"
    firestarter = {
        "activity_id": firestarter_id,
        "name": "UAT4356、Cisco FirepowerへFIRESTARTERを展開",
        "activity_type": "malware-campaign",
        "first_observed": time_point(None),
        "last_observed": time_point(None),
        "reported_at": time_point(
            "2026-04-23T00:00:00Z", "day", "known", "source-publication"
        ),
        "description": (
            "Cisco Talosは、UAT4356がCisco Firepower/FXOS機器を継続的に標的とし、"
            "CVE-2025-20333とCVE-2025-20362を悪用して独自バックドアFIRESTARTERを"
            "展開したと報告した。FIRESTARTERはLINAプロセス内で任意コードを実行し、"
            "CSP_MOUNT_LISTを改変して再起動をまたぐ永続化を行う。"
        ),
        "target_refs": [],
        "malware_refs": ["malware--firestarter"],
        "infrastructure_refs": [],
        "confidence": "high",
        "evidence_refs": [CISCO_FIRESTARTER_SOURCE["source_id"]],
        "analyst_notes": (
            "Ciscoはcontinued active targetingとするが観測開始・終了日は明示しないため"
            "期間はunknown、公開日はreported_atにのみ設定した。"
        ),
        "ttp_refs": [],
        "victim_refs": [],
        "stix_object_type": "campaign",
        "activity_refs": [],
        "grouping_context": None,
    }
    upsert_activity(storm1849, firestarter)
    merge_malware(
        storm1849,
        malware_id="malware--firestarter",
        name="FIRESTARTER",
        aliases=[],
        platforms=["Network Device"],
        description=(
            "Custom UAT4356 backdoor executing inside Cisco LINA and persisting "
            "through CSP_MOUNT_LIST manipulation."
        ),
        first_observed=time_point(None),
        last_observed=time_point(None),
        evidence_refs=[CISCO_FIRESTARTER_SOURCE["source_id"]],
    )

    for source in (MICROSOFT_TOOLSHELL_SOURCE, MICROSOFT_STORM2603_PARALLEL_SOURCE):
        merge_source(storm2603, source)
    toolshell = migrate_profile_activity_id(
        storm2603,
        STORM2603_TOOLSHELL_LEGACY_ACTIVITY_ID,
        STORM2603_TOOLSHELL_ACTIVITY_ID,
    )
    if toolshell is None:
        known_tool_ids = {
            item.get("id")
            for item in storm2603.get("capabilities", {}).get("tools", [])
        }
        known_ttp_ids = {
            item.get("ttp_id") for item in storm2603.get("ttps", [])
        }
        toolshell = {
            "activity_id": STORM2603_TOOLSHELL_ACTIVITY_ID,
            "activity_type": "ransomware-extortion",
            "stix_object_type": "campaign",
            "grouping_context": None,
            "activity_refs": [],
            "target_refs": [],
            "malware_refs": [],
            "tool_refs": sorted(
                known_tool_ids
                & {
                    "tool--storm-2603-mimikatz",
                    "tool--storm-2603-psexec",
                    "tool--storm-2603-impacket",
                }
            ),
            "infrastructure_refs": [
                "infrastructure--storm-2603-post-exploitation-c2",
                "infrastructure--storm-2603-updatemicfosoft-c2",
            ],
            "ttp_refs": sorted(
                known_ttp_ids
                & {
                    "ttp--storm-2603-toolshell-credential-dumping",
                    "ttp--storm-2603-toolshell-service-execution",
                    "ttp--storm-2603-toolshell-domain-policy",
                    "ttp--storm-2603-toolshell-encryption-impact",
                }
            ),
            "victim_refs": [],
            "evidence_refs": [],
        }
        storm2603.setdefault("activities", []).append(toolshell)
    storm2603["victim_cases"] = [
        item
        for item in storm2603.get("victim_cases", [])
        if toolshell["activity_id"] not in item.get("activity_refs", [])
    ]
    toolshell.update(
        {
            "activity_id": STORM2603_TOOLSHELL_ACTIVITY_ID,
            "name": "Storm-2603、ToolShell悪用後にWarlockランサムウェアを展開",
            "description": (
                "Microsoftは、Storm-2603が2025年7月18日以降、オンプレミス"
                "SharePointのToolShell脆弱性を悪用し、MimikatzやPsExecで横展開後、"
                "グループポリシーでWarlockランサムウェアを展開したと報告した。"
                "同時期にはLinen TyphoonとViolet Typhoonも別個に悪用しており、"
                "個別被害組織をStorm-2603へ一括帰属しない。"
            ),
            "first_observed": time_point(
                "2025-07-18T00:00:00Z", "day", "known", "source-stated"
            ),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2025-07-22T00:00:00Z", "day", "known", "source-publication"
            ),
            "target_refs": [],
            "victim_refs": [],
            "confidence": "high",
            "activity_type": "ransomware-extortion",
            "stix_object_type": "campaign",
            "grouping_context": None,
            "activity_refs": [],
            "infrastructure_refs": [
                "infrastructure--storm-2603-post-exploitation-c2",
                "infrastructure--storm-2603-updatemicfosoft-c2",
            ],
            "analyst_notes": (
                "MicrosoftがStorm-2603固有として記述した侵入チェーンだけを保持。"
                "NNSAその他の個別被害者は同クラスタへの帰属が明示されないため除外。"
            ),
        }
    )
    toolshell["evidence_refs"] = [MICROSOFT_TOOLSHELL_SOURCE["source_id"]]
    remove_activity(storm2603, "activity--daily-aacbe5410f1223b930a5")
    remove_activity(storm2603, "activity--daily-e8fd6208405a17b2c79d")
    retained_profile = {
        key: value for key, value in storm2603.items() if key != "sources"
    }

    def references_superseded_source(value: Any, source_id: str) -> bool:
        if isinstance(value, dict):
            return any(
                references_superseded_source(item, source_id)
                for item in value.values()
            )
        if isinstance(value, list):
            return any(
                references_superseded_source(item, source_id) for item in value
            )
        return value == source_id

    storm2603["sources"] = [
        source
        for source in storm2603.get("sources", [])
        if source.get("source_id") not in STORM2603_SUPERSEDED_SOURCE_IDS
        or references_superseded_source(
            retained_profile, source.get("source_id", "")
        )
    ]
    merge_malware(
        storm2603,
        malware_id="malware--warlock-ransomware",
        name="Warlock ransomware",
        aliases=["Warlock"],
        platforms=["Windows"],
        description="Ransomware deployed by Storm-2603 after ToolShell exploitation.",
        first_observed=toolshell["first_observed"],
        last_observed=toolshell["last_observed"],
        evidence_refs=[MICROSOFT_TOOLSHELL_SOURCE["source_id"]],
    )
    toolshell["malware_refs"] = sorted(
        set(toolshell.get("malware_refs", [])) | {"malware--warlock-ransomware"}
    )
    parallel_id = "activity--storm-2603--parallel-intrusion-2026"
    parallel_tool_ids = {
        "tool--storm-2603-velociraptor",
        "tool--storm-2603-cloudflare-tunnel",
        "tool--zoho-assist-unattended-agent",
        "tool--storm-2603-vscode-remote-ssh",
    }
    known_parallel_tool_ids = {
        item.get("id")
        for item in storm2603.get("capabilities", {}).get("tools", [])
    } & parallel_tool_ids
    parallel_ttp_ids = {
        item.get("ttp_id")
        for item in storm2603.get("ttps", [])
        if parallel_id in item.get("activity_refs", [])
    }
    upsert_activity(
        storm2603,
        {
            "activity_id": parallel_id,
            "name": "Storm-2603と無関係な第2主体が同居した並行侵入事例",
            "activity_type": "intrusion",
            "first_observed": time_point(None),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2026-06-22T00:00:00Z", "day", "known", "source-publication"
            ),
            "description": (
                "Microsoft DARTは、一つの被害環境でStorm-2603と無関係な第2主体が"
                "並行して活動した事例を報告した。Storm-2603側はSharePointを探索し、"
                "Velociraptor、Cloudflare Tunnel、Zoho Assist、VS Code経由SSHなどを"
                "用いて権限・永続性・遠隔アクセスを確保した。別主体のDLLサイド"
                "ローディングや独自バックドアはStorm-2603の能力として扱わない。"
            ),
            "target_refs": [],
            "malware_refs": [],
            "tool_refs": sorted(known_parallel_tool_ids),
            "infrastructure_refs": [],
            "confidence": "high",
            "evidence_refs": [MICROSOFT_STORM2603_PARALLEL_SOURCE["source_id"]],
            "analyst_notes": (
                "同一被害環境と時間的重複はactor relationshipを意味しない。"
                "Microsoftがunrelatedと明記した境界を保持する。"
            ),
            "ttp_refs": sorted(parallel_ttp_ids),
            "victim_refs": [],
            "stix_object_type": "incident",
            "activity_refs": [],
            "grouping_context": None,
        },
    )

    merge_source(zirconium, MICROSOFT_TOOLSHELL_SOURCE)
    remove_activity(zirconium, "activity--daily-f8164c2182ec1f2d8e79")
    violet = find_activity(zirconium, "activity--daily-f1508e67055f2e956163")
    zirconium["victim_cases"] = [
        item
        for item in zirconium.get("victim_cases", [])
        if violet["activity_id"] not in item.get("activity_refs", [])
    ]
    violet.update(
        {
            "name": "Violet Typhoon、オンプレミスSharePointのToolShellを悪用",
            "description": (
                "Microsoftは、Violet Typhoon（ZIRCONIUM/APT31）が2025年7月7日頃から"
                "オンプレミスSharePointの脆弱性を悪用したと報告した。同じ脆弱性は"
                "Linen TyphoonとStorm-2603にも別個に悪用されており、NNSAを含む"
                "個別被害組織をViolet Typhoonへ一括帰属する根拠は示されていない。"
            ),
            "first_observed": time_point(
                "2025-07-07T00:00:00Z", "day", "known", "source-stated"
            ),
            "last_observed": time_point(None),
            "reported_at": time_point(
                "2025-07-22T00:00:00Z", "day", "known", "source-publication"
            ),
            "target_refs": [],
            "victim_refs": [],
            "confidence": "high",
            "evidence_refs": [MICROSOFT_TOOLSHELL_SOURCE["source_id"]],
            "analyst_notes": (
                "MicrosoftがViolet Typhoonへ帰属した活動範囲に限定。複数主体が同じ"
                "脆弱性を悪用したため、共通IOCだけで各被害を再帰属しない。"
            ),
        }
    )


def update_daily_review_state(profiles_root: Path, decisions_path: Path) -> None:
    ledger_path = profiles_root / "vanilla-tempest" / "daily-observations.json"
    ledger = load_json(ledger_path)
    note = (
        "一次資料再検証: 記事の主題・妨害対象はFox Tempestであり、Vanilla Tempestは"
        "同サービスの利用者として事例節に登場する。Fox Tempestのサービス運営・"
        "妨害をVanilla Tempest自身の独立活動として扱うのは主体誤認となるため不採用。"
        "Vanilla Tempestの署名済み偽Teams攻撃は既存活動へ一次資料を統合した。"
    )
    for record in ledger.get("records", []):
        if record.get("record_id") == "daily-record--c535922b3c89d69acd5cd17a":
            record["review_status"] = "rejected"
            record["suggested_action"] = "reject"
            record["confidence"] = "high"
            record["review_notes"] = note
            record["activity_claim"] = {
                "assessment": "non-subject",
                "actor_role": "service-customer",
                "match_location": "body",
                "evidence_text": (
                    "Microsoft says Fox Tempest operated the MSaaS and Vanilla "
                    "Tempest was one customer using Fox Tempest-signed malware."
                ),
                "reasons": ["記事主題のFox Tempestとサービス利用者を分離"],
                "suggested_confidence": "high",
            }
    ledger["updated_at"] = utc_now()
    write_json_atomic(ledger_path, ledger)

    decisions = load_json(decisions_path)
    key = (
        "vanilla-tempest|https://www.microsoft.com/en-us/security/blog/2026/05/19/"
        "exposing-fox-tempest-a-malware-signing-service-operation/"
    )
    decisions[key] = {
        "confidence": "high",
        "review_notes": note,
        "review_status": "rejected",
    }

    storm_ledger_path = profiles_root / "storm-2603" / "daily-observations.json"
    storm_ledger = load_json(storm_ledger_path)
    superseded_storm_notes = {
        (
            "https://www.bleepingcomputer.com/news/security/"
            "microsoft-sharepoint-servers-also-targeted-in-ransomware-attacks/"
        ): (
            "Microsoft一次資料に基づくstable ToolShell activityへ置換済みのため不採用。"
            "この記事は二次報道であり、同時期の複数主体・個別被害・Warlock展開を一つの"
            "Storm-2603 activityへ混在させない。一次資料がStorm-2603固有に記述した侵入"
            "チェーンだけをcurated activityで保持する。"
        ),
        (
            "https://www.bleepingcomputer.com/news/security/"
            "ransomware-gangs-join-attacks-targeting-microsoft-sharepoint-servers/"
        ): (
            "Microsoft一次資料に基づくstable ToolShell activityへ置換済みのため不採用。"
            "この記事は複数の国家系主体とランサムウェア主体を集約した二次報道であり、"
            "共有脆弱性や被害集計からStorm-2603固有の活動・動機・被害者を拡張しない。"
        ),
        (
            "https://www.bleepingcomputer.com/news/security/"
            "us-nuclear-weapons-agency-hacked-in-microsoft-sharepoint-attacks/"
        ): (
            "Microsoft一次資料に基づくstable ToolShell activityへ置換済みのため不採用。"
            "二次報道が列挙するNNSAその他の個別被害はStorm-2603へ個別帰属されていない"
            "ため、Storm-2603 activityのvictim/target根拠として取り込まない。"
        ),
    }
    for reference, rejection_note in superseded_storm_notes.items():
        decisions.setdefault(f"storm-2603|{reference}", {}).update(
            {
                "confidence": "medium",
                "review_notes": rejection_note,
                "review_status": "rejected",
            }
        )
    for record in storm_ledger.get("records", []):
        reference = record.get("activity", {}).get("activity_reference", "")
        if reference not in superseded_storm_notes:
            continue
        decision = decisions[f"storm-2603|{reference}"]
        record["review_status"] = "rejected"
        record["suggested_action"] = "reject"
        record["confidence"] = decision.get("confidence", "medium")
        record["review_notes"] = decision["review_notes"]
    storm_ledger["updated_at"] = utc_now()
    write_json_atomic(storm_ledger_path, storm_ledger)

    apt37_title = "APT37、侵害端末のKメッセンジャーからHWP／LNKとRoKRATを拡散"
    apt37_summary = (
        "Genians Security Centerは、APT37が2024年11月13日に韓国のKメッセンジャー"
        "団体チャットへ悪性HWP文書とZIP内のLNKを時間差で配布した活動を分析した。"
        "初期スピアフィッシング後に侵害端末で偵察・探索を行い、ログイン中の"
        "メッセンジャーを追加配布経路として悪用した。HWPのOLEとLNK内PowerShellから"
        "ファイルレスで実行されるペイロードは、APT37のRoKRAT系列と特定された。"
    )
    apt37_period = {
        "first_observed": time_point(
            "2024-11-13T00:00:00Z", "day", "known", "Genians: K-messenger delivery"
        ),
        "last_observed": time_point(
            "2024-11-13T00:00:00Z", "day", "known", "Genians: K-messenger delivery"
        ),
    }
    apt37_note = (
        "一次資料再検証: 日次記事の見出しと主題は別クラスタContagious Interviewの"
        "FERRET活動で、APT37は末尾の独立したニュース項目にだけ登場する。そのため"
        "activity_overridesで、GeniansがAPT37へ直接帰属した2024-11-13のKメッセンジャー"
        "経由HWP/LNK・RoKRAT活動へ限定した。"
    )
    apt37_ledger_path = profiles_root / "apt37" / "daily-observations.json"
    apt37_ledger = load_json(apt37_ledger_path)
    for record in apt37_ledger.get("records", []):
        if record.get("record_id") != "daily-record--c093c6edea29f9fcc0ac9209":
            continue
        record["activity"]["title"] = apt37_title
        record["activity"]["summary"] = apt37_summary
        record["activity"]["primary_url"] = GENIANS_APT37_SOURCE["url"]
        record["activity_period"] = apt37_period
        record["confidence"] = "high"
        record["review_notes"] = apt37_note
        record["activity_claim"] = {
            "assessment": "strong-subject",
            "actor_role": "operator",
            "match_location": "primary-report",
            "evidence_text": (
                "Genians: HWP, LNK 악성코드를 활용한 APT37 그룹의 집요한 공격 전술 분석"
            ),
            "reasons": ["APT37固有の一次分析へ活動表示を限定"],
            "suggested_confidence": "high",
        }
        primary = {
            "url": GENIANS_APT37_SOURCE["url"],
            "source_type": "primary-report",
        }
        if primary["url"] not in {item.get("url") for item in record.get("sources", [])}:
            record.setdefault("sources", []).append(primary)
    apt37_ledger["updated_at"] = utc_now()
    write_json_atomic(apt37_ledger_path, apt37_ledger)
    decisions[
        "apt37|https://thehackernews.com/2025/02/north-korean-hackers-deploy-ferret.html"
    ] = {
        "review_status": "approved",
        "confidence": "high",
        "activity_overrides": {"title": apt37_title, "summary": apt37_summary},
        "activity_period": apt37_period,
        "review_notes": apt37_note,
    }

    aws_period = {
        "first_observed": time_point(
            "2025-03-01T00:00:00Z",
            "month",
            "known",
            "AWS: typo-crypto compromise in March 2025",
        ),
        "last_observed": time_point(
            "2026-03-01T00:00:00Z",
            "month",
            "known",
            "AWS: axios compromise in March 2026",
        ),
    }
    aws_note = (
        "AWS一次資料を再確認。公開日は2026-07-29。typo-crypto（2025-03）、debug/chalk"
        "（2025-09）、axios（2026-03）を同一DPRK系アクターへmedium confidenceで帰属する。"
        "本文の名称はSAPPHIRE SLEET等でAPT38表記はないため、MITRE G0082を介した"
        "overlappingスコープとして保持し完全同一とは断定しない。"
    )
    apt38_ledger_path = profiles_root / "apt38" / "daily-observations.json"
    apt38_ledger = load_json(apt38_ledger_path)
    for record in apt38_ledger.get("records", []):
        if record.get("record_id") != "daily-record--e7e43253a3ee354a756068f0":
            continue
        record["activity"]["title"] = (
            "Sapphire Sleet系クラスタ、npmパッケージのサプライチェーンを侵害"
        )
        record["activity"]["primary_url"] = (
            "https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-"
            "hacker-group-behind-open-source-supply-chain-attacks/"
        )
        record["activity_period"] = aws_period
        record["review_notes"] = aws_note
    apt38_ledger["updated_at"] = utc_now()
    write_json_atomic(apt38_ledger_path, apt38_ledger)
    aws_key = (
        "apt38|https://aws.amazon.com/jp/blogs/security/amazon-identifies-north-korean-"
        "hacker-group-behind-open-source-supply-chain-attacks/"
    )
    aws_decision = decisions[aws_key]
    aws_decision["activity_overrides"] = {
        "title": "Sapphire Sleet系クラスタ、npmパッケージのサプライチェーンを侵害",
        "summary": next(
            record["activity"]["summary"]
            for record in apt38_ledger["records"]
            if record["record_id"] == "daily-record--e7e43253a3ee354a756068f0"
        ),
    }
    aws_decision["activity_period"] = aws_period
    aws_decision["review_notes"] = aws_note

    water_title = "Water Galuraが運営するQilin RaaS、被害者への法的圧力機能を追加"
    water_summary = (
        "Water Galuraが運営するQilin RaaSは、アフィリエイト向けパネルへ被害者に"
        "支払い圧力をかける「Call Lawyer」機能を追加した。公開集計ではQilinの被害"
        "主張が2025年4月に72件、5月に55件確認され、Rust/C製ペイロード、ネットワーク"
        "拡散、ログ消去、交渉自動化、DDoS、スパム、データ保管などを提供するサービス"
        "として報告された。QilinはRaaS／ランサムウェア名であり、Water Galuraの"
        "無条件な別名としては扱わない。"
    )
    water_period = {
        "first_observed": time_point(
            "2025-04-01T00:00:00Z", "month", "known", "source-stated victim count"
        ),
        "last_observed": time_point(
            "2025-05-01T00:00:00Z", "month", "known", "source-stated victim count"
        ),
    }
    water_note = (
        "entity境界を再検証。The Hacker NewsはQilinグループをWater Galuraとも表記するが、"
        "MITRE ATT&CK G1050/S1242はWater Galura（GOLD FEATHER）を運営者、Qilinを"
        "RaaS softwareとして分離する。activity_overridesもこの区別に合わせた。"
    )
    water_ledger_path = profiles_root / "water-galura" / "daily-observations.json"
    water_ledger = load_json(water_ledger_path)
    for record in water_ledger.get("records", []):
        if record.get("record_id") != "daily-record--e30bc3c3abfd77cddd949226":
            continue
        record["activity"]["title"] = water_title
        record["activity"]["summary"] = water_summary
        record["activity_period"] = water_period
        record["review_notes"] = water_note
        record["activity_claim"] = {
            "assessment": "strong-subject",
            "actor_role": "raas-operator",
            "match_location": "body",
            "evidence_text": (
                "MITRE ATT&CK: Water Galura are the operators of the Qilin RaaS."
            ),
            "reasons": ["運営者Water GaluraとSoftware Qilinを分離"],
            "suggested_confidence": "medium",
        }
    water_ledger["updated_at"] = utc_now()
    write_json_atomic(water_ledger_path, water_ledger)
    decisions[
        "water-galura|https://thehackernews.com/2025/06/"
        "qilin-ransomware-adds-call-lawyer.html"
    ] = {
        "review_status": "approved",
        "confidence": "medium",
        "activity_overrides": {"title": water_title, "summary": water_summary},
        "activity_period": water_period,
        "review_notes": water_note,
    }

    unc6040_title = "UNC6040、vishingでSalesforce接続アプリを承認させデータを窃取"
    unc6040_summary = (
        "GTIGは、UNC6040がITサポートを装った音声フィッシングで従業員を誘導し、"
        "攻撃者管理のSalesforce接続アプリを承認させてCRMデータを窃取したと報告した。"
        "GTIGは初期侵入・窃取をUNC6040、後続のShinyHunters名義の恐喝をUNC6240として"
        "分けて追跡し、提携の可能性は示すが同一主体とは断定していない。"
    )
    unc6040_period = {
        "first_observed": time_point(None),
        "last_observed": time_point(None),
    }
    unc6040_note = (
        "GTIG一次資料で再検証。Salesforceへの音声フィッシングとデータ窃取はUNC6040、"
        "後続のShinyHunters名義の恐喝はUNC6240として別々に追跡されている。"
        "二次記事の『ShinyHunters(UNC6040)』という同一視を除去し、活動期間は推測しない。"
    )
    unc6040_ledger_path = profiles_root / "unc6040" / "daily-observations.json"
    unc6040_ledger = load_json(unc6040_ledger_path)
    for record in unc6040_ledger.get("records", []):
        if record.get("record_id") != "daily-record--dcc1e326e606705f98d43595":
            continue
        record["activity"]["title"] = unc6040_title
        record["activity"]["summary"] = unc6040_summary
        record["activity"]["primary_url"] = GTIG_UNC6040_SOURCE["url"]
        record["activity_period"] = unc6040_period
        record["confidence"] = "high"
        record["review_notes"] = unc6040_note
        record["activity_claim"] = {
            "assessment": "strong-subject",
            "actor_role": "initial-access-and-data-theft-operator",
            "match_location": "primary-report",
            "evidence_text": (
                "GTIG tracks UNC6040 as the actor conducting Salesforce vishing "
                "and initial data theft, separately from UNC6240 extortion."
            ),
            "reasons": ["UNC6040とUNC6240の追跡境界を一次資料に合わせて保持"],
            "suggested_confidence": "high",
        }
        primary = {
            "url": GTIG_UNC6040_SOURCE["url"],
            "source_type": "primary-report",
        }
        if primary["url"] not in {item.get("url") for item in record.get("sources", [])}:
            record.setdefault("sources", []).append(primary)
    unc6040_ledger["updated_at"] = utc_now()
    write_json_atomic(unc6040_ledger_path, unc6040_ledger)
    decisions[
        "unc6040|https://www.bleepingcomputer.com/news/security/"
        "shinyhunters-behind-salesforce-data-theft-attacks-at-qantas-allianz-life-and-lvmh/"
    ] = {
        "review_status": "approved",
        "confidence": "high",
        "activity_overrides": {
            "title": unc6040_title,
            "summary": unc6040_summary,
            "primary_url": GTIG_UNC6040_SOURCE["url"],
        },
        "activity_period": unc6040_period,
        "review_notes": unc6040_note,
    }

    unc6671_title = "UNC6671、vishingでSSO資格情報を窃取しSaaSデータを流出"
    unc6671_summary = (
        "Mandiantは、UNC6671が2026年1月初旬からIT担当者を装って電話し、偽の認証"
        "サイトでSSO資格情報とMFAコードを窃取したと報告した。侵入後はOktaから"
        "SharePointとOneDriveへアクセスした。手口はUNC6661と類似するが、後続の恐喝は"
        "ShinyHunters名義ではなく異なるTox IDを使い、別の人物が関与する可能性がある。"
    )
    unc6671_period = {
        "first_observed": time_point(
            "2026-01-01T00:00:00Z", "month", "known", "source-stated"
        ),
        "last_observed": time_point(None),
    }
    unc6671_note = (
        "Mandiant/GTIG一次資料で再検証。UNC6661、UNC6671、UNC6240は提携・なりすましの"
        "可能性を残す別クラスタとして追跡される。UNC6671固有の侵入と、ブランドなしの"
        "後続恐喝だけに表示を限定した。"
    )
    unc6671_ledger_path = profiles_root / "unc6671" / "daily-observations.json"
    unc6671_ledger = load_json(unc6671_ledger_path)
    for record in unc6671_ledger.get("records", []):
        if record.get("record_id") != "daily-record--0697f946d4469dc9883a5c9a":
            continue
        record["activity"]["title"] = unc6671_title
        record["activity"]["summary"] = unc6671_summary
        record["activity"]["primary_url"] = GTIG_UNC6671_SOURCE["url"]
        record["activity_period"] = unc6671_period
        record["confidence"] = "high"
        record["review_notes"] = unc6671_note
        record["activity_claim"] = {
            "assessment": "strong-subject",
            "actor_role": "operator",
            "match_location": "primary-report",
            "evidence_text": (
                "Mandiant separately tracks UNC6671's January 2026 SSO and SaaS "
                "data-theft intrusion and its unbranded follow-on extortion."
            ),
            "reasons": ["ShinyHunters傘下名称ではなくUNC6671固有の活動へ限定"],
            "suggested_confidence": "high",
        }
        primary = {
            "url": GTIG_UNC6671_SOURCE["url"],
            "source_type": "primary-report",
        }
        if primary["url"] not in {item.get("url") for item in record.get("sources", [])}:
            record.setdefault("sources", []).append(primary)
    unc6671_ledger["updated_at"] = utc_now()
    write_json_atomic(unc6671_ledger_path, unc6671_ledger)
    decisions[
        "unc6671|https://www.bleepingcomputer.com/news/security/"
        "mandiant-details-how-shinyhunters-abuse-sso-to-steal-cloud-data/"
    ] = {
        "review_status": "approved",
        "confidence": "high",
        "activity_overrides": {
            "title": unc6671_title,
            "summary": unc6671_summary,
            "primary_url": GTIG_UNC6671_SOURCE["url"],
        },
        "activity_period": unc6671_period,
        "review_notes": unc6671_note,
    }

    unc2286_note = (
        "一次資料再検証: Cisco TalosはJumbledPath活動をSalt Typhoonへ帰属するがUNC2286を"
        "使用していない。共同CISA勧告もベンダー名は一対一対応しない場合があると明記し、"
        "UNC2286を列挙していない。二次記事だけの別名主張を根拠に活動を複製しない。"
    )
    unc2286_ledger_path = profiles_root / "unc2286" / "daily-observations.json"
    unc2286_ledger = load_json(unc2286_ledger_path)
    for record in unc2286_ledger.get("records", []):
        if record.get("record_id") != "daily-record--2c3e99f982af03e6e5abbb47":
            continue
        record["review_status"] = "rejected"
        record["suggested_action"] = "reject"
        record["confidence"] = "medium"
        record["review_notes"] = unc2286_note
        record["activity_claim"] = {
            "assessment": "non-subject",
            "actor_role": "taxonomy-reference",
            "match_location": "secondary-report",
            "evidence_text": (
                "The secondary article calls UNC2286 an alias; the cited Cisco "
                "primary report attributes the activity only to Salt Typhoon."
            ),
            "reasons": ["一次資料でUNC2286への活動帰属を確認できない"],
            "suggested_confidence": "medium",
        }
    unc2286_ledger["updated_at"] = utc_now()
    write_json_atomic(unc2286_ledger_path, unc2286_ledger)
    decisions[
        "unc2286|https://www.bleepingcomputer.com/news/security/"
        "salt-typhoon-uses-jumbledpath-malware-to-spy-on-us-telecom-networks/"
    ] = {
        "review_status": "rejected",
        "confidence": "medium",
        "review_notes": unc2286_note,
    }

    salt_title = "Salt Typhoon、通信事業者のネットワーク機器でJumbledPathを使用"
    salt_summary = (
        "Cisco Talosは、Salt Typhoonが米国の大手通信事業者へ侵入し、盗取した正規資格"
        "情報で複数ベンダーのネットワーク機器へアクセスしたと報告した。Go製ELF"
        "ユーティリティJumbledPathは、離れたCisco機器でパケットキャプチャを行い、"
        "経路上のログを妨害し、暗号化した取得データを返送するために使用された。"
    )
    salt_period = {
        "first_observed": time_point(None),
        "last_observed": time_point(None),
    }
    salt_note = (
        "Cisco Talos一次資料へ表示を限定。二次記事が併記した別調査の期間・地域と、"
        "一次資料で確認できないUNC2286の完全同一別名主張を除去した。"
    )
    salt_ledger_path = profiles_root / "salt-typhoon" / "daily-observations.json"
    salt_ledger = load_json(salt_ledger_path)
    for record in salt_ledger.get("records", []):
        if record.get("record_id") != "daily-record--4e15138dd5323d6e8406c8b4":
            continue
        record["activity"]["title"] = salt_title
        record["activity"]["summary"] = salt_summary
        record["activity"]["primary_url"] = CISCO_SALT_SOURCE["url"]
        record["activity_period"] = salt_period
        record["confidence"] = "high"
        record["review_notes"] = salt_note
        record["activity_claim"] = {
            "assessment": "strong-subject",
            "actor_role": "operator",
            "match_location": "primary-report",
            "evidence_text": "Cisco Talos attributes the investigated campaign to Salt Typhoon.",
            "reasons": ["Salt Typhoonへの一次資料帰属を確認"],
            "suggested_confidence": "high",
        }
        primary = {
            "url": CISCO_SALT_SOURCE["url"],
            "source_type": "primary-report",
        }
        if primary["url"] not in {item.get("url") for item in record.get("sources", [])}:
            record.setdefault("sources", []).append(primary)
    salt_ledger["updated_at"] = utc_now()
    write_json_atomic(salt_ledger_path, salt_ledger)
    decisions[
        "salt-typhoon|https://www.bleepingcomputer.com/news/security/"
        "salt-typhoon-uses-jumbledpath-malware-to-spy-on-us-telecom-networks/"
    ] = {
        "review_status": "approved",
        "confidence": "high",
        "activity_overrides": {
            "title": salt_title,
            "summary": salt_summary,
            "primary_url": CISCO_SALT_SOURCE["url"],
        },
        "activity_period": salt_period,
        "review_notes": salt_note,
    }

    konni_title = (
        "KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布"
    )
    konni_summary = (
        "Check Point Researchは、KONNIに関連付けたフィッシング活動で、ブロック"
        "チェーン関連の開発者・エンジニアを狙うおとり文書と悪性LNKを確認した。"
        "LNKはPowerShellローダから、永続化・UAC回避・分析回避・C2タスク実行機能を"
        "持つAI支援生成と評価されたPowerShellバックドアを展開する。"
    )
    konni_period = {
        "first_observed": time_point(
            "2025-10-01T00:00:00Z",
            "month",
            "known",
            "source-stated-sample-upload",
        ),
        "last_observed": time_point(None),
    }
    konni_note = (
        "Check Point一次分析でKONNIへの活動帰属と2025年10月の初期亜種を確認。"
        "ProofpointはTA406をKonni/Opal Sleet活動とのoverlapとして扱うため、TA406では"
        "medium、Konniではhigh confidenceとし、exact aliasには昇格しない。"
    )
    for slug, record_id, confidence in (
        ("ta406", "daily-record--ed16c556a166870fdeb2a4ac", "medium"),
        ("konni", "daily-record--647f622408c58cbd428c2cbc", "high"),
    ):
        ledger_path = profiles_root / slug / "daily-observations.json"
        ledger = load_json(ledger_path)
        for record in ledger.get("records", []):
            if record.get("record_id") != record_id:
                continue
            record["activity"]["title"] = konni_title
            record["activity"]["summary"] = konni_summary
            record["activity"]["primary_url"] = CHECKPOINT_KONNI_SOURCE["url"]
            record["activity_period"] = konni_period
            record["confidence"] = confidence
            record["review_notes"] = konni_note
            record["activity_claim"] = {
                "assessment": "strong-subject",
                "actor_role": "operator" if slug == "konni" else "overlapping-cluster",
                "match_location": "primary-report",
                "evidence_text": (
                    "Check Point directly attributes the campaign to KONNI; "
                    "Proofpoint states that TA406 overlaps Konni activity."
                ),
                "reasons": ["一次資料の直接帰属とcross-vendor境界を分離"],
                "suggested_confidence": confidence,
            }
            primary = {
                "url": CHECKPOINT_KONNI_SOURCE["url"],
                "source_type": "primary-report",
            }
            if primary["url"] not in {
                item.get("url") for item in record.get("sources", [])
            }:
                record.setdefault("sources", []).append(primary)
        ledger["updated_at"] = utc_now()
        write_json_atomic(ledger_path, ledger)
        decisions[
            f"{slug}|https://www.bleepingcomputer.com/news/security/"
            "konni-hackers-target-blockchain-engineers-with-ai-built-malware/"
        ] = {
            "review_status": "approved",
            "confidence": confidence,
            "activity_overrides": {
                "title": konni_title,
                "summary": konni_summary,
                "primary_url": CHECKPOINT_KONNI_SOURCE["url"],
            },
            "activity_period": konni_period,
            "review_notes": konni_note,
        }

    quishing_url = (
        "https://www.bleepingcomputer.com/news/security/"
        "fbi-warns-about-kimsuky-hackers-using-qr-codes-to-phish-us-orgs/"
    )
    apt43_quishing_note = (
        "FBI一次資料は2025年5〜6月のQRコード・スピアフィッシングをKimsukyへ帰属し、"
        "APT43を記載していない。APT43/Kimsukyのcross-vendor overlapだけを根拠に個別活動を"
        "APT43へ複製しない。"
    )
    kimsuky_quishing_note = (
        "同一のFBI活動はactivity--kimsuky-quishing-2025として一次資料、観測期間、TTP、"
        "標的を構造化済み。二次記事由来の日次レコードは重複するため不採用。"
    )
    for slug, record_id, note, role in (
        (
            "apt43",
            "daily-record--47a3435a13311fff4bdba862",
            apt43_quishing_note,
            "taxonomy-reference",
        ),
        (
            "kimsuky",
            "daily-record--7fba10858bc6d43d600f7b78",
            kimsuky_quishing_note,
            "duplicate-corroboration",
        ),
    ):
        ledger_path = profiles_root / slug / "daily-observations.json"
        ledger = load_json(ledger_path)
        for record in ledger.get("records", []):
            if record.get("record_id") != record_id:
                continue
            record["review_status"] = "rejected"
            record["suggested_action"] = "reject"
            record["confidence"] = "high"
            record["review_notes"] = note
            record["activity_claim"] = {
                "assessment": "non-subject" if slug == "apt43" else "duplicate",
                "actor_role": role,
                "match_location": "primary-report",
                "evidence_text": (
                    "The FBI FLASH attributes the activity to Kimsuky and does "
                    "not mention APT43."
                ),
                "reasons": [
                    "APT43への個別活動帰属なし"
                    if slug == "apt43"
                    else "一次資料版canonical活動と重複"
                ],
                "suggested_confidence": "high",
            }
        ledger["updated_at"] = utc_now()
        write_json_atomic(ledger_path, ledger)
        decisions[f"{slug}|{quishing_url}"] = {
            "review_status": "rejected",
            "confidence": "high",
            "review_notes": note,
        }

    clickfix_url = (
        "https://thehackernews.com/2025/09/"
        "dprk-hackers-use-clickfix-to-deliver.html"
    )
    clickfix_note = (
        "記事の主題である2025年5月後半のClickFix・BeaverTail・InvisibleFerret活動は"
        "Contagious Interviewへ帰属されている。Kimsuky/APT43は同じ記事の末尾にある"
        "別ニュース項目であり、主活動の実行主体ではないため、この日次候補は不採用。"
    )
    for slug, record_id in (
        ("apt43", "daily-record--ad2a0b8acf43d0efef90675b"),
        ("kimsuky", "daily-record--f1c379b17bba17ff76922589"),
    ):
        ledger_path = profiles_root / slug / "daily-observations.json"
        ledger = load_json(ledger_path)
        for record in ledger.get("records", []):
            if record.get("record_id") != record_id:
                continue
            record["review_status"] = "rejected"
            record["suggested_action"] = "reject"
            record["confidence"] = "high"
            record["review_notes"] = clickfix_note
            record["activity_claim"] = {
                "assessment": "non-subject",
                "actor_role": "separate-news-item",
                "match_location": "later-section",
                "evidence_text": (
                    "The main ClickFix/BeaverTail campaign is described as "
                    "Contagious Interview; Kimsuky/APT43 is introduced in a "
                    "separate later section."
                ),
                "reasons": ["複数トピック記事の主活動と別ニュース項目を分離"],
                "suggested_confidence": "high",
            }
        ledger["updated_at"] = utc_now()
        write_json_atomic(ledger_path, ledger)
        decisions[f"{slug}|{clickfix_url}"] = {
            "review_status": "rejected",
            "confidence": "high",
            "review_notes": clickfix_note,
        }
    write_json_atomic(decisions_path, decisions)


def update_catalog(catalog_path: Path) -> None:
    catalog = load_json(catalog_path)
    by_slug = {item["slug"]: item for item in catalog["actors"]}
    ta444 = by_slug.get("ta444")
    if ta444:
        aliases = list(ta444.get("aliases", []))
        for name in (
            "BlueNoroff",
            "Sapphire Sleet",
            "COPERNICIUM",
            "STARDUST CHOLLIMA",
            "CageyChameleon",
        ):
            if normalized_name(name) not in {
                normalized_name(item) for item in aliases
            }:
                aliases.append(name)
        ta444["aliases"] = sorted(aliases, key=normalized_name)
    write_json_atomic(catalog_path, catalog)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profiles-root", type=Path, default=PROFILES)
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    parser.add_argument("--review-decisions", type=Path, default=REVIEW_DECISIONS)
    args = parser.parse_args()

    profiles: dict[str, dict[str, Any]] = {}
    for slug in (
        "andariel",
        "apt45",
        "mustang-panda",
        "vanilla-tempest",
        "ta444",
        "apt37",
        "apt38",
        "apt43",
        "water-galura",
        "unc5342",
        "contagious-interview",
        "kimsuky",
        "ta406",
        "konni",
        "unc6040",
        "unc6240",
        "unc6661",
        "unc6671",
        "unc2286",
        "salt-typhoon",
        "apt29",
        "apt41",
        "moonstone-sleet",
        "scattered-spider",
        "breeze-comet",
        "unc5174",
        "cl-sta-1015",
        "unc5221",
        "unc5820",
        "unc6395",
        "storm-1849",
        "storm-2603",
        "zirconium",
    ):
        profiles[slug] = load_json(args.profiles_root / slug / "actor-profile.json")

    fix_mustang_panda(profiles["mustang-panda"])
    fix_vanilla_tempest(profiles["vanilla-tempest"])
    fix_ta444(profiles["ta444"], profiles["apt38"])
    fix_apt37(profiles["apt37"])
    fix_apt38_aws_supply_chain(profiles["apt38"])
    fix_water_galura(profiles["water-galura"])
    fix_actor_relationships(
        profiles["apt45"],
        profiles["andariel"],
        profiles["unc5342"],
        profiles["contagious-interview"],
        profiles["kimsuky"],
    )
    fix_kimsuky_quishing_duplicates(profiles["apt43"], profiles["kimsuky"])
    fix_clickfix_beavertail_multitopic_boundary(
        profiles["apt43"],
        profiles["kimsuky"],
        profiles["contagious-interview"],
    )
    fix_vendor_cluster_boundaries(
        profiles["unc6040"],
        profiles["unc6240"],
        profiles["unc6661"],
        profiles["unc6671"],
        profiles["unc2286"],
        profiles["salt-typhoon"],
    )
    fix_ta406_konni_boundary(profiles["ta406"], profiles["konni"])
    fix_reviewed_primary_activity_evidence(
        profiles["apt29"],
        profiles["apt41"],
        profiles["kimsuky"],
        profiles["moonstone-sleet"],
        profiles["unc5221"],
        profiles["unc5820"],
        profiles["unc6395"],
    )
    fix_scattered_spider_primary_boundaries(profiles["scattered-spider"])
    fix_react2shell_cluster_boundary(
        profiles["unc5174"], profiles["cl-sta-1015"]
    )
    fix_new_actor_links_and_activity(
        profiles["breeze-comet"],
        profiles["storm-1849"],
        profiles["storm-2603"],
        profiles["zirconium"],
    )

    for slug, profile in profiles.items():
        profile["actor"]["aliases"].sort(
            key=lambda item: normalized_name(item.get("name", ""))
        )
        profile["activities"].sort(key=lambda item: item["activity_id"])
        profile["capabilities"]["malware"].sort(
            key=lambda item: normalized_name(item.get("name", ""))
        )
        materialize_profile_diamonds(profile)
        profile["updated_at"] = utc_now()
        write_json_atomic(args.profiles_root / slug / "actor-profile.json", profile)

    update_daily_review_state(args.profiles_root, args.review_decisions)
    update_catalog(args.catalog)
    print(
        json.dumps(
            {
                "profiles_updated": sorted(profiles),
                "removed_false_activity": VANILLA_FALSE_ACTIVITY_ID,
                "primary_sources_added": 34,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
