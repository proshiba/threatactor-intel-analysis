# TA455 脅威アクタープロファイル

- プロファイルID: `actor--ta455`
- 状態: draft
- 更新日時: 2026-07-29T15:36:12Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

TA455の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA455**
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
| etda-threat-group-cards | TA455, Smoke Sandstorm | canonical-name | 高 | Iran | https://www.microsoft.com/en-us/security/security-insider/smoke-sandstorm<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Subgroup%3A+TA455%2C+Smoke+Sandstorm&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA455 | canonical-name | 高 | IR | https://www.clearskysec.com/irdreamjob24/ |
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
| イランのハッカーが「夢の仕事」誘導でSnailResinマルウェアを展開し航空宇宙業界を攻撃 | infrastructure-operation | 不明 | 不明 | 2024-11-14 | target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--b94dc560a327b601965d |  | ttp--activity-rule--eb98ef3db37259929a88 | victim--activity-rule--6a4912bf6d33cae8f7dc | イランのTA455ハッカーが「夢の仕事」詐欺を用いてSnailResinマルウェアを配信し、航空宇宙分野を狙っています。 偽の採用サイトとLinkedInを通じ、悪意のあるファイルが含まれたZIPを被害者に配布します。 SnailResinが感染するとSlugResinバックドアが起動し、情報窃取や権限昇格が可能となります。 GitHubを使用し、C2通信を隠蔽しながら、さらに感染を広げる手法が使われています。 TA455は、北朝鮮のLazarusが使っている手法を模倣し、帰属を誤らせる効果を狙っている可能性があります。 | 中 | `source--daily-27498943ada7ba352f55` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 運輸・航空・海運 | 活動「イランのハッカーが「夢の仕事」誘導でSnailResinマルウェアを展開し航空宇宙業界を攻撃」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-27498943ada7ba352f55` |
| sectors | 防衛・軍事 | 活動「イランのハッカーが「夢の仕事」誘導でSnailResinマルウェアを展開し航空宇宙業界を攻撃」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-27498943ada7ba352f55` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: イランのハッカーが「夢の仕事」誘導でSnailResinマルウェアを展開し航空宇宙業界を攻撃 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--b94dc560a327b601965d |  | ttp--activity-rule--eb98ef3db37259929a88 | 開発環境／ソースコード |  | 不明 | 不明 | 2024-11-14 | 中 | `source--daily-27498943ada7ba352f55` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1102.003 | One-Way Communication | GitHubを使用し、C2通信を隠蔽しながら、さらに感染を広げる手法が使われています。 |  | activity--daily-86a7b33d62fd6f99ee6d | 不明 | 不明 | 中 | `source--daily-27498943ada7ba352f55` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 10件（`artifacts.csv`）

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
| source--daily-27498943ada7ba352f55 | イランのハッカーが「夢の仕事」誘導でSnailResinマルウェアを展開し航空宇宙業界を攻撃 | thehackernews.com | 2024-11-14 | https://thehackernews.com/2024/11/iranian-hackers-use-dream-job-lures-to.html | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta455--4346f79647b4845b | Iranian Dream Job ver1 |  | 不明 | Charming Kitten/Iranian-Dream-Job-ver1.pdf | report | TLP:CLEAR | 中 |
| source--ta455--70894526c761d571 | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--ta455--e5e440e4b2c64992 | ta455 |  | 不明 | actor_profile/evidence/ta455.csv | structured-data | TLP:CLEAR | 中 |
| source--ta455--ecceb7706fc8f8b1 | eset apt activity report q2 2025 q3 2025 |  | 2025 | summary/2025/eset-apt-activity-report-q2-2025-q3-2025.pdf | report | TLP:CLEAR | 中 |
| source--ta455--ed8c558f3cb1c624 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
