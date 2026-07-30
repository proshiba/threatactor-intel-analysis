# UAC-0188 脅威アクタープロファイル

- プロファイルID: `actor--uac-0188`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UAC-0188の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0188**
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
| ハッカー、トロイの木馬化されたマインスイーパークローンを使って金融機関をフィッシング | phishing-campaign | 不明 | 不明 | 2024-05-27 | target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--4221b5fbb827488c6eaa |  | ttp--activity-rule--47e67d974c4b21273613 | victim--activity-rule--330b99555e5684be6e6b | UAC-0188が金融機関を標的にトロイの木馬化されたマインスイーパーのPythonクローンを使用 医療文書を装ったフィッシングメールによりマルウェアを配布。メールにはdropbox上のマルウェアへのリンクが存在 dropboxからSCRファイルをダウンロードし実行すると、MinesweeperのPythonクローンコードと、リモートから取得する悪意のあるPythonコードが含まれる マルウェアはSuperOps RMMをインストールし、リモートアクセスを取得 CERT-UAが複数の侵害を確認 | 中 | `source--daily-d10b7c56549314679c89` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 医療・ヘルスケア | 活動「ハッカー、トロイの木馬化されたマインスイーパークローンを使って金融機関をフィッシング」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-d10b7c56549314679c89` |
| sectors | 金融 | 活動「ハッカー、トロイの木馬化されたマインスイーパークローンを使って金融機関をフィッシング」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-d10b7c56549314679c89` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ハッカー、トロイの木馬化されたマインスイーパークローンを使って金融機関をフィッシング | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--4221b5fbb827488c6eaa |  | ttp--activity-rule--47e67d974c4b21273613 | メール／メールアカウント, VPN／リモートアクセス機器 |  | 不明 | 不明 | 2024-05-27 | 中 | `source--daily-d10b7c56549314679c89` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.006 | Python | メールにはdropbox上のマルウェアへのリンクが存在 dropboxからSCRファイルをダウンロードし実行すると、MinesweeperのPythonクローンコードと、リモートから取得する悪意のあるPythonコードが含まれる マルウェアはSuperOps RMMをインストールし、リモートアクセスを取得 CERT-UAが複数の侵害を確認 |  | activity--daily-e3f19b42e89889105297 | 不明 | 不明 | 中 | `source--daily-d10b7c56549314679c89` |

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
| source--daily-d10b7c56549314679c89 | ハッカー、トロイの木馬化されたマインスイーパークローンを使って金融機関をフィッシング | bleepingcomputer.com | 2024-05-27 | https://www.bleepingcomputer.com/news/security/hackers-phish-finance-orgs-using-trojanized-minesweeper-clone/ | osint-report | TLP:CLEAR | 中 |
| source--uac-0188--29933bed2eea8193 | Cyber operations by russia new goals, tools and groups |  | 不明 | International Strategic/Russia/Cyber operations by russia new goals, tools and groups.pdf | report | TLP:CLEAR | 中 |
| source--uac-0188--6a4ac818fc560077 | uac 0188 |  | 不明 | actor_profile/evidence/uac-0188.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
