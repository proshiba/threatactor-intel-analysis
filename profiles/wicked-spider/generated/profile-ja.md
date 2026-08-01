# Wicked Spider 脅威アクタープロファイル

- プロファイルID: `actor--wicked-spider`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Wicked Spiderの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Wicked Spider**
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
| etda-threat-group-cards | Wicked Spider, APT 22 | canonical-name | 高 | China | https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-july-wicked-spider/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Wicked+Spider%2C+APT+22&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT41 | canonical-name | 高 | CN, People's Republic of China | https://securelist.com/winnti-faq-more-than-just-a-game/57585/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>http://williamshowalter.com/a-universal-windows-bootkit/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| APT17 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イタリア | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてイタリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | インド | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | インドネシア | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | シンガポール | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてシンガポールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | スイス | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてスイスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | スウェーデン | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてスウェーデンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | トルコ | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ミャンマー | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてミャンマーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ロシア | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 南アフリカ | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国として南アフリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 日本 | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 米国 | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 香港 | 構造化OSINTの被害国フィールドでWicked Spiderの標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 東アジア | 中国、日本、韓国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | インドネシア、シンガポール、タイ、ミャンマーで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | イタリア、オランダ、スイス、スウェーデン、トルコ、ドイツ、フランス、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 29件（`artifacts.csv`）

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
| source--wicked-spider--100f43f24ba349bf | wicked spider |  | 不明 | actor_profile/evidence/wicked-spider.csv | structured-data | TLP:CLEAR | 中 |
| source--wicked-spider--4ab5430714c1b798 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--wicked-spider--73781b4b55fd0606 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--wicked-spider--c228fce0b8132dff | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--wicked-spider--9eecdf768d20a919 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--wicked-spider--fcd7f9c5a7118f81 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--wicked-spider--b4c0ef6de7aa2a0d | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--wicked-spider--f9162c09c47fe17a | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
