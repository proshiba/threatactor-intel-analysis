# APT-C-27 脅威アクタープロファイル

- プロファイルID: `actor--apt-c-27`
- 状態: draft
- 更新日時: 2026-07-29T15:36:09Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

APT-C-27の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT-C-27**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Golden Rat | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Goldmouse | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Goldmouse/Gold Mouse/Gold Rat | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Link to OilRig? | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 97; mapping requires review. |

## 帰属

Meta linked the observed 2021 network to Syria's Air Force Intelligence.

- 国: Syria
- スポンサー種別: state
- 確度: 高
- 証拠: `source--meta-syria-hackers-2021`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| APT-C-37 | distinct-from | Meta reported the two clusters as separate Syrian networks linked to different units within Syria's Air Force Intelligence. | 高 | `source--meta-syria-hackers-2021` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim | Middle East |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Goldmouse, APT-C-27 | canonical-name | 高 | Syria | https://ti.360.net/blog/articles/apt-c-27-(goldmouse):-suspected-target-attack-against-the-middle-east-with-winrar-exploit-en/<br>https://blog.360totalsecurity.com/en/the-sample-analysis-of-apt-c-27s-recent-attack/<br>http://blogs.360.cn/post/SEA_role_influence_cyberattacks.html |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT-C-27 | canonical-name | 高 | SY | https://ti.360.net/blog/articles/apt-c-27-(goldmouse):-suspected-target-attack-against-the-middle-east-with-winrar-exploit-en/<br>https://ti.360.net/blog/articles/analysis-of-apt-c-27/<br>https://web.archive.org/web/20180827024318/http://csecybsec.com/download/zlab/20180723_CSE_APT27_Syria_v1.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 黄金鼠 - APT-C-27 | canonical-name | 高 |  | https://apt.360.net/report/apts/100.html<br>https://apt.360.net/report/apts/98.html<br>https://apt.360.net/report/apts/26.html |

### 関係性候補（未統合）

候補なし

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--silverhawk | SilverHawk | Custom Android malware also called HmzaRAT. | 不明 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| malware--meta-unnamed-android-2021 | Unnamed Android family (Meta 2021) | Previously unnamed Android malware distributed in trojanized Telegram and Syrian news applications. | 不明 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |

### ツール

未確認

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infra--meta-apt-c-27-phishing | APT-C-27 credential phishing infrastructure | Blogspot-hosted credential phishing pages reported by Meta. | 不明 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| infra--meta-apt-c-27-delivery | APT-C-27 Android malware delivery infrastructure | Compromised and cloud-hosted sites used to distribute Android malware. | 2020 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| infra--meta-apt-c-27-c2 | APT-C-27 command-and-control infrastructure | Server used for C2 and Android malware distribution. | 不明 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Meta Syrian network disruption (October 2021) | cyber-espionage | 2021-10 | 2021-10 | 2021-11-16 | target--country--syria | malware--silverhawk, malware--meta-unnamed-android-2021 |  | victim--activity-rule--fd272643244685f97d5e | APT-C-27: Meta disrupted SEA/APT-C-27 accounts and infrastructure linked to Syrian Air Force Intelligence. The actor used credential phishing and trojanized Android applications. | 高 | `source--meta-syria-hackers-2021` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Syria | Meta observed targeting of people and organizations in Syria. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| sectors | Civil Society | Meta's observed victim set included Civil Society targets. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| sectors | Defense | Meta's observed victim set included Defense targets. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| sectors | Government | Meta's observed victim set included Government targets. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| roles | activists | Meta identified activists in the observed victim set. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| roles | humanitarian organizations | Meta identified humanitarian organizations in the observed victim set. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| roles | journalists | Meta identified journalists in the observed victim set. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| roles | military opposition | Meta identified military opposition in the observed victim set. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |

選定ロジック: Syrian civil-society, media, humanitarian, opposition, and former military targets holding politically or militarily relevant information.

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Meta Syrian network disruption (October 2021) | 非公開 | anonymous | unknown | reported | target--country--syria | malware--meta-unnamed-android-2021, malware--silverhawk |  | モバイル端末 |  | 2021-10 | 2021-10 | 2021-11-16 | 高 | `source--meta-syria-hackers-2021` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 14件
- IOC観測: 15件
- 複数攻撃で観測: 0件
- 要レビュー候補: 6件
- 非IOC artifact観測: 23件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| The previous China attribution for APT-C-27 is contradicted by direct Meta observations linking the activity to Syrian Air Force Intelligence. | 高 | `source--meta-syria-hackers-2021` | The old assertion depended only on worksheet placement and is retained as superseded counterevidence in the claim audit. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- Structured OSINT country metadata is disjoint from the profile attribution; see osint-crosscheck.json and retain both assessments pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--apt-c-27--ce2f663514cbb01c | apt c 27 |  | 不明 | actor_profile/evidence/apt-c-27.csv | structured-data | TLP:CLEAR | 中 |
| source--apt-c-27--89e05968dfed2712 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--apt-c-27--ad52130be22386ef | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--apt-c-27--507bf9aae2d6fe69 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--apt-c-27--1112f361b59e7278 | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--apt-c-27--edc480f4b1c85db6 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--meta-syria-hackers-2021 | Taking Action Against Hackers in Pakistan and Syria | Meta | 2021-11-16 | https://about.fb.com/news/2021/11/taking-action-against-hackers-in-pakistan-and-syria/ | vendor-research | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
