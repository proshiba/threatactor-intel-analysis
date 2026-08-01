# UNC5537 脅威アクタープロファイル

- プロファイルID: `actor--unc5537`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC5537の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC5537**
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
| etda-threat-group-cards | UNC5537 | canonical-name | 高 | Canada | https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion<br>https://www.bleepingcomputer.com/news/security/pure-storage-confirms-data-breach-after-snowflake-account-hack/<br>https://krebsonsecurity.com/2025/02/u-s-soldier-charged-in-att-hack-searched-can-hacking-be-treason/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UNC5537 | canonical-name | 高 |  | https://research.checkpoint.com/2024/17th-june-threat-intelligence-report/<br>https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion |
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
| Ticketmasterから流出したSnowflake攻撃データ、再び販売リストに掲載 | ransomware-extortion | 不明 | 不明 | 2025-06-11 |  |  |  | victim--activity-rule--45487905e25cd639cdeb | 2024年のSnowflake攻撃で流出したTicketmasterの569GB分の顧客データが、Arkana Securityという恐喝グループによって再販リストに一時掲載。 掲載されたデータは以前に盗まれたもので、新たな侵害ではなく再流通である。 データには“RapeFlake”という窃取ツールの痕跡も含まれていた。 当該販売リストは数日で削除され、現在は閲覧不可となっている。 この攻撃にはShinyHuntersやUNC5537（Scattered Spider）などのAPTグループが関与していた。 Arkanaがこのデータを以前購入したのか、以前データを持っていた脅威アクターで構成されているのか、あるいはShinyHuntersと協力して販売しているのかは不明。 | 中 | `source--daily-50b897d744561404ee8d` |
| Pure Storage、Snowflakeアカウントのハッキング後にデータ侵害を確認 | malware-campaign | 不明 | 不明 | 2024-06-12 |  |  |  |  | Pure StorageのSnowflakeワークスペースが侵害され、顧客名、ユーザー名、メールアドレスなどの情報が侵害された アレイアクセスの資格情報や顧客システムに保存されているその他のデータは侵害されていない 同社は即座に対応し、さらなる不正アクセスを防止 進行中の攻撃の影響を受ける可能性のある約165の組織に通知済み さらにSnowflakeの顧客に対して、情報窃取型マルウェアで窃取した資格情報を使った攻撃も進行している | 中 | `source--daily-e8268dd0f05d0e93b4d0` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Ticketmasterから流出したSnowflake攻撃データ、再び販売リストに掲載 | UNC5537 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: Ticketmasterから流出したSnowflake攻撃データ、再び販売リストに掲載 | 中 |
| Pure Storage、Snowflakeアカウントのハッキング後にデータ侵害を確認 | UNC5537 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Ticketmasterから流出したSnowflake攻撃データ、再び販売リストに掲載 | 非公開 | anonymous | unknown | reported |  |  |  |  |  | 不明 | 不明 | 2025-06-11 | 中 | `source--daily-50b897d744561404ee8d` |

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
| source--daily-50b897d744561404ee8d | Ticketmasterから流出したSnowflake攻撃データ、再び販売リストに掲載 | bleepingcomputer.com | 2025-06-11 | https://www.bleepingcomputer.com/news/security/stolen-ticketmaster-data-from-snowflake-attacks-briefly-for-sale-again/ | osint-report | TLP:CLEAR | 中 |
| source--daily-e8268dd0f05d0e93b4d0 | Pure Storage、Snowflakeアカウントのハッキング後にデータ侵害を確認 | bleepingcomputer.com | 2024-06-12 | https://www.bleepingcomputer.com/news/security/pure-storage-confirms-data-breach-after-snowflake-account-hack/ | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc5537--77fef4fffc5f5760 | ShinyHunters |  | 不明 | cybercrime/ShinyHunters/ShinyHunters.pdf | report | TLP:CLEAR | 中 |
| source--unc5537--7defd99777db344a | 2024 H1 Threat Intel Report Final |  | 2024 | summary/2024/2024-H1-Threat-Intel-Report-Final.pdf | report | TLP:CLEAR | 中 |
| source--unc5537--9285511fa67f7da4 | unc5537 |  | 不明 | actor_profile/evidence/unc5537.csv | structured-data | TLP:CLEAR | 中 |
| source--unc5537--d2cb397f64bd5f8f | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
