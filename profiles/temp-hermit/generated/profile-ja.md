# TEMP.Hermit 脅威アクタープロファイル

- プロファイルID: `actor--temp-hermit`
- 状態: draft
- 更新日時: 2026-09-20T13:48:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

TEMP.Hermitの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TEMP.Hermit**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| HERMIT NEPTUNE | catalog / Google Threat Intelligence Group | exact | 高 | `source--actor-mapping-workbook`, `source--gtig-unified-actor-naming-2026` | Alias scope must be reviewed before publication. GTIG's July 2026 table explicitly maps the previous name to this new unified name. Exactness is within GTIG's taxonomy; other vendors may use different collection boundaries. |

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
| APT38 | overlaps-with | APT38 and TEMP.Hermit have shared resources, but Mandiant describes their activity as disparate and tracks them separately. | 高 | `source--mandiant-apt38-temp-hermit-boundary-2018` |
| APT38 | overlaps-with | APT38 and TEMP.Hermit have shared resources, but Mandiant describes their activity as disparate and tracks them separately. | 高 | `source--mandiant-apt38-temp-hermit-boundary-2018` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | VOLGMER, PEACHPIT |
| Infrastructure |  |
| Victim | Korean Peninsula, US Aerospace, SWIFT-fraud operations in East Asia |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-09-20T13:47:46Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | HERMIT NEPTUNE | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system |
| etda-threat-group-cards | Bluenoroff, APT 38, Stardust Chollima | canonical-name | 高 | North Korea | https://threatpost.com/lazarus-apt-spinoff-linked-to-banking-hacks/124746/<br>https://www.microsoft.com/en-us/security/blog/2024/11/22/microsoft-shares-latest-intelligence-on-north-korean-and-chinese-threat-actors-at-cyberwarcon/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Subgroup%3A+Bluenoroff%2C+APT+38%2C+Stardust+Chollima&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TEMP.Hermit | canonical-name | 高 | KP | https://www.fireeye.com/blog/threat-research/2018/02/attacks-leveraging-adobe-zero-day.html<br>https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

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
| malware--volgmer | VOLGMER | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--peachpit | PEACHPIT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | レビュー済みアクターマッピングの標的欄に記録された米国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 東アジア | レビュー済みアクターマッピングの標的欄に記録された東アジアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 24件（`artifacts.csv`）

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
| source--temp-hermit--df54853ad7e7b12d | temp hermit |  | 不明 | actor_profile/evidence/temp-hermit.csv | structured-data | TLP:CLEAR | 中 |
| source--temp-hermit--8953699a2a6af798 | APT43 Report |  | 不明 | APT43/APT43 Report.pdf | report | TLP:CLEAR | 中 |
| source--temp-hermit--922b655a2719fd72 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--temp-hermit--d811a9e13ca739c2 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--temp-hermit--4df122a03557a438 | North Korea’s Cyber Strategy |  | 不明 | International Strategic/Korea/North Korea’s Cyber Strategy.pdf | report | TLP:CLEAR | 中 |
| source--temp-hermit--19598de9de949943 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--temp-hermit--3a1ba0a4d20cd1f2 | WithSecure Lazarus No Pineapple Threat Intelligence Report 2023 |  | 2023 | lazarus/WithSecure-Lazarus-No-Pineapple-Threat-Intelligence-Report-2023.pdf | report | TLP:CLEAR | 中 |
| source--temp-hermit--f59eeacdceb147c4 | 20240919 |  | 2024-09-19 | parse-daily/.cache/tech-memo/daily-news/news/2024_07-09/20240919.md | repository-notes | TLP:CLEAR | 中 |
| source--temp-hermit--4d2841a148ac4c83 | review decisions |  | 不明 | parse-daily/review-decisions.json | structured-data | TLP:CLEAR | 中 |
| source--temp-hermit--d90127ddf24b521d | rpt mtrends 2021 fireeye |  | 2021 | summary/2021/rpt-mtrends-2021-fireeye.pdf | report | TLP:CLEAR | 中 |
| source--temp-hermit--653f68aa4b031938 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--temp-hermit--975810caa356a683 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--temp-hermit--42f215de02433e72 | search |  | 不明 | ui/api/v1/search.json | structured-data | TLP:CLEAR | 中 |
| source--gtig-unified-actor-naming-2026 | Updated Cyber Threat Actor Naming System | Google Threat Intelligence Group | 2026-07-24 | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--mandiant-apt38-temp-hermit-boundary-2018 | APT38: Details on New North Korean Regime-Backed Threat Group | Mandiant | 2018-10-03 | https://cloud.google.com/blog/topics/threat-intelligence/apt38-details-on-new-north-korean-regime-backed-threat-group/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-gtig-threat-actor-naming | Google Threat Intelligence Group Unified Threat Actor Naming | Google Threat Intelligence Group | 不明 | actor_profile/reference/osint/gtig-threat-actor-naming.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
