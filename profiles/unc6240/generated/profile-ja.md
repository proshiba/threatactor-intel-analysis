# UNC6240 脅威アクタープロファイル

- プロファイルID: `actor--unc6240`
- 状態: draft
- 更新日時: 2026-07-29T15:36:12Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC6240の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC6240**
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
| Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | ransomware-extortion | 不明 | 不明 | 2026-02-02 |  |  |  | victim--activity-rule--08fecf1c5b48c6bc87e9 | Mandiantは、ShinyHuntersのSaaSデータ窃取が、電話を伴うvishingと企業風フィッシングでSSO資格情報とMFAコードを奪う手口で拡大と説明。 攻撃者はIT/ヘルプデスクを装い通話中に偽ポータルへ誘導、奪取直後にログインし正規MFAを操作して自機を登録して持続化。 侵害後はOkta/Entra/GoogleのSSOダッシュボードを足場に、Salesforce（主標的）やMicrosoft 365、SharePoint、DocuSignなどへ横断アクセス。 MandiantはUNC6661/UNC6671/UNC6240（ShinyHunters）を追跡し、前二者が侵入・窃取、UNC6240が恐喝を担いTox IDを再利用と指摘。 これらの攻撃を検知するために、SSO侵害直後の大量流出、SharePoint/OneDriveのPowerShell UAでのアクセス、ToogleBox Recallの不意なOAuthやMFA通知削除を監視することを提案。 | 中 | `source--daily-02e1336153d9062de8f2` |
| Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | ransomware-extortion | 2025-05-29 | 2025-05-29 | 2025-08-26 | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | victim--activity-rule--dd9c7a0f1e6caf1b0984 | サードパーティベンダー経由で不正アクセス、1,111,386人の顧客データが流出。 侵害は2025年5月29日発生、翌30日に検知・封じ込めを実施と説明。 氏名・住所・生年月日・運転免許番号・SSN下4桁などが流出。 8月22日から影響者へ通知、メイン州AGに通知サンプル提出。 攻撃はSalesforce悪用で、vishingと悪性OAuth連携→データ窃取・恐喝。 | 中 | `source--daily-8012423fa9a259605e9c` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 金融 | 活動「Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響」の記述で標的として明示された産業。 | 2025-05-29 | 2025-05-29 | 中 | `source--daily-8012423fa9a259605e9c` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | 非公開 | anonymous | unknown | reported |  |  |  | クラウド／SaaS | data-theft: Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | 不明 | 不明 | 2026-02-02 | 中 | `source--daily-02e1336153d9062de8f2` |
| 被害事例: Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | Salesforce攻撃後にFarmers Insurance | named | organization | reported | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | クラウド／SaaS | data-theft: サードパーティベンダー経由で不正アクセス、1,111,386人の顧客データが流出。 | 2025-05-29 | 2025-05-29 | 2025-08-26 | 中 | `source--daily-8012423fa9a259605e9c` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 3件（`artifacts.csv`）

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
| source--daily-02e1336153d9062de8f2 | Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | bleepingcomputer.com | 2026-02-02 | https://www.bleepingcomputer.com/news/security/mandiant-details-how-shinyhunters-abuse-sso-to-steal-cloud-data/ | osint-report | TLP:CLEAR | 中 |
| source--daily-8012423fa9a259605e9c | Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | bleepingcomputer.com | 2025-08-26 | https://www.bleepingcomputer.com/news/security/farmers-insurance-data-breach-impacts-11m-people-after-salesforce-attack/ | osint-report | TLP:CLEAR | 中 |
| source--unc6240--2c7acfc0f73ec191 | ShinyHunters |  | 不明 | cybercrime/ShinyHunters/ShinyHunters.pdf | report | TLP:CLEAR | 中 |
| source--unc6240--ddfed6d1e692a60c | cybersecurity forecast 2026 en |  | 2026 | summary/2025/cybersecurity-forecast-2026-en.pdf | report | TLP:CLEAR | 中 |
| source--unc6240--df2a78f9305a5534 | unc6240 |  | 不明 | actor_profile/evidence/unc6240.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
