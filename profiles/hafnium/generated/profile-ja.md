# HAFNIUM 脅威アクタープロファイル

- プロファイルID: `actor--hafnium`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

HAFNIUMの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **HAFNIUM**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Operation Exchange Marauder | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Silk Typhoon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC2639, UNC2640, UNC2643 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Ant | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 101; mapping requires review. |

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
| Adversary | [HAFNIUM](https://attack.mitre.org/groups/G0125) is a likely state-sponsored cyber espionage group operating out of China that has been active since at least January 2021. [HAFNIUM](https://attack.mitre.org/groups/G0125) primarily targets entities in the US across a number of industry sectors, including infectious disease researchers, law firms, higher education institutions, defense contractors, policy think tanks, and NGOs. [HAFNIUM](https://attack.mitre.org/groups/G0125) has targeted remote management tools and cloud software for intial access and has demonstrated an ability to quickly operationalize exploits for identified vulnerabilities in edge devices.(Citation: Microsoft HAFNIUM March 2020)(Citation: Volexity Exchange Marauder March 2021)(Citation: Microsoft Silk Typhoon MAR 2025) |
| Capability | ASPXSpy, China Chopper, Tarrask, Procdump, 7-Zip, Nishang, PowerCat, Covenant, Impacket, PsExec |
| Infrastructure |  |
| Victim | Microsoft Exchange Server |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Hafnium | canonical-name | 高 | China | https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/<br>https://therecord.media/white-house-formally-blames-chinas-ministry-of-state-security-for-microsoft-exchange-hack/<br>https://www.dropbox.com/s/dwiygk49pos4vqx/Whitepaper%204%20MS%20Exchange%200-days.pdf?dl=0 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Silk Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | HAFNIUM | canonical-name | 高 | CN | https://attack.mitre.org/groups/G0125/<br>https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers<br>https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/ |
| misp-microsoft-activity-group | HAFNIUM | canonical-name | 高 |  | https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/ |
| misp-microsoft-activity-group | Silk Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | HAFNIUM - G0125 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0125<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/ |
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
| malware--7-zip | 7-Zip | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--aspxspy | ASPXSpy | [ASPXSpy](https://attack.mitre.org/software/S0073) is a Web shell. It has been modified by [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors to create the ASPXTool version. (Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--china-chopper | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.(Citation: Lee 2013) It has been used by several threat groups.(Citation: Dell TG-3390)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Rapid7 HAFNIUM Mar 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--nishang | Nishang | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--powercat | PowerCat | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--procdump | Procdump | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--tarrask | Tarrask | [Tarrask](https://attack.mitre.org/software/S1011) is malware that has been used by [HAFNIUM](https://attack.mitre.org/groups/G0125) since at least August 2021. [Tarrask](https://attack.mitre.org/software/S1011) was designed to evade digital defenses and maintain persistence by generating concealed scheduled tasks.(Citation: Tarrask scheduled task) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--covenant | Covenant | [Covenant](https://attack.mitre.org/software/S1155) is a multi-platform command and control framework written in .NET. While designed for penetration testing and security research, the tool has also been used by threat actors such as [HAFNIUM](https://attack.mitre.org/groups/G0125) during operations. [Covenant](https://attack.mitre.org/software/S1155) functions through a central listener managing multiple deployed "Grunts" that communicate back to the controller.(Citation: Github Covenant)(Citation: Microsoft HAFNIUM March 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Murky Pandaハッカー、クラウドの信頼関係を悪用して下流の顧客環境を侵害 | malware-campaign | 不明 | 不明 | 2025-08-23 |  | malware--china-chopper |  | victim--activity-rule--ab17a374efa3597bd312 | 中国系Murky Panda(Silk Typhoon/Hafnium)がクラウドの信頼関係を悪用し侵入。 SaaS/CSP侵害とEntra ID SecretやDAP権限を用いダウンストリーム顧客へ横展開。 メール/アプリ閲覧、バックドア作成、権限昇格で持続的アクセスと機密データを窃取。 初期侵入にCVE-2023-3519やCVE-2025-0282、ExchangeのProxyLogon等を悪用。 Neo-reGeorg/China ChopperといったOSSのWebShellやCloudedHopeというカスタムマルウェアを使用、SOHOプロキシを使って悪意のある通信を正規通信で隠す。 | 中 | `source--daily-befd567d8c384fdf1dc2` |
| Operation Exchange Marauder | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Operation Exchange Marauder

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | [HAFNIUM](https://attack.mitre.org/groups/G0125) primarily targets entities in the US across a number of industry sectors, including infectious disease researchers, law firms, higher education institutions, defense contractors, policy think tanks, and NGOs. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 全世界 | 構造化OSINTの被害地域フィールドでHAFNIUMの標的範囲として全世界が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | 防衛・軍事 | [HAFNIUM](https://attack.mitre.org/groups/G0125) primarily targets entities in the US across a number of industry sectors, including infectious disease researchers, law firms, higher education institutions, defense contractors, policy think tanks, and NGOs. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 非営利・市民社会 | [HAFNIUM](https://attack.mitre.org/groups/G0125) primarily targets entities in the US across a number of industry sectors, including infectious disease researchers, law firms, higher education institutions, defense contractors, policy think tanks, and NGOs. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 教育・研究 | [HAFNIUM](https://attack.mitre.org/groups/G0125) primarily targets entities in the US across a number of industry sectors, including infectious disease researchers, law firms, higher education institutions, defense contractors, policy think tanks, and NGOs. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 法律 | [HAFNIUM](https://attack.mitre.org/groups/G0125) primarily targets entities in the US across a number of industry sectors, including infectious disease researchers, law firms, higher education institutions, defense contractors, policy think tanks, and NGOs. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Murky Pandaハッカー、クラウドの信頼関係を悪用して下流の顧客環境を侵害 | 非公開 | anonymous | unknown | reported |  | malware--china-chopper |  | メール／メールアカウント, クラウド／SaaS | data-theft: メール/アプリ閲覧、バックドア作成、権限昇格で持続的アクセスと機密データを窃取。 | 不明 | 不明 | 2025-08-23 | 中 | `source--daily-befd567d8c384fdf1dc2` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used <code>procdump</code> to dump the LSASS process memory.(Citation: Microsoft HAFNIUM March 2020)(Citation: Volexity Exchange Marauder March 2021)(Citation: Rapid7 HAFNIUM Mar 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.003 | NTDS | [HAFNIUM](https://attack.mitre.org/groups/G0125) has stolen copies of the Active Directory database (NTDS.DIT).(Citation: Volexity Exchange Marauder March 2021)(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [HAFNIUM](https://attack.mitre.org/groups/G0125) has collected data and files from a compromised machine.(Citation: Rapid7 HAFNIUM Mar 2021)(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has collected IP information via IPInfo.(Citation: Rapid7 HAFNIUM Mar 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016.001 | Internet Connection Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has checked for network connectivity from a compromised host using `ping`, including attempts to contact `google[.]com`.(Citation: Rapid7 HAFNIUM Mar 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has enumerated domain controllers using `net group "Domain computers"` and `nltest /dclist`.(Citation: Rapid7 HAFNIUM Mar 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `whoami` to gather user information.(Citation: Rapid7 HAFNIUM Mar 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `tasklist` to enumerate processes.(Citation: Rapid7 HAFNIUM Mar 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used the Exchange Power Shell module <code>Set-OabVirtualDirectoryPowerShell</code> to export mailbox data.(Citation: Microsoft HAFNIUM March 2020)(Citation: Volexity Exchange Marauder March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `cmd.exe` to execute commands on the victim's machine.(Citation: Rapid7 HAFNIUM Mar 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [HAFNIUM](https://attack.mitre.org/groups/G0125) has targeted unpatched applications to elevate access in targeted organizations.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used open-source C2 frameworks, including [Covenant](https://attack.mitre.org/software/S1155).(Citation: Microsoft HAFNIUM March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used the NT AUTHORITY\SYSTEM account to create files on Exchange servers.(Citation: FireEye Exchange Zero Days March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.004 | Cloud Accounts | [HAFNIUM](https://attack.mitre.org/groups/G0125) has abused service principals in compromised environments to enable data exfiltration.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [HAFNIUM](https://attack.mitre.org/groups/G0125) has searched file contents on a compromised host.(Citation: Rapid7 HAFNIUM Mar 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1095 | Non-Application Layer Protocol | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used TCP for C2.(Citation: Microsoft HAFNIUM March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098 | Account Manipulation | [HAFNIUM](https://attack.mitre.org/groups/G0125) has granted privileges to domain accounts and reset the password for default admin accounts.(Citation: Volexity Exchange Marauder March 2021)(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [HAFNIUM](https://attack.mitre.org/groups/G0125) has downloaded malware and tools--including Nishang and PowerCat--onto a compromised host.(Citation: Microsoft HAFNIUM March 2020)(Citation: Rapid7 HAFNIUM Mar 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.003 | Password Spraying | [HAFNIUM](https://attack.mitre.org/groups/G0125) has gained initial access through password spray attacks.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.002 | Remote Email Collection | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used web shells and MSGraph to export mailbox data.(Citation: Microsoft HAFNIUM March 2020)(Citation: Volexity Exchange Marauder March 2021)(Citation: Microsoft Silk Typhoon MAR 2025)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used MSGraph to exfiltrate data from email, OneDrive, and SharePoint.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used ASCII encoding for C2 traffic.(Citation: Microsoft HAFNIUM March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.002 | Domain Account | [HAFNIUM](https://attack.mitre.org/groups/G0125) has created domain accounts.(Citation: Volexity Exchange Marauder March 2021)(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [HAFNIUM](https://attack.mitre.org/groups/G0125) has exploited multiple vulnerabilities to compromise edge devices and on-premises versions of Microsoft Exchange Server.(Citation: Microsoft HAFNIUM March 2020)(Citation: Volexity Exchange Marauder March 2021)(Citation: FireEye Exchange Zero Days March 2021)(Citation: Tarrask scheduled task)(Citation: Microsoft Log4j Vulnerability Exploitation December 2021)(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used stolen API keys and credentials associated with privilege access management (PAM), cloud app providers, and cloud data management companies to access downstream customer environments.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.002 | Sharepoint | [HAFNIUM](https://attack.mitre.org/groups/G0125) has abused compromised credentials to exfiltrate data from SharePoint.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used <code>rundll32</code> to load malicious DLLs.(Citation: Volexity Exchange Marauder March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [HAFNIUM](https://attack.mitre.org/groups/G0125) has deployed multiple web shells on compromised servers including SIMPLESEESHARP, SPORTSBALL, [China Chopper](https://attack.mitre.org/software/S0020), and [ASPXSpy](https://attack.mitre.org/software/S0073).(Citation: Microsoft HAFNIUM March 2020)(Citation: Volexity Exchange Marauder March 2021)(Citation: FireEye Exchange Zero Days March 2021)(Citation: Tarrask scheduled task)(Citation: Rapid7 HAFNIUM Mar 2021)(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1530 | Data from Cloud Storage | [HAFNIUM](https://attack.mitre.org/groups/G0125) has exfitrated data from OneDrive.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.001 | Application Access Token | [HAFNIUM](https://attack.mitre.org/groups/G0125) has abused service principals with administrative permissions for data exfiltration.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.006 | Cloud Secrets Management Stores | [HAFNIUM](https://attack.mitre.org/groups/G0125) has moved laterally from on-premises environments to steal passwords from Azure key vaults.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used 7-Zip and WinRAR to compress stolen files for exfiltration.(Citation: Microsoft HAFNIUM March 2020)(Citation: Volexity Exchange Marauder March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | [HAFNIUM](https://attack.mitre.org/groups/G0125) has hidden files on a compromised host.(Citation: Rapid7 HAFNIUM Mar 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [HAFNIUM](https://attack.mitre.org/groups/G0125) has exfiltrated data to file sharing sites, including MEGA.(Citation: Microsoft HAFNIUM March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [HAFNIUM](https://attack.mitre.org/groups/G0125) has operated from leased virtual private servers (VPS) in the United States.(Citation: Microsoft HAFNIUM March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.005 | Botnet | [HAFNIUM](https://attack.mitre.org/groups/G0125) has incorporated leased devices into covert networks to obfuscate communications.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | [HAFNIUM](https://attack.mitre.org/groups/G0125) has acquired web services for use in C2 and exfiltration.(Citation: Microsoft HAFNIUM March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.005 | Botnet | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used compromised devices in covert networks to obfuscate communications.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | [HAFNIUM](https://attack.mitre.org/groups/G0125) has collected e-mail addresses for users they intended to target.(Citation: Volexity Exchange Marauder March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1590 | Gather Victim Network Information | [HAFNIUM](https://attack.mitre.org/groups/G0125) gathered the fully qualified domain names (FQDNs) for targeted Exchange servers in the victim's environment.(Citation: Volexity Exchange Marauder March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1590.005 | IP Addresses | [HAFNIUM](https://attack.mitre.org/groups/G0125) has obtained IP addresses for publicly-accessible Exchange servers.(Citation: Volexity Exchange Marauder March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1592.004 | Client Configurations | [HAFNIUM](https://attack.mitre.org/groups/G0125) has interacted with Office 365 tenants to gather details regarding target's environments.(Citation: Microsoft HAFNIUM March 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1593.003 | Code Repositories | [HAFNIUM](https://attack.mitre.org/groups/G0125) has discovered leaked corporate credentials on public repositories including GitHub.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | [HAFNIUM](https://attack.mitre.org/groups/G0125) has cleared actor-performed actions from logs.(Citation: Microsoft Silk Typhoon MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 34件（`artifacts.csv`）

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
| source--daily-befd567d8c384fdf1dc2 | Murky Pandaハッカー、クラウドの信頼関係を悪用して下流の顧客環境を侵害 | bleepingcomputer.com | 2025-08-23 | https://www.bleepingcomputer.com/news/security/murky-panda-hackers-exploit-cloud-trust-to-hack-downstream-customers/ | osint-report | TLP:CLEAR | 中 |
| source--hafnium--0fa00884982af997 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--hafnium--3532d1fb659445f1 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--hafnium--3fdc327cb5d16fed | CTA 2024 Olympics Threat Assessment Supplemental Report Combined rev |  | 2024 | summary/2024/CTA-2024-Olympics-Threat-Assessment-Supplemental-Report_Combined_rev.pdf | report | TLP:CLEAR | 中 |
| source--hafnium--70e82760d1928ebd | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--hafnium--7122a0188e5840d0 | 2021 Vulnerability Landscape |  | 2021 | summary/2022/2021 Vulnerability Landscape.pdf | report | TLP:CLEAR | 中 |
| source--hafnium--80036084081d2ade | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--hafnium--84acd50c1375a028 | hafnium |  | 不明 | actor_profile/evidence/hafnium.csv | structured-data | TLP:CLEAR | 中 |
| source--hafnium--8bb6cd85fa946d5e | sophos 2022 threat report |  | 2022 | summary/2022/sophos-2022-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--hafnium--91c7d8b6dc2425e4 | 2021(APT) Microsoft Digital Defense Report |  | 2021 | summary/2021/2021(APT) Microsoft Digital Defense Report.pdf | report | TLP:CLEAR | 中 |
| source--hafnium--bf80f3c9bc1190e8 | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--hafnium--d110d7cfc0eb63b6 | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
