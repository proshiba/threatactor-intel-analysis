# Vanilla Tempest 脅威アクタープロファイル

- プロファイルID: `actor--vanilla-tempest`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Vanilla Tempestの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Vanilla Tempest**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DEV-0832 | Microsoft Threat Intelligence | exact | 高 | `source--microsoft-dev0832-vice-society-2022` | Microsoft explicitly states that DEV-0832 is also known as Vice Society and that DEV-0832 is now tracked as Vanilla Tempest. |
| Vice Society | Microsoft Threat Intelligence | exact | 高 | `source--microsoft-dev0832-vice-society-2022` | Microsoft explicitly states that DEV-0832 is also known as Vice Society and that DEV-0832 is now tracked as Vanilla Tempest. |
| VICE SPIDER | Microsoft Threat Intelligence | exact | 高 | `source--microsoft-dev0832-vice-society-2022` | Microsoft explicitly states that DEV-0832 is also known as Vice Society and that DEV-0832 is now tracked as Vanilla Tempest. |

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
| Fox Tempest | uses-service-of | Vanilla Tempest used Fox Tempest's malware-signing-as-a-service to obtain fraudulently signed Teams installers carrying Oyster and, in some intrusions, Rhysida ransomware. | 高 | `source--daily-1f90e973408c7fac0a86` |

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
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Vanilla Tempest | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Vanilla Tempest | canonical-name | 高 |  | https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-opportunistic-ransomware-campaigns-impacting-us-education-sector/<br>https://fourcore.io/blogs/rhysida-ransomware-history-ttp-adversary-emulation<br>https://detect.fyi/rhysida-ransomware-and-the-detection-opportunities-3599e9a02bb2 |
| misp-microsoft-activity-group | Vanilla Tempest | canonical-name | 高 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Vanilla Tempest | canonical-name | 高 |  |  |

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
| malware--blackcat | BlackCat | Ransomware payload used by DEV-0832. | 2022-07 | 2022-10 | 高 | `source--microsoft-dev0832-vice-society-2022` |
| malware--oyster | Oyster | Modular multistage backdoor deployed from trojanized Teams installers; it provides persistence, C2, host discovery, and follow-on delivery. | 2025-06 | 2025-10 | 高 | `source--daily-1f90e973408c7fac0a86` |
| malware--portstarter | PortStarter | Go backdoor used by DEV-0832 to alter firewall settings and open ports for C2. | 2022-07 | 2022-10 | 高 | `source--microsoft-dev0832-vice-society-2022` |
| malware--quantumlocker | QuantumLocker | Ransomware payload used by DEV-0832. | 2022-07 | 2022-10 | 高 | `source--microsoft-dev0832-vice-society-2022` |
| malware--redalert | RedAlert | Ransomware variant used by DEV-0832 in late September 2022. | 2022-07 | 2022-10 | 高 | `source--microsoft-dev0832-vice-society-2022` |
| malware--rhysida | Rhysida | Ransomware deployed by Vanilla Tempest in some intrusions using the same Fox Tempest-signed Teams-installer process. | 2025-06 | 2025-10 | 高 | `source--daily-1f90e973408c7fac0a86` |
| malware--systembc | SystemBC | Commodity backdoor and proxy used in DEV-0832 intrusions. | 2022-07 | 2022-10 | 高 | `source--microsoft-dev0832-vice-society-2022` |
| malware--zeppelin | Zeppelin | Ransomware family and basis of a Vice Society-branded variant used by DEV-0832. | 2022-07 | 2022-10 | 高 | `source--microsoft-dev0832-vice-society-2022` |

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
| Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | ransomware-extortion | 不明 | 不明 | 2024-09-19 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--260bd106ff4950e5430d | malware--blackcat, malware--rhysida, malware--zeppelin |  | victim--activity-rule--05f5af54d1d0b127513b | Vanilla Tempest(別名:DEV-0832、Vice Society)は米国の医療機関にINCランサムウェアを使用した攻撃を実施。 攻撃の一環として、Gootloader経由でネットワーク侵入し、SupperマルウェアやAnyDeskを使用した。 攻撃により患者データベースのアクセスが失われ、予定の変更を余儀なくされた。 Vanilla Tempestはランサムウェアのアフィリエイトであり、BlackCat、Quantum Locker、Zeppelin、Rhysidaなどのさまざまなランサムウェアを使用。 Vanilla Tempestは他にも教育、製造業、IT分野を標的にしている。 | 高 | `source--daily-c1b12b52abae4635e5ea` |
| Vanilla Tempest、Fox Tempest署名済みの偽TeamsインストーラでOysterを配布 | ransomware-extortion | 2025-06 | 2025-10 | 2025-10-17 |  | malware--oyster, malware--rhysida |  | victim--activity-rule--f98095af9352ea1ab8e2 | Vanilla Tempestは遅くとも2025年6月からFox TempestのMSaaSへトロイ化したMicrosoft Teamsインストーラを持ち込み、不正署名済みバイナリを正規広告、マルバタイジング、SEOポイズニング経由で配布した。偽MSTeamsSetup.exeはOyster（Broomstick）バックドアを展開し、観測事例の一部ではRhysidaランサムウェアも配備された。Microsoftは2025年10月に関連する200超の証明書を失効させた。 | 高 | `source--daily-1f90e973408c7fac0a86`, `source--daily-5287a969660d1bb7e309` |
| DEV-0832／Vanilla Tempestによる2022年の教育機関向け恐喝活動 | ransomware-extortion | 2022-07 | 2022-10 | 2022-10-25 |  | malware--blackcat, malware--portstarter, malware--quantumlocker, malware--redalert, malware--systembc, malware--zeppelin |  | victim--activity-rule--ad048966393781a542ab | MicrosoftはDEV-0832（現Vanilla Tempest、Vice Society）が2022年7月から10月に米国を中心とする教育機関へランサムウェアと恐喝活動を実施したと報告した。同集団はBlackCat、QuantumLocker、Zeppelin、Vice Society固有Zeppelin亜種、RedAlertを切り替え、SystemBCとPortStarterも使用した。過去の機会的攻撃には地方政府と小売も含まれる。 | 高 | `source--microsoft-dev0832-vice-society-2022` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | Vanilla Tempest | BlackCat, Rhysida, Zeppelin | 情報なし | 情報なし | 米国, 医療・ヘルスケア | 被害事例: Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | 高 |
| Vanilla Tempest、Fox Tempest署名済みの偽TeamsインストーラでOysterを配布 | Vanilla Tempest | Oyster, Rhysida | 情報なし | 情報なし | 情報なし | 被害事例: Vanilla Tempest、Fox Tempest署名済みの偽TeamsインストーラでOysterを配布 | 高 |
| DEV-0832／Vanilla Tempestによる2022年の教育機関向け恐喝活動 | Vanilla Tempest | BlackCat, PortStarter, QuantumLocker, RedAlert, SystemBC, Zeppelin | 情報なし | 情報なし | 政府・行政, 小売・ホスピタリティ | 被害事例: DEV-0832／Vanilla Tempestによる2022年の教育機関向け恐喝活動 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | 活動「Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-c1b12b52abae4635e5ea` |
| sectors | 政府・行政 | 活動「DEV-0832／Vanilla Tempestによる2022年の教育機関向け恐喝活動」の記述で標的として明示された産業。 | 2022-07 | 2022-10 | 中 | `source--microsoft-dev0832-vice-society-2022` |
| sectors | 医療・ヘルスケア | 活動「Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-c1b12b52abae4635e5ea` |
| sectors | 小売・ホスピタリティ | 活動「DEV-0832／Vanilla Tempestによる2022年の教育機関向け恐喝活動」の記述で標的として明示された産業。 | 2022-07 | 2022-10 | 中 | `source--microsoft-dev0832-vice-society-2022` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--260bd106ff4950e5430d | malware--blackcat, malware--rhysida, malware--zeppelin |  |  | encryption: Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | 不明 | 不明 | 2024-09-19 | 高 | `source--daily-c1b12b52abae4635e5ea` |
| 被害事例: DEV-0832／Vanilla Tempestによる2022年の教育機関向け恐喝活動 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--570d54d1d21fab6540a9 | malware--blackcat, malware--portstarter, malware--quantumlocker, malware--redalert, malware--systembc, malware--zeppelin |  |  | encryption: MicrosoftはDEV-0832（現Vanilla Tempest、Vice Society）が2022年7月から10月に米国を中心とする教育機関へランサムウェアと恐喝活動を実施したと報告した。 | 2022-07 | 2022-10 | 2022-10-25 | 高 | `source--microsoft-dev0832-vice-society-2022` |
| 被害事例: Vanilla Tempest、Fox Tempest署名済みの偽TeamsインストーラでOysterを配布 | 非公開 | anonymous | unknown | reported |  | malware--oyster, malware--rhysida |  |  | encryption: 偽MSTeamsSetup.exeはOyster（Broomstick）バックドアを展開し、観測事例の一部ではRhysidaランサムウェアも配備された。 | 2025-06 | 2025-10 | 2025-10-17 | 高 | `source--daily-1f90e973408c7fac0a86`, `source--daily-5287a969660d1bb7e309` |

