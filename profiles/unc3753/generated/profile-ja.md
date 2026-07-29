# UNC3753 脅威アクタープロファイル

- プロファイルID: `actor--unc3753`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC3753の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC3753**
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
| FBI、法律事務所を標的とするLuna Mothによる恐喝攻撃に警告 | ransomware-extortion | 不明 | 不明 | 2025-05-24 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--adfe952bca03d050ae2b, target--activity-rule--sector--dfc80b76cad93a318adc |  |  | victim--activity-rule--44fccb623b114e538b5e | FBIは、Silent Ransom Group（別名Luna Moth、Chatty Spider、UNC3753）が米国の法律事務所を標的にしていると警告。 攻撃手法は、ITサポートを装ったソーシャルエンジニアリングやコールバック型フィッシングを用いて、リモートアクセスを取得。 被害者のシステムを暗号化せず、機密データを盗み出し、公開をちらつかせて身代金を要求。 攻撃者は、偽のITサポートポータルを作成し、従業員にリモートセッションへの参加を促す。 FBIは、これらの攻撃が2023年春以降、特に法律事務所を狙ってしていると報告。 | 中 | `source--daily-a577dc352eda576c7ea9` |
| Silent Ransom Group、偽のITサポート電話で法律事務所を標的に | ransomware-extortion | 2026-01 | 2026-05 | 2026-06-08 | target--activity-rule--sector--adfe952bca03d050ae2b |  |  | victim--activity-rule--6a449f8ecb6a841d1d5c | Silent Ransom Groupは、米国の法律事務所や専門サービス組織を偽ITサポート通話で積極的に狙っている。 Mandiantによると、UNC3753/Luna Moth/Chatty Spiderは2026年1月から5月に数十組織を標的にした。 攻撃は請求書風の無害なメールから始まり、その後の電話でIT担当者を装い遠隔サポート参加を促す。 攻撃者はAnyDesk、Zoho Assist、Bomgar、SuperOpsなどを導入させ、文書管理やクラウド保存先からデータを盗む。 盗難後は30分以内に恐喝要求が届くこともあり、未対応なら従業員や外部顧客へ連絡すると脅す。 | 高 | `source--daily-11c1de526630b46d3629` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | 活動「FBI、法律事務所を標的とするLuna Mothによる恐喝攻撃に警告」の記述で標的として明示された国・地域。 | 2026-01 | 2026-05 | 中 | `source--daily-11c1de526630b46d3629`, `source--daily-a577dc352eda576c7ea9` |
| sectors | 法律 | 活動「FBI、法律事務所を標的とするLuna Mothによる恐喝攻撃に警告」の記述で標的として明示された産業。 | 2026-01 | 2026-05 | 中 | `source--daily-11c1de526630b46d3629`, `source--daily-a577dc352eda576c7ea9` |
| sectors | 製造・産業 | 活動「FBI、法律事務所を標的とするLuna Mothによる恐喝攻撃に警告」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-a577dc352eda576c7ea9` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: FBI、法律事務所を標的とするLuna Mothによる恐喝攻撃に警告 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--adfe952bca03d050ae2b, target--activity-rule--sector--dfc80b76cad93a318adc |  |  | VPN／リモートアクセス機器 | encryption: 被害者のシステムを暗号化せず、機密データを盗み出し、公開をちらつかせて身代金を要求。 | 不明 | 不明 | 2025-05-24 | 中 | `source--daily-a577dc352eda576c7ea9` |
| 被害事例: Silent Ransom Group、偽のITサポート電話で法律事務所を標的に | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--adfe952bca03d050ae2b |  |  | メール／メールアカウント, クラウド／SaaS |  | 2026-01 | 2026-05 | 2026-06-08 | 高 | `source--daily-11c1de526630b46d3629` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 9件
- IOC観測: 9件
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
| source--daily-11c1de526630b46d3629 | Silent Ransom Group、偽のITサポート電話で法律事務所を標的に | cloud.google.com | 2026-06-08 | https://cloud.google.com/blog/topics/threat-intelligence/targeted-campaign-us-law-firms | osint-report | TLP:CLEAR | 中 |
| source--daily-a577dc352eda576c7ea9 | FBI、法律事務所を標的とするLuna Mothによる恐喝攻撃に警告 | bleepingcomputer.com | 2025-05-24 | https://www.bleepingcomputer.com/news/security/fbi-warns-of-luna-moth-extortion-attacks-targeting-law-firms/ | osint-report | TLP:CLEAR | 中 |
| source--unc3753--30249e36868ef344 | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--unc3753--78fdac1aeb9a05cf | unc3753 |  | 不明 | actor_profile/evidence/unc3753.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
