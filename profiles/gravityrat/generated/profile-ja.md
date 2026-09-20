# GravityRAT 脅威アクタープロファイル

- プロファイルID: `actor--gravityrat`
- 状態: deprecated
- 更新日時: 2026-09-20T08:53:44Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

GravityRATはMalwareとして扱い、旧actor profileはdeprecatedとする。ESETが追跡するGravityRAT運用主体はSpaceCobraとして別profile化する。

## アクター名とAlias

- 正規名: **GravityRAT**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

Deprecated entity conflation; no actor attribution is asserted for the GravityRAT software name.

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
- 調査日時: 2026-09-19T00:54:53Z
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

選定ロジック: Deprecated legacy actor profile. 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 2件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| GravityRAT is malware rather than a canonical actor; the legacy actor profile is deprecated. | 高 | `source--mitre-gravityrat-s0237`, `source--eset-spacecobra-gravityrat-2023` | Entity-type correction. |

### 情報ギャップ


### 不確実性

- Historical reporting may use malware names metonymically for operators; source scope must be checked before actor attribution.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--gravityrat--f52b2c246b760d7a | gravityrat |  | 不明 | actor_profile/evidence/gravityrat.csv | structured-data | TLP:CLEAR | 中 |
| source--mitre-gravityrat-s0237 | GravityRAT, Software S0237 | MITRE ATT&CK | 不明 | https://attack.mitre.org/software/S0237/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--eset-spacecobra-gravityrat-2023 | Android GravityRAT goes after WhatsApp backups | ESET | 2023-06-15 | https://www.welivesecurity.com/2023/06/15/android-gravityrat-goes-after-whatsapp-backups/ | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

actor--gravityratは既存参照互換性のため保持するが、新規Actor帰属には使用しない。