## MITRE ATT&CK Matrixデータ

TTPなし

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
- 1 alias lead(s) remain non-canonical pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-5287a969660d1bb7e309 | Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害 | bleepingcomputer.com | 2025-10-17 | https://www.bleepingcomputer.com/news/microsoft/microsoft-disrupts-ransomware-attacks-targeting-teams-users/ | osint-report | TLP:CLEAR | 中 |
| source--daily-c1b12b52abae4635e5ea | Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | bleepingcomputer.com | 2024-09-19 | https://www.bleepingcomputer.com/news/microsoft/microsoft-vanilla-tempest-hit-healthcare-with-inc-ransomware/ | osint-report | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--vanilla-tempest--8a1291014fecfa23 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--vanilla-tempest--aaf7df4e91b7c721 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--vanilla-tempest--b98106625f6c9506 | vanilla tempest |  | 不明 | actor_profile/evidence/vanilla-tempest.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--vice-society--000985ff0c99e8d0 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--096e6a5ab122cf81 | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--378bd77c1a55d9ff | 2024 Trustwave Public Sector Threat Landscape |  | 2024 | summary/2024/2024_Trustwave_Public_Sector_Threat_Landscape.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--442c439e9d287b2f | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--4f2821a5f3b2de05 | Global Threat Report 2025 |  | 2025 | summary/2025/Global Threat Report 2025.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--640b74e7279a78c6 | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--6ec9e1c9c889aebe | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--77ff6bce69a046a1 | Semiannual+Ransomware+Report+ +H1+2024 |  | 2024 | cybercrime/2024/Semiannual+Ransomware+Report+-+H1+2024.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--78abb303ef02d1f9 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--a6e96b7f3b48daa9 | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--c6993c45964e8808 | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--vice-society--cbb2021149e25c3a | vice society |  | 不明 | actor_profile/evidence/vice-society.csv | structured-data | TLP:CLEAR | 中 |
| source--vice-society--e007f780b44a14fb | positive research 2023 eng |  | 2023 | summary/2023/positive-research-2023-eng.pdf | report | TLP:CLEAR | 中 |
| source--microsoft-dev0832-vice-society-2022 | DEV-0832 (Vice Society) opportunistic ransomware campaigns impacting US education sector | Microsoft Threat Intelligence | 2022-10-25 | https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-opportunistic-ransomware-campaigns-impacting-us-education-sector/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--daily-1f90e973408c7fac0a86 | Exposing Fox Tempest: A malware-signing service operation | Microsoft Threat Intelligence | 2026-05-19 | https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/ | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
