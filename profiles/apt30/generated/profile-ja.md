# APT30 脅威アクタープロファイル

- プロファイルID: `actor--apt30`
- 状態: draft
- 更新日時: 2026-09-21T04:18:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

APT30の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT30**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| ISTHMUS CASTLE | Google Threat Intelligence Group | exact | 高 | `source--gtig-unified-actor-naming-2026` | GTIG's July 2026 table explicitly maps the previous name to this new unified name. Exactness is within GTIG's taxonomy; other vendors may use different collection boundaries. |

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
| Lotus Blossom | overlaps-with | 共有alias: APT30 | 低 | `source--mitre-attack-19-1` |
| Naikon | related-to | While [Naikon](https://attack.mitre.org/groups/G0019) shares some characteristics with [APT30](https://attack.mitre.org/groups/G0013), the two groups do not appear to be exact matches.(Citation: Baumgartner Golovkin Naikon 2015) | 中 | `source--mitre-attack-19-2` |

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
| gtig-threat-actor-naming | ISTHMUS CASTLE | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system |
| etda-threat-group-cards | APT 30, Override Panda | canonical-name | 高 | China | https://www2.fireeye.com/rs/fireye/images/rpt-apt30.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=APT+30%2C+Override+Panda&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Raspberry Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT30 | canonical-name | 高 | CN, China | https://attack.mitre.org/wiki/Group/G0013<br>https://www2.fireeye.com/rs/fireye/images/rpt-apt30.pdf<br>https://www.mandiant.com/resources/insights/apt-groups |
| misp-microsoft-activity-group | Raspberry Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | APT30 - G0013 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0013<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf<br>https://securelist.com/the-naikon-apt/69953/ |
| misp-mitre-intrusion-set | APT30 - G0013 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0013<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf<br>https://securelist.com/the-naikon-apt/69953/ |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | APT30 | canonical-name | 高 | CN |  |

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
| malware--backspace | BACKSPACE | [BACKSPACE](https://attack.mitre.org/software/S0031) is a backdoor used by [APT30](https://attack.mitre.org/groups/G0013) that dates back to at least 2005. (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--flashflood | FLASHFLOOD | [FLASHFLOOD](https://attack.mitre.org/software/S0036) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--neteagle | NETEAGLE | [NETEAGLE](https://attack.mitre.org/software/S0034) is a backdoor developed by [APT30](https://attack.mitre.org/groups/G0013) with compile dates as early as 2008. It has two main variants known as “Scout” and “Norton.” (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--shipshape | SHIPSHAPE | [SHIPSHAPE](https://attack.mitre.org/software/S0028) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--spaceship | SPACESHIP | [SPACESHIP](https://attack.mitre.org/software/S0035) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

Naikon; Camera Shy

## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1204.002 | Malicious File | [APT30](https://attack.mitre.org/groups/G0013) has relied on users to execute malicious file attachments delivered via spearphishing emails.(Citation: FireEye APT30) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [APT30](https://attack.mitre.org/groups/G0013) has used spearphishing emails with malicious DOC attachments.(Citation: FireEye APT30) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| source--apt30--9bcc0faced92a447 | apt30 |  | 不明 | actor_profile/evidence/apt30.csv | structured-data | TLP:CLEAR | 中 |
| source--apt30--6c5b516851ad6e68 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--apt30--6ccf04c1b58ce289 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--apt30--97d79850a7bcfa8d | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--apt30--b210ae7aaf706f3e | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--apt30--ef695be437ddd5dc | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--gtig-unified-actor-naming-2026 | Updated Cyber Threat Actor Naming System | Google Threat Intelligence Group | 2026-07-24 | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-gtig-threat-actor-naming | Google Threat Intelligence Group Unified Threat Actor Naming | Google Threat Intelligence Group | 不明 | actor_profile/reference/osint/gtig-threat-actor-naming.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
