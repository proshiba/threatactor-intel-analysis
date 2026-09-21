# PROMETHIUM 脅威アクタープロファイル

- プロファイルID: `actor--strongpity`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

PROMETHIUMの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **PROMETHIUM**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| StrongPity | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | MITRE ATT&CK lists StrongPity as an Associated Group for G0056, but also states that the name has been used for both the group and its malware. It is therefore retained as an overlapping actor name, not as an exact software-to-actor identity assertion. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | Actor-specific reporting explicitly describes espionage or intelligence collection. | 高 | `source--mitre-attack-19-1`, `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description; not inferred from country or state sponsorship. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| NEODYMIUM | overlaps-with | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has demonstrated similarity to another activity group called [NEODYMIUM](https://attack.mitre.org/groups/G0055) due to overlapping victim and campaign characteristics.(Citation: Microsoft NEODYMIUM Dec 2016)(Citation: Microsoft SIR Vol 21)(Citation: Talos Promethium June 2020) | 高 | `source--mitre-attack-19-2` |

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
| etda-threat-group-cards | Promethium, StrongPity | canonical-name | 高 | Turkey | https://www.microsoft.com/security/blog/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/<br>https://securelist.com/on-the-strongpity-waterhole-attacks-targeting-italian-and-belgian-encryption-users/76147/<br>https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Magenta Dust | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | PROMETHIUM | canonical-name | 高 | TR | https://www.microsoft.com/security/blog/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/<br>https://www.virusbulletin.com/conference/vb2016/abstracts/last-minute-paper-strongpity-waterhole-attacks-targeting-italian-and-belgian-encryption-users<br>https://attack.mitre.org/groups/G0056/ |
| misp-microsoft-activity-group | Magenta Dust | canonical-name | 高 | TR | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | PROMETHIUM | canonical-name | 高 |  | https://blogs.technet.microsoft.com/mmpc/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/ |
| misp-mitre-enterprise-intrusion-set | PROMETHIUM - G0056 | mitre-external-id | 高 |  | http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf<br>https://attack.mitre.org/groups/G0056<br>https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html |
| misp-mitre-intrusion-set | PROMETHIUM - G0056 | mitre-external-id | 高 |  | http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf<br>https://attack.mitre.org/groups/G0056<br>https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | PROMETHIUM | canonical-name | 高 |  |  |

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
| malware--strongpity | StrongPity | [StrongPity](https://attack.mitre.org/software/S0491) is an information stealing malware used by [PROMETHIUM](https://attack.mitre.org/groups/G0056).(Citation: Bitdefender StrongPity June 2020)(Citation: Talos Promethium June 2020) | 2016-05-01T07:00:00.000Z | 2023-01-01T08:00:00.000Z | 高 | `source--mitre-attack-19-2` |
| malware--truvasys | Truvasys | [Truvasys](https://attack.mitre.org/software/S0178) is first-stage malware that has been used by [PROMETHIUM](https://attack.mitre.org/groups/G0056). It is a collection of modules written in the Delphi programming language. (Citation: Microsoft Win Defender Truvasys Sep 2017) (Citation: Microsoft NEODYMIUM Dec 2016) (Citation: Microsoft SIR Vol 21) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C0033 | campaign | 2016-05-01T07:00:00.000Z | 2023-01-01T08:00:00.000Z | 2026-05-12 |  | malware--strongpity |  |  | [C0033](https://attack.mitre.org/campaigns/C0033) was a [PROMETHIUM](https://attack.mitre.org/groups/G0056) campaign during which they used [StrongPity](https://attack.mitre.org/software/S0491) to target Android users. [C0033](https://attack.mitre.org/campaigns/C0033) was the first publicly documented mobile campaign for [PROMETHIUM](https://attack.mitre.org/groups/G0056), who previously used Windows-based techniques.(Citation: welivesec_strongpity) | 高 | `source--mitre-attack-19-2` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| C0033 | PROMETHIUM | StrongPity | 情報なし | 情報なし | 情報なし | 情報なし | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | トルコ | MITRE ATT&CKのGroup概要でPROMETHIUMの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| regions | 全世界 | MITRE ATT&CKのGroup概要でPROMETHIUMの標的範囲として全世界が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1036.004 | Masquerade Task or Service | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has named services to appear legitimate.(Citation: Talos Promethium June 2020)(Citation: Bitdefender StrongPity June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has disguised malicious installer files by bundling them with legitimate software installers.(Citation: Talos Promethium June 2020)(Citation: Bitdefender StrongPity June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has created admin accounts on a compromised host.(Citation: Bitdefender StrongPity June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1189 | Drive-by Compromise | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has used watering hole attacks to deliver malicious versions of legitimate installers.(Citation: Bitdefender StrongPity June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has attempted to get users to execute compromised installation files for legitimate software including compression applications, security software, browsers, file recovery applications, and other tools and utilities.(Citation: Talos Promethium June 2020)(Citation: Bitdefender StrongPity June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control, Persistence, Stealth | T1205.001 | Port Knocking | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has used a script that configures the knockd service and firewall to only accept C2 connections from systems that use a specified sequence of knock ports.(Citation: Bitdefender StrongPity June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has created new services and modified existing services for persistence.(Citation: Bitdefender StrongPity June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has used Registry run keys to establish persistence.(Citation: Talos Promethium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1553.002 | Code Signing | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has signed code with self-signed certificates.(Citation: Bitdefender StrongPity June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1587.002 | Code Signing Certificates | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has created self-signed certificates to sign malicious installers.(Citation: Bitdefender StrongPity June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1587.003 | Digital Certificates | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has created self-signed digital certificates for use in HTTPS C2 traffic.(Citation: Talos Promethium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| source--strongpity--1387165c1aa70400 | README |  | 不明 | StrongPity/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
