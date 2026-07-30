# Winter Vivern 脅威アクタープロファイル

- プロファイルID: `actor--winter-vivern`
- 状態: draft
- 更新日時: 2026-07-29T23:13:55Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Winter Vivernの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Winter Vivern**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| TA473 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UAC-0114 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | Winter Vivern is a group linked to Russian and Belorussian interests active since at least 2020 targeting various European government and NGO entities, along with sporadic targeting of Indian and US victims. The group leverages a combination of document-based phishing activity and server-side exploitation for initial access, leveraging adversary-controlled and -created infrastructure for follow-on command and control.(Citation: DomainTools WinterVivern 2021)(Citation: SentinelOne WinterVivern 2023)(Citation: CERT-UA WinterVivern 2023)(Citation: ESET WinterVivern 2023)(Citation: Proofpoint WinterVivern 2023) |
| Capability | APERETIF |
| Infrastructure |  |
| Victim | Lithuania, India, Vatican, Slovakia, Poland, Ukraine, Italy, India, sectors: govt., telecom |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Winter Vivern | canonical-name | 高 |  | https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/<br>https://www.domaintools.com/resources/blog/winter-vivern-a-look-at-re-crafted-government-maldocs/<br>https://lab52.io/blog/winter-vivern-all-summer/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Winter Vivern | canonical-name | 高 | RU | https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/<br>https://www.domaintools.com/resources/blog/winter-vivern-a-look-at-re-crafted-government-maldocs<br>https://www.welivesecurity.com/en/eset-research/winter-vivern-exploits-zero-day-vulnerability-roundcube-webmail-servers/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Winter Vivern - G1035 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1035<br>https://cert.gov.ua/article/3761104<br>https://www.domaintools.com/resources/blog/winter-vivern-a-look-at-re-crafted-government-maldocs/ |
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
| malware--aperetif | APERETIF | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| countries | イタリア | Targeting text mentions italy. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | インド | Targeting text mentions india. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | ウクライナ | Targeting text mentions ukraine. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ウズベキスタン | 構造化OSINTの被害国フィールドでWinter Vivernの標的・被害国としてウズベキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ジョージア | 構造化OSINTの被害国フィールドでWinter Vivernの標的・被害国としてジョージアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スロバキア | レビュー済みアクターマッピングの標的欄に記録されたスロバキアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | チュニジア | 構造化OSINTの被害国フィールドでWinter Vivernの標的・被害国としてチュニジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでWinter Vivernの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ポーランド | Targeting text mentions poland. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | モルドバ | 構造化OSINTの被害国フィールドでWinter Vivernの標的・被害国としてモルドバが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | リトアニア | Targeting text mentions lithuania. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | Winter Vivern is a group linked to Russian and Belorussian interests active since at least 2020 targeting various European government and NGO entities, along with sporadic targeting of Indian and US victims. | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ウクライナ、スロバキア、ポーランド、モルドバで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | MITRE ATT&CKのGroup概要でWinter Vivernの標的範囲として欧州が明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 非営利・市民社会 | Winter Vivern is a group linked to Russian and Belorussian interests active since at least 2020 targeting various European government and NGO entities, along with sporadic targeting of Indian and US victims. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | Winter Vivern is a group linked to Russian and Belorussian interests active since at least 2020 targeting various European government and NGO entities, along with sporadic targeting of Indian and US victims. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Exfiltration | T1020 | Automated Exfiltration | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP.(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [Winter Vivern](https://attack.mitre.org/groups/G1035) PowerShell scripts execute `whoami` to identify the executing user.(Citation: SentinelOne WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [Winter Vivern](https://attack.mitre.org/groups/G1035) created specially-crafted documents mimicking legitimate government or similar documents during phishing campaigns.(Citation: SentinelOne WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [Winter Vivern](https://attack.mitre.org/groups/G1035) has distributed malicious scripts and executables mimicking virus scanners.(Citation: SentinelOne WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP.(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Winter Vivern](https://attack.mitre.org/groups/G1035) executed PowerShell scripts that would subsequently attempt to establish persistence by creating scheduled tasks objects to periodically retrieve and execute remotely-hosted payloads.(Citation: DomainTools WinterVivern 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056 | Input Capture | oitationfor Client Execution T1203 Persistence: ValidAccounts T1078 Credential Access: Exploitationfor Credential Access T1212 Credential Access: Input Capture T1056 Discovery:FileandDirectoryDiscovery T1083 Collection:Email Collection T1114 CommandandControl:Non-StandardPort T1571 12 CTA RU 2024 0217 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--winter-vivern--1d914b49257b6f86` |
| Collection, Credential Access | T1056.003 | Web Portal Capture | [Winter Vivern](https://attack.mitre.org/groups/G1035) registered and hosted domains to allow for creation of web pages mimicking legitimate government email logon sites to collect logon information.(Citation: SentinelOne WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | [Winter Vivern](https://attack.mitre.org/groups/G1035) used XLM 4.0 macros for initial code execution for malicious document files.(Citation: DomainTools WinterVivern 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Winter Vivern](https://attack.mitre.org/groups/G1035) passed execution from document macros to PowerShell scripts during initial access operations.(Citation: DomainTools WinterVivern 2021) [Winter Vivern](https://attack.mitre.org/groups/G1035) used batch scripts that called PowerShell commands as part of initial access and installation operations.(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Winter Vivern](https://attack.mitre.org/groups/G1035) distributed Windows batch scripts disguised as virus scanners to prompt download of malicious payloads using built-in system tools.(Citation: SentinelOne WinterVivern 2023)(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered malicious JavaScript to exploit targets when exploiting Roundcube Webmail servers.(Citation: ESET WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Winter Vivern](https://attack.mitre.org/groups/G1035) uses HTTP and HTTPS protocols for exfiltration and command and control activity.(Citation: SentinelOne WinterVivern 2023)(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | B—MITREATT&CKTechniques Tactic:Technique ATT&CKCode Initial Access: Phishing T1566 Execution: Exploitationfor Client Execution T1203 Persistence: ValidAccounts T1078 Credential Access: Exploitationfor Credential Access T1212 Credential Access: Input Capture T1056 Discovery:FileandDirectoryDiscovery T1083 Collection:Email Collection T1114 CommandandControl:Non-StandardPort T1571 12 CTA RU 2024 0217 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--winter-vivern--1d914b49257b6f86` |
| Discovery | T1082 | System Information Discovery | [Winter Vivern](https://attack.mitre.org/groups/G1035) script execution includes basic victim information gathering steps which are then transmitted to command and control servers.(Citation: DomainTools WinterVivern 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered malicious JavaScript payloads capable of listing folders and emails in exploited email servers.(Citation: ESET WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--winter-vivern--1d914b49257b6f86` |
| Command And Control | T1105 | Ingress Tool Transfer | [Winter Vivern](https://attack.mitre.org/groups/G1035) executed PowerShell scripts to create scheduled tasks to retrieve remotely-hosted payloads.(Citation: DomainTools WinterVivern 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered PowerShell scripts capable of taking screenshots of victim machines.(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114 | Email Collection | al Access: Exploitationfor Credential Access T1212 Credential Access: Input Capture T1056 Discovery:FileandDirectoryDiscovery T1083 Collection:Email Collection T1114 CommandandControl:Non-StandardPort T1571 12 CTA RU 2024 0217 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--winter-vivern--1d914b49257b6f86` |
| Collection | T1114.001 | Local Email Collection | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered malicious JavaScript payloads capable of exfiltrating email messages from exploited email servers.(Citation: ESET WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP.(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered exploit payloads via base64-encoded payloads in malicious email messages.(Citation: ESET WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | [Winter Vivern](https://attack.mitre.org/groups/G1035) created dedicated web pages mimicking legitimate government websites to deliver malicious fake anti-virus software.(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Winter Vivern](https://attack.mitre.org/groups/G1035) has exploited known and zero-day vulnerabilities in software usch as Roundcube Webmail servers and the "Follina" vulnerability.(Citation: ESET WinterVivern 2023)(Citation: Proofpoint WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | f99120ae6525c0eaf37de32e AppendixB—MITREATT&CKTechniques Tactic:Technique ATT&CKCode Initial Access: Phishing T1566 Execution: Exploitationfor Client Execution T1203 Persistence: ValidAccounts T1078 Credential Access: Exploitationfor Credential Access T1212 Credential Access: Input Capture T1056 Discovery:FileandDirectoryDiscovery T1083 Collection:Email Collection T1114 CommandandControl:Non-StandardPort T1571 12 CTA RU 2024 0217 RecordedFut |  |  | 不明 | 不明 | 中 | `source--winter-vivern--1d914b49257b6f86` |
| Execution | T1204.001 | Malicious Link | [Winter Vivern](https://attack.mitre.org/groups/G1035) has mimicked legitimate government-related domains to deliver malicious webpages containing links to documents or other content for user execution.(Citation: SentinelOne WinterVivern 2023)(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1212 | Exploitation for Credential Access | Access: Phishing T1566 Execution: Exploitationfor Client Execution T1203 Persistence: ValidAccounts T1078 Credential Access: Exploitationfor Credential Access T1212 Credential Access: Input Capture T1056 Discovery:FileandDirectoryDiscovery T1083 Collection:Email Collection T1114 CommandandControl:Non-StandardPort T1571 12 CTA RU 2024 0217 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--winter-vivern--1d914b49257b6f86` |
| Initial Access | T1566 | Phishing | 5314199a26ea22b3e9ecdfd06fae74483deb9ef0245aefdc72f99120ae6525c0eaf37de32e AppendixB—MITREATT&CKTechniques Tactic:Technique ATT&CKCode Initial Access: Phishing T1566 Execution: Exploitationfor Client Execution T1203 Persistence: ValidAccounts T1078 Credential Access: Exploitationfor Credential Access T1212 Credential Access: Input Capture T1056 Discovery:FileandDirectoryDiscovery T1083 Collection:Email Collection T1114 CommandandControl:Non- |  |  | 不明 | 不明 | 中 | `source--winter-vivern--1d914b49257b6f86` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Winter Vivern](https://attack.mitre.org/groups/G1035) leverages malicious attachments delivered via email for initial access activity.(Citation: DomainTools WinterVivern 2021)(Citation: SentinelOne WinterVivern 2023)(Citation: CERT-UA WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | ess T1212 Credential Access: Input Capture T1056 Discovery:FileandDirectoryDiscovery T1083 Collection:Email Collection T1114 CommandandControl:Non-StandardPort T1571 12 CTA RU 2024 0217 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--winter-vivern--1d914b49257b6f86` |
| Resource Development | T1583.001 | Domains | [Winter Vivern](https://attack.mitre.org/groups/G1035) registered domains mimicking other entities throughout various campaigns.(Citation: DomainTools WinterVivern 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [Winter Vivern](https://attack.mitre.org/groups/G1035) used adversary-owned and -controlled servers to host web vulnerability scanning applications.(Citation: SentinelOne WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.006 | Web Services | [Winter Vivern](https://attack.mitre.org/groups/G1035) has used compromised WordPress sites to host malicious payloads for download.(Citation: SentinelOne WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | [Winter Vivern](https://attack.mitre.org/groups/G1035) has used remotely-hosted instances of the Acunetix vulnerability scanner.(Citation: SentinelOne WinterVivern 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 5件
- IOC観測: 5件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
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
| source--winter-vivern--1d914b49257b6f86 | Russia Aligned TAG 70 Targets European Government and Military Mail Servers in New Espionage Campaign |  | 不明 | Winter Vivern/Russia-Aligned TAG-70 Targets European Government and Military Mail Servers in New Espionage Campaign.pdf | report | TLP:CLEAR | 中 |
| source--winter-vivern--90b785e2badbc71a | readme |  | 不明 | Winter Vivern/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
