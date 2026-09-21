# InvisiMole 脅威アクタープロファイル

- プロファイルID: `actor--invisimole`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

InvisiMoleは少なくとも2013年から活動するサイバースパイ集団で、2019年後半から2020年に東欧の軍事・外交組織を標的化した。Gamaredonによる初期侵入後に同名のモジュール型スパイウェアを選別配布する協力関係が確認されている。

## アクター名とAlias

- 正規名: **InvisiMole**
- 初回観測: 2013
- 最終観測: 2020-06-18
- 活動状態: unknown

Aliasなし

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | ESET explicitly describes InvisiMole as a cyber-espionage group and documents extensive spying capabilities. | 高 | `source--eset-invisimole-hidden-arsenal-2020` | Motivation is source-stated, not inferred from geography. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| actor--gamaredon | cooperates-with | ESET observed Gamaredon malware establishing initial access and delivering InvisiMole to a small, selected subset of targets. ESET explicitly treats the two as distinct groups with different TTPs. | 高 | `source--eset-invisimole-hidden-arsenal-2020` |

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
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | InvisiMole | canonical-name | 高 | Russia | https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=InvisiMole&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-0593 | canonical-name | 高 | Russia | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | InvisiMole | canonical-name | 高 |  | https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/<br>https://www.welivesecurity.com/2020/06/18/digging-up-invisimole-hidden-arsenal/ |
| misp-microsoft-activity-group | Storm-0593 | canonical-name | 高 | RU, Russia | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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
| malware--invisimole | InvisiMole | 同名グループが使用するモジュール型スパイウェア。RC2CLとRC2FMのバックドア、更新版のTCP/DNSダウンローダーを含む。 | 2013 | 2020-06-18 | 高 | `source--eset-invisimole-hidden-arsenal-2020` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| InvisiMoleによる東欧の軍事・外交組織へのスパイ活動 | cyber-espionage | 2019-10 | 2020-06-18 | 2020-06-18 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d, target--targeting-audit--region--e469a12091a1d97c652a | malware--invisimole |  | victim--activity-rule--1203af6b336e894538e2 | ESETは2019年後半から2020年6月18日の報告時点まで、東欧の少数の高位組織、特に軍事部門と政府・行政に属する外交使節団を標的とする攻撃を観測した。Gamaredonが先に侵入した端末の一部へ、より選別的にInvisiMoleを配布した。 | 高 | `source--eset-invisimole-hidden-arsenal-2020` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| InvisiMoleによる東欧の軍事・外交組織へのスパイ活動 | InvisiMole | InvisiMole | 情報なし | 情報なし | 政府・行政, 防衛・軍事, 東欧 | 被害事例: InvisiMoleによる東欧の軍事・外交組織へのスパイ活動 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 東欧 | 活動「InvisiMoleによる東欧の軍事・外交組織へのスパイ活動」の記述で標的地域として東欧が明示されている。 | 2019-10 | 2020-06-18 | 中 | `source--eset-invisimole-hidden-arsenal-2020` |
| sectors | 政府・行政 | 活動「InvisiMoleによる東欧の軍事・外交組織へのスパイ活動」の記述で標的として明示された産業。 | 2019-10 | 2020-06-18 | 中 | `source--eset-invisimole-hidden-arsenal-2020` |
| sectors | 防衛・軍事 | 活動「InvisiMoleによる東欧の軍事・外交組織へのスパイ活動」の記述で標的として明示された産業。 | 2019-10 | 2020-06-18 | 中 | `source--eset-invisimole-hidden-arsenal-2020` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: InvisiMoleによる東欧の軍事・外交組織へのスパイ活動 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d | malware--invisimole |  | エンドポイント | espionage: InvisiMoleによる東欧の軍事・外交組織へのスパイ活動 | 2019-10 | 2020-06-18 | 2020-06-18 | 高 | `source--eset-invisimole-hidden-arsenal-2020` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 5件（`artifacts.csv`）

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
| source--invisimole--2ca703cea36bc56b | invisimole |  | 不明 | actor_profile/evidence/invisimole.csv | structured-data | TLP:CLEAR | 中 |
| source--invisimole--ceecccfa98060922 | cyberespionage gamaredon way |  | 不明 | Gamaredon/cyberespionage-gamaredon-way.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--200940392ffce5f1 | gamaredon in 2025 |  | 2025 | Gamaredon/gamaredon-in-2025.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--fc17a2b008911bfa | Russia’s Cyber Tactics Lessons Learned 2022 |  | 2022 | International Strategic/Russia/Russia’s Cyber Tactics Lessons Learned 2022.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--3ee228046cae3bcc | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--e57dacad4de51ff5 | ESET Threat Report Q22020 |  | 不明 | summary/2020/ESET_Threat_Report_Q22020.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--3752d5c2958c9ac4 | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--dc11ae0f2797b20d | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--d56bbca9590b59e3 | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--0b36c4ac3c7c58b2 | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--invisimole--7c31ca40d198dc5a | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--5e3d782f228e4736 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--8cfb3d5ca089aba3 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--invisimole--a7faefccf02c88c2 | RussianCyber |  | 不明 | summary/2024/RussianCyber.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--eset-invisimole-hidden-arsenal-2020 | Digging up InvisiMole's hidden arsenal | ESET Research | 2020-06-18 | https://www.welivesecurity.com/2020/06/18/digging-up-invisimole-hidden-arsenal/ | vendor-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
