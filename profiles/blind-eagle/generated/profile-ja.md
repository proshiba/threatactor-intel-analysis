# Blind Eagle 脅威アクタープロファイル

- プロファイルID: `actor--blind-eagle`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Blind Eagleの標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Blind Eagle**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT-C-36 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| APT-Q-98 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| AguilaCiega | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TAG-144 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| South America | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 62; mapping requires review. |

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
| Adversary | [APT-C-36](https://attack.mitre.org/groups/G0099) is a suspected South American threat group that has engaged in espionage and financially motivated operations since at least 2018. [APT-C-36](https://attack.mitre.org/groups/G0099) has targeted government institutions and entities in the financial, energy, and professional manufacturing sectors across Colombia and other Latin American countries.(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: Recorded Future TAG-144 AUG 2025) |
| Capability | HeartCrypt, PureCrypter, Caminho, njRAT, Imminent RAT, DCRAT, AsyncRAT, Remcos, Imminent Monitor, QuasarRAT |
| Infrastructure |  |
| Victim | Colombian government institutions |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Blind Eagle | canonical-name | 高 | Colombia | https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/<br>https://threatmon.io/apt-blind-eagles-malware-arsenal-technical-analysis/<br>https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/tracing-blind-eagle-to-proton66/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT-C-36 | canonical-name | 高 |  | https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/<br>https://www.ecucert.gob.ec/wp-content/uploads/2022/03/alerta-APTs-2022-03-23.pdf<br>https://blogs.blackberry.com/en/2023/02/blind-eagle-apt-c-36-targets-colombia |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | APT-C-36 - G0099 | mitre-external-id | 高 |  | https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf<br>https://attack.mitre.org/groups/G0099<br>https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/ |
| misp-360net | 盲眼鹰 - APT-C-36 | single-alias-intersection | 中 | namerica | https://apt.360.net/report/apts/83.html |

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
| malware--heartcrypt | HeartCrypt | [HeartCrypt](https://attack.mitre.org/software/S9018) is a packer-as-a-service (PaaS) used to protect malware that has been available since at least 2024. [HeartCrypt](https://attack.mitre.org/software/S9018) has been used to pack a variety of malware including [Lumma Stealer](https://attack.mitre.org/software/S1213), [Remcos](https://attack.mitre.org/software/S0332), and Rhadamanthys. In the [HeartCrypt](https://attack.mitre.org/software/S9018) PaaS model, customers submit malware via private messaging services and it is then packed and returned by the operator as a new binary.(Citation: Palo Alto HeartCrypt DEC 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--purecrypter | PureCrypter | PureCrypter is a fully-featured malware loader, developed by a threat actor called “PureCoder," that has been in use since at least 2021 to distribute a variety of remote access trojans and information stealers.(Citation: Zscaler PureCrypter JUN 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--caminho | Caminho | [Caminho](https://attack.mitre.org/software/S9016) is a downloader that has been used by threat actors since at least 2025 to deliver various strains of malware such as XWorm.(Citation: Zscaler BlindEagle DEC 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--njrat | njRAT | [njRAT](https://attack.mitre.org/software/S0385) is a remote access tool (RAT) that was first observed in 2012. It has been used by threat actors in the Middle East.(Citation: Fidelis njRAT June 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--imminent-rat | Imminent RAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--dcrat | DCRAT | [DCRAT](https://attack.mitre.org/software/S9017) is a variant of the open-source [AsyncRAT](https://attack.mitre.org/software/S1087) developed in C# with additional capabilities such as patching Microsoft’s Antimalware Scan Interface (AMSI).(Citation: Zscaler BlindEagle DEC 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--asyncrat | AsyncRAT | [AsyncRAT](https://attack.mitre.org/software/S1087) is an open-source remote access tool originally available through the NYANxCAT Github repository that has been used in malicious campaigns.(Citation: Morphisec Snip3 May 2021)(Citation: Cisco Operation Layover September 2021)(Citation: Telefonica Snip3 December 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--remcos | Remcos | [Remcos](https://attack.mitre.org/software/S0332) is a closed-source tool that is marketed as a remote control and surveillance software by a company called Breaking Security. [Remcos](https://attack.mitre.org/software/S0332) has been observed being used in malware campaigns.(Citation: Riskiq Remcos Jan 2018)(Citation: Talos Remcos Aug 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--imminent-monitor | Imminent Monitor | [Imminent Monitor](https://attack.mitre.org/software/S0434) was a commodity remote access tool (RAT) offered for sale from 2012 until 2019, when an operation was conducted to take down the Imminent Monitor infrastructure. Various cracked versions and variations of this RAT are still in circulation.(Citation: Imminent Unit42 Dec2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--quasarrat | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) is an open-source, remote access tool that has been publicly available on GitHub since at least 2014. [QuasarRAT](https://attack.mitre.org/software/S0262) is developed in the C# language.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | エクアドル | 構造化OSINTの被害国フィールドでBlind Eagleの標的・被害国としてエクアドルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | コロンビア | MITRE ATT&CKのGroup概要でBlind Eagleの標的国として明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | スペイン | 構造化OSINTの被害国フィールドでBlind Eagleの標的・被害国としてスペインが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | チリ | 構造化OSINTの被害国フィールドでBlind Eagleの標的・被害国としてチリが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | パナマ | 構造化OSINTの被害国フィールドでBlind Eagleの標的・被害国としてパナマが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 米国 | [APT-C-36](https://attack.mitre.org/groups/G0099) has targeted government institutions and entities in the financial, energy, and professional manufacturing sectors across Colombia and other Latin American countries.(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: Recorded Future TAG-144 AUG 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | 中南米 | MITRE ATT&CKのGroup概要でBlind Eagleの標的範囲として中南米が明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南米 | エクアドル、コロンビア、チリで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | エネルギー | [APT-C-36](https://attack.mitre.org/groups/G0099) has targeted government institutions and entities in the financial, energy, and professional manufacturing sectors across Colombia and other Latin American countries.(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: Recorded Future TAG-144 AUG 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 金融 | [APT-C-36](https://attack.mitre.org/groups/G0099) has targeted government institutions and entities in the financial, energy, and professional manufacturing sectors across Colombia and other Latin American countries.(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: Recorded Future TAG-144 AUG | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 製造・産業 | [APT-C-36](https://attack.mitre.org/groups/G0099) has targeted government institutions and entities in the financial, energy, and professional manufacturing sectors across Colombia and other Latin American countries.(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: Recorded Future TAG-144 AUG 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027 | Obfuscated Files or Information | [APT-C-36](https://attack.mitre.org/groups/G0099) has used ConfuserEx to obfuscate its variant of [Imminent Monitor](https://attack.mitre.org/software/S0434), compressed payloads and RAT packages, and password protected encrypted email attachments to avoid detection.(Citation: QiAnXin APT-C-36 Feb2019) [APT-C-36](https://attack.mitre.org/groups/G0099) has also compressed initial droppers into ZIP, LHA and UUE formats.(Citation: Kaspersky BlindEagle AUG 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | [APT-C-36](https://attack.mitre.org/groups/G0099) has used steganography to hide malicious code, typically in the resource section of executable files.(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Recorded Future TAG-144 AUG 2025)(Citation: Recorded Future TAG-144 AUG 2025)(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [APT-C-36](https://attack.mitre.org/groups/G0099) has used encoded and obfuscated files, images, and executables.(Citation: Kaspersky BlindEagle AUG 2024)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.016 | Junk Code Insertion | [APT-C-36](https://attack.mitre.org/groups/G0099) has used junk characters to obfuscate malicious scripts.(Citation: Recorded Future TAG-144 AUG 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | dns.org:2050 MITRE ATT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Stealth | T1036.004 | Masquerade Task or Service | [APT-C-36](https://attack.mitre.org/groups/G0099) has disguised its scheduled tasks as those used by Google.(Citation: QiAnXin APT-C-36 Feb2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [APT-C-36](https://attack.mitre.org/groups/G0099) has disguised malicious executables to appear as legitimate files.(Citation: Kaspersky BlindEagle AUG 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [APT-C-36](https://attack.mitre.org/groups/G0099) has used WMI to execute PowerShell.(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [APT-C-36](https://attack.mitre.org/groups/G0099) has used a macro function to set scheduled tasks, disguised as those used by Google.(Citation: QiAnXin APT-C-36 Feb2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | f IP febenvi[.]duckdns.org:2050 MITRE ATT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Privilege Escalation, Stealth | T1055.012 | Process Hollowing | [APT-C-36](https://attack.mitre.org/groups/G0099) has used process hollowing to execute malware in the memory of legitimate processes.(Citation: Kaspersky BlindEagle AUG 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [APT-C-36](https://attack.mitre.org/groups/G0099) has used PowerShell in malware execution including as part of fileless attack chains to download additional payloads.(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Zscaler BlindEagle DEC 2025)<br> |  |  | 不明 | 不明 | 高 | `source--blind-eagle--6823726904c42306`, `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [APT-C-36](https://attack.mitre.org/groups/G0099) has used VBScript for initial malware deployment including within a malicious Word document which is executed upon the document opening.(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Kaspersky BlindEagle AUG 2024)(Citation: LevelBlue Blind Eagle Proton66 JUN 2025)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript |  [APT-C-36](https://attack.mitre.org/groups/G0099) has used a fileless attack chain composed of three JavaScript code snippets to execute subsequent payloads.(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1064 | Scripting | nts/940363101067411527/94639004997978 1130/cacha.pdf IP febenvi[.]duckdns.org:2050 MITRE ATT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Command And Control | T1071 | Application Layer Protocol | Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Command And Control | T1105 | Ingress Tool Transfer | [APT-C-36](https://attack.mitre.org/groups/G0099) has downloaded binary data from a specified domain after the malicious document is opened.(Citation: QiAnXin APT-C-36 Feb2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [APT-C-36](https://attack.mitre.org/groups/G0099) has used VPNs in their operational infrastructure.(Citation: Recorded Future TAG-144 AUG 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [APT-C-36](https://attack.mitre.org/groups/G0099) has used malicious links in emails, often impersonating official notifications and documents, to direct users to execute malicious payloads.(Citation: Kaspersky BlindEagle AUG 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [APT-C-36](https://attack.mitre.org/groups/G0099) has prompted victims to open attachments and to accept macros in order to execute the subsequent payload.(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Recorded Future TAG-144 AUG 2025) [APT-C-36](https://attack.mitre.org/groups/G0099) has also lured victims into opening malicious files hosted on Google Drive that triggered WebDAV requests to download malware.(Citation: Check Point Blind Eagle MAR 2025)(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1480 | Execution Guardrails | [APT-C-36](https://attack.mitre.org/groups/G0099) has used geolocation filtering in malware delivery to redirect traffic not coming from a targeted region or country, such as Ecuador or Colombia, to legitimate sites.(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Recorded Future TAG-144 AUG 2025)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | TT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Lateral Movement | T1534 | Internal Spearphishing | [APT-C-36](https://attack.mitre.org/groups/G0099) has used a compromised account to send a phishing email to an address likely used and monitored by the IT team within the same targeted organization.(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | /94639004997978 1130/cacha.pdf IP febenvi[.]duckdns.org:2050 MITRE ATT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Stealth | T1564.003 | Hidden Window | [APT-C-36](https://attack.mitre.org/groups/G0099) has set the ShowWindow property of the Win32_ProcessStartup object to zero to hide PowerShell execution.(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [APT-C-36](https://attack.mitre.org/groups/G0099) has used spearphishing emails with malicious .pdf and .docx files and password protected RAR attachments to avoid being detected by the email gateway.(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Recorded Future TAG-144 AUG 2025)(Citation: Recorded Future TAG-144 AUG 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [APT-C-36](https://attack.mitre.org/groups/G0099) has sent emails containing a link that appear to lead to an urgent notification from a government institution, at times using URL shorteners like cort[.]as, acortaurl[.]com, and gtly[.]to.(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: Check Point Blind Eagle MAR 2025)(Citation: Recorded Future TAG-144 AUG 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1568 | Dynamic Resolution | [APT-C-36](https://attack.mitre.org/groups/G0099) has used DDNS services such as DuckDNS, noip[.]com, and con-ip[.]com to redirect victims to sites or repositories hosting malware implants.(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: LevelBlue Blind Eagle Proton66 JUN 2025)(Citation: Recorded Future TAG-144 AUG 2025)(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [APT-C-36](https://attack.mitre.org/groups/G0099) has used port 4050 for C2 communications.(Citation: QiAnXin APT-C-36 Feb2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [APT-C-36](https://attack.mitre.org/groups/G0099) has used side-loading to execute the HijackLoader payload.(Citation: Kaspersky BlindEagle AUG 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [APT-C-36](https://attack.mitre.org/groups/G0099) has acquired domains to host malicious payloads.(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: LevelBlue Blind Eagle Proton66 JUN 2025)(Citation: Recorded Future TAG-144 AUG 2025)(Citation: Recorded Future TAG-144 AUG 2025)(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [APT-C-36](https://attack.mitre.org/groups/G0099) has incorporated virtual private servers (VPS) into its operational infrastructure.(Citation: Recorded Future TAG-144 AUG 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | [APT-C-36](https://attack.mitre.org/groups/G0099) campaign architecture has included image hosting sites, Pastebin, Discord, GitHub, Google Drive, BitBucket, and Dropbox.(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: Recorded Future TAG-144 AUG 2025)(Citation: Zscaler BlindEagle DEC 2025)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.005 | Botnet | [APT-C-36](https://attack.mitre.org/groups/G0099) has used a botnet management interface to control large numbers of compromised hosts.(Citation: LevelBlue Blind Eagle Proton66 JUN 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | [APT-C-36](https://attack.mitre.org/groups/G0099) has regularly used compromised email accounts in spearphishing campaigns.(Citation: Recorded Future TAG-144 AUG 2025)(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.003 | Cloud Accounts | [APT-C-36](https://attack.mitre.org/groups/G0099) has used compromised Google Drive accounts including one associated with a  Colombian government organization.(Citation: Recorded Future TAG-144 AUG 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [APT-C-36](https://attack.mitre.org/groups/G0099) has customized existing malware with new capabilities including [njRAT](https://attack.mitre.org/software/S0385), [AsyncRAT](https://attack.mitre.org/software/S1087), LimeRAT, and BitRAT.(Citation: Kaspersky BlindEagle AUG 2024)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | [APT-C-36](https://attack.mitre.org/groups/G0099) has utilized well known malware including the Packer-as-a-Service HeartCrypt, PureCrypter, and open-source RATs such as [Remcos](https://attack.mitre.org/software/S0332).(Citation: Check Point Blind Eagle MAR 2025)(Citation: LevelBlue Blind Eagle Proton66 JUN 2025)(Citation: Recorded Future TAG-144 AUG 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [APT-C-36](https://attack.mitre.org/groups/G0099) utilizes tools well known in crime communities and has obtained and used a modified variant of [Imminent Monitor](https://attack.mitre.org/software/S0434).(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Check Point Blind Eagle MAR 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1593 | Search Open Websites/Domains | [APT-C-36](https://attack.mitre.org/groups/G0099) has gathered information on Colombian financial institutions, including Bancolombia, BBVA, Banco Caja Social, and Davivienda to craft phishing pages.(Citation: LevelBlue Blind Eagle Proton66 JUN 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [APT-C-36](https://attack.mitre.org/groups/G0099) has staged malware implants on group-owned repositories and sites.(Citation: Kaspersky BlindEagle AUG 2024)(Citation: LevelBlue Blind Eagle Proton66 JUN 2025)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1683.001 | Written Content | [APT-C-36](https://attack.mitre.org/groups/G0099) has generated email content impersonating official notifications and documents that direct victims to execute malicious payloads.(Citation: Kaspersky BlindEagle AUG 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1683.002 | Audio-Visual Content | [APT-C-36](https://attack.mitre.org/groups/G0099) has used phishing pages appearing like legitimate banking login portals to compromise credentials.(Citation: LevelBlue Blind Eagle Proton66 JUN 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | [APT-C-36](https://attack.mitre.org/groups/G0099) has impersonated banks including Banco Davivienda, Bancolombia, and BBVA as well as government institutions such as Colombia’s National Directorate of Taxes and Customs, Ministry of Foreign Affairs, and Office of the Attorney General.(Citation: Kaspersky BlindEagle AUG 2024)(Citation: LevelBlue Blind Eagle Proton66 JUN 2025)(Citation: Recorded Future TAG-144 AUG 2025)(Citation: Zscaler BlindEagle DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 102件
- IOC観測: 106件
- 複数攻撃で観測: 0件
- 要レビュー候補: 74件
- 非IOC artifact観測: 68件（`artifacts.csv`）

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
| source--blind-eagle--849392cad6eb513c | APT Blind Eagles |  | 不明 | BlindEagle/APT_Blind_Eagles.pdf | report | TLP:CLEAR | 中 |
| source--blind-eagle--6823726904c42306 | APT Blind Eagles Malware Arsenal Technical Analysis of the New |  | 不明 | BlindEagle/APT_Blind_Eagles_Malware_Arsenal_Technical_Analysis_of_the_New.pdf | report | TLP:CLEAR | 中 |
| source--blind-eagle--78eda3d14cb3fe38 | README |  | 不明 | BlindEagle/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
