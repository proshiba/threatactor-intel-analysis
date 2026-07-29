# RedFoxtrot 脅威アクタープロファイル

- プロファイルID: `actor--redfoxtrot`
- 状態: draft
- 更新日時: 2026-07-29T15:36:11Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

RedFoxtrotの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **RedFoxtrot**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| ?Moshen Dragon, Nomad Panda, Goblin Panda, LuckyMouse, Cycldek, Emissary Panda, TG-3390 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 106; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

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
| Capability | PlugX-Talisman, ShadowPad, GUNTERS |
| Infrastructure |  |
| Victim | South Asia Telecom & Defense |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | RedFoxtrot | canonical-name | 高 | China | https://www.recordedfuture.com/redfoxtrot-china-pla-targets-bordering-asian-countries/<br>https://go.recordedfuture.com/redfoxtrot-insikt-report<br>https://www.sentinelone.com/labs/moshen-dragons-triad-and-error-approach-abusing-security-software-to-sideload-plugx-and-shadowpad/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | DAGGER PANDA | canonical-name | 高 | CN, China | https://securelist.com/the-icefog-apt-a-tale-of-cloak-and-three-daggers/57331/<br>https://securelist.com/the-icefog-apt-hits-us-targets-with-java-backdoor/58209/<br>https://www.cfr.org/interactive/cyber-operations/icefog |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--plugx-talisman | PlugX-Talisman | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--shadowpad | ShadowPad | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--gunters | GUNTERS | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Privilege Escalation, Stealth | T1055 | Process Injection | roka Регион Начало операции TOP Mitre АТР, Америка Декабрь 2020 • Supply Chain Compromise (T1195) • Virtualization/Sandbox Evasion (T1497) • Process Injection (T1055) • Credentials from Passwo |  |  | 不明 | 不明 | 中 | `source--redfoxtrot--8c328368bf518208` |
| Initial Access | T1195 | Supply Chain Compromise | с груп - пировками, такими как RedFoxtrot и Nomad Panda. Earth Berberoka Регион Начало операции TOP Mitre АТР, Америка Декабрь 2020 • Supply Chain Compromise (T1195) • Virtualization/Sandbox Evasion (T1497) • Process Injection (T1055) • Credentials from Passwo |  |  | 不明 | 不明 | 中 | `source--redfoxtrot--8c328368bf518208` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | t и Nomad Panda. Earth Berberoka Регион Начало операции TOP Mitre АТР, Америка Декабрь 2020 • Supply Chain Compromise (T1195) • Virtualization/Sandbox Evasion (T1497) • Process Injection (T1055) • Credentials from Passwo |  |  | 不明 | 不明 | 中 | `source--redfoxtrot--8c328368bf518208` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 20件（`artifacts.csv`）

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
| source--redfoxtrot--8c328368bf518208 | redfoxtrot |  | 不明 | actor_profile/evidence/redfoxtrot.csv | structured-data | TLP:CLEAR | 中 |
| source--redfoxtrot--edbb6a08d7b2a77f | RedFoxtrot group |  | 不明 | International Strategic/China/RedFoxtrot_group.pdf | report | TLP:CLEAR | 中 |
| source--redfoxtrot--924e8dca2e9805d9 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--redfoxtrot--7e11e3dd24324091 | 2022 Adversary Infrastructure Report |  | 2022 | summary/2022/2022 Adversary Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--redfoxtrot--597a5d6c6b13ea07 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--redfoxtrot--1e24571a3d786be5 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--redfoxtrot--7b38394cdb70e627 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
