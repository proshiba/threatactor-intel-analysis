# Play 脅威アクタープロファイル

- プロファイルID: `actor--play`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Playの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Play**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Play](https://attack.mitre.org/groups/G1040) is a ransomware group that has been active since at least 2022 deploying  [Playcrypt](https://attack.mitre.org/software/S1162) ransomware against the business, government, critical infrastructure, healthcare, and media sectors in North America, South America, and Europe. [Play](https://attack.mitre.org/groups/G1040) actors employ a double-extortion model, encrypting systems after exfiltrating data, and are presumed by security researchers to operate as a closed group.(Citation: CISA Play Ransomware Advisory December 2023)(Citation: Trend Micro Ransomware Spotlight Play July 2023) |
| Capability | Playcrypt, Cobalt Strike, BloodHound, Empire, Nltest, Mimikatz, AdFind, Wevtutil, PsExec |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Play - G1040 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1040<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a<br>https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

候補なし

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--playcrypt | Playcrypt | [Playcrypt](https://attack.mitre.org/software/S1162) is a ransomware that has been used by [Play](https://attack.mitre.org/groups/G1040) since at least 2022 in attacks against against the business, government, critical infrastructure, healthcare, and media sectors in North America, South America, and Europe. [Playcrypt](https://attack.mitre.org/software/S1162) derives its name from adding the .play extension to encrypted files and has overlap with tactics and tools associated with Hive and Nokoyawa ransomware and infrastructure associated with Quantum ransomware.(Citation: Microsoft PlayCrypt August 2022)(Citation: CISA Play Ransomware Advisory December 2023)(Citation: Trend Micro Ransomware Spotlight Play July 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--bloodhound | BloodHound | [BloodHound](https://attack.mitre.org/software/S0521) is an Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment.(Citation: GitHub Bloodhound)(Citation: CrowdStrike BloodHound April 2018)(Citation: FoxIT Wocao December 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nltest | Nltest | [Nltest](https://attack.mitre.org/software/S0359) is a Windows command-line utility used to list domain controllers and enumerate domain trusts.(Citation: Nltest Manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--adfind | AdFind | [AdFind](https://attack.mitre.org/software/S0552) is a free command-line query tool that can be used for gathering information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--wevtutil | Wevtutil | [Wevtutil](https://attack.mitre.org/software/S0645) is a Windows command-line utility that enables administrators to retrieve information about event logs and publishers.(Citation: Wevtutil Microsoft Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

活動履歴なし



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1030 | Data Transfer Size Limits | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048 | Exfiltration Over Alternative Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 26件
- IOC観測: 29件
- 複数攻撃で観測: 0件
- 要レビュー候補: 18件
- 非IOC artifact観測: 259件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--play--1d18f15a8520d3bf | play |  | 不明 | actor_profile/evidence/play.csv | structured-data | TLP:CLEAR | 中 |
| source--play--0872d8bdf85e2856 | Trends Artificial Intelligence |  | 不明 | AISecurity/2025/Trends_Artificial_Intelligence.pdf | report | TLP:CLEAR | 中 |
| source--play--087f7b26fdf1abc6 | Searching for Diamonds Cross Domain Opportunities in Cyber Threat Intelligence |  | 不明 | AISecurity/CTI/Searching_for_Diamonds_Cross-Domain_Opportunities_in_Cyber_Threat_Intelligence.pdf | report | TLP:CLEAR | 中 |
| source--play--f153b954b1de7808 | OWASP Top 10 for LLM Applications 2025 |  | 2025 | AISecurity/OWASP Top 10 for LLM Applications 2025.pdf | report | TLP:CLEAR | 中 |
| source--play--f18e10bb3db72a94 | CSA RUSSIAN GRU TARGET LOGISTICS |  | 不明 | APT28/CSA_RUSSIAN_GRU_TARGET_LOGISTICS.pdf | report | TLP:CLEAR | 中 |
| source--play--4f0eb93a0d8a63fa | Technical threat report Arid Viper April 2021 |  | 2021 | Arid Viper/Technical-threat-report-Arid-Viper-April-2021.pdf | report | TLP:CLEAR | 中 |
| source--play--aa6c06661b3f3c59 | Amnesty Cellebrite |  | 不明 | Cellebrite/Amnesty-Cellebrite.pdf | report | TLP:CLEAR | 中 |
| source--play--a8505a49ade51c1f | Technical report Armagedon |  | 不明 | Gamaredon/Technical report Armagedon.pdf | report | TLP:CLEAR | 中 |
| source--play--c8da418de9a3649c | ADRN Surveillance Supply Chain Report |  | 不明 | International Strategic/Africa/ADRN_Surveillance_Supply_Chain_Report.pdf | report | TLP:CLEAR | 中 |
| source--play--febe24d807958d4d | national cyber threat assessment 2025 2026 e |  | 不明 | International Strategic/Canada/national-cyber-threat-assessment-2025-2026-e.pdf | report | TLP:CLEAR | 中 |
| source--play--f46bc23297ec23cd | Linking South Asian cyber espionnage groups to publish |  | 不明 | International Strategic/India/Linking_South_Asian_cyber_espionnage_groups-to-publish.pdf | report | TLP:CLEAR | 中 |
| source--play--0448528531b79bf8 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--play--e151b6d6ece25d8f | Cyber operations by russia new goals, tools and groups |  | 不明 | International Strategic/Russia/Cyber operations by russia new goals, tools and groups.pdf | report | TLP:CLEAR | 中 |
| source--play--dc62070c00584aa3 | google fog of war research report |  | 不明 | International Strategic/Russia/google_fog_of_war_research_report.pdf | report | TLP:CLEAR | 中 |
| source--play--343bfe3c32762464 | Oceanlotus APK sample |  | 不明 | Oceanlotus/Oceanlotus-APK-sample.TXT | text-data | TLP:CLEAR | 中 |
| source--play--c2f3fbdc2ba15c4d | Buying Spying Insights into Commercial Surveillance Vendors TAG report |  | 不明 | Spyware/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf | report | TLP:CLEAR | 中 |
| source--play--575448efbdbbcccf | ResidentBat A new spyware family used by Belarusian KGB |  | 不明 | Spyware/ResidentBat-A new spyware family used by Belarusian KGB.pdf | report | TLP:CLEAR | 中 |
| source--play--ee33a8037059e204 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--play--06861593faca52d3 | Bitdefender PR Whitepaper BitterAPT creat4571 en EN GenericUse |  | 不明 | bitter/2020/Bitdefender-PR-Whitepaper-BitterAPT-creat4571-en-EN-GenericUse.pdf | report | TLP:CLEAR | 中 |
| source--play--280b83161753c732 | Quarterly Adversarial Threat Report Q2 2022 |  | 2022 | bitter/2022/Quarterly-Adversarial-Threat-Report-Q2-2022.pdf | report | TLP:CLEAR | 中 |
| source--play--3058653ae79e2497 | Semiannual+Ransomware+Report+ +H1+2024 |  | 2024 | cybercrime/2024/Semiannual+Ransomware+Report+-+H1+2024.pdf | report | TLP:CLEAR | 中 |
| source--play--78be73e5ba624833 | infoblox report vigorish viper a venomous bet |  | 不明 | cybercrime/2024/infoblox-report-vigorish-viper-a-venomous-bet-.pdf | report | TLP:CLEAR | 中 |
| source--play--3fc34333439773a6 | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--play--1eb2173cf3c7fc8c | 2025 IC3Report |  | 2025 | cybercrime/2026/2025_IC3Report.pdf | report | TLP:CLEAR | 中 |
| source--play--8b939dc15392f7c1 | batshadow vietnamese threat group vampire bot report |  | 不明 | cybercrime/BatShadow/batshadow-vietnamese-threat-group-vampire-bot-report.pdf | report | TLP:CLEAR | 中 |
| source--play--7254f6a72902c441 | HUMAN Report BADBOX and PEACHPIT |  | 不明 | cybercrime/botnet/BADBOX/HUMAN_Report_BADBOX-and-PEACHPIT.pdf | report | TLP:CLEAR | 中 |
| source--play--dd20ce38853e58e5 | Dragon Messenger APT Group123 |  | 不明 | group123/Dragon Messenger_APT_Group123.pdf | report | TLP:CLEAR | 中 |
| source--play--4f02bec9fe72edbc | kimsuky 2023 03 20 joint cyber security advisory |  | 2023-03-20 | kimsuky/kimsuky-2023-03-20-joint-cyber-security-advisory.pdf | report | TLP:CLEAR | 中 |
| source--play--0e9351c15e5da6eb | The Lazarus Constellation |  | 不明 | lazarus/The_Lazarus_Constellation.pdf | report | TLP:CLEAR | 中 |
| source--play--763a59b8bfd0e142 | mobile APT threat report |  | 不明 | mobile-APT/mobile-APT-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--play--b47f4b24e6bb271e | global perspective of the sidewinder apt |  | 不明 | sidewinder/global-perspective-of-the-sidewinder-apt.pdf | report | TLP:CLEAR | 中 |
| source--play--7d6d12f98e06115b | APT blackberry mobile malware report |  | 不明 | summary/2020/APT-blackberry-mobile-malware-report.pdf | report | TLP:CLEAR | 中 |
| source--play--f7a4ca09f7101ee2 | ESET Threat Report Q22020 |  | 不明 | summary/2020/ESET_Threat_Report_Q22020.pdf | report | TLP:CLEAR | 中 |
| source--play--5fe7a65f6d8405e5 | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--play--43f5d6901f0845aa | Offensive Cyber Capabilities Proliferation Report |  | 不明 | summary/2021/Offensive-Cyber-Capabilities-Proliferation-Report.pdf | report | TLP:CLEAR | 中 |
| source--play--f229f84179ac2568 | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--play--11e35f19b14202a9 | sophos 2021 threat report |  | 2021 | summary/2021/sophos-2021-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--play--38685834fce653fb | Upstream Security Global Automotive Cybersecurity Report 2022 |  | 2022 | summary/2022/Upstream_Security-Global_Automotive_Cybersecurity_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--play--07d88b7294ed6b94 | sophos 2022 threat report |  | 2022 | summary/2022/sophos-2022-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--play--c1a1dcbbd7b3de86 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--play--40580b77c028a947 | Crypto Crime Report 2023 |  | 2023 | summary/2023/Crypto_Crime_Report_2023.pdf | report | TLP:CLEAR | 中 |
| source--play--98e930a70f0839fa | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--play--ca5b28bf7435545a | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--play--4b490bb8641fa2c3 | positive research 2023 eng |  | 2023 | summary/2023/positive-research-2023-eng.pdf | report | TLP:CLEAR | 中 |
| source--play--2356296a2053cc70 | 2023 RESEARCH REPORT |  | 2023 | summary/2024/2023 RESEARCH REPORT.pdf | report | TLP:CLEAR | 中 |
| source--play--a574d16530e2841e | 2024 H1 Threat Intel Report Final |  | 2024 | summary/2024/2024-H1-Threat-Intel-Report-Final.pdf | report | TLP:CLEAR | 中 |
| source--play--5a97a6b7ea7e3542 | 2024 dbir data breach investigations report |  | 2024 | summary/2024/2024-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--play--f061e8e739f7d1a8 | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--play--9778953419a40ce7 | 2024 Cyber Threat Report Huntress FINAL |  | 2024 | summary/2024/2024_Cyber_Threat_Report_Huntress_FINAL.pdf | report | TLP:CLEAR | 中 |
| source--play--ed5bfeed9bce81cf | 2024 Trustwave Public Sector Threat Landscape |  | 2024 | summary/2024/2024_Trustwave_Public_Sector_Threat_Landscape.pdf | report | TLP:CLEAR | 中 |
| source--play--5d16ad611b41b501 | CERTFR 2024 CTI 002 |  | 2024 | summary/2024/CERTFR-2024-CTI-002.pdf | report | TLP:CLEAR | 中 |
| source--play--7e35446c1d0b2090 | Coalition 2024 Claims Report Mid Year Update |  | 2024 | summary/2024/Coalition_2024-Claims-Report-Mid-Year-Update.pdf | report | TLP:CLEAR | 中 |
| source--play--2cf32ec4328a5fa3 | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--play--0ea82e4922fc6f41 | GRIT Ransomware Annual Report 2023 |  | 2023 | summary/2024/GRIT_Ransomware_Annual_Report_2023.pdf | report | TLP:CLEAR | 中 |
| source--play--9dbb216b5630ea95 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--play--8d34d46153e1ae21 | Norma+Cyber+Annual+Threat+Assessment+ +Spreads |  | 不明 | summary/2024/Norma+Cyber+Annual+Threat+Assessment+-+Spreads.pdf | report | TLP:CLEAR | 中 |
| source--play--9908c6e86bfcbf91 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--play--a1e8b706612d6a30 | RussianCyber |  | 不明 | summary/2024/RussianCyber.pdf | report | TLP:CLEAR | 中 |
| source--play--1eeae6397391ed7f | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--play--7db09e7784741cbb | Worldwide Ransomware Attacks as of June 2024 Consistent With Previous Year Sep2024 |  | 2024 | summary/2024/Worldwide_Ransomware_Attacks_as_of_June_2024_Consistent_With_Previous_Year_Sep2024.pdf | report | TLP:CLEAR | 中 |
| source--play--13e57073eedadd8e | eset threat report h12024 |  | 不明 | summary/2024/eset-threat-report-h12024.pdf | report | TLP:CLEAR | 中 |
| source--play--82635b615317f1e5 | eset threat report h22024 |  | 不明 | summary/2024/eset-threat-report-h22024.pdf | report | TLP:CLEAR | 中 |
| source--play--f1ac308e68da9f5f | rapid7 2024 attack intelligence report |  | 2024 | summary/2024/rapid7_2024_attack_intelligence_report.pdf | report | TLP:CLEAR | 中 |
| source--play--35af603545f80ab8 | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--play--932139f55c95ef8c | tool of first resort israel hamas war cyber |  | 不明 | summary/2024/tool-of-first-resort-israel-hamas-war-cyber.pdf | report | TLP:CLEAR | 中 |
| source--play--2a36aa61f5309644 | 2024 Threat Intelligence Annual Report |  | 2024 | summary/2025/2024 Threat Intelligence Annual Report.pdf | report | TLP:CLEAR | 中 |
| source--play--2bb0392eae95685d | 2024YiR report |  | 2024 | summary/2025/2024YiR-report.pdf | report | TLP:CLEAR | 中 |
| source--play--d76a9042b98d1852 | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--play--3c61fb6e0945f50a | 2025 Global Threat Intelligence Report |  | 2025 | summary/2025/2025 Global Threat Intelligence Report .pdf | report | TLP:CLEAR | 中 |
| source--play--41dcac09ada2109b | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--play--30dab70452b55b70 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--play--742f997abc9f8eab | Dragos 2025 OT Cybersecurity Report A Year in Review |  | 2025 | summary/2025/Dragos-2025-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--play--5fca0ec419549548 | Global Threat Report 2025 |  | 2025 | summary/2025/Global Threat Report 2025.pdf | report | TLP:CLEAR | 中 |
| source--play--be4e7ada57996b0d | Microsoft Digital Defense Report 2025 |  | 2025 | summary/2025/Microsoft-Digital-Defense-Report-2025.pdf | report | TLP:CLEAR | 中 |
| source--play--55c5ef1df747cb12 | PL Report CP 2024 |  | 2024 | summary/2025/PL_Report_CP_2024.pdf | report | TLP:CLEAR | 中 |
| source--play--bb60ee151d89d4e3 | Security Navigator 2026 |  | 2026 | summary/2025/Security_Navigator_2026.pdf | report | TLP:CLEAR | 中 |
| source--play--dd61a483d1b18be2 | SixMap Research Energy Sector Exposure Assessment |  | 不明 | summary/2025/SixMap-Research_Energy-Sector-Exposure-Assessment.pdf | report | TLP:CLEAR | 中 |
| source--play--f3fad5266f1267e1 | annual threat report 2024 |  | 2024 | summary/2025/annual-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--play--d8dd63b6a4bd044f | eset apt activity report q2 2025 q3 2025 |  | 2025 | summary/2025/eset-apt-activity-report-q2-2025-q3-2025.pdf | report | TLP:CLEAR | 中 |
| source--play--84bd6e080245ae54 | eset threat report h12025 |  | 不明 | summary/2025/eset-threat-report-h12025.pdf | report | TLP:CLEAR | 中 |
| source--play--de3fdf729f6823ef | eset threat report h22025 |  | 不明 | summary/2025/eset-threat-report-h22025.pdf | report | TLP:CLEAR | 中 |
| source--play--6c0f977437801439 | threat landscape report 2025 |  | 2025 | summary/2025/threat-landscape-report-2025.pdf | report | TLP:CLEAR | 中 |
| source--play--003a4ddb0556ccbb | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--play--54fa22a1d25ca61e | 2025 Year in Review  Malicious Infrastructure |  | 2025 | summary/2026/2025 Year in Review- Malicious Infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--play--05495272e5437e00 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--play--39cb514ac9df39cd | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--play--d8315978d0cc7abb | CyberProof 2026 Global Threat Intelligence Report |  | 2026 | summary/2026/CyberProof_2026_Global_Threat_Intelligence_Report.pdf | report | TLP:CLEAR | 中 |
| source--play--4c7cbeb47e8a09dc | Threat Report 2026 v4 |  | 2026 | summary/2026/Threat Report 2026 v4.pdf | report | TLP:CLEAR | 中 |
| source--play--66c187a919f40bdf | [Report] Bitsight State of the Underground 2026 |  | 2026 | summary/2026/[Report] Bitsight State of the Underground 2026.pdf | report | TLP:CLEAR | 中 |
| source--play--53ba917fb848d730 | 002 |  | 不明 | summary/UNREDACTEDMagazine/002.pdf | report | TLP:CLEAR | 中 |
| source--play--8dc375f875e200ce | 004 |  | 不明 | summary/UNREDACTEDMagazine/004.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
