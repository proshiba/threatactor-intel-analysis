# LuminousMoth 脅威アクタープロファイル

- プロファイルID: `actor--luminousmoth`
- 状態: draft
- 更新日時: 2026-09-21T04:35:02Z
- 構造バージョン: 1.3.0

## エグゼクティブサマリー

LuminousMothの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **LuminousMoth**
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

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | Actor-specific reporting explicitly describes espionage or intelligence collection. | 高 | `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description; not inferred from country or state sponsorship. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Mustang Panda | overlaps-with | MITRE ATT&CK 19.2 tracks Mustang Panda (G0129) and LuminousMoth (G1014) separately and describes their connection as based on targeting, TTP, and infrastructure overlap. | 高 | `source--mitre-attack-19-2` |

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
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | LuminousMoth | canonical-name | 高 | China | https://securelist.com/apt-luminousmoth/103332/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=LuminousMoth&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Twill Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | MUSTANG PANDA | canonical-name | 高 | CN, China | https://www.cfr.org/interactive/cyber-operations/mustang-panda<br>https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/<br>https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf |
| misp-microsoft-activity-group | Twill Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Mustang Panda - G0129 | canonical-name | 高 |  | https://attack.mitre.org/groups/G0129<br>https://blog.cloudflare.com/2026-threat-report/<br>https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware |
| misp-mitre-enterprise-intrusion-set | LuminousMoth - G1014 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1014<br>https://securelist.com/apt-luminousmoth/103332/<br>https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited |
| misp-mitre-intrusion-set | Mustang Panda - G0129 | canonical-name | 高 |  | https://attack.mitre.org/groups/G0129<br>https://blog.cloudflare.com/2026-threat-report/<br>https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware |
| misp-mitre-intrusion-set | LuminousMoth - G1014 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1014<br>https://securelist.com/apt-luminousmoth/103332/<br>https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | LuminousMoth | canonical-name | 高 |  |  |

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
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--plugx | PlugX | [PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.(Citation: Lastline PlugX Analysis)(Citation: FireEye Clandestine Fox Part 2)(Citation: New DragonOK)(Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| countries | タイ | MITRE ATT&CKのGroup概要でLuminousMothの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| countries | フィリピン | MITRE ATT&CKのGroup概要でLuminousMothの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| countries | ミャンマー | MITRE ATT&CKのGroup概要でLuminousMothの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| regions | 東南アジア | MITRE ATT&CKのGroup概要でLuminousMothの標的範囲として東南アジアが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | 政府・行政 | [LuminousMoth](https://attack.mitre.org/groups/G1014) has targeted high-profile organizations, including government entities, in Myanmar, the Philippines, Thailand, and other parts of Southeast Asia. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | [LuminousMoth](https://attack.mitre.org/groups/G1014) has collected files and data from compromised machines.(Citation: Kaspersky LuminousMoth July 2021)(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Exfiltration | T1030 | Data Transfer Size Limits | [LuminousMoth](https://attack.mitre.org/groups/G1014) has split archived files into multiple parts to bypass a 5MB limit.(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1033 | System Owner/User Discovery | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used a malicious DLL to collect the username from compromised hosts.(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [LuminousMoth](https://attack.mitre.org/groups/G1014) has disguised their exfiltration malware as `ZoomVideoApp.exe`.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used malware that exfiltrates stolen data to its C2 server.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [LuminousMoth](https://attack.mitre.org/groups/G1014) has created scheduled tasks to establish persistence for their tools.(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1071.001 | Web Protocols | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used HTTP for C2.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1083 | File and Directory Discovery | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used malware that scans for files in the Documents, Desktop, and Download folders and in other drives.(Citation: Kaspersky LuminousMoth July 2021)(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Lateral Movement | T1091 | Replication Through Removable Media | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used malicious DLLs to spread malware to connected removable USB drives on infected machines.(Citation: Kaspersky LuminousMoth July 2021)(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [LuminousMoth](https://attack.mitre.org/groups/G1014) has downloaded additional malware and tools onto a compromised host.(Citation: Kaspersky LuminousMoth July 2021)(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used malware that adds Registry keys for persistence.(Citation: Kaspersky LuminousMoth July 2021)(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.001 | Malicious Link | [LuminousMoth](https://attack.mitre.org/groups/G1014) has lured victims into clicking malicious Dropbox download links delivered through spearphishing.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1539 | Steal Web Session Cookie | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used an unnamed post-exploitation tool to steal cookies from the Chrome browser.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used malicious DLLs that setup persistence in the Registry Key `HKCU\Software\Microsoft\Windows\Current Version\Run`.(Citation: Kaspersky LuminousMoth July 2021)(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1553.002 | Code Signing | [LuminousMoth](https://attack.mitre.org/groups/G1014) has signed their malware with a valid digital signature.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Collection, Credential Access | T1557.002 | ARP Cache Poisoning | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used ARP spoofing to redirect a compromised machine to an actor-controlled website.(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Collection | T1560 | Archive Collected Data | [LuminousMoth](https://attack.mitre.org/groups/G1014) has manually archived stolen files from victim machines before exfiltration.(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1564.001 | Hidden Files and Directories | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used malware to store malicious binaries in hidden directories on victim's USB drives.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.002 | Spearphishing Link | [LuminousMoth](https://attack.mitre.org/groups/G1014) has sent spearphishing emails containing a malicious Dropbox download link.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [LuminousMoth](https://attack.mitre.org/groups/G1014) has exfiltrated data to Google Drive.(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Stealth | T1574.001 | DLL | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used legitimate executables such as `winword.exe` and `igfxem.exe` to side-load their malware.(Citation: Kaspersky LuminousMoth July 2021)(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1587.001 | Malware | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used unique malware for information theft and exfiltration.(Citation: Kaspersky LuminousMoth July 2021)(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.001 | Malware | [LuminousMoth](https://attack.mitre.org/groups/G1014) has obtained and used malware such as [Cobalt Strike](https://attack.mitre.org/software/S0154).(Citation: Kaspersky LuminousMoth July 2021)(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.002 | Tool | [LuminousMoth](https://attack.mitre.org/groups/G1014) has obtained an ARP spoofing tool from GitHub.(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.004 | Digital Certificates | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used a valid digital certificate for some of their malware.(Citation: Kaspersky LuminousMoth July 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1608.001 | Upload Malware | [LuminousMoth](https://attack.mitre.org/groups/G1014) has hosted malicious payloads on Dropbox.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1608.004 | Drive-by Target | [LuminousMoth](https://attack.mitre.org/groups/G1014) has redirected compromised machines to an actor-controlled webpage through HTML injection.(Citation: Bitdefender LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1608.005 | Link Target | [LuminousMoth](https://attack.mitre.org/groups/G1014) has created a link to a Dropbox file that has been used in their spear-phishing operations.(Citation: Kaspersky LuminousMoth July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| source--luminousmoth--2fe7d99f88bd7a04 | luminousmoth |  | 不明 | actor_profile/evidence/luminousmoth.csv | structured-data | TLP:CLEAR | 中 |
| source--luminousmoth--45a9ededc1b9d1c9 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--luminousmoth--8de1cf25e69b928d | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--luminousmoth--162d0f5c09813d5e | search |  | 不明 | ui/api/v1/search.json | structured-data | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
