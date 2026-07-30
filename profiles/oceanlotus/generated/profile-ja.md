# OceanLotus 脅威アクタープロファイル

- プロファイルID: `actor--oceanlotus`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

OceanLotusの標準化プロファイル。リポジトリ内の専用資料9件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **OceanLotus**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT32 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| APT-C-00 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| BISMUTH | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Canvas Cyclone | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| SeaLotus | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| SectorF01 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 14; mapping requires review. |
| CyberOne Security, CyberOne Technologies, Hành Tinh Company Limited, Planet and Diacauso | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 14; mapping requires review. |
| Vietnam | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 14; mapping requires review. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [APT32](https://attack.mitre.org/groups/G0050) is a suspected Vietnam-based threat group that has been active since at least 2014. The group has targeted multiple private sector industries as well as foreign governments, dissidents, and journalists with a strong focus on Southeast Asian countries like Vietnam, the Philippines, Laos, and Cambodia. They have extensively used strategic web compromises to compromise victims.(Citation: FireEye APT32 May 2017)(Citation: Volexity OceanLotus Nov 2017)(Citation: ESET OceanLotus) |
| Capability | RotaJakiro, KOMPROGO, Kerrdown, WINDSHIELD, SOUNDBITE, Cobalt Strike, OSX_OCEANLOTUS.D, Goopy, Denis, PHOREAL, Unique suite & OTS, Microsoft ActiveMime file attachments, Net, ipconfig, Arp, netsh, Mimikatz |
| Infrastructure |  |
| Victim | This threat actor targets organizations of interest to the Vietnamese government for espionage purposes. Victims have included human rights organizations, research institutes and maritime construction firms in China, and media organizations. Heavily targeting the automotive sector since 2018. |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 32, OceanLotus, SeaLotus | canonical-name | 高 | Vietnam | https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html<br>https://www.welivesecurity.com/wp-content/uploads/2018/03/ESET_OceanLotus.pdf<br>https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/SpyRATsofOceanLotusMalwareWhitePaper.pdf |
| etda-threat-group-cards | Bismuth | multiple-name-intersection | 高 | Vietnam | https://www.microsoft.com/security/blog/2020/11/30/threat-actor-leverages-coin-miner-techniques-to-stay-under-the-radar-heres-how-to-spot-them/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Bismuth&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Canvas Cyclone | canonical-name | 高 | Vietnam | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT32 | canonical-name | 高 | VN, Vietnam | https://attack.mitre.org/groups/G0050/<br>https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html<br>https://www.cybereason.com/labs-operation-cobalt-kitty-a-large-scale-apt-in-asia-carried-out-by-the-oceanlotus-group/ |
| misp-microsoft-activity-group | Canvas Cyclone | canonical-name | 高 | VN, Vietnam | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | APT32 - G0050 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0050<br>https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html<br>https://www.volexity.com/blog/2017/11/06/oceanlotus-blossoms-mass-digital-surveillance-and-exploitation-of-asean-nations-the-media-human-rights-and-civil-society/ |
| misp-mitre-intrusion-set | APT32 - G0050 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0050<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://www.amnestyusa.org/wp-content/uploads/2021/02/Click-and-Bait_Vietnamese-Human-Rights-Defenders-Targeted-with-Spyware-Attacks.pdf |
| misp-360net | 海莲花 - APT-C-00 | canonical-name | 高 | vietnam | https://apt.360.net/report/apts/93.html<br>https://apt.360.net/report/apts/1.html<br>https://apt.360.net/report/apts/94.html |

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
| malware--rotajakiro | RotaJakiro | [RotaJakiro](https://attack.mitre.org/software/S1078) is a 64-bit Linux backdoor used by [APT32](https://attack.mitre.org/groups/G0050). First seen in 2018, it uses a plugin architecture to extend capabilities. [RotaJakiro](https://attack.mitre.org/software/S1078) can determine it's permission level and execute according to access type (`root` or `user`).(Citation: RotaJakiro 2021 netlab360 analysis)(Citation: netlab360 rotajakiro vs oceanlotus) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--komprogo | KOMPROGO | [KOMPROGO](https://attack.mitre.org/software/S0156) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050) that is capable of process, file, and registry management. (Citation: FireEye APT32 May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--kerrdown | Kerrdown | [Kerrdown](https://attack.mitre.org/software/S0585) is a custom downloader that has been used by [APT32](https://attack.mitre.org/groups/G0050) since at least 2018 to install spyware from a server on the victim's network.(Citation: Amnesty Intl. Ocean Lotus February 2021)(Citation: Unit 42 KerrDown February 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--windshield | WINDSHIELD | [WINDSHIELD](https://attack.mitre.org/software/S0155) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050). (Citation: FireEye APT32 May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--soundbite | SOUNDBITE | [SOUNDBITE](https://attack.mitre.org/software/S0157) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050). (Citation: FireEye APT32 May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--osx-oceanlotus-d | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) is a macOS backdoor used by [APT32](https://attack.mitre.org/groups/G0050). First discovered in 2015, [APT32](https://attack.mitre.org/groups/G0050) has continued to make improvements using a plugin architecture to extend capabilities, specifically using `.dylib` files. [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can also determine it's permission level and execute according to access type (`root` or `user`).(Citation: Unit42 OceanLotus 2017)(Citation: TrendMicro MacOS April 2018)(Citation: Trend Micro MacOS Backdoor November 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--goopy | Goopy | [Goopy](https://attack.mitre.org/software/S0477) is a Windows backdoor and Trojan used by [APT32](https://attack.mitre.org/groups/G0050) and shares several similarities to another backdoor used by the group ([Denis](https://attack.mitre.org/software/S0354)). [Goopy](https://attack.mitre.org/software/S0477) is named for its impersonation of the legitimate Google Updater executable.(Citation: Cybereason Cobalt Kitty 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--denis | Denis | [Denis](https://attack.mitre.org/software/S0354) is a Windows backdoor and Trojan used by [APT32](https://attack.mitre.org/groups/G0050). [Denis](https://attack.mitre.org/software/S0354) shares several similarities to the [SOUNDBITE](https://attack.mitre.org/software/S0157) backdoor and has been used in conjunction with the [Goopy](https://attack.mitre.org/software/S0477) backdoor.(Citation: Cybereason Oceanlotus May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--phoreal | PHOREAL | [PHOREAL](https://attack.mitre.org/software/S0158) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050). (Citation: FireEye APT32 May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--unique-suite-ots | Unique suite & OTS | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--microsoft-activemime-file-attachments | Microsoft ActiveMime file attachments | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--arp | Arp | [Arp](https://attack.mitre.org/software/S0099) displays and modifies information about a system's Address Resolution Protocol (ARP) cache. (Citation: TechNet Arp) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netsh | netsh | [netsh](https://attack.mitre.org/software/S0108) is a scripting utility used to interact with networking components on local or remote systems. (Citation: TechNet Netsh) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cobalt Kitty | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Cobalt Kitty

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イラン | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてイランが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インド | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-360net` |
| countries | インドネシア | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-360net` |
| countries | カンボジア | MITRE ATT&CKのGroup概要でOceanLotusの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | シンガポール | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてシンガポールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | デンマーク | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてデンマークが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ネパール | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてネパールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | バングラデシュ | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてバングラデシュが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-360net` |
| countries | フィリピン | MITRE ATT&CKのGroup概要でOceanLotusの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | フランス | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブルネイ | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてブルネイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | MITRE ATT&CKのGroup概要でOceanLotusの標的国として明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-360net` |
| countries | ミャンマー | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国としてミャンマーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ラオス | MITRE ATT&CKのGroup概要でOceanLotusの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | Targeting text mentions china. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| countries | 日本 | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでOceanLotusの標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | アジア | MITRE ATT&CKのGroup概要でOceanLotusの標的範囲としてアジアが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 南アジア | インド、ネパール、バングラデシュで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-360net` |
| regions | 東アジア | 中国、日本、韓国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | MITRE ATT&CKのGroup概要でOceanLotusの標的範囲として東南アジアが明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | オランダ、デンマーク、ドイツ、フランス、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | Education and Research | Targeting text indicates the Education and Research sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Media | Targeting text indicates the Media sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1001 | Data Obfuscation | Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码经过混淆处理，对变量名函数名等进行简单命名后如下： |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Credential Access | T1003 | OS Credential Dumping | [APT32](https://attack.mitre.org/groups/G0050) used GetPassword_x64 to harvest credentials.(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | [APT32](https://attack.mitre.org/groups/G0050) used Mimikatz and customized versions of Windows Credential Dumper to harvest credentials.(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | TLP：WHITE 腾讯安全御见威胁情报中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscat |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1007 | System Service Discovery | TLP：WHITE 腾讯安全御见威胁情报中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Cus |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1012 | Query Registry | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor can query the Windows Registry to gather system information. (Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [APT32](https://attack.mitre.org/groups/G0050) used the <code>ipconfig /all</code> command to gather the IP address from the system.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [APT32](https://attack.mitre.org/groups/G0050) has enumerated DC servers using the command <code>net group "Domain Controllers" /domain</code>. The group has also used the <code>ping</code> command.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [APT32](https://attack.mitre.org/groups/G0050) used [Net](https://attack.mitre.org/software/S0039) to use Windows' hidden network shares to copy their tools to remote machines for execution.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1024 | MITRE ATT&CK T1024 | io Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码经过混淆处理，对变量名函数名等进行简单命名后如下： |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Collection | T1025 | Data from Removable Media | TLP：WHITE 腾讯安全御见威胁情报中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Por |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Stealth | T1027 | Obfuscated Files or Information | 0 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery T1082 System Inform |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Stealth | T1027.010 | Command Obfuscation | [APT32](https://attack.mitre.org/groups/G0050) has used the `Invoke-Obfuscation` framework to obfuscate their PowerShell.(Citation: FireEye APT32 May 2017)(Citation: GitHub Invoke-Obfuscation)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.011 | Fileless Storage | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has stored its configuration in a registry key.(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [APT32](https://attack.mitre.org/groups/G0050) has performed code obfuscation, including encoding payloads using Base64 and using a framework called "Dont-Kill-My-Cat (DKMC). [APT32](https://attack.mitre.org/groups/G0050) also encrypts the library used for network exfiltration with AES-256 in CBC mode in their macOS backdoor.(Citation: FireEye APT32 May 2017)(Citation: GitHub Invoke-Obfuscation)(Citation: ESET OceanLotus)(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017)(Citation: ESET OceanLotus Mar 2019)(Citation: ESET OceanLotus macOS April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.016 | Junk Code Insertion | [APT32](https://attack.mitre.org/groups/G0050) includes garbage code to mislead anti-malware software and researchers.(Citation: ESET OceanLotus)(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [APT32](https://attack.mitre.org/groups/G0050) collected the victim's username and executed the <code>whoami</code> command on the victim's machine. [APT32](https://attack.mitre.org/groups/G0050) executed shellcode to collect the username on the victim's machine. (Citation: FireEye APT32 April 2020)(Citation: ESET OceanLotus)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [APT32](https://attack.mitre.org/groups/G0050) has disguised a Cobalt Strike beacon as a Flash Installer.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Stealth | T1036.003 | Rename Legitimate Utilities | [APT32](https://attack.mitre.org/groups/G0050) has moved and renamed pubprn.vbs to a .txt file to avoid detection.(Citation: Twitter ItsReallyNick APT32 pubprn Masquerade) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [APT32](https://attack.mitre.org/groups/G0050) has used hidden or non-printing characters to help masquerade service names, such as appending a Unicode no-break space character to a legitimate service name. [APT32](https://attack.mitre.org/groups/G0050) has also impersonated the legitimate Flash installer file name "install_flashplayer.exe".(Citation: FireEye APT32 May 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [APT32](https://attack.mitre.org/groups/G0050) has renamed a NetCat binary to kb-10233.exe to masquerade as a Windows update. [APT32](https://attack.mitre.org/groups/G0050) has also renamed a Cobalt Strike beacon payload to install_flashplayers.exe. (Citation: Cybereason Cobalt Kitty 2017)(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has exfiltrated data using the already opened channel with its C&C server.(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1043 | Commonly Used Port | 05 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码 |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1046 | Network Service Discovery | [APT32](https://attack.mitre.org/groups/G0050) performed network scanning on the network to search for open ports, services, OS finger-printing, and other vulnerabilities.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1047 | Windows Management Instrumentation | [APT32](https://attack.mitre.org/groups/G0050) used WMI to deploy their tools on remote machines and to gather information about the Outlook process.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor can exfiltrate data by encoding it in the subdomain field of DNS packets.(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [APT32](https://attack.mitre.org/groups/G0050) used the <code>netstat -anpo tcp</code> command to display TCP connections on the victim's machine.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053 | Scheduled Task/Job | TLP：WHITE 腾讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [APT32](https://attack.mitre.org/groups/G0050) has used scheduled tasks to persist on victim systems.(Citation: FireEye APT32 May 2017)(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017)(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | [APT32](https://attack.mitre.org/groups/G0050) malware has injected a Cobalt Strike beacon into Rundll32.exe.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056 | Input Capture | on T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery T1082 System Information Discovery |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Collection, Credential Access | T1056.001 | Keylogging | [APT32](https://attack.mitre.org/groups/G0050) has abused the PasswordChangeNotify to monitor for and capture account password changes.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | 2 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery T1082 System Information Discovery |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1059 | Command and Scripting Interpreter | [APT32](https://attack.mitre.org/groups/G0050) has used COM scriptlets to download Cobalt Strike beacons.(Citation: Cybereason Cobalt Kitty 2017)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [APT32](https://attack.mitre.org/groups/G0050) has used PowerShell-based tools, PowerShell one-liners, and shellcode loaders for execution.(Citation: FireEye APT32 May 2017)(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [APT32](https://attack.mitre.org/groups/G0050) has used cmd.exe for execution.(Citation: Cybereason Cobalt Kitty 2017)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [APT32](https://attack.mitre.org/groups/G0050) has used macros, COM scriptlets, and VBS scripts.(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | [APT32](https://attack.mitre.org/groups/G0050) has used JavaScript for drive-by downloads and C2 communications.(Citation: Cybereason Cobalt Kitty 2017)(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1060 | MITRE ATT&CK T1060 | TLP：WHITE 腾讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1065 | MITRE ATT&CK T1065 | lipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码经过混淆处理，对变量名函数名等进行简单命名后如下： |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [APT32](https://attack.mitre.org/groups/G0050) has used CVE-2016-7255 to escalate privileges.(Citation: FireEye APT32 May 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [APT32](https://attack.mitre.org/groups/G0050)'s macOS backdoor can receive a “delete” command.(Citation: ESET OceanLotus macOS April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.006 | Timestomp | [APT32](https://attack.mitre.org/groups/G0050) has used scheduled task raw XML with a backdated timestamp of June 2, 2016. The group has also set the creation time of the files dropped by the second stage of the exploit to match the creation time of kernel32.dll. Additionally, [APT32](https://attack.mitre.org/groups/G0050) has used a random value to modify the timestamp of the file storing the clientID.(Citation: FireEye APT32 May 2017)(Citation: ESET OceanLotus Mar 2019)(Citation: ESET OceanLotus macOS April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [APT32](https://attack.mitre.org/groups/G0050) has used JavaScript that communicates over HTTP or HTTPS to attacker controlled domains to download additional frameworks. The group has also used downloaded encrypted payloads over HTTP.(Citation: Volexity OceanLotus Nov 2017)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.003 | Mail Protocols | [APT32](https://attack.mitre.org/groups/G0050) has used email for C2 via an Office macro.(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Lateral Movement | T1072 | Software Deployment Tools | [APT32](https://attack.mitre.org/groups/G0050) compromised McAfee ePO to move laterally by distributing malware as a software deployment task.(Citation: FireEye APT32 May 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | [APT32](https://attack.mitre.org/groups/G0050) has used legitimate local admin account credentials.(Citation: FireEye APT32 May 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [APT32](https://attack.mitre.org/groups/G0050) has collected the OS version and computer name from victims. One of the group's backdoors can also query the Windows Registry to gather system information, and another macOS backdoor performs a fingerprint of the machine on its first connection to the C&C server. [APT32](https://attack.mitre.org/groups/G0050) executed shellcode to identify the name of the infected host.(Citation: ESET OceanLotus)(Citation: ESET OceanLotus Mar 2019)(Citation: ESET OceanLotus macOS April 2019)(Citation: FireEye APT32 April 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1083 | File and Directory Discovery | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor possesses the capability to list files and directories on a machine. (Citation: ESET OceanLotus Mar 2019)	<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1085 | MITRE ATT&CK T1085 | Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1087.001 | Local Account | [APT32](https://attack.mitre.org/groups/G0050) enumerated administrative users using the commands <code>net localgroup administrators</code>.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1094 | MITRE ATT&CK T1094 | T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码经过混淆处理，对变量名函数名等进行简单命名后如下： |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1099 | MITRE ATT&CK T1099 | T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery T1082 System Information Discovery |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Command And Control | T1102 | Web Service | [APT32](https://attack.mitre.org/groups/G0050) has used Dropbox, Amazon S3, and Google Drive to host malicious downloads.(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [APT32](https://attack.mitre.org/groups/G0050) has added JavaScript to victim websites to download additional frameworks that profile and compromise website visitors.(Citation: Volexity OceanLotus Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | hardware.com cdnwebmedia.com 43.251.100.20 43.254.217.67 114.118.80.233 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1107 | MITRE ATT&CK T1107 | 讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discove |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has modified the Windows Registry to store the backdoor's configuration. (Citation: ESET OceanLotus Mar 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Collection | T1113 | Screen Capture | y Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Collection | T1115 | Clipboard Data | 534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1117 | MITRE ATT&CK T1117 | TLP：WHITE 腾讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Collection | T1123 | Audio Capture | 中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1129 | Shared Modules | 43.251.100.20 43.254.217.67 114.118.80.233 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1135 | Network Share Discovery | [APT32](https://attack.mitre.org/groups/G0050) used the <code>net view</code> command to show all shares available, including the administrative shares such as <code>C$</code> and <code>ADMIN$</code>.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Persistence | T1137 | Office Application Startup | [APT32](https://attack.mitre.org/groups/G0050) have replaced Microsoft Outlook's VbaProject.OTM file to install a backdoor macro for persistence.(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Ser |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1179 | MITRE ATT&CK T1179 | TLP：WHITE 腾讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Cr |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Initial Access | T1189 | Drive-by Compromise | [APT32](https://attack.mitre.org/groups/G0050) has infected victims by tricking them into visiting compromised watering hole websites.(Citation: ESET OceanLotus)(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1193 | MITRE ATT&CK T1193 | us.melvillepitcairn.com upgrade.coldriverhardware.com cdnwebmedia.com 43.251.100.20 43.254.217.67 114.118.80.233 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1203 | Exploitation for Client Execution | [APT32](https://attack.mitre.org/groups/G0050) has used RTF document that includes an exploit to execute malicious code. (CVE-2017-11882)(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1204 | User Execution | T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1204.001 | Malicious Link | [APT32](https://attack.mitre.org/groups/G0050) has lured targets to download a Cobalt Strike beacon by including a malicious link within spearphishing emails.(Citation: Cybereason Cobalt Kitty 2017)(Citation: Volexity Ocean Lotus November 2020)(Citation: Amnesty Intl. Ocean Lotus February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [APT32](https://attack.mitre.org/groups/G0050) has attempted to lure users to execute a malicious dropper delivered via a spearphishing attachment.(Citation: ESET OceanLotus)(Citation: Cybereason Oceanlotus May 2017)(Citation: ESET OceanLotus Mar 2019)(Citation: FireEye APT32 April 2020)(Citation: Amnesty Intl. Ocean Lotus February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1216.001 | PubPrn | [APT32](https://attack.mitre.org/groups/G0050) has used PubPrn.vbs within execution scripts to execute malware, possibly bypassing defenses.(Citation: Twitter ItsReallyNick Status Update APT32 PubPrn) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | [APT32](https://attack.mitre.org/groups/G0050) has used mshta.exe for code execution.(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.010 | Regsvr32 | [APT32](https://attack.mitre.org/groups/G0050) created a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053) that used regsvr32.exe to execute a COM scriptlet that dynamically downloaded a backdoor and injected it into memory. The group has also used regsvr32 to run their backdoor.(Citation: ESET OceanLotus Mar 2019)(Citation: FireEye APT32 May 2017)(Citation: Cybereason Cobalt Kitty 2017)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [APT32](https://attack.mitre.org/groups/G0050) malware has used rundll32.exe to execute an initial infection process.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1222.002 | Linux and Mac Permissions | [APT32](https://attack.mitre.org/groups/G0050)'s macOS backdoor changes the permission of the file it wants to execute to 755.(Citation: ESET OceanLotus macOS April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1223 | MITRE ATT&CK T1223 | ttachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Persistence | T1505.003 | Web Shell | [APT32](https://attack.mitre.org/groups/G0050) has used Web shells to maintain access to victim websites.(Citation: Volexity OceanLotus Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1534 | Internal Spearphishing | TLP：WHITE 腾讯安全御见威胁情报中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cr |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [APT32](https://attack.mitre.org/groups/G0050) modified Windows Services to ensure PowerShell scripts were loaded on the system. [APT32](https://attack.mitre.org/groups/G0050) also creates a Windows service to establish persistence.(Citation: ESET OceanLotus)(Citation: Cybereason Cobalt Kitty 2017)(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [APT32](https://attack.mitre.org/groups/G0050) established persistence using Registry Run keys, both to execute PowerShell and VBS scripts as well as to execute their backdoor directly.(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017)(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | [APT32](https://attack.mitre.org/groups/G0050) has used pass the hash for lateral movement.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.003 | Pass the Ticket | [APT32](https://attack.mitre.org/groups/G0050) successfully gained remote access by using pass the ticket.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.002 | Credentials in Registry | [APT32](https://attack.mitre.org/groups/G0050) used Outlook Credential Dumper to harvest credentials stored in Windows registry.(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560 | Archive Collected Data | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has used LZMA compression and RC4 encryption before exfiltration.(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | [APT32](https://attack.mitre.org/groups/G0050)'s macOS backdoor hides the clientID file via a chflags function.(Citation: ESET OceanLotus macOS April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.003 | Hidden Window | [APT32](https://attack.mitre.org/groups/G0050) has used the WindowStyle parameter to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows. (Citation: FireEye APT32 May 2017) (Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.004 | NTFS File Attributes | [APT32](https://attack.mitre.org/groups/G0050) used NTFS alternate data streams to hide their payloads.(Citation: Cybereason Cobalt Kitty 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [APT32](https://attack.mitre.org/groups/G0050) has sent spearphishing emails with a malicious executable disguised as a document or spreadsheet.(Citation: ESET OceanLotus)(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017)(Citation: ESET OceanLotus Mar 2019)(Citation: FireEye APT32 April 2020)(Citation: Amnesty Intl. Ocean Lotus February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [APT32](https://attack.mitre.org/groups/G0050) has sent spearphishing emails containing malicious links.(Citation: ESET OceanLotus)(Citation: Cybereason Oceanlotus May 2017)(Citation: FireEye APT32 April 2020)(Citation: Volexity Ocean Lotus November 2020)(Citation: Amnesty Intl. Ocean Lotus February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has used Windows services as a way to execute its malicious payload. (Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [APT32](https://attack.mitre.org/groups/G0050) has deployed tools after moving laterally using administrative accounts.(Citation: Cybereason Cobalt Kitty 2017)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | An [APT32](https://attack.mitre.org/groups/G0050) backdoor can use HTTP over a non-standard TCP port (e.g 14146) which is specified in the backdoor configuration.(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [APT32](https://attack.mitre.org/groups/G0050) ran legitimately-signed executables from Symantec and McAfee which load a malicious DLL. The group also side-loads its backdoor by dropping a library and a legitimate, signed executable (AcroTranscoder).(Citation: Cybereason Oceanlotus May 2017)(Citation: Cybereason Cobalt Kitty 2017)(Citation: ESET OceanLotus Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [APT32](https://attack.mitre.org/groups/G0050) has set up and operated websites to gather information and deliver malware.(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | [APT32](https://attack.mitre.org/groups/G0050) has set up Dropbox, Amazon S3, and Google Drive to host malicious downloads.(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | [APT32](https://attack.mitre.org/groups/G0050) has set up Facebook pages in tandem with fake websites.(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [APT32](https://attack.mitre.org/groups/G0050) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002) and [Cobalt Strike](https://attack.mitre.org/software/S0154), and a variety of other open-source tools from GitHub.(Citation: FireEye APT32 May 2017)(Citation: Cybereason Oceanlotus May 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | [APT32](https://attack.mitre.org/groups/G0050) has conducted targeted surveillance against activists and bloggers.(Citation: Amnesty Intl. Ocean Lotus February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | [APT32](https://attack.mitre.org/groups/G0050) has collected e-mail addresses for activists and bloggers in order to target them with spyware.(Citation: Amnesty Intl. Ocean Lotus February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | [APT32](https://attack.mitre.org/groups/G0050) has used malicious links to direct users to web pages designed to harvest credentials.(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [APT32](https://attack.mitre.org/groups/G0050) has hosted malicious payloads in Dropbox, Amazon S3, and Google Drive for use during targeting.(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.004 | Drive-by Target | [APT32](https://attack.mitre.org/groups/G0050) has stood up websites containing numerous articles and content scraped from the Internet to make them appear legitimate, but some of these pages include malicious JavaScript to profile the potential victim or infect them via a fake software update.(Citation: Volexity Ocean Lotus November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | [APT32](https://attack.mitre.org/groups/G0050) has cleared select event log entries.(Citation: FireEye APT32 May 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 335件
- IOC観測: 383件
- 複数攻撃で観測: 0件
- 要レビュー候補: 182件
- 非IOC artifact観測: 327件（`artifacts.csv`）

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
| source--oceanlotus--a7175b421ca1736c | ESET OceanLotus |  | 不明 | Oceanlotus/ESET_OceanLotus.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--d9ef73283beaecf5 | OceanLotus' Attacks to Indochinese Peninsula Evolution of Targets, Techniques and Procedure |  | 不明 | Oceanlotus/OceanLotus' Attacks to Indochinese Peninsula Evolution of Targets, Techniques and Procedure.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--0a5ba4ea429a9916 | OceanLotus Steganography Malware Analysis White Paper |  | 不明 | Oceanlotus/OceanLotus-Steganography-Malware-Analysis-White-Paper.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--9a1ee229cc72c74b | Oceanlotus APK sample |  | 不明 | Oceanlotus/Oceanlotus-APK-sample.TXT | text-data | TLP:CLEAR | 中 |
| source--oceanlotus--8c52284824684bb3 | README |  | 不明 | Oceanlotus/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--oceanlotus--4987b0d4cde44760 | Stairwell threat report The origin of APT32 macros |  | 不明 | Oceanlotus/Stairwell-threat-report-The-origin-of-APT32-macros.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--e15849fad928c3c1 | apt32 report 2019 |  | 2019 | Oceanlotus/apt32_report_2019.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--5bb5ce3ec25f97e9 | hunting rule |  | 不明 | Oceanlotus/hunting-rule.txt | text-data | TLP:CLEAR | 中 |
| source--oceanlotus--692f1686b5c44964 | README |  | 不明 | Oceanlotus/sample/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-360net | MISP 360.net suspected-victim fields | MISP Project / 360.net | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
