# FIN11 脅威アクタープロファイル

- プロファイルID: `actor--fin11`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

FIN11の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **FIN11**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| RAZOR COMET | catalog / Google Threat Intelligence Group | exact | 高 | `source--gtig-unified-actor-naming-2026` | Alias scope must be reviewed before publication. GTIG's July 2026 table explicitly maps the previous name to this new unified name. Exactness is within GTIG's taxonomy; other vendors may use different collection boundaries. |

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
| TA505 | overlaps-with | FIN11 includes a subset of activity publicly called TA505, but early TA505 operations are not attributed to FIN11 and the names are not interchangeable. | 高 | `source--mandiant-fin11-ta505-boundary-2020` |

## 関連する企業・個人

関連エンティティなし

### エンティティ関係

確認された関係なし

### 法的措置

確認された法的措置なし

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
| gtig-threat-actor-naming | RAZOR COMET | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system |
| etda-threat-group-cards | FIN11 | canonical-name | 高 |  | https://www.fireeye.com/blog/threat-research/2020/10/fin11-email-campaigns-precursor-for-ransomware-data-theft.html<br>https://cybernews.com/security/cl0p-hacker-hides-in-ukraine/<br>https://therecord.media/clop-moveit-zero-day-dustin-childs-interview |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | FIN11 | canonical-name | 高 |  | https://www.fireeye.com/blog/threat-research/2019/10/shikata-ga-nai-encoder-still-going-strong.html<br>https://www.fireeye.com/blog/threat-research/2020/10/fin11-email-campaigns-precursor-for-ransomware-data-theft.html<br>https://www.brighttalk.com/webcast/7451/447347 |
| misp-microsoft-activity-group | Lace Tempest | canonical-name | 高 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | FIN11 | canonical-name | 高 |  |  |

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

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

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
- 非IOC artifact観測: 2件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- Motivation lead 'financial-gain' is not canonical; only aggregation/workbook evidence is available.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--fin11--69b1cad7b6e24a50 | fin11 |  | 不明 | actor_profile/evidence/fin11.csv | structured-data | TLP:CLEAR | 中 |
| source--fin11--ac8417991befa665 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--fin11--799a5d3137f8c543 | 20251003 |  | 2025-10-03 | parse-daily/.cache/tech-memo/daily-news/news/2025_10-12/20251003.md | repository-notes | TLP:CLEAR | 中 |
| source--fin11--93e0a54e35498e16 | 20251018 |  | 2025-10-18 | parse-daily/.cache/tech-memo/daily-news/news/2025_10-12/20251018.md | repository-notes | TLP:CLEAR | 中 |
| source--fin11--a99980d6a249d562 | review decisions |  | 不明 | parse-daily/review-decisions.json | structured-data | TLP:CLEAR | 中 |
| source--fin11--bc1eaec02147d278 | state |  | 不明 | parse-daily/state.json | structured-data | TLP:CLEAR | 中 |
| source--fin11--91b5c807a523c87a | unknown clusters |  | 不明 | parse-daily/unknown-clusters.json | structured-data | TLP:CLEAR | 中 |
| source--fin11--fa51ac602bc955d9 | rpt mtrends 2021 fireeye |  | 2021 | summary/2021/rpt-mtrends-2021-fireeye.pdf | report | TLP:CLEAR | 中 |
| source--fin11--90a784f6c7722945 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--fin11--dcc5237d82df8059 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--fin11--0fed00383b15b50f | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--fin11--ea7ca82a8d092221 | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--fin11--30a32d8dc1356552 | Year in Review of ZeroDays |  | 不明 | summary/2024/Year_in_Review_of_ZeroDays.pdf | report | TLP:CLEAR | 中 |
| source--fin11--04cf465966872372 | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--fin11--67c8cac83c0b8146 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--fin11--68bbe53dc2a98f4f | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--fin11--7f28a01b4f784d6a | search |  | 不明 | ui/api/v1/search.json | structured-data | TLP:CLEAR | 中 |
| source--gtig-unified-actor-naming-2026 | Updated Cyber Threat Actor Naming System | Google Threat Intelligence Group | 2026-07-24 | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--mandiant-fin11-ta505-boundary-2020 | FIN11: Widespread Email Campaigns as Precursor for Ransomware and Data Theft | Mandiant | 2020-10-14 | https://cloud.google.com/blog/topics/threat-intelligence/fin11-email-campaigns-precursor-for-ransomware-data-theft | vendor-threat-research | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-gtig-threat-actor-naming | Google Threat Intelligence Group Unified Threat Actor Naming | Google Threat Intelligence Group | 不明 | actor_profile/reference/osint/gtig-threat-actor-naming.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
