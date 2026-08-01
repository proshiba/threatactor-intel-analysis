# Ember Bear 脅威アクタープロファイル

- プロファイルID: `actor--ember-bear`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Ember Bearの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Ember Bear**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Bleeding Bear | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Cadet Blizzard | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DEV-0586 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Frozenvista | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Lorec Bear | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Lorec53 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Saint Bear | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Storm-0587 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA471 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UAC-0056 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC2589 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the Russia worksheet.

- 国: Russia
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
| Adversary | [Ember Bear](https://attack.mitre.org/groups/G1003) is a Russian state-sponsored cyber espionage group that has been active since at least 2020, linked to Russia's General Staff Main Intelligence Directorate (GRU) 161st Specialist Training Center (Unit 29155).(Citation: CISA GRU29155 2024) [Ember Bear](https://attack.mitre.org/groups/G1003) has primarily focused operations against Ukrainian government and telecommunication entities, but has also operated against critical infrastructure entities in Europe and the Americas.(Citation: Cadet Blizzard emerges as novel threat actor) [Ember Bear](https://attack.mitre.org/groups/G1003) conducted the [WhisperGate](https://attack.mitre.org/software/S0689) destructive wiper attacks against Ukraine in early 2022.(Citation: CrowdStrike Ember Bear Profile March 2022)(Citation: Mandiant UNC2589 March 2022)(Citation: CISA GRU29155 2024) There is some confusion as to whether [Ember Bear](https://attack.mitre.org/groups/G1003) overlaps with another Russian-linked entity referred to as [Saint Bear](https://attack.mitre.org/groups/G1031). At present available evidence strongly suggests these are distinct activities with different behavioral profiles.(Citation: Cadet Blizzard emerges as novel threat actor)(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) |
| Capability | reGeorg, P.A.S. Webshell, WhisperGate, Saint Bot, WhisperGate wiper, Elephant Framework, BloodHound, Impacket, ngrok, Rclone, Responder, CrackMapExec, PsExec |
| Infrastructure |  |
| Victim | Ukraine, limited evidence to suggest that the group has been involved in attacks on targets in Kyrgyzstan. Third-party reporting has also linked the group to attacks on Georgia. |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Cadet Blizzard | multiple-name-intersection | 高 | Russia | https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Cadet+Blizzard&n=1 |
| etda-threat-group-cards | SaintBear, Lorec53 | canonical-name | 高 | Russia | https://nsfocusglobal.com/apt-retrospection-lorec53-an-active-russian-hack-group-launched-phishing-attacks-against-georgian-government/<br>https://www.crowdstrike.com/blog/who-is-ember-bear/<br>https://services.google.com/fh/files/blogs/google_fog_of_war_research_report.pdf |
| cert-ua-uac-index | UAC-0056 | single-alias-intersection | 中 |  | https://cert.gov.ua/article/38374<br>https://cert.gov.ua/article/703548<br>https://cert.gov.ua/article/619229 |
| microsoft-threat-actor-mapping | Cadet Blizzard | canonical-name | 高 | Russia | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | SaintBear | canonical-name | 高 | RU | https://malpedia.caad.fkie.fraunhofer.de/details/win.graphsteel<br>https://cert.gov.ua/article/38374<br>https://blog.malwarebytes.com/threat-intelligence/2022/04/new-uac-0056-activity-theres-a-go-elephant-in-the-room/ |
| misp-threat-actor | DEV-0586 | multiple-name-intersection | 高 | RU | https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/<br>https://msrc-blog.microsoft.com/2022/02/28/analysis-resources-cyber-threat-activity-ukraine/<br>https://unit42.paloaltonetworks.com/atoms/ruinousursa/ |
| misp-microsoft-activity-group | Cadet Blizzard | canonical-name | 高 | RU, Russia | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Ember Bear - G1003 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1003<br>https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/<br>https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf |
| misp-mitre-intrusion-set | Saint Bear - G1031 | multiple-name-intersection | 高 |  | https://attack.mitre.org/groups/G1031<br>https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/<br>https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/ |
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
| malware--elephant-framework | Elephant Framework | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--p-a-s-webshell | P.A.S. Webshell | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) is a publicly available multifunctional PHP webshell in use since at least 2016 that provides remote access and execution on target web servers.(Citation: ANSSI Sandworm January 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--regeorg | reGeorg | [reGeorg](https://attack.mitre.org/software/S1187) is an open-source web shell written in Python that can be used as a proxy to bypass firewall rules and tunnel data in and out of targeted networks.(Citation: Fortinet reGeorg MAR 2019)(Citation: GitHub reGeorg 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--saint-bot | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) is a .NET downloader that has been used by [Saint Bear](https://attack.mitre.org/groups/G1031) since at least March 2021.(Citation: Malwarebytes Saint Bot April 2021)(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 ) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--whispergate | WhisperGate | [WhisperGate](https://attack.mitre.org/software/S0689) is a multi-stage wiper designed to look like ransomware that has been used against multiple government, non-profit, and information technology organizations in Ukraine since at least January 2022.(Citation: Cybereason WhisperGate February 2022)(Citation: Unit 42 WhisperGate January 2022)(Citation: Microsoft WhisperGate January 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--whispergate-wiper | WhisperGate wiper | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--bloodhound | BloodHound | [BloodHound](https://attack.mitre.org/software/S0521) is an Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment.(Citation: GitHub Bloodhound)(Citation: CrowdStrike BloodHound April 2018)(Citation: FoxIT Wocao December 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ngrok | ngrok | [ngrok](https://attack.mitre.org/software/S0508) is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. [ngrok](https://attack.mitre.org/software/S0508) has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.(Citation: Zdnet Ngrok September 2018)(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes LazyScripter Feb 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--rclone | Rclone | [Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation: DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--responder | Responder | Responder is an open source tool used for LLMNR, NBT-NS and MDNS poisoning, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication. (Citation: GitHub Responder) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--crackmapexec | CrackMapExec | [CrackMapExec](https://attack.mitre.org/software/S0488), or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. [CrackMapExec](https://attack.mitre.org/software/S0488) collects Active Directory information to conduct lateral movement through targeted networks.(Citation: CME Github September 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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
| 米国と同盟国、ロシアのGRU部隊が重要インフラ攻撃に関与と発表 | cyber-espionage | 不明 | 不明 | 2024-09-06 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--country--ukraine |  | ttp--activity-rule--f17a61b0acfb89cfe4ba | victim--activity-rule--84ba967e4f2df409774e | 米国と同盟国が、重要インフラ攻撃を積極的に行っているロシアのハッカー集団(Cadet BlizzardおよびEmber Bearとして追跡)にロシアのGRU部隊のUnit29155が関与していると発表。 GRU部隊29155は、NATO加盟国やウクライナを対象としたサイバー攻撃を行った。 2020年以降、スパイ活動のための情報の収集、機密情報の盗難と漏洩による評判の失墜、データの破壊による組織的な妨害を目的とした攻撃を行っている。 主要ターゲットはエネルギー、政府、航空宇宙分野を含む米国の重要インフラ。 米国は、GRUのUnit 29155の一員とみられる5人のロシア軍情報将校に関する情報に対して、最大1,000万ドルの報奨金を発表。 | 中 | `source--daily-f1baa9d2403423a63284` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 米国と同盟国、ロシアのGRU部隊が重要インフラ攻撃に関与と発表 | Ember Bear | 情報なし | T1485 Data Destruction | 情報なし | 米国, ウクライナ | 被害事例: 米国と同盟国、ロシアのGRU部隊が重要インフラ攻撃に関与と発表 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ウクライナ | Targeting text mentions ukraine. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--daily-f1baa9d2403423a63284`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | キルギス | Targeting text mentions kyrgyzstan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | ジョージア | Targeting text mentions georgia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 活動「米国と同盟国、ロシアのGRU部隊が重要インフラ攻撃に関与と発表」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-f1baa9d2403423a63284`, `source--target-audit-etda-threat-group-cards` |
| regions | NATO加盟国 | 活動「米国と同盟国、ロシアのGRU部隊が重要インフラ攻撃に関与と発表」の記述で標的地域としてNATO加盟国が明示されている。 | 不明 | 不明 | 中 | `source--daily-f1baa9d2403423a63284` |
| regions | 中南米 | 構造化OSINTの被害地域フィールドでEmber Bearの標的範囲として中南米が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中央アジア | 構造化OSINTの被害地域フィールドでEmber Bearの標的範囲として中央アジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | 構造化OSINTの被害地域フィールドでEmber Bearの標的範囲として欧州が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 米国と同盟国、ロシアのGRU部隊が重要インフラ攻撃に関与と発表 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--country--ukraine |  | ttp--activity-rule--f17a61b0acfb89cfe4ba |  | espionage: 2020年以降、スパイ活動のための情報の収集、機密情報の盗難と漏洩による評判の失墜、データの破壊による組織的な妨害を目的とした攻撃を行っている。 | 不明 | 不明 | 2024-09-06 | 中 | `source--daily-f1baa9d2403423a63284` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Impact | T1485 | Data Destruction | 2020年以降、スパイ活動のための情報の収集、機密情報の盗難と漏洩による評判の失墜、データの破壊による組織的な妨害を目的とした攻撃を行っている。 |  | activity--daily-b7a84ad717db2af67833 | 不明 | 不明 | 中 | `source--daily-f1baa9d2403423a63284` |
| Credential Access | T1003 | OS Credential Dumping | [Ember Bear](https://attack.mitre.org/groups/G1003) gathers credential material from target systems, such as SSH keys, to facilitate access to victim environments.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | [Ember Bear](https://attack.mitre.org/groups/G1003) uses legitimate Sysinternals tools such as procdump to dump LSASS memory.(Citation: Cadet Blizzard emerges as novel threat actor)(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.002 | Security Account Manager | [Ember Bear](https://attack.mitre.org/groups/G1003) acquires victim credentials by extracting registry hives such as the Security Account Manager through commands such as <code>reg save</code>.(Citation: Cadet Blizzard emerges as novel threat actor)(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.004 | LSA Secrets | [Ember Bear](https://attack.mitre.org/groups/G1003) has used frameworks such as [Impacket](https://attack.mitre.org/software/S0357) to dump LSA secrets for credential capture.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [Ember Bear](https://attack.mitre.org/groups/G1003) gathers victim system information such as enumerating the volume of a given device or extracting system and security event logs for analysis.(Citation: Cadet Blizzard emerges as novel threat actor)(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Ember Bear](https://attack.mitre.org/groups/G1003) has used tools such as Nmap and MASSCAN for remote service discovery.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021 | Remote Services | [Ember Bear](https://attack.mitre.org/groups/G1003) uses valid network credentials gathered through credential harvesting to move laterally within victim networks, often employing the [Impacket](https://attack.mitre.org/software/S0357) framework to do so.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [Ember Bear](https://attack.mitre.org/groups/G1003) has renamed the legitimate Sysinternals tool procdump to alternative names such as <code>dump64.exe</code> to evade detection.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Ember Bear](https://attack.mitre.org/groups/G1003) has renamed tools to match legitimate utilities, such as renaming GOST tunneling instances to `java` in victim environments.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [Ember Bear](https://attack.mitre.org/groups/G1003) has used tools such as NMAP for remote system discovery and enumeration in victim environments.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [Ember Bear](https://attack.mitre.org/groups/G1003) has used WMI execution with password hashes for command execution and lateral movement.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Ember Bear](https://attack.mitre.org/groups/G1003) uses remotely scheduled tasks to facilitate remote command execution on victim machines.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Ember Bear](https://attack.mitre.org/groups/G1003) has used PowerShell commands to gather information from compromised systems,  such as email servers.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Ember Bear](https://attack.mitre.org/groups/G1003) deletes files related to lateral movement to avoid detection.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | [Ember Bear](https://attack.mitre.org/groups/G1003) has used DNS tunnelling tools, such as dnscat/2 and Iodine, for C2 purposes.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.001 | Default Accounts | [Ember Bear](https://attack.mitre.org/groups/G1003) has abused default user names and passwords in externally-accessible IP cameras for initial access.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.003 | Multi-hop Proxy | [Ember Bear](https://attack.mitre.org/groups/G1003) has configured multi-hop proxies via ProxyChains within victim environments.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1095 | Non-Application Layer Protocol | [Ember Bear](https://attack.mitre.org/groups/G1003) uses socket-based tunneling utilities for command and control purposes such as NetCat and Go Simple Tunnel (GOST). These tunnels are used to push interactive command prompts over the created sockets.(Citation: Cadet Blizzard emerges as novel threat actor) [Ember Bear](https://attack.mitre.org/groups/G1003) has also used reverse TCP connections from Meterpreter installations to communicate back with C2 infrastructure.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | [Ember Bear](https://attack.mitre.org/groups/G1003) used the `su-bruteforce` tool to brute force specific users using the `su` command.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.003 | Password Spraying | [Ember Bear](https://attack.mitre.org/groups/G1003) has conducted password spraying against Outlook Web Access (OWA) infrastructure to identify valid user names and passwords.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Ember Bear](https://attack.mitre.org/groups/G1003) modifies registry values for anti-forensics and defense evasion purposes.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114 | Email Collection | [Ember Bear](https://attack.mitre.org/groups/G1003) attempts to collect mail from accessed systems and servers.(Citation: Cadet Blizzard emerges as novel threat actor)(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [Ember Bear](https://attack.mitre.org/groups/G1003) engages in mass collection from compromised systems during intrusions.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1125 | Video Capture | [Ember Bear](https://attack.mitre.org/groups/G1003) has exfiltrated images from compromised IP cameras.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [Ember Bear](https://attack.mitre.org/groups/G1003) have used VPNs both for initial access to victim environments and for persistence within them following compromise.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Ember Bear](https://attack.mitre.org/groups/G1003) gains initial access to victim environments by exploiting external-facing services. Examples include exploitation of CVE-2021-26084 in Confluence servers; CVE-2022-41040, ProxyShell, and other vulnerabilities in Microsoft Exchange; and multiple vulnerabilities in open-source platforms such as content management systems.(Citation: Cadet Blizzard emerges as novel threat actor)(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195 | Supply Chain Compromise | [Ember Bear](https://attack.mitre.org/groups/G1003) has compromised information technology providers and software developers providing services to targets of interest, building initial access to ultimate victims at least in part through compromise of service providers that work with the victim organizations.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [Ember Bear](https://attack.mitre.org/groups/G1003) has used exploits to enable follow-on execution of frameworks such as Meterpreter.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | [Ember Bear](https://attack.mitre.org/groups/G1003) has used exploits for vulnerabilities such as MS17-010, also known as `Eternal Blue`, during operations.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1491.002 | External Defacement | [Ember Bear](https://attack.mitre.org/groups/G1003) is linked to the defacement of several Ukrainian organization websites.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [Ember Bear](https://attack.mitre.org/groups/G1003) deploys web shells following initial access for either follow-on command execution or protocol tunneling. Example web shells used by [Ember Bear](https://attack.mitre.org/groups/G1003) include P0wnyshell, reGeorg, [P.A.S. Webshell](https://attack.mitre.org/software/S0598), and custom variants of publicly-available web shell examples.(Citation: Cadet Blizzard emerges as novel threat actor)(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | [Ember Bear](https://attack.mitre.org/groups/G1003) has used pass-the-hash techniques for lateral movement in victim environments.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [Ember Bear](https://attack.mitre.org/groups/G1003) has dumped configuration settings in accessed IP cameras including plaintext credentials.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560 | Archive Collected Data | [Ember Bear](https://attack.mitre.org/groups/G1003) has compressed collected data prior to exfiltration.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1561.002 | Disk Structure Wipe | [Ember Bear](https://attack.mitre.org/groups/G1003) conducted destructive operations against victims, including disk structure wiping, via the [WhisperGate](https://attack.mitre.org/software/S0689) malware in Ukraine.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Ember Bear](https://attack.mitre.org/groups/G1003) has used tools such as [Rclone](https://attack.mitre.org/software/S1040) to exfiltrate information from victim environments to cloud storage such as `mega.nz`.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [Ember Bear](https://attack.mitre.org/groups/G1003) retrieves follow-on payloads direct from adversary-owned infrastructure for deployment on compromised hosts.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [Ember Bear](https://attack.mitre.org/groups/G1003) has used various non-standard ports for C2 communication.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [Ember Bear](https://attack.mitre.org/groups/G1003) has used ProxyChains to tunnel protocols to internal networks.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583 | Acquire Infrastructure | [Ember Bear](https://attack.mitre.org/groups/G1003) uses services such as IVPN, SurfShark, and Tor to add anonymization to operations.(Citation: Cadet Blizzard emerges as novel threat actor) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [Ember Bear](https://attack.mitre.org/groups/G1003) has used virtual private servers (VPSs) to host tools, perform reconnaissance, exploit victim infrastructure, and as a destination for data exfiltration.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585 | Establish Accounts | [Ember Bear](https://attack.mitre.org/groups/G1003) has created accounts on dark web forums to obtain various tools and malware.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | [Ember Bear](https://attack.mitre.org/groups/G1003) has acquired malware and related tools from dark web forums.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.005 | Exploits | [Ember Bear](https://attack.mitre.org/groups/G1003) has obtained exploitation scripts against publicly-disclosed vulnerabilities from public repositories.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.001 | Scanning IP Blocks | [Ember Bear](https://attack.mitre.org/groups/G1003) has targeted IP ranges for vulnerability scanning related to government and critical infrastructure organizations.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | [Ember Bear](https://attack.mitre.org/groups/G1003) has used publicly available tools such as MASSCAN and Acunetix for vulnerability scanning of public-facing infrastructure.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1654 | Log Enumeration | [Ember Bear](https://attack.mitre.org/groups/G1003) has enumerated SECURITY and SYSTEM log files during intrusions.(Citation: CISA GRU29155 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 3件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 3件
- 非IOC artifact観測: 102件（`artifacts.csv`）

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
| source--daily-f1baa9d2403423a63284 | 米国と同盟国、ロシアのGRU部隊が重要インフラ攻撃に関与と発表 | bleepingcomputer.com | 2024-09-06 | https://www.bleepingcomputer.com/news/security/us-and-allies-link-russian-military-hackers-behind-critical-infrastructure-attacks-to-gru-unit-29155/ | osint-report | TLP:CLEAR | 中 |
| source--ember-bear--0dd06d31baf6e8d5 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--1a876ab78f9cbe10 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--ember-bear--222b5728dc2fd56f | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--2e0d6b860eba4628 | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--ember-bear--31ce7194f93c4fb7 | google fog of war research report |  | 不明 | International Strategic/Russia/google_fog_of_war_research_report.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--3691f89917b6856e | ember bear |  | 不明 | actor_profile/evidence/ember-bear.csv | structured-data | TLP:CLEAR | 中 |
| source--ember-bear--40cba50ffc964066 | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--4eba0d82db68ec59 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--ember-bear--5774423bdf399ec6 | A year of Russian hybrid warfare in Ukraine MS Threat Intelligence |  | 不明 | International Strategic/Russia/A_year_of_Russian_hybrid_warfare_in_Ukraine_MS_Threat_Intelligence.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--63207b705d433568 | Microsoft Digital Defense Report 2022 |  | 2022 | summary/2022/Microsoft Digital Defense Report 2022.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--65cfb261598b6c87 | RussianCyber |  | 不明 | summary/2024/RussianCyber.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--6db5c42dd8d25689 | Ukraine Report Q1 2023 |  | 2023 | International Strategic/Ukraine/Ukraine-Report-Q1_2023.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--6f094699f88b54ad | Report on the state of cyberspace security Poland 2022 |  | 2022 | summary/2023/Report_on_the_state_of_cyberspace_security_Poland_2022.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--7561a682509eaecb | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--788856179c873745 | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--7d4b7b83976afa45 | Global APT 2023 Mid Year Report QIANXIN |  | 2023 | summary/2023/Global APT 2023 Mid-Year Report-QIANXIN.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--7ed7b515afb715f1 | Microsoft Defending Ukraine Early Lessons from the Cyber War |  | 不明 | summary/2022/Microsoft_Defending Ukraine_Early Lessons from the Cyber War.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--859ed4ead4610010 | CrowdStrike 2025 Threat Hunting Report |  | 2025 | summary/2025/CrowdStrike 2025 Threat Hunting Report.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--9311ce891bbf4f7b | MS UkraineSpecialReport |  | 不明 | summary/2022/MS_UkraineSpecialReport.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--93e4d311c137b9f5 | aa24 249a russian military cyber actors target us and global critical infrastructure |  | 不明 | International Strategic/Russia/WhisperGate/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--b18ff9714d5d6c97 | Russia’s Cyber Tactics Lessons Learned 2022 |  | 2022 | International Strategic/Russia/Russia’s Cyber Tactics Lessons Learned 2022.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--b23f959b0c74dd5f | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--b62f11560f2fb26b | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--bcac037bed3fa1b4 | CrowdStrike2023GlobalThreatReport |  | 2023 | summary/2023/CrowdStrike2023GlobalThreatReport.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--c2415f782b0efd53 | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--c32aaa3b89c9005a | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--c74d3463554db297 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--ef9d2c4332817f7c | 2023 Network Vulnerability Situation Research Report |  | 2023 | summary/2024/2023 Network Vulnerability Situation Research Report.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--fb2b6abe0b1e399f | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--ember-bear--fceef9bf8018bac4 | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
