# Silence 脅威アクタープロファイル

- プロファイルID: `actor--silence`
- 状態: draft
- 更新日時: 2026-07-29T15:36:11Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Silenceの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Silence**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Whisper Spider | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Silence](https://attack.mitre.org/groups/G0091) is a financially motivated threat actor targeting financial institutions in different countries. The group was first seen in June 2016. Their main targets reside in Russia, Ukraine, Belarus, Azerbaijan, Poland and Kazakhstan. They compromised various banking systems, including the Russian Central Bank's Automated Workstation Client, ATMs, and card processing.(Citation: Cyber Forensicator Silence Jan 2019)(Citation: SecureList Silence Nov 2017)  |
| Capability | Empire, Winexe, SDelete |
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
| etda-threat-group-cards | Silence, Contract Crew | canonical-name | 高 |  | https://securelist.com/the-silence/83009/<br>https://reaqta.com/2019/01/silence-group-targeting-russian-banks/<br>https://newsroom.accenture.com/news/accenture-report-reveals-new-cybercrime-operating-model-among-high-profile-threat-groups.htm |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Silence group | canonical-name | 高 |  | https://reaqta.com/2019/01/silence-group-targeting-russian-banks/<br>https://www.group-ib.com/blog/silence<br>https://securelist.com/the-silence/83009/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Silence - G0091 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0091<br>https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf<br>https://securelist.com/the-silence/83009/ |
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

未確認

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--winexe | Winexe | [Winexe](https://attack.mitre.org/software/S0191) is a lightweight, open source tool similar to [PsExec](https://attack.mitre.org/software/S0029) designed to allow system administrators to execute commands on remote servers. (Citation: Winexe Github Sept 2013) [Winexe](https://attack.mitre.org/software/S0191) is unique in that it is a GNU/Linux based client. (Citation: Überwachung APT28 Forfiles June 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--sdelete | SDelete | [SDelete](https://attack.mitre.org/software/S0195) is an application that securely deletes data in a way that makes it unrecoverable. It is part of the Microsoft Sysinternals suite of tools. (Citation: Microsoft SDelete July 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ロシア | Their main targets reside in Russia, Ukraine, Belarus, Azerbaijan, Poland and Kazakhstan. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | ウクライナ | Their main targets reside in Russia, Ukraine, Belarus, Azerbaijan, Poland and Kazakhstan. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 金融 | [Silence](https://attack.mitre.org/groups/G0091) is a financially motivated threat actor targeting financial institutions in different countries. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [Silence](https://attack.mitre.org/groups/G0091) has used the Farse6.1 utility (based on [Mimikatz](https://attack.mitre.org/software/S0002)) to extract credentials from lsass.exe.(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Silence](https://attack.mitre.org/groups/G0091) has used Nmap to scan the corporate network, build a network topology, and identify vulnerable hosts.(Citation: Group IB Silence Sept 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Silence](https://attack.mitre.org/groups/G0091) has used RDP for lateral movement.(Citation: Group IB Silence Sept 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [Silence](https://attack.mitre.org/groups/G0091) has used environment variable string substitution for obfuscation.(Citation: Cyber Forensicator Silence Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Silence](https://attack.mitre.org/groups/G0091) has named its backdoor "WINWORD.exe".(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Silence](https://attack.mitre.org/groups/G0091) has used scheduled tasks to stage its operation.(Citation: Cyber Forensicator Silence Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | [Silence](https://attack.mitre.org/groups/G0091) has injected a DLL library containing a Trojan into the fwmain32.exe process.(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Silence](https://attack.mitre.org/groups/G0091) has used PowerShell to download and execute payloads.(Citation: Cyber Forensicator Silence Jan 2019)(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Silence](https://attack.mitre.org/groups/G0091) has used Windows command-line to run commands.(Citation: Cyber Forensicator Silence Jan 2019)(Citation: SecureList Silence Nov 2017)(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [Silence](https://attack.mitre.org/groups/G0091) has used VBS scripts.(Citation: Cyber Forensicator Silence Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | [Silence](https://attack.mitre.org/groups/G0091) has used JS scripts.(Citation: Cyber Forensicator Silence Jan 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Silence](https://attack.mitre.org/groups/G0091) has deleted artifacts, including scheduled tasks, communicates files from the C2 and other logs.(Citation: Cyber Forensicator Silence Jan 2019)(Citation: Group IB Silence Sept 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Lateral Movement | T1072 | Software Deployment Tools | [Silence](https://attack.mitre.org/groups/G0091) has used RAdmin, a remote software tool used to remotely control workstations and ATMs.(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Silence](https://attack.mitre.org/groups/G0091) has used compromised credentials to log on to other systems and escalate privileges.(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.002 | External Proxy | [Silence](https://attack.mitre.org/groups/G0091) has used ProxyBot, which allows the attacker to redirect traffic from the current node to the backconnect server via Sock4\Socks5.(Citation: Group IB Silence Sept 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Silence](https://attack.mitre.org/groups/G0091) has downloaded additional modules and malware to victim’s machines.(Citation: Group IB Silence Sept 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | [Silence](https://attack.mitre.org/groups/G0091) has leveraged the Windows API, including using CreateProcess() or ShellExecute(), to perform a variety of tasks.(Citation: SecureList Silence Nov 2017)(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Silence](https://attack.mitre.org/groups/G0091) can create, delete, or modify a specified Registry key or value.(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [Silence](https://attack.mitre.org/groups/G0091) can capture victim screen activity.(Citation: SecureList Silence Nov 2017)(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1125 | Video Capture | [Silence](https://attack.mitre.org/groups/G0091) has been observed making videos of victims to observe bank employees day to day activities.(Citation: SecureList Silence Nov 2017)(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Silence](https://attack.mitre.org/groups/G0091) attempts to get users to launch malicious attachments delivered via spearphishing emails.(Citation: Cyber Forensicator Silence Jan 2019)(Citation: SecureList Silence Nov 2017)(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.001 | Compiled HTML File | [Silence](https://attack.mitre.org/groups/G0091) has weaponized CHM files in their phishing campaigns.(Citation: Cyber Forensicator Silence Jan 2019)(Citation: SecureList Silence Nov 2017)(Citation: Group IB Silence Aug 2019)(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Silence](https://attack.mitre.org/groups/G0091) has used <code>HKCU\Software\Microsoft\Windows\CurrentVersion\Run</code>, <code>HKLM\Software\Microsoft\Windows\CurrentVersion\Run</code>, and the Startup folder to establish persistence.(Citation: Group IB Silence Sept 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | [Silence](https://attack.mitre.org/groups/G0091) has used a valid certificate to sign their primary loader Silence.Downloader (aka TrueBot).(Citation: Group IB Silence Aug 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Silence](https://attack.mitre.org/groups/G0091) has sent emails with malicious DOCX, CHM, LNK and ZIP attachments. (Citation: Cyber Forensicator Silence Jan 2019)(Citation: SecureList Silence Nov 2017)(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | [Silence](https://attack.mitre.org/groups/G0091) has used [Winexe](https://attack.mitre.org/software/S0191) to install a service on the remote system.(Citation: SecureList Silence Nov 2017)(Citation: Group IB Silence Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [Silence](https://attack.mitre.org/groups/G0091) has used port 444 when sending data about the system from the client to the server.(Citation: Group IB Silence Sept 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Silence](https://attack.mitre.org/groups/G0091) has obtained and modified versions of publicly-available tools like [Empire](https://attack.mitre.org/software/S0363) and [PsExec](https://attack.mitre.org/software/S0029).(Citation: Group IB Silence Aug 2019) (Citation: SecureList Silence Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 34件（`artifacts.csv`）

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
| source--silence--c14ed54c3bda62a1 | silence |  | 不明 | actor_profile/evidence/silence.csv | structured-data | TLP:CLEAR | 中 |
| source--silence--33573d1f03d17fe2 | APT28 CERTFR 2023 EN |  | 2023 | APT28/APT28_CERTFR_2023_EN.pdf | report | TLP:CLEAR | 中 |
| source--silence--dde68b63bba1994b | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--silence--705a83ff7f537377 | national cyber threat assessment 2025 2026 e |  | 不明 | International Strategic/Canada/national-cyber-threat-assessment-2025-2026-e.pdf | report | TLP:CLEAR | 中 |
| source--silence--d1ff0f0b23662d6c | README |  | 不明 | README.md | repository-notes | TLP:CLEAR | 中 |
| source--silence--23eed535aba1f80b | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--silence--5d486f6498177684 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--silence--5c9a45674ce7dc73 | README |  | 不明 | kimsuky/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--silence--184dfe20b112a1ab | kimsuky note |  | 不明 | kimsuky/kimsuky-note.txt | text-data | TLP:CLEAR | 中 |
| source--silence--7657c19c41ad0031 | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--silence--90325e151b477795 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--silence--d170991d1b57d064 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--silence--8106515074887bbd | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--silence--ae3f1bee3396b35b | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--silence--6994df601d305974 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
