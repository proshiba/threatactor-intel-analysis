# BITTER 脅威アクタープロファイル

プロファイルID: `actor--bitter`  
状態: draft  
更新日時: 2026-07-25T14:07:08Z  
構造バージョン: 1.0.0

## エグゼクティブサマリー

BITTERの標準化プロファイル。リポジトリ内の専用資料8件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **BITTER**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| T-APT-17 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| APT-C-08 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 63; mapping requires review. |
| Manling Flower (Manlinghua) | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 63; mapping requires review. |
| offshore APT organization from South Asia | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 63; mapping requires review. |

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
| Adversary | [BITTER](https://attack.mitre.org/groups/G1002) is a suspected South Asian cyber espionage threat group that has been active since at least 2013. [BITTER](https://attack.mitre.org/groups/G1002) has targeted government, energy, and engineering organizations in Pakistan, China, Bangladesh, and Saudi Arabia.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) |
| Capability | ZxxZ, BitterRAT, ArtraDownloader, SlideRAT |
| Infrastructure |  |
| Victim | Pakistan, Saudi Arabia, PRC |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Bitter | canonical-name | 高 | [South Asia] | https://unit42.paloaltonetworks.com/multiple-artradownloader-variants-used-by-bitter-to-target-pakistan/<br>https://www.proofpoint.com/us/blog/threat-insight/bitter-end-unraveling-eight-years-espionage-antics-part-one<br>https://www.threatray.com/blog/the-bitter-end-unraveling-eight-years-of-espionage-antics-part-two |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | HAZY TIGER | canonical-name | 高 | IN | https://www.bitdefender.com/files/News/CaseStudies/study/352/Bitdefender-PR-Whitepaper-BitterAPT-creat4571-en-EN-GenericUse.pdf<br>https://mp.weixin.qq.com/s/8j_rHA7gdMxY1_X8alj8Zg<br>https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/cyber-year-in-retrospect/yir-cyber-threats-report-download.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | BITTER - G1002 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1002<br>https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html<br>https://www.forcepoint.com/blog/x-labs/bitter-targeted-attack-against-pakistan |
| misp-360net | 蔓灵花 - APT-C-08 | single-alias-intersection | 中 | india | https://apt.360.net/report/apts/5.html |

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
| malware--zxxz | ZxxZ | [ZxxZ](https://attack.mitre.org/software/S1013) is a trojan written in Visual C++ that has been used by [BITTER](https://attack.mitre.org/groups/G1002) since at least August 2021, including against Bangladeshi government personnel.(Citation: Cisco Talos Bitter Bangladesh May 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--bitterrat | BitterRAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--artradownloader | ArtraDownloader | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sliderat | SlideRAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| countries | Pakistan | Targeting text mentions pakistan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | /iMessage delivery T1539 Steal Web Session Cookie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious Link Phishing link click |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Command And Control | T1095 | Non-Application Layer Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1111 | Multi-Factor Authentication Interception | hnique ID Technique Name Usage T1566.002 Spearphishing Link WhatsApp/iMessage delivery T1539 Steal Web Session Cookie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious Link Phishing link click |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | okie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious Link Phishing link click |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1539 | Steal Web Session Cookie | .]com iMessage phishing sender MITRE ATT&CK Mapping Technique ID Technique Name Usage T1566.002 Spearphishing Link WhatsApp/iMessage delivery T1539 Steal Web Session Cookie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious Link Phishing link click |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Execution | T1559.002 | Dynamic Data Exchange | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | 40 Email Addresses Email Usage idapple[.]review@icloud[.]com iMessage phishing sender MITRE ATT&CK Mapping Technique ID Technique Name Usage T1566.002 Spearphishing Link WhatsApp/iMessage delivery T1539 Steal Web Session Cookie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Command And Control | T1568 | Dynamic Resolution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573 | Encrypted Channel | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 468件
- IOC観測: 627件
- 複数攻撃で観測: 0件
- 要レビュー候補: 64件
- 非IOC artifact観測: 51件（`artifacts.csv`）

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
| source--bitter--97af4adeea02b675 | Android Bitter ioc |  | 不明 | bitter/2020/Android-Bitter-ioc.txt | text-data | TLP:CLEAR | 中 |
| source--bitter--9de41446a9a72262 | Bitdefender PR Whitepaper BitterAPT creat4571 en EN GenericUse |  | 不明 | bitter/2020/Bitdefender-PR-Whitepaper-BitterAPT-creat4571-en-EN-GenericUse.pdf | report | TLP:CLEAR | 中 |
| source--bitter--4b3b9e7d26c1cf64 | Quarterly Adversarial Threat Report Q2 2022 |  | 2022 | bitter/2022/Quarterly-Adversarial-Threat-Report-Q2-2022.pdf | report | TLP:CLEAR | 中 |
| source--bitter--717acb7afca6cd59 | README |  | 不明 | bitter/2022/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--bitter--d98102cdd748dedd | Espionage for repression forensic analysis of a cross border hack for hire campaign targeting civil society in MENA 2026 |  | 2026 | bitter/2026/Espionage-for-repression-forensic-analysis-of-a-cross-border-hack-for-hire-campaign-targeting-civil-society-in-MENA-2026.pdf | report | TLP:CLEAR | 中 |
| source--bitter--2cfec8a10f89e0b3 | Rotten Apple An Invasive Threat Actor Targeting Civil Society in Lebanon |  | 不明 | bitter/2026/Rotten-Apple_-An-Invasive-Threat-Actor-Targeting-Civil-Society-in-Lebanon.pdf | report | TLP:CLEAR | 中 |
| source--bitter--88ab3c36687131db | readme |  | 不明 | bitter/2026/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--bitter--f28edd1d5cabb4e9 | Inf |  | 不明 | bitter/Inf.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
