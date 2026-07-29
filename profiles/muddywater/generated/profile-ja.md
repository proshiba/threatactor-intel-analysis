# MuddyWater 脅威アクタープロファイル

- プロファイルID: `actor--muddywater`
- 状態: draft
- 更新日時: 2026-07-27T11:17:24Z
- 構造バージョン: 1.0.0

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| BlackWater | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | phishing-campaign | 不明 | 不明 | 2025-04-18 | 中国・イラン・ロシア・北朝鮮支援のAPTがClickFixを用いたフィッシング攻撃を展開。 TA427 (Kimsuky): 2025年1月と2月に、シンクタンク部門の少数組織の個人を標的としたフィッシングキャンペーンでClickFixを使用 TA450 (MuddyWater): イランに関連するこのグループは、持続的なアクセスを維持するために、Levelなどの正当なリモート監視および管理 (RMM) ソフトウェアを悪用するためにClickFixを利用 UNK_RemoteRogue: 2024年末に確認されたこのロシアの可能性のあるグループは、侵害された可能性のあるZimbraサーバーから送信された、Microsoft Officeドキュメントへのリンクを含むおとりメールを使用してClickFixを使用 PowerShellコマンドを利用しQuasar RATやRMMソフトを導入。 日本大使館を装った誘導や、YouTube動画を含む偽ページなどを利用。 | 中 | `source--daily-07ef6046e1668f840b3a` |
| MuddyWaterのDarkBitランサムウェアが解読され、無償データ復旧が可能に | ransomware-extortion | 不明 | 不明 | 2025-08-12 | ProferoがDarkBitの暗号化を解読し、2023年の被害企業で無償復旧に成功。 攻撃はVMware ESXiを暗号化。加害者は親イラン系を装い80BTC要求、交渉拒否し影響工作。 イスラエル当局はDarkBitをイラン支援APT「MuddyWater」と関連付け。 鍵生成のエントロピーが低く、タイムスタンプ併用で鍵空間を数十億通りに縮小。 VMDKヘッダと疎な構造を活用し多数のデータを復元。公開デクリプタは未提供。 | 高 | `source--daily-949ebd7fa1bed210b3ea` |
| MuddyWaterハッカー、攻撃でChaosランサムウェアを囮として使用 | ransomware-extortion | 不明 | 不明 | 2026-05-07 | イラン系MuddyWaterは、Microsoft Teamsのソーシャルエンジニアリングで侵入し、Chaosランサムウェア攻撃を装った。 攻撃では認証情報窃取、永続化、リモートアクセス、データ流出、恐喝メール、Chaosリークサイト掲載が行われた。 Rapid7は、ランサムウェア要素は諜報活動の隠蔽と帰属妨害のために使われた可能性が高いと評価した。 攻撃者はQuick Assist風フィッシングやローカルテキスト入力で認証情報を奪い、RDP、DWAgent、AnyDeskで永続化した。 ms_upd.exeがMicrosoft WebView2アプリを装うGame.exeバックドアを投下し、コマンド実行やファイル操作などを可能にした。 | 中 | `source--daily-f760c7a2efdf8be3ce1f` |
| 新しいBugSleepマルウェア、MuddyWater攻撃に展開 | phishing-campaign | 不明 | 不明 | 2024-07-16 | MuddyWaterハッキンググループが新しいBugSleepマルウェアを使用。 マルウェアはフィッシングメールを通じて配布。 イスラエル他様々な国で、政府機関、航空会社、メディアなどを標的としている。 Egnyteのファイル共有プラットフォームを利用。 Microsoft EdgeやGoogle Chromeなどのプロセスにインジェクトされる。 | 高 | `source--daily-b7b35ebe9f7da71be64d` |
| イラン系ハッカーがPhoenixバックドアで100超の政府機関を標的に | phishing-campaign | 不明 | 不明 | 2025-10-24 | Group-IBは国家支援のイラン系MuddyWaterがPhoenix v4を用い、100超の政府機関を標的にしたと報告。 8月19日からNordVPN経由の侵害アカウントでフィッシングを展開、中東および北アフリカの政府・国際機関へ送信、24日にC2停止。 添付WordのVBAがFakeUpdateローダーを書き込み、C:\ProgramData\sysprocupdate.exe生成とレジストリ変更で持続化。 Phoenix v4はCOM永続化を追加しWinHTTPでC2通信、スリープ/アップロード/ダウンロード/シェル等のコマンドを実装。 攻撃基盤ではPDQやAction1 RMMも確認。Chrome等のブラウザ資格情報窃取ツールで情報収集を実施。 | 中 | `source--daily-d22b60937b867ca96947` |
| イランのMuddyWaterハッカーグループ、新しいC2ツール「DarkBeatC2」を採用 | phishing-campaign | 不明 | 不明 | 2024-04-13 | MuddyWaterが新C2ツール「DarkBeatC2」を採用 主にイスラエルの機関を対象に攻撃 攻撃はスピアフィッシングメールから開始 DarkBeatC2を介して追加ペイロードと通信 脅威活動は少なくとも2017年から活動中 | 高 | `source--daily-deef5a66e14d100f87cf` |
| Operation Quicksand | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| イラン系ハッカー、大手韓国電子メーカーを標的に | cyber-espionage | 2026-02 | 2026-02 | 2026-05-15 | イラン関連のMuddyWaterは、複数国・複数業種の少なくとも9組織を狙う広範なサイバースパイ活動を展開した。 被害には韓国の大手電子メーカー、政府機関、中東の国際空港、アジアの産業メーカー、教育機関が含まれる。 Symantecによると、攻撃者は2026年2月に韓国電子メーカーのネットワーク内に約1週間滞在した。 攻撃ではDLLサイドローディング、PowerShell、Node.jsローダー、ChromElevatorなどが使われた。 攻撃者は認証情報窃取、偵察、スクリーンショット取得、永続化、SOCKS5トンネル作成、データ流出を行った。 | 高 | `source--daily-ad0ed26155c84becbe19` |

BlackWater; Operation Quicksand

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.004 | LSA Secrets | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.005 | Cached Domain Credentials | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.004 | Compile After Delivery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.002 | External Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1104 | Multi-Stage Channels | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1137.001 | Office Template Macros | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.004 | Malicious Copy and Paste | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.003 | CMSTP | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219.002 | Remote Desktop Software | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518 | Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1534 | Internal Spearphishing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555 | Credentials from Password Stores | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.001 | Component Object Model | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.002 | Dynamic Data Exchange | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1590.004 | Network Topology | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
