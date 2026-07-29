# APT-C-37 脅威アクタープロファイル

- プロファイルID: `actor--apt-c-37`
- 状態: draft
- 更新日時: 2026-07-29T15:36:09Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

APT-C-37の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT-C-37**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Papa Bear | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Pat Bear | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Pat/Patted Bear | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Racquet Bear | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Slap Bear | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |

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
| APT-C-27 | distinct-from | Meta reported the two clusters as separate Syrian networks linked to different units within Syria's Air Force Intelligence. | 高 | `source--meta-syria-hackers-2021` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Pat Bear, APT-C-37 | canonical-name | 高 | Syria | http://blogs.360.cn/post/SEA_role_influence_cyberattacks.html<br>https://cybersecurity.att.com/blogs/labs-research/alien-labs-2019-analysis-of-threat-groups-molerats-and-apt-c-37#When:14:00:00Z<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Subgroup%3A+Pat+Bear%2C+APT-C-37&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 拍拍熊 - APT-C-37 | canonical-name | 高 |  | https://apt.360.net/report/apts/28.html<br>https://apt.360.net/report/apts/103.html |

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
| malware--sslove | SSLove | Likely in-house Android malware distributed as a fake WhatsApp application. | 不明 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| malware--sandrorat | SandroRAT | Commodity Android remote-access malware used in the observed campaign. | 不明 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |

### ツール

未確認

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infra--meta-apt-c-37-c2 | APT-C-37 command-and-control infrastructure | Long-running C2 server reported by Meta. | 不明 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Meta Syrian network disruption (October 2021) | cyber-espionage | 2021-10 | 2021-10 | 2021-11-16 | target--country--syria | malware--sslove, malware--sandrorat |  | victim--activity-rule--fd272643244685f97d5e | APT-C-37: Meta disrupted APT-C-37 infrastructure linked to a separate Syrian Air Force Intelligence unit. The actor used credential phishing, SandroRAT, and SSLove against opposition-linked targets. | 高 | `source--meta-syria-hackers-2021` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Syria | Meta observed targeting of people and organizations in Syria. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| sectors | Civil Society | Meta's observed victim set included Civil Society targets. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| sectors | Defense | Meta's observed victim set included Defense targets. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| sectors | Government | Meta's observed victim set included Government targets. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| roles | former military personnel | Meta identified former military personnel in the observed victim set. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |
| roles | Free Syrian Army-linked persons | Meta identified Free Syrian Army-linked persons in the observed victim set. | 2021-10 | 2021-10 | 高 | `source--meta-syria-hackers-2021` |

選定ロジック: Syrian civil-society, media, humanitarian, opposition, and former military targets holding politically or militarily relevant information.

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Meta Syrian network disruption (October 2021) | 非公開 | anonymous | unknown | reported | target--country--syria | malware--sandrorat, malware--sslove |  |  |  | 2021-10 | 2021-10 | 2021-11-16 | 高 | `source--meta-syria-hackers-2021` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 8件
- IOC観測: 12件
- 複数攻撃で観測: 0件
- 要レビュー候補: 6件
- 非IOC artifact観測: 10件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| The previous China attribution for APT-C-37 is contradicted by direct Meta observations linking the activity to Syrian Air Force Intelligence. | 高 | `source--meta-syria-hackers-2021` | The old assertion depended only on worksheet placement and is retained as superseded counterevidence in the claim audit. |

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
| source--apt-c-37--c5182ee6ef4d9146 | apt c 37 |  | 不明 | actor_profile/evidence/apt-c-37.csv | structured-data | TLP:CLEAR | 中 |
| source--apt-c-37--8b48290b6cf47748 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--apt-c-37--673fc95c3a98f3eb | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--meta-syria-hackers-2021 | Taking Action Against Hackers in Pakistan and Syria | Meta | 2021-11-16 | https://about.fb.com/news/2021/11/taking-action-against-hackers-in-pakistan-and-syria/ | vendor-research | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
