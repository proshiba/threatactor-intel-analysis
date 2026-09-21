# UAC-0010 脅威アクタープロファイル

- プロファイルID: `actor--uac-0010`
- 状態: deprecated
- 更新日時: 2026-09-21T04:15:15Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UAC-0010の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0010**
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
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Gamaredon Group | canonical-name | 高 | Russia | https://www.lookingglasscyber.com/wp-content/uploads/2015/08/Operation_Armageddon_Final.pdf<br>https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-evolution/<br>https://www.fortinet.com/blog/threat-research/gamaredon-group-ttp-profile-analysis.html |
| cert-ua-uac-index | UAC-0010 | canonical-name | 高 |  | https://cert.gov.ua/article/971405<br>https://cert.gov.ua/article/40240<br>https://cert.gov.ua/article/1229152 |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Gamaredon Group | canonical-name | 高 | RU | http://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution<br>https://www.lookingglasscyber.com/wp-content/uploads/2015/08/Operation_Armageddon_Final.pdf<br>https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-evolution |
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

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| This profile is an exact-identity duplicate of Gamaredon (actor--gamaredon). | 高 | `source--scpc-uac0010-gamaredon-2023` | Entity-boundary correction. |

### 情報ギャップ


### 不確実性


## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-f9666a37c61d10f83b24 | FSBのマトリョーシカ #1/3：展開され続けるGamaredonの贈り物――GammaPhishとGammaWorm | blog.sekoia.io | 2026-06-03 | https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/ | osint-report | TLP:CLEAR | 中 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--uac-0010--0ba16103b9604a22 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--uac-0010--2ffd50a1c7118090 | Cyber operations by russia new goals, tools and groups |  | 不明 | International Strategic/Russia/Cyber operations by russia new goals, tools and groups.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--468ae9d2482ad88e | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--7796988d52bfe416 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--a76dad0c653387b5 | Russia’s Cyber Tactics Lessons Learned 2022 |  | 2022 | International Strategic/Russia/Russia’s Cyber Tactics Lessons Learned 2022.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--b45fb340c5aab58c | uac 0010 |  | 不明 | actor_profile/evidence/uac-0010.csv | structured-data | TLP:CLEAR | 中 |
| source--uac-0010--d67ea89733ee989d | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--fe514e7b8f9ef46b | RussianCyber |  | 不明 | summary/2024/RussianCyber.pdf | report | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--scpc-uac0010-gamaredon-2023 | Another UAC-0010 Story | State Cyber Protection Centre of Ukraine | 2023-01 | https://scpc.gov.ua/api/docs/19b0a96e-8c31-44bf-863e-cd3e0b651f22/19b0a96e-8c31-44bf-863e-cd3e0b651f22.pdf | government-technical-report | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
