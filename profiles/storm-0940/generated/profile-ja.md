# Storm-0940 脅威アクタープロファイル

- プロファイルID: `actor--storm-0940`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Storm-0940の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Storm-0940**
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
| microsoft-threat-actor-mapping | Storm-0940 | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Storm-0940 | canonical-name | 高 | CN | https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/ |
| misp-microsoft-activity-group | Storm-0940 | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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
| マイクロソフト：中国のハッカーがQuad7ボットネットを使用し認証情報を窃取 | cyber-espionage | 不明 | 不明 | 2024-11-01 |  |  | ttp--activity-rule--34c7b2c43f3e860d3bc6, ttp--activity-rule--3843caa70d7480d4e7bb | victim--activity-rule--dbe9d7537d95d92bd57e | 中国のハッカーがSOHOルーターなどを乗っ取って構築したQuad7ボットネットを使用し、認証情報を窃取。 パスワードスプレー攻撃で認証情報を収集し、複数の中国のハッカー集団によって使用。特に「Storm-0940」と呼ばれる攻撃者がQuad7から認証情報を使用して攻撃しているのが確認された。 攻撃者は侵害したSOHOルーターなどに対して、telnetとSOCKS5プロキシサーバーを設置。 パスワードスプレーで得た認証情報で組織内に侵入し、さらにネットワーク内で権限を拡大しデータを抽出。 SOHOルーターなどをどうやって侵害しているかは不明。Sekoiaのハニーポットへの侵入では、未公開の脆弱性を利用していた。 攻撃の最終的な目標は、標的のネットワークからデータを抜き取ること。これは、サイバースパイ活動が目的である可能性が高い。 | 中 | `source--daily-1cd41f481ad33e011f4b` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| マイクロソフト：中国のハッカーがQuad7ボットネットを使用し認証情報を窃取 | Storm-0940 | 情報なし | T1110.003 Password Spraying, T1090 Proxy | 情報なし | 情報なし | 被害事例: マイクロソフト：中国のハッカーがQuad7ボットネットを使用し認証情報を窃取 | 中 |



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: マイクロソフト：中国のハッカーがQuad7ボットネットを使用し認証情報を窃取 | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--activity-rule--34c7b2c43f3e860d3bc6, ttp--activity-rule--3843caa70d7480d4e7bb | サーバー, ネットワーク機器 | credential-theft: マイクロソフト：中国のハッカーがQuad7ボットネットを使用し認証情報を窃取<br>espionage: これは、サイバースパイ活動が目的である可能性が高い。 | 不明 | 不明 | 2024-11-01 | 中 | `source--daily-1cd41f481ad33e011f4b` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1110.003 | Password Spraying | パスワードスプレー攻撃で認証情報を収集し、複数の中国のハッカー集団によって使用。 |  | activity--daily-2b566a7bbc5026664971 | 不明 | 不明 | 中 | `source--daily-1cd41f481ad33e011f4b` |
| Command And Control | T1090 | Proxy | 攻撃者は侵害したSOHOルーターなどに対して、telnetとSOCKS5プロキシサーバーを設置。 |  | activity--daily-2b566a7bbc5026664971 | 不明 | 不明 | 中 | `source--daily-1cd41f481ad33e011f4b` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 2件（`artifacts.csv`）

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
| source--daily-1cd41f481ad33e011f4b | マイクロソフト：中国のハッカーがQuad7ボットネットを使用し認証情報を窃取 | bleepingcomputer.com | 2024-11-01 | https://www.bleepingcomputer.com/news/security/microsoft-chinese-hackers-use-quad7-botnet-to-steal-credentials/ | osint-report | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--storm-0940--ab00c400f6ad95c2 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--storm-0940--f06157dd3a046482 | storm 0940 |  | 不明 | actor_profile/evidence/storm-0940.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
