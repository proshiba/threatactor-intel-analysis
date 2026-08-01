# UNC6040 脅威アクタープロファイル

- プロファイルID: `actor--unc6040`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC6040の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC6040**
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
| misp-threat-actor | UNC6040 | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion<br>https://cloud.google.com/blog/topics/threat-intelligence/technical-analysis-vishing-threats/<br>https://www.varonis.com/blog/salesforce-vishing-threat-unc604 |
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
| Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | ransomware-extortion | 2025-05-29 | 2025-05-29 | 2025-08-26 | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | victim--activity-rule--83af84c95d1121969dec | サードパーティベンダー経由で不正アクセス、1,111,386人の顧客データが流出。 侵害は2025年5月29日発生、翌30日に検知・封じ込めを実施と説明。 氏名・住所・生年月日・運転免許番号・SSN下4桁などが流出。 8月22日から影響者へ通知、メイン州AGに通知サンプル提出。 攻撃はSalesforce悪用で、vishingと悪性OAuth連携→データ窃取・恐喝。 | 中 | `source--daily-8012423fa9a259605e9c` |
| Google、Salesforceアカウントを標的としたデータ恐喝攻撃を警告 | ransomware-extortion | 不明 | 不明 | 2025-06-05 |  |  |  | victim--activity-rule--1fa6e836484db0ee9a8a | GoogleのThreat Intelligence Group（GTIG）は、UNC6040と追跡される脅威グループが、SalesforceのData Loaderアプリケーションを悪用したソーシャルエンジニアリング攻撃を展開していると報告。 攻撃者は、ITサポートを装って従業員に電話をかけ、改ざんされたData LoaderアプリケーションをSalesforce環境に接続させるよう誘導。 この手法により、攻撃者は機密情報へのアクセスを獲得し、他のクラウドサービスや内部ネットワークへの侵入も可能となる。 約20の組織が影響を受け、一部ではデータの窃取が成功している。 攻撃者は、被害者に恐喝を行うが、ShinyHuntersとの連携を主張し圧力を高める事例も観測されている。 | 中 | `source--daily-80e44f9cbc707f36952a` |
| FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | ransomware-extortion | 不明 | 不明 | 2025-09-15 |  |  |  | victim--activity-rule--8c7205640a5b006f025c | FBIはUNC6040/UNC6395がSalesforce環境を侵害しデータ窃取・恐喝を行うとしてFLASHを公開、IOCの提供で防御強化を促した。 UNC6040は2024年末以降、偽IT支援やvishingで従業員を欺き、悪性Salesforce Data Loader OAuthアプリ（My Ticket Portal等）を接続させた。 接続後にAccounts/Contactsなどを大量流出させ、ShinyHuntersが恐喝に悪用。GoogleやAdidasなどの大手にも影響が及んだとされる。 UNC6395はSalesloft DriftのOAuth/リフレッシュトークンを悪用（8/8〜18頃）し、Salesforceのサポートケース情報を狙って侵害した。 流出データからAWS鍵やパスワード、Snowflakeトークン等を抽出し横展開。Salesloftはトークン失効と再認証を実施、被害は多数に及んだ。 | 高 | `source--daily-d18643e84905959f1988` |
| ShinyHuntersがSalesforceデータ窃取攻撃を主導、Qantas・Allianz Life・LVMHが被害 | phishing-campaign | 不明 | 不明 | 2025-07-31 |  |  |  | victim--activity-rule--0afbad5604962472d1de | ShinyHuntersが音声フィッシングでSalesforce環境に不正アプリを接続 Qantas・Allianz Life・LVMHなど複数社の顧客データが6–7月に流出 従業員に接続コード入力を促しData Loader OAuthを乗っ取り Okta偽装サイトで資格情報とMFAトークン窃取も併用 現時点で公開漏洩なし、攻撃者は私的に身代金を要求中 | 中 | `source--daily-636d2791761dd2b53914` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | UNC6040 | 情報なし | 情報なし | 情報なし | 金融 | Salesforce攻撃後にFarmers Insurance | 中 |
| Google、Salesforceアカウントを標的としたデータ恐喝攻撃を警告 | UNC6040 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: Google、Salesforceアカウントを標的としたデータ恐喝攻撃を警告 | 中 |
| FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | UNC6040 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | 高 |
| ShinyHuntersがSalesforceデータ窃取攻撃を主導、Qantas・Allianz Life・LVMHが被害 | UNC6040 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: ShinyHuntersがSalesforceデータ窃取攻撃を主導、Qantas・Allianz Life・LVMHが被害 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 金融 | 活動「Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響」の記述で標的として明示された産業。 | 2025-05-29 | 2025-05-29 | 中 | `source--daily-8012423fa9a259605e9c` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ShinyHuntersがSalesforceデータ窃取攻撃を主導、Qantas・Allianz Life・LVMHが被害 | 非公開 | aggregate | multiple-organizations | reported |  |  |  | クラウド／SaaS | data-theft: ShinyHuntersがSalesforceデータ窃取攻撃を主導、Qantas・Allianz Life・LVMHが被害<br>credential-theft: ShinyHuntersが音声フィッシングでSalesforce環境に不正アプリを接続 Qantas・Allianz Life・LVMHなど複数社の顧客データが6–7月に流出 従業員に接続コード入力を促しData Loader OAuthを乗っ取り Okta偽装サイトで資格情報とMFAトークン窃取も併用 現時点で公開漏洩なし、攻撃者は私的に身代金を要求中 | 不明 | 不明 | 2025-07-31 | 中 | `source--daily-636d2791761dd2b53914` |
| 被害事例: Google、Salesforceアカウントを標的としたデータ恐喝攻撃を警告 | 非公開 | aggregate | multiple-organizations | reported |  |  |  | クラウド／SaaS | data-theft: 約20の組織が影響を受け、一部ではデータの窃取が成功している。 | 不明 | 不明 | 2025-06-05 | 中 | `source--daily-80e44f9cbc707f36952a` |
| 被害事例: Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | Salesforce攻撃後にFarmers Insurance | named | organization | reported | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | クラウド／SaaS | data-theft: サードパーティベンダー経由で不正アクセス、1,111,386人の顧客データが流出。 | 2025-05-29 | 2025-05-29 | 2025-08-26 | 中 | `source--daily-8012423fa9a259605e9c` |
| 被害事例: FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | 非公開 | anonymous | unknown | reported |  |  |  | クラウド／SaaS | data-theft: FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | 不明 | 不明 | 2025-09-15 | 高 | `source--daily-d18643e84905959f1988` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 6件（`artifacts.csv`）

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
| source--daily-636d2791761dd2b53914 | ShinyHuntersがSalesforceデータ窃取攻撃を主導、Qantas・Allianz Life・LVMHが被害 | bleepingcomputer.com | 2025-07-31 | https://www.bleepingcomputer.com/news/security/shinyhunters-behind-salesforce-data-theft-attacks-at-qantas-allianz-life-and-lvmh/ | osint-report | TLP:CLEAR | 中 |
| source--daily-8012423fa9a259605e9c | Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | bleepingcomputer.com | 2025-08-26 | https://www.bleepingcomputer.com/news/security/farmers-insurance-data-breach-impacts-11m-people-after-salesforce-attack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-80e44f9cbc707f36952a | Google、Salesforceアカウントを標的としたデータ恐喝攻撃を警告 | bleepingcomputer.com | 2025-06-05 | https://www.bleepingcomputer.com/news/security/google-hackers-target-salesforce-accounts-in-data-extortion-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-d18643e84905959f1988 | FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | bleepingcomputer.com | 2025-09-15 | https://www.bleepingcomputer.com/news/security/fbi-warns-of-unc6040-unc6395-hackers-stealing-salesforce-data/ | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc6040--b0855250f118458d | ShinyHunters |  | 不明 | cybercrime/ShinyHunters/ShinyHunters.pdf | report | TLP:CLEAR | 中 |
| source--unc6040--ba9208b874d30aa1 | unc6040 |  | 不明 | actor_profile/evidence/unc6040.csv | structured-data | TLP:CLEAR | 中 |
| source--unc6040--fa88612d0bc5ab99 | 2025 IC3Report |  | 2025 | cybercrime/2026/2025_IC3Report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
