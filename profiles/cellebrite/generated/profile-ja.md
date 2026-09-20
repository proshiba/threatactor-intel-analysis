# Cellebrite 脅威アクタープロファイル

- プロファイルID: `actor--cellebrite`
- 状態: draft
- 更新日時: 2026-09-19T00:00:50Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Cellebriteはデジタルフォレンジック／端末アクセス技術のベンダーとして追跡する。顧客・政府機関がCellebrite製品を使用した事例を、Cellebrite自身の攻撃活動としては扱わない。

## アクター名とAlias

- 正規名: **Cellebrite**
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

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| commercial | Commercial digital-forensics and device-access technology vendor. | 高 | `source--cellebrite--90a6ad972f6fa9a4` | Commercial vendor role only; this is not an assertion that Cellebrite operated the reviewed Serbian intrusions. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | Commercial device-access / digital-forensics technology. |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `no-match`
- 調査日時: 2026-09-20T13:47:46Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
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

選定ロジック: No victim targeting is assigned to Cellebrite from customer-operated use of its products. 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 122件
- IOC観測: 137件
- 複数攻撃で観測: 0件
- 要レビュー候補: 77件
- 非IOC artifact観測: 24件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| The reviewed Serbian device-access incidents are not Cellebrite-operated intrusions; Cellebrite is the product/exploit vendor in those reports. | 高 | `source--cellebrite--90a6ad972f6fa9a4` | Corrected after actor/vendor/operator role review. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性


## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--cellebrite--90a6ad972f6fa9a4 | Amnesty reporting on Cellebrite product misuse in Serbia | Amnesty International | 不明 | Cellebrite/Amnesty-Cellebrite.pdf | report | TLP:CLEAR | 高 |
| source--cellebrite--d3efba9fe5ded235 | readme |  | 不明 | Cellebrite/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--daily-5968af3fdd75f2b8e823 | Google、標的型攻撃で悪用されたAndroidゼロデイ脆弱性を修正 | bleepingcomputer.com | 2025-03-05 | https://www.bleepingcomputer.com/news/security/google-fixes-android-zero-days-exploited-in-targeted-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-a2ace93812b6d990cbcf | Google、攻撃で悪用されたAndroidゼロデイを含む60以上の脆弱性を修正 | bleepingcomputer.com | 2025-04-08 | https://www.bleepingcomputer.com/news/security/google-fixes-android-zero-days-exploited-in-attacks-60-other-flaws/ | osint-report | TLP:CLEAR | 中 |
| source--daily-beb73f1716914fd50808 | セルビア警察、Cellebriteのゼロデイ攻撃を使用してAndroid携帯をアンロック | bleepingcomputer.com | 2025-03-01 | https://www.bleepingcomputer.com/news/security/serbian-police-used-cellebrite-zero-day-hack-to-unlock-android-phones/ | osint-report | TLP:CLEAR | 中 |

## 自由記述

2026-09 correctness reviewでセルビア当局による製品利用3件をCellebriteのActivityから除外した。
