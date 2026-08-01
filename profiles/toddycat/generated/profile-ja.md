# ToddyCat 脅威アクタープロファイル

- プロファイルID: `actor--toddycat`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

ToddyCatの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **ToddyCat**
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
| Adversary | [ToddyCat](https://attack.mitre.org/groups/G1022) is a sophisticated threat group that has been active since at least 2020 using custom loaders and malware in multi-stage infection chains against government and military targets across Europe and Asia.(Citation: Kaspersky ToddyCat June 2022)(Citation: Kaspersky ToddyCat Check Logs October 2023) |
| Capability | Ninja, LoFiSe, China Chopper, Cobalt Strike, Samurai, Pcexter, Net, netstat, Ping |
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
| etda-threat-group-cards | ToddyCat | canonical-name | 高 | China | https://securelist.com/toddycat/106799/<br>https://securelist.com/toddycat-keep-calm-and-check-logs/110696/<br>https://securelist.com/toddycat-traffic-tunneling-data-extraction-tools/112443/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-0247 | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | ToddyCat | canonical-name | 高 |  | https://www.bleepingcomputer.com/news/security/new-toddycat-apt-group-targets-exchange-servers-in-asia-europe/<br>https://securelist.com/toddycat/106799/<br>https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/ |
| misp-microsoft-activity-group | Storm-0247 | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | ToddyCat - G1022 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1022<br>https://securelist.com/toddycat-keep-calm-and-check-logs/110696/<br>https://securelist.com/toddycat/106799/ |
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
| malware--china-chopper | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.(Citation: Lee 2013) It has been used by several threat groups.(Citation: Dell TG-3390)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Rapid7 HAFNIUM Mar 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lofise | LoFiSe | [LoFiSe](https://attack.mitre.org/software/S1101) has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) since at least 2023 to identify and collect files of interest on targeted systems.(Citation: Kaspersky ToddyCat Check Logs October 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ninja | Ninja | [Ninja](https://attack.mitre.org/software/S1100) is a malware developed in C++ that has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) to penetrate networks and control remote systems since at least 2020.  [Ninja](https://attack.mitre.org/software/S1100) is possibly part of a post exploitation toolkit exclusively used by [ToddyCat](https://attack.mitre.org/groups/G1022) and allows multiple operators to work simultaneously on the same machine. [Ninja](https://attack.mitre.org/software/S1100) has been used against government and military entities in Europe and Asia and observed in specific infection chains being deployed by [Samurai](https://attack.mitre.org/software/S1099).(Citation: Kaspersky ToddyCat June 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pcexter | Pcexter | [Pcexter](https://attack.mitre.org/software/S1102) is an uploader that has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) since at least 2023 to exfiltrate stolen files.(Citation: Kaspersky ToddyCat Check Logs October 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--samurai | Samurai | [Samurai](https://attack.mitre.org/software/S1099) is a passive backdoor that has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) since at least 2020. [Samurai](https://attack.mitre.org/software/S1099) allows arbitrary C# code execution and is used with multiple modules for remote administration and lateral movement.(Citation: Kaspersky ToddyCat June 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netstat | netstat | [netstat](https://attack.mitre.org/software/S0104) is an operating system utility that displays active TCP connections, listening ports, and network statistics. (Citation: TechNet Netstat) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| ロシアのハッカーグループToddyCat、先進的ツールを用いて大規模データ窃盗 | malware-campaign | 不明 | 不明 | 2024-04-23 | target--mitre-group--sector--4b54b35dbf4d37f11090, target--mitre-group--sector--ec7e1256d113b34011d0 |  |  | victim--activity-rule--5c3a350426f23f252837 | ToddyCatがアジア太平洋地域の主に政府機関（一部は防衛関連）を狙う Samraiというバックドアを利用してアクセス維持 データ収集とアップロードの自動化ツールを使用 OneDriveを通じてデータを外部へ転送 防御機能を回避する技術を積極的に使用 | 高 | `source--daily-2abe7ad9ba2e35aecc22` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| ロシアのハッカーグループToddyCat、先進的ツールを用いて大規模データ窃盗 | ToddyCat | 情報なし | 情報なし | 情報なし | 政府・行政, 防衛・軍事 | 被害事例: ロシアのハッカーグループToddyCat、先進的ツールを用いて大規模データ窃盗 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イラン | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてイランが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | インド | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | インドネシア | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ウズベキスタン | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてウズベキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | カザフスタン | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてカザフスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | キルギス | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてキルギスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | スロバキア | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてスロバキアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | タイ | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ロシア | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでToddyCatの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | アジア | 活動「ロシアのハッカーグループToddyCat、先進的ツールを用いて大規模データ窃盗」の記述で標的地域としてアジアが明示されている。 | 不明 | 不明 | 中 | `source--daily-2abe7ad9ba2e35aecc22` |
| regions | アジア太平洋 | 活動「ロシアのハッカーグループToddyCat、先進的ツールを用いて大規模データ窃盗」の記述で標的地域としてアジア太平洋が明示されている。 | 不明 | 不明 | 中 | `source--daily-2abe7ad9ba2e35aecc22` |
| regions | 中央アジア | ウズベキスタン、カザフスタン、キルギスで確認された標的・被害事例を中央アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南アジア | アフガニスタン、インド、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | インドネシア、タイ、ベトナム、マレーシアで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東欧 | スロバキア、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | スロバキア、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 政府・行政 | [ToddyCat](https://attack.mitre.org/groups/G1022) is a sophisticated threat group that has been active since at least 2020 using custom loaders and malware in multi-stage infection chains against government and military targets across Europe and Asia.(Citation: Kaspersky ToddyCat June 2022)(Citation: Kaspersky ToddyCat Check Logs October 2023) | 不明 | 不明 | 高 | `source--daily-2abe7ad9ba2e35aecc22`, `source--mitre-attack-19-1` |
| sectors | 防衛・軍事 | [ToddyCat](https://attack.mitre.org/groups/G1022) is a sophisticated threat group that has been active since at least 2020 using custom loaders and malware in multi-stage infection chains against government and military targets across Europe and Asia.(Citation: Kaspersky ToddyCat June 2022)(Citation: Kaspersky ToddyCat Check Logs October 2023) | 不明 | 不明 | 高 | `source--daily-2abe7ad9ba2e35aecc22`, `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ロシアのハッカーグループToddyCat、先進的ツールを用いて大規模データ窃盗 | 非公開 | anonymous | unknown | reported | target--mitre-group--sector--4b54b35dbf4d37f11090, target--mitre-group--sector--ec7e1256d113b34011d0 |  |  |  |  | 不明 | 不明 | 2024-04-23 | 高 | `source--daily-2abe7ad9ba2e35aecc22` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | [ToddyCat](https://attack.mitre.org/groups/G1022) has run scripts to collect documents from targeted hosts.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | tachment (T1566.001) • Command and Scripting Interpreter: Windows Command Shell (T1059.003) • Modify Registry (T1112) • System Network Configuration Discovery (T1016) ToddyCat – относительно новая APT-группировка, ответственная за многочисленные атаки, обнаруженные с декабря 2020 года, на высо - копоставленные организации в Европе и Азии. Затронутые органи- зации, как правительственные, так |  |  | 不明 | 不明 | 中 | `source--toddycat--d3ad8145a5cd7324` |
| Discovery | T1018 | Remote System Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has used `ping %REMOTE_HOST%` for post exploit discovery.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [ToddyCat](https://attack.mitre.org/groups/G1022) has used locally mounted network shares for lateral movement through targated environments.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [ToddyCat](https://attack.mitre.org/groups/G1022) has used the name `debug.exe` for malware components.(Citation: Kaspersky ToddyCat June 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [ToddyCat](https://attack.mitre.org/groups/G1022) has used WMI to execute scripts for post exploit document collection.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has used `netstat -anop tcp` to discover TCP connections to compromised hosts.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [ToddyCat](https://attack.mitre.org/groups/G1022) has used scheduled tasks to execute discovery commands and scripts for collection.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has run `cmd /c start /b tasklist` to enumerate processes.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [ToddyCat](https://attack.mitre.org/groups/G1022) has used Powershell scripts to perform post exploit collection.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [ToddyCat](https://attack.mitre.org/groups/G1022) has used .bat scripts and `cmd` for execution on compromised hosts.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--toddycat--d3ad8145a5cd7324` |
| Discovery | T1069.002 | Domain Groups | [ToddyCat](https://attack.mitre.org/groups/G1022) has executed `net group "domain admins" /dom` for discovery on compromised machines.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf {"page": 52} ToddyCat Protocol: Web Protocols T1071.001 The service process mentioned above connected to 154.202.56[.]211:443 and made a POST request: hxxps:/ /154.202.56[.]211/collector/3.0/. This URL matches the URL path structure used by ToddyCat. Ingress Tool Transfer T1105 Several scripts and executable files were downloaded fro |  |  | 不明 | 不明 | 中 | `source--toddycat--d3ad8145a5cd7324` |
| Collection | T1074.002 | Remote Data Staging | [ToddyCat](https://attack.mitre.org/groups/G1022) manually transferred collected files to an exfiltration host using xcopy.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [ToddyCat](https://attack.mitre.org/groups/G1022) has used compromised domain admin credentials to mount local network shares.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has run scripts to enumerate recently modified documents having either a .pdf, .doc, .docx, .xls or .xlsx extension.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [ToddyCat](https://attack.mitre.org/groups/G1022) has run `net user %USER% /dom` for account discovery.(Citation: Kaspersky ToddyCat Check Logs October 2023)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1095 | Non-Application Layer Protocol | [ToddyCat](https://attack.mitre.org/groups/G1022) has used a passive backdoor that receives commands with UDP packets.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | 56[.]211:443 and made a POST request: hxxps:/ /154.202.56[.]211/collector/3.0/. This URL matches the URL path structure used by ToddyCat. Ingress Tool Transfer T1105 Several scripts and executable files were downloaded from this C2 server to the target host. Interestingly, PowerShell scripts were downloaded several times but with different MD5 hashes. Th |  |  | 不明 | 不明 | 中 | `source--toddycat--d3ad8145a5cd7324` |
| Execution | T1106 | Native API | [ToddyCat](https://attack.mitre.org/groups/G1022) has used `WinExec` to execute commands received from C2 on compromised hosts.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | p Folder (T1547.001) • Phishing: Spearphishing Attachment (T1566.001) • Command and Scripting Interpreter: Windows Command Shell (T1059.003) • Modify Registry (T1112) • System Network Configuration Discovery (T1016) ToddyCat – относительно новая APT-группировка, ответственная за многочисленные атаки, обнаруженные с декабря 2020 года, на высо - копоставленные организации в Европе и Азии. Затронутые органи- зации, как правительственные, так |  |  | 不明 | 不明 | 中 | `source--toddycat--d3ad8145a5cd7324` |
| Initial Access | T1190 | Exploit Public-Facing Application | [ToddyCat](https://attack.mitre.org/groups/G1022) has exploited the ProxyLogon vulnerability (CVE-2021-26855) to compromise Exchange Servers at multiple organizations.(Citation: Kaspersky ToddyCat June 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) can determine is Kaspersky software is running on an endpoint by running `cmd /c wmic process where name="avp.exe"`.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | g to ToddyCat. When investigating the alert, we focused on a suspicious DLL that was run as a Windows service (Create or Modify System Process: Windows Service T1543.003). The ToddyCat alert was triggered by their typical pattern o |  |  | 不明 | 不明 | 中 | `source--toddycat--d3ad8145a5cd7324` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | огий. ToddyCat Регион Начало операции TOP Mitre АТР, Европа, Россия и СНГ Декабрь 2020 • Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (T1547.001) • Phishing: Spearphishing Attachment (T1566.001) • Command an |  |  | 不明 | 不明 | 中 | `source--toddycat--d3ad8145a5cd7324` |
| Collection | T1560.001 | Archive via Utility | [ToddyCat](https://attack.mitre.org/groups/G1022) has leveraged  xcopy, 7zip, and RAR to stage and compress collected documents prior to exfiltration.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.003 | Hidden Window | [ToddyCat](https://attack.mitre.org/groups/G1022) has hidden malicious scripts using `powershell.exe -windowstyle hidden`. (Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | ТР, Европа, Россия и СНГ Декабрь 2020 • Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (T1547.001) • Phishing: Spearphishing Attachment (T1566.001) • Command an |  |  | 不明 | 不明 | 中 | `source--toddycat--d3ad8145a5cd7324` |
| Initial Access | T1566.003 | Spearphishing via Service | [ToddyCat](https://attack.mitre.org/groups/G1022) has sent loaders configured to run [Ninja](https://attack.mitre.org/software/S1100) as zip archives via Telegram.(Citation: Kaspersky ToddyCat June 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [ToddyCat](https://attack.mitre.org/groups/G1022) has used a DropBox uploader to exfiltrate stolen files.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1680 | Local Storage Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has collected information on bootable drives including model, vendor, and serial numbers.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | Prior to executing a backdoor [ToddyCat](https://attack.mitre.org/groups/G1022)  has run `cmd /c start /b netsh advfirewall firewall add rule name="SGAccessInboundRule" dir=in protocol=udp action=allow localport=49683` to allow the targeted system to receive UDP packets on port 49683.(Citation: Kaspersky ToddyCat Check Logs October 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
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
| source--daily-2abe7ad9ba2e35aecc22 | ロシアのハッカーグループToddyCat、先進的ツールを用いて大規模データ窃盗 | thehackernews.com | 2024-04-23 | https://thehackernews.com/2024/04/russian-hacker-group-toddycat-uses.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--toddycat--1c043c570ef7a25f | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--toddycat--7a8cb570834e3afd | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--toddycat--d3ad8145a5cd7324 | toddycat |  | 不明 | actor_profile/evidence/toddycat.csv | structured-data | TLP:CLEAR | 中 |
| source--toddycat--f93d8ac1da540be8 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
