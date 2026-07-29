# Axiom 脅威アクタープロファイル

- プロファイルID: `actor--axiom`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Axiomの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Axiom**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT17 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Deputy Dog (iDefense) | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Dogfish (iDefense) | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Group 72 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Tailgater Team | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Winnti Umbrella | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Dogfish (iDefense), Deputy Dog (iDefense), Winnti Umbrella | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 10; mapping requires review. |
| Shell Crew, Hidden Lynx, Axiom | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 10; mapping requires review. |

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
| APT17 | overlaps-with | 共有alias: APT17, Tailgater Team | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| BARIUM | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Ke3chang | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| LEAD | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| PassCV | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Winnti Group | overlaps-with | Some reporting suggests a degree of overlap between [Axiom](https://attack.mitre.org/groups/G0001) and [Winnti Group](https://attack.mitre.org/groups/G0044) but the two groups appear to be distinct based on differences in reporting on TTPs and targeting.(Citation: Kaspersky Winnti April 2013)(Citation: Kaspersky Winnti June 2015)(Citation: Novetta Winnti April 2015) | 高 | `source--mitre-attack-19-1` |
| Winnti Group | related-to | The group has heavily targeted the gaming industry, but it has also expanded the scope of its targeting.(Citation: Kaspersky Winnti April 2013)(Citation: Kaspersky Winnti June 2015)(Citation: Novetta Winnti April 2015) Some reporting suggests a number of other groups, including [Axiom](https://attack.mitre.org/groups/G0001), [APT17](https://attack.mitre.org/groups/G0025), and [Ke3chang](https://attack.mitre.org/groups/G0004), are closely linked to [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: 401 TRG Winnti Umbrella May 2018) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Axiom](https://attack.mitre.org/groups/G0001) is a suspected Chinese cyber espionage group that has targeted the aerospace, defense, government, manufacturing, and media sectors since at least 2008. Some reporting suggests a degree of overlap between [Axiom](https://attack.mitre.org/groups/G0001) and [Winnti Group](https://attack.mitre.org/groups/G0044) but the two groups appear to be distinct based on differences in reporting on TTPs and targeting.(Citation: Kaspersky Winnti April 2013)(Citation: Kaspersky Winnti June 2015)(Citation: Novetta Winnti April 2015) |
| Capability | PlugX, Hydraq, gh0st RAT, Derusbi, Hikit, PoisonIvy, ZxShell, Zox, Winnti, Deputy Dog, HTRAN, HDRoot, Fscan, Timestomper |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 17, Deputy Dog, Elderwood, Sneaky Panda | multiple-name-intersection | 高 | China | http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf<br>https://intrusiontruth.wordpress.com/2019/07/24/apt17-is-run-by-the-jinan-bureau-of-the-chinese-ministry-of-state-security/<br>https://intezer.com/evidence-aurora-operation-still-active-supply-chain-attack-through-ccleaner/ |
| etda-threat-group-cards | Axiom, Group 72 | canonical-name | 高 | China | https://blogs.cisco.com/security/talos/threat-spotlight-group-72<br>http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Axiom%2C+Group+72&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Heart Typhoon | single-alias-intersection | 中 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT17 | canonical-name | 高 | CN, China | https://web.archive.org/web/20130924130243/https://www.fireeye.com/blog/technical/cyber-exploits/2013/09/operation-deputydog-zero-day-cve-2013-3893-attack-against-japanese-targets.html<br>https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2013/hidden_lynx.pdf<br>https://www.cfr.org/interactive/cyber-operations/apt-17 |
| misp-microsoft-activity-group | Heart Typhoon | single-alias-intersection | 中 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | APT17 - G0025 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0025<br>https://www2.fireeye.com/rs/fireye/images/APT17%20Report.pdf |
| misp-mitre-enterprise-intrusion-set | Axiom - G0001 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0001<br>http://www.novetta.com/wp-content/uploads/2014/11/Executive%20Summary-Final%201.pdf<br>https://kasperskycontenthub.com/wp-content/uploads/sites/43/vlpdfs/winnti-more-than-just-a-game-130410.pdf |
| misp-mitre-intrusion-set | Axiom - G0001 | mitre-external-id | 高 |  | http://blogs.cisco.com/security/talos/threat-spotlight-group-72<br>https://attack.mitre.org/groups/G0001<br>https://securelist.com/games-are-over/70991/ |
| misp-mitre-intrusion-set | APT17 - G0025 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0025<br>https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| APT17 | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Axiom | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Winnti Group | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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
| malware--hydraq | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) is a data-theft trojan first used by [Elderwood](https://attack.mitre.org/groups/G0066) in the 2009 Google intrusion known as Operation Aurora, though variations of this trojan have been used in more recent campaigns by other Chinese actors, possibly including [APT17](https://attack.mitre.org/groups/G0025).(Citation: MicroFocus 9002 Aug 2016)(Citation: Symantec Elderwood Sept 2012)(Citation: Symantec Trojan.Hydraq Jan 2010)(Citation: ASERT Seven Pointed Dagger Aug 2015)(Citation: FireEye DeputyDog 9002 November 2013)(Citation: ProofPoint GoT 9002 Aug 2017)(Citation: FireEye Sunshop Campaign May 2013)(Citation: PaloAlto 3102 Sept 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--gh0st-rat | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) is a remote access tool (RAT). The source code is public and it has been used by multiple groups.(Citation: FireEye Hacking Team)(Citation: Arbor Musical Chairs Feb 2018)(Citation: Nccgroup Gh0st April 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--derusbi | Derusbi | [Derusbi](https://attack.mitre.org/software/S0021) is malware used by multiple Chinese APT groups.(Citation: Novetta-Axiom)(Citation: ThreatConnect Anthem) Both Windows and Linux variants have been observed.(Citation: Fidelis Turbo) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hikit | Hikit | [Hikit](https://attack.mitre.org/software/S0009) is malware that has been used by [Axiom](https://attack.mitre.org/groups/G0001) for late-stage persistence and exfiltration after the initial compromise.(Citation: Novetta-Axiom)(Citation: FireEye Hikit Rootkit) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--poisonivy | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) is a popular remote access tool (RAT) that has been used by many groups.(Citation: FireEye Poison Ivy)(Citation: Symantec Elderwood Sept 2012)(Citation: Symantec Darkmoon Aug 2005) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--zxshell | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) is a remote administration tool and backdoor that can be downloaded from the Internet, particularly from Chinese hacker websites. It has been used since at least 2004.(Citation: FireEye APT41 Aug 2019)(Citation: Talos ZxShell Oct 2014) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--zox | Zox | [Zox](https://attack.mitre.org/software/S0672) is a remote access tool that has been used by [Axiom](https://attack.mitre.org/groups/G0001) since at least 2008.(Citation: Novetta-Axiom) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--winnti | Winnti | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--deputy-dog | Deputy Dog | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--htran | HTRAN | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--hdroot | HDRoot | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--fscan | Fscan | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--timestomper | Timestomper | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| Command And Control | T1001.002 | Steganography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003 | OS Credential Dumping | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.008 | Accessibility Features | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553 | Subvert Trust Controls | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560 | Archive Collected Data | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1563.002 | RDP Hijacking | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.002 | DNS Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.005 | Botnet | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 32件（`artifacts.csv`）

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
| source--axiom--e6264323a3558dd2 | axiom |  | 不明 | actor_profile/evidence/axiom.csv | structured-data | TLP:CLEAR | 中 |
| source--axiom--be46fc37a4c4d854 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--axiom--4186879d0e241269 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--axiom--7fb9c0881e91d7f1 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--axiom--a653bee3db2bd037 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--axiom--f8b9358ec74913b3 | APT blackberry mobile malware report |  | 不明 | summary/2020/APT-blackberry-mobile-malware-report.pdf | report | TLP:CLEAR | 中 |
| source--axiom--9c11de249938c892 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--axiom--47828acad64d2ee2 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
