# UNC6671 脅威アクタープロファイル

- プロファイルID: `actor--unc6671`
- 状態: draft
- 更新日時: 2026-09-21T04:38:04Z
- 構造バージョン: 1.2.0

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

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| UNC6240 | taxonomy-overlaps-with | GTIG tracks UNC6661, UNC6671, and UNC6240 separately within recent ShinyHunters-branded SaaS theft reporting to preserve possible partnership and impersonation boundaries. | 高 | `source--gtig-shinyhunters-saas-clusters-2026` |
| UNC6661 | taxonomy-overlaps-with | GTIG tracks UNC6661, UNC6671, and UNC6240 separately within recent ShinyHunters-branded SaaS theft reporting to preserve possible partnership and impersonation boundaries. | 高 | `source--gtig-shinyhunters-saas-clusters-2026` |

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
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UNC6671 | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

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
| UNC6671、vishingでSSO資格情報を窃取しSaaSデータを流出 | ransomware-extortion | 2026-01 | 不明 | 2026-01-30 |  |  |  | victim--activity-rule--a246d00432371496b99a | Mandiantは、UNC6671が2026年1月初旬からIT担当者を装って電話し、被害組織を偽の認証サイトへ誘導してSSO資格情報とMFAコードを窃取したと報告した。侵入後はOktaアカウントへアクセスし、PowerShellを用いてSharePointとOneDriveの機密データを取得した。手口はUNC6661と類似する一方、UNC6671に続く恐喝メールはShinyHunters名義ではなく、異なるTox IDを使用しており、Mandiantは別の人物が関与する可能性を示している。 | 高 | `source--gtig-shinyhunters-saas-clusters-2026` |
| ヘッジファンドへのサイバー攻撃、BlackFile関連の恐喝グループUNC6671と関連 | ransomware-extortion | 不明 | 不明 | 2026-08-07 | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | victim--activity-rule--9d131ccb215967a3529e | ヘッジファンド、プライベートエクイティ、金融機関を狙う最近の攻撃が、BlackFile関連の恐喝グループUNC6671に関連付けられた。 Point72、Millennium Management、Two Sigma、Citadelなどが標的となり、従業員を電話で騙すボイスフィッシングが使用された。 攻撃者は企業ITヘルプデスクを装ってパスキーやMFA更新を要求し、AiTMフィッシングサイトへ誘導して認証情報とセッションCookieを窃取する。 Microsoft 365やOktaのSSOアカウントを侵害後、接続されたクラウドサービスから自動的にデータを窃取し、セキュリティ通知などを削除する。 UNC6671はBlackFileに加えてRedact、Pink、Helix、Falconを使用し、Mandiantは現在UNC6671によって侵害された数十組織の侵害対応を支援している。 | 高 | `source--daily-0f56214542b30c75b57a` |
| 新たな恐喝グループBlackFile、急増するビッシング攻撃との関連が判明 | ransomware-extortion | 2026-02 | 不明 | 2026-04-25 | target--activity-rule--sector--570d54d1d21fab6540a9, target--targeting-audit--country--0051ba349f4de879afc7 |  |  | victim--activity-rule--c73d93cb0373fa6407ec | 2026年2月以降、金銭目的の新たな脅威グループBlackFileが、小売・ホスピタリティ業界を狙うデータ窃取と恐喝攻撃に関与していると報告された。 攻撃者は企業のITヘルプデスクを装い、偽の社内ログインページへ誘導して従業員の認証情報とワンタイムパスコードを盗み出す。 盗んだ認証情報で自分たちの端末を登録してMFAを回避し、社内ディレクトリを悪用して幹部レベルのアカウントへアクセスを広げる。 その後、SalesforceやSharePointの標準APIで「confidential」や「SSN」を含む文書を持ち出し、闇サイト公開や高額な恐喝要求につなげる。 被害企業の従業員や幹部にはスワッティングも行われており、RH-ISACは電話対応手順強化と発信者確認の徹底を勧告している。 | 中 | `source--daily-2c44dcb080c9a145473f` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| UNC6671、vishingでSSO資格情報を窃取しSaaSデータを流出 | UNC6671 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: UNC6671によるSSO・SaaSデータ窃取 | 高 |
| ヘッジファンドへのサイバー攻撃、BlackFile関連の恐喝グループUNC6671と関連 | UNC6671 | 情報なし | 情報なし | 情報なし | 金融 | 被害事例: ヘッジファンドへのサイバー攻撃、BlackFile関連の恐喝グループUNC6671と関連 | 高 |
| 新たな恐喝グループBlackFile、急増するビッシング攻撃との関連が判明 | UNC6671 | 情報なし | 情報なし | 情報なし | 小売・ホスピタリティ, タイ | 被害事例: 新たな恐喝グループBlackFile、急増するビッシング攻撃との関連が判明 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | タイ | 活動「新たな恐喝グループBlackFile、急増するビッシング攻撃との関連が判明」の記述で標的・被害国として明示されている。 | 2026-02 | 不明 | 中 | `source--daily-2c44dcb080c9a145473f` |
| sectors | 金融 | 活動「ヘッジファンドへのサイバー攻撃、BlackFile関連の恐喝グループUNC6671と関連」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-0f56214542b30c75b57a` |
| sectors | 小売・ホスピタリティ | 活動「新たな恐喝グループBlackFile、急増するビッシング攻撃との関連が判明」の記述で標的として明示された産業。 | 2026-02 | 不明 | 中 | `source--daily-2c44dcb080c9a145473f` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ヘッジファンドへのサイバー攻撃、BlackFile関連の恐喝グループUNC6671と関連 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | メール／メールアカウント, クラウド／SaaS | data-theft: Microsoft 365やOktaのSSOアカウントを侵害後、接続されたクラウドサービスから自動的にデータを窃取し、セキュリティ通知などを削除する。<br>credential-theft: 攻撃者は企業ITヘルプデスクを装ってパスキーやMFA更新を要求し、AiTMフィッシングサイトへ誘導して認証情報とセッションCookieを窃取する。 | 不明 | 不明 | 2026-08-07 | 高 | `source--daily-0f56214542b30c75b57a` |
| 被害事例: UNC6671によるSSO・SaaSデータ窃取 | 非公開 | aggregate | multiple-organizations | reported |  |  |  | メール／メールアカウント | data-theft: UNC6671、vishingでSSO資格情報を窃取しSaaSデータを流出 | 2026-01 | 不明 | 2026-01-30 | 高 | `source--gtig-shinyhunters-saas-clusters-2026` |
| 被害事例: 新たな恐喝グループBlackFile、急増するビッシング攻撃との関連が判明 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--570d54d1d21fab6540a9 |  |  | エンドポイント, クラウド／SaaS | data-theft: 2026年2月以降、金銭目的の新たな脅威グループBlackFileが、小売・ホスピタリティ業界を狙うデータ窃取と恐喝攻撃に関与していると報告された。 | 2026-02 | 不明 | 2026-04-25 | 中 | `source--daily-2c44dcb080c9a145473f` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

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
| source--daily-0f56214542b30c75b57a | ヘッジファンドへのサイバー攻撃、BlackFile関連の恐喝グループUNC6671と関連 | cloud.google.com | 2026-08-07 | https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments | osint-report | TLP:CLEAR | 中 |
| source--daily-2c44dcb080c9a145473f | 新たな恐喝グループBlackFile、急増するビッシング攻撃との関連が判明 | bleepingcomputer.com | 2026-04-25 | https://www.bleepingcomputer.com/news/security/new-blackfile-extortion-gang-targets-retail-and-hospitality-orgs/ | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc6671--15492d6c3cf37155 | ShinyHunters |  | 不明 | cybercrime/ShinyHunters/ShinyHunters.pdf | report | TLP:CLEAR | 中 |
| source--unc6671--1b02430d978be1b1 | unc6671 |  | 不明 | actor_profile/evidence/unc6671.csv | structured-data | TLP:CLEAR | 中 |
| source--gtig-shinyhunters-saas-clusters-2026 | Vishing for Access: Tracking the Expansion of ShinyHunters-Branded SaaS Data Theft | Mandiant / Google Threat Intelligence Group | 2026-01-30 | https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
