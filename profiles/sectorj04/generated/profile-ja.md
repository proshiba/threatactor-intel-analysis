# SectorJ04 脅威アクタープロファイル

- プロファイルID: `actor--sectorj04`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

SectorJ04の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **SectorJ04**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

The repository mapping workbook places this actor in the Russia worksheet.

- 国: Russia
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| TA505 | overlaps-with | 共有alias: SectorJ04 | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | Dridex, The Trick, Locky, Jaff, FlawedAmmyy, GraceWire    malicious software signed with valid digital signatures |
| Infrastructure |  |
| Victim |  |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | TA505, Graceful Spider, Gold Evergreen | canonical-name | 高 | Russia | https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta505-dridex-globeimposter<br>https://www.secureworks.com/research/evolution-of-the-gold-evergreen-threat-group<br>https://krebsonsecurity.com/2019/12/inside-evil-corp-a-100m-cybercrime-menace/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA505 | canonical-name | 高 | RU | https://www.bleepingcomputer.com/news/security/ta505-group-adopts-new-servhelper-backdoor-and-flawedgrace-rat/<br>https://www.proofpoint.com/sites/default/files/ta505_timeline_final4_0.png<br>https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta505-dridex-globeimposter |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| MONTY SPIDER | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--dridex | Dridex | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--the-trick | The Trick | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--locky | Locky | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--jaff | Jaff | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--flawedammyy | FlawedAmmyy | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--gracewire-malicious-software-signed-with-valid-digital-signatures | GraceWire    malicious software signed with valid digital signatures | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| countries | インド | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | カナダ | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | シンガポール | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてシンガポールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | スペイン | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてスペインが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | セルビア | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてセルビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | タイ | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | チェコ | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてチェコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | トルコ | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ハンガリー | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてハンガリーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ルーマニア | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国としてルーマニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 日本 | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 米国 | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでSectorJ04の標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 全世界 | 構造化OSINTの被害地域フィールドでSectorJ04の標的範囲として全世界が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 南欧 | スペイン、セルビアで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 東アジア | 日本、韓国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | シンガポール、タイで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 東欧 | チェコ、ハンガリー、ルーマニアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 欧州 | スペイン、セルビア、チェコ、トルコ、ドイツ、ハンガリー、ルーマニア、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 7件（`artifacts.csv`）

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
| source--sectorj04--81f6ad8cde5b75d7 | sectorj04 |  | 不明 | actor_profile/evidence/sectorj04.csv | structured-data | TLP:CLEAR | 中 |
| source--sectorj04--b41d5d8e6c385951 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--sectorj04--3efe2719f19a060b | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 不明 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
