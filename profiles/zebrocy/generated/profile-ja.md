# Zebrocy 脅威アクタープロファイル

- プロファイルID: `actor--zebrocy`
- 状態: deprecated
- 更新日時: 2026-09-21T02:11:28Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Zebrocyの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Zebrocy**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

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
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `no-match`
- 調査日時: 2026-09-19T01:10:23Z
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

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 2件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Zebrocy is malware used by APT28/Sednit, not a canonical threat actor. | 高 | `source--mitre-zebrocy-s0251`, `source--eset-zebrocy-2018` | Entity-boundary correction. |

### 情報ギャップ


### 不確実性


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
| source--mitre-zebrocy-s0251 | Zebrocy, Software S0251 | MITRE ATT&CK | 不明 | https://attack.mitre.org/software/S0251/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--eset-zebrocy-2018 | Sednit: What's going on with Zebrocy? | ESET | 2018-11-20 | https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/ | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
