# Tortoiseshell 脅威アクタープロファイル

- プロファイルID: `actor--tortoiseshell`
- 状態: draft
- 更新日時: 2026-07-29T15:39:43Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Tortoiseshellの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Tortoiseshell**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| CURIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Crimson Sandstorm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA456 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Yellow Liderc | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| APT35 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 27; mapping requires review. |
| Imperial Kitten | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 27; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

未評価

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [CURIUM](https://attack.mitre.org/groups/G1012) is an Iranian threat group, first reported in September 2019 and active since at least July 2018, targeting IT service providers in the Middle East.(Citation: Symantec Tortoiseshell 2019) [CURIUM](https://attack.mitre.org/groups/G1012) has since invested in building relationships with potential targets via social media over a period of months to establish trust and confidence before sending malware. Security researchers note [CURIUM](https://attack.mitre.org/groups/G1012) has demonstrated great patience and persistence by chatting with potential targets daily and sending benign files to help lower their security consciousness.(Citation: Microsoft Iranian Threat Actor Trends November 2021) |
| Capability | IMAPLoader, Backdoor.Syskit, Poison Frog, Infostealer/Sha.exe/Sha432.exe, Infostealer/stereoversioncontrol.exe, get-logon-history.ps1 |
| Infrastructure |  |
| Victim | IT providers in Saudi Arabia |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Magic Hound, APT 35, Cobalt Illusion, Charming Kitten | single-alias-intersection | 中 | Iran | https://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf<br>https://en.wikipedia.org/wiki/Charming_Kitten<br>https://vblocalhost.com/uploads/VB2021-Haeghebaert.pdf |
| etda-threat-group-cards | Tortoiseshell, Imperial Kitten | canonical-name | 高 | Iran | https://www.symantec.com/blogs/threat-intelligence/tortoiseshell-apt-supply-chain<br>https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Tortoiseshell%2C+Imperial+Kitten&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Crimson Sandstorm | canonical-name | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Cuboid Sandstorm | single-alias-intersection | 中 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Mint Sandstorm | single-alias-intersection | 中 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Smoke Sandstorm | single-alias-intersection | 中 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT35 | single-alias-intersection | 中 | IR | https://www.fireeye.com/content/dam/collateral/en/mtrends-2018.pdf<br>https://attack.mitre.org/groups/G0059/<br>https://www.cfr.org/interactive/cyber-operations/magic-hound |
| misp-threat-actor | Tortoiseshell | canonical-name | 高 | IR, Iran (Islamic Republic of) | https://www.symantec.com/blogs/threat-intelligence/tortoiseshell-apt-supply-chain<br>https://www.darkreading.com/threat-intelligence/iranian-government-hackers-target-us-veterans/d/d-id/1335897<br>https://ctoatncsc.substack.com/p/cto-at-ncsc-summary-week-ending-october |
| misp-threat-actor | Bohrium | single-alias-intersection | 中 | IR | https://twitter.com/CyberAmyHB/status/1532398956918890500 |
| misp-microsoft-activity-group | Crimson Sandstorm | canonical-name | 高 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Cuboid Sandstorm | single-alias-intersection | 中 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Mint Sandstorm | single-alias-intersection | 中 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Smoke Sandstorm | single-alias-intersection | 中 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Magic Hound - G0059 | single-alias-intersection | 中 |  | http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf<br>https://attack.mitre.org/groups/G0059<br>https://blog.certfa.com/posts/charming-kitten-christmas-gift/ |
| misp-mitre-intrusion-set | CURIUM - G1012 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1012<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/tortoiseshell-apt-supply-chain |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Bohrium | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Tortoiseshell | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--imaploader | IMAPLoader | [IMAPLoader](https://attack.mitre.org/software/S1152) is a .NET-based loader malware exclusively associated with [CURIUM](https://attack.mitre.org/groups/G1012) operations since at least 2022. [IMAPLoader](https://attack.mitre.org/software/S1152) leverages email protocols for command and control and payload delivery.(Citation: PWC Yellow Liderc 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--backdoor-syskit | Backdoor.Syskit | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--poison-frog | Poison Frog | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--infostealer-sha-exe-sha432-exe | Infostealer/Sha.exe/Sha432.exe | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--infostealer-stereoversioncontrol-exe | Infostealer/stereoversioncontrol.exe | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--get-logon-history-ps1 | get-logon-history.ps1 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

活動履歴なし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Saudi Arabia | Targeting text mentions saudi arabia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | メディア・報道 | 2019 and active since at least July 2018, targeting IT service providers in the Middle East.(Citation: Symantec Tortoiseshell 2019) [CURIUM](https://attack.mitre.org/groups/G1012) has since invested in building relationships with potential targets via social media over a period of months to establish trust and confidence before sending malware. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | [CURIUM](https://attack.mitre.org/groups/G1012) has exfiltrated data from a compromised machine.(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [CURIUM](https://attack.mitre.org/groups/G1012) has used IMAP and SMTPS for exfiltration via tools such as [IMAPLoader](https://attack.mitre.org/software/S1152).(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.002 | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [CURIUM](https://attack.mitre.org/groups/G1012) has used SMTPS to exfiltrate collected data from victims.(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [CURIUM](https://attack.mitre.org/groups/G1012) has leveraged PowerShell scripts for initial process execution and data gathering in victim environments.(Citation: Symantec Tortoiseshell 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [CURIUM](https://attack.mitre.org/groups/G1012) deploys information gathering tools focused on capturing IP configuration, running application, system information, and network connectivity information.(Citation: Symantec Tortoiseshell 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | [CURIUM](https://attack.mitre.org/groups/G1012) deployed mechanisms to check system time information following strategic website compromise attacks.(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | [CURIUM](https://attack.mitre.org/groups/G1012) has used strategic website compromise to infect victims with malware such as [IMAPLoader](https://attack.mitre.org/software/S1152).(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [CURIUM](https://attack.mitre.org/groups/G1012) has lured users into opening malicious files delivered via social media.(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [CURIUM](https://attack.mitre.org/groups/G1012) has been linked to web shells following likely server compromise as an initial access vector into victim networks.(Citation: Symantec Tortoiseshell 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [CURIUM](https://attack.mitre.org/groups/G1012) has used phishing with malicious attachments for initial access to victim environments.(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.003 | Spearphishing via Service | [CURIUM](https://attack.mitre.org/groups/G1012) has used social media to deliver malicious files to victims.(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [CURIUM](https://attack.mitre.org/groups/G1012) created domains to facilitate strategic website compromise and credential capture activities.(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [CURIUM](https://attack.mitre.org/groups/G1012) created virtual private server instances to facilitate use of malicious domains and other items.(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.004 | Server | [CURIUM](https://attack.mitre.org/groups/G1012) has created dedicated servers for command and control and exfiltration purposes.(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.006 | Web Services | [CURIUM](https://attack.mitre.org/groups/G1012) has compromised legitimate websites to enable strategic website compromise attacks.(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | [CURIUM](https://attack.mitre.org/groups/G1012) has established a network of fictitious social media accounts, including on Facebook and LinkedIn, to establish relationships with victims, often posing as an attractive woman.(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [CURIUM](https://attack.mitre.org/groups/G1012) has created dedicated email accounts for use with tools such as [IMAPLoader](https://attack.mitre.org/software/S1152).(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | [CURIUM](https://attack.mitre.org/groups/G1012) used malicious links to adversary-controlled resources for credential harvesting.(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.004 | Drive-by Target | [CURIUM](https://attack.mitre.org/groups/G1012) used strategic website compromise to fingerprint then target victims.(Citation: PWC Yellow Liderc 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 0件（`artifacts.csv`）

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
| source--tortoiseshell--a6829fde0253dab4 | README |  | 不明 | Tortoiseshell/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
