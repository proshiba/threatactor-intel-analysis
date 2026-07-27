# MirrorFace 脅威アクタープロファイル

- プロファイルID: `actor--mirrorface`
- 状態: draft
- 更新日時: 2026-07-27T11:04:33Z
- 構造バージョン: 1.0.0

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
| malware--hiddenface | HiddenFace | [HiddenFace](https://attack.mitre.org/software/S9023) is a modular backdoor developed and used exclusively by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2021. [HiddenFace](https://attack.mitre.org/software/S9023) can communicate both actively and passively and has been used against political and academic targets.(Citation: JPCERT MirrorFace JUL 2024)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: Trend Micro Earth Kasha Updates APR 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lodeinfo | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) is a fileless backdoor malware first identified in 2020 that has been used by actors including [MirrorFace](https://attack.mitre.org/groups/G1054), primarily against media, diplomatic, governmental, and public sector organizations in Japan.(Citation: Kaspersky LODEINFO OCT 2022)(Citation: ITOCHU LODEINFO JAN 2024)(Citation: ESET MirrorFace DEC 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--mirrorstealer | MirrorStealer | [MirrorStealer](https://attack.mitre.org/software/S9022) is a credential stealer that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2022 to steal credentials from various applications, including browsers and email clients. [MirrorStealer](https://attack.mitre.org/software/S9022) has been delivered directly into system memory via commands issued by [LODEINFO](https://attack.mitre.org/software/S9020).(Citation: ESET MirrorFace DEC 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--noopldr | NOOPLDR | [NOOPLDR](https://attack.mitre.org/software/S9025) is a shellcode loader with XML/C# and DLL versions that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) to load [HiddenFace](https://attack.mitre.org/software/S9023).(Citation: Trend Micro Earth Kasha NOV 2024)<br> | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--roaminghouse | ROAMINGHOUSE | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) is a dropper malware used by [MirrorFace](https://attack.mitre.org/groups/G1054) to extract and execute embedded payloads including [UPPERCUT](https://attack.mitre.org/software/S0275) components.(Citation: Trend Micro Earth Kasha Updates APR 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--uppercut | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) is a 32-bit HTTP-based backdoor that has been used by [menuPass](https://attack.mitre.org/groups/G0045) since at least 2017.(Citation: FireEye APT10 Sept 2018) Once thought to be exclusive to [menuPass](https://attack.mitre.org/groups/G0045), [UPPERCUT](https://attack.mitre.org/software/S0275) was also observed being used by [menuPass](https://attack.mitre.org/groups/G0045)-associated [MirrorFace](https://attack.mitre.org/groups/G1054) during [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060).(Citation: Trend Micro Earth Kasha Anel NOV 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| MirrorFaceハッカー、日本政府や政治家を2019年から標的に | phishing-campaign | 不明 | 不明 | 2025-01-10 | 日本の国家警察庁（NPA）と内閣サイバーセキュリティセンターは、中国政府支援のハッカー集団「MirrorFace」が2019年から日本の政府機関や政治家を標的にしていると発表。 MirrorFaceは、ネットワーク機器の脆弱性を悪用し、LODEINFOやANELなどのマルウェアを使用して情報を窃取。 攻撃の目的は、日本の先端技術や国家安全保障に関する情報の収集とされる。 同グループは、フィッシングメールを用いてマルウェアを配布し、選挙前には特に政治家を狙った攻撃を実施。 NPAは、MirrorFaceのハッカーによる3つの異なるキャンペーンを特定。 キャンペーンA（2019年～2023年）: シンクタンク、政府機関、政治家、メディアを標的に、マルウェアを含む電子メールを送信して情報を盗み出した。 | 高 | `source--daily-7947b8d03c9ba0e3f2c3` |
| 中国関連のMirrorFace、ANELおよびAsyncRATを展開し新たなサイバースパイ活動を実施 | phishing-campaign | 不明 | 不明 | 2025-03-19 | 中国と関連するサイバー攻撃グループMirrorFaceが、中央ヨーロッパの外交組織を標的に、新たなサイバースパイ活動「Operation AkaiRyū」を展開。 この攻撃では、カスタマイズされたAsyncRATの亜種と、以前APT10が使用していたバックドア「ANEL」を使用。 ANELの使用は、MirrorFaceが以前使用していたLODEINFOから切り替えた可能性を示すだけでなく、2018年後半または2019年頃に一度使用が中止されたANELが再び使用されたという点で重要。 攻撃手法として、スピアフィッシングメールを用いて、悪意のあるドキュメントやリンクを開かせ、マルウェアを展開。 攻撃者は、Visual Studio Codeのリモートトンネル機能を利用し、侵入したシステムへのステルスなアクセスを確立。 MirrorFaceは、以前は日本の組織を主な標的としていたが、今回の攻撃はその活動範囲の拡大を示唆。 | 高 | `source--daily-5e94939f6aa20488691a` |
| Operation AkaiRyū | campaign | 2004-06-01T04:00:00.000Z | 2004-09-01T04:00:00.000Z | 2026-05-12 | [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060) (Japanese for RedDragon) was a cyberespionage spearphishing campaign conducted by [MirrorFace](https://attack.mitre.org/groups/G1054) between June and September 2024 against entities in Japan and Central Europe. [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060) notably included the first reported targeting of a European entity by [MirrorFace](https://attack.mitre.org/groups/G1054), as well as their use of [UPPERCUT](https://attack.mitre.org/software/S0275), which was thought to be exclusive to [menuPass](https://attack.mitre.org/groups/G0045).(Citation: ESET MirrorFace 2025)(Citation: Trend Micro Earth Kasha Anel NOV 2024) | 高 | `source--mitre-attack-19-1` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.002 | Security Account Manager | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.003 | NTDS | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.008 | Masquerade File Type | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.002 | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.002 | File Transfer Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.002 | Remote Data Staging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.001 | Local Email Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mirrorface--b9e4ffba14793168`, `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mirrorface--b9e4ffba14793168`, `source--mitre-attack-19-1` |
| Stealth | T1221 | Template Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | h BRI; targets Southeast Asian Governments, Telecommunications, Australia, Japan Exploit public-facing apps (T1190) Spear phishing (T1566) Encrypted webshells (T1505.003) MirrorFace (Earth Kasha) Espionage targeting Japanese media, political organizations, research institutions Spear phishing (T1566) Malware deployment (T1204.002) Mustang Panda Espionage including against Southeast Asian law enforcement a |  |  | 不明 | 不明 | 中 | `source--mirrorface--b9e4ffba14793168` |
| Defense Impairment | T1553.002 | Code Signing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Defense Impairment, Persistence | T1556.002 | Password Filter DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | nexus) Espionage aligned with BRI; targets Southeast Asian Governments, Telecommunications, Australia, Japan Exploit public-facing apps (T1190) Spear phishing (T1566) Encrypted webshells (T1505.003) MirrorFace (Earth Kasha) Espionage targeting Japanese media, political organizations, research institutions Spear phishing (T1566) Malware deployment (T1204.002) Mustang Panda Espionage including against Southeast Asian law enforcement a |  |  | 不明 | 不明 | 中 | `source--mirrorface--b9e4ffba14793168` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mirrorface--b9e4ffba14793168`, `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1574.002 | MITRE ATT&CK T1574.002 | summary/2023/eset_apt_activity_report_t32022.pdf {"page": 4} MirrorFace lcode containing a TurboSlate downloader (T1574.002 [3]). It’s unusual for Goblin Panda to target European countries but this might be a change in the group’s targeting, as observed with Mustang Panda in recent months. MirrorFace In September and October 2022, ESET researchers detected a new spearphishing campaign carried out by |  |  | 不明 | 不明 | 中 | `source--mirrorface--b9e4ffba14793168` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591 | Gather Victim Org Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1614.001 | System Language Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686.003 | Windows Host Firewall | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
