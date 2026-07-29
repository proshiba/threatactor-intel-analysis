# Magecart 脅威アクタープロファイル

- プロファイルID: `actor--magecart`
- 状態: draft
- 更新日時: 2026-07-29T15:36:10Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Magecartの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Magecart**
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

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | MageCart | canonical-name | 高 |  | https://www.bleepingcomputer.com/news/security/british-airways-fell-victim-to-card-scraping-attack/<br>https://www.bleepingcomputer.com/news/security/feedify-hacked-with-magecart-information-stealing-script/<br>https://www.bleepingcomputer.com/news/security/magecart-group-compromises-plugin-used-in-thousands-of-stores-makes-rookie-mistake/ |
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
| クレジットカード窃取キャンペーン、盗難決済情報の保管にStripeを悪用 | campaign | 不明 | 不明 | 2026-06-06 | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | victim--activity-rule--450ca787b4c7bb9ad8ac | 新たなMagecartキャンペーンが、StripeのAPI基盤をカード窃取ペイロードのホストと流出データ保管に悪用している。 悪意ある活動はオンライン店舗が信頼しやすいGoogle Tag ManagerとStripeのドメインに依存している。 悪性コードは正規に見えるGTMコンテナから読み込まれ、Magento/Adobe Commerceのチェックアウトページを狙う。 窃取対象はカード番号、有効期限、CVV、氏名、請求先住所、メールアドレス、電話番号などである。 SansecはFirestoreを使う亜種も確認し、Stripe上の記録作成日から少なくとも2025年12月24日以降の活動を示唆した。 | 中 | `source--daily-5b3e49d018b8dff5644f` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 金融 | 活動「クレジットカード窃取キャンペーン、盗難決済情報の保管にStripeを悪用」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5b3e49d018b8dff5644f` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: クレジットカード窃取キャンペーン、盗難決済情報の保管にStripeを悪用 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | メール／メールアカウント |  | 不明 | 不明 | 2026-06-06 | 中 | `source--daily-5b3e49d018b8dff5644f` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 22件
- IOC観測: 23件
- 複数攻撃で観測: 0件
- 要レビュー候補: 18件
- 非IOC artifact観測: 17件（`artifacts.csv`）

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
| source--daily-5b3e49d018b8dff5644f | クレジットカード窃取キャンペーン、盗難決済情報の保管にStripeを悪用 | sansec.io | 2026-06-06 | https://sansec.io/research/stripe-api-skimmer-infrastructure | osint-report | TLP:CLEAR | 中 |
| source--magecart--15766072d35a10d4 | README |  | 不明 | Magecart/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
