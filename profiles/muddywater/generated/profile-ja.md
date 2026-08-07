# MuddyWater 脅威アクタープロファイル

- プロファイルID: `actor--muddywater`
- 状態: draft
- 更新日時: 2026-08-07T10:35:26Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

MuddyWaterの標準化プロファイル。リポジトリ内の専用資料5件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **MuddyWater**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Earth Vetala | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| MERCURY | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Mango Sandstorm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| MuddyKrill | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Seedworm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Static Kitten | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA450 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TEMP.Zagros | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Cobalt Ulster | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 19; mapping requires review. |
| SectorD02 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 19; mapping requires review. |

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
| Adversary | [MuddyWater](https://attack.mitre.org/groups/G0069) is a cyber espionage group assessed to be a subordinate element within Iran's Ministry of Intelligence and Security (MOIS).(Citation: CYBERCOM Iranian Intel Cyber January 2022) Since at least 2017, [MuddyWater](https://attack.mitre.org/groups/G0069) has targeted a range of government and private organizations across sectors, including telecommunications, local government, finance, defense, and oil and natural gas organizations, in the Middle East (specifically the UAE and Saudi Arabia), Asia, Africa, Europe, and North America. [MuddyWater](https://attack.mitre.org/groups/G0069) has reused domains dating back to October 2025, and has a preference for NameCheap and Hosterdaddy Private Limited (AS136557). In late 2025 and early 2026, [MuddyWater](https://attack.mitre.org/groups/G0069) used commercial satellite internet (i.e., Starlink) for command and control (C2) communication. (Citation: FalconFeeds_Iran_Mar2026)(Citation: Huntio_IranInfra_Mar2026)(Citation: Unit 42 MuddyWater Nov 2017)(Citation: Symantec MuddyWater Dec 2018)(Citation: ClearSky MuddyWater Nov 2018)(Citation: ClearSky MuddyWater June 2019)(Citation: Reaqta MuddyWater November 2017)(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: Talos MuddyWater Jan 2022)(Citation: NaumaanProofpoint_GlobalClickFix_April2025)(Citation: ESET_MuddyWater_Dec2025)(Citation: SymantecCarbonBlack_Seedworm_Mar2026)    |
| Capability | Tsundere Botnet, RustyWater, SHARPSTATS, MuddyViper, Fooder, Mori, LP-Notes, PowGoop, STARWHALE, POWERSTATS, Small Sieve, PoweMuddy, ScreenConnect, MoriAgent, Pudpoul, Thanos Ransomware, Covicli, RemoteUtilities, PowerSploit, Empire, Rclone, Out1, ConnectWise, Mimikatz, LaZagne, CrackMapExec, Koadic |
| Infrastructure |  |
| Victim | individuals in Asia and the Middle East, government and defense entities in Central and Southwest Asia |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | MuddyWater, Seedworm, TEMP.Zagros, Static Kitten | canonical-name | 高 | Iran | https://reaqta.com/2017/11/muddywater-apt-targeting-middle-east/<br>https://www.symantec.com/blogs/threat-intelligence/seedworm-espionage-group<br>https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Mango Sandstorm | canonical-name | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | MuddyWater | canonical-name | 高 | IR, Iran (Islamic Republic of) | https://unit42.paloaltonetworks.com/unit42-muddying-the-water-targeted-attacks-in-the-middle-east/<br>https://www.cfr.org/interactive/cyber-operations/muddywater<br>https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html |
| misp-microsoft-activity-group | Mango Sandstorm | canonical-name | 高 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | MuddyWater - G0069 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0069<br>https://researchcenter.paloaltonetworks.com/2017/11/unit42-muddying-the-water-targeted-attacks-in-the-middle-east/ |
| misp-mitre-intrusion-set | MuddyWater - G0069 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0069<br>https://blog.cloudflare.com/2026-threat-report/<br>https://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html |
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
| malware--covicli | Covicli | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--fooder | Fooder | [Fooder](https://attack.mitre.org/software/S9033) is a custom 64-bit C/C++ loader used by [MuddyWater](https://attack.mitre.org/groups/G0069) that can decrypt and reflectively load embedded payloads such as a go-socks5 proxy utility, the open-source HackBrowserData infostealer, or the [MuddyViper](https://attack.mitre.org/software/S9032) backdoor. [Fooder](https://attack.mitre.org/software/S9033) has frequently masqueraded as an entertainment executable, such as the Snake game (e.g., `Snake_Game.exe`).(Citation: ESET_MuddyWater_Dec2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lp-notes | LP-Notes | [LP-Notes](https://attack.mitre.org/software/S9036) is a C/C++ Windows credential stealer used by [MuddyWater](https://attack.mitre.org/groups/G0069). [LP-Notes](https://attack.mitre.org/software/S9036) was named after the `lp-notes.txt` file that is used to store stolen credentials.(Citation: ESET_MuddyWater_Dec2025)   | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--mori | Mori | [Mori](https://attack.mitre.org/software/S1047) is a backdoor that has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least January 2022.(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: CYBERCOM Iranian Intel Cyber January 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--moriagent | MoriAgent | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--muddyviper | MuddyViper | [MuddyViper](https://attack.mitre.org/software/S9032) is custom backdoor written in C and C++ used by [MuddyWater](https://attack.mitre.org/groups/G0069) for command and control (C2) communications and persistence. [MuddyViper](https://attack.mitre.org/software/S9032) is loaded by [Fooder](https://attack.mitre.org/software/S9033) and sends frequent messages to the C2 server.(Citation: ESET_MuddyWater_Dec2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--powemuddy | PoweMuddy | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--powerstats | POWERSTATS | [POWERSTATS](https://attack.mitre.org/software/S0223) is a PowerShell-based first stage backdoor used by [MuddyWater](https://attack.mitre.org/groups/G0069). (Citation: Unit 42 MuddyWater Nov 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--powgoop | PowGoop | [PowGoop](https://attack.mitre.org/software/S1046) is a loader that consists of a DLL loader and a PowerShell-based downloader; it has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) as their main loader.(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: CYBERCOM Iranian Intel Cyber January 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pudpoul | Pudpoul | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--rustywater | RustyWater | [RustyWater](https://attack.mitre.org/software/S9037) is a Rust-based implant used by [MuddyWater](https://attack.mitre.org/groups/G0069). Historically, [MuddyWater](https://attack.mitre.org/groups/G0069) has used PowerShell-based tools and [RustyWater](https://attack.mitre.org/software/S9037) reflects a shift in tooling, demonstrating better techniques for defense evasion and reverse engineering.(Citation: CloudSEK_RustyWater_Jan2026) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--screenconnect | ScreenConnect | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sharpstats | SHARPSTATS | [SHARPSTATS](https://attack.mitre.org/software/S0450) is a .NET backdoor used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least 2019.(Citation: TrendMicro POWERSTATS V3 June 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--small-sieve | Small Sieve | [Small Sieve](https://attack.mitre.org/software/S1035) is a Telegram Bot API-based Python backdoor that has been distributed using a Nullsoft Scriptable Install System (NSIS) Installer; it has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least January 2022.(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: NCSC GCHQ Small Sieve Jan 2022)<br><br>Security researchers have also noted [Small Sieve](https://attack.mitre.org/software/S1035)'s use by UNC3313, which may be associated with [MuddyWater](https://attack.mitre.org/groups/G0069).(Citation: Mandiant UNC3313 Feb 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--starwhale | STARWHALE | [STARWHALE](https://attack.mitre.org/software/S1037) is Windows Script File (WSF) backdoor that has been used by [MuddyWater](https://attack.mitre.org/groups/G0069), possibly since at least November 2021; there is also a [STARWHALE](https://attack.mitre.org/software/S1037) variant written in Golang with similar capabilities. Security researchers have also noted the use of [STARWHALE](https://attack.mitre.org/software/S1037) by UNC3313, which may be associated with [MuddyWater](https://attack.mitre.org/groups/G0069).(Citation: Mandiant UNC3313 Feb 2022)(Citation: DHS CISA AA22-055A MuddyWater February 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--thanos-ransomware | Thanos Ransomware | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--tsundere-botnet | Tsundere Botnet | [Tsundere Botnet](https://attack.mitre.org/software/S9034) is a botnet first reported in mid-2025 that is delivered via MSI installer or a PowerShell script. It leverages Node.js and JavaScript for payload delivery and execution, and uses smart contracts on the blockchain to host command and control (C2) addresses. [Tsundere Botnet](https://attack.mitre.org/software/S9034) is attributed to a likely Russian-speaking threat actor.<br><br>A variant named DinDoor has been linked to [MuddyWater](https://attack.mitre.org/groups/G0069) operations and uses the Deno runtime for execution rather than Node.js.(Citation: Checkpoint_MOISCyberCrime_Mar2026)(Citation: SOCRadar_MuddyWaterDindoor_Mar2026)(Citation: CAL_MuddyWater_Mar2026)(Citation: SecureListUbiedo_Tsundere_Nov2025)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--remoteutilities | RemoteUtilities | [RemoteUtilities](https://attack.mitre.org/software/S0592) is a legitimate remote administration tool that has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least 2021 for execution on target machines.(Citation: Trend Micro Muddy Water March 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--powersploit | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--rclone | Rclone | [Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation: DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--out1 | Out1 | [Out1](https://attack.mitre.org/software/S0594) is a remote access tool written in python and used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least 2021.(Citation: Trend Micro Muddy Water March 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--connectwise | ConnectWise | [ConnectWise](https://attack.mitre.org/software/S0591) is a legitimate remote administration tool that has been used since at least 2016 by threat actors including [MuddyWater](https://attack.mitre.org/groups/G0069) and [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) to connect to and conduct lateral movement in target environments.(Citation: Anomali Static Kitten February 2021)(Citation: Trend Micro Muddy Water March 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--crackmapexec | CrackMapExec | [CrackMapExec](https://attack.mitre.org/software/S0488), or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. [CrackMapExec](https://attack.mitre.org/software/S0488) collects Active Directory information to conduct lateral movement through targeted networks.(Citation: CME Github September 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BlackWater | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | phishing-campaign | 不明 | 不明 | 2025-04-18 | target--activity-rule--country--72caf60a2fbce4a1be7a |  | ttp--activity-rule--8a62cee39ddda59204db, ttp--activity-rule--b151f73dbd3a8fe978b9 | victim--activity-rule--2e097805778cd4de90a6 | 中国・イラン・ロシア・北朝鮮支援のAPTがClickFixを用いたフィッシング攻撃を展開。 TA427 (Kimsuky): 2025年1月と2月に、シンクタンク部門の少数組織の個人を標的としたフィッシングキャンペーンでClickFixを使用 TA450 (MuddyWater): イランに関連するこのグループは、持続的なアクセスを維持するために、Levelなどの正当なリモート監視および管理 (RMM) ソフトウェアを悪用するためにClickFixを利用 UNK_RemoteRogue: 2024年末に確認されたこのロシアの可能性のあるグループは、侵害された可能性のあるZimbraサーバーから送信された、Microsoft Officeドキュメントへのリンクを含むおとりメールを使用してClickFixを使用 PowerShellコマンドを利用しQuasar RATやRMMソフトを導入。 日本大使館を装った誘導や、YouTube動画を含む偽ページなどを利用。 | 中 | `source--daily-07ef6046e1668f840b3a` |
| MuddyWaterのDarkBitランサムウェアが解読され、無償データ復旧が可能に | ransomware-extortion | 不明 | 不明 | 2025-08-12 |  |  | ttp--activity-rule--b9cb4278ced315a8fcc2 | victim--activity-rule--c39933a0c415d45dc683 | ProferoがDarkBitの暗号化を解読し、2023年の被害企業で無償復旧に成功。 攻撃はVMware ESXiを暗号化。加害者は親イラン系を装い80BTC要求、交渉拒否し影響工作。 イスラエル当局はDarkBitをイラン支援APT「MuddyWater」と関連付け。 鍵生成のエントロピーが低く、タイムスタンプ併用で鍵空間を数十億通りに縮小。 VMDKヘッダと疎な構造を活用し多数のデータを復元。公開デクリプタは未提供。 | 高 | `source--daily-949ebd7fa1bed210b3ea` |
| MuddyWaterハッカー、攻撃でChaosランサムウェアを囮として使用 | ransomware-extortion | 不明 | 不明 | 2026-05-07 |  |  |  | victim--activity-rule--7b33e99334977e206b23 | イラン系MuddyWaterは、Microsoft Teamsのソーシャルエンジニアリングで侵入し、Chaosランサムウェア攻撃を装った。 攻撃では認証情報窃取、永続化、リモートアクセス、データ流出、恐喝メール、Chaosリークサイト掲載が行われた。 Rapid7は、ランサムウェア要素は諜報活動の隠蔽と帰属妨害のために使われた可能性が高いと評価した。 攻撃者はQuick Assist風フィッシングやローカルテキスト入力で認証情報を奪い、RDP、DWAgent、AnyDeskで永続化した。 ms_upd.exeがMicrosoft WebView2アプリを装うGame.exeバックドアを投下し、コマンド実行やファイル操作などを可能にした。 | 中 | `source--daily-f760c7a2efdf8be3ce1f` |
| 新しいBugSleepマルウェア、MuddyWater攻撃に展開 | phishing-campaign | 不明 | 不明 | 2024-07-16 | target--activity-rule--country--904728608f27c39df0df, target--activity-rule--sector--5403aec9c83d6a925f61 |  |  | victim--activity-rule--2649a00662971dc4307e | MuddyWaterハッキンググループが新しいBugSleepマルウェアを使用。 マルウェアはフィッシングメールを通じて配布。 イスラエル他様々な国で、政府機関、航空会社、メディアなどを標的としている。 Egnyteのファイル共有プラットフォームを利用。 Microsoft EdgeやGoogle Chromeなどのプロセスにインジェクトされる。 | 高 | `source--daily-b7b35ebe9f7da71be64d` |
| イラン系ハッカーがPhoenixバックドアで100超の政府機関を標的に | phishing-campaign | 不明 | 不明 | 2025-10-24 | target--sector--government |  | ttp--activity-rule--243b88fbeb77593a10aa | victim--activity-rule--c82368fb1efd6f7470ed | Group-IBは国家支援のイラン系MuddyWaterがPhoenix v4を用い、100超の政府機関を標的にしたと報告。 8月19日からNordVPN経由の侵害アカウントでフィッシングを展開、中東および北アフリカの政府・国際機関へ送信、24日にC2停止。 添付WordのVBAがFakeUpdateローダーを書き込み、C:\ProgramData\sysprocupdate.exe生成とレジストリ変更で持続化。 Phoenix v4はCOM永続化を追加しWinHTTPでC2通信、スリープ/アップロード/ダウンロード/シェル等のコマンドを実装。 攻撃基盤ではPDQやAction1 RMMも確認。Chrome等のブラウザ資格情報窃取ツールで情報収集を実施。 | 中 | `source--daily-d22b60937b867ca96947` |
| イラン系ハッカー、大手韓国電子メーカーを標的に | cyber-espionage | 2026-02 | 2026-02 | 2026-05-15 | target--activity-rule--country--6cb716c577f256f44a3e, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--e7608f51421ca8b1e297, target--sector--government |  | ttp--activity-rule--9ec6997a03bc56042379, ttp--activity-rule--f5ac9f5f4870df904875, ttp--activity-rule--fb868c07a0a02c9cf751 | victim--activity-rule--1634a387c73e6503f854 | イラン関連のMuddyWaterは、複数国・複数業種の少なくとも9組織を狙う広範なサイバースパイ活動を展開した。 被害には韓国の大手電子メーカー、政府機関、中東の国際空港、アジアの産業メーカー、教育機関が含まれる。 Symantecによると、攻撃者は2026年2月に韓国電子メーカーのネットワーク内に約1週間滞在した。 攻撃ではDLLサイドローディング、PowerShell、Node.jsローダー、ChromElevatorなどが使われた。 攻撃者は認証情報窃取、偵察、スクリーンショット取得、永続化、SOCKS5トンネル作成、データ流出を行った。 | 高 | `source--daily-ad0ed26155c84becbe19` |
| イランのMuddyWaterハッカーグループ、新しいC2ツール「DarkBeatC2」を採用 | phishing-campaign | 不明 | 不明 | 2024-04-13 | target--activity-rule--country--904728608f27c39df0df |  |  | victim--activity-rule--413bff8e6c421ef97bec | MuddyWaterが新C2ツール「DarkBeatC2」を採用 主にイスラエルの機関を対象に攻撃 攻撃はスピアフィッシングメールから開始 DarkBeatC2を介して追加ペイロードと通信 脅威活動は少なくとも2017年から活動中 | 高 | `source--daily-deef5a66e14d100f87cf` |
| Operation Quicksand | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| BlackWater | MuddyWater | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | MuddyWater | 情報なし | T1204.004 Malicious Copy and Paste, T1059.001 PowerShell | 情報なし | ロシア | 被害事例: 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | 中 |
| MuddyWaterのDarkBitランサムウェアが解読され、無償データ復旧が可能に | MuddyWater | 情報なし | T1486 Data Encrypted for Impact | 情報なし | 情報なし | 被害事例: MuddyWaterのDarkBitランサムウェアが解読され、無償データ復旧が可能に | 高 |
| MuddyWaterハッカー、攻撃でChaosランサムウェアを囮として使用 | MuddyWater | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: MuddyWaterハッカー、攻撃でChaosランサムウェアを囮として使用 | 中 |
| 新しいBugSleepマルウェア、MuddyWater攻撃に展開 | MuddyWater | 情報なし | 情報なし | 情報なし | イスラエル, メディア・報道 | 被害事例: 新しいBugSleepマルウェア、MuddyWater攻撃に展開 | 高 |
| イラン系ハッカーがPhoenixバックドアで100超の政府機関を標的に | MuddyWater | 情報なし | T1071.001 Web Protocols | 情報なし | Government | 被害事例: イラン系ハッカーがPhoenixバックドアで100超の政府機関を標的に | 中 |
| イラン系ハッカー、大手韓国電子メーカーを標的に | MuddyWater | 情報なし | T1574.001 DLL, T1113 Screen Capture, T1059.001 PowerShell | 情報なし | 韓国, 製造・産業, 教育・研究, Government | 被害事例: イラン系ハッカー、大手韓国電子メーカーを標的に | 高 |
| イランのMuddyWaterハッカーグループ、新しいC2ツール「DarkBeatC2」を採用 | MuddyWater | 情報なし | 情報なし | 情報なし | イスラエル | 被害事例: イランのMuddyWaterハッカーグループ、新しいC2ツール「DarkBeatC2」を採用 | 高 |
| Operation Quicksand | MuddyWater | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

BlackWater; Operation Quicksand

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アゼルバイジャン | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてアゼルバイジャンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アラブ首長国連邦 | MITRE ATT&CKのGroup概要でMuddyWaterの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | アルメニア | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてアルメニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | 活動「新しいBugSleepマルウェア、MuddyWater攻撃に展開」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-b7b35ebe9f7da71be64d`, `source--daily-deef5a66e14d100f87cf`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イラク | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてイラクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イラン | 活動「国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a`, `source--target-audit-etda-threat-group-cards` |
| countries | インド | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ウクライナ | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてウクライナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エジプト | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてエジプトが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オマーン | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてオマーンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストリア | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてオーストリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カタール | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてカタールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | クウェート | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてクウェートが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | サウジアラビア | MITRE ATT&CKのGroup概要でMuddyWaterの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ジョージア | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてジョージアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | スーダン | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてスーダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タジキスタン | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてタジキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タンザニア | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてタンザニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チュニジア | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてチュニジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | バーレーン | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてバーレーンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ベラルーシ | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてベラルーシが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポルトガル | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてポルトガルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マリ | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてマリが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ヨルダン | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてヨルダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ラオス | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてラオスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | レバノン | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国としてレバノンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 活動「国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a`, `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | 活動「国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a` |
| countries | 米国 | 構造化OSINTの被害国フィールドでMuddyWaterの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 韓国 | 活動「イラン系ハッカー、大手韓国電子メーカーを標的に」の記述で標的として明示された国・地域。 | 2026-02 | 2026-02 | 中 | `source--daily-ad0ed26155c84becbe19` |
| regions | アジア | MITRE ATT&CKのGroup概要でMuddyWaterの標的範囲としてアジアが明示されている。 | 2026-02 | 2026-02 | 高 | `source--actor-mapping-workbook`, `source--daily-ad0ed26155c84becbe19`, `source--mitre-attack-19-1` |
| regions | アフリカ | 活動「イラン系ハッカーがPhoenixバックドアで100超の政府機関を標的に」の記述で標的地域としてアフリカが明示されている。 | 不明 | 不明 | 中 | `source--daily-d22b60937b867ca96947`, `source--target-audit-etda-threat-group-cards` |
| regions | コーカサス | アゼルバイジャン、アルメニア、ジョージアで確認された標的・被害事例をコーカサスとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 中東 | MITRE ATT&CKのGroup概要でMuddyWaterの標的範囲として中東が明示されている。 | 2026-02 | 2026-02 | 高 | `source--actor-mapping-workbook`, `source--daily-07ef6046e1668f840b3a`, `source--daily-ad0ed26155c84becbe19`, `source--daily-b7b35ebe9f7da71be64d`, `source--daily-d22b60937b867ca96947`, `source--daily-deef5a66e14d100f87cf`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 北アフリカ | 活動「イラン系ハッカーがPhoenixバックドアで100超の政府機関を標的に」の記述で標的地域として北アフリカが明示されている。 | 不明 | 不明 | 中 | `source--daily-d22b60937b867ca96947`, `source--target-audit-etda-threat-group-cards` |
| regions | 南アジア | アフガニスタン、インド、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東アジア | 中国、韓国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a`, `source--daily-ad0ed26155c84becbe19` |
| regions | 東南アジア | タイ、ラオスで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ウクライナ、ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | ウクライナ、オランダ、オーストリア、トルコ、ベラルーシ、ポルトガルで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | メディア・報道 | 活動「新しいBugSleepマルウェア、MuddyWater攻撃に展開」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-b7b35ebe9f7da71be64d` |
| sectors | 製造・産業 | 活動「イラン系ハッカー、大手韓国電子メーカーを標的に」の記述で標的として明示された産業。 | 2026-02 | 2026-02 | 中 | `source--daily-ad0ed26155c84becbe19` |
| sectors | 教育・研究 | 活動「イラン系ハッカー、大手韓国電子メーカーを標的に」の記述で標的として明示された産業。 | 2026-02 | 2026-02 | 中 | `source--daily-ad0ed26155c84becbe19` |
| sectors | 情報通信 | Ministry of Intelligence and Security (MOIS).(Citation: CYBERCOM Iranian Intel Cyber January 2022) Since at least 2017, [MuddyWater](https://attack.mitre.org/groups/G0069) has targeted a range of government and private organizations across sectors, including telecommunications, local government, finance, defense, and oil and natural gas organizations, in the Middle East (specifically the UAE and Saudi Arabia), Asia, Africa, Europe, and North America. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Government | Targeting text indicates the Government sector. | 2026-02 | 2026-02 | 中 | `source--actor-mapping-workbook`, `source--daily-ad0ed26155c84becbe19`, `source--daily-d22b60937b867ca96947`, `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: イラン系ハッカー、大手韓国電子メーカーを標的に | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6cb716c577f256f44a3e, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--e7608f51421ca8b1e297, target--sector--government |  | ttp--activity-rule--9ec6997a03bc56042379, ttp--activity-rule--f5ac9f5f4870df904875, ttp--activity-rule--fb868c07a0a02c9cf751 |  | data-theft: 攻撃者は認証情報窃取、偵察、スクリーンショット取得、永続化、SOCKS5トンネル作成、データ流出を行った。<br>credential-theft: 攻撃者は認証情報窃取、偵察、スクリーンショット取得、永続化、SOCKS5トンネル作成、データ流出を行った。<br>espionage: イラン関連のMuddyWaterは、複数国・複数業種の少なくとも9組織を狙う広範なサイバースパイ活動を展開した。 | 2026-02 | 2026-02 | 2026-05-15 | 高 | `source--daily-ad0ed26155c84becbe19` |
| 被害事例: 新しいBugSleepマルウェア、MuddyWater攻撃に展開 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--904728608f27c39df0df, target--activity-rule--sector--5403aec9c83d6a925f61 |  |  | メール／メールアカウント |  | 不明 | 不明 | 2024-07-16 | 高 | `source--daily-b7b35ebe9f7da71be64d` |
| 被害事例: 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--72caf60a2fbce4a1be7a |  | ttp--activity-rule--8a62cee39ddda59204db, ttp--activity-rule--b151f73dbd3a8fe978b9 | メール／メールアカウント, サーバー |  | 不明 | 不明 | 2025-04-18 | 中 | `source--daily-07ef6046e1668f840b3a` |
| 被害事例: イランのMuddyWaterハッカーグループ、新しいC2ツール「DarkBeatC2」を採用 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--904728608f27c39df0df |  |  | メール／メールアカウント |  | 不明 | 不明 | 2024-04-13 | 高 | `source--daily-deef5a66e14d100f87cf` |
| 被害事例: MuddyWaterハッカー、攻撃でChaosランサムウェアを囮として使用 | 非公開 | anonymous | unknown | reported |  |  |  | メール／メールアカウント, VPN／リモートアクセス機器 | data-theft: 攻撃では認証情報窃取、永続化、リモートアクセス、データ流出、恐喝メール、Chaosリークサイト掲載が行われた。<br>credential-theft: 攻撃では認証情報窃取、永続化、リモートアクセス、データ流出、恐喝メール、Chaosリークサイト掲載が行われた。<br>encryption: MuddyWaterハッカー、攻撃でChaosランサムウェアを囮として使用 | 不明 | 不明 | 2026-05-07 | 中 | `source--daily-f760c7a2efdf8be3ce1f` |
| 被害事例: MuddyWaterのDarkBitランサムウェアが解読され、無償データ復旧が可能に | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--activity-rule--b9cb4278ced315a8fcc2 |  | encryption: MuddyWaterのDarkBitランサムウェアが解読され、無償データ復旧が可能に | 不明 | 不明 | 2025-08-12 | 高 | `source--daily-949ebd7fa1bed210b3ea` |
| 被害事例: イラン系ハッカーがPhoenixバックドアで100超の政府機関を標的に | 非公開 | anonymous | unknown | reported | target--sector--government |  | ttp--activity-rule--243b88fbeb77593a10aa | VPN／リモートアクセス機器 | espionage: Chrome等のブラウザ資格情報窃取ツールで情報収集を実施。 | 不明 | 不明 | 2025-10-24 | 中 | `source--daily-d22b60937b867ca96947` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1071.001 | Web Protocols | Phoenix v4はCOM永続化を追加しWinHTTPでC2通信、スリープ/アップロード/ダウンロード/シェル等のコマンドを実装。 |  | activity--daily-bc81c28cf709a0060462 | 不明 | 不明 | 中 | `source--daily-d22b60937b867ca96947` |
| Execution | T1204.004 | Malicious Copy and Paste | 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 |  | activity--daily-3086f27375c7783939d6 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a` |
| Execution, Stealth | T1574.001 | DLL | 攻撃ではDLLサイドローディング、PowerShell、Node.jsローダー、ChromElevatorなどが使われた。 |  | activity--daily-c095462a559b1a9c6436 | 2026-02 | 2026-02 | 中 | `source--daily-ad0ed26155c84becbe19` |
| Execution | T1059.001 | PowerShell | UNK_RemoteRogue: 2024年末に確認されたこのロシアの可能性のあるグループは、侵害された可能性のあるZimbraサーバーから送信された、Microsoft Officeドキュメントへのリンクを含むおとりメールを使用してClickFixを使用 PowerShellコマンドを利用しQuasar RATやRMMソフトを導入。 |  | activity--daily-3086f27375c7783939d6 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a` |
| Impact | T1486 | Data Encrypted for Impact | MuddyWaterのDarkBitランサムウェアが解読され、無償データ復旧が可能に ProferoがDarkBitの暗号化を解読し、2023年の被害企業で無償復旧に成功。 |  | activity--daily-6d58c1ff3ee5484f19f1 | 不明 | 不明 | 中 | `source--daily-949ebd7fa1bed210b3ea` |
| Collection | T1113 | Screen Capture | 攻撃者は認証情報窃取、偵察、スクリーンショット取得、永続化、SOCKS5トンネル作成、データ流出を行った。 |  | activity--daily-c095462a559b1a9c6436 | 2026-02 | 2026-02 | 中 | `source--daily-ad0ed26155c84becbe19` |
| Execution | T1059.001 | PowerShell | 攻撃ではDLLサイドローディング、PowerShell、Node.jsローダー、ChromElevatorなどが使われた。 |  | activity--daily-c095462a559b1a9c6436 | 2026-02 | 2026-02 | 中 | `source--daily-ad0ed26155c84becbe19` |
| Credential Access | T1003.001 | LSASS Memory | [MuddyWater](https://attack.mitre.org/groups/G0069) has performed credential dumping with [Mimikatz](https://attack.mitre.org/software/S0002) and procdump64.exe.(Citation: Unit 42 MuddyWater Nov 2017)(Citation: Symantec MuddyWater Dec 2018)(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.004 | LSA Secrets | [MuddyWater](https://attack.mitre.org/groups/G0069) has performed credential dumping with [LaZagne](https://attack.mitre.org/software/S0349).(Citation: Unit 42 MuddyWater Nov 2017)(Citation: Symantec MuddyWater Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.005 | Cached Domain Credentials | [MuddyWater](https://attack.mitre.org/groups/G0069) has performed credential dumping with [LaZagne](https://attack.mitre.org/software/S0349).(Citation: Unit 42 MuddyWater Nov 2017)(Citation: Symantec MuddyWater Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware to collect the victim’s IP address and domain name.(Citation: Securelist MuddyWater Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | [MuddyWater](https://attack.mitre.org/groups/G0069) has stored obfuscated JavaScript code in an image file named temp.jpg.(Citation: ClearSky MuddyWater Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.004 | Compile After Delivery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used the .NET csc.exe tool to compile executables from downloaded C# code.(Citation: ClearSky MuddyWater Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [MuddyWater](https://attack.mitre.org/groups/G0069) has used Daniel Bohannon’s Invoke-Obfuscation framework and obfuscated PowerShell scripts.(Citation: Unit 42 MuddyWater Nov 2017)(Citation: GitHub Invoke-Obfuscation) The group has also used other obfuscation methods, including Base64 obfuscation of VBScripts and PowerShell commands.(Citation: Unit 42 MuddyWater Nov 2017)(Citation: FireEye MuddyWater Mar 2018)(Citation: Securelist MuddyWater Oct 2018)(Citation: Talos MuddyWater May 2019)(Citation: ClearSky MuddyWater June 2019)(Citation: Trend Micro Muddy Water March 2021)(Citation: Talos MuddyWater Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can collect the victim’s username.(Citation: Securelist MuddyWater Oct 2018)(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [MuddyWater](https://attack.mitre.org/groups/G0069) has disguised malicious executables and used filenames and Registry key names associated with Windows Defender.(Citation: FireEye MuddyWater Mar 2018)(Citation: Talos MuddyWater May 2019)(Citation: Anomali Static Kitten February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [MuddyWater](https://attack.mitre.org/groups/G0069) has used C2 infrastructure to receive exfiltrated data.(Citation: Reaqta MuddyWater November 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that leveraged WMI for execution and querying host information.(Citation: Securelist MuddyWater Oct 2018)(Citation: ClearSky MuddyWater Nov 2018)(Citation: Talos MuddyWater May 2019)(Citation: DHS CISA AA22-055A MuddyWater February 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used a PowerShell backdoor to check for Skype connections on the target machine.(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [MuddyWater](https://attack.mitre.org/groups/G0069) has used scheduled tasks to establish persistence.(Citation: Reaqta MuddyWater November 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware to obtain a list of running processes on the system.(Citation: Securelist MuddyWater Oct 2018)(Citation: ClearSky MuddyWater June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [MuddyWater](https://attack.mitre.org/groups/G0069) has used PowerShell for execution.(Citation: FireEye MuddyWater Mar 2018)(Citation: MuddyWater TrendMicro June 2018)(Citation: Securelist MuddyWater Oct 2018)(Citation: Symantec MuddyWater Dec 2018)(Citation: ClearSky MuddyWater Nov 2018)(Citation: Talos MuddyWater May 2019)(Citation: Reaqta MuddyWater November 2017)(Citation: Trend Micro Muddy Water March 2021)(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: Talos MuddyWater Jan 2022)(Citation: NaumaanProofpoint_GlobalClickFix_April2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [MuddyWater](https://attack.mitre.org/groups/G0069) has used a custom tool for creating reverse shells.(Citation: Symantec MuddyWater Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [MuddyWater](https://attack.mitre.org/groups/G0069) has used VBScript files to execute its [POWERSTATS](https://attack.mitre.org/software/S0223) payload, as well as macros.(Citation: FireEye MuddyWater Mar 2018)(Citation: MuddyWater TrendMicro June 2018)(Citation: Securelist MuddyWater Oct 2018)(Citation: Symantec MuddyWater Dec 2018)(Citation: ClearSky MuddyWater Nov 2018)(Citation: ClearSky MuddyWater June 2019)(Citation: Reaqta MuddyWater November 2017)(Citation: Trend Micro Muddy Water March 2021)(Citation: Talos MuddyWater Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | [MuddyWater](https://attack.mitre.org/groups/G0069) has developed tools in Python including [Out1](https://attack.mitre.org/software/S0594).(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | [MuddyWater](https://attack.mitre.org/groups/G0069) has used JavaScript files to execute its [POWERSTATS](https://attack.mitre.org/software/S0223) payload.(Citation: ClearSky MuddyWater Nov 2018)(Citation: FireEye MuddyWater Mar 2018)(Citation: DHS CISA AA22-055A MuddyWater February 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [MuddyWater](https://attack.mitre.org/groups/G0069) has used HTTP for C2 communications.(Citation: ClearSky MuddyWater June 2019)(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [MuddyWater](https://attack.mitre.org/groups/G0069) has stored a decoy PDF file within a victim's `%temp%` folder.(Citation: Talos MuddyWater Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can collect the victim’s OS version and machine name.(Citation: Securelist MuddyWater Oct 2018)(Citation: Talos MuddyWater May 2019)(Citation: Reaqta MuddyWater November 2017)(Citation: Trend Micro Muddy Water March 2021)(Citation: Talos MuddyWater Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that checked if the ProgramData folder had folders or files with the keywords "Kasper," "Panda," or "ESET."(Citation: Securelist MuddyWater Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [MuddyWater](https://attack.mitre.org/groups/G0069) has used <code>cmd.exe net user /domain</code> to enumerate domain users.(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | [MuddyWater](https://attack.mitre.org/groups/G0069) has used NordVPN to proxy phishing emails, making them appear to originate from France.(Citation: FalconFeeds_Iran_Mar2026)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.002 | External Proxy | [MuddyWater](https://attack.mitre.org/groups/G0069) has controlled [POWERSTATS](https://attack.mitre.org/software/S0223) from behind a proxy network to obfuscate the C2 location.(Citation: Symantec MuddyWater Dec 2018) [MuddyWater](https://attack.mitre.org/groups/G0069) has used a series of compromised websites that victims connected to randomly to relay information to command and control (C2).(Citation: Reaqta MuddyWater November 2017)(Citation: Trend Micro Muddy Water March 2021) [MuddyWater](https://attack.mitre.org/groups/G0069) has also used go-socks5 variants to bypass firewalls and Network Address Translation (NAT), to communicate with a hardcoded C2 server, and to exfiltrate data.(Citation: ESET_MuddyWater_Dec2025)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | [MuddyWater](https://attack.mitre.org/groups/G0069) has used web services including OneHub to distribute remote access tools.(Citation: Anomali Static Kitten February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1104 | Multi-Stage Channels | [MuddyWater](https://attack.mitre.org/groups/G0069) has used one C2 to obtain enumeration scripts and monitor web logs, but a different C2 to send data back.(Citation: Talos MuddyWater May 2019)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can upload additional files to the victim’s machine.(Citation: Securelist MuddyWater Oct 2018)(Citation: ClearSky MuddyWater Nov 2018)(Citation: Reaqta MuddyWater November 2017)(Citation: Trend Micro Muddy Water March 2021) [MuddyWater](https://attack.mitre.org/groups/G0069) has used PowerShell commands to install remote management and monitoring (RMM) software on the victim’s machine to conduct espionage and to exfiltrate data.(Citation: NaumaanProofpoint_GlobalClickFix_April2025)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can capture screenshots of the victim’s machine.(Citation: Securelist MuddyWater Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | [MuddyWater](https://attack.mitre.org/groups/G0069) has used tools to encode C2 communications including Base64 encoding.(Citation: ClearSky MuddyWater June 2019)(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1137.001 | Office Template Macros | [MuddyWater](https://attack.mitre.org/groups/G0069) has used a Word Template, Normal.dotm, for persistence.(Citation: Reaqta MuddyWater November 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [MuddyWater](https://attack.mitre.org/groups/G0069) has decoded base64-encoded PowerShell, JavaScript, and VBScript.(Citation: FireEye MuddyWater Mar 2018)(Citation: MuddyWater TrendMicro June 2018)(Citation: ClearSky MuddyWater Nov 2018)(Citation: Talos MuddyWater Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [MuddyWater](https://attack.mitre.org/groups/G0069) has exploited the Microsoft Exchange memory corruption vulnerability (CVE-2020-0688).(Citation: DHS CISA AA22-055A MuddyWater February 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [MuddyWater](https://attack.mitre.org/groups/G0069) has exploited the Office vulnerability CVE-2017-0199 for execution.(Citation: ClearSky MuddyWater June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [MuddyWater](https://attack.mitre.org/groups/G0069) has distributed URLs in phishing e-mails that link to lure documents.(Citation: Anomali Static Kitten February 2021)(Citation: Trend Micro Muddy Water March 2021)(Citation: Proofpoint TA450 Phishing March 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [MuddyWater](https://attack.mitre.org/groups/G0069) has attempted to get users to open malicious PDF attachment and to enable macros and launch malicious Microsoft Word documents delivered via spearphishing emails.(Citation: Unit 42 MuddyWater Nov 2017)(Citation: FireEye MuddyWater Mar 2018)(Citation: Securelist MuddyWater Oct 2018)(Citation: Talos MuddyWater May 2019)(Citation: ClearSky MuddyWater June 2019)(Citation: Reaqta MuddyWater November 2017)(Citation: Anomali Static Kitten February 2021)(Citation: Trend Micro Muddy Water March 2021)(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: Talos MuddyWater Jan 2022)(Citation: Proofpoint TA450 Phishing March 2024) Additionally, [MuddyWater](https://attack.mitre.org/groups/G0069) has used a Word document with a malicious Visual Basic for Applications (VBA) macro; when enabled, the CertificationKit.ini payload is constructed and executed.(Citation: CloudSEK_RustyWater_Jan2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.004 | Malicious Copy and Paste | [MuddyWater](https://attack.mitre.org/groups/G0069) has leveraged ClickFix type tactics enticing victims to copy and paste malicious PowerShell code.(Citation: NaumaanProofpoint_GlobalClickFix_April2025)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | [MuddyWater](https://attack.mitre.org/groups/G0069) has exploited the Microsoft Netlogon vulnerability (CVE-2020-1472).(Citation: DHS CISA AA22-055A MuddyWater February 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.003 | CMSTP | [MuddyWater](https://attack.mitre.org/groups/G0069) has used CMSTP.exe and a malicious INF to execute its [POWERSTATS](https://attack.mitre.org/software/S0223) payload.(Citation: FireEye MuddyWater Mar 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | [MuddyWater](https://attack.mitre.org/groups/G0069) has used mshta.exe to execute its [POWERSTATS](https://attack.mitre.org/software/S0223) payload and to pass a PowerShell one-liner for execution.(Citation: FireEye MuddyWater Mar 2018)(Citation: Securelist MuddyWater Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that leveraged rundll32.exe in a Registry Run key to execute a .dll.(Citation: Securelist MuddyWater Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219.002 | Remote Desktop Software | [MuddyWater](https://attack.mitre.org/groups/G0069) has leveraged RMM solutions including ScreenConnect, AteraAgent, SimpleHelp, Action1, Level, and PDQ to facilitate follow-on actions within compromised hosts to include data exfiltration.(Citation: Trend Micro Muddy Water March 2021)(Citation: Anomali Static Kitten February 2021)(Citation: Proofpoint TA450 Phishing March 2024)(Citation: group-ib_muddywater_infra)(Citation: FalconFeeds_Iran_Mar2026)(Citation: NaumaanProofpoint_GlobalClickFix_April2025)(Citation: FalconFeeds_MuddyWaterPSRust_Mar2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518 | Software Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used a PowerShell backdoor to check for Skype connectivity on the target machine.(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware to check running processes against a hard-coded list of security tools often used by malware researchers.(Citation: Securelist MuddyWater Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1534 | Internal Spearphishing | [MuddyWater](https://attack.mitre.org/groups/G0069) has used compromised mailboxes within target organizations to send spearphishing emails.(Citation: FalconFeeds_Iran_Mar2026)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [MuddyWater](https://attack.mitre.org/groups/G0069) has added Registry Run key <code>KCU\Software\Microsoft\Windows\CurrentVersion\Run\SystemTextEncoding</code> to establish persistence.(Citation: FireEye MuddyWater Mar 2018)(Citation: Securelist MuddyWater Oct 2018)(Citation: Talos MuddyWater May 2019)(Citation: Reaqta MuddyWater November 2017)(Citation: Trend Micro Muddy Water March 2021)(Citation: Talos MuddyWater Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | [MuddyWater](https://attack.mitre.org/groups/G0069) uses various techniques to bypass UAC.(Citation: ClearSky MuddyWater Nov 2018)(Citation: NaumaanProofpoint_GlobalClickFix_April2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [MuddyWater](https://attack.mitre.org/groups/G0069) has run a tool that steals passwords saved in victim email.(Citation: Symantec MuddyWater Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555 | Credentials from Password Stores | [MuddyWater](https://attack.mitre.org/groups/G0069) has performed credential dumping with [LaZagne](https://attack.mitre.org/software/S0349) and other tools, including by dumping passwords saved in victim email.(Citation: Unit 42 MuddyWater Nov 2017)(Citation: Symantec MuddyWater Dec 2018)(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [MuddyWater](https://attack.mitre.org/groups/G0069) has run tools including Browser64 to steal passwords saved in victim web browsers.(Citation: Symantec MuddyWater Dec 2018)(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.001 | Component Object Model | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that has the capability to execute malicious code via COM, DCOM, and Outlook.(Citation: Securelist MuddyWater Oct 2018)(Citation: ClearSky MuddyWater June 2019)(Citation: DHS CISA AA22-055A MuddyWater February 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.002 | Dynamic Data Exchange | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can execute PowerShell scripts via DDE.(Citation: Securelist MuddyWater Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [MuddyWater](https://attack.mitre.org/groups/G0069) has used the native Windows cabinet creation tool, makecab.exe, likely to compress stolen data to be uploaded.(Citation: Symantec MuddyWater Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | [MuddyWater](https://attack.mitre.org/groups/G0069) has sent phishing emails to targets from the email address support@microsoftonlines[.]com.(Citation: NaumaanProofpoint_GlobalClickFix_April2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [MuddyWater](https://attack.mitre.org/groups/G0069) has compromised third parties and used compromised accounts to send spearphishing emails with targeted attachments to recipients.(Citation: Unit 42 MuddyWater Nov 2017)(Citation: FireEye MuddyWater Mar 2018)(Citation: Securelist MuddyWater Oct 2018)(Citation: ClearSky MuddyWater June 2019)(Citation: Anomali Static Kitten February 2021)(Citation: Trend Micro Muddy Water March 2021)(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: Proofpoint TA450 Phishing March 2024)(Citation: ESET_MuddyWater_Dec2025)(Citation: SOCRadar_MuddyWaterDindoor_Mar2026) [MuddyWater](https://attack.mitre.org/groups/G0069) has also sent spearphishing emails with the attachment Cybersecurity.doc, which served as the primarily payload for the next stage.(Citation: CloudSEK_RustyWater_Jan2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [MuddyWater](https://attack.mitre.org/groups/G0069) has sent targeted spearphishing e-mails with malicious links.(Citation: Anomali Static Kitten February 2021)(Citation: Trend Micro Muddy Water March 2021)(Citation: Proofpoint TA450 Phishing March 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [MuddyWater](https://attack.mitre.org/groups/G0069) has attempted to exfiltrate data to Wasabi, a cloud storage service, using [Rclone](https://attack.mitre.org/software/S1040).(Citation: SOCRadar_MuddyWaterDindoor_Mar2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [MuddyWater](https://attack.mitre.org/groups/G0069) has used ports 8043 and 8848 for botnet C2 communication.(Citation: FalconFeeds_MuddyWaterPSRust_Mar2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | [MuddyWater](https://attack.mitre.org/groups/G0069) has used AES to encrypt C2 responses.(Citation: Talos MuddyWater Jan 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [MuddyWater](https://attack.mitre.org/groups/G0069) maintains persistence on victim networks through side-loading dlls to trick legitimate programs into running malware.(Citation: DHS CISA AA22-055A MuddyWater February 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [MuddyWater](https://attack.mitre.org/groups/G0069) has established domains, some of which appeared to spoof legitimate domains for use in operations.(Citation: NaumaanProofpoint_GlobalClickFix_April2025)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | [MuddyWater](https://attack.mitre.org/groups/G0069) has used file sharing services including OneHub, Sync, and TeraBox to distribute tools.(Citation: Anomali Static Kitten February 2021)(Citation: Trend Micro Muddy Water March 2021)(Citation: Proofpoint TA450 Phishing March 2024)(Citation: ESET_MuddyWater_Dec2025)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | [MuddyWater](https://attack.mitre.org/groups/G0069) has used publicly available malware for operations, likely to blend in with other cybercriminals.(Citation: Huntio_IranInfra_Mar2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MuddyWater has used legitimate tools [ConnectWise](https://attack.mitre.org/software/S0591), [RemoteUtilities](https://attack.mitre.org/software/S0592), and SimpleHelp to gain access to the target environment.(Citation: Anomali Static Kitten February 2021)(Citation: group-ib_muddywater_infra)(Citation: ESET_MuddyWater_Dec2025)(Citation: NaumaanProofpoint_GlobalClickFix_April2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1590.004 | Network Topology | [MuddyWater](https://attack.mitre.org/groups/G0069) has mapped target networks; access to this information and more is then shared/sold to other Iran threat actors.(Citation: FalconFeeds_MuddyWaterPSRust_Mar2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | [MuddyWater](https://attack.mitre.org/groups/G0069) has used support@microsoftonlines[.]com to send phishing emails that masqueraded as security updates from Microsoft.(Citation: NaumaanProofpoint_GlobalClickFix_April2025) [MuddyWater](https://attack.mitre.org/groups/G0069) has also impersonated TMCell (Altyn Asyr CJSC), the primary mobile operator in Turkmenistan, sending phishing emails with the email domain info@tmcell.(Citation: CloudSEK_RustyWater_Jan2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [MuddyWater](https://attack.mitre.org/groups/G0069) can disable the system's local proxy settings.(Citation: Trend Micro Muddy Water March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 239件
- IOC観測: 279件
- 複数攻撃で観測: 0件
- 要レビュー候補: 69件
- 非IOC artifact観測: 46件（`artifacts.csv`）

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
| source--daily-07ef6046e1668f840b3a | 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | thehackernews.com | 2025-04-18 | https://thehackernews.com/2025/04/state-sponsored-hackers-weaponize.html | osint-report | TLP:CLEAR | 中 |
| source--daily-949ebd7fa1bed210b3ea | MuddyWaterのDarkBitランサムウェアが解読され、無償データ復旧が可能に | bleepingcomputer.com | 2025-08-12 | https://www.bleepingcomputer.com/news/security/muddywaters-darkbit-ransomware-cracked-for-free-data-recovery/ | osint-report | TLP:CLEAR | 中 |
| source--daily-ad0ed26155c84becbe19 | イラン系ハッカー、大手韓国電子メーカーを標的に | security.com | 2026-05-15 | https://www.security.com/threat-intelligence/iran-seedworm-electronics | osint-report | TLP:CLEAR | 中 |
| source--daily-b7b35ebe9f7da71be64d | 新しいBugSleepマルウェア、MuddyWater攻撃に展開 | bleepingcomputer.com | 2024-07-16 | https://www.bleepingcomputer.com/news/security/new-bugsleep-malware-implant-deployed-in-muddywater-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-d22b60937b867ca96947 | イラン系ハッカーがPhoenixバックドアで100超の政府機関を標的に | bleepingcomputer.com | 2025-10-24 | https://www.bleepingcomputer.com/news/security/iranian-hackers-targeted-over-100-govt-orgs-with-phoenix-backdoor/ | osint-report | TLP:CLEAR | 中 |
| source--daily-deef5a66e14d100f87cf | イランのMuddyWaterハッカーグループ、新しいC2ツール「DarkBeatC2」を採用 | thehackernews.com | 2024-04-13 | https://thehackernews.com/2024/04/iranian-muddywater-hackers-adopt-new-c2.html | osint-report | TLP:CLEAR | 中 |
| source--daily-f760c7a2efdf8be3ce1f | MuddyWaterハッカー、攻撃でChaosランサムウェアを囮として使用 | rapid7.com | 2026-05-07 | https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--muddywater--2e79f520fa3d06d8 | Iranian intel cyber suite of malware uses open source tools |  | 不明 | muddywater/Iranian intel cyber suite of malware uses open source tools.pdf | report | TLP:CLEAR | 中 |
| source--muddywater--4536dea64d925d9a | Clearsky Iranian APT group ‘MuddyWater’ Adds Exploits to Their Arsenal |  | 不明 | muddywater/Clearsky-Iranian-APT-group-‘MuddyWater’-Adds-Exploits-to-Their-Arsenal.pdf | report | TLP:CLEAR | 中 |
| source--muddywater--4c6282d70993109c | README |  | 不明 | muddywater/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--muddywater--6c27a0ecd5aa5629 | README |  | 不明 | muddywater/greenleaker/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--muddywater--77fecc73ab07f06c | wp new muddywater findings uncovered |  | 不明 | muddywater/wp_new_muddywater_findings_uncovered.pdf | report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
