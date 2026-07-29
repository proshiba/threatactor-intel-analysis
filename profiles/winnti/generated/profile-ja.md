# Winnti Group 脅威アクタープロファイル

- プロファイルID: `actor--winnti`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Winnti Groupの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Winnti Group**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Blackfly | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Wicked Panda | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |
| BRONZE ATLAS | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |
| APT41 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |
| Winnti Umbrella, BARIUM, LEAD, RedEcho, Vanadinite, TAG-22 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |
| Deep Panda, Wicked Spider | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |

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

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| APT41 | overlaps-with | MITRE states that APT41 overlaps at least partially with public reporting on Winnti Group. | 高 | `source--mitre-live-apt41-2025` |
| Axiom | overlaps-with | Some reporting suggests a degree of overlap between [Axiom](https://attack.mitre.org/groups/G0001) and [Winnti Group](https://attack.mitre.org/groups/G0044) but the two groups appear to be distinct based on differences in reporting on TTPs and targeting.(Citation: Kaspersky Winnti April 2013)(Citation: Kaspersky Winnti June 2015)(Citation: Novetta Winnti April 2015) | 高 | `source--mitre-attack-19-1` |
| Axiom | related-to | The group has heavily targeted the gaming industry, but it has also expanded the scope of its targeting.(Citation: Kaspersky Winnti April 2013)(Citation: Kaspersky Winnti June 2015)(Citation: Novetta Winnti April 2015) Some reporting suggests a number of other groups, including [Axiom](https://attack.mitre.org/groups/G0001), [APT17](https://attack.mitre.org/groups/G0025), and [Ke3chang](https://attack.mitre.org/groups/G0004), are closely linked to [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: 401 TRG Winnti Umbrella May 2018) | 中 | `source--mitre-attack-19-1` |
| APT17 | related-to | The group has heavily targeted the gaming industry, but it has also expanded the scope of its targeting.(Citation: Kaspersky Winnti April 2013)(Citation: Kaspersky Winnti June 2015)(Citation: Novetta Winnti April 2015) Some reporting suggests a number of other groups, including [Axiom](https://attack.mitre.org/groups/G0001), [APT17](https://attack.mitre.org/groups/G0025), and [Ke3chang](https://attack.mitre.org/groups/G0004), are closely linked to [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: 401 TRG Winnti Umbrella May 2018) | 中 | `source--mitre-attack-19-1` |
| Ke3chang | related-to | The group has heavily targeted the gaming industry, but it has also expanded the scope of its targeting.(Citation: Kaspersky Winnti April 2013)(Citation: Kaspersky Winnti June 2015)(Citation: Novetta Winnti April 2015) Some reporting suggests a number of other groups, including [Axiom](https://attack.mitre.org/groups/G0001), [APT17](https://attack.mitre.org/groups/G0025), and [Ke3chang](https://attack.mitre.org/groups/G0004), are closely linked to [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: 401 TRG Winnti Umbrella May 2018) | 中 | `source--mitre-attack-19-1` |
| Earth Lusca | related-to | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used malware commonly used by other Chinese threat groups, including [APT41](https://attack.mitre.org/groups/G0096) and the [Winnti Group](https://attack.mitre.org/groups/G0044) cluster, however security researchers assess [Earth Lusca](https://attack.mitre.org/groups/G1006)'s techniques and infrastructure are separate.(Citation: TrendMicro EarthLusca 2022) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Winnti Group](https://attack.mitre.org/groups/G0044) is a threat group with Chinese origins that has been active since at least 2010. The group has heavily targeted the gaming industry, but it has also expanded the scope of its targeting.(Citation: Kaspersky Winnti April 2013)(Citation: Kaspersky Winnti June 2015)(Citation: Novetta Winnti April 2015) Some reporting suggests a number of other groups, including [Axiom](https://attack.mitre.org/groups/G0001), [APT17](https://attack.mitre.org/groups/G0025), and [Ke3chang](https://attack.mitre.org/groups/G0004), are closely linked to [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: 401 TRG Winnti Umbrella May 2018) |
| Capability | PlugX, PipeMon, Winnti for Windows, Winnti, AceHash, Webshells, ZxShell, ShadowPad |
| Infrastructure |  |
| Victim | ThyssenKrupp, Gameforge, Valve, Teamviewer,Siemens, Sumitomo, BASF, Covestro, Shin-Etsu, Bayer, Roche |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 41 | multiple-name-intersection | 高 | China | http://content.fireeye.com/apt41/rpt-apt41<br>https://arstechnica.com/information-technology/2018/05/researchers-link-a-decade-of-potent-hacks-to-chinese-intelligence-group/<br>https://www.kaspersky.com/about/press-releases/2019_operation-shadowhammer-new-supply-chain-attack |
| etda-threat-group-cards | Winnti Group, Wicked Panda | canonical-name | 高 | China | https://blog.trendmicro.com/trendlabs-security-intelligence/pigs-malware-examining-possible-member-winnti-group/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>https://401trg.com/burning-umbrella/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Brass Typhoon | multiple-name-intersection | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Leopard Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT41 | multiple-name-intersection | 高 | CN, People's Republic of China | https://securelist.com/winnti-faq-more-than-just-a-game/57585/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>http://williamshowalter.com/a-universal-windows-bootkit/ |
| misp-microsoft-activity-group | Brass Typhoon | multiple-name-intersection | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Leopard Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Winnti Group - G0044 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0044<br>https://kasperskycontenthub.com/wp-content/uploads/sites/43/vlpdfs/winnti-more-than-just-a-game-130410.pdf<br>https://securelist.com/games-are-over/70991/ |
| misp-mitre-intrusion-set | Winnti Group - G0044 | mitre-external-id | 高 |  | http://www.symantec.com/connect/blogs/suckfly-revealing-secret-life-your-code-signing-certificates<br>https://401trg.github.io/pages/burning-umbrella.html<br>https://attack.mitre.org/groups/G0044 |
| misp-mitre-intrusion-set | APT41 - G0096 | multiple-name-intersection | 高 |  | https://attack.mitre.org/groups/G0096<br>https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| APT17 | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Axiom | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| APT17 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--plugx | PlugX | [PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.(Citation: Lastline PlugX Analysis)(Citation: FireEye Clandestine Fox Part 2)(Citation: New DragonOK)(Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pipemon | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) is a multi-stage modular backdoor used by [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: ESET PipeMon May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--winnti-for-windows | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) is a modular remote access Trojan (RAT) that has been used likely by multiple groups to carry out intrusions in various regions since at least 2010, including by one group referred to as the same name, [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: Kaspersky Winnti April 2013)(Citation: Microsoft Winnti Jan 2017)(Citation: Novetta Winnti April 2015)(Citation: 401 TRG Winnti Umbrella May 2018). The Linux variant is tracked separately under [Winnti for Linux](https://attack.mitre.org/software/S0430).(Citation: Chronicle Winnti for Linux May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--winnti | Winnti | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--acehash | AceHash | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--webshells | Webshells | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--zxshell | ZxShell | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--shadowpad | ShadowPad | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| Stealth | T1014 | Rootkit | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 3件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 19件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| MITRE states that APT41 overlaps at least partially with public reporting on Winnti Group. | 高 | `source--mitre-live-apt41-2025` | verification_status=supported; Partial overlap is not exact identity and does not imply all Winnti-umbrella activity is APT41. An exact-alias assertion would be stronger than the cited source supports. |

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
| source--winnti--636389da9b57970f | README |  | 不明 | Winnti/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--winnti--d3e8a2db904a2b19 | winnti apt group docks in sri lanka for new campaign final |  | 不明 | Winnti/winnti-apt-group-docks-in-sri-lanka-for-new-campaign-final.pdf | report | TLP:CLEAR | 中 |
| source--mitre-live-apt41-2025 | APT41, Group G0096 | MITRE ATT&CK | 2025-06-11 | https://attack.mitre.org/groups/G0096/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
