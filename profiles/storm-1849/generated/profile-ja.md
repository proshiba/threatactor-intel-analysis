# Storm-1849 脅威アクタープロファイル

- プロファイルID: `actor--storm-1849`
- 状態: draft
- 更新日時: 2026-07-29T15:36:11Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Storm-1849の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Storm-1849**
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
| misp-threat-actor | Storm-1849 | canonical-name | 高 |  | https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/ |
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
| ArcaneDoorハッカー、政府ネットワーク侵入にシスコのゼロデイを利用 | malware-campaign | 不明 | 不明 | 2024-04-25 |  |  |  |  | ArcaneDoorグループがシスコ製品の脆弱性を悪用。 政府機関のネットワークが全世界で影響を受ける。 CiscoのAdaptive Security Appliance（ASA）またはFirepower Threat Defense（FTD）で、2つのゼロデイ脆弱性が利用された。 CVE-2024-20353（サービス拒否）とCVE-2024-20359（永続的なローカルコード実行） Line RunnerとLine Dancerという2つのマルウェアを使い、機器の制御とデータ抽出を実行。 シスコが修正パッチの配布とアップグレードを推奨。 | 中 | `source--daily-d9c025cbaad1eeab6c4c` |
| CISA、ゼロデイ攻撃で悪用されたCisco脆弱性の緊急修正を連邦機関に指示 | intrusion | 不明 | 不明 | 2025-09-26 |  |  |  | victim--activity-rule--7d9de1948e3665d055bf | CISAは緊急指令25-03を発出し、ゼロデイで悪用されたCisco ASA/FTDの脆弱性修正をFCEB機関に義務付けた。 対象はCVE-2025-20333とCVE-2025-20362で、連鎖時は認証不要で遠隔から装置を完全に制御され得る。 各機関は全ASA/Firepowerの洗い出し、CISA手順でのフォレンジック収集と侵害評価、侵害機器の即時切断が求められる。 非侵害機器は9月26日12:00（米東部）までにパッチ適用、EoSのASAは9月30日までに恒久的にネットワークから外す。 攻撃はArcaneDoor作戦に関連付けられ、ROMMON改変やログ無効化等の高度な回避・持続化手口が確認された。 | 中 | `source--daily-0bfff87681065487c0a5` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: CISA、ゼロデイ攻撃で悪用されたCisco脆弱性の緊急修正を連邦機関に指示 | 非公開 | anonymous | unknown | reported |  |  |  |  |  | 不明 | 不明 | 2025-09-26 | 中 | `source--daily-0bfff87681065487c0a5` |

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
| source--daily-0bfff87681065487c0a5 | CISA、ゼロデイ攻撃で悪用されたCisco脆弱性の緊急修正を連邦機関に指示 | bleepingcomputer.com | 2025-09-26 | https://www.bleepingcomputer.com/news/security/cisa-orders-agencies-to-patch-cisco-flaws-exploited-in-zero-day-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-d9c025cbaad1eeab6c4c | ArcaneDoorハッカー、政府ネットワーク侵入にシスコのゼロデイを利用 | bleepingcomputer.com | 2024-04-25 | https://www.bleepingcomputer.com/news/security/arcanedoor-hackers-exploit-cisco-zero-days-to-breach-govt-networks/ | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--storm-1849--0a1cb35487ca2b17 | storm 1849 |  | 不明 | actor_profile/evidence/storm-1849.csv | structured-data | TLP:CLEAR | 中 |
| source--storm-1849--35f0a39d0a8d91a7 | UK NCC Group Cyber Threat Intelligence Report September 2025 |  | 2025 | summary/2025/UK_NCC_Group_Cyber_Threat_Intelligence_Report_September_2025_.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
