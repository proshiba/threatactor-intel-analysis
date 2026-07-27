# Earth Lusca 脅威アクタープロファイル

- プロファイルID: `actor--earth-lusca`
- 状態: draft
- 更新日時: 2026-07-27T11:04:31Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Earth Luscaの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Earth Lusca**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Charcoal Typhoon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| CHROMIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ControlX | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TAG-22 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| APT41 | related-to | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used malware commonly used by other Chinese threat groups, including [APT41](https://attack.mitre.org/groups/G0096) and the [Winnti Group](https://attack.mitre.org/groups/G0044) cluster, however security researchers assess [Earth Lusca](https://attack.mitre.org/groups/G1006)'s techniques and infrastructure are separate.(Citation: TrendMicro EarthLusca 2022) | 中 | `source--mitre-attack-19-1` |
| Winnti Group | related-to | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used malware commonly used by other Chinese threat groups, including [APT41](https://attack.mitre.org/groups/G0096) and the [Winnti Group](https://attack.mitre.org/groups/G0044) cluster, however security researchers assess [Earth Lusca](https://attack.mitre.org/groups/G1006)'s techniques and infrastructure are separate.(Citation: TrendMicro EarthLusca 2022) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Earth Lusca](https://attack.mitre.org/groups/G1006) is a suspected China-based cyber espionage group that has been active since at least April 2019. [Earth Lusca](https://attack.mitre.org/groups/G1006) has targeted organizations in Australia, China, Hong Kong, Mongolia, Nepal, the Philippines, Taiwan, Thailand, Vietnam, the United Arab Emirates, Nigeria, Germany, France, and the United States. Targets included government institutions, news media outlets, gambling companies, educational institutions, COVID-19 research organizations, telecommunications companies, religious movements banned in China, and cryptocurrency trading platforms; security researchers assess some [Earth Lusca](https://attack.mitre.org/groups/G1006) operations may be financially motivated.(Citation: TrendMicro EarthLusca 2022)<br><br>[Earth Lusca](https://attack.mitre.org/groups/G1006) has used malware commonly used by other Chinese threat groups, including [APT41](https://attack.mitre.org/groups/G0096) and the [Winnti Group](https://attack.mitre.org/groups/G0044) cluster, however security researchers assess [Earth Lusca](https://attack.mitre.org/groups/G1006)'s techniques and infrastructure are separate.(Citation: TrendMicro EarthLusca 2022) |
| Capability | Winnti for Linux, Cobalt Strike, ShadowPad, certutil, PowerSploit, Tasklist, Nltest, Mimikatz, NBTscan |
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
| etda-threat-group-cards | Earth Lusca | canonical-name | 高 | China | https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf<br>https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Earth+Lusca&n=1 |
| etda-threat-group-cards | RedHotel, TAG-22 | single-alias-intersection | 中 | China | https://www.recordedfuture.com/chinese-group-tag-22-targets-nepal-philippines-taiwan/<br>https://go.recordedfuture.com/hubfs/reports/cta-2023-0808.pdf<br>https://www.sentinelone.com/labs/unmasking-i-soon-the-leak-that-revealed-chinas-cyber-operations/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Charcoal Typhoon | multiple-name-intersection | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Earth Lusca | canonical-name | 高 | CN | https://hello.global.ntt/-/media/ntt/global/insights/white-papers/the-operations-of-winnti-group.pdf<br>https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf<br>https://www.recordedfuture.com/chinese-group-tag-22-targets-nepal-philippines-taiwan |
| misp-microsoft-activity-group | Charcoal Typhoon | multiple-name-intersection | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Earth Lusca - G1006 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1006<br>https://go.recordedfuture.com/hubfs/reports/cta-2023-0808.pdf<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
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
| malware--daily-f196d446e69f62aacb40 | SprySOCKS | Earth Luscaとの直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 2023 | 2024 | 高 | `source--daily-ff80b256acceafc23ada` |
| malware--shadowpad | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) is a modular backdoor that was first identified in a supply chain compromise of the NetSarang software in mid-July 2017. The malware was originally thought to be exclusively used by [APT41](https://attack.mitre.org/groups/G0096), but has since been observed to be used by various Chinese threat activity groups. (Citation: Recorded Future RedEcho Feb 2021)(Citation: Securelist ShadowPad Aug 2017)(Citation: Kaspersky ShadowPad Aug 2017)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--winnti-for-linux | Winnti for Linux | [Winnti for Linux](https://attack.mitre.org/software/S0430) is a trojan, seen since at least 2015, designed specifically for targeting Linux systems. Reporting indicates the winnti malware family is shared across a number of actors including [Winnti Group](https://attack.mitre.org/groups/G0044). The Windows variant is tracked separately under [Winnti for Windows](https://attack.mitre.org/software/S0141).(Citation: Chronicle Winnti for Linux May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--powersploit | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tasklist | Tasklist | The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nltest | Nltest | [Nltest](https://attack.mitre.org/software/S0359) is a Windows command-line utility used to list domain controllers and enumerate domain trusts.(Citation: Nltest Manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nbtscan | NBTscan | [NBTscan](https://attack.mitre.org/software/S0590) is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)(Citation: Symantec Waterbug Jun 2019)(Citation: FireEye APT39 Jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| 攻撃グループ「Earth Lusca」が台湾総統選挙を目前に地政学的トピックを用いてサイバー諜報活動を展開 | cyber-espionage | 不明 | 不明 | 2024-03-15 | 攻撃グループ「Earth Lusca」が台湾総統選挙を目前に地政学的トピックを用いてサイバー諜報活動を展開 | 高 | `source--daily-4c4674e1b8568e329ce6` |
| SprySOCKS LinuxマルウェアのWindows版、政府機関への攻撃に使用 | malware-campaign | 2023 | 2024 | 2026-06-17 | ESETは、従来Linux向けとされていたSprySOCKSマルウェアのWindows版が政府機関攻撃に使われたと報告した。 攻撃は2023年から2024年にかけて、台湾、タイ、パキスタン、ホンジュラスの政府組織を標的にしていた。 ESETはこの活動を、中国系脅威アクターEarth Lusca、別名FishMongerに高い確度で帰属している。 Windows版にはWIN_DRVとWIN_PLUSがあり、WIN_DRVはカーネルドライバでプロセス、通信、ファイル、レジストリを隠蔽する。 一部の攻撃シナリオでは、Secure Boot脆弱性CVE-2023-24932を悪用するUEFIブートキットの関与も示唆された。 | 高 | `source--daily-ff80b256acceafc23ada` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.006 | DCSync | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.004 | SSH Authorized Keys | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--earth-lusca--98b7035a52ea7c69`, `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--earth-lusca--98b7035a52ea7c69`, `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.012 | Print Processors | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | Anonymous/RussiaUkrainewar/Report_Notes_of_Cyber_inspector_.pdf {"page": 151} Chromium из файлов. T1555.003 Credentials from Web Browsers Angry Likho может извлекать с целью хищения аутентификационные данные из браузеров. APT может работать с большинством современных браузеров, включая браузеры на основе Chromium. T1555.005 Password Managers Angry Likho может извлекать учетные данные |  |  | 不明 | 不明 | 中 | `source--earth-lusca--98b7035a52ea7c69` |
| Credential Access | T1555.005 | Password Managers | извлекать с целью хищения аутентификационные данные из браузеров. APT может работать с большинством современных браузеров, включая браузеры на основе Chromium. T1555.005 Password Managers Angry Likho может извлекать учетные данные из различных менеджеров паролей. Например, импланты, основанные на Rhadamanthys Stealer, могут извлекать учетные данные из менеджеров паролей KeeP |  |  | 不明 | 不明 | 中 | `source--earth-lusca--98b7035a52ea7c69` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.004 | Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.004 | Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 52件
- IOC観測: 57件
- 複数攻撃で観測: 0件
- 要レビュー候補: 30件
- 非IOC artifact観測: 103件（`artifacts.csv`）

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
| source--daily-4c4674e1b8568e329ce6 | 攻撃グループ「Earth Lusca」が台湾総統選挙を目前に地政学的トピックを用いてサイバー諜報活動を展開 | trendmicro.com | 2024-03-15 | https://www.trendmicro.com/ja_jp/research/24/c/earth-lusca-uses-geopolitical-lure-to-target-taiwan.html | osint-report | TLP:CLEAR | 中 |
| source--daily-ff80b256acceafc23ada | SprySOCKS LinuxマルウェアのWindows版、政府機関への攻撃に使用 | welivesecurity.com | 2026-06-17 | https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/ | osint-report | TLP:CLEAR | 中 |
| source--earth-lusca--032dd9b35df3a5f5 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--199829ebd56f38eb | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--1a1e407a4362eb69 | wp void balaur tracking a cybermercenarys activities |  | 不明 | CyberMerceNary/wp-void-balaur-tracking-a-cybermercenarys-activities.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--1a9368088602e490 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--earth-lusca--1e640b2aea499dd6 | cyberespionage gamaredon way |  | 不明 | Gamaredon/cyberespionage-gamaredon-way.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--23943fb3d1d136c3 | 2024 Annual Cybersecurity Vulnerability Threat Landscape Research Report |  | 2024 | summary/2025/2024_Annual_Cybersecurity_Vulnerability_Threat_Landscape_Research_Report.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--2b747471cb1a7c41 | 0day  In the Wild |  | 不明 | 0day _In the Wild_.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--earth-lusca--2bb88150059ba49f | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--earth-lusca--33d4c1d6ac8ff0d7 | Operation Marstech Mayhem Report 021025 03 |  | 不明 | lazarus/Operation-Marstech-Mayhem-Report_021025_03.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--3ac6ac9c5fe64a5e | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--433072d91d3dd87a | 2021(APT) Microsoft Digital Defense Report |  | 2021 | summary/2021/2021(APT) Microsoft Digital Defense Report.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--573b1b4eac57b638 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--59eb5df1f0425423 | amezit |  | 不明 | International Strategic/Russia/Vulkan/amezit.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--5c1d54aaa37e8e0e | Microsoft Edge Security StegoAd |  | 不明 | cybercrime/2026/Microsoft_Edge_Security_StegoAd.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--6023615a8b04e193 | elastic global threat report 2024 |  | 2024 | summary/2024/elastic-global-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--6a018d06363e5e6c | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--703cd54add1a3959 | 202512 |  | 2025-12 | information_operations/Meta’s threat disruptions/202512.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--75e8559c85eac27e | Charting China’s Climb as a Leading Global Cyber Power |  | 不明 | International Strategic/China/Charting China’s Climb as a Leading Global Cyber Power.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--760426aa8af40469 | elastic global threat report 2025 |  | 2025 | summary/2025/elastic-global-threat-report-2025.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--78e9a028e57eb891 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--7a688810045b62fc | gamaredon in 2025 |  | 2025 | Gamaredon/gamaredon-in-2025.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--7d65222e8beaf156 | study of a targeted attack on a russian enterprise in the mechanical engineering sector en |  | 不明 | UNC****/NoName/study_of_a_targeted_attack_on_a_russian_enterprise_in_the_mechanical_engineering_sector_en.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--81606f683c2b5776 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--840f146d8b7530f7 | ESET Threat Report Q22020 |  | 不明 | summary/2020/ESET_Threat_Report_Q22020.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--87269f0b852c709d | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--88e015a851a0644b | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--931a2201b0913fe0 | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--96794c55f6a5ee34 | 2023 Network Vulnerability Situation Research Report |  | 2023 | summary/2024/2023 Network Vulnerability Situation Research Report.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--98b7035a52ea7c69 | earth lusca |  | 不明 | actor_profile/evidence/earth-lusca.csv | structured-data | TLP:CLEAR | 中 |
| source--earth-lusca--9b0e27675a9c4c0a | OceanLotus' Attacks to Indochinese Peninsula Evolution of Targets, Techniques and Procedure |  | 不明 | Oceanlotus/OceanLotus' Attacks to Indochinese Peninsula Evolution of Targets, Techniques and Procedure.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--9ba7d1f46c5f350a | Buying Spying Insights into Commercial Surveillance Vendors TAG report |  | 不明 | Spyware/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--a7937abb956e7d73 | readme |  | 不明 | lazarus/fudmodule/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--earth-lusca--ab5b3680b8da3e28 | cert nz cyber change behavioural insights 2022 online version |  | 2022 | International Strategic/New Zealand/cert-nz-cyber-change-behavioural-insights-2022-online-version.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--b2a90d80928fd56d | Hurdling Over Hazards  Multifaceted Threats to the Paris Olympics |  | 不明 | summary/2024/Hurdling Over Hazards- Multifaceted Threats to the Paris Olympics.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--b6235c7794cb0e32 | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--bc23ccefae2a2a61 | 003 |  | 不明 | summary/UNREDACTEDMagazine/003.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--bd4f9dd295314458 | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--c0053c5d733a7845 | kimsuky 2023 03 20 joint cyber security advisory |  | 2023-03-20 | kimsuky/kimsuky-2023-03-20-joint-cyber-security-advisory.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--c7eda091c53f3701 | NCSC MAR Infamous Chisel |  | 不明 | Sandworm/NCSC-MAR-Infamous-Chisel.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--cbe51c6e3dc9357a | Report Notes of Cyber inspector |  | 不明 | Anonymous/RussiaUkrainewar/Report_Notes_of_Cyber_inspector_.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--cdc3a8201297cd1a | SideCopy |  | 不明 | SideCopy/SideCopy.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--d436b7ac73dae330 | winnti apt group docks in sri lanka for new campaign final |  | 不明 | Winnti/winnti-apt-group-docks-in-sri-lanka-for-new-campaign-final.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--df02256dee31c1b3 | Browser Security Annual Report 2024 |  | 2024 | summary/2024/Browser-Security-Annual-Report-2024.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--df5aaa905a981b9e | MacMalware 2023 |  | 2023 | summary/2024/MacMalware_2023.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--e110797480bd6733 | Updated MATA attacks Eastern Europe full report ENG |  | 不明 | lazarus/MATA/Updated-MATA-attacks-Eastern-Europe_full-report_ENG.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--f29d03d993f1f420 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--earth-lusca--f9e32a04ccd9fd36 | 2025 Mid Year Vulnerability Landscape Research Report |  | 2025 | summary/2025/2025 Mid-Year Vulnerability Landscape Research Report.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
