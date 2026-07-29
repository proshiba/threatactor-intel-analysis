# VOID MANTICORE 脅威アクタープロファイル

- プロファイルID: `actor--void-manticore`
- 状態: draft
- 更新日時: 2026-07-27T11:17:27Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

VOID MANTICOREの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **VOID MANTICORE**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BANISHED KITTEN | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| COBALT MYSTIQUE | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Handala Hack | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| HomeLand Justice | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Karma | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Karmabelow80 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Red Sandstorm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) is a threat group assessed to operate on behalf of Iran’s Ministry of Intelligence and Security (MOIS).(Citation: Check Point VOID MANTICORE Handala Hack March 2026) Active since at least mid-2022, VOID MANTICORE has targeted government entities, critical infrastructure, and private sector organizations across Albania, Israel, and the United States.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) conducts destructive cyber operations, combining wiper attacks with hack-and-leak campaigns. The group has operated under multiple public-facing personas, including [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) in operations against Albania, Karma and Karma Below in campaigns targeting Israeli organizations, and Handala Hack, its current primary persona, which has claimed activity against Israeli and U.S. entities, including a March 2026 attack against Stryker Corporation.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: DOJ FBI Handala Hack March 2026)  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has been observed collaborating with Scarred Manticore, which has been linked to initial access operations preceding VOID MANTICORE’s activity.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026)  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | HomeLand Justice | canonical-name | 高 | Iran | https://www.clearskysec.com/wp-content/uploads/2024/01/No-Justice-Wiper.pdf<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=HomeLand+Justice&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Red Sandstorm | canonical-name | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | HomeLand Justice | single-alias-intersection | 中 | IR | https://www.picussecurity.com/resource/blog/cisa-alert-aa22-264a-iranian-homeland-justice-apt-groups-ttp<br>https://www.attackiq.com/2022/09/23/attack-graph-response-to-us-cert-alert-aa22-264a-iranian-state-actors-conduct-cyber-operations-against-the-government-of-albania/<br>https://www.mandiant.com/resources/blog/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against |
| misp-threat-actor | BANISHED KITTEN | multiple-name-intersection | 高 | IR, Iran (Islamic Republic of) | https://www.crowdstrike.com/adversaries/banished-kitten/<br>https://services.google.com/fh/files/misc/tool-of-first-resort-israel-hamas-war-cyber.pdf |
| misp-threat-actor | Void Manticore | canonical-name | 高 | IR | https://research.checkpoint.com/2024/bad-karma-no-justice-void-manticore-destructive-activities-in-israel/ |
| misp-microsoft-activity-group | Red Sandstorm | canonical-name | 高 | IR, Iran | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | VOID MANTICORE - G1055 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1055<br>https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment<br>https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/ |
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

未確認

### ツール

未確認

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| BiBiワイパーの新バージョンがディスクパーティションテーブルも破壊 | disruptive-activity | 不明 | 不明 | 2024-05-21 | 新バージョンのBiBi Wiperがディスクパーティションテーブルを破壊 攻撃はイスラエルとアルバニアで発生 攻撃者はイランのハッカーグループであるVoid Manticore Void Manticoreは多様な破壊ツールを使用 新バージョンはデータ復旧を困難にする | 中 | `source--daily-0d70b2cb1fe1f39ff860` |
| HomeLand Justice | campaign | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 2026-05-12 | [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) was a disruptive cyber campaign conducted by Iranian state-affiliated actors against Albanian government networks in July and September 2022. The activity combined ransomware, wiper malware, and data leak operations. Initial access for [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) was established as early as May 2021, and threat actors moved laterally, exfiltrated sensitive information, and maintained persistence for approximately 14 months prior to the destructive phase of the operation. Responsibility was claimed by the "HomeLand Justice" front, which framed the campaign as retaliation against the Mujahedeen-e Khalq (MEK), an Iranian opposition group with a presence in Albania. Multiple Iran-nexus groups are assessed to have participated in the campaign, including [HEXANE](https://attack.mitre.org/groups/G1001) who probed victim infrastructure.(Citation: Mandiant ROADSWEEP August 2022)(Citation: Microsoft Albanian Government Attacks September 2022)(Citation: CISA Iran Albanian Attacks September 2022) A second wave of attacks was launched in September 2022 using similar tactics following public attribution of the previous activity to Iran and the severing of diplomatic ties between Iran and Albania.(Citation: CISA Iran Albanian Attacks September 2022)<br><br> | 高 | `source--mitre-attack-19-1` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.015 | Compression | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Lateral Movement | T1072 | Software Deployment Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074 | Data Staged | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.004 | Cloud Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098 | Account Manipulation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.001 | Password Guessing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.004 | Credential Stuffing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.002 | Remote Email Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1123 | Audio Capture | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1125 | Video Capture | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.002 | Sharepoint | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219.002 | Remote Desktop Software | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Privilege Escalation | T1484.001 | Group Policy Modification | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1485 | Data Destruction | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1490 | Inhibit System Recovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.002 | Credentials in Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1561.001 | Disk Content Wipe | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1561.002 | Disk Structure Wipe | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.003 | Hidden Window | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.004 | Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1651 | Cloud Administration Command | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1679 | Selective Exclusion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686.003 | Windows Host Firewall | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 65件（`artifacts.csv`）

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
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-0d70b2cb1fe1f39ff860 | BiBiワイパーの新バージョンがディスクパーティションテーブルも破壊 | bleepingcomputer.com | 2024-05-21 | https://www.bleepingcomputer.com/news/security/new-bibi-wiper-version-also-destroys-the-disk-partition-table/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--void-manticore--0402ab708c2b3b30 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--void-manticore--0ad84d5ffade7472 | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--15b241fd48f227db | Semiannual+Ransomware+Report+ +H1+2024 |  | 2024 | cybercrime/2024/Semiannual+Ransomware+Report+-+H1+2024.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--1cf02c350fe8a86e | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--40ac301c05170014 | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--432520f2738bbc2c | void manticore |  | 不明 | actor_profile/evidence/void-manticore.csv | structured-data | TLP:CLEAR | 中 |
| source--void-manticore--491ffb169527ff34 | Russian Ransomware C2 Network Discovered in Censys Data |  | 不明 | summary/2022/Russian Ransomware C2 Network Discovered in Censys Data.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--5f00205af443971a | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--6c4456aaa341ac6c | the rise of state sponsored hacktivism |  | 不明 | Anonymous/the-rise-of-state-sponsored-hacktivism.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--7001c6c11351daa6 | mobile APT threat report |  | 不明 | mobile-APT/mobile-APT-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--a1f77e6e9c133da5 | VB2022 Exploit archaeology a forensic history of in the wild NSO Group exploits |  | 2022 | NSOGroup/VB2022-Exploit-archaeology-a-forensic-history-of-in-the-wild-NSO-Group-exploits.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--a3e1662f3971c94c | Claude Mythos Preview System Card |  | 不明 | AISecurity/Claude Mythos Preview System Card.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--a7dc8c791d13500e | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--ae6876bd7aa0f48a | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--b9b346da5842493e | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--bede1a8da90bf2b0 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--c6ce9deb8a7e5fa5 | Public Report EN 2025 DIGITAL |  | 2025 | International Strategic/Canada/Public Report_EN_2025_DIGITAL.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--caf4bc945a22099d | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--d79d08d6c77f4ed5 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--e61cfd99872b143b | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--eb26cccb5d8b7a99 | tool of first resort israel hamas war cyber |  | 不明 | summary/2024/tool-of-first-resort-israel-hamas-war-cyber.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--ef9c292f567e0dc2 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
