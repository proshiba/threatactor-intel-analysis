# Aoqin Dragon 脅威アクタープロファイル

- プロファイルID: `actor--aoqin-dragon`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Aoqin Dragonの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Aoqin Dragon**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

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
| Adversary | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) is a suspected Chinese cyber espionage threat group that has been active since at least 2013. [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has primarily targeted government, education, and telecommunication organizations in Australia, Cambodia, Hong Kong, Singapore, and Vietnam. Security researchers noted a potential association between [Aoqin Dragon](https://attack.mitre.org/groups/G1007) and UNC94, based on malware, infrastructure, and targets.(Citation: SentinelOne Aoqin Dragon June 2022) |
| Capability | Mongall, Heyoka Backdoor |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Aoqin Dragon | canonical-name | 高 | China | https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Aoqin+Dragon&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Aoqin Dragon | canonical-name | 高 | CN | https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/<br>https://khonggianmang.vn/uploads/CB_941_Canhbao_APT_36c5a857fa.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Aoqin Dragon - G1007 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1007<br>https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/ |
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
| malware--mongall | Mongall | [Mongall](https://attack.mitre.org/software/S1026) is a backdoor that has been used since at least 2013, including by [Aoqin Dragon](https://attack.mitre.org/groups/G1007).(Citation: SentinelOne Aoqin Dragon June 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--heyoka-backdoor | Heyoka Backdoor | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) is a custom backdoor--based on the Heyoka open source exfiltration tool--that  has been used by [Aoqin Dragon](https://attack.mitre.org/groups/G1007) since at least 2013.(Citation: SentinelOne Aoqin Dragon June 2022)(Citation: Sourceforge Heyoka 2022)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.002 | Software Packing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | ugh Removable Media (T1091) • Dynamic-link Library Injection (T1055.001) • Application Layer Protocol: Web Protocols (T1071.001) • System Owner/User Discovery (T1033) • System Information Discovery (T1082) Aoqin Dragon – APT группа, действующая с 2012 года против государ - ственных, образовательных и телекоммуникационных организаций в Юго-Восточной Азии и Австралии. Для первоначального доступа группа использует эксплойты и поддельны |  |  | 不明 | 不明 | 中 | `source--aoqin-dragon--66a71cac9ab63fe1` |
| Stealth | T1036 | Masquerading | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | марта 2021 года. Aoqin Dragon Регион Начало операции TOP Mitre АТР Январь 2012 • Replication Through Removable Media (T1091) • Dynamic-link Library Injection (T1055.001) • Application Layer Protocol: Web Protocols (T1071.001) • System Owner/User Dis |  |  | 不明 | 不明 | 中 | `source--aoqin-dragon--66a71cac9ab63fe1` |
| Command And Control | T1071.001 | Web Protocols | P Mitre АТР Январь 2012 • Replication Through Removable Media (T1091) • Dynamic-link Library Injection (T1055.001) • Application Layer Protocol: Web Protocols (T1071.001) • System Owner/User Dis |  |  | 不明 | 不明 | 中 | `source--aoqin-dragon--66a71cac9ab63fe1` |
| Discovery | T1082 | System Information Discovery | ink Library Injection (T1055.001) • Application Layer Protocol: Web Protocols (T1071.001) • System Owner/User Discovery (T1033) • System Information Discovery (T1082) Aoqin Dragon – APT группа, действующая с 2012 года против государ - ственных, образовательных и телекоммуникационных организаций в Юго-Восточной Азии и Австралии. Для первоначального доступа группа использует эксплойты и поддельны |  |  | 不明 | 不明 | 中 | `source--aoqin-dragon--66a71cac9ab63fe1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Lateral Movement | T1091 | Replication Through Removable Media | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--aoqin-dragon--66a71cac9ab63fe1`, `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
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
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--aoqin-dragon--66a71cac9ab63fe1 | aoqin dragon |  | 不明 | actor_profile/evidence/aoqin-dragon.csv | structured-data | TLP:CLEAR | 中 |
| source--aoqin-dragon--22dd69fd38e41d90 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
