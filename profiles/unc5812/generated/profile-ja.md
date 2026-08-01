# UNC5812 脅威アクタープロファイル

- プロファイルID: `actor--unc5812`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC5812の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC5812**
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ロシア、ウクライナ徴兵対象者にWindowsおよびAndroidマルウェアで攻撃 | cyber-espionage | 不明 | 不明 | 2024-10-29 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a |  |  | victim--activity-rule--0fb5975e7f282c1f913a | ロシアのUNC5812グループが、ウクライナ徴兵者を標的にしたスパイ活動/世論操作キャンペーンを実施。 偽の「民間防衛」アプリが情報窃取や位置追跡用のマルウェアを配布。 Windowsでは情報スティーラ「PureStealer」、Androidでは「CraxsRAT」を使用。 アプリがGoogle Play Protectを無効化させ、スパイ活動を許可します。 Googleは検出対策を強化し、Safe Browsingリストを更新。 | 中 | `source--daily-1c77a9c15728423b9d08` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| ロシア、ウクライナ徴兵対象者にWindowsおよびAndroidマルウェアで攻撃 | UNC5812 | 情報なし | 情報なし | 情報なし | ウクライナ, ロシア | 被害事例: ロシア、ウクライナ徴兵対象者にWindowsおよびAndroidマルウェアで攻撃 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ウクライナ | 活動「ロシア、ウクライナ徴兵対象者にWindowsおよびAndroidマルウェアで攻撃」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-1c77a9c15728423b9d08` |
| countries | ロシア | 活動「ロシア、ウクライナ徴兵対象者にWindowsおよびAndroidマルウェアで攻撃」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-1c77a9c15728423b9d08` |
| regions | 東欧 | ウクライナ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-1c77a9c15728423b9d08` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ロシア、ウクライナ徴兵対象者にWindowsおよびAndroidマルウェアで攻撃 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a |  |  | モバイル端末 | espionage: ロシアのUNC5812グループが、ウクライナ徴兵者を標的にしたスパイ活動/世論操作キャンペーンを実施。 | 不明 | 不明 | 2024-10-29 | 中 | `source--daily-1c77a9c15728423b9d08` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 1件（`artifacts.csv`）

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
| source--daily-1c77a9c15728423b9d08 | ロシア、ウクライナ徴兵対象者にWindowsおよびAndroidマルウェアで攻撃 | bleepingcomputer.com | 2024-10-29 | https://www.bleepingcomputer.com/news/security/russia-targets-ukrainian-conscripts-with-windows-android-malware/ | osint-report | TLP:CLEAR | 中 |
| source--unc5812--c3628b0d6f615912 | unc5812 |  | 不明 | actor_profile/evidence/unc5812.csv | structured-data | TLP:CLEAR | 中 |
| source--unc5812--c96bc154a5c14896 | CERTFR 2025 CTI 004 |  | 2025 | summary/2025/CERTFR-2025-CTI-004.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
