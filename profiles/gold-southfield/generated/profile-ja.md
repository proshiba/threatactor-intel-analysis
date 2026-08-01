# GOLD SOUTHFIELD 脅威アクタープロファイル

- プロファイルID: `actor--gold-southfield`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

GOLD SOUTHFIELDの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **GOLD SOUTHFIELD**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Pinchy Spider | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) is a financially motivated threat group active since at least 2018 that operates the [REvil](https://attack.mitre.org/software/S0496) Ransomware-as-a Service (RaaS). [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) provides backend infrastructure for affiliates recruited on underground forums to perpetrate high value deployments. By early 2020, [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) started capitalizing on the new trend of stealing data and further extorting the victim to pay for their data to not get publicly leaked.(Citation: Secureworks REvil September 2019)(Citation: Secureworks GandCrab and REvil September 2019)(Citation: Secureworks GOLD SOUTHFIELD)(Citation: CrowdStrike Evolution of Pinchy Spider July 2021) |
| Capability | REvil, GandCrab, ConnectWise |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Pinchy Spider, Gold Southfield | canonical-name | 高 | Russia | https://www.crowdstrike.com/blog/pinchy-spider-adopts-big-game-hunting/<br>https://krebsonsecurity.com/2019/07/whos-behind-the-gandcrab-ransomware/<br>https://www.secureworks.com/blog/revil-the-gandcrab-connection |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | PINCHY SPIDER | single-alias-intersection | 中 |  | https://www.crowdstrike.com/resources/reports/2019-crowdstrike-global-threat-report/<br>https://www.crowdstrike.com/blog/pinchy-spider-adopts-big-game-hunting/<br>https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf |
| misp-threat-actor | GOLD SOUTHFIELD | canonical-name | 高 |  | http://www.secureworks.com/research/threat-profiles/gold-southfield<br>https://www.secureworks.com/research/revil-sodinokibi-ransomware<br>https://www.secureworks.com/blog/how-cyber-adversaries-are-adapting-to-exploit-the-global-pandemic |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | GOLD SOUTHFIELD - G0115 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0115<br>https://www.crowdstrike.com/blog/the-evolution-of-revil-ransomware-and-pinchy-spider/<br>https://www.secureworks.com/blog/revil-the-gandcrab-connection |
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
| malware--revil | REvil | [REvil](https://attack.mitre.org/software/S0496) is a ransomware family that has been linked to the [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) group and operated as ransomware-as-a-service (RaaS) since at least April 2019. [REvil](https://attack.mitre.org/software/S0496), which as been used against organizations in the manufacturing, transportation, and electric sectors, is highly configurable and shares code similarities with the GandCrab RaaS.(Citation: Secureworks REvil September 2019)(Citation: Intel 471 REvil March 2020)(Citation: Group IB Ransomware May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--gandcrab | GandCrab | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--connectwise | ConnectWise | [ConnectWise](https://attack.mitre.org/software/S0591) is a legitimate remote administration tool that has been used since at least 2016 by threat actors including [MuddyWater](https://attack.mitre.org/groups/G0069) and [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) to connect to and conduct lateral movement in target environments.(Citation: Anomali Static Kitten February 2021)(Citation: Trend Micro Muddy Water March 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 全世界 | 構造化OSINTの被害地域フィールドでGOLD SOUTHFIELDの標的範囲として全世界が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.010 | Command Obfuscation | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has executed base64 encoded PowerShell scripts on compromised hosts.(Citation: Tetra Defense Sodinokibi March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has staged and executed PowerShell scripts on compromised hosts.(Citation: Tetra Defense Sodinokibi March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has used the remote monitoring and management tool ConnectWise to obtain screen captures from victim's machines.(Citation: Tetra Defense Sodinokibi March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has used publicly-accessible RDP and remote management and monitoring (RMM) servers to gain access to victim machines.(Citation: Secureworks REvil September 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has exploited Oracle WebLogic vulnerabilities for initial compromise.(Citation: Secureworks REvil September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has distributed ransomware by backdooring software installers via a strategic web compromise of the site hosting Italian WinRAR.(Citation: Secureworks REvil September 2019)(Citation: Secureworks GandCrab and REvil September 2019)(Citation: Secureworks GOLD SOUTHFIELD) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has breached Managed Service Providers (MSP's) to deliver malware to MSP customers.(Citation: Secureworks REvil September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has used the cloud-based remote management and monitoring tool "ConnectWise Control" to deploy [REvil](https://attack.mitre.org/software/S0496).(Citation: Tetra Defense Sodinokibi March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has conducted malicious spam (malspam) campaigns to gain access to victim's machines.(Citation: Secureworks REvil September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 29件（`artifacts.csv`）

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
| source--gold-southfield--fc951a6fab9446cc | gold southfield |  | 不明 | actor_profile/evidence/gold-southfield.csv | structured-data | TLP:CLEAR | 中 |
| source--gold-southfield--4c4dbc8dbbf23374 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--gold-southfield--f83e4ccccd70ad2e | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--gold-southfield--0f9ae07a5b48f56e | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--gold-southfield--98ce42cf30c8ee27 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--gold-southfield--bec5eb8744affae8 | 2022 Global Threat Report |  | 2022 | summary/2022/2022 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--gold-southfield--5360439e83fd4c54 | 2022 Apr Ransomware Report v3 |  | 2022 | summary/2022/2022-Apr-Ransomware-Report-v3.pdf | report | TLP:CLEAR | 中 |
| source--gold-southfield--fc919b8be42aed19 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--gold-southfield--1109cf73695e601f | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--gold-southfield--bc9c885f45bc6451 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
