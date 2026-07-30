# Vice Society 脅威アクタープロファイル

- プロファイルID: `actor--vice-society`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Vice Societyの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Vice Society**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

The repository mapping workbook places this actor in the Russia worksheet.

- 国: Russia
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
| Adversary |  |
| Capability | PrintNightmare, HelloKitty and Zeppelin ransomware |
| Infrastructure |  |
| Victim | Education and research institutes |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Vanilla Tempest | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Vanilla Tempest | canonical-name | 高 |  | https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-opportunistic-ransomware-campaigns-impacting-us-education-sector/<br>https://fourcore.io/blogs/rhysida-ransomware-history-ttp-adversary-emulation<br>https://detect.fyi/rhysida-ransomware-and-the-detection-opportunities-3599e9a02bb2 |
| misp-microsoft-activity-group | Vanilla Tempest | canonical-name | 高 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
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
| malware--hellokitty-and-zeppelin-ransomware | HelloKitty and Zeppelin ransomware | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--printnightmare | PrintNightmare | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | ransomware-extortion | 不明 | 不明 | 2024-09-19 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--260bd106ff4950e5430d |  |  | victim--activity-rule--ff2191c48399b7a73241 | Vanilla Tempest(別名:DEV-0832、Vice Society)は米国の医療機関にINCランサムウェアを使用した攻撃を実施。 攻撃の一環として、Gootloader経由でネットワーク侵入し、SupperマルウェアやAnyDeskを使用した。 攻撃により患者データベースのアクセスが失われ、予定の変更を余儀なくされた。 Vanilla Tempestはランサムウェアのアフィリエイトであり、BlackCat、Quantum Locker、Zeppelin、Rhysidaなどのさまざまなランサムウェアを使用。 Vanilla Tempestは他にも教育、製造業、IT分野を標的にしている。 | 中 | `source--daily-c1b12b52abae4635e5ea` |
| Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害 | ransomware-extortion | 不明 | 不明 | 2025-10-17 | target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--e7608f51421ca8b1e297 |  |  | victim--activity-rule--aa28ddb3998708678c1e | Microsoftは10月上旬のRhysida連携攻撃を妨害し、偽Teamsインストーラ署名に使われた200超の証明書を失効させた。 攻撃者Vanilla Tempest（Vice Society/VICE SPIDER）はteams-install[.]top等の偽サイトでOysterバックドアを配布した。 配布は9月下旬のマルバタイジングやSEOポイズニングで行われ、正規と同名MSTeamsSetup[.]exeで利用者を欺いた。 悪性インストーラは署名済みOysterを展開し、遠隔操作・情報窃取・追加ペイロード投下を可能にする。 同集団は金銭目的で教育・医療・IT・製造を頻繁に標的化し、近年は主にRhysidaを展開している。 | 中 | `source--daily-5287a969660d1bb7e309` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | 活動「Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-c1b12b52abae4635e5ea` |
| sectors | 医療・ヘルスケア | 活動「Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5287a969660d1bb7e309`, `source--daily-c1b12b52abae4635e5ea` |
| sectors | 製造・産業 | 活動「Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5287a969660d1bb7e309` |
| sectors | 教育・研究 | 活動「Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5287a969660d1bb7e309` |
| sectors | Education and Research | Targeting text indicates the Education and Research sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--e7608f51421ca8b1e297 |  |  |  | encryption: Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害 | 不明 | 不明 | 2025-10-17 | 中 | `source--daily-5287a969660d1bb7e309` |
| 被害事例: Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--260bd106ff4950e5430d |  |  |  | encryption: Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | 不明 | 不明 | 2024-09-19 | 中 | `source--daily-c1b12b52abae4635e5ea` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 27件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- Structured OSINT country metadata is disjoint from the profile attribution; see osint-crosscheck.json and retain both assessments pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-5287a969660d1bb7e309 | Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害 | bleepingcomputer.com | 2025-10-17 | https://www.bleepingcomputer.com/news/microsoft/microsoft-disrupts-ransomware-attacks-targeting-teams-users/ | osint-report | TLP:CLEAR | 中 |
| source--daily-c1b12b52abae4635e5ea | Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | bleepingcomputer.com | 2024-09-19 | https://www.bleepingcomputer.com/news/microsoft/microsoft-vanilla-tempest-hit-healthcare-with-inc-ransomware/ | osint-report | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
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
| source--vice-society--e2e1bc5b0435feaa | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
