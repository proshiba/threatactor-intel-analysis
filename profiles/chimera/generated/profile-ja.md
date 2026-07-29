# Chimera 脅威アクタープロファイル

- プロファイルID: `actor--chimera`
- 状態: draft
- 更新日時: 2026-07-29T15:38:34Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Chimeraの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Chimera**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| GELSEMIUM | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Gelsemium | overlaps-with | 共有alias: Gelsemium, GELSEMIUM | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Chimera](https://attack.mitre.org/groups/G0114) is a suspected China-based threat group that has been active since at least 2018 targeting the semiconductor industry in Taiwan as well as data from the airline industry.(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021) |
| Capability | Cobalt Strike, OwlProxy, SessionManager, Net, BloodHound, Mimikatz, esentutl, PsExec |
| Infrastructure |  |
| Victim | Taiwan semiconductors |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Chimera | canonical-name | 高 | China | https://cycraft.com/download/%5BTLP-White%5D20200415%20Chimera_V4.1.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Chimera&n=1 |
| etda-threat-group-cards | Gelsemium | single-alias-intersection | 中 | China | https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf<br>https://www.venustech.com.cn/uploads/2018/08/231401512426.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Gelsemium&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Gelsemium | single-alias-intersection | 中 |  | https://www.welivesecurity.com/2021/06/09/gelsemium-when-threat-actors-go-gardening/<br>https://www.venustech.com.cn/uploads/2018/08/231401512426.pdf<br>https://hitcon.org/2016/pacific/0composition/pdf/1202/1202%20R0%200930%20an%20intelligance-driven%20approach%20to%20cyber%20defense.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Chimera - G0114 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0114<br>https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf<br>https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/ |
| misp-mitre-intrusion-set | Gelsemium - G0141 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0141<br>https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf |
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
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--owlproxy | OwlProxy | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sessionmanager | SessionManager | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--bloodhound | BloodHound | [BloodHound](https://attack.mitre.org/software/S0521) is an Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment.(Citation: GitHub Bloodhound)(Citation: CrowdStrike BloodHound April 2018)(Citation: FoxIT Wocao December 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--esentutl | esentutl | [esentutl](https://attack.mitre.org/software/S0404) is a command-line tool that provides database utilities for the Windows Extensible Storage Engine.(Citation: Microsoft Esentutl) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| countries | Taiwan | Targeting text mentions taiwan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | 運輸・航空・海運 | [Chimera](https://attack.mitre.org/groups/G0114) is a suspected China-based threat group that has been active since at least 2018 targeting the semiconductor industry in Taiwan as well as data from the airline industry.(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.003 | NTDS | [Chimera](https://attack.mitre.org/groups/G0114) has gathered the SYSTEM registry and ntds.dit files from target systems.(Citation: Cycraft Chimera April 2020) [Chimera](https://attack.mitre.org/groups/G0114) specifically has used the NtdsAudit tool to dump the password hashes of domain users via <code>msadcs.exe "NTDS.dit" -s "SYSTEM" -p RecordedTV_pdmp.txt --users-csv RecordedTV_users.csv</code> and used ntdsutil to copy the Active Directory database.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used <code>net start</code> and <code>net use</code> for system service discovery.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | [Chimera](https://attack.mitre.org/groups/G0114) has queried Registry keys using <code>reg query \\<host>\HKU\<SID>\SOFTWARE\Microsoft\Terminal Server Client\Servers</code> and <code>reg query \\<host>\HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Internet Settings</code>.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used [ipconfig](https://attack.mitre.org/software/S0100), [Ping](https://attack.mitre.org/software/S0097), and <code>tracert</code> to enumerate the IP address and network environment and settings of the local host.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has utilized various scans and queries to find domain controllers and remote services in the target environment.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Chimera](https://attack.mitre.org/groups/G0114) has used RDP to access targeted systems.(Citation: Cycraft Chimera April 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [Chimera](https://attack.mitre.org/groups/G0114) has used Windows admin shares to move laterally.(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.006 | Windows Remote Management | [Chimera](https://attack.mitre.org/groups/G0114) has used WinRM for lateral movement.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [Chimera](https://attack.mitre.org/groups/G0114) has encoded PowerShell commands.(Citation: Cycraft Chimera April 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used the <code>quser</code> command to show currently logged on users.(Citation: NCC Group Chimera January 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Chimera](https://attack.mitre.org/groups/G0114) has renamed malware to GoogleUpdate.exe and WinRAR to jucheck.exe, RecordedTV.ms, teredo.tmp, update.exe, and msadcs1.exe.(Citation: Cycraft Chimera April 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1039 | Data from Network Shared Drive | [Chimera](https://attack.mitre.org/groups/G0114) has collected data of interest from network shares.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [Chimera](https://attack.mitre.org/groups/G0114) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) C2 beacons for data exfiltration.(Citation: NCC Group Chimera January 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used the <code>get -b <start ip> -e <end ip> -p</code> command for network scanning as well as a custom Python tool  packed into a Windows executable named Get.exe to scan IP ranges for HTTP.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [Chimera](https://attack.mitre.org/groups/G0114) has used WMIC to execute remote commands.(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used <code>netstat -ano \| findstr EST</code> to discover network connections.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Chimera](https://attack.mitre.org/groups/G0114) has used scheduled tasks to invoke Cobalt Strike including through batch script <code>schtasks /create /ru "SYSTEM" /tn "update" /tr "cmd /c c:\windows\temp\update.bat" /sc once /f /st</code> and to maintain persistence.(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used <code>tasklist</code> to enumerate processes.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Chimera](https://attack.mitre.org/groups/G0114) has used PowerShell scripts to execute malicious payloads and the DSInternals PowerShell module to make use of Active Directory features.(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Chimera](https://attack.mitre.org/groups/G0114) has used the Windows Command Shell and batch scripts for execution on compromised hosts.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.001 | Local Groups | [Chimera](https://attack.mitre.org/groups/G0114) has used <code>net localgroup administrators</code> to identify  accounts with local administrative rights.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Chimera](https://attack.mitre.org/groups/G0114) has performed file deletion to evade detection.(Citation: Cycraft Chimera April 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.006 | Timestomp | [Chimera](https://attack.mitre.org/groups/G0114) has used a Windows version of the Linux <code>touch</code> command to modify the date and time stamp on DLLs.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Chimera](https://attack.mitre.org/groups/G0114) has used HTTPS for C2 communications.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | [Chimera](https://attack.mitre.org/groups/G0114) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) to encapsulate C2 in DNS traffic.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [Chimera](https://attack.mitre.org/groups/G0114) has staged stolen data locally on compromised hosts.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.002 | Remote Data Staging | [Chimera](https://attack.mitre.org/groups/G0114) has staged stolen data on designated servers in the target environment.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Chimera](https://attack.mitre.org/groups/G0114) has used a valid account to maintain persistence via scheduled task.(Citation: Cycraft Chimera April 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [Chimera](https://attack.mitre.org/groups/G0114) has used compromised domain accounts to gain access to the target environment.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has utilized multiple commands to identify data of interest in file and directory listings.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | [Chimera](https://attack.mitre.org/groups/G0114) has used <code>net user</code> for account discovery.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [Chimera](https://attack.mitre.org/groups/G0114) has has used <code>net user /dom</code> and <code>net user Administrator</code> to enumerate domain accounts including administrator accounts.(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Chimera](https://attack.mitre.org/groups/G0114) has remotely copied tools and malware onto targeted systems.(Citation: Cycraft Chimera April 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | [Chimera](https://attack.mitre.org/groups/G0114) has used direct Windows system calls by leveraging Dumpert.(Citation: Cycraft Chimera April 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.003 | Password Spraying | [Chimera](https://attack.mitre.org/groups/G0114) has used multiple password spraying attacks against victim's remote services to obtain valid user and administrator accounts.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.004 | Credential Stuffing | [Chimera](https://attack.mitre.org/groups/G0114) has used credential stuffing against victim's remote services to obtain valid accounts.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1111 | Multi-Factor Authentication Interception | [Chimera](https://attack.mitre.org/groups/G0114) has registered alternate phone numbers for compromised users to intercept 2FA codes sent via SMS.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.001 | Local Email Collection | [Chimera](https://attack.mitre.org/groups/G0114) has harvested data from victim's e-mail including through execution of <code>wmic /node:<ip> process call create "cmd /c copy c:\Users\<username>\<path>\backup.pst c:\windows\temp\backup.pst" copy "i:\<path>\<username>\My Documents\<filename>.pst"<br>copy</code>.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.002 | Remote Email Collection | [Chimera](https://attack.mitre.org/groups/G0114) has harvested data from remote mailboxes including through execution of <code>\\<hostname>\c$\Users\<username>\AppData\Local\Microsoft\Outlook*.ost</code>.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [Chimera](https://attack.mitre.org/groups/G0114) has used custom DLLs for continuous retrieval of data from memory.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used <code>time /t</code> and <code>net time \\ip/hostname</code> for system time discovery.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [Chimera](https://attack.mitre.org/groups/G0114) has used legitimate credentials to login to an external VPN, Citrix, SSH, and other remote services.(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used <code>net share</code> and <code>net view</code> to identify network shares of interest.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1201 | Password Policy Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used the NtdsAudit utility to collect information related to accounts and passwords.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.002 | Sharepoint | [Chimera](https://attack.mitre.org/groups/G0114) has collected documents from the victim's SharePoint.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used <code>type \\<hostname>\c$\Users\<username>\Favorites\Links\Bookmarks bar\Imported From IE\*citrix*</code> for bookmark discovery.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has <code>nltest /domain_trusts</code> to identify domain trust relationships.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | [Chimera](https://attack.mitre.org/groups/G0114) has dumped password hashes for use in pass the hash authentication attacks.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Defense Impairment, Persistence | T1556.001 | Domain Controller Authentication | [Chimera](https://attack.mitre.org/groups/G0114)'s malware has altered the NTLM authentication program on domain controllers to allow [Chimera](https://attack.mitre.org/groups/G0114) to login without a valid credential.(Citation: Cycraft Chimera April 2020)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [Chimera](https://attack.mitre.org/groups/G0114) has used gzip for Linux OS and a modified RAR software to archive data on Windows hosts.(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Chimera](https://attack.mitre.org/groups/G0114) has exfiltrated stolen data to OneDrive accounts.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | [Chimera](https://attack.mitre.org/groups/G0114) has used [PsExec](https://attack.mitre.org/software/S0029) to deploy beacons on compromised systems.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [Chimera](https://attack.mitre.org/groups/G0114) has copied tools between compromised hosts using SMB.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [Chimera](https://attack.mitre.org/groups/G0114) has encapsulated [Cobalt Strike](https://attack.mitre.org/software/S0154)'s C2 protocol in DNS and HTTPS.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [Chimera](https://attack.mitre.org/groups/G0114) has used side loading to place malicious DLLs in memory.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Chimera](https://attack.mitre.org/groups/G0114) has obtained and used tools such as [BloodHound](https://attack.mitre.org/software/S0521), [Cobalt Strike](https://attack.mitre.org/software/S0154), [Mimikatz](https://attack.mitre.org/software/S0002), and [PsExec](https://attack.mitre.org/software/S0029).(Citation: Cycraft Chimera April 2020)(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.001 | Credentials | [Chimera](https://attack.mitre.org/groups/G0114) has collected credentials for the target organization from previous breaches for use in brute force attacks.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1680 | Local Storage Discovery | [Chimera](https://attack.mitre.org/groups/G0114) has used `fsutil fsinfo drives`, `systeminfo`, and `vssadmin list shadows` for system information including shadow volumes and drive information.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | [Chimera](https://attack.mitre.org/groups/G0114) has cleared event logs on compromised hosts.(Citation: NCC Group Chimera January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 28件（`artifacts.csv`）

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
| source--chimera--d4c16ff82ad4d37c | chimera |  | 不明 | actor_profile/evidence/chimera.csv | structured-data | TLP:CLEAR | 中 |
| source--chimera--09822664751bafa6 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--chimera--2fdbafaff7636a56 | article |  | 不明 | kimsuky/APTDown/article.txt | text-data | TLP:CLEAR | 中 |
| source--chimera--5c154a52d7acf987 | 2021 NCC Group Annual Research Report |  | 2021 | summary/2022/2021-NCC-Group-Annual-Research-Report.pdf | report | TLP:CLEAR | 中 |
| source--chimera--ca1e2f44836367d6 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--chimera--9a6c63261e1550bb | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--chimera--87fd006b8afc2ede | eset apt activity report q4 2023 q1 2024 |  | 2023 | summary/2024/eset-apt-activity-report-q4-2023-q1-2024.pdf | report | TLP:CLEAR | 中 |
| source--chimera--3aeaa356dbdfc7f8 | eset threat report h22024 |  | 不明 | summary/2024/eset-threat-report-h22024.pdf | report | TLP:CLEAR | 中 |
| source--chimera--fcd59fa2b9768151 | readme |  | 不明 | summary/2024/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--chimera--3c54b12a29aa0fc6 | TLP CLEAR CERT EU TLR 2024 v1 |  | 2024 | summary/2025/TLP-CLEAR-CERT-EU-TLR-2024-v1.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
