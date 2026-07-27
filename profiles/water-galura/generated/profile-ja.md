# Water Galura 脅威アクタープロファイル

- プロファイルID: `actor--water-galura`
- 状態: draft
- 更新日時: 2026-07-27T11:17:27Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Water Galuraの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Water Galura**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| GOLD FEATHER | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Water Galura](https://attack.mitre.org/groups/G1050) are the operators of the [Qilin](https://attack.mitre.org/software/S1242) Ransomware-as-a-Service (RaaS) who handle payload generation, ransom negotiations, and the publication of stolen data for [Qilin](https://attack.mitre.org/software/S1242) affilates recruited on Russian cybercrime forums. [Water Galura](https://attack.mitre.org/groups/G1050) have been active since at least 2022 and use a double extortion model where they demand payment for providing decryption keys and for refraining from publishing the stolen data to their leak site.(Citation: BushidoToken Qilin RaaS JUN 2024)(Citation: Sophos Qilin MSP APR 2025) |
| Capability | Qilin, Tor |
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
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Water Galura - G1050 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1050<br>https://blog.bushidotoken.net/2024/06/tracking-adversaries-qilin-raas.html<br>https://news.sophos.com/en-us/2025/04/01/sophos-mdr-tracks-ongoing-campaign-by-qilin-affiliates-targeting-screenconnect/ |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--qilin | Qilin | [Qilin](https://attack.mitre.org/software/S1242) is a ransomware family operated as a ransomware-as-a-service (RaaS) that has been active since at least 2022. It includes variants written in Go and Rust capable of targeting Windows, Linux, and VMware ESXi environments. [Qilin](https://attack.mitre.org/software/S1242) shares functionality overlaps with [Black Basta](https://attack.mitre.org/software/S1070), [REvil](https://attack.mitre.org/software/S0496), and [BlackCat](https://attack.mitre.org/software/S1068) ransomware. [Qilin](https://attack.mitre.org/software/S1242) affiliates have targeted multiple entities worldwide with the majority of victims in the US, France, Canada, and the UK, primarily in the manufacturing, technology, financial services, and healthcare sectors.(Citation: Trend Micro Agenda Ransomware AUG 2022)(Citation: SentinelOne Qilin NOV 2022)(Citation: BushidoToken Qilin RaaS JUN 2024)(Citation: Sophos Qilin MSP APR 2025)(Citation: Trend Micro Agenda Ransomware OCT 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--tor | Tor | [Tor](https://attack.mitre.org/software/S0183) is a software suite and network that provides increased anonymity on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and routing information. [Tor](https://attack.mitre.org/software/S0183) utilizes "Onion Routing," in which messages are encrypted with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded on to the next node until it reaches its destination. (Citation: Dingledine Tor The Second-Generation Onion Router) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Qilinランサムウェア、身代金増額を迫る「弁護士呼び出し」機能を追加 | ransomware-extortion | 不明 | 不明 | 2025-06-21 | QilinランサムウェアRaaSがアフィリエイト向けパネルに「弁護士呼び出し」機能を追加し、被害者に支払い圧力を強化。 Qilinは、2025年4月に72件の被害、5月に55件を確認、通年でCl0p・Akiraに次ぐ304件を記録。 アフィリエイトにはRust/C製ペイロード、ネットワーク拡散、ログクリーン、交渉自動化など高度な攻撃ツールを提供。 法的支援、スパムサービス、PB規模のデータストレージ、DDoSツールなどを備えたフルサービスのサイバー犯罪プラットフォームに進化。 RansomHubのアフィリエイトがQilinに移行し、ここ数か月のQilinランサムウェア活動の急増に寄与 | 中 | `source--daily-3c55cd8958f6103f4eaf` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Impact | T1486 | Data Encrypted for Impact | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| source--daily-3c55cd8958f6103f4eaf | Qilinランサムウェア、身代金増額を迫る「弁護士呼び出し」機能を追加 | thehackernews.com | 2025-06-21 | https://thehackernews.com/2025/06/qilin-ransomware-adds-call-lawyer.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--water-galura--280658d2598270cb | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--water-galura--83ea455fedc5476b | water galura |  | 不明 | actor_profile/evidence/water-galura.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
