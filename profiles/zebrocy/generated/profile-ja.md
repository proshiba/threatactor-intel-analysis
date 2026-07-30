# Zebrocy 脅威アクタープロファイル

- プロファイルID: `actor--zebrocy`
- 状態: draft
- 更新日時: 2026-07-29T23:13:55Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Zebrocyの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Zebrocy**
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
| Capability |  |
| Infrastructure |  |
| Victim | Germany, Indonesia, the United States, Taiwan, India, France, Serbia, Ecuador, Argentina, South Korea, Japan, China, Britain, South Africa, Italy, Hong Kong, Romania, Ukraine, Macedonia, Russia, Switzerland, Senegal, the Philippines, UAE, Qatar, Saudi Arabia, Pakistan, Thailand, Bahrain, Turkey, Bulgaria, Bangladesh |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `no-match`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
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

未確認

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
| countries | アラブ首長国連邦 | レビュー済みアクターマッピングの標的欄に記録されたアラブ首長国連邦を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | アルゼンチン | Targeting text mentions argentina. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | イタリア | Targeting text mentions italy. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | インド | Targeting text mentions india. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | インドネシア | Targeting text mentions indonesia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | ウクライナ | Targeting text mentions ukraine. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | エクアドル | Targeting text mentions ecuador. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | カタール | レビュー済みアクターマッピングの標的欄に記録されたカタールを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | サウジアラビア | Targeting text mentions saudi arabia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | スイス | Targeting text mentions switzerland. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | セネガル | レビュー済みアクターマッピングの標的欄に記録されたセネガルを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | セルビア | レビュー済みアクターマッピングの標的欄に記録されたセルビアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | タイ | Targeting text mentions thailand. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | トルコ | Targeting text mentions turkey. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | ドイツ | Targeting text mentions germany. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | バングラデシュ | Targeting text mentions bangladesh. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | バーレーン | レビュー済みアクターマッピングの標的欄に記録されたバーレーンを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | パキスタン | Targeting text mentions pakistan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | フィリピン | Targeting text mentions philippines. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | フランス | Targeting text mentions france. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | ブルガリア | レビュー済みアクターマッピングの標的欄に記録されたブルガリアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | ルーマニア | Targeting text mentions romania. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | ロシア | Targeting text mentions russia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 中国 | Targeting text mentions china. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 北マケドニア | レビュー済みアクターマッピングの標的欄に記録された北マケドニアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 南アフリカ | レビュー済みアクターマッピングの標的欄に記録された南アフリカを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 台湾 | Targeting text mentions taiwan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 日本 | Targeting text mentions japan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 米国 | Targeting text mentions united states. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 韓国 | Targeting text mentions south korea. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 香港 | Targeting text mentions hong kong. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | アフリカ | レビュー済みアクターマッピングの標的欄に記録されたアフリカを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 中南米 | アルゼンチン、エクアドルで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 中東 | アラブ首長国連邦、カタール、サウジアラビア、トルコ、バーレーンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 南アジア | インド、バングラデシュ、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 南欧 | イタリア、セルビア、北マケドニアで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 南米 | アルゼンチン、エクアドルで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 東アジア | 中国、台湾、日本、韓国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 東南アジア | インドネシア、タイ、フィリピンで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 東欧 | ウクライナ、ブルガリア、ルーマニア、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 欧州 | イタリア、ウクライナ、スイス、セルビア、トルコ、ドイツ、フランス、ブルガリア、ルーマニア、北マケドニアで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 45件（`artifacts.csv`）

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
| source--zebrocy--b6f295572f215ac5 | zebrocy |  | 不明 | actor_profile/evidence/zebrocy.csv | structured-data | TLP:CLEAR | 中 |
| source--zebrocy--a4ba69d67da07182 | 2019 04 05 ioc mark |  | 2019-04-05 | APT28/IOC/2019-04-05-ioc-mark.txt | text-data | TLP:CLEAR | 中 |
| source--zebrocy--b3d72a2a54dbd635 | README |  | 不明 | APT28/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--zebrocy--88b3cac0fd13f1b7 | sednit update analysis zebrocy |  | 不明 | APT28/history-report-pdf/sednit-update-analysis-zebrocy_.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--82fc9cc456dfdb04 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--80bf0fc378034bfd | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--672d3036283c9392 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--3a626ceed476c742 | ESET Threat Report Q22020 |  | 不明 | summary/2020/ESET_Threat_Report_Q22020.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--b3db5d9d59d9f961 | APT group activities under the shadow of the epidemic(2020) |  | 2020 | summary/2021/APT group activities under the shadow of the epidemic(2020).pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--d23630803791c6e9 | Global APT Research Report for the first half of 2021 360 |  | 2021 | summary/2021/Global APT Research Report for the first half of 2021-360.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--0cd52be16bfa3e66 | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--434b97f09eb949de | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--a477e036e7598530 | XForce Threat Intelligence 2022 |  | 2022 | summary/2022/XForce_Threat_Intelligence_2022.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--2b771e6a90f71ed6 | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--zebrocy--be5e9f1e9d5be62f | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
