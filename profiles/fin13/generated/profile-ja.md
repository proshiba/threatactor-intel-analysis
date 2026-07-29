# FIN13 脅威アクタープロファイル

- プロファイルID: `actor--fin13`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

FIN13の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **FIN13**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Elephant Beetle | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [FIN13](https://attack.mitre.org/groups/G1016) is a financially motivated cyber threat group that has targeted the financial, retail, and hospitality industries in Mexico and Latin America, as early as 2016. [FIN13](https://attack.mitre.org/groups/G1016) achieves its objectives by stealing intellectual property, financial data, mergers and acquisition information, or PII.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |
| Capability | certutil, Impacket, Empire, Mimikatz |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Elephant Beetle | single-alias-intersection | 中 |  | https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia- Elephant Beetle_Jan2022.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Elephant+Beetle&n=1 |
| etda-threat-group-cards | FIN13 | canonical-name | 高 |  | https://www.mandiant.com/resources/fin13-cybercriminal-mexico<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=FIN13&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | FIN13 | canonical-name | 高 | RU | https://www.mandiant.com/resources/fin13-cybercriminal-mexico<br>https://blog.sygnia.co/elephant-beetle-an-organized-financial-theft-operation<br>https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | FIN13 - G1016 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1016<br>https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf<br>https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico |
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

未確認

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| countries | メキシコ | MITRE ATT&CKのGroup概要でFIN13の標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| sectors | 小売・ホスピタリティ | [FIN13](https://attack.mitre.org/groups/G1016) is a financially motivated cyber threat group that has targeted the financial, retail, and hospitality industries in Mexico and Latin America, as early as 2016. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 金融 | [FIN13](https://attack.mitre.org/groups/G1016) is a financially motivated cyber threat group that has targeted the financial, retail, and hospitality industries in Mexico and Latin America, as early as 2016. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 医療・ヘルスケア | [FIN13](https://attack.mitre.org/groups/G1016) is a financially motivated cyber threat group that has targeted the financial, retail, and hospitality industries in Mexico and Latin America, as early as 2016. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [FIN13](https://attack.mitre.org/groups/G1016) has obtained memory dumps with ProcDump to parse and extract credentials from a victim's LSASS process memory with [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.002 | Security Account Manager | [FIN13](https://attack.mitre.org/groups/G1016) has extracted the SAM and SYSTEM registry hives using the `reg.exe` binary for obtaining password hashes from a compromised machine.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.003 | NTDS | [FIN13](https://attack.mitre.org/groups/G1016) has harvested the NTDS.DIT file and leveraged the [Impacket](https://attack.mitre.org/software/S0357) tool on the compromised domain controller to locally decrypt it.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [FIN13](https://attack.mitre.org/groups/G1016) has gathered stolen credentials, sensitive data such as point-of-sale (POS), and ATM data from a compromised network before exfiltration.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has used `nslookup` and `ipconfig` for network reconnaissance efforts. [FIN13](https://attack.mitre.org/groups/G1016) has also utilized a compromised Symantec Altiris console and LanDesk account to retrieve network information.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016.001 | Internet Connection Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has used `Ping` and `tracert` for network reconnaissance efforts.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [FIN13](https://attack.mitre.org/groups/G1016) has remotely accessed compromised environments via Remote Desktop Services (RDS) for lateral movement.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [FIN13](https://attack.mitre.org/groups/G1016) has leveraged SMB to move laterally within a compromised network via application servers and SQL servers.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [FIN13](https://attack.mitre.org/groups/G1016) has remotely accessed compromised environments via secure shell (SSH) for lateral movement.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.006 | Windows Remote Management | [FIN13](https://attack.mitre.org/groups/G1016) has leveraged `WMI` to move laterally within a compromised network via application servers and SQL servers.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [FIN13](https://attack.mitre.org/groups/G1016) has masqueraded staged data by using the Windows [certutil](https://attack.mitre.org/software/S0160) utility to generate fake Base64 encoded certificates with the input file.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [FIN13](https://attack.mitre.org/groups/G1016) has used scheduled tasks names such as `acrotyr` and `AppServicesr` to mimic the same names in a compromised network's `C:\Windows` directory.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [FIN13](https://attack.mitre.org/groups/G1016) has masqueraded WAR files to look like legitimate packages such as, wsexample.war, wsexamples.com, examples.war, and exampl3s.war.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has utilized `nmap` for reconnaissance efforts. [FIN13](https://attack.mitre.org/groups/G1016) has also scanned for internal MS-SQL servers in a compromised network.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [FIN13](https://attack.mitre.org/groups/G1016) has utilized `WMI` to execute commands and move laterally on compromised Windows machines.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has used `netstat` and other net  commands for network reconnaissance efforts.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [FIN13](https://attack.mitre.org/groups/G1016) has created scheduled tasks in the `C:\Windows` directory of the compromised network.(Citation: Mandiant FIN13 Aug 2022)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [FIN13](https://attack.mitre.org/groups/G1016) has logged the keystrokes of victims to escalate privileges.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [FIN13](https://attack.mitre.org/groups/G1016) has used PowerShell commands to obtain DNS data from a compromised network.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [FIN13](https://attack.mitre.org/groups/G1016) has leveraged `xp_cmdshell` and Windows Command Shell to execute commands on a compromised machine. [FIN13](https://attack.mitre.org/groups/G1016) has also attempted to leverage the ‘xp_cmdshell’ SQL procedure to execute remote commands on internal MS-SQL servers.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [FIN13](https://attack.mitre.org/groups/G1016) has used VBS scripts for code execution on comrpomised machines.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069 | Permission Groups Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has enumerated all users and roles from a victim's main treasury system.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [FIN13](https://attack.mitre.org/groups/G1016) has used HTTP requests to chain multiple web shells and to contact actor-controlled C2 servers prior to exfiltrating stolen data.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [FIN13](https://attack.mitre.org/groups/G1016) has utilized the following temporary folders on compromised Windows and Linux systems for their operations prior to exfiltration: `C:\Windows\Temp` and `/tmp`.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.001 | Default Accounts | [FIN13](https://attack.mitre.org/groups/G1016) has leveraged default credentials for authenticating myWebMethods (WMS) and QLogic web management interface to gain initial access.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has collected local host information by utilizing Windows commands `systeminfo`, `fsutil`, and `fsinfo`. [FIN13](https://attack.mitre.org/groups/G1016) has also utilized a compromised Symantex Altiris console and LanDesk account to retrieve host information.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has used the Windows `dir` command to enumerate files and directories in a victim's network.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087 | Account Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has enumerated all users and their roles from a victim's main treasury system.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [FIN13](https://attack.mitre.org/groups/G1016) can identify user accounts associated with a Service Principal Name and query Service Principal Names within the domain by utilizing the following scripts: `GetUserSPNs.vbs` and `querySpn.vbs`.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.001 | Internal Proxy | [FIN13](https://attack.mitre.org/groups/G1016) has utilized a proxy tool to communicate between compromised assets.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.007 | Additional Local or Domain Groups | [FIN13](https://attack.mitre.org/groups/G1016) has assigned newly created accounts the sysadmin role to maintain persistence.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [FIN13](https://attack.mitre.org/groups/G1016) has downloaded additional tools and malware to compromised systems.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [FIN13](https://attack.mitre.org/groups/G1016) has gained access to compromised environments via remote access services such as the corporate virtual private network (VPN).(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1134.003 | Make and Impersonate Token | [FIN13](https://attack.mitre.org/groups/G1016) has utilized tools such as Incognito V2 for token manipulation and impersonation.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has executed net view commands for enumeration of open shares on compromised machines.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.001 | Local Account | [FIN13](https://attack.mitre.org/groups/G1016) has created MS-SQL local accounts in a compromised network.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [FIN13](https://attack.mitre.org/groups/G1016) has utilized `certutil` to decode base64 encoded versions of custom malware.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [FIN13](https://attack.mitre.org/groups/G1016) has exploited known vulnerabilities such as CVE-2017-1000486 (Primefaces Application Expression Language Injection), CVE-2015-7450 (WebSphere Application Server SOAP Deserialization Exploit), CVE-2010-5326 (SAP NewWeaver Invoker Servlet Exploit), and EDB-ID-24963 (SAP NetWeaver ConfigServlet Remote Code Execution) to gain initial access.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [FIN13](https://attack.mitre.org/groups/G1016) has utilized obfuscated and open-source web shells such as JspSpy, reGeorg, MiniWebCmdShell, and Vonloesch Jsp File Browser 1.2 to enable remote code execution and to execute commands on compromised web server.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [FIN13](https://attack.mitre.org/groups/G1016) has used Windows Registry run keys such as, `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run\hosts` to maintain persistence.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | [FIN13](https://attack.mitre.org/groups/G1016) has used the PowerShell utility `Invoke-SMBExec` to execute the pass the hash method for lateral movement within an compromised environment.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [FIN13](https://attack.mitre.org/groups/G1016) has obtained administrative credentials by browsing through local files on a compromised machine.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Defense Impairment, Persistence | T1556 | Modify Authentication Process | [FIN13](https://attack.mitre.org/groups/G1016) has replaced legitimate KeePass binaries with trojanized versions to collect passwords from numerous applications.(Citation: Mandiant FIN13 Aug 2022)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [FIN13](https://attack.mitre.org/groups/G1016) has compressed the dump output of compromised credentials with a 7zip binary.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | [FIN13](https://attack.mitre.org/groups/G1016) has created hidden files and folders within a compromised Linux system `/tmp` directory. [FIN13](https://attack.mitre.org/groups/G1016) also has used `attrib.exe` to hide gathered local host information.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1565 | Data Manipulation | [FIN13](https://attack.mitre.org/groups/G1016) has injected fraudulent transactions into compromised networks that mimic legitimate behavior to siphon off incremental amounts of money.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [FIN13](https://attack.mitre.org/groups/G1016) has utilized web shells and Java tools for tunneling capabilities to and from compromised assets.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [FIN13](https://attack.mitre.org/groups/G1016) has used IISCrack.dll as a side-loading technique to load a malicious version of httpodbc.dll on old IIS Servers (CVE-2001-0507).(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [FIN13](https://attack.mitre.org/groups/G1016) has utilized custom malware to maintain persistence in a compromised environment.(Citation: Mandiant FIN13 Aug 2022)(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [FIN13](https://attack.mitre.org/groups/G1016) has utilized publicly available tools such as [Mimikatz](https://attack.mitre.org/software/S0002), [Impacket](https://attack.mitre.org/software/S0357), PWdump7, ProcDump, Nmap, and Incognito V2 for targeting efforts.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | [FIN13](https://attack.mitre.org/groups/G1016) has researched employees to target for social engineering attacks.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1590.004 | Network Topology | [FIN13](https://attack.mitre.org/groups/G1016) has searched for infrastructure that can provide remote access to an environment for targeting efforts.(Citation: Mandiant FIN13 Aug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | [FIN13](https://attack.mitre.org/groups/G1016) has observed the victim's software and infrastructure over several months to understand the technical process of legitimate financial transactions, prior to attempting to conduct fraudulent transactions.(Citation: Sygnia Elephant Beetle Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 6件（`artifacts.csv`）

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
| source--fin13--5a1c2766fdffd795 | fin13 |  | 不明 | actor_profile/evidence/fin13.csv | structured-data | TLP:CLEAR | 中 |
| source--fin13--a2f9313179779203 | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--fin13--617f575a8aaf0416 | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--fin13--4db4fbde7e443885 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--fin13--3109e0b68f37c2ea | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--fin13--a0c514dc8bf3d005 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
