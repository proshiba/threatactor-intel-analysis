# Storm-1849 脅威アクタープロファイル

- プロファイルID: `actor--storm-1849`
- 状態: draft
- 更新日時: 2026-09-21T08:16:06Z
- 構造バージョン: 1.3.0

## エグゼクティブサマリー

Storm-1849の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Storm-1849**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| UAT4356 | Cisco Talos / Microsoft Threat Intelligence | exact | 高 | `source--cisco-talos-arcanedoor-2024` | Cisco states that the actor it tracks as UAT4356 is tracked by Microsoft as Storm-1849. Exactness is scoped to that explicit mapping. |

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
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Storm-1849 | canonical-name | 高 |  | https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/ |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--firestarter | FIRESTARTER | Custom UAT4356 backdoor executing inside Cisco LINA and persisting through CSP_MOUNT_LIST manipulation. | 不明 | 不明 | 高 | `source--cisco-talos-uat4356-firestarter-2026` |
| malware--line-dancer | Line Dancer | Memory-resident shellcode interpreter used on Cisco ASA devices. | 2023-12 | 2024-01 | 高 | `source--cisco-talos-arcanedoor-2024` |
| malware--line-runner | Line Runner | Persistent Lua-based backdoor used on Cisco ASA devices. | 2023-12 | 2024-01 | 高 | `source--cisco-talos-arcanedoor-2024` |

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
| UAT4356／Storm-1849によるArcaneDoor作戦 | malware-campaign | 2023-12 | 2024-01 | 2024-04-24 | target--targeting-audit--region--23d705447763748f4693 | malware--line-dancer, malware--line-runner |  |  | Cisco Talosは、UAT4356（Microsoft: Storm-1849）が世界各地の政府ネットワークにあるCisco ASAを狙った諜報作戦ArcaneDoorを報告した。主活動は2023年12月～2024年1月で、Line DancerとLine Runnerを用いて設定変更、偵察、通信取得・流出、永続化を行った。 | 高 | `source--cisco-talos-arcanedoor-2024`, `source--daily-d9c025cbaad1eeab6c4c` |
| CISA、ゼロデイ攻撃で悪用されたCisco脆弱性の緊急修正を連邦機関に指示 | intrusion | 不明 | 不明 | 2025-09-26 |  |  |  | victim--activity-rule--7d9de1948e3665d055bf | CISAは緊急指令25-03を発出し、ゼロデイで悪用されたCisco ASA/FTDの脆弱性修正をFCEB機関に義務付けた。 対象はCVE-2025-20333とCVE-2025-20362で、連鎖時は認証不要で遠隔から装置を完全に制御され得る。 各機関は全ASA/Firepowerの洗い出し、CISA手順でのフォレンジック収集と侵害評価、侵害機器の即時切断が求められる。 非侵害機器は9月26日12:00（米東部）までにパッチ適用、EoSのASAは9月30日までに恒久的にネットワークから外す。 攻撃はArcaneDoor作戦に関連付けられ、ROMMON改変やログ無効化等の高度な回避・持続化手口が確認された。 | 中 | `source--daily-0bfff87681065487c0a5` |
| UAT4356、Cisco FirepowerへFIRESTARTERを展開 | malware-campaign | 不明 | 不明 | 2026-04-23 |  | malware--firestarter |  |  | Cisco Talosは、UAT4356がCisco Firepower/FXOS機器を継続的に標的とし、CVE-2025-20333とCVE-2025-20362を悪用して独自バックドアFIRESTARTERを展開したと報告した。FIRESTARTERはLINAプロセス内で任意コードを実行し、CSP_MOUNT_LISTを改変して再起動をまたぐ永続化を行う。 | 高 | `source--cisco-talos-uat4356-firestarter-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| UAT4356／Storm-1849によるArcaneDoor作戦 | Storm-1849 | Line Dancer, Line Runner | 情報なし | 情報なし | 全世界 | 情報なし | 高 |
| CISA、ゼロデイ攻撃で悪用されたCisco脆弱性の緊急修正を連邦機関に指示 | Storm-1849 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: CISA、ゼロデイ攻撃で悪用されたCisco脆弱性の緊急修正を連邦機関に指示 | 中 |
| UAT4356、Cisco FirepowerへFIRESTARTERを展開 | Storm-1849 | FIRESTARTER | 情報なし | 情報なし | 情報なし | 情報なし | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 全世界 | 活動「UAT4356／Storm-1849によるArcaneDoor作戦」の記述で標的地域として全世界が明示されている。 | 2023-12 | 2024-01 | 中 | `source--cisco-talos-arcanedoor-2024`, `source--daily-d9c025cbaad1eeab6c4c` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

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
| source--daily-0bfff87681065487c0a5 | CISA、ゼロデイ攻撃で悪用されたCisco脆弱性の緊急修正を連邦機関に指示 | bleepingcomputer.com | 2025-09-26 | https://www.bleepingcomputer.com/news/security/cisa-orders-agencies-to-patch-cisco-flaws-exploited-in-zero-day-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-d9c025cbaad1eeab6c4c | ArcaneDoorハッカー、政府ネットワーク侵入にシスコのゼロデイを利用 | bleepingcomputer.com | 2024-04-25 | https://www.bleepingcomputer.com/news/security/arcanedoor-hackers-exploit-cisco-zero-days-to-breach-govt-networks/ | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--storm-1849--0a1cb35487ca2b17 | storm 1849 |  | 不明 | actor_profile/evidence/storm-1849.csv | structured-data | TLP:CLEAR | 中 |
| source--storm-1849--35f0a39d0a8d91a7 | UK NCC Group Cyber Threat Intelligence Report September 2025 |  | 2025 | summary/2025/UK_NCC_Group_Cyber_Threat_Intelligence_Report_September_2025_.pdf | report | TLP:CLEAR | 中 |
| source--cisco-talos-arcanedoor-2024 | ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices | Cisco Talos | 2024-04-24 | https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--cisco-talos-uat4356-firestarter-2026 | UAT-4356's Targeting of Cisco Firepower Devices | Cisco Talos | 2026-04-23 | https://blog.talosintelligence.com/uat-4356-firestarter/ | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
