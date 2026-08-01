# Rocke 脅威アクタープロファイル

- プロファイルID: `actor--rocke`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Rockeの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Rocke**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Iron Group | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Rocke](https://attack.mitre.org/groups/G0106) is an alleged Chinese-speaking adversary whose primary objective appeared to be cryptojacking, or stealing victim system resources for the purposes of mining cryptocurrency. The name [Rocke](https://attack.mitre.org/groups/G0106) comes from the email address "rocke@live.cn" used to create the wallet which held collected cryptocurrency. Researchers have detected overlaps between [Rocke](https://attack.mitre.org/groups/G0106) and the Iron Cybercrime Group, though this attribution has not been confirmed.(Citation: Talos Rocke August 2018) |
| Capability | XBash |
| Infrastructure |  |
| Victim | Cybercrime, Cryptomining, Cryptojacking |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Rocke, Iron Group | canonical-name | 高 | China | https://redcanary.com/blog/rocke-cryptominer/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Rocke%2C+Iron+Group&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Iron Group | single-alias-intersection | 中 |  | https://www.intezer.com/iron-cybercrime-group-under-the-scope-2/ |
| misp-threat-actor | Rocke | canonical-name | 高 |  | https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html<br>https://unit42.paloaltonetworks.com/malware-used-by-rocke-group-evolves-to-evade-detection-by-cloud-security-products/<br>https://www.intezer.com/blog-technical-analysis-cryptocurrency-mining-war-on-the-cloud/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Rocke - G0106 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0106<br>https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html |
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
| malware--xbash | XBash | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

未確認

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
| sectors | 暗号資産・Web3 | [Rocke](https://attack.mitre.org/groups/G0106) is an alleged Chinese-speaking adversary whose primary objective appeared to be cryptojacking, or stealing victim system resources for the purposes of mining cryptocurrency. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1014 | Rootkit | [Rocke](https://attack.mitre.org/groups/G0106) has modified /etc/ld.so.preload to hook libc functions in order to hide the installed dropper and mining software in process lists.(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Rocke](https://attack.mitre.org/groups/G0106) has looked for IP addresses in the known_hosts file on the infected system and attempted to SSH into them.(Citation: Talos Rocke August 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [Rocke](https://attack.mitre.org/groups/G0106) has spread its coinminer via SSH.(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | [Rocke](https://attack.mitre.org/groups/G0106) has modified UPX headers after packing files to break unpackers.(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | [Rocke](https://attack.mitre.org/groups/G0106)'s miner has created UPX-packed files in the Windows Start Menu Folder.(Citation: Talos Rocke August 2018)(Citation: Unit 42 Rocke January 2019)(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.004 | Compile After Delivery | [Rocke](https://attack.mitre.org/groups/G0106) has compiled malware, delivered to victims as .c files, with the GNU Compiler Collection (GCC).(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Rocke](https://attack.mitre.org/groups/G0106) has used shell scripts which download mining executables and saves them with the filename "java".(Citation: Talos Rocke August 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1037 | Boot or Logon Initialization Scripts | [Rocke](https://attack.mitre.org/groups/G0106) has installed an "init.d" startup script to maintain persistence.(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [Rocke](https://attack.mitre.org/groups/G0106) conducted scanning for exposed TCP port 7001 as well as SSH and Redis servers.(Citation: Talos Rocke August 2018)(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.003 | Cron | [Rocke](https://attack.mitre.org/groups/G0106) installed a cron job that downloaded and executed files from the C2.(Citation: Talos Rocke August 2018)(Citation: Unit 42 Rocke January 2019)(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.002 | Portable Executable Injection | [Rocke](https://attack.mitre.org/groups/G0106)'s miner, "TermsHost.exe", evaded defenses by injecting itself into Windows processes, including Notepad.exe.(Citation: Talos Rocke August 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [Rocke](https://attack.mitre.org/groups/G0106) can detect a running process's PID on the infected machine.(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | [Rocke](https://attack.mitre.org/groups/G0106) used shell scripts to run commands which would obtain persistence and execute the cryptocurrency mining malware.(Citation: Talos Rocke August 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | [Rocke](https://attack.mitre.org/groups/G0106) has used Python-based malware to install and spread their coinminer.(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Rocke](https://attack.mitre.org/groups/G0106) has deleted files on infected machines.(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.006 | Timestomp | [Rocke](https://attack.mitre.org/groups/G0106) has changed the time stamp of certain files.(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | [Rocke](https://attack.mitre.org/groups/G0106) issued wget requests from infected systems to the C2.(Citation: Talos Rocke August 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Rocke](https://attack.mitre.org/groups/G0106) has executed wget and curl commands to Pastebin over the HTTPS protocol.(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Rocke](https://attack.mitre.org/groups/G0106) has used uname -m to collect the name and information about the infected system's kernel.(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | [Rocke](https://attack.mitre.org/groups/G0106) has used Pastebin, Gitee, and GitLab for Command and Control.(Citation: Anomali Rocke March 2019)(Citation: Talos Rocke August 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.001 | Dead Drop Resolver | [Rocke](https://attack.mitre.org/groups/G0106) has used Pastebin to check the version of beaconing malware and redirect to another Pastebin hosting updated malware.(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Rocke](https://attack.mitre.org/groups/G0106) used malware to download additional malicious files to the target system.(Citation: Talos Rocke August 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Rocke](https://attack.mitre.org/groups/G0106) has extracted tar.gz files after downloading them from a C2 server.(Citation: Talos Rocke August 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Rocke](https://attack.mitre.org/groups/G0106) exploited Apache Struts, Oracle WebLogic (CVE-2017-10271), and Adobe ColdFusion (CVE-2017-3066) vulnerabilities to deliver malware.(Citation: Talos Rocke August 2018)(Citation: Unit 42 Rocke January 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1222.002 | Linux and Mac Permissions | [Rocke](https://attack.mitre.org/groups/G0106) has changed file permissions of files so they could not be modified.(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1496.001 | Compute Hijacking | [Rocke](https://attack.mitre.org/groups/G0106) has distributed cryptomining malware.(Citation: Talos Rocke August 2018)(Citation: Unit 42 Rocke January 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [Rocke](https://attack.mitre.org/groups/G0106) used scripts which detected and uninstalled antivirus software.(Citation: Talos Rocke August 2018)(Citation: Unit 42 Rocke January 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.002 | Systemd Service | [Rocke](https://attack.mitre.org/groups/G0106) has installed a systemd service script to maintain persistence.(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Rocke](https://attack.mitre.org/groups/G0106)'s miner has created UPX-packed files in the Windows Start Menu Folder.(Citation: Talos Rocke August 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.004 | Private Keys | [Rocke](https://attack.mitre.org/groups/G0106) has used SSH private keys on the infected machine to spread its coinminer throughout a network.(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | [Rocke](https://attack.mitre.org/groups/G0106) downloaded a file "libprocesshider", which could hide files on the target system.(Citation: Talos Rocke August 2018)(Citation: Unit 42 Rocke January 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [Rocke](https://attack.mitre.org/groups/G0106)'s miner connects to a C2 server using port 51640.(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.006 | Dynamic Linker Hijacking | [Rocke](https://attack.mitre.org/groups/G0106) has modified /etc/ld.so.preload to hook libc functions in order to hide the installed dropper and mining software in process lists.(Citation: Anomali Rocke March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [Rocke](https://attack.mitre.org/groups/G0106) used scripts which detected and uninstalled antivirus software.(Citation: Talos Rocke August 2018)(Citation: Unit 42 Rocke January 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.006 | Clear Linux or Mac System Logs | [Rocke](https://attack.mitre.org/groups/G0106) has cleared log files within the /var/log/ folder.(Citation: Anomali Rocke March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | [Rocke](https://attack.mitre.org/groups/G0106) used scripts which killed processes and added firewall rules to block traffic related to other cryptominers.(Citation: Talos Rocke August 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 29件（`artifacts.csv`）

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
| source--rocke--fab01aae2a18c470 | rocke |  | 不明 | actor_profile/evidence/rocke.csv | structured-data | TLP:CLEAR | 中 |
| source--rocke--4a8fe4ac4a4b7a2d | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--rocke--b25396042582626a | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--rocke--f4aa6084623a4ec4 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--rocke--f4432cdaaa9f6ac9 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--rocke--8dfa6951b86a6d57 | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
