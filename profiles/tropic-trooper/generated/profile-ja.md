# Tropic Trooper 脅威アクタープロファイル

- プロファイルID: `actor--tropic-trooper`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Tropic Trooperの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Tropic Trooper**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| KeyBoy | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| KeyBoys | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Pirate Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Tropic Trooper & KeyBoy | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 65; mapping requires review. |

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
| Adversary | [Tropic Trooper](https://attack.mitre.org/groups/G0081) is an unaffiliated threat group that has led targeted campaigns against targets in Taiwan, the Philippines, and Hong Kong. [Tropic Trooper](https://attack.mitre.org/groups/G0081) focuses on targeting government, healthcare, transportation, and high-tech industries and has been active since 2011.(Citation: TrendMicro Tropic Trooper Mar 2018)(Citation: Unit 42 Tropic Trooper Nov 2016)(Citation: TrendMicro Tropic Trooper May 2020) |
| Capability | KeyBoy, USBferry, PoisonIvy, YAHOYAH, ShadowPad, BITSAdmin |
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
| etda-threat-group-cards | Tropic Trooper, Pirate Panda, APT 23, KeyBoy | canonical-name | 高 | China | https://blogs.cisco.com/security/scope-of-keyboy-targeted-malware-attacks<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Tropic+Trooper%2C+Pirate+Panda%2C+APT+23%2C+KeyBoy&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT23 | canonical-name | 高 | CN | https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/<br>http://www.crowdstrike.com/blog/rhetoric-foreshadows-cyber-activity-in-the-south-china-sea/<br>https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Tropic Trooper - G0081 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0081<br>https://blog.trendmicro.com/trendlabs-security-intelligence/tropic-trooper-new-strategy/<br>https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf |
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
| malware--keyboy | KeyBoy | [KeyBoy](https://attack.mitre.org/software/S0387) is malware that has been used in targeted campaigns against members of the Tibetan Parliament in 2016.(Citation: CitizenLab KeyBoy Nov 2016)(Citation: PWC KeyBoys Feb 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--usbferry | USBferry | [USBferry](https://attack.mitre.org/software/S0452) is an information stealing malware and has been used by [Tropic Trooper](https://attack.mitre.org/groups/G0081) in targeted attacks against Taiwanese and Philippine air-gapped military environments. [USBferry](https://attack.mitre.org/software/S0452) shares an overlapping codebase with [YAHOYAH](https://attack.mitre.org/software/S0388), though it has several features which makes it a distinct piece of malware.(Citation: TrendMicro Tropic Trooper May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--poisonivy | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) is a popular remote access tool (RAT) that has been used by many groups.(Citation: FireEye Poison Ivy)(Citation: Symantec Elderwood Sept 2012)(Citation: Symantec Darkmoon Aug 2005) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--yahoyah | YAHOYAH | [YAHOYAH](https://attack.mitre.org/software/S0388) is a Trojan used by [Tropic Trooper](https://attack.mitre.org/groups/G0081) as a second-stage backdoor.(Citation: TrendMicro TropicTrooper 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--shadowpad | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) is a modular backdoor that was first identified in a supply chain compromise of the NetSarang software in mid-July 2017. The malware was originally thought to be exclusively used by [APT41](https://attack.mitre.org/groups/G0096), but has since been observed to be used by various Chinese threat activity groups. (Citation: Recorded Future RedEcho Feb 2021)(Citation: Securelist ShadowPad Aug 2017)(Citation: Kaspersky ShadowPad Aug 2017)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--bitsadmin | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| countries | インド | 構造化OSINTの被害国フィールドでTropic Trooperの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでTropic Trooperの標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでTropic Trooperの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでTropic Trooperの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでTropic Trooperの標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 香港 | 構造化OSINTの被害国フィールドでTropic Trooperの標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | チベット | 構造化OSINTの被害地域フィールドでTropic Trooperの標的範囲としてチベットが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | 構造化OSINTの被害地域フィールドでTropic Trooperの標的範囲として中東が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | 台湾、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | フィリピン、ベトナム、マレーシアで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | 政府・行政 | [Tropic Trooper](https://attack.mitre.org/groups/G0081) focuses on targeting government, healthcare, transportation, and high-tech industries and has been active since 2011.(Citation: TrendMicro Tropic Trooper Mar 2018)(Citation: Unit 42 Tropic Trooper Nov 2016)(Citation: TrendMicro Tropic Trooper May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 運輸・航空・海運 | [Tropic Trooper](https://attack.mitre.org/groups/G0081) focuses on targeting government, healthcare, transportation, and high-tech industries and has been active since 2011.(Citation: TrendMicro Tropic Trooper Mar 2018)(Citation: Unit 42 Tropic Trooper Nov 2016)(Citation: TrendMicro Tropic Trooper May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 医療・ヘルスケア | [Tropic Trooper](https://attack.mitre.org/groups/G0081) focuses on targeting government, healthcare, transportation, and high-tech industries and has been active since 2011.(Citation: TrendMicro Tropic Trooper Mar 2018)(Citation: Unit 42 Tropic Trooper Nov 2016)(Citation: TrendMicro Tropic Trooper May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1016 | System Network Configuration Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used scripts to collect the host's network topology.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1020 | Automated Exfiltration | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used a copy function to automatically exfiltrate sensitive data from air-gapped systems using USB storage.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used JPG files with encrypted payloads to mask their backdoor routines and evade detection.(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has encrypted configuration files.(Citation: TrendMicro Tropic Trooper Mar 2018)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) used <code>letmein</code> to scan for saved usernames on the target system.(Citation: TrendMicro TropicTrooper 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has hidden payloads in Flash directories and fake installer files.(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) used <code>pr</code> and an openly available tool to scan for open ports on target systems.(Citation: TrendMicro TropicTrooper 2015)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has tested if the localhost network is available and other connection capability on an infected system using command scripts.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1052.001 | Exfiltration over USB | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has exfiltrated data using USB storage devices.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has injected a DLL backdoor into dllhost.exe and svchost.exe.(Citation: TrendMicro Tropic Trooper Mar 2018)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) is capable of enumerating the running processes on the system using <code>pslist</code>.(Citation: Unit 42 Tropic Trooper Nov 2016)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used Windows command scripts.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has deleted dropper files on an infected system using command scripts.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used HTTP in communication with the C2.(Citation: Anomali Pirate Panda April 2020)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | [Tropic Trooper](https://attack.mitre.org/groups/G0081)'s backdoor has communicated to the C2 over the DNS protocol.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used known administrator account credentials to execute the backdoor directly.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has detected a target system’s OS version.(Citation: TrendMicro TropicTrooper 2015)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has monitored files' modified time.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Lateral Movement | T1091 | Replication Through Removable Media | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has attempted to transfer [USBferry](https://attack.mitre.org/software/S0452) from an infected USB device by copying an Autorun function to the target machine.(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used a delivered trojan to download additional files.(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used multiple Windows APIs including HttpInitialize, HttpCreateHttpHandle, and HttpAddUrl.(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has collected information automatically using the adversary's [USBferry](https://attack.mitre.org/software/S0452) attack.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used base64 encoding to hide command strings delivered from the C2.(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) used <code>netview</code> to scan target systems for shared resources.(Citation: TrendMicro TropicTrooper 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Tropic Trooper](https://attack.mitre.org/groups/G0081) used shellcode with an XOR algorithm to decrypt a payload. [Tropic Trooper](https://attack.mitre.org/groups/G0081) also decrypted image files which contained a payload.(Citation: Unit 42 Tropic Trooper Nov 2016)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has executed commands through Microsoft security vulnerabilities, including CVE-2017-11882, CVE-2018-0802, and CVE-2012-0158.(Citation: TrendMicro Tropic Trooper Mar 2018)(Citation: Unit 42 Tropic Trooper Nov 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has lured victims into executing malware via malicious e-mail attachments.(Citation: Anomali Pirate Panda April 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1221 | Template Injection | [Tropic Trooper](https://attack.mitre.org/groups/G0081) delivered malicious documents with the XLSX extension, typically used by OpenXML documents, but the file itself was actually an OLE (XLS) document.(Citation: Unit 42 Tropic Trooper Nov 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has started a web service in the target host and wait for the adversary to connect, acting as a web shell.(Citation: TrendMicro Tropic Trooper May 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518 | Software Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081)'s backdoor could list the infected system's installed software.(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) can search for anti-virus software running on the system.(Citation: Unit 42 Tropic Trooper Nov 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has installed a service pointing to a malicious DLL dropped to disk.(Citation: PWC KeyBoys Feb 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has created shortcuts in the Startup folder to establish persistence.(Citation: Anomali Pirate Panda April 2020)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.004 | Winlogon Helper DLL | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has created the Registry key <code>HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell</code> and sets the value to establish persistence.(Citation: Unit 42 Tropic Trooper Nov 2016)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has created a hidden directory under <code>C:\ProgramData\Apple\Updates\</code> and <code>C:\Users\Public\Documents\Flash\</code>.(Citation: TrendMicro Tropic Trooper Mar 2018)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Tropic Trooper](https://attack.mitre.org/groups/G0081) sent spearphishing emails that contained malicious Microsoft Office and fake installer file attachments.(Citation: Unit 42 Tropic Trooper Nov 2016)(Citation: TrendMicro TropicTrooper 2015)(Citation: CitizenLab Tropic Trooper Aug 2018)(Citation: Anomali Pirate Panda April 2020)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573 | Encrypted Channel | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has encrypted traffic with the C2 to prevent network detection.(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.002 | Asymmetric Cryptography | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used SSL to connect to C2 servers.(Citation: TrendMicro Tropic Trooper Mar 2018)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has been known to side-load DLLs using a valid version of a Windows Address Book and Windows Defender executable with one of their tools.(Citation: CitizenLab KeyBoy Nov 2016)(Citation: Anomali Pirate Panda April 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1680 | Local Storage Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has detected a target system’s system volume information.(Citation: TrendMicro TropicTrooper 2015)(Citation: TrendMicro Tropic Trooper May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 42件（`artifacts.csv`）

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
| source--tropic-trooper--469c4e88100b33a7 | tropic trooper |  | 不明 | actor_profile/evidence/tropic-trooper.csv | structured-data | TLP:CLEAR | 中 |
| source--tropic-trooper--2a6d6d99143a8a50 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--39bfa8c0e49c4e89 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--71d90f6375e11222 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--19a73475b0b862a7 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--e6e81c4401e76a17 | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--f2026c227a316f12 | mpressioncss ta report 2020 5 en |  | 2020 | summary/2021/mpressioncss_ta_report_2020_5_en.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--04a6ce570ccfa602 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--24906e55871ed59b | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--da742e99d6706895 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--28b066aeac00a89f | kaspersky ics cert apt attacks on industrial organizations in h2 2022 en |  | 2022 | summary/2023/kaspersky-ics-cert-apt-attacks-on-industrial-organizations-in-h2-2022-en.pdf | report | TLP:CLEAR | 中 |
| source--tropic-trooper--911ee3902410aca7 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
