# White Company 脅威アクタープロファイル

- プロファイルID: `actor--white-company-fefa7c0a`
- 状態: deprecated
- 更新日時: 2026-09-19T00:00:54Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

このWhite CompanyプロファイルはThe White Company（actor--white-company）の重複としてdeprecatedとする。

## アクター名とAlias

- 正規名: **White Company**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

Duplicate profile; attribution is maintained in actor--white-company.

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

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

ターゲット情報なし

選定ロジック: Deprecated duplicate; targets are maintained in actor--white-company. 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 6件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| This profile is a duplicate of The White Company (actor--white-company / MITRE G0089) and is deprecated. | 高 | `source--white-company-fefa7c0a--d836b38e032577f3` | Both profiles point to Operation Shaheen and the same WhiteCompany report corpus. |

### 情報ギャップ


### 不確実性


## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--white-company-fefa7c0a--2beccd7997390071 | white company fefa7c0a |  | 不明 | actor_profile/evidence/white-company-fefa7c0a.csv | structured-data | TLP:CLEAR | 中 |
| source--white-company-fefa7c0a--45b884c25710f04c | README |  | 不明 | WhiteCompany/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--white-company-fefa7c0a--d836b38e032577f3 | WhiteCompanyOperationShaheenReport |  | 不明 | WhiteCompany/WhiteCompanyOperationShaheenReport.pdf | report | TLP:CLEAR | 中 |

## 自由記述

新規参照はactor--white-companyを使用する。
