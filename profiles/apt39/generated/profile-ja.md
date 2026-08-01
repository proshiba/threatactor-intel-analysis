# APT39 脅威アクタープロファイル

- プロファイルID: `actor--apt39`
- 状態: draft
- 更新日時: 2026-07-29T23:13:53Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

APT39の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT39**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Chafer | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ITG07 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Remix Kitten | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Cadelle | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 8; mapping requires review. |
| Rana | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 8; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
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
| Adversary | [APT39](https://attack.mitre.org/groups/G0087) is one of several names for cyber espionage activity conducted by the Iranian Ministry of Intelligence and Security (MOIS) through the front company Rana Intelligence Computing since at least 2014. [APT39](https://attack.mitre.org/groups/G0087) has primarily targeted the travel, hospitality, academic, and telecommunications industries in Iran and across Asia, Africa, Europe, and North America to track individuals and entities considered to be a threat by the MOIS.(Citation: FireEye APT39 Jan 2019)(Citation: Symantec Chafer Dec 2015)(Citation: FBI FLASH APT39 September 2020)(Citation: Dept. of Treasury Iran Sanctions September 2020)(Citation: DOJ Iran Indictments September 2020) |
| Capability | ASPXSpy, Cadelspy, MechaFlounder, Remexi, Web Shells (aspx spy, b374k), plink, RemCom, VNC Bypass scanner, CoreSecurity tools, Impacket / Python exploits, NSSM, HTTPTunnel, SSH Tunnels to Windows Servers, Windows Credential Editor, pwdump, Mimikatz, NBTscan, CrackMapExec, ftp, PsExec |
| Infrastructure |  |
| Victim | Airlines, Airports, Transportation, Logistics - worldwide |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Cadelle | single-alias-intersection | 中 | Iran | https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Cadelle&n=1 |
| etda-threat-group-cards | Chafer, APT 39 | canonical-name | 高 | Iran | https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html<br>https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets<br>https://securityintelligence.com/posts/observations-of-itg07-cyber-operations/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Burgundy Sandstorm | multiple-name-intersection | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Cadelle | single-alias-intersection | 中 | IR | https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets |
| misp-threat-actor | APT39 | canonical-name | 高 | IR | https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html<br>https://www.symantec.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions<br>https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/ |
| misp-microsoft-activity-group | Burgundy Sandstorm | multiple-name-intersection | 高 | IR, Iran | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | APT39 - G0087 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0087<br>https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf<br>https://home.treasury.gov/news/press-releases/sm1127 |
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
| malware--aspxspy | ASPXSpy | [ASPXSpy](https://attack.mitre.org/software/S0073) is a Web shell. It has been modified by [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors to create the ASPXTool version. (Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cadelspy | Cadelspy | [Cadelspy](https://attack.mitre.org/software/S0454) is a backdoor that has been used by [APT39](https://attack.mitre.org/groups/G0087).(Citation: Symantec Chafer Dec 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--mechaflounder | MechaFlounder | [MechaFlounder](https://attack.mitre.org/software/S0459) is a python-based remote access tool (RAT) that has been used by [APT39](https://attack.mitre.org/groups/G0087). The payload uses a combination of actor developed code and code snippets freely available online in development communities.(Citation: Unit 42 MechaFlounder March 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--remexi | Remexi | [Remexi](https://attack.mitre.org/software/S0375) is a Windows-based Trojan that was developed in the C programming language.(Citation: Securelist Remexi Jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--web-shells-aspx-spy | Web Shells (aspx spy | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--b374k | b374k) | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--plink | plink | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--remcom | RemCom | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--vnc-bypass-scanner | VNC Bypass scanner | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--coresecurity-tools | CoreSecurity tools | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--impacket-python-exploits | Impacket / Python exploits | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--nssm | NSSM | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--httptunnel | HTTPTunnel | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--ssh-tunnels-to-windows-servers | SSH Tunnels to Windows Servers | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--windows-credential-editor | Windows Credential Editor | [Windows Credential Editor](https://attack.mitre.org/software/S0005) is a password dumping tool. (Citation: Amplia WCE) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--pwdump | pwdump | [pwdump](https://attack.mitre.org/software/S0006) is a credential dumper. (Citation: Wikipedia pwdump) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nbtscan | NBTscan | [NBTscan](https://attack.mitre.org/software/S0590) is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)(Citation: Symantec Waterbug Jun 2019)(Citation: FireEye APT39 Jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--crackmapexec | CrackMapExec | [CrackMapExec](https://attack.mitre.org/software/S0488), or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. [CrackMapExec](https://attack.mitre.org/software/S0488) collects Active Directory information to conduct lateral movement through targeted networks.(Citation: CME Github September 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ftp | ftp | [ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.(Citation: Microsoft FTP)(Citation: Linux FTP) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでAPT39の標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | 構造化OSINTの被害国フィールドでAPT39の標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イラン | [APT39](https://attack.mitre.org/groups/G0087) has primarily targeted the travel, hospitality, academic, and telecommunications industries in Iran and across Asia, Africa, Europe, and North America to track individuals and entities considered to be a threat by the MOIS.(Citation: FireEye APT39 Jan 2019)(Citation: Symantec Chafer Dec 2015)(Citation: FBI FLASH APT39 September 2020)(Citation: Dept. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | クウェート | 構造化OSINTの被害国フィールドでAPT39の標的・被害国としてクウェートが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | サウジアラビア | 構造化OSINTの被害国フィールドでAPT39の標的・被害国としてサウジアラビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スペイン | 構造化OSINTの被害国フィールドでAPT39の標的・被害国としてスペインが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 構造化OSINTの被害国フィールドでAPT39の標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ヨルダン | 構造化OSINTの被害国フィールドでAPT39の標的・被害国としてヨルダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでAPT39の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | アジア | MITRE ATT&CKのGroup概要でAPT39の標的範囲としてアジアが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | アフリカ | MITRE ATT&CKのGroup概要でAPT39の標的範囲としてアフリカが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 中東 | 構造化OSINTの被害地域フィールドでAPT39の標的範囲として中東が記録されている。 | 不明 | 不明 | 中 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | 全世界 | レビュー済みアクターマッピングの標的欄に記録された全世界を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 北米 | MITRE ATT&CKのGroup概要でAPT39の標的範囲として北米が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 欧州 | MITRE ATT&CKのGroup概要でAPT39の標的範囲として欧州が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| sectors | 医療・ヘルスケア | [APT39](https://attack.mitre.org/groups/G0087) has primarily targeted the travel, hospitality, academic, and telecommunications industries in Iran and across Asia, Africa, Europe, and North America to track individuals and entities considered to be a threat by the MOIS.(Citation: FireEye APT39 Jan 2019)(Citation: Symantec Chafer Dec 2015)(Citation: FBI FLASH APT39 September 2020)(Citation: Dept. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 情報通信 | [APT39](https://attack.mitre.org/groups/G0087) has primarily targeted the travel, hospitality, academic, and telecommunications industries in Iran and across Asia, Africa, Europe, and North America to track individuals and entities considered to be a threat by the MOIS.(Citation: FireEye APT39 Jan 2019)(Citation: Symantec Chafer Dec 2015)(Citation: FBI FLASH APT39 September 2020)(Citation: Dept. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 小売・ホスピタリティ | [APT39](https://attack.mitre.org/groups/G0087) has primarily targeted the travel, hospitality, academic, and telecommunications industries in Iran and across Asia, Africa, Europe, and North America to track individuals and entities considered to be a threat by the MOIS.(Citation: FireEye APT39 Jan 2019)(Citation: Symantec Chafer Dec 2015)(Citation: FBI FLASH APT39 September 2020)(Citation: Dept. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 教育・研究 | [APT39](https://attack.mitre.org/groups/G0087) has primarily targeted the travel, hospitality, academic, and telecommunications industries in Iran and across Asia, Africa, Europe, and North America to track individuals and entities considered to be a threat by the MOIS.(Citation: FireEye APT39 Jan 2019)(Citation: Symantec Chafer Dec 2015)(Citation: FBI FLASH APT39 September 2020)(Citation: Dept. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003 | OS Credential Dumping | [APT39](https://attack.mitre.org/groups/G0087) has used different versions of Mimikatz to obtain credentials.(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | [APT39](https://attack.mitre.org/groups/G0087) has used Mimikatz, Windows Credential Editor and ProcDump to dump credentials.(Citation: FireEye APT39 Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [APT39](https://attack.mitre.org/groups/G0087) has used various tools to steal files from the compromised host.(Citation: Symantec Chafer February 2018)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | [APT39](https://attack.mitre.org/groups/G0087) has used various strains of malware to query the Registry.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [APT39](https://attack.mitre.org/groups/G0087) has used [NBTscan](https://attack.mitre.org/software/S0590) and custom tools to discover remote systems.(Citation: FireEye APT39 Jan 2019)(Citation: BitDefender Chafer May 2020)(Citation: Symantec Chafer February 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [APT39](https://attack.mitre.org/groups/G0087) has been seen using RDP for lateral movement and persistence, in some cases employing the rdpwinst tool for mangement of multiple sessions.(Citation: FireEye APT39 Jan 2019)(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [APT39](https://attack.mitre.org/groups/G0087) has used SMB for lateral movement.(Citation: Symantec Chafer February 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [APT39](https://attack.mitre.org/groups/G0087) used secure shell (SSH) to move laterally among their targets.(Citation: FireEye APT39 Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | [APT39](https://attack.mitre.org/groups/G0087) has packed tools with UPX, and has repacked a modified version of [Mimikatz](https://attack.mitre.org/software/S0002) to thwart anti-virus detection.(Citation: FireEye APT39 Jan 2019)(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [APT39](https://attack.mitre.org/groups/G0087) has used malware to drop encrypted CAB files.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [APT39](https://attack.mitre.org/groups/G0087) used [Remexi](https://attack.mitre.org/software/S0375) to collect usernames from the system.(Citation: Symantec Chafer Dec 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [APT39](https://attack.mitre.org/groups/G0087) has used malware disguised as Mozilla Firefox and a tool named mfevtpse.exe to proxy C2 communications, closely mimicking a legitimate McAfee file mfevtps.exe.(Citation: BitDefender Chafer May 2020)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [APT39](https://attack.mitre.org/groups/G0087) has exfiltrated stolen victim data through C2 communications.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [APT39](https://attack.mitre.org/groups/G0087) has used [CrackMapExec](https://attack.mitre.org/software/S0488) and a custom port scanner known as BLUETORCH for network scanning.(Citation: FireEye APT39 Jan 2019)(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [APT39](https://attack.mitre.org/groups/G0087) has created scheduled tasks for persistence.(Citation: FireEye APT39 Jan 2019)(Citation: BitDefender Chafer May 2020)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056 | Input Capture | [APT39](https://attack.mitre.org/groups/G0087) has utilized tools to capture mouse movements.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [APT39](https://attack.mitre.org/groups/G0087) has used tools for capturing keystrokes.(Citation: Symantec Chafer February 2018)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | [APT39](https://attack.mitre.org/groups/G0087) has utilized custom scripts to perform internal reconnaissance.(Citation: FireEye APT39 Jan 2019)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [APT39](https://attack.mitre.org/groups/G0087) has used PowerShell to execute malicious code.(Citation: BitDefender Chafer May 2020)(Citation: Symantec Chafer February 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [APT39](https://attack.mitre.org/groups/G0087) has utilized malicious VBS scripts in malware.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | [APT39](https://attack.mitre.org/groups/G0087) has used a command line utility and a network scanner written in python.(Citation: BitDefender Chafer May 2020)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.010 | AutoHotKey & AutoIT | [APT39](https://attack.mitre.org/groups/G0087) has utilized AutoIt malware scripts embedded in Microsoft Office documents or malicious links.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [APT39](https://attack.mitre.org/groups/G0087) has used malware to delete files after they are deployed on a compromised host.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [APT39](https://attack.mitre.org/groups/G0087) has used HTTP in communications with C2.(Citation: BitDefender Chafer May 2020)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | [APT39](https://attack.mitre.org/groups/G0087) has used remote access tools that leverage DNS in communications with C2.(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [APT39](https://attack.mitre.org/groups/G0087) has utilized tools to aggregate data prior to exfiltration.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [APT39](https://attack.mitre.org/groups/G0087) has used stolen credentials to compromise Outlook Web Access (OWA).(Citation: FireEye APT39 Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [APT39](https://attack.mitre.org/groups/G0087) has used tools with the ability to search for files on a compromised host.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.001 | Internal Proxy | [APT39](https://attack.mitre.org/groups/G0087) used custom tools to create SOCK5 and custom protocol proxies between infected hosts.(Citation: FireEye APT39 Jan 2019)(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.002 | External Proxy | [APT39](https://attack.mitre.org/groups/G0087) has used various tools to proxy C2 communications.(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | [APT39](https://attack.mitre.org/groups/G0087) has communicated with C2 through files uploaded to and downloaded from DropBox.(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [APT39](https://attack.mitre.org/groups/G0087) has downloaded tools to compromised hosts.(Citation: Symantec Chafer February 2018)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | [APT39](https://attack.mitre.org/groups/G0087) has used Ncrack to reveal credentials.(Citation: FireEye APT39 Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [APT39](https://attack.mitre.org/groups/G0087) has used a screen capture utility to take screenshots on a compromised host.(Citation: Symantec Chafer February 2018)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1115 | Clipboard Data | [APT39](https://attack.mitre.org/groups/G0087) has used tools capable of stealing contents of the clipboard.(Citation: Symantec Chafer February 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | [APT39](https://attack.mitre.org/groups/G0087) has used the post exploitation tool [CrackMapExec](https://attack.mitre.org/software/S0488) to enumerate network shares.(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.001 | Local Account | [APT39](https://attack.mitre.org/groups/G0087) has created accounts on multiple compromised hosts to perform actions within the network.(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [APT39](https://attack.mitre.org/groups/G0087) has used malware to decrypt encrypted CAB files.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [APT39](https://attack.mitre.org/groups/G0087) has used SQL injection for initial compromise.(Citation: Symantec Chafer February 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Stealth | T1197 | BITS Jobs | [APT39](https://attack.mitre.org/groups/G0087) has used the BITS protocol to exfiltrate stolen data from a compromised host.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [APT39](https://attack.mitre.org/groups/G0087) has sent spearphishing emails in an attempt to lure users to click on a malicious link.(Citation: FireEye APT39 Jan 2019)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [APT39](https://attack.mitre.org/groups/G0087) has sent spearphishing emails in an attempt to lure users to click on a malicious attachment.(Citation: FireEye APT39 Jan 2019)(Citation: BitDefender Chafer May 2020)(Citation: Symantec Chafer February 2018)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [APT39](https://attack.mitre.org/groups/G0087) has installed ANTAK and ASPXSPY web shells.(Citation: FireEye APT39 Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.010 | AppInit DLLs | [APT39](https://attack.mitre.org/groups/G0087) has used malware to set <code>LoadAppInit_DLLs</code> in the Registry key <code>SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows</code> in order to establish persistence.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [APT39](https://attack.mitre.org/groups/G0087) has maintained persistence using the startup folder.(Citation: FireEye APT39 Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.009 | Shortcut Modification | [APT39](https://attack.mitre.org/groups/G0087) has modified LNK shortcuts.(Citation: FireEye APT39 Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.006 | Code Signing Policy Modification | [APT39](https://attack.mitre.org/groups/G0087) has used malware to turn off the <code>RequireSigned</code> feature which ensures only signed DLLs can be run on Windows.(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555 | Credentials from Password Stores | [APT39](https://attack.mitre.org/groups/G0087) has used the Smartftp Password Decryptor tool to decrypt FTP passwords.(Citation: BitDefender Chafer May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [APT39](https://attack.mitre.org/groups/G0087) has used WinRAR and 7-Zip to compress an archive stolen data.(Citation: FireEye APT39 Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [APT39](https://attack.mitre.org/groups/G0087) leveraged spearphishing emails with malicious attachments to initially compromise victims.(Citation: FireEye APT39 Jan 2019)(Citation: Symantec Chafer February 2018)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [APT39](https://attack.mitre.org/groups/G0087) leveraged spearphishing emails with malicious links to initially compromise victims.(Citation: FireEye APT39 Jan 2019)(Citation: FBI FLASH APT39 September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | [APT39](https://attack.mitre.org/groups/G0087) has used post-exploitation tools including RemCom and the Non-sucking Service Manager (NSSM) to execute processes.(Citation: BitDefender Chafer May 2020)(Citation: Symantec Chafer February 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [APT39](https://attack.mitre.org/groups/G0087) has modified and used customized versions of publicly-available tools like PLINK and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: BitDefender Chafer May 2020)(Citation: IBM ITG07 June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--apt39--47a36781b9d1e163 | README |  | 不明 | Chafer-APT39/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
