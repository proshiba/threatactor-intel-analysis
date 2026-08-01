# MirrorFace 脅威アクタープロファイル

- プロファイルID: `actor--mirrorface`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

MirrorFaceの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **MirrorFace**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Earth Kasha | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| menuPass | overlaps-with | [MirrorFace](https://attack.mitre.org/groups/G1054) is a People's Republic of China (PRC)-aligned cyberespionage actor believed to be a subgroup under the [menuPass](https://attack.mitre.org/groups/G0045) umbrella based on targeting, tools, and infrastructure overlaps. | 高 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [MirrorFace](https://attack.mitre.org/groups/G1054) is a People's Republic of China (PRC)-aligned cyberespionage actor believed to be a subgroup under the [menuPass](https://attack.mitre.org/groups/G0045) umbrella based on targeting, tools, and infrastructure overlaps. [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. Subsequent [MirrorFace](https://attack.mitre.org/groups/G1054) operations included targets in Central Europe and featured use of [LODEINFO](https://attack.mitre.org/software/S9020), [HiddenFace](https://attack.mitre.org/software/S9023), and [UPPERCUT](https://attack.mitre.org/software/S0275) malware.(Citation: Kaspersky LODEINFO OCT 2022)(Citation: Kaspersky LODEINFO Part II OCT 2022)(Citation: ESET MirrorFace DEC 2022)(Citation: JPCERT MirrorFace JUL 2024)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: Trend Micro Earth Kasha Updates APR 2025) |
| Capability | ROAMINGHOUSE, MirrorStealer, NOOPLDR, LODEINFO, HiddenFace, Cobalt Strike, DOWNIISSA, UPPERCUT, Net, ipconfig, Tasklist, BITSAdmin, Nltest, nbtstat, Ping, Wevtutil |
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
| etda-threat-group-cards | Operation LiberalFace, MirrorFace | canonical-name | 高 | China | https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/<br>https://www.bleepingcomputer.com/news/security/mirrorface-hackers-targeting-japanese-govt-politicians-since-2019/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Operation+LiberalFace%2C+MirrorFace&n=1 |
| etda-threat-group-cards | Stone Panda, APT 10, menuPass | single-alias-intersection | 中 | China | https://intrusiontruth.wordpress.com/2018/08/15/apt10-was-managed-by-the-tianjin-bureau-of-the-chinese-ministry-of-state-security/<br>https://www.carbonblack.com/2019/02/25/defeating-compiler-level-obfuscations-used-in-apt10-malware/<br>https://adeo.com.tr/wp-content/uploads/2020/02/APT10_v1.2_public.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | MirrorFace | canonical-name | 高 | CN | https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/<br>https://web-assets.esetstatic.com/wls/2023/01/eset_apt_activity_report_t32022.pdf<br>https://blog.sekoia.io/my-teas-not-cold-an-overview-of-china-cyber-threat/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | MirrorFace - G1054 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1054<br>https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html<br>https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/ |
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
| malware--downiissa | DOWNIISSA | [DOWNIISSA](https://attack.mitre.org/software/S9021) is a shellcode downloader that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2022 to deploy payloads, including the [LODEINFO](https://attack.mitre.org/software/S9020) backdoor.(Citation: Kaspersky LODEINFO OCT 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hiddenface | HiddenFace | [HiddenFace](https://attack.mitre.org/software/S9023) is a modular backdoor developed and used exclusively by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2021. [HiddenFace](https://attack.mitre.org/software/S9023) can communicate both actively and passively and has been used against political and academic targets.(Citation: JPCERT MirrorFace JUL 2024)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: Trend Micro Earth Kasha Updates APR 2025) | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--lodeinfo | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) is a fileless backdoor malware first identified in 2020 that has been used by actors including [MirrorFace](https://attack.mitre.org/groups/G1054), primarily against media, diplomatic, governmental, and public sector organizations in Japan.(Citation: Kaspersky LODEINFO OCT 2022)(Citation: ITOCHU LODEINFO JAN 2024)(Citation: ESET MirrorFace DEC 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--mirrorstealer | MirrorStealer | [MirrorStealer](https://attack.mitre.org/software/S9022) is a credential stealer that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2022 to steal credentials from various applications, including browsers and email clients. [MirrorStealer](https://attack.mitre.org/software/S9022) has been delivered directly into system memory via commands issued by [LODEINFO](https://attack.mitre.org/software/S9020).(Citation: ESET MirrorFace DEC 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--noopldr | NOOPLDR | [NOOPLDR](https://attack.mitre.org/software/S9025) is a shellcode loader with XML/C# and DLL versions that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) to load [HiddenFace](https://attack.mitre.org/software/S9023).(Citation: Trend Micro Earth Kasha NOV 2024)<br> | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--roaminghouse | ROAMINGHOUSE | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) is a dropper malware used by [MirrorFace](https://attack.mitre.org/groups/G1054) to extract and execute embedded payloads including [UPPERCUT](https://attack.mitre.org/software/S0275) components.(Citation: Trend Micro Earth Kasha Updates APR 2025) | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--uppercut | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) is a 32-bit HTTP-based backdoor that has been used by [menuPass](https://attack.mitre.org/groups/G0045) since at least 2017.(Citation: FireEye APT10 Sept 2018) Once thought to be exclusive to [menuPass](https://attack.mitre.org/groups/G0045), [UPPERCUT](https://attack.mitre.org/software/S0275) was also observed being used by [menuPass](https://attack.mitre.org/groups/G0045)-associated [MirrorFace](https://attack.mitre.org/groups/G1054) during [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060).(Citation: Trend Micro Earth Kasha Anel NOV 2024) | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--mitre--s9027 | ANELLDR | [ANELLDR](https://attack.mitre.org/software/S9027), a loader that has been in use since at least 2018, was designed to decrypt and execute [UPPERCUT](https://attack.mitre.org/software/S0275) in memory. [ANELLDR](https://attack.mitre.org/software/S9027) can use anti-analysis techniques and is known to share code overlap with [HiddenFace](https://attack.mitre.org/software/S9023).(Citation: Trend Micro Earth Kasha Anel NOV 2024)(Citation: ESET MirrorFace 2025) | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tasklist | Tasklist | The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--bitsadmin | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nltest | Nltest | [Nltest](https://attack.mitre.org/software/S0359) is a Windows command-line utility used to list domain controllers and enumerate domain trusts.(Citation: Nltest Manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nbtstat | nbtstat | [nbtstat](https://attack.mitre.org/software/S0102) is a utility used to troubleshoot NetBIOS name resolution. (Citation: TechNet Nbtstat) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--wevtutil | Wevtutil | [Wevtutil](https://attack.mitre.org/software/S0645) is a Windows command-line utility that enables administrators to retrieve information about event logs and publishers.(Citation: Wevtutil Microsoft Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mitre--s0099 | Arp | [Arp](https://attack.mitre.org/software/S0099) displays and modifies information about a system's Address Resolution Protocol (ARP) cache. (Citation: TechNet Arp) | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| tool--mitre--s1087 | AsyncRAT | [AsyncRAT](https://attack.mitre.org/software/S1087) is an open-source remote access tool originally available through the NYANxCAT Github repository that has been used in malicious campaigns.(Citation: Morphisec Snip3 May 2021)(Citation: Cisco Operation Layover September 2021)(Citation: Telefonica Snip3 December 2021) | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| tool--mitre--s1144 | FRP | [FRP](https://attack.mitre.org/software/S1144), which stands for Fast Reverse Proxy, is an openly available tool that is capable of exposing a server located behind a firewall or Network Address Translation (NAT) to the Internet. [FRP](https://attack.mitre.org/software/S1144) can support multiple protocols including TCP, UDP, and HTTP(S) and has been abused by threat actors to proxy command and control communications.(Citation: FRP GitHub)(Citation: Joint Cybersecurity Advisory Volt Typhoon June 2023)(Citation: RedCanary Mockingbird May 2020)(Citation: DFIR Phosphorus November 2021) | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| tool--mitre--s1071 | Rubeus | [Rubeus](https://attack.mitre.org/software/S1071) is a C# toolset designed for raw Kerberos interaction that has been used since at least 2020, including in ransomware operations.(Citation: GitHub Rubeus March 2023)(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020) | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |

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
| MirrorFaceハッカー、日本政府や政治家を2019年から標的に | phishing-campaign | 不明 | 不明 | 2025-01-10 | target--mitre-group--country--37778ff5178839a8849f, target--mitre-group--sector--1641197b302f5f13c922, target--mitre-group--sector--2cf49a251cc2f8d2ebc7 | malware--lodeinfo, malware--uppercut |  | victim--activity-rule--c31b37c188374ef1e875 | 日本の国家警察庁（NPA）と内閣サイバーセキュリティセンターは、中国政府支援のハッカー集団「MirrorFace」が2019年から日本の政府機関や政治家を標的にしていると発表。 MirrorFaceは、ネットワーク機器の脆弱性を悪用し、LODEINFOやANELなどのマルウェアを使用して情報を窃取。 攻撃の目的は、日本の先端技術や国家安全保障に関する情報の収集とされる。 同グループは、フィッシングメールを用いてマルウェアを配布し、選挙前には特に政治家を狙った攻撃を実施。 NPAは、MirrorFaceのハッカーによる3つの異なるキャンペーンを特定。 キャンペーンA（2019年～2023年）: シンクタンク、政府機関、政治家、メディアを標的に、マルウェアを含む電子メールを送信して情報を盗み出した。 | 高 | `source--daily-7947b8d03c9ba0e3f2c3` |
| 中国関連のMirrorFace、ANELおよびAsyncRATを展開し新たなサイバースパイ活動を実施 | phishing-campaign | 不明 | 不明 | 2025-03-19 | target--mitre-group--country--37778ff5178839a8849f | malware--lodeinfo, malware--uppercut | ttp--activity-rule--549dd264a2ed9f9674a3 | victim--activity-rule--ccf5ee5b782cacd2bcc6 | 中国と関連するサイバー攻撃グループMirrorFaceが、中央ヨーロッパの外交組織を標的に、新たなサイバースパイ活動「Operation AkaiRyū」を展開。 この攻撃では、カスタマイズされたAsyncRATの亜種と、以前APT10が使用していたバックドア「ANEL」を使用。 ANELの使用は、MirrorFaceが以前使用していたLODEINFOから切り替えた可能性を示すだけでなく、2018年後半または2019年頃に一度使用が中止されたANELが再び使用されたという点で重要。 攻撃手法として、スピアフィッシングメールを用いて、悪意のあるドキュメントやリンクを開かせ、マルウェアを展開。 攻撃者は、Visual Studio Codeのリモートトンネル機能を利用し、侵入したシステムへのステルスなアクセスを確立。 MirrorFaceは、以前は日本の組織を主な標的としていたが、今回の攻撃はその活動範囲の拡大を示唆。 | 高 | `source--daily-5e94939f6aa20488691a` |
| Operation AkaiRyū | campaign | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 2026-05-12 | target--mitre-group--country--37778ff5178839a8849f | malware--hiddenface, malware--mitre--s9027, malware--roaminghouse, malware--uppercut | ttp--mitre-campaign--0615aac85e80e41144bb, ttp--mitre-campaign--0a4418db0215ed4ccf84, ttp--mitre-campaign--0af294a0f653c7a81d52, ttp--mitre-campaign--0e9804d01deb8bf19360, ttp--mitre-campaign--3abe8e37a1d2524e7d64, ttp--mitre-campaign--3b2ff5f9ca53f8ea8ade, ttp--mitre-campaign--3fd9e61b853f21db61ad, ttp--mitre-campaign--532713ee28a924f410d8, ttp--mitre-campaign--63692a71dde473686716, ttp--mitre-campaign--6a0db95948eb07f9b5f5, ttp--mitre-campaign--6a328128a4311b902774, ttp--mitre-campaign--6d894165f79103fb7b13, ttp--mitre-campaign--75ec9b2edb2a98c362cf, ttp--mitre-campaign--7e1030935a3d088d3be4, ttp--mitre-campaign--83534bc4c31d99368763, ttp--mitre-campaign--91ba7e737caee9bcf0ad, ttp--mitre-campaign--a5a32c382b0bbc5912cc, ttp--mitre-campaign--ad818a515a67e865a3d7, ttp--mitre-campaign--b756e09f45825745c190, ttp--mitre-campaign--d17e381eae039fc34205, ttp--mitre-campaign--d24e6a9c75f618111462, ttp--mitre-campaign--d8e96572f8061584dfb7, ttp--mitre-campaign--dc824352b526298bc3a0, ttp--mitre-campaign--dfa3961b1f2192797c7b, ttp--mitre-campaign--e7114b46a9b944bc4da4, ttp--mitre-campaign--fef30df7c47664002861 | victim--activity-rule--2ce4157a78cf9939a231 | [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060) (Japanese for RedDragon) was a cyberespionage spearphishing campaign conducted by [MirrorFace](https://attack.mitre.org/groups/G1054) between June and September 2024 against entities in Japan and Central Europe. [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060) notably included the first reported targeting of a European entity by [MirrorFace](https://attack.mitre.org/groups/G1054), as well as their use of [UPPERCUT](https://attack.mitre.org/software/S0275), which was thought to be exclusive to [menuPass](https://attack.mitre.org/groups/G0045).(Citation: ESET MirrorFace 2025)(Citation: Trend Micro Earth Kasha Anel NOV 2024) | 高 | `source--mitre-attack-19-1` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| MirrorFaceハッカー、日本政府や政治家を2019年から標的に | MirrorFace | LODEINFO, UPPERCUT | 情報なし | 情報なし | 日本, メディア・報道, 政府・行政 | 被害事例: MirrorFaceハッカー、日本政府や政治家を2019年から標的に | 高 |
| 中国関連のMirrorFace、ANELおよびAsyncRATを展開し新たなサイバースパイ活動を実施 | MirrorFace | LODEINFO, UPPERCUT | T1566.002 Spearphishing Link | 情報なし | 日本 | 被害事例: 中国関連のMirrorFace、ANELおよびAsyncRATを展開し新たなサイバースパイ活動を実施 | 高 |
| Operation AkaiRyū | MirrorFace | HiddenFace, ANELLDR, ROAMINGHOUSE, UPPERCUT | T1082 System Information Discovery, T1070.004 File Deletion, T1585.002 Email Accounts, T1685.005 Clear Windows Event Logs, T1137.001 Office Template Macros, T1566.001 Spearphishing Attachment, T1588.002 Tool, T1016 System Network Configuration Discovery, T1608.005 Link Target, T1587.001 Malware, T1566.002 Spearphishing Link, T1059.003 Windows Command Shell, T1059.005 Visual Basic, T1047 Windows Management Instrumentation, T1219.001 IDE Tunneling, T1585.003 Cloud Accounts, T1127.001 MSBuild, T1036.008 Masquerade File Type, T1083 File and Directory Discovery, T1204.002 Malicious File, T1217 Browser Information Discovery, T1586.002 Email Accounts, T1059.001 PowerShell, T1553.002 Code Signing, T1219 Remote Access Tools, T1204.001 Malicious Link | 情報なし | 日本 | 被害事例: Operation AkaiRyū | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 日本 | [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--daily-5e94939f6aa20488691a`, `source--daily-7947b8d03c9ba0e3f2c3`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | 中央欧州 | MITRE ATT&CKのGroup概要でMirrorFaceの標的範囲として中央欧州が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 欧州 | MITRE ATT&CKのGroup概要でMirrorFaceの標的範囲として欧州が明示されている。 | 不明 | 不明 | 高 | `source--daily-5e94939f6aa20488691a`, `source--mitre-attack-19-1` |
| sectors | 教育・研究 | [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | メディア・報道 | [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. | 不明 | 不明 | 高 | `source--daily-7947b8d03c9ba0e3f2c3`, `source--mitre-attack-19-1` |
| sectors | 政府・行政 | [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. | 不明 | 不明 | 高 | `source--daily-7947b8d03c9ba0e3f2c3`, `source--mitre-attack-19-1` |
| sectors | 防衛・軍事 | [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 金融 | [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 製造・産業 | [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Operation AkaiRyū | 非公開 | anonymous | unknown | reported | target--mitre-group--country--37778ff5178839a8849f | malware--hiddenface, malware--mitre--s9027, malware--roaminghouse, malware--uppercut | ttp--mitre-campaign--0615aac85e80e41144bb, ttp--mitre-campaign--0a4418db0215ed4ccf84, ttp--mitre-campaign--0af294a0f653c7a81d52, ttp--mitre-campaign--0e9804d01deb8bf19360, ttp--mitre-campaign--3abe8e37a1d2524e7d64, ttp--mitre-campaign--3b2ff5f9ca53f8ea8ade, ttp--mitre-campaign--3fd9e61b853f21db61ad, ttp--mitre-campaign--532713ee28a924f410d8, ttp--mitre-campaign--63692a71dde473686716, ttp--mitre-campaign--6a0db95948eb07f9b5f5, ttp--mitre-campaign--6a328128a4311b902774, ttp--mitre-campaign--6d894165f79103fb7b13, ttp--mitre-campaign--75ec9b2edb2a98c362cf, ttp--mitre-campaign--7e1030935a3d088d3be4, ttp--mitre-campaign--83534bc4c31d99368763, ttp--mitre-campaign--91ba7e737caee9bcf0ad, ttp--mitre-campaign--a5a32c382b0bbc5912cc, ttp--mitre-campaign--ad818a515a67e865a3d7, ttp--mitre-campaign--b756e09f45825745c190, ttp--mitre-campaign--d17e381eae039fc34205, ttp--mitre-campaign--d24e6a9c75f618111462, ttp--mitre-campaign--d8e96572f8061584dfb7, ttp--mitre-campaign--dc824352b526298bc3a0, ttp--mitre-campaign--dfa3961b1f2192797c7b, ttp--mitre-campaign--e7114b46a9b944bc4da4, ttp--mitre-campaign--fef30df7c47664002861 |  | espionage: [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060) (Japanese for RedDragon) was a cyberespionage spearphishing campaign conducted by [MirrorFace](https://attack.mitre.org/groups/G1054) between June and September 2024 against entities in Japan and Central Europe. | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 2026-05-12 | 高 | `source--mitre-attack-19-1` |
| 被害事例: MirrorFaceハッカー、日本政府や政治家を2019年から標的に | 非公開 | anonymous | unknown | reported | target--mitre-group--country--37778ff5178839a8849f, target--mitre-group--sector--1641197b302f5f13c922, target--mitre-group--sector--2cf49a251cc2f8d2ebc7 | malware--lodeinfo, malware--uppercut |  | メール／メールアカウント, ネットワーク機器 |  | 不明 | 不明 | 2025-01-10 | 高 | `source--daily-7947b8d03c9ba0e3f2c3` |
| 被害事例: 中国関連のMirrorFace、ANELおよびAsyncRATを展開し新たなサイバースパイ活動を実施 | 非公開 | aggregate | multiple-organizations | reported | target--mitre-group--country--37778ff5178839a8849f | malware--lodeinfo, malware--uppercut | ttp--activity-rule--549dd264a2ed9f9674a3 | メール／メールアカウント | espionage: 中国関連のMirrorFace、ANELおよびAsyncRATを展開し新たなサイバースパイ活動を実施 | 不明 | 不明 | 2025-03-19 | 高 | `source--daily-5e94939f6aa20488691a` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1566.002 | Spearphishing Link | 攻撃手法として、スピアフィッシングメールを用いて、悪意のあるドキュメントやリンクを開かせ、マルウェアを展開。 |  | activity--daily-c40529bdb22ceb255b99 | 不明 | 不明 | 中 | `source--daily-5e94939f6aa20488691a` |
| Discovery | T1082 | System Information Discovery | <br>During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) collected system information.(Citation: Trend Micro Earth Kasha Anel NOV 2024) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) deleted delivered tools and files from compromised hosts.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used free email providers such as Gmail for spearphishing.(Citation: Trend Micro Earth Kasha Anel NOV 2024)(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) cleared Windows event logs post compromise.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Persistence | T1137.001 | Office Template Macros | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) loaded malicious Word templates containing VBA code leading to installation of [UPPERCUT](https://attack.mitre.org/software/S0275).(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) distributed crafted spearphishing emails containing malicious attachments.(Citation: ESET MirrorFace 2025)(Citation: Trend Micro Earth Kasha Anel NOV 2024) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) deployed multiple publicly available tools including PuTTY, [FRP](https://attack.mitre.org/software/S1144), and [Rubeus](https://attack.mitre.org/software/S1071).(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used [Arp](https://attack.mitre.org/software/S0099) and `dir` for discovery in compromised environments.(Citation: Trend Micro Earth Kasha Anel NOV 2024) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.005 | Link Target | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used links to direct victims to malicious files hosted on OneDrive.(Citation: Trend Micro Earth Kasha Anel NOV 2024)(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used  custom malware, as well as customized variants of publicly available tools.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) sent spearphishing emails with malicious OneDrive links.(Citation: Trend Micro Earth Kasha Anel NOV 2024) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used `cmd.exe` to run PowerShell commands to drop additional files on the compromised host.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used Word templates containing VBA code for malware execution.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used WMI to proxy execution of [UPPERCUT](https://attack.mitre.org/software/S0275).(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219.001 | IDE Tunneling | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) abused Visual Studio Code (VS Code) remote tunnels to gain access and execute code on compromised machines.(Citation: ESET MirrorFace 2025)<br> |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.003 | Cloud Accounts | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) established OneDrive accounts to host malicious payloads.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1127.001 | MSBuild | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used MSBuild to compile and execute its FaceXInjector injection tool.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.008 | Masquerade File Type | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) disguised LNK and SFX (self-extracting) files as Word documents to lure victims into opening malicious files.(Citation: Trend Micro Earth Kasha Anel NOV 2024)(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | <br>During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) enumerated file system details in compromised environments.(Citation: Trend Micro Earth Kasha Anel NOV 2024) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) lured victims into executing malicious payloads by opening email attachments.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) exported Chrome web data including contact information, keywords, autofill data, and stored credit card information.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used compromised accounts to send spearphishing emails.(Citation: Trend Micro Earth Kasha Anel NOV 2024) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used PowerShell in execution chains to drop additional files such as embedded CAB files.(Citation: Trend Micro Earth Kasha Anel NOV 2024)(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) abused a signed McAfee executable to load [UPPERCUT](https://attack.mitre.org/software/S0275).(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) used remote access tools including PuTTY.(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | During [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060), [MirrorFace](https://attack.mitre.org/groups/G1054) lured users into executing malicious payloads with links to resources hosted on OneDrive.(Citation: Trend Micro Earth Kasha Anel NOV 2024)(Citation: ESET MirrorFace 2025) |  | activity--operation-akairy | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | [MirrorFace](https://attack.mitre.org/groups/G1054) has dumped LSASS memory for credential access.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.002 | Security Account Manager | [MirrorFace](https://attack.mitre.org/groups/G1054) has used vssadmin to copy registry hives including SAM.(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.003 | NTDS | [MirrorFace](https://attack.mitre.org/groups/G1054) has dumped NTDS.dit through volume shadow copies.(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [MirrorFace](https://attack.mitre.org/groups/G1054) gathered data and files of interest from victim's systems.(Citation: Trend Micro Earth Kasha NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [Tasklist](https://attack.mitre.org/software/S0057) for discovery post compromise.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [ipconfig](https://attack.mitre.org/software/S0100) for reconnaissance.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [Ping](https://attack.mitre.org/software/S0097) for system discovery.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [MirrorFace](https://attack.mitre.org/groups/G1054) has used RDP to exfiltrate files of interest.(Citation: Trend Micro Earth Kasha NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [MirrorFace](https://attack.mitre.org/groups/G1054) has used SMB to copy malware between systems in compromised environments.(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [MirrorFace](https://attack.mitre.org/groups/G1054) has used Base64 encoded shellcode in infection chains to evade detection.(Citation: ITOCHU LODEINFO JAN 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used Windows native tools to enumerate user information.(Citation: Trend Micro Earth Kasha NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.008 | Masquerade File Type | [MirrorFace](https://attack.mitre.org/groups/G1054) has crafted malware payloads to appear as Privacy-Enhanced Mail (PEM) files.(Citation: ITOCHU LODEINFO JAN 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [MirrorFace](https://attack.mitre.org/groups/G1054) has leveraged WMIC on targeted systems post compromise.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.002 | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [MirrorFace](https://attack.mitre.org/groups/G1054) has used Secure File Transfer Protocol (SFTP) for file exfiltration.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [Tasklist](https://attack.mitre.org/software/S0057) on compromised hosts for discovery.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [MirrorFace](https://attack.mitre.org/groups/G1054) has used `cmd.exe` for malware execution, file discovery, and manual file manipulation.(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: Trend Micro Earth Kasha Updates APR 2025)(Citation: JPCERT MirrorFace JUL 2024)(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [MirrorFace](https://attack.mitre.org/groups/G1054) has used remote templates with VBA code in malware infection chains.(Citation: ITOCHU LODEINFO JAN 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [MirrorFace](https://attack.mitre.org/groups/G1054) has deleted directories containing malware and archives with files collected from the victim environment.(Citation: ESET MirrorFace DEC 2022)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: Trend Micro Earth Kasha Updates APR 2025)(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.002 | File Transfer Protocols | [MirrorFace](https://attack.mitre.org/groups/G1054) has used the the PuTTY suite Secure Copy Protocol (SCP) client for file transfer.(Citation: ESET MirrorFace DEC 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.002 | Remote Data Staging | [MirrorFace](https://attack.mitre.org/groups/G1054) has gathered data and files of interest on a single victim machine.(Citation: Trend Micro Earth Kasha NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has employed malicious macros and native Windows tools such as csvde.exe, nltest.exe and quser.exe for discovery.(Citation: ITOCHU LODEINFO JAN 2024)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has run commands to check the content of folders on compromised hosts and has specifically targeted files with .doc, .ppt, .xls, .jtd, .eml, .xps, and .pdf extensions.(Citation: ESET MirrorFace DEC 2022)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [MirrorFace](https://attack.mitre.org/groups/G1054) has used native Windows tools to obtain domain user information.(Citation: Trend Micro Earth Kasha NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | [MirrorFace](https://attack.mitre.org/groups/G1054) has used the GO Simple Tunnel (GOST) proxy tool.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.001 | Local Email Collection | [MirrorFace](https://attack.mitre.org/groups/G1054) has exfiltrated stored emails from compromised hosts.(Citation: ESET MirrorFace DEC 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [MirrorFace](https://attack.mitre.org/groups/G1054) has exploited vulnerabilities in Fortigate and Array AG devices for initial access.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mirrorface--b9e4ffba14793168`, `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [MirrorFace](https://attack.mitre.org/groups/G1054) has lured victims into opening crafted Word, Excel, and SFX files for execution.(Citation: Kaspersky LODEINFO OCT 2022)(Citation: ESET MirrorFace DEC 2022)(Citation: ITOCHU LODEINFO JAN 2024)(Citation: Trend Micro Earth Kasha Updates APR 2025) |  |  | 不明 | 不明 | 高 | `source--mirrorface--b9e4ffba14793168`, `source--mitre-attack-19-1` |
| Stealth | T1221 | Template Injection | [MirrorFace](https://attack.mitre.org/groups/G1054) has used remote template injection to retrieve malicious payloads from the C2.(Citation: ITOCHU LODEINFO JAN 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has run `nltest.exe  /domain_trusts` on compromised systems to discover domain relationships.(Citation: Trend Micro Earth Kasha NOV 2024)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | h BRI; targets Southeast Asian Governments, Telecommunications, Australia, Japan Exploit public-facing apps (T1190) Spear phishing (T1566) Encrypted webshells (T1505.003) MirrorFace (Earth Kasha) Espionage targeting Japanese media, political organizations, research institutions Spear phishing (T1566) Malware deployment (T1204.002) Mustang Panda Espionage including against Southeast Asian law enforcement a |  |  | 不明 | 不明 | 中 | `source--mirrorface--b9e4ffba14793168` |
| Defense Impairment | T1553.002 | Code Signing | [MirrorFace](https://attack.mitre.org/groups/G1054) has abused a known Microsoft digital signature verification issues to append encrypted data to digital signatures that still appear to be validly signed.(Citation: ESET MirrorFace DEC 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Defense Impairment, Persistence | T1556.002 | Password Filter DLL | [MirrorFace](https://attack.mitre.org/groups/G1054) has used a tool named MRSAStealer as a password filter to collect credentials on password changes.(Citation: ESET MirrorFace DEC 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [MirrorFace](https://attack.mitre.org/groups/G1054) has used rar.exe and the Makecab utility to archive files of interest prior to exfiltration.(Citation: ESET MirrorFace DEC 2022)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | nexus) Espionage aligned with BRI; targets Southeast Asian Governments, Telecommunications, Australia, Japan Exploit public-facing apps (T1190) Spear phishing (T1566) Encrypted webshells (T1505.003) MirrorFace (Earth Kasha) Espionage targeting Japanese media, political organizations, research institutions Spear phishing (T1566) Malware deployment (T1204.002) Mustang Panda Espionage including against Southeast Asian law enforcement a |  |  | 不明 | 不明 | 中 | `source--mirrorface--b9e4ffba14793168` |
| Initial Access | T1566.001 | Spearphishing Attachment | [MirrorFace](https://attack.mitre.org/groups/G1054) has sent spearphishing emails with malicious attachments to deliver malware payloads.(Citation: Kaspersky LODEINFO OCT 2022)(Citation: ESET MirrorFace DEC 2022)(Citation: ITOCHU LODEINFO JAN 2024) |  |  | 不明 | 不明 | 高 | `source--mirrorface--b9e4ffba14793168`, `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [MirrorFace](https://attack.mitre.org/groups/G1054) has embedded OneDrive URLs in emails leading to malicious file installation.(Citation: Trend Micro Earth Kasha Updates APR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [MirrorFace](https://attack.mitre.org/groups/G1054) has used legitimate EXE files to load malicious DLLs via sideloading.(Citation: Kaspersky LODEINFO OCT 2022)(Citation: ESET MirrorFace DEC 2022)(Citation: ITOCHU LODEINFO JAN 2024)(Citation: Trend Micro Earth Kasha NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1574.002 | MITRE ATT&CK T1574.002 | summary/2023/eset_apt_activity_report_t32022.pdf {"page": 4} MirrorFace lcode containing a TurboSlate downloader (T1574.002 [3]). It’s unusual for Goblin Panda to target European countries but this might be a change in the group’s targeting, as observed with Mustang Panda in recent months. MirrorFace In September and October 2022, ESET researchers detected a new spearphishing campaign carried out by |  |  | 不明 | 不明 | 中 | `source--mirrorface--b9e4ffba14793168` |
| Resource Development | T1587.001 | Malware | [MirrorFace](https://attack.mitre.org/groups/G1054) has created and continued to develop custom strains of malware including [LODEINFO](https://attack.mitre.org/software/S9020).(Citation: ESET MirrorFace DEC 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [MirrorFace](https://attack.mitre.org/groups/G1054) has used tools including the Secure Copy Protocol (SCP) client from PuTTY and [Cobalt Strike](https://attack.mitre.org/software/S0154).(Citation: ESET MirrorFace DEC 2022)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591 | Gather Victim Org Information | [MirrorFace](https://attack.mitre.org/groups/G1054) has placed specific content in phishing emails to target members of particular political parties.(Citation: ESET MirrorFace DEC 2022)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1614.001 | System Language Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has deployed shellcode to check for Japanese Microsoft Office settings.(Citation: ITOCHU LODEINFO JAN 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | [MirrorFace](https://attack.mitre.org/groups/G1054) has sent targeted emails purporting to be from a Japanese political party’s PR department.(Citation: ESET MirrorFace DEC 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [MirrorFace](https://attack.mitre.org/groups/G1054) has disabled Windows Defender in compromised environments.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | [MirrorFace](https://attack.mitre.org/groups/G1054) has deleted Windows event logs.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686.003 | Windows Host Firewall | [MirrorFace](https://attack.mitre.org/groups/G1054) can modify the system firewall to allow communication to certain ports.(Citation: JPCERT MirrorFace JUL 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 15件（`artifacts.csv`）

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
| source--daily-5e94939f6aa20488691a | 中国関連のMirrorFace、ANELおよびAsyncRATを展開し新たなサイバースパイ活動を実施 | thehackernews.com | 2025-03-19 | https://thehackernews.com/2025/03/china-linked-mirrorface-deploys-anel.html | osint-report | TLP:CLEAR | 中 |
| source--daily-7947b8d03c9ba0e3f2c3 | MirrorFaceハッカー、日本政府や政治家を2019年から標的に | bleepingcomputer.com | 2025-01-10 | https://www.bleepingcomputer.com/news/security/mirrorface-hackers-targeting-japanese-govt-politicians-since-2019/ | osint-report | TLP:CLEAR | 中 |
| source--mirrorface--53e785c48f775c1e | Threat Report 2026 v4 |  | 2026 | summary/2026/Threat Report 2026 v4.pdf | report | TLP:CLEAR | 中 |
| source--mirrorface--544767cd28a98390 | eset apt activity report q4 2023 q1 2024 |  | 2023 | summary/2024/eset-apt-activity-report-q4-2023-q1-2024.pdf | report | TLP:CLEAR | 中 |
| source--mirrorface--5774303f03d7d653 | eset threat report h12025 |  | 不明 | summary/2025/eset-threat-report-h12025.pdf | report | TLP:CLEAR | 中 |
| source--mirrorface--9e0b11aef7c89e7c | eset apt activity report q42022 q12023 |  | 不明 | summary/2023/eset_apt_activity_report_q42022_q12023.pdf | report | TLP:CLEAR | 中 |
| source--mirrorface--b9e4ffba14793168 | mirrorface |  | 不明 | actor_profile/evidence/mirrorface.csv | structured-data | TLP:CLEAR | 中 |
| source--mirrorface--cb1d03e29a3ab476 | eset apt activity report t32022 |  | 不明 | summary/2023/eset_apt_activity_report_t32022.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
