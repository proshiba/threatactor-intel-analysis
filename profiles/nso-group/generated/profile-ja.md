# NSO Group 脅威アクタープロファイル

- プロファイルID: `actor--nso-group`
- 状態: draft
- 更新日時: 2026-07-29T15:36:11Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

NSO Groupの標準化プロファイル。リポジトリ内の専用資料8件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **NSO Group**
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

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| commercial | Commercial offensive-security or surveillance operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

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
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | Night Tsunami | canonical-name | 高 | IL, Israel | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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
| NSOグループ、1,400人のWhatsAppユーザーへのスパイウェア攻撃で1億6,700万ドルの罰金 | cyber-espionage | 不明 | 不明 | 2025-05-08 |  |  |  | victim--activity-rule--a9280aeb33960dcd9ad1 | 米連邦陪審は、イスラエルのスパイウェア企業NSOグループに対し、WhatsAppユーザー1,400人への攻撃に関して1億6,700万ドルの罰金を命じた。 攻撃は2019年5月、WhatsAppの当時ゼロデイであった脆弱性（CVE-2019-3568）を悪用し、Pegasusスパイウェアをユーザーのデバイスに感染させた。 この判決は、スパイウェア開発企業が違法な監視行為で初めて法的責任を問われた画期的な事例となった。 Meta（旧Facebook）は、この判決をデジタルプライバシーとセキュリティの重要な勝利と位置づけている。 裁判では、NSO Groupが感染操作に直接関与しており、直接的な責任があることが明らかになった。 | 中 | `source--daily-a62bcc3c33756a92b707` |
| WhatsApp、NSOの新たなスパイウェア・フィッシング攻撃を阻止したと発表 | phishing-campaign | 不明 | 不明 | 2026-06-09 |  |  |  |  | WhatsAppは、ユーザーから報告されたソーシャルエンジニアリング攻撃を調査し、NSO関連の攻撃を阻止した。 攻撃者は標的に悪性リンクをクリックさせ、WhatsApp外部のWebサイトへ誘導しようとしていた。 Metaは、攻撃者がWhatsApp上でテスト用アカウントやグループを作成していたことも確認し、削除した。 NSO Groupはイスラエルの商用スパイウェア企業で、Pegasusを政治家、活動家、記者らに使ってきたことで知られる。 Metaは、今回の活動が2025年の恒久的差止命令に違反すると主張している。 | 高 | `source--daily-e8f4b9d0a614c1696cf5` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: NSOグループ、1,400人のWhatsAppユーザーへのスパイウェア攻撃で1億6,700万ドルの罰金 | 非公開 | aggregate | multiple-organizations | reported |  |  |  |  | privacy: Meta（旧Facebook）は、この判決をデジタルプライバシーとセキュリティの重要な勝利と位置づけている。 | 不明 | 不明 | 2025-05-08 | 中 | `source--daily-a62bcc3c33756a92b707` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 48件
- IOC観測: 67件
- 複数攻撃で観測: 0件
- 要レビュー候補: 23件
- 非IOC artifact観測: 31件（`artifacts.csv`）

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
| source--daily-a62bcc3c33756a92b707 | NSOグループ、1,400人のWhatsAppユーザーへのスパイウェア攻撃で1億6,700万ドルの罰金 | bleepingcomputer.com | 2025-05-08 | https://www.bleepingcomputer.com/news/legal/nso-group-fined-167m-for-spyware-attacks-on-1-400-whatsapp-users/ | osint-report | TLP:CLEAR | 中 |
| source--daily-e8f4b9d0a614c1696cf5 | WhatsApp、NSOの新たなスパイウェア・フィッシング攻撃を阻止したと発表 | about.fb.com | 2026-06-09 | https://about.fb.com/news/2026/06/fighting-spyware-an-update-from-whatsapp/ | osint-report | TLP:CLEAR | 中 |
| source--nso-group--25c12a20509800b5 | ExoneratingMorocco DisprovingTheSpyware |  | 不明 | NSOGroup/Morocco/ExoneratingMorocco-DisprovingTheSpyware.pdf | report | TLP:CLEAR | 中 |
| source--nso-group--2f4d62bc993498f9 | README |  | 不明 | NSOGroup/Morocco/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--nso-group--63bc982219df0301 | VB2022 Exploit archaeology a forensic history of in the wild NSO Group exploits |  | 2022 | NSOGroup/VB2022-Exploit-archaeology-a-forensic-history-of-in-the-wild-NSO-Group-exploits.pdf | report | TLP:CLEAR | 中 |
| source--nso-group--70e88ee0cb1df29d | Six Palestinian human rights defenders hacked with |  | 不明 | NSOGroup/Six Palestinian human rights defenders hacked with.pdf | report | TLP:CLEAR | 中 |
| source--nso-group--769597e33c7ccdd4 | README |  | 不明 | NSOGroup/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--nso-group--9fef2836510723a4 | Asia 24 Frielingsdorf YouShallNotPassAnalysing |  | 不明 | NSOGroup/Asia-24-Frielingsdorf-YouShallNotPassAnalysing.pdf | report | TLP:CLEAR | 中 |
| source--nso-group--b87edb53311bf320 | article 3 |  | 不明 | NSOGroup/Morocco/article_3.pdf | report | TLP:CLEAR | 中 |
| source--nso-group--bfa99cbc899e9b3a | Memo Citizen Lab Raymundo Ramos 230304 |  | 不明 | NSOGroup/Memo-Citizen-Lab-Raymundo-Ramos-230304.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
