# Saint Bear 脅威アクタープロファイル

- プロファイルID: `actor--saint-bear`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Saint Bearの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Saint Bear**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Lorec53 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Storm-0587 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| TA471 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| UAC-0056 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Ember Bear | overlaps-with | [Ember Bear](https://attack.mitre.org/groups/G1003) is a Russian state-sponsored cyber espionage group that has been active since at least 2020, linked to Russia's General Staff Main Intelligence Directorate (GRU) 161st Specialist Training Center (Unit 29155).(Citation: CISA GRU29155 2024) [Ember Bear](https://attack.mitre.org/groups/G1003) has primarily focused operations against Ukrainian government and telecommunication entities, but has also operated against critical infrastructure entities in Europe and the Americas.(Citation: Cadet Blizzard emerges as novel threat actor) [Ember Bear](https://attack.mitre.org/groups/G1003) conducted the [WhisperGate](https://attack.mitre.org/software/S0689) destructive wiper attacks against Ukraine in early 2022.(Citation: CrowdStrike Ember Bear Profile March 2022)(Citation: Mandiant UNC2589 March 2022)(Citation: CISA GRU29155 2024) There is some confusion as to whether [Ember Bear](https://attack.mitre.org/groups/G1003) overlaps with another Russian-linked entity referred to as [Saint Bear](https://attack.mitre.org/groups/G1031). | 高 | `source--mitre-attack-19-2` |
| Ember Bear | distinct-from | MITRE ATT&CK 19.2 states that Saint Bear and Ember Bear were confused in past reporting but exhibit distinct behaviors, tools, and targeting; shared naming must not merge the clusters. | 高 | `source--mitre-attack-19-2` |

## 関連する企業・個人

関連エンティティなし

### エンティティ関係

確認された関係なし

### 法的措置

確認された法的措置なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | SaintBear, Lorec53 | canonical-name | 高 | Russia | https://nsfocusglobal.com/apt-retrospection-lorec53-an-active-russian-hack-group-launched-phishing-attacks-against-georgian-government/<br>https://www.crowdstrike.com/blog/who-is-ember-bear/<br>https://services.google.com/fh/files/blogs/google_fog_of_war_research_report.pdf |
| cert-ua-uac-index | UAC-0056 | single-alias-intersection | 中 |  | https://cert.gov.ua/article/38374<br>https://cert.gov.ua/article/703548<br>https://cert.gov.ua/article/619229 |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | SaintBear | canonical-name | 高 | RU | https://malpedia.caad.fkie.fraunhofer.de/details/win.graphsteel<br>https://cert.gov.ua/article/38374<br>https://blog.malwarebytes.com/threat-intelligence/2022/04/new-uac-0056-activity-theres-a-go-elephant-in-the-room/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Ember Bear - G1003 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G1003<br>https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/<br>https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf |
| misp-mitre-enterprise-intrusion-set | Saint Bear - G1031 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1031<br>https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/<br>https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/ |
| misp-mitre-intrusion-set | Ember Bear - G1003 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G1003<br>https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/<br>https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf |
| misp-mitre-intrusion-set | Saint Bear - G1031 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1031<br>https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/<br>https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/ |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Saint Bear | canonical-name | 高 | RU |  |

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
| malware--outsteel | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) is a file uploader and document stealer developed with the scripting language AutoIT that has been used by [Saint Bear](https://attack.mitre.org/groups/G1031) since at least March 2021.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--saint-bot | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) is a .NET downloader that has been used by [Saint Bear](https://attack.mitre.org/groups/G1031) since at least March 2021.(Citation: Malwarebytes Saint Bot April 2021)(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ウクライナ | [Saint Bear](https://attack.mitre.org/groups/G1031) is a Russian-nexus threat actor active since early 2021, primarily targeting entities in Ukraine and Georgia. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| countries | ジョージア | MITRE ATT&CKのGroup概要でSaint Bearの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.002 | Software Packing | [Saint Bear](https://attack.mitre.org/groups/G1031) clones .NET assemblies from other .NET binaries as well as cloning code signing certificates from other software to obfuscate the initial loader payload.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Saint Bear](https://attack.mitre.org/groups/G1031) initial payloads included encoded follow-on payloads located in the resources file of the first-stage loader.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059 | Command and Scripting Interpreter | [Saint Bear](https://attack.mitre.org/groups/G1031) has used the Windows Script Host (wscript) to execute intermediate files written to victim machines.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.001 | PowerShell | [Saint Bear](https://attack.mitre.org/groups/G1031) relies extensively on PowerShell execution from malicious attachments and related content to retrieve and execute follow-on payloads.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.003 | Windows Command Shell | [Saint Bear](https://attack.mitre.org/groups/G1031) initial loaders will also drop a malicious Windows batch file, available via open source GitHub repositories, that disables Microsoft Defender functionality.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.007 | JavaScript | [Saint Bear](https://attack.mitre.org/groups/G1031) has delivered malicious Microsoft Office files containing an embedded JavaScript object that would, on execution, download and execute [OutSteel](https://attack.mitre.org/software/S1017) and [Saint Bot](https://attack.mitre.org/software/S1018).(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Saint Bear](https://attack.mitre.org/groups/G1031) will leverage malicious Windows batch scripts to modify registry values associated with Windows Defender functionality.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1203 | Exploitation for Client Execution | [Saint Bear](https://attack.mitre.org/groups/G1031) has leveraged vulnerabilities in client applications such as CVE-2017-11882 in Microsoft Office to enable code execution in victim environments.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.001 | Malicious Link | [Saint Bear](https://attack.mitre.org/groups/G1031) has, in addition to email-based phishing attachments, used malicious websites masquerading as legitimate entities to host links to malicious files for user execution.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 )(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [Saint Bear](https://attack.mitre.org/groups/G1031) relies on user interaction and execution of malicious attachments and similar for initial execution on victim systems.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | [Saint Bear](https://attack.mitre.org/groups/G1031) contains several anti-analysis and anti-virtualization checks.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1553.002 | Code Signing | [Saint Bear](https://attack.mitre.org/groups/G1031) has used an initial loader malware featuring a legitimate code signing certificate associated with "Electrum Technologies GmbH."(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Saint Bear](https://attack.mitre.org/groups/G1031) uses a variety of file formats, such as Microsoft Office documents, ZIP archives, PDF documents, and other items as phishing attachments for initial access.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583.006 | Web Services | [Saint Bear](https://attack.mitre.org/groups/G1031) has leveraged the Discord content delivery network to host malicious content for retrieval during initial access operations.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1589.002 | Email Addresses | [Saint Bear](https://attack.mitre.org/groups/G1031) gathered victim email information in advance of phishing operations for targeted attacks.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1608.001 | Upload Malware | [Saint Bear](https://attack.mitre.org/groups/G1031) has used the Discord content delivery network for hosting malicious content referenced in links and emails.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1684.001 | Impersonation | [Saint Bear](https://attack.mitre.org/groups/G1031) has impersonated government and related entities in both phishing activity and developing web sites with malicious links that mimic legitimate resources.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1685 | Disable or Modify Tools | [Saint Bear](https://attack.mitre.org/groups/G1031) will modify registry entries and scheduled task objects associated with Windows Defender to disable its functionality.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
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
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--saint-bear--7d2c5e58600dbc59 | saint bear |  | 不明 | actor_profile/evidence/saint-bear.csv | structured-data | TLP:CLEAR | 中 |
| source--saint-bear--93e747009ef920ce | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--saint-bear--55314119aef6803a | search |  | 不明 | ui/api/v1/search.json | structured-data | TLP:CLEAR | 中 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
