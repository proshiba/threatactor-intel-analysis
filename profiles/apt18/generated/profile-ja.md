# APT18 脅威アクタープロファイル

- プロファイルID: `actor--apt18`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

APT18の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT18**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Dynamite Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA428 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TG-0416 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Threat Group-0416 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Wekby | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
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
| Adversary | [APT18](https://attack.mitre.org/groups/G0026) is a threat group that has operated since at least 2009 and has targeted a range of industries, including technology, manufacturing, human rights groups, government, and medical. (Citation: Dell Lateral Movement) |
| Capability | gh0st RAT, hcdLoader, Pisloader, HTTPBrowser, TokenControl, TManger, cmd |
| Infrastructure |  |
| Victim | Aerospace and Defence; Construction and Engineering; Education; Health and Biotechnology; High Tech; Telecommunications; Transportation |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 18, Dynamite Panda, Wekby | canonical-name | 高 | China | https://apt.etda.or.th/cgi-bin/showcard.cgi?g=APT+18%2C+Dynamite+Panda%2C+Wekby&n=1 |
| etda-threat-group-cards | TA428 | single-alias-intersection | 中 | China | https://www.proofpoint.com/us/threat-insight/post/chinese-apt-operation-lagtime-it-targets-government-information-technology<br>https://st.drweb.com/static/new-www/news/2021/april/drweb_research_attacks_on_russian_research_institutes_en.pdf<br>https://labs.sentinelone.com/thundercats-hack-the-fsb-your-taxes-didnt-pay-for-this-op/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Satin Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT18 | canonical-name | 高 | CN, China | https://threatpost.com/apt-gang-branches-out-to-medical-espionage-in-community-health-breach/107828<br>https://www.cfr.org/interactive/cyber-operations/apt-18<br>https://attack.mitre.org/groups/G0026 |
| misp-threat-actor | TA428 | single-alias-intersection | 中 | CN | https://www.proofpoint.com/us/threat-insight/post/chinese-apt-operation-lagtime-it-targets-government-information-technology<br>https://www.recordedfuture.com/china-linked-ta428-threat-group<br>https://decoded.avast.io/luigicamastra/apt-group-targeting-governmental-agencies-in-east-asia |
| misp-microsoft-activity-group | Satin Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | APT18 - G0026 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0026<br>http://www.secureworks.com/resources/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems/ |
| misp-mitre-intrusion-set | APT18 - G0026 | mitre-external-id | 高 |  | http://www.secureworks.com/resources/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems/<br>https://attack.mitre.org/groups/G0026<br>https://www.anomali.com/blog/evasive-maneuvers-the-wekby-group-attempts-to-evade-analysis-via-custom-rop |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| SAMURAI PANDA | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--gh0st-rat | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) is a remote access tool (RAT). The source code is public and it has been used by multiple groups.(Citation: FireEye Hacking Team)(Citation: Arbor Musical Chairs Feb 2018)(Citation: Nccgroup Gh0st April 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hcdloader | hcdLoader | [hcdLoader](https://attack.mitre.org/software/S0071) is a remote access tool (RAT) that has been used by [APT18](https://attack.mitre.org/groups/G0026). (Citation: Dell Lateral Movement) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pisloader | Pisloader | [Pisloader](https://attack.mitre.org/software/S0124) is a malware family that is notable due to its use of DNS as a C2 protocol as well as its use of anti-analysis tactics. It has been used by [APT18](https://attack.mitre.org/groups/G0026) and is similar to another malware family, [HTTPBrowser](https://attack.mitre.org/software/S0070), that has been used by the group. (Citation: Palo Alto DNS Requests) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--httpbrowser | HTTPBrowser | [HTTPBrowser](https://attack.mitre.org/software/S0070) is malware that has been used by several threat groups. (Citation: ThreatStream Evasion Analysis) (Citation: Dell TG-3390) It is believed to be of Chinese origin. (Citation: ThreatConnect Anthem) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--tokencontrol | TokenControl | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--tmanger | TManger | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--cmd | cmd | [cmd](https://attack.mitre.org/software/S0106) is the Windows command-line interpreter that can be used to interact with systems and execute other processes and utilities. (Citation: TechNet Cmd)<br><br>Cmd.exe contains native functionality to perform many operations to interact with the system, including listing files in a directory (e.g., <code>dir</code> (Citation: TechNet Dir)), deleting files (e.g., <code>del</code> (Citation: TechNet Del)), and copying files (e.g., <code>copy</code> (Citation: TechNet Copy)). | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Healthcare | Targeting text indicates the Healthcare sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Education and Research | Targeting text indicates the Education and Research sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf {"page": 98} TA428 ol remote systems. Windows Management Instrumentation T1047 Examples of procedures Example 1 One of the most widespread variants of WMI use is running a process on a remote machine using wmic.exe: Use of wmic.exe by the TA428 group: wmic /node:<ip> /user:<domain>\<username> /password:<password> process call create "cmd /c systeminfo >$te |  |  | 不明 | 不明 | 中 | `source--apt18--6bf111e59271820a` |
| Execution, Persistence, Privilege Escalation | T1053.002 | At | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 42件（`artifacts.csv`）

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
| source--apt18--6bf111e59271820a | apt18 |  | 不明 | actor_profile/evidence/apt18.csv | structured-data | TLP:CLEAR | 中 |
| source--apt18--da821fe1c3ca05f4 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--apt18--db0e02eca27981af | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--apt18--becdd6e442eed672 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--apt18--ed02c6978bd524bc | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--apt18--e8a8f014530a872e | mpressioncss ta report 2020 5 en |  | 2020 | summary/2021/mpressioncss_ta_report_2020_5_en.pdf | report | TLP:CLEAR | 中 |
| source--apt18--ff466d2a0613cb95 | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--apt18--9f730b4af9b9aefb | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--apt18--36bc8d20db07009b | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--apt18--14a70c401e9230d6 | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--apt18--87537cac4ba2adf8 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--apt18--b2b62129a2b1744b | kaspersky ics cert apt attacks on industrial organizations in h2 2022 en |  | 2022 | summary/2023/kaspersky-ics-cert-apt-attacks-on-industrial-organizations-in-h2-2022-en.pdf | report | TLP:CLEAR | 中 |
| source--apt18--8f4e91c80ba83c29 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--apt18--b60ab30d3578c504 | SixMap Research Energy Sector Exposure Assessment |  | 不明 | summary/2025/SixMap-Research_Energy-Sector-Exposure-Assessment.pdf | report | TLP:CLEAR | 中 |
| source--apt18--9e4c9468fbca0ffe | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
