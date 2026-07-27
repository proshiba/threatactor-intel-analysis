# APT30 脅威アクタープロファイル

- プロファイルID: `actor--apt30`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

APT30の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT30**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Naikon | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 13; mapping requires review. |
| Lotus Panda | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 13; mapping requires review. |
| PLA Unit 78020 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 13; mapping requires review. |
| Thrip, Billbug | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 13; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Naikon | overlaps-with | 共有alias: APT30 | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Raspberry Typhoon | overlaps-with | 共有alias: APT30 | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Naikon | related-to | While [Naikon](https://attack.mitre.org/groups/G0019) shares some characteristics with [APT30](https://attack.mitre.org/groups/G0013), the two groups do not appear to be exact matches.(Citation: Baumgartner Golovkin Naikon 2015) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [APT30](https://attack.mitre.org/groups/G0013) is a threat group suspected to be associated with the Chinese government. While [Naikon](https://attack.mitre.org/groups/G0019) shares some characteristics with [APT30](https://attack.mitre.org/groups/G0013), the two groups do not appear to be exact matches.(Citation: FireEye APT30)(Citation: Baumgartner Golovkin Naikon 2015) |
| Capability | FLASHFLOOD, NETEAGLE, SPACESHIP, SHIPSHAPE, BACKSPACE, RARSTONE, XSControl |
| Infrastructure |  |
| Victim | satellite communications operator, Telecoms, and Defense Companies, Hong Kong |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 30, Override Panda | canonical-name | 高 | China | https://www2.fireeye.com/rs/fireye/images/rpt-apt30.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=APT+30%2C+Override+Panda&n=1 |
| etda-threat-group-cards | Naikon, Lotus Panda | multiple-name-intersection | 高 | China | https://securelist.com/the-chronicles-of-the-hellsing-apt-the-empire-strikes-back/69567/<br>https://securelist.com/the-naikon-apt/69953/<br>https://exchange.xforce.ibmcloud.com/threat-group/guid:2f1962c4d7c0c994981c5bc363823c44 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Raspberry Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Naikon | multiple-name-intersection | 高 | CN, China | https://securelist.com/analysis/publications/69953/the-naikon-apt/<br>https://www.fireeye.com/blog/threat-research/2014/03/spear-phishing-the-news-cycle-apt-actors-leverage-interest-in-the-disappearance-of-malaysian-flight-mh-370.html<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf |
| misp-threat-actor | APT30 | canonical-name | 高 | CN, China | https://attack.mitre.org/wiki/Group/G0013<br>https://www2.fireeye.com/rs/fireye/images/rpt-apt30.pdf<br>https://www.mandiant.com/resources/insights/apt-groups |
| misp-threat-actor | LOTUS PANDA | single-alias-intersection | 中 | CN, China | https://securelist.com/blog/research/70726/the-spring-dragon-apt/<br>https://securelist.com/spring-dragon-updated-activity/79067/<br>https://www.cfr.org/interactive/cyber-operations/lotus-blossom |
| misp-microsoft-activity-group | Raspberry Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Naikon - G0019 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0019<br>https://securelist.com/files/2015/05/TheNaikonAPT-MsnMM1.pdf<br>http://cdn2.hubspot.net/hubfs/454298/Project%20CAMERASHY%20ThreatConnect%20Copyright%202015.pdf |
| misp-mitre-enterprise-intrusion-set | APT30 - G0013 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0013<br>https://www2.fireeye.com/rs/fireye/images/rpt-apt30.pdf<br>https://securelist.com/the-naikon-apt/69953/ |
| misp-mitre-intrusion-set | APT30 - G0013 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0013<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf<br>https://securelist.com/the-naikon-apt/69953/ |
| misp-mitre-intrusion-set | Naikon - G0019 | single-alias-intersection | 中 |  | http://cdn2.hubspot.net/hubfs/454298/Project_CAMERASHY_ThreatConnect_Copyright_2015.pdf<br>https://attack.mitre.org/groups/G0019<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| APT30 | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Naikon | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Raspberry Typhoon | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--flashflood | FLASHFLOOD | [FLASHFLOOD](https://attack.mitre.org/software/S0036) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--neteagle | NETEAGLE | [NETEAGLE](https://attack.mitre.org/software/S0034) is a backdoor developed by [APT30](https://attack.mitre.org/groups/G0013) with compile dates as early as 2008. It has two main variants known as “Scout” and “Norton.” (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--spaceship | SPACESHIP | [SPACESHIP](https://attack.mitre.org/software/S0035) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--shipshape | SHIPSHAPE | [SHIPSHAPE](https://attack.mitre.org/software/S0028) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--backspace | BACKSPACE | [BACKSPACE](https://attack.mitre.org/software/S0031) is a backdoor used by [APT30](https://attack.mitre.org/groups/G0013) that dates back to at least 2005. (Citation: FireEye APT30) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--rarstone | RARSTONE | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--xscontrol | XSControl | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| Naikon | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Camera Shy | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Naikon; Camera Shy

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Hong Kong | Targeting text mentions hong kong. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 3件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 3件
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
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
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

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
