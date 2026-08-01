# APT-C-01 脅威アクタープロファイル

- プロファイルID: `actor--apt-c-01`
- 状態: draft
- 更新日時: 2026-07-29T23:11:59Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

APT-C-01の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT-C-01**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| PoisonVine | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |

## 帰属

Public reporting places Green Spot / PoisonVine / APT-C-01 in Taiwan and describes targeting of Chinese government, military, aviation, research, and maritime entities. Exact state command is not independently confirmed.

- 国: Taiwan
- スポンサー種別: state
- 確度: 中
- 証拠: `source--cfr-taiwan-offensive-cyber-2022`, `source--apt-c-01--c225ad868f45dc7c`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | Poison Ivy, ZxShell, Kanbox RAT, CVE-2012-0158, CVE-2014-6352, CVE-2017-8759 |
| Infrastructure |  |
| Victim | government agencies, military individuals, research institutes, maritime agencies |
| Socio-political | China |

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
| misp-threat-actor | GreenSpot | single-alias-intersection | 中 | TW | https://hunt.io/blog/greenspot-apt-targets-163com-fake-downloads-spoofing<br>https://www.antiy.net/p/greenspotoperations-grow-for-many-years/<br>https://www.virusbulletin.com/virusbulletin/2019/11/vb2019-paper-vine-climbing-over-great-firewall-longterm-attack-against-china/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 毒云藤 - APT-C-01 | canonical-name | 高 | taiwan | https://apt.360.net/report/apts/2.html |

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
| malware--poison-ivy | Poison Ivy | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--zxshell | ZxShell | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--kanbox-rat | Kanbox RAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2012-0158 | CVE-2012-0158 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2014-6352 | CVE-2014-6352 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2017-8759 | CVE-2017-8759 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 中国 | Primary geographic target in the reviewed public reporting. | 不明 | 不明 | 中 | `source--cfr-taiwan-offensive-cyber-2022`, `source--target-audit-misp-360net` |
| sectors | Aviation | Public reporting identifies Aviation entities as targets. | 不明 | 不明 | 中 | `source--cfr-taiwan-offensive-cyber-2022` |
| sectors | Defense | Public reporting identifies Defense entities as targets. | 不明 | 不明 | 中 | `source--cfr-taiwan-offensive-cyber-2022` |
| sectors | Education and Research | Public reporting identifies Education and Research entities as targets. | 不明 | 不明 | 中 | `source--cfr-taiwan-offensive-cyber-2022` |
| sectors | Government | Public reporting identifies Government entities as targets. | 不明 | 不明 | 中 | `source--cfr-taiwan-offensive-cyber-2022` |
| sectors | Maritime | Public reporting identifies Maritime entities as targets. | 不明 | 不明 | 中 | `source--cfr-taiwan-offensive-cyber-2022` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: Entities holding Chinese government, defense, aviation, maritime, and cross-Strait policy information. 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 21件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| The previous China attribution was a worksheet-placement artifact; available OSINT instead associates APT-C-01 with Taiwan. | 中 | `source--cfr-taiwan-offensive-cyber-2022`, `source--apt-c-01--c225ad868f45dc7c` | Counterevidence review: no independent source supporting a China-sponsored APT-C-01 cluster was found in the fixed datasets. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- Structured OSINT country metadata is disjoint from the profile attribution; see osint-crosscheck.json and retain both assessments pending original-source review.
- Taiwan/ICEF command claims rely substantially on sources from the PRC; treat sponsor and unit-level attribution as estimative.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--apt-c-01--e7134b90ef5bd50d | apt c 01 |  | 不明 | actor_profile/evidence/apt-c-01.csv | structured-data | TLP:CLEAR | 中 |
| source--apt-c-01--c225ad868f45dc7c | Investigation report on Cyberattacks launched by Taiwan ICEFCOM EN |  | 不明 | International Strategic/China/Investigation_report_on_Cyberattacks_launched_by_Taiwan_ICEFCOM_EN.pdf | report | TLP:CLEAR | 中 |
| source--apt-c-01--b9413df3529b75d2 | Global APT Research Report for the first half of 2021 360 |  | 2021 | summary/2021/Global APT Research Report for the first half of 2021-360.pdf | report | TLP:CLEAR | 中 |
| source--apt-c-01--106890deb6d765ca | 2022 APT TRENDS INSIGHT REPORT |  | 2022 | summary/2023/2022_APT_TRENDS_INSIGHT_REPORT.pdf | report | TLP:CLEAR | 中 |
| source--apt-c-01--904d9ee36707433a | 2024 Global APT Research Report |  | 2024 | summary/2025/2024 Global APT Research Report.pdf | report | TLP:CLEAR | 中 |
| source--apt-c-01--dae8f0ec7a5b43c3 | 2025 Global APT Threat Research Report |  | 2025 | summary/2026/2025 Global APT Threat Research Report.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--cfr-taiwan-offensive-cyber-2022 | Taiwan's Offensive Cyber Capabilities and Ramifications for a Taiwan-China Conflict | Council on Foreign Relations | 2022-12-07 | https://www.cfr.org/articles/taiwans-offensive-cyber-capabilities-and-ramifications-taiwan-china-conflict | policy-research | TLP:CLEAR | 高 |
| source--target-audit-misp-360net | MISP 360.net suspected-victim fields | MISP Project / 360.net | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
