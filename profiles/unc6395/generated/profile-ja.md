# UNC6395 脅威アクタープロファイル

- プロファイルID: `actor--unc6395`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC6395の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC6395**
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
| misp-threat-actor | UNC6395 | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift |
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
| Google、Salesloft侵害が一部Workspaceアカウントに影響と警告 | intrusion | 不明 | 不明 | 2025-08-30 |  |  |  | victim--activity-rule--52701ce28b5a212c3477 | GoogleはSalesloftのDrift侵害が拡大し、一部Workspaceメールにも影響と警告。 盗難OAuthトークンでSalesforceのCases等へ照会し、鍵やトークン等の秘匿情報を探索。 8月9日、Drift Email連携のトークンで少数のWorkspaceアカウントのメールに不正アクセス。 トークンは失効済み。Googleは該当連携を無効化し、顧客に通知。 全Drift関連トークンの失効・再発行、連携見直しと痕跡調査を実施するよう要請。 | 中 | `source--daily-14a0a74759d412438e33` |
| パロアルトネットワークス、データ侵害で顧客情報とサポートケース情報が流出 | intrusion | 不明 | 不明 | 2025-09-03 |  |  |  | victim--activity-rule--45fd1c065fee4a6b386a | Paloalto Networksは、Salesloft Drift由来のOAuthトークン悪用でSalesforceデータが流出と公表。 影響はSalesforceのCRMに限定、製品・システム・サービスへの影響なし。 流出は主に連絡先等とケース本文で、添付や技術ファイルは含まず。 攻撃はUNC6395が関与とされ、Torやログ削除・自動化で大規模窃取。 同社はトークン無効化・鍵ローテ等を実施し、顧客に調査を推奨。 | 中 | `source--daily-f65973d8369eb0277faf` |
| FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | ransomware-extortion | 不明 | 不明 | 2025-09-15 |  |  |  | victim--activity-rule--ac83caa59af2fa4c9b18 | FBIはUNC6040/UNC6395がSalesforce環境を侵害しデータ窃取・恐喝を行うとしてFLASHを公開、IOCの提供で防御強化を促した。 UNC6040は2024年末以降、偽IT支援やvishingで従業員を欺き、悪性Salesforce Data Loader OAuthアプリ（My Ticket Portal等）を接続させた。 接続後にAccounts/Contactsなどを大量流出させ、ShinyHuntersが恐喝に悪用。GoogleやAdidasなどの大手にも影響が及んだとされる。 UNC6395はSalesloft DriftのOAuth/リフレッシュトークンを悪用（8/8〜18頃）し、Salesforceのサポートケース情報を狙って侵害した。 流出データからAWS鍵やパスワード、Snowflakeトークン等を抽出し横展開。Salesloftはトークン失効と再認証を実施、被害は多数に及んだ。 | 高 | `source--daily-d18643e84905959f1988` |
| Salesloft：3月のGitHubリポジトリ侵害がSalesforceデータ窃取攻撃に発展 | intrusion | 不明 | 不明 | 2025-09-09 |  |  |  | victim--activity-rule--1a80c726c6a7162426fd | Salesloftは3月にGitHubを侵害され、8月のSalesforceデータ窃取に発展と説明。 DriftのOAuthトークンが窃取され、顧客環境横断のアクセスに悪用。 Salesforceのサポートケースからシークレット情報を収集、AWS鍵やSnowflakeアクセストークン等。 Mandiantは3–6月にリポジトリダウンロードや不正ワークフロー作成を確認。 攻撃はUNC6395に帰属、ShinyHuntersとScattered Spider関与の主張も。 | 中 | `source--daily-5ccc06758fe72e4fc05e` |
| Salesloftが侵害され、Salesforceデータ窃取攻撃用のOAuthトークンが盗まれる | infrastructure-operation | 不明 | 不明 | 2025-08-27 |  |  | ttp--activity-rule--b489d625786d2bc516b3 | victim--activity-rule--0c6a735d410dbf488002 | SalesloftのDrift-Salesforce連携のOAuth/リフレッシュトークンが盗まれ、顧客環境で窃取に悪用。 攻撃は2025/8/8〜8/18に実施。AWS鍵・パスワード・Snowflakeトークン等の取得を狙う。 Salesloftは全トークンを失効させ再認証を要求。影響は同連携を使う顧客に限定と説明。 GTIGはUNC6395(ShinyHunters)として追跡。SOQLで秘密抽出、インフラを隠すためにTorやAWS・DigitalOceanといったホスティングプロバイダーも利用。 リクエストにはpythonまたはカスタムツール用のUser-Agentが利用されていた。 python-requests/2.32.4、Python/3.11 aiohttp/3.12.15 | 中 | `source--daily-1280007d047388eb38ef` |



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Salesloftが侵害され、Salesforceデータ窃取攻撃用のOAuthトークンが盗まれる | Salesloft | named | organization | reported |  |  | ttp--activity-rule--b489d625786d2bc516b3 | クラウド／SaaS | data-theft: Salesloftが侵害され、Salesforceデータ窃取攻撃用のOAuthトークンが盗まれる<br>credential-theft: SalesloftのDrift-Salesforce連携のOAuth/リフレッシュトークンが盗まれ、顧客環境で窃取に悪用。 | 不明 | 不明 | 2025-08-27 | 中 | `source--daily-1280007d047388eb38ef` |
| 被害事例: Salesloft：3月のGitHubリポジトリ侵害がSalesforceデータ窃取攻撃に発展 | Salesloft：3月 | named | organization | reported |  |  |  | クラウド／SaaS, 開発環境／ソースコード | data-theft: Salesloft：3月のGitHubリポジトリ侵害がSalesforceデータ窃取攻撃に発展 | 不明 | 不明 | 2025-09-09 | 中 | `source--daily-5ccc06758fe72e4fc05e` |
| 被害事例: パロアルトネットワークス、データ侵害で顧客情報とサポートケース情報が流出 | パロアルトネットワークス | named | organization | reported |  |  |  | クラウド／SaaS | data-theft: パロアルトネットワークス、データ侵害で顧客情報とサポートケース情報が流出<br>credential-theft: Paloalto Networksは、Salesloft Drift由来のOAuthトークン悪用でSalesforceデータが流出と公表。<br>privacy: パロアルトネットワークス、データ侵害で顧客情報とサポートケース情報が流出 | 不明 | 不明 | 2025-09-03 | 中 | `source--daily-f65973d8369eb0277faf` |
| 被害事例: Google、Salesloft侵害が一部Workspaceアカウントに影響と警告 | 非公開 | anonymous | unknown | reported |  |  |  | メール／メールアカウント, クラウド／SaaS |  | 不明 | 不明 | 2025-08-30 | 中 | `source--daily-14a0a74759d412438e33` |
| 被害事例: FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | 非公開 | aggregate | multiple-organizations | reported |  |  |  | クラウド／SaaS | data-theft: FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | 不明 | 不明 | 2025-09-15 | 高 | `source--daily-d18643e84905959f1988` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.006 | Python | python-requests/2.32.4、Python/3.11 aiohttp/3.12.15 |  | activity--daily-8c3751b2994642569734 | 不明 | 不明 | 中 | `source--daily-1280007d047388eb38ef` |

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
| source--daily-1280007d047388eb38ef | Salesloftが侵害され、Salesforceデータ窃取攻撃用のOAuthトークンが盗まれる | bleepingcomputer.com | 2025-08-27 | https://www.bleepingcomputer.com/news/security/salesloft-breached-to-steal-oauth-tokens-for-salesforce-data-theft-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-14a0a74759d412438e33 | Google、Salesloft侵害が一部Workspaceアカウントに影響と警告 | bleepingcomputer.com | 2025-08-30 | https://www.bleepingcomputer.com/news/security/google-warns-salesloft-breach-impacted-some-workspace-accounts/ | osint-report | TLP:CLEAR | 中 |
| source--daily-5ccc06758fe72e4fc05e | Salesloft：3月のGitHubリポジトリ侵害がSalesforceデータ窃取攻撃に発展 | bleepingcomputer.com | 2025-09-09 | https://www.bleepingcomputer.com/news/security/salesloft-march-github-repo-breach-led-to-salesforce-data-theft-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-d18643e84905959f1988 | FBIがUNC6040／UNC6395によるSalesforceデータ窃取を警告 | bleepingcomputer.com | 2025-09-15 | https://www.bleepingcomputer.com/news/security/fbi-warns-of-unc6040-unc6395-hackers-stealing-salesforce-data/ | osint-report | TLP:CLEAR | 中 |
| source--daily-f65973d8369eb0277faf | パロアルトネットワークス、データ侵害で顧客情報とサポートケース情報が流出 | bleepingcomputer.com | 2025-09-03 | https://www.bleepingcomputer.com/news/security/palo-alto-networks-data-breach-exposes-customer-info-support-cases/ | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc6395--09b1fc1004b448e9 | 2025 IC3Report |  | 2025 | cybercrime/2026/2025_IC3Report.pdf | report | TLP:CLEAR | 中 |
| source--unc6395--70b58fc77f2d89e3 | ShinyHunters |  | 不明 | cybercrime/ShinyHunters/ShinyHunters.pdf | report | TLP:CLEAR | 中 |
| source--unc6395--b4ea36e343b3154b | unc6395 |  | 不明 | actor_profile/evidence/unc6395.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
