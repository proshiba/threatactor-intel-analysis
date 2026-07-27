# UNC6671 脅威アクタープロファイル

- プロファイルID: `actor--unc6671`
- 状態: draft
- 更新日時: 2026-07-27T11:17:27Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

UNC6671の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC6671**
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
| misp-threat-actor | UNC6671 | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft/ |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | ransomware-extortion | 不明 | 不明 | 2026-02-02 | Mandiantは、ShinyHuntersのSaaSデータ窃取が、電話を伴うvishingと企業風フィッシングでSSO資格情報とMFAコードを奪う手口で拡大と説明。 攻撃者はIT/ヘルプデスクを装い通話中に偽ポータルへ誘導、奪取直後にログインし正規MFAを操作して自機を登録して持続化。 侵害後はOkta/Entra/GoogleのSSOダッシュボードを足場に、Salesforce（主標的）やMicrosoft 365、SharePoint、DocuSignなどへ横断アクセス。 MandiantはUNC6661/UNC6671/UNC6240（ShinyHunters）を追跡し、前二者が侵入・窃取、UNC6240が恐喝を担いTox IDを再利用と指摘。 これらの攻撃を検知するために、SSO侵害直後の大量流出、SharePoint/OneDriveのPowerShell UAでのアクセス、ToogleBox Recallの不意なOAuthやMFA通知削除を監視することを提案。 | 中 | `source--daily-02e1336153d9062de8f2` |
| 新たな恐喝グループBlackFile、急増するビッシング攻撃との関連が判明 | ransomware-extortion | 不明 | 不明 | 2026-04-25 | 2026年2月以降、金銭目的の新たな脅威グループBlackFileが、小売・ホスピタリティ業界を狙うデータ窃取と恐喝攻撃に関与していると報告された。 攻撃者は企業のITヘルプデスクを装い、偽の社内ログインページへ誘導して従業員の認証情報とワンタイムパスコードを盗み出す。 盗んだ認証情報で自分たちの端末を登録してMFAを回避し、社内ディレクトリを悪用して幹部レベルのアカウントへアクセスを広げる。 その後、SalesforceやSharePointの標準APIで「confidential」や「SSN」を含む文書を持ち出し、闇サイト公開や高額な恐喝要求につなげる。 被害企業の従業員や幹部にはスワッティングも行われており、RH-ISACは電話対応手順強化と発信者確認の徹底を勧告している。 | 中 | `source--daily-2c44dcb080c9a145473f` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

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
| source--daily-02e1336153d9062de8f2 | Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | bleepingcomputer.com | 2026-02-02 | https://www.bleepingcomputer.com/news/security/mandiant-details-how-shinyhunters-abuse-sso-to-steal-cloud-data/ | osint-report | TLP:CLEAR | 中 |
| source--daily-2c44dcb080c9a145473f | 新たな恐喝グループBlackFile、急増するビッシング攻撃との関連が判明 | bleepingcomputer.com | 2026-04-25 | https://www.bleepingcomputer.com/news/security/new-blackfile-extortion-gang-targets-retail-and-hospitality-orgs/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc6671--15492d6c3cf37155 | ShinyHunters |  | 不明 | cybercrime/ShinyHunters/ShinyHunters.pdf | report | TLP:CLEAR | 中 |
| source--unc6671--1b02430d978be1b1 | unc6671 |  | 不明 | actor_profile/evidence/unc6671.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
