# Storm-1811 脅威アクタープロファイル

- プロファイルID: `actor--storm-1811`
- 状態: draft
- 更新日時: 2026-07-29T15:36:11Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Storm-1811の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Storm-1811**
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

未評価

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Storm-1811](https://attack.mitre.org/groups/G1046) is a financially-motivated entity linked to [Black Basta](https://attack.mitre.org/software/S1070) ransomware deployment. [Storm-1811](https://attack.mitre.org/groups/G1046) is notable for unique phishing and social engineering mechanisms for initial access, such as overloading victim email inboxes with non-malicious spam to prompt a fake "help desk" interaction leading to the deployment of adversary tools and capabilities.(Citation: Microsoft Storm-1811 2024)(Citation: rapid7-email-bombing)(Citation: RedCanary Storm-1811 2024)(Citation: RedCanary June Insights 2024) |
| Capability | Black Basta, Cobalt Strike, QakBot, Impacket, BITSAdmin, Quick Assist, PsExec |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-1811 | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | UNC4393 | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/unc4393-goes-gently-into-silentnight<br>https://www.security.com/threat-intelligence/black-basta-ransomware-zero-day<br>https://cloud.google.com/blog/topics/threat-intelligence/detecting-disrupting-malvertising-backdoors/ |
| misp-microsoft-activity-group | Storm-1811 | canonical-name | 高 |  | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Storm-1811 - G1046 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1046<br>https://redcanary.com/blog/threat-intelligence/intelligence-insights-june-2024/<br>https://redcanary.com/blog/threat-intelligence/storm-1811-black-basta/ |
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
| malware--black-basta | Black Basta | [Black Basta](https://attack.mitre.org/software/S1070) is ransomware written in C++ that has been offered within the ransomware-as-a-service (RaaS) model since at least April 2022; there are variants that target Windows and VMWare ESXi servers. [Black Basta](https://attack.mitre.org/software/S1070) operations have included the double extortion technique where in addition to demanding ransom for decrypting the files of targeted organizations the cyber actors also threaten to post sensitive information to a leak site if the ransom is not paid. [Black Basta](https://attack.mitre.org/software/S1070) affiliates have targeted multiple high-value organizations, with the largest number of victims based in the U.S. Based on similarities in TTPs, leak sites, payment sites, and negotiation tactics, security researchers assess the [Black Basta](https://attack.mitre.org/software/S1070) RaaS operators could include current or former members of the [Conti](https://attack.mitre.org/software/S0575) group.(Citation: Palo Alto Networks Black Basta August 2022)(Citation: Deep Instinct Black Basta August 2022)(Citation: Minerva Labs Black Basta May 2022)(Citation: Avertium Black Basta June 2022)(Citation: NCC Group Black Basta June 2022)(Citation: Cyble Black Basta May 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--qakbot | QakBot | [QakBot](https://attack.mitre.org/software/S0650) is a modular banking trojan that has been used primarily by financially-motivated actors since at least 2007. [QakBot](https://attack.mitre.org/software/S0650) is continuously maintained and developed and has evolved from an information stealer into a delivery agent for ransomware, most notably [ProLock](https://attack.mitre.org/software/S0654) and [Egregor](https://attack.mitre.org/software/S0554).(Citation: Trend Micro Qakbot December 2020)(Citation: Red Canary Qbot)(Citation: Kaspersky QakBot September 2021)(Citation: ATT QakBot April 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--bitsadmin | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--quick-assist | Quick Assist | [Quick Assist](https://attack.mitre.org/software/S1209) is a remote assistance tool primarily for Microsoft Windows, although a macOS version also exists. [Quick Assist](https://attack.mitre.org/software/S1209) allows for remote screen sharing and, with end user approval, remote control and command execution on the enabling device.(Citation: Microsoft Storm-1811 2024)(Citation: Microsoft Quick Assist 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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
| Windows Quick Assistを悪用したBlack Bastaランサムウェア攻撃 | ransomware-extortion | 不明 | 不明 | 2024-05-16 | target--mitre-group--sector--6ace32369b881a0c4d24 | malware--black-basta | ttp--activity-rule--d7c3d4655179616e68af | victim--activity-rule--4510836a063ad9eed051 | Black Bastaランサムウェアを使う脅威アクター(Storm-1811)がWindows Quick Assistを悪用 攻撃者はソーシャルエンジニアリングで被害者のネットワークを侵入 大量のスパムメールを送信後、Microsoftサポートを装って電話をかけ、ソーシャルエンジニアリングでアクセス許可を騙し取る マルウェアや悪意のあるバッチファイルをダウンロード MicrosoftはQuick Assistの使用を見直すよう呼びかけ | 中 | `source--daily-1ba1d9f38d8366b3c0a3` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 製造・産業 | [Storm-1811](https://attack.mitre.org/groups/G1046) is notable for unique phishing and social engineering mechanisms for initial access, such as overloading victim email inboxes with non-malicious spam to prompt a fake "help desk" interaction leading to the deployment of adversary tools and capabilities.(Citation: Microsoft Storm-1811 2024)(Citation: rapid7-email | 不明 | 不明 | 高 | `source--daily-1ba1d9f38d8366b3c0a3`, `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Windows Quick Assistを悪用したBlack Bastaランサムウェア攻撃 | 非公開 | aggregate | multiple-organizations | reported | target--mitre-group--sector--6ace32369b881a0c4d24 | malware--black-basta | ttp--activity-rule--d7c3d4655179616e68af | メール／メールアカウント | encryption: Windows Quick Assistを悪用したBlack Bastaランサムウェア攻撃 | 不明 | 不明 | 2024-05-16 | 中 | `source--daily-1ba1d9f38d8366b3c0a3` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.003 | Windows Command Shell | Black Bastaランサムウェアを使う脅威アクター(Storm-1811)がWindows Quick Assistを悪用 攻撃者はソーシャルエンジニアリングで被害者のネットワークを侵入 大量のスパムメールを送信後、Microsoftサポートを装って電話をかけ、ソーシャルエンジニアリングでアクセス許可を騙し取る マルウェアや悪意のあるバッチファイルをダウンロード MicrosoftはQuick Assistの使用を見直すよう呼びかけ | malware--black-basta | activity--daily-34b52b95ce7e51038b32 | 不明 | 不明 | 中 | `source--daily-1ba1d9f38d8366b3c0a3` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [Storm-1811](https://attack.mitre.org/groups/G1046) has attempted to move laterally in victim environments via SMB using [Impacket](https://attack.mitre.org/software/S0357).(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [Storm-1811](https://attack.mitre.org/groups/G1046) has used OpenSSH to establish an SSH tunnel to victims for persistent access.(Citation: Microsoft Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Storm-1811](https://attack.mitre.org/groups/G1046) XOR encodes a [Cobalt Strike](https://attack.mitre.org/software/S0154) installation payload in a DLL file that is decoded with a hardcoded key when called by a legitimate 7zip installation process.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [Storm-1811](https://attack.mitre.org/groups/G1046) has used `whoami.exe` to determine if the active user on a compromised system is an administrator.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [Storm-1811](https://attack.mitre.org/groups/G1046) has prompted users to download and execute batch scripts that masquerade as legitimate update files during initial access and social engineering operations.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Storm-1811](https://attack.mitre.org/groups/G1046) has disguised [Cobalt Strike](https://attack.mitre.org/software/S0154) installers as a malicious DLL masquerading as part of a legitimate 7zip installation package.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.010 | Masquerade Account Name | [Storm-1811](https://attack.mitre.org/groups/G1046) has created Microsoft Teams accounts that spoof IT support and helpdesk members for use in application and voice phishing.(Citation: Microsoft Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.002 | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [Storm-1811](https://attack.mitre.org/groups/G1046) has exfiltrated captured user credentials via Secure Copy Protocol (SCP).(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056 | Input Capture | [Storm-1811](https://attack.mitre.org/groups/G1046) has used a PowerShell script to capture user credentials after prompting a user to authenticate to run a malicious script masquerading as a legitimate update item.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Storm-1811](https://attack.mitre.org/groups/G1046) has used PowerShell for multiple purposes, such as using PowerShell scripts executing in an infinite loop to create an SSH connection to a command and control server.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Storm-1811](https://attack.mitre.org/groups/G1046) has used multiple batch scripts during initial access and subsequent actions on victim machines.(Citation: Microsoft Storm-1811 2024)(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [Storm-1811](https://attack.mitre.org/groups/G1046) has locally staged captured credentials for subsequent manual exfiltration.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [Storm-1811](https://attack.mitre.org/groups/G1046) has performed domain account enumeration during intrusions.(Citation: Microsoft Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Storm-1811](https://attack.mitre.org/groups/G1046) has used scripted `cURL` commands, [BITSAdmin](https://attack.mitre.org/software/S0190), and other mechanisms to retrieve follow-on batch scripts and tools for execution on victim devices.(Citation: Microsoft Storm-1811 2024)(Citation: rapid7-email-bombing)(Citation: RedCanary June Insights 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Storm-1811](https://attack.mitre.org/groups/G1046) has distributed password-protected archives such as ZIP files during intrusions.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Storm-1811](https://attack.mitre.org/groups/G1046) has prompted users to execute downloaded software and payloads as the result of social engineering activity.(Citation: Microsoft Storm-1811 2024)(Citation: rapid7-email-bombing)(Citation: RedCanary Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219.002 | Remote Desktop Software | [Storm-1811](https://attack.mitre.org/groups/G1046) has abused multiple types of legitimate remote access software and tools, such as ScreenConnect, NetSupport Manager, and AnyDesk.(Citation: Microsoft Storm-1811 2024)(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1222.001 | Windows Permissions | [Storm-1811](https://attack.mitre.org/groups/G1046) has used `cacls.exe` via batch script to modify file and directory permissions in victim environments.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | [Storm-1811](https://attack.mitre.org/groups/G1046) has enumerated domain accounts and access during intrusions.(Citation: Microsoft Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | [Storm-1811](https://attack.mitre.org/groups/G1046) is a financially-motivated entity linked to the deployment of [Black Basta](https://attack.mitre.org/software/S1070) ransomware in victim environments.(Citation: Microsoft Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Storm-1811](https://attack.mitre.org/groups/G1046) has created Windows Registry Run keys that execute various batch scripts to establish persistence on victim devices.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [Storm-1811](https://attack.mitre.org/groups/G1046) has distributed malicious links to victims that redirect to EvilProxy-based phishing sites to harvest credentials.(Citation: Microsoft Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.003 | Spearphishing via Service | [Storm-1811](https://attack.mitre.org/groups/G1046) has used Microsoft Teams to send messages and initiate voice calls to victims posing as IT support personnel.(Citation: Microsoft Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.004 | Spearphishing Voice | [Storm-1811](https://attack.mitre.org/groups/G1046) has initiated voice calls with victims posing as IT support to prompt users to download and execute scripts and other tools for initial access.(Citation: Microsoft Storm-1811 2024)(Citation: rapid7-email-bombing)(Citation: RedCanary Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [Storm-1811](https://attack.mitre.org/groups/G1046) has used the [Impacket](https://attack.mitre.org/software/S0357) toolset to move and remotely execute payloads to other hosts in victim networks.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [Storm-1811](https://attack.mitre.org/groups/G1046) has deployed a malicious DLL (7z.DLL) that is sideloaded by a modified, legitimate installer (7zG.exe) when that installer is executed with an additional command line parameter of `b` at runtime to load a [Cobalt Strike](https://attack.mitre.org/software/S0154) beacon payload.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [Storm-1811](https://attack.mitre.org/groups/G1046) has created domains for use with RMM tools.(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.003 | Cloud Accounts | [Storm-1811](https://attack.mitre.org/groups/G1046) has created malicious accounts to enable activity via Microsoft Teams, typically spoofing various IT support and helpdesk themes.(Citation: Microsoft Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Storm-1811](https://attack.mitre.org/groups/G1046) acquired various legitimate and malicious tools, such as RMM software and commodity malware packages, for operations.(Citation: Microsoft Storm-1811 2024)(Citation: rapid7-email-bombing) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1667 | Email Bombing | [Storm-1811](https://attack.mitre.org/groups/G1046) has deployed large volumes of non-malicious email spam to victims in order to prompt follow-on interactions with the threat actor posing as IT support or helpdesk to resolve the problem.(Citation: rapid7-email-bombing)(Citation: RedCanary Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | [Storm-1811](https://attack.mitre.org/groups/G1046) impersonates help desk and IT support personnel for phishing and social engineering purposes during initial access to victim environments.(Citation: Microsoft Storm-1811 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 9件（`artifacts.csv`）

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
| source--daily-1ba1d9f38d8366b3c0a3 | Windows Quick Assistを悪用したBlack Bastaランサムウェア攻撃 | bleepingcomputer.com | 2024-05-16 | https://www.bleepingcomputer.com/news/security/windows-quick-assist-abused-in-black-basta-ransomware-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--storm-1811--6364d1bf145e58a6 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--storm-1811--7187587b3cf12824 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--storm-1811--b047318da9540fcf | storm 1811 |  | 不明 | actor_profile/evidence/storm-1811.csv | structured-data | TLP:CLEAR | 中 |
| source--storm-1811--f48ceffd73aa076f | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
