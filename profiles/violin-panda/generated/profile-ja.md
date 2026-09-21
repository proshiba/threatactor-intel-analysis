# Violin Panda 脅威アクタープロファイル

- プロファイルID: `actor--violin-panda`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Violin Pandaの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Violin Panda**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT20 | catalog / Google Threat Intelligence Group | exact | 高 | `source--gtig-unified-actor-naming-2026` | Alias scope must be reviewed before publication. GTIG's July 2026 table explicitly maps the previous name to this new unified name. Exactness is within GTIG's taxonomy; other vendors may use different collection boundaries. |
| RIDGE CASTLE | Google Threat Intelligence Group | exact | 高 | `source--gtig-unified-actor-naming-2026` | GTIG's July 2026 table explicitly maps the previous name to this new unified name. Exactness is within GTIG's taxonomy; other vendors may use different collection boundaries. |

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
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | RIDGE CASTLE | multiple-name-intersection | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system |
| etda-threat-group-cards | APT 20, Violin Panda | canonical-name | 高 | China | https://unit42.paloaltonetworks.com/recent-watering-hole-attacks-attributed-apt-group-th3bug-using-poison-ivy/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=APT+20%2C+Violin+Panda&n=1 |
| etda-threat-group-cards | Nitro, Covert Grove | single-alias-intersection | 中 | China | https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the_nitro_attacks.pdf<br>https://blog.trendmicro.com/trendlabs-security-intelligence/the-significance-of-the-nitro-attacks/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Nitro%2C+Covert+Grove&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Nitro | single-alias-intersection | 中 | CN | https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2011/the_nitro_attacks.pdf<br>https://unit42.paloaltonetworks.com/new-indicators-compromise-apt-group-nitro-uncovered/<br>https://blog.trendmicro.com/trendlabs-security-intelligence/the-significance-of-the-nitro-attacks/ |
| misp-threat-actor | APT20 | canonical-name | 高 | CN | http://researchcenter.paloaltonetworks.com/2014/09/recent-watering-hole-attacks-attributed-apt-group-th3bug-using-poison-ivy/<br>https://www.fox-it.com/nl/actueel/whitepapers/operation-wocao-shining-a-light-on-one-of-chinas-hidden-hacking-groups/<br>https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2015/Aug.10.The_Italian_Connection_An_analysis_of_exploit_supply_chains_and_digital_quartermasters/HTExploitTelemetry.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | APT20 | single-alias-intersection | 中 | CN |  |

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

th3bug; Wocao

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

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- 2 alias lead(s) remain non-canonical pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--violin-panda--f4e44c4436ec2716 | violin panda |  | 不明 | actor_profile/evidence/violin-panda.csv | structured-data | TLP:CLEAR | 中 |
| source--violin-panda--96b5dd05c9f114db | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--violin-panda--229038b84d91e3a9 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--violin-panda--428e7cc5f0547025 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--violin-panda--6253671558dc6d82 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--violin-panda--f653732df5fd3477 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--gtig-unified-actor-naming-2026 | Updated Cyber Threat Actor Naming System | Google Threat Intelligence Group | 2026-07-24 | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-gtig-threat-actor-naming | Google Threat Intelligence Group Unified Threat Actor Naming | Google Threat Intelligence Group | 不明 | actor_profile/reference/osint/gtig-threat-actor-naming.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
