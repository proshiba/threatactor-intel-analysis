# UNC3782 脅威アクタープロファイル

- プロファイルID: `actor--unc3782`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC3782の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC3782**
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
| 北朝鮮ハッカー、TRONユーザーから1日で1億3700万ドルを盗むフィッシング攻撃を実行 | phishing-campaign | 不明 | 不明 | 2025-04-24 | target--activity-rule--sector--63c9fa67327d005b07b7 |  |  | victim--activity-rule--9b4239577b21c13ce760 | 北朝鮮関連のハッカー集団UNC3782が、TRONユーザーを標的にした大規模なフィッシング攻撃を実行。 2023年に、UNC3782はTRONユーザーに対してフィッシングオペレーションを実施し、1日で1億3700万ドル以上の暗号資産を不正に移転。 攻撃は、Web3および暗号通貨分野の開発者を狙ったもので、UNC1069、UNC4899、UNC5342など他の北朝鮮関連の脅威グループも関与。 これらの活動は、北朝鮮の大量破壊兵器（WMD）プログラムやその他の戦略的資産の資金調達を目的としている。 暗号通貨の窃盗は、北朝鮮が国際的な制裁を回避するために追求しているいくつかの手段の一つ。 | 中 | `source--daily-434d874b398754ef9357` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 暗号資産・Web3 | 活動「北朝鮮ハッカー、TRONユーザーから1日で1億3700万ドルを盗むフィッシング攻撃を実行」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-434d874b398754ef9357` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 北朝鮮ハッカー、TRONユーザーから1日で1億3700万ドルを盗むフィッシング攻撃を実行 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--63c9fa67327d005b07b7 |  |  |  |  | 不明 | 不明 | 2025-04-24 | 中 | `source--daily-434d874b398754ef9357` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 7件（`artifacts.csv`）

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
| source--daily-434d874b398754ef9357 | 北朝鮮ハッカー、TRONユーザーから1日で1億3700万ドルを盗むフィッシング攻撃を実行 | thehackernews.com | 2025-04-24 | https://thehackernews.com/2025/04/dprk-hackers-steal-137m-from-tron-users.html | osint-report | TLP:CLEAR | 中 |
| source--unc3782--3a57535af07edeed | unc3782 |  | 不明 | actor_profile/evidence/unc3782.csv | structured-data | TLP:CLEAR | 中 |
| source--unc3782--65994dd78aa33026 | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--unc3782--8a89d1afe3937c61 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
