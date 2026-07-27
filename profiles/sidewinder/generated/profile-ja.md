# Sidewinder 脅威アクタープロファイル

- プロファイルID: `actor--sidewinder`
- 状態: draft
- 更新日時: 2026-07-27T11:04:35Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Sidewinderの標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Sidewinder**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Rattlesnake | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| T-APT-04 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| India | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 52; mapping requires review. |

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
| SideCopy | related-to | [SideCopy](https://attack.mitre.org/groups/G1008)'s name comes from its infection chain that tries to mimic that of [Sidewinder](https://attack.mitre.org/groups/G0121), a suspected Indian threat group.(Citation: MalwareBytes SideCopy Dec 2021) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Sidewinder](https://attack.mitre.org/groups/G0121) is a suspected Indian threat actor group that has been active since at least 2012. They have been observed targeting government, military, and business entities throughout Asia, primarily focusing on Pakistan, China, Nepal, and Afghanistan.(Citation: ATT Sidewinder January 2021)(Citation: Securelist APT Trends April 2018)(Citation: Cyble Sidewinder September 2020) |
| Capability | SideWinder.AntiBot.Script, Koadic |
| Infrastructure |  |
| Victim | Military, Govenment, Pakistan, "South Asian countries" |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | SideWinder, Rattlesnake | canonical-name | 高 | India | https://securelist.com/apt-trends-report-q1-2018/85280/<br>https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/fireeye-sidewinder-targeted-attack.pdf<br>https://medium.com/@Sebdraven/apt-sidewinder-tricks-powershell-anti-forensics-and-execution-side-loading-5bc1a7e7c84c |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | RAZOR TIGER | canonical-name | 高 | IN, India | https://securelist.com/apt-trends-report-q1-2018/85280/<br>https://blog.trendmicro.com/trendlabs-security-intelligence/first-active-attack-exploiting-cve-2019-2215-found-on-google-play-linked-to-sidewinder-apt-group/<br>https://otx.alienvault.com/pulse/5fd10760f9afb730d37c4742/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Sidewinder - G0121 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0121<br>https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf<br>https://cybleinc.com/2020/09/26/sidewinder-apt-targets-with-futuristic-tactics-and-techniques/ |
| misp-360net | 响尾蛇 - APT-C-24 | canonical-name | 高 | india | https://apt.360.net/report/apts/92.html |

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
| malware--sidewinder-antibot-script | SideWinder.AntiBot.Script | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--koadic | Koadic | [Koadic](https://attack.mitre.org/software/S0250) is a Windows post-exploitation framework and penetration testing tool that is publicly available on GitHub. [Koadic](https://attack.mitre.org/software/S0250) has several options for staging payloads and creating implants, and performs most of its operations using Windows Script Host.(Citation: Github Koadic)(Citation: Palo Alto Sofacy 06-2018)(Citation: MalwareBytes LazyScripter Feb 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| SideWinder APT、アジア、中東、アフリカの海事、原子力、ITセクターを標的に | phishing-campaign | 不明 | 不明 | 2025-03-12 | SideWinderと呼ばれる高度な持続的脅威（APT）グループが、南アジア、東南アジア、中東、アフリカの海事および物流企業を主な標的にしている。 2024年に観測された攻撃は、バングラデシュ、カンボジア、ジブチ、エジプト、アラブ首長国連邦、ベトナムに及び、原子力発電所や原子力エネルギーインフラ、電気通信、コンサルティング、ITサービス企業、不動産代理店、ホテルも標的となっている。 攻撃手法は、スピアフィッシングメールを介して、Microsoft Officeの既知の脆弱性（CVE-2017-11882）を悪用し、最終的にStealerBotと呼ばれるマルウェアを展開する。 SideWinderは、セキュリティソフトウェアの検出を回避し、感染したシステム上での持続性を延ばすために、ツールセットを継続的に改良している。 同グループは、インドの標的を攻撃しており、以前はインド起源の可能性が指摘されていた。 | 高 | `source--daily-da76d64966b546f28391` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Pakistan | Targeting text mentions pakistan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | elation of reboot events with new outbound connections Delay network access post-reboot for inspection Post- Compromise Local logging for operator tracking T1005 (Local Data Collection) Detection of non- standard application logging Log review and anomaly detection Table 3. RagaSerpent MITRE TTP ATTC&K |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373`, `source--sidewinder--1d23a413a917d260` |
| Discovery | T1007 | System Service Discovery | bs Published: January 13th 2021 Intelligence current as of: December 11th 2020 Page 19 o T1518: Software Discovery o T1082: System Information Discovery o T1007: System Service Discovery o T1124: System Time Discovery • TA0009: Collection o T1119: Automated Collection o T1602: Data from Configuration Repository § T1602.002: Network Device Configuration Dump o T1005: Data from Local System o T1039: Data from Network Shared Drive o T1025: |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1020 | Automated Exfiltration | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Collection | T1025 | Data from Removable Media | 02: Data from Configuration Repository § T1602.002: Network Device Configuration Dump o T1005: Data from Local System o T1039: Data from Network Shared Drive o T1025: Data from Removable Media o T1074: Data Staged § T1074.001: Local Data Staging • TA0011: Command and Control o T1071: Application Layer Protocol • TA0010: Exfiltration o T1020: Automated Exfiltration o T1041: Exfiltration Over C2 Channel |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Stealth | T1027 | Obfuscated Files or Information | 2) of ClientSetup.exe achieves Persistence (T1543.003) by installing MANC.exe as an auto-starting Windows Service. Defense Evasion involves Obfuscated Files (T1027), hidden staging directories, and process Masquerading (T1036.004) (e.g., running under svchost.exe). The Command and Control (C2) IP (e.g., 45.119.55.66) is derived from the installer filename, stored in YTSysConfig.ini, and used for outbound raw TCP communication. |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Stealth | T1027.002 | Software Packing | ces collisions 5 Payload is packed/compressed, and embedded content is staged from internal resources (self- extracting installer behavior) Defense Evasion T1027.002 Obfuscated/ Compressed Files and Information: Software Packing conceals → real payload components until runtime |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | 480 EDR detection of unusual global mutexes Alert-only (high-fidelity indicator); threat hunting pivot Defense Evasion Masquerading as legitimate software T1036 File path and naming anomaly detection Enforce signed software execution Staging Creation of uncommon directories (C:\install\, C:\log\) T1036 File system monitoring for root-level directory creation Restrict write access to system root Command & Control Outbound commun |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Stealth | T1036.004 | Masquerade Task or Service | alling MANC.exe as an auto-starting Windows Service. Defense Evasion involves Obfuscated Files (T1027), hidden staging directories, and process Masquerading (T1036.004) (e.g., running under svchost.exe). The Command and Control (C2) IP (e.g., 45.119.55.66) is derived from the installer filename, stored in YTSysConfig.ini, and used for outbound raw TCP communication. A Discovery/Scoping step is also present, where the NETConfig.ytf |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--0ae2943d4dd4a373` |
| Collection | T1039 | Data from Network Shared Drive | tion o T1119: Automated Collection o T1602: Data from Configuration Repository § T1602.002: Network Device Configuration Dump o T1005: Data from Local System o T1039: Data from Network Shared Drive o T1025: Data from Removable Media o T1074: Data Staged § T1074.001: Local Data Staging • TA0011: Command and Control o T1071: Application Layer Protocol • TA0010: Exfiltration o T1020: Automated Exfiltration o T1041: Exfiltration Over C2 Channel |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | aged § T1074.001: Local Data Staging • TA0011: Command and Control o T1071: Application Layer Protocol • TA0010: Exfiltration o T1020: Automated Exfiltration o T1041: Exfiltration Over C2 Channel |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Execution | T1059 | Command and Scripting Interpreter | signed or low-reputation executables Application allowlisting; restrict user execution rights Execution Installer spawning secondary payloads from %TEMP% T1059 Process tree monitoring for child EXEs from TEMP Block execution from TEMP directories Persistence Registry modification for execution path T1547.001 Registry integrity monitoring on HKLM\Software\ Wow6432Node Harden registry permissions; audit startup entries Defense E |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373`, `source--sidewinder--1d23a413a917d260` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Execution | T1059.007 | JavaScript | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Discovery | T1069 | Permission Groups Discovery | -Loading • TA0007: Discovery o T1087: Account Discovery § T1087.001: Local Account o T1083: File and Directory Discovery o T1120: Peripheral Device Discovery o T1069: Permission Groups Discovery o T1057: Process Discovery |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Command And Control | T1071 | Application Layer Protocol | staller writes local configuration (YTSysConfig, section [YTSTATUS]) including ServerIP / ZRServerIP and operational flags Command and Control (pre-stage) T1071 (inferred) Application Layer Protocol configures → downstream agent knows where/how to connect 12 Server address is operator- parameterized by parsing an IPv4-like prefix from the executable filename (e.g., 45.119.55.66ClientSetup.exe) Defense Evasion T1027 (concep- tu |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373`, `source--sidewinder--1d23a413a917d260` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--0ae2943d4dd4a373` |
| Collection | T1074 | Data Staged | ory § T1602.002: Network Device Configuration Dump o T1005: Data from Local System o T1039: Data from Network Shared Drive o T1025: Data from Removable Media o T1074: Data Staged § T1074.001: Local Data Staging • TA0011: Command and Control o T1071: Application Layer Protocol • TA0010: Exfiltration o T1020: Automated Exfiltration o T1041: Exfiltration Over C2 Channel |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Collection | T1074.001 | Local Data Staging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | 04: User Execution § T1204.002: Malicious File § T1204.001: Malicious Link • TA0003: Persistence o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading o T1078: Valid Accounts • TA0004: Privilege Escalation o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading • TA0005: Defense Evasion o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading • TA0007: Discovery o T1087: Account Discovery § T1087.001: Local Account o T1083: F |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Discovery | T1087 | Account Discovery | ijack Execution Flow § T1574.002: DLL Side-Loading • TA0005: Defense Evasion o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading • TA0007: Discovery o T1087: Account Discovery § T1087.001: Local Account o T1083: File and Directory Discovery o T1120: Peripheral Device Discovery o T1069: Permission Groups Discovery o T1057: Process Discovery |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Discovery | T1087.001 | Local Account | 4.002: DLL Side-Loading • TA0005: Defense Evasion o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading • TA0007: Discovery o T1087: Account Discovery § T1087.001: Local Account o T1083: File and Directory Discovery o T1120: Peripheral Device Discovery o T1069: Permission Groups Discovery o T1057: Process Discovery |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Command And Control | T1095 | Non-Application Layer Protocol | network activity hides under a legitimate-looking name 24 Masqueraded svchost.exe establishes outbound raw TCP to 45[.]119[.]55[.]66 Command and Control T1095 Non- Application Layer Protocol establishes → C2 channel for tasking/ control Table 2. Summary of RagaSerpent’s Attack Stages The threat actor aligns more strongly with an India-origin Advanced Persistent Threat (APT), specifically SideWinder, with any observed Chinese |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--0ae2943d4dd4a373` |
| Execution | T1106 | Native API | r stage begins 4 SelfDecom “CreateMutexA(..., “Global\SelfDecom”)” enforces a single-instance guard (mutex) to prevent re-entry / noisy execution Execution T1106 Native API controls → execution flow stays deterministic and reduces collisions 5 Payload is packed/compressed, and embedded content is staged from internal resources (self- extracting installer behavior) Defense Evasion T1027.002 Obfuscated/ Compressed Files and Inform |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Defense Impairment, Persistence | T1112 | Modify Registry | used as install markers/lookup by other components) HKLM\ SYSTEM\CurrentControlSet\ Services\MANC and HKEY_ LOCAL_MACHINE\SOFTWARE\ BeaView Defense Evasion T1112 Modify Registry supports → later stages can locate installed paths and state 14 MANC.exe writes Safe Mode service entries: HKLM\SYSTEM\ ControlSet001\Control\SafeBoot\ Minimal\Manc = Service Persistence T1543.003 Create or Modify System Process: Windows Service extends → |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Collection | T1119 | Automated Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Discovery | T1120 | Peripheral Device Discovery | Execution Flow § T1574.002: DLL Side-Loading • TA0007: Discovery o T1087: Account Discovery § T1087.001: Local Account o T1083: File and Directory Discovery o T1120: Peripheral Device Discovery o T1069: Permission Groups Discovery o T1057: Process Discovery |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Discovery | T1124 | System Time Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | hip (MITRE-style) 6 Installer extracts resource payload (“SETUP”) and runs inflate/deflate- like decompression to materialize files on disk Defense Evasion T1140 Deobfuscate/ Decode Files or Information unpacks → drops/ installable components become available 7 Installer creates directories and drops/copies components (multi- stage layout; includes helper executables) Execution T1106 Native API stages → next-stage component(s) can |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Execution | T1204 | User Execution | ommand and Scripting Interpreter § T1059.007: JavaScript/Jscript § T1059.001: PowerShell § T1059.005: Visual Basic o T1203: Exploitation for Client Execution o T1204: User Execution § T1204.002: Malicious File § T1204.001: Malicious Link • TA0003: Persistence o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading o T1078: Valid Accounts • TA0004: Privilege Escalation o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading • TA0005 |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--0ae2943d4dd4a373`, `source--sidewinder--1d23a413a917d260` |
| Stealth | T1218.005 | Mshta | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1480 | Execution Guardrails | on HKLM\Software\ Wow6432Node Harden registry permissions; audit startup entries Defense Evasion Mutex creation to prevent reinfection (Global\SelfDecom) T1480 EDR detection of unusual global mutexes Alert-only (high-fidelity indicator); threat hunting pivot Defense Evasion Masquerading as legitimate software T1036 File path and naming anomaly detection Enforce signed software execution Staging Creation of uncommon directories |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Discovery | T1518 | Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--1d23a413a917d260` |
| Discovery | T1518.001 | Security Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | tion & Persistence: User-driven execution leading to staged deployment of payloads (e.g., MANC.exe) and establishing persistence via Windows Service creation (T1543.003). • C2 Communication: Direct, raw TCP beaconing to hardcoded IPs (e.g., 45.119.55.66). • Evasion: Heavy reliance on behavioral evasion (mutexes, process masquerading) over infrastructure evasion. Outlook: Defense must shift from blocking static Indicators of Compromise (IOCs) t |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Persistence, Privilege Escalation | T1546.015 | Component Object Model Hijacking | iability across control sets 17 FSHost32.exe writes COM registration artifacts: HKLM\ SOFTWARE\Classes\AppID\ NetworkCVSIcon.DLL with AppID GUID Persistence T1546.015 Component Object Model Hijacking prepares → COM- based activation surface (AppID/ registration) 18 FSHost32.exe writes COM CLSID artifacts: HKLM\ SOFTWARE\Classes\CLSID\ {2F0B3348-...}\InprocServer32 (ThreadingModel=Apartment) and CLSID\{...}\AppID Persistence T1546.015 Co |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--0ae2943d4dd4a373` |
| Execution | T1559.002 | Dynamic Data Exchange | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1562.001 | MITRE ATT&CK T1562.001 | ) can be executed 8 svchost.exe deletes UpperFilters under HKLM\SYSTEM\ ControlSet001\Control\ Class\{36FC9E60-C465- 11CF-8056-444553540000} Defense Evasion T1562.001 (inferred) Impair Defenses: Disable or Modify Tools degrades → system filtering behavior (may reduce monitoring/controls depending on environment) 9 MANC.exe deletes ProxyBypass and IntranetName values under HKLM\SOFTWARE\Microsoft\ Windows\CurrentVersion\ Internet Se |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--0ae2943d4dd4a373`, `source--sidewinder--1d23a413a917d260` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sidewinder--0ae2943d4dd4a373`, `source--sidewinder--1d23a413a917d260` |
| Execution, Stealth | T1574 | Hijack Execution Flow | Visual Basic o T1203: Exploitation for Client Execution o T1204: User Execution § T1204.002: Malicious File § T1204.001: Malicious Link • TA0003: Persistence o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading o T1078: Valid Accounts • TA0004: Privilege Escalation o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading • TA0005: Defense Evasion o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading • TA0007: Discovery o T |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1574.002 | MITRE ATT&CK T1574.002 | ion for Client Execution o T1204: User Execution § T1204.002: Malicious File § T1204.001: Malicious Link • TA0003: Persistence o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading o T1078: Valid Accounts • TA0004: Privilege Escalation o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading • TA0005: Defense Evasion o T1574: Hijack Execution Flow § T1574.002: DLL Side-Loading • TA0007: Discovery o T1087: Account Discovery § T1087.001 |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Resource Development | T1583 | Acquire Infrastructure | iness Relationships § T1591.001: Determine Physical Locations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA0042: Resource Development o T1583: Acquire Infrastructure § T1583.001: Domains § T1583.004: Server • TA0001: Initial Access o T1566.001: Spearphishing Attachment o T1566.002: Spearphishing Link • TA0002: Execution o T1059: Command and Scripting Interpreter § T1059.007: JavaScript/Jscript § T1059.001: PowerShell |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Resource Development | T1583.001 | Domains | detection Enforce DMARC/DKIM/ SPF; block executable attachments from email Initial Access Phishing links leading to lookalike domains or IP-hosted payloads T1583.001 URL reputation scoring; detection of newly registered domains Domain monitoring; restrict access to newly registered domains Execution User execution of malicious installer (EXE) T1204.002 EDR alerts on unsigned or low-reputation executables Application allowlisting; re |  |  | 不明 | 不明 | 中 | `source--sidewinder--0ae2943d4dd4a373`, `source--sidewinder--1d23a413a917d260` |
| Resource Development | T1583.004 | Server | ocations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA0042: Resource Development o T1583: Acquire Infrastructure § T1583.001: Domains § T1583.004: Server • TA0001: Initial Access o T1566.001: Spearphishing Attachment o T1566.002: Spearphishing Link • TA0002: Execution o T1059: Command and Scripting Interpreter § T1059.007: JavaScript/Jscript § T1059.001: PowerShell § T1059.005: Visual Basic o T1203: Exploitation for Clien |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Reconnaissance | T1589 | Gather Victim Identity Information | abs Published: January 13th 2021 Intelligence current as of: December 11th 2020 Page 18 Appendix A. Mapped to ATT&CK Framework • TA0043: Reconnaissance o T1589: Gather Victim Identity Information § T1589.002: Email Addresses § T1589.003: Employee Names o T1591: Gather Victim Org Information § T1591.002: Business Relationships § T1591.001: Determine Physical Locations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Reconnaissance | T1589.002 | Email Addresses | e current as of: December 11th 2020 Page 18 Appendix A. Mapped to ATT&CK Framework • TA0043: Reconnaissance o T1589: Gather Victim Identity Information § T1589.002: Email Addresses § T1589.003: Employee Names o T1591: Gather Victim Org Information § T1591.002: Business Relationships § T1591.001: Determine Physical Locations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA0042: Resource Development o T1583: Acquire Infr |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Reconnaissance | T1589.003 | Employee Names | h 2020 Page 18 Appendix A. Mapped to ATT&CK Framework • TA0043: Reconnaissance o T1589: Gather Victim Identity Information § T1589.002: Email Addresses § T1589.003: Employee Names o T1591: Gather Victim Org Information § T1591.002: Business Relationships § T1591.001: Determine Physical Locations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA0042: Resource Development o T1583: Acquire Infrastructure § T1583.001: Domai |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Reconnaissance | T1591 | Gather Victim Org Information | A. Mapped to ATT&CK Framework • TA0043: Reconnaissance o T1589: Gather Victim Identity Information § T1589.002: Email Addresses § T1589.003: Employee Names o T1591: Gather Victim Org Information § T1591.002: Business Relationships § T1591.001: Determine Physical Locations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA0042: Resource Development o T1583: Acquire Infrastructure § T1583.001: Domains § T1583.004: Server • |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Reconnaissance | T1591.001 | Determine Physical Locations | ctim Identity Information § T1589.002: Email Addresses § T1589.003: Employee Names o T1591: Gather Victim Org Information § T1591.002: Business Relationships § T1591.001: Determine Physical Locations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA0042: Resource Development o T1583: Acquire Infrastructure § T1583.001: Domains § T1583.004: Server • TA0001: Initial Access o T1566.001: Spearphishing Attachment o T1566.002: Spea |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Reconnaissance | T1591.002 | Business Relationships | 3: Reconnaissance o T1589: Gather Victim Identity Information § T1589.002: Email Addresses § T1589.003: Employee Names o T1591: Gather Victim Org Information § T1591.002: Business Relationships § T1591.001: Determine Physical Locations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA0042: Resource Development o T1583: Acquire Infrastructure § T1583.001: Domains § T1583.004: Server • TA0001: Initial Access o T1566.001: Spearp |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Reconnaissance | T1591.003 | Identify Business Tempo | il Addresses § T1589.003: Employee Names o T1591: Gather Victim Org Information § T1591.002: Business Relationships § T1591.001: Determine Physical Locations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA0042: Resource Development o T1583: Acquire Infrastructure § T1583.001: Domains § T1583.004: Server • TA0001: Initial Access o T1566.001: Spearphishing Attachment o T1566.002: Spearphishing Link • TA0002: Execution o T1059 |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Reconnaissance | T1591.004 | Identify Roles | mes o T1591: Gather Victim Org Information § T1591.002: Business Relationships § T1591.001: Determine Physical Locations § T1591.003: Identify Business Tempo § T1591.004: Identify Roles • TA0042: Resource Development o T1583: Acquire Infrastructure § T1583.001: Domains § T1583.004: Server • TA0001: Initial Access o T1566.001: Spearphishing Attachment o T1566.002: Spearphishing Link • TA0002: Execution o T1059: Command and Scripting Interpreter § |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Reconnaissance | T1598.002 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1602 | Data from Configuration Repository | ery o T1082: System Information Discovery o T1007: System Service Discovery o T1124: System Time Discovery • TA0009: Collection o T1119: Automated Collection o T1602: Data from Configuration Repository § T1602.002: Network Device Configuration Dump o T1005: Data from Local System o T1039: Data from Network Shared Drive o T1025: Data from Removable Media o T1074: Data Staged § T1074.001: Local Data Staging • TA0011: Command and Control o T107 |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |
| Collection | T1602.002 | Network Device Configuration Dump | T1007: System Service Discovery o T1124: System Time Discovery • TA0009: Collection o T1119: Automated Collection o T1602: Data from Configuration Repository § T1602.002: Network Device Configuration Dump o T1005: Data from Local System o T1039: Data from Network Shared Drive o T1025: Data from Removable Media o T1074: Data Staged § T1074.001: Local Data Staging • TA0011: Command and Control o T1071: Application Layer Protocol • TA0010: Exfiltra |  |  | 不明 | 不明 | 中 | `source--sidewinder--1d23a413a917d260` |

## IOC／artifact概要

- IOC値: 218件
- IOC観測: 250件
- 複数攻撃で観測: 0件
- 要レビュー候補: 31件
- 非IOC artifact観測: 171件（`artifacts.csv`）

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
| source--daily-da76d64966b546f28391 | SideWinder APT、アジア、中東、アフリカの海事、原子力、ITセクターを標的に | thehackernews.com | 2025-03-12 | https://thehackernews.com/2025/03/sidewinder-apt-targets-maritime-nuclear.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--sidewinder--0ae2943d4dd4a373 | RagaSerpent SideWinder Adjacent Tax Audit Cluster MultiCountry Targeted Chain |  | 不明 | sidewinder/RagaSerpent SideWinder-Adjacent Tax Audit Cluster MultiCountry Targeted Chain.pdf | report | TLP:CLEAR | 中 |
| source--sidewinder--1d23a413a917d260 | global perspective of the sidewinder apt |  | 不明 | sidewinder/global-perspective-of-the-sidewinder-apt.pdf | report | TLP:CLEAR | 中 |
| source--sidewinder--64e1d418ba54a0af | readme |  | 不明 | sidewinder/readme.md | repository-notes | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
