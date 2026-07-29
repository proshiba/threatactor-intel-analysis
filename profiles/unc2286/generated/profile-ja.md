# UNC2286 脅威アクタープロファイル

- プロファイルID: `actor--unc2286`
- 状態: draft
- 更新日時: 2026-07-29T15:36:12Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC2286の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC2286**
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
| etda-threat-group-cards | Salt Typhoon, GhostEmperor | canonical-name | 高 | China | https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2021/09/30094337/GhostEmperor_technical-details_PDF_eng.pdf<br>https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | GhostEmperor | canonical-name | 高 | CN | https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2021/09/30094337/GhostEmperor_technical-details_PDF_eng.pdf<br>https://www.welivesecurity.com/2021/09/23/famoussparrow-suspicious-hotel-guest/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Earth Estries | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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
| Salt Typhoon、JumbledPathマルウェアを使用して米国の通信ネットワークをスパイ | cyber-espionage | 不明 | 不明 | 2025-02-21 | target--activity-rule--country--6604ad21c713b8dfd8c7 |  |  | victim--activity-rule--b1249093f60c28b7f2b3 | 中国政府支援のハッキンググループであるSalt Typhoon（別名：Earth Estries、GhostEmperor、UNC2286）は、米国の通信プロバイダーを標的とし、カスタムマルウェア「JumbledPath」を使用してネットワークトラフィックを監視し、機密データを収集しています。 Salt Typhoonは、2019年以降活動しており、主に政府機関や通信会社への侵入を行っています。 最近、米国当局は、Salt TyphoonがVerizon、AT&T、Lumen Technologies、T-Mobileなどの米国の主要通信プロバイダーへの侵入に成功し、一部の政府関係者のプライベートな通信や裁判所認可の盗聴要求に関する情報を盗み取ったと確認しました。 さらに、Recorded FutureのInsikt Groupは、Salt Typhoonが2024年12月から2025年1月の間に、米国、南米、インドを含む1,000台以上のCiscoネットワークデバイスを標的にしたと報告しています。 Cisco Talosは、Salt Typhoonのハッカーが主に盗まれた認証情報を使用して、コアネットワークインフラストラクチャに侵入し、一部のケースでは3年以上にわたり活動していたと明らかにしました。 | 中 | `source--daily-976395d39cbe624f587e` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | 活動「Salt Typhoon、JumbledPathマルウェアを使用して米国の通信ネットワークをスパイ」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-976395d39cbe624f587e` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Salt Typhoon、JumbledPathマルウェアを使用して米国の通信ネットワークをスパイ | 非公開 | anonymous | unknown | reported | target--activity-rule--country--6604ad21c713b8dfd8c7 |  |  |  |  | 不明 | 不明 | 2025-02-21 | 中 | `source--daily-976395d39cbe624f587e` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 2件（`artifacts.csv`）

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
| source--daily-976395d39cbe624f587e | Salt Typhoon、JumbledPathマルウェアを使用して米国の通信ネットワークをスパイ | bleepingcomputer.com | 2025-02-21 | https://www.bleepingcomputer.com/news/security/salt-typhoon-uses-jumbledpath-malware-to-spy-on-us-telecom-networks/ | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc2286--33918c43e145da63 | [Report] Bitsight State of the Underground 2026 |  | 2026 | summary/2026/[Report] Bitsight State of the Underground 2026.pdf | report | TLP:CLEAR | 中 |
| source--unc2286--56493a9195ef18a0 | unc2286 |  | 不明 | actor_profile/evidence/unc2286.csv | structured-data | TLP:CLEAR | 中 |
| source--unc2286--f588ad9bd7fcfa82 | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
