# Aquatic Panda 脅威アクタープロファイル

- プロファイルID: `actor--aquatic-panda`
- 状態: draft
- 更新日時: 2026-07-29T23:11:59Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Aquatic Pandaの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Aquatic Panda**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

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
| Adversary | [Aquatic Panda](https://attack.mitre.org/groups/G0143) is a suspected China-based threat group with a dual mission of intelligence collection and industrial espionage. Active since at least May 2020, [Aquatic Panda](https://attack.mitre.org/groups/G0143) has primarily targeted entities in the telecommunications, technology, and government sectors.(Citation: CrowdStrike AQUATIC PANDA December 2021) |
| Capability | Winnti for Linux, Cobalt Strike, Winnti for Windows, njRAT, ShadowPad, Wevtutil |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Aquatic Panda | canonical-name | 高 | China | https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Aquatic+Panda&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Charcoal Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Earth Lusca | canonical-name | 高 | CN | https://hello.global.ntt/-/media/ntt/global/insights/white-papers/the-operations-of-winnti-group.pdf<br>https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf<br>https://www.recordedfuture.com/chinese-group-tag-22-targets-nepal-philippines-taiwan |
| misp-microsoft-activity-group | Charcoal Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Aquatic Panda - G0143 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0143<br>https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/ |
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
| malware--njrat | njRAT | [njRAT](https://attack.mitre.org/software/S0385) is a remote access tool (RAT) that was first observed in 2012. It has been used by threat actors in the Middle East.(Citation: Fidelis njRAT June 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--shadowpad | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) is a modular backdoor that was first identified in a supply chain compromise of the NetSarang software in mid-July 2017. The malware was originally thought to be exclusively used by [APT41](https://attack.mitre.org/groups/G0096), but has since been observed to be used by various Chinese threat activity groups. (Citation: Recorded Future RedEcho Feb 2021)(Citation: Securelist ShadowPad Aug 2017)(Citation: Kaspersky ShadowPad Aug 2017)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--winnti-for-linux | Winnti for Linux | [Winnti for Linux](https://attack.mitre.org/software/S0430) is a trojan, seen since at least 2015, designed specifically for targeting Linux systems. Reporting indicates the winnti malware family is shared across a number of actors including [Winnti Group](https://attack.mitre.org/groups/G0044). The Windows variant is tracked separately under [Winnti for Windows](https://attack.mitre.org/software/S0141).(Citation: Chronicle Winnti for Linux May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--winnti-for-windows | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) is a modular remote access Trojan (RAT) that has been used likely by multiple groups to carry out intrusions in various regions since at least 2010, including by one group referred to as the same name, [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: Kaspersky Winnti April 2013)(Citation: Microsoft Winnti Jan 2017)(Citation: Novetta Winnti April 2015)(Citation: 401 TRG Winnti Umbrella May 2018). The Linux variant is tracked separately under [Winnti for Linux](https://attack.mitre.org/software/S0430).(Citation: Chronicle Winnti for Linux May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に | cyber-espionage | 2022-01 | 2022-10 | 2025-03-22 | target--activity-rule--country--0c17dd6f4a5e07d5f7d6, target--activity-rule--country--2113be5c12a85bcb7b3b, target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--95e363d6dfa8c6f2ecbb, target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--activity-rule--sector--e7608f51421ca8b1e297, target--mitre-group--sector--b35d0af2e7c9f2e2e6ec | malware--shadowpad |  | victim--activity-rule--157e8e01ba0178ccb52b | 中国のAPTグループ「Aquatic Panda」は、2022年1月から10月にかけて、7つの組織を標的としたスパイ活動を行った。 標的には、台湾、ハンガリー、トルコ、タイ、フランス、米国の政府、カトリック慈善団体、NGO、シンクタンクが含まれていた。 攻撃には、ShadowPad、SodaMaster、Spyderなどのマルウェアが使用された。 Aquatic Pandaは、少なくとも2019年から活動している中国のサイバースパイ集団で、Winntiグループの一部とされる。 2022年の攻撃では、ScatterBee、ShadowPad、Spyder、SodaMaster、RPipeCommanderの5つのマルウェアファミリーが使用された。 この活動はESETによって「Operation FishMedley」とコードネームが付けられた。 | 高 | `source--daily-a9818c561227639f76fb` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | タイ | 活動「中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に」の記述で標的・被害国として明示されている。 | 2022-01 | 2022-10 | 中 | `source--daily-a9818c561227639f76fb`, `source--target-audit-misp-threat-actor` |
| countries | トルコ | 活動「中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に」の記述で標的・被害国として明示されている。 | 2022-01 | 2022-10 | 中 | `source--daily-a9818c561227639f76fb` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ナイジェリア | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国としてナイジェリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ネパール | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国としてネパールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ハンガリー | 活動「中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に」の記述で標的・被害国として明示されている。 | 2022-01 | 2022-10 | 中 | `source--daily-a9818c561227639f76fb` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | フランス | 活動「中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に」の記述で標的として明示された国・地域。 | 2022-01 | 2022-10 | 中 | `source--daily-a9818c561227639f76fb`, `source--target-audit-misp-threat-actor` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | モンゴル | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国としてモンゴルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 中国 | 活動「中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に」の記述で標的として明示された国・地域。 | 2022-01 | 2022-10 | 中 | `source--daily-a9818c561227639f76fb`, `source--target-audit-misp-threat-actor` |
| countries | 台湾 | 活動「中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に」の記述で標的として明示された国・地域。 | 2022-01 | 2022-10 | 中 | `source--daily-a9818c561227639f76fb`, `source--target-audit-misp-threat-actor` |
| countries | 日本 | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 米国 | 活動「中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に」の記述で標的として明示された国・地域。 | 2022-01 | 2022-10 | 中 | `source--daily-a9818c561227639f76fb`, `source--target-audit-misp-threat-actor` |
| countries | 香港 | 構造化OSINTの被害国フィールドでAquatic Pandaの標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 中東 | アラブ首長国連邦、トルコで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-a9818c561227639f76fb`, `source--target-audit-misp-threat-actor` |
| regions | 東アジア | モンゴル、中国、台湾、日本、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-a9818c561227639f76fb`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | タイ、フィリピン、ベトナムで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-a9818c561227639f76fb`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | トルコ、ドイツ、ハンガリー、フランスで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-a9818c561227639f76fb`, `source--target-audit-misp-threat-actor` |
| sectors | 非営利・市民社会 | 活動「中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に」の記述で標的として明示された産業。 | 2022-01 | 2022-10 | 中 | `source--daily-a9818c561227639f76fb` |
| sectors | 教育・研究 | 活動「中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に」の記述で標的として明示された産業。 | 2022-01 | 2022-10 | 中 | `source--daily-a9818c561227639f76fb` |
| sectors | 情報通信 | Active since at least May 2020, [Aquatic Panda](https://attack.mitre.org/groups/G0143) has primarily targeted entities in the telecommunications, technology, and government sectors.(Citation: CrowdStrike AQUATIC PANDA December 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | Active since at least May 2020, [Aquatic Panda](https://attack.mitre.org/groups/G0143) has primarily targeted entities in the telecommunications, technology, and government sectors.(Citation: CrowdStrike AQUATIC PANDA December 2021) | 2022-01 | 2022-10 | 高 | `source--daily-a9818c561227639f76fb`, `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--0c17dd6f4a5e07d5f7d6, target--activity-rule--country--2113be5c12a85bcb7b3b, target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--95e363d6dfa8c6f2ecbb, target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--activity-rule--sector--e7608f51421ca8b1e297, target--mitre-group--sector--b35d0af2e7c9f2e2e6ec | malware--shadowpad |  |  | espionage: 中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に | 2022-01 | 2022-10 | 2025-03-22 | 高 | `source--daily-a9818c561227639f76fb` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted to harvest credentials through LSASS memory dumping.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [Aquatic Panda](https://attack.mitre.org/groups/G0143) captured local Windows security event log data from victim machines using the <code>wevtutil</code> utility to extract contents to an <code>evtx</code> output file.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted to discover services for third party EDR products.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021 | Remote Services | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used remote scheduled tasks to install malicious software on victim systems during lateral movement actions.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Aquatic Panda](https://attack.mitre.org/groups/G0143) leveraged stolen credentials to move laterally via RDP in victim environments.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used remote shares to enable lateral movement in victim environments.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used SSH with captured user credentials to move laterally in victim environments.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has encoded PowerShell commands in Base64.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) gathers information on recently logged-in users on victim devices.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [Aquatic Panda](https://attack.mitre.org/groups/G0143) created new, malicious services using names such as <code>Windows User Service</code> to attempt to blend in with legitimate items on victim systems.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Aquatic Panda](https://attack.mitre.org/groups/G0143) renamed or moved malicious binaries to legitimate locations to evade defenses and blend into victim environments.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used WMI for lateral movement in victim environments.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has downloaded additional scripts and executed Base64 encoded commands in PowerShell.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted and failed to run Bash commands on a Windows host by passing them to <code>cmd /C</code>.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used malicious shell scripts in Linux environments following access via SSH to install Linux versions of Winnti malware.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.003 | Clear Command History | [Aquatic Panda](https://attack.mitre.org/groups/G0143) cleared command history in Linux environments to remove traces of activity after operations.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has deleted malicious executables from compromised machines.(Citation: CrowdStrike AQUATIC PANDA December 2021)(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used multiple mechanisms to capture valid user accounts for victim domains to enable lateral movement and access to additional hosts in victim environments.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used native OS commands to understand privilege levels and system details.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087 | Account Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used the <code>last</code> command in Linux environments to identify recently logged-in users on victim machines.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has downloaded additional malware onto compromised hosts.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Aquatic Panda](https://attack.mitre.org/groups/G0143) modified the victim registry to enable the `RestrictedAdmin` mode feature, allowing for pass the hash behaviors to function via RDP.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used rundll32.exe to proxy execution of a malicious DLL file identified as a keylogging binary.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted to discover third party endpoint detection and response (EDR) tools on compromised systems.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [Aquatic Panda](https://attack.mitre.org/groups/G0143) created new Windows services for persistence that masqueraded as legitimate Windows services via name change.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used a registry edit to enable a Windows feature called <code>RestrictedAdmin</code> in victim environments. This change allowed [Aquatic Panda](https://attack.mitre.org/groups/G0143) to leverage "pass the hash" mechanisms as the alteration allows for RDP connections with a valid account name and hash only, without possessing a cleartext password value.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used several publicly available tools, including WinRAR and 7zip, to compress collected files and memory dumps prior to exfiltration.(Citation: CrowdStrike AQUATIC PANDA December 2021)(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used DLL search-order hijacking to load `exe`, `dll`, and `dat` files into memory.(Citation: CrowdStrike AQUATIC PANDA December 2021) [Aquatic Panda](https://attack.mitre.org/groups/G0143) loaded a malicious DLL into the legitimate Windows Security Health Service executable (<code>SecurityHealthService.exe</code>) to execute malicious code on victim systems.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.006 | Dynamic Linker Hijacking | [Aquatic Panda](https://attack.mitre.org/groups/G0143) modified the <code>ld.so</code> preload file in Linux environments to enable persistence for Winnti malware.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has acquired and used [njRAT](https://attack.mitre.org/software/S0385) in its operations.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has acquired and used [Cobalt Strike](https://attack.mitre.org/software/S0154) in its operations.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used publicly accessible DNS logging services to identify servers vulnerable to Log4j (CVE 2021-44228).(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1654 | Log Enumeration | [Aquatic Panda](https://attack.mitre.org/groups/G0143) enumerated logs related to authentication in Linux environments prior to deleting selective entries for defense evasion purposes.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted to stop endpoint detection and response (EDR) tools on compromised systems.(Citation: CrowdStrike AQUATIC PANDA December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | [Aquatic Panda](https://attack.mitre.org/groups/G0143) clears Windows Event Logs following activity to evade defenses.(Citation: Crowdstrike HuntReport 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 8件（`artifacts.csv`）

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
| source--aquatic-panda--4aaf88a8200e317f | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--aquatic-panda--ad17e73e8f441dc4 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--aquatic-panda--d7f361259dc43cd9 | 2022 Global Threat Report |  | 2022 | summary/2022/2022 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--aquatic-panda--fa7c992d31ee0392 | aquatic panda |  | 不明 | actor_profile/evidence/aquatic-panda.csv | structured-data | TLP:CLEAR | 中 |
| source--daily-a9818c561227639f76fb | 中国関連のAPT「Aquatic Panda」、10ヶ月にわたるスパイ活動で7つの国際組織を標的に | thehackernews.com | 2025-03-22 | https://thehackernews.com/2025/03/china-linked-apt-aquatic-panda-10-month.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
