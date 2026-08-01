# TeamTNT 脅威アクタープロファイル

- プロファイルID: `actor--teamtnt`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

TeamTNTの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TeamTNT**
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
| Adversary | [TeamTNT](https://attack.mitre.org/groups/G0139) is a threat group that has primarily targeted cloud and containerized environments. The group as been active since at least October 2019 and has mainly focused its efforts on leveraging cloud and container resources to deploy cryptocurrency miners in victim environments.(Citation: Palo Alto Black-T October 2020)(Citation: Lacework TeamTNT May 2021)(Citation: Intezer TeamTNT September 2020)(Citation: Cado Security TeamTNT Worm August 2020)(Citation: Unit 42 Hildegard Malware)(Citation: Trend Micro TeamTNT)(Citation: ATT TeamTNT Chimaera September 2020)(Citation: Aqua TeamTNT August 2020)(Citation: Intezer TeamTNT Explosion September 2021) |
| Capability | Hildegard, MimiPenguin, Peirates, LaZagne |
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
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TeamTNT | canonical-name | 高 |  | https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/<br>https://malpedia.caad.fkie.fraunhofer.de/details/elf.teamtnt<br>https://blog.aquasec.com/teamtnt-campaign-against-docker-kubernetes-environment |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | TeamTNT - G0139 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0139<br>https://blog.aquasec.com/container-security-tnt-container-attack<br>https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera |
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
| malware--hildegard | Hildegard | [Hildegard](https://attack.mitre.org/software/S0601) is malware that targets misconfigured kubelets for initial access and runs cryptocurrency miner operations. The malware was first observed in January 2021. The TeamTNT activity group is believed to be behind [Hildegard](https://attack.mitre.org/software/S0601). (Citation: Unit 42 Hildegard Malware) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mimipenguin | MimiPenguin | [MimiPenguin](https://attack.mitre.org/software/S0179) is a credential dumper, similar to [Mimikatz](https://attack.mitre.org/software/S0002), designed specifically for Linux platforms. (Citation: MimiPenguin GitHub May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--peirates | Peirates | [Peirates](https://attack.mitre.org/software/S0683) is a post-exploitation Kubernetes exploitation framework with a focus on gathering service account tokens for lateral movement and privilege escalation. The tool is written in GoLang and publicly available on GitHub.(Citation: Peirates GitHub) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| sectors | 暗号資産・Web3 | The group as been active since at least October 2019 and has mainly focused its efforts on leveraging cloud and container resources to deploy cryptocurrency miners in victim environments.(Citation: Palo Alto Black-T October 2020)(Citation: Lacework TeamTNT May 2021)(Citation: Intezer TeamTNT September 2020)(Citation: Cado Security TeamTNT Worm August 2020)(Citation: Unit 42 Hildegard Malware)(Citation: Trend Micr | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1007 | System Service Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for services such as Alibaba Cloud Security's aliyun service and BMC Helix Cloud Security's bmc-agent service in order to disable them.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1014 | Rootkit | [TeamTNT](https://attack.mitre.org/groups/G0139) has used rootkits such as the open-source Diamorphine rootkit and their custom bots to hide cryptocurrency mining activities on the machine.(Citation: Trend Micro TeamTNT) (Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has enumerated the host machine’s IP address.(Citation: Trend Micro TeamTNT) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [TeamTNT](https://attack.mitre.org/groups/G0139) has used SSH to connect back to victim machines.(Citation: Intezer TeamTNT September 2020) [TeamTNT](https://attack.mitre.org/groups/G0139) has also used SSH to transfer tools and payloads onto victim hosts and execute them.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | [TeamTNT](https://attack.mitre.org/groups/G0139) has used UPX and Ezuri packer to pack its binaries.(Citation: Trend Micro TeamTNT) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [TeamTNT](https://attack.mitre.org/groups/G0139) has encrypted its binaries via AES and encoded files using Base64.(Citation: Trend Micro TeamTNT)(Citation: Aqua TeamTNT August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [TeamTNT](https://attack.mitre.org/groups/G0139) has disguised their scripts with docker-related file names.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [TeamTNT](https://attack.mitre.org/groups/G0139) has replaced .dockerd and .dockerenv with their own scripts and cryptocurrency mining software.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has used masscan to search for open Docker API ports and Kubernetes clusters.(Citation: Cado Security TeamTNT Worm August 2020)(Citation: Unit 42 Hildegard Malware)(Citation: Cisco Talos Intelligence Group) [TeamTNT](https://attack.mitre.org/groups/G0139) has also used malware that utilizes zmap and zgrab to search for vulnerable services in cloud environments.(Citation: Palo Alto Black-T October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048 | Exfiltration Over Alternative Protocol | [TeamTNT](https://attack.mitre.org/groups/G0139) has sent locally staged files with collected credentials to C2 servers using cURL.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has run <code>netstat -anp</code> to search for rival malware connections.(Citation: Trend Micro TeamTNT) [TeamTNT](https://attack.mitre.org/groups/G0139) has also used `libprocesshider` to modify <code>/etc/ld.so.preload</code>.(Citation: ATT TeamTNT Chimaera September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for rival malware and removes it if found.(Citation: Trend Micro TeamTNT) [TeamTNT](https://attack.mitre.org/groups/G0139) has also searched for running processes containing the strings aliyun or liyun to identify machines running Alibaba Cloud Security tools.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [TeamTNT](https://attack.mitre.org/groups/G0139) has executed PowerShell commands in batch scripts.(Citation: ATT TeamTNT Chimaera September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [TeamTNT](https://attack.mitre.org/groups/G0139) has used batch scripts to download tools and executing cryptocurrency miners.(Citation: ATT TeamTNT Chimaera September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | [TeamTNT](https://attack.mitre.org/groups/G0139) has used shell scripts for execution.(Citation: Trend Micro TeamTNT)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.009 | Cloud API | [TeamTNT](https://attack.mitre.org/groups/G0139) has leveraged AWS CLI to enumerate cloud environments with compromised credentials.(Citation: Talos TeamTNT) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.013 | Container CLI/API | TeamTNT targeted misconfigured containers and used container CLI tools.(Citation: Cisco Talos Blog) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.003 | Clear Command History | [TeamTNT](https://attack.mitre.org/groups/G0139) has cleared command history with <code>history -c</code>.(Citation: Trend Micro TeamTNT)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [TeamTNT](https://attack.mitre.org/groups/G0139) has used a payload that removes itself after running. [TeamTNT](https://attack.mitre.org/groups/G0139) also has deleted locally staged files for collecting credentials or scan results for local IP addresses after exfiltrating them.(Citation: ATT TeamTNT Chimaera September 2020)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | [TeamTNT](https://attack.mitre.org/groups/G0139) has used an IRC bot for C2 communications.(Citation: Trend Micro TeamTNT) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [TeamTNT](https://attack.mitre.org/groups/G0139) has the `curl` command to send credentials over HTTP and the `curl` and `wget` commands to download new software.(Citation: Intezer TeamTNT September 2020)(Citation: Cado Security TeamTNT Worm August 2020)(Citation: Cisco Talos Intelligence Group) [TeamTNT](https://attack.mitre.org/groups/G0139) has also used a custom user agent HTTP header in shell scripts.(Citation: Trend Micro TeamTNT) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [TeamTNT](https://attack.mitre.org/groups/G0139) has aggregated collected credentials in text files before exfiltrating.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for system version, architecture, and hostname information.(Citation: ATT TeamTNT Chimaera September 2020)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has used a script that checks `/proc/*/environ` for environment variables related to AWS.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.004 | SSH Authorized Keys | [TeamTNT](https://attack.mitre.org/groups/G0139) has added RSA keys in <code>authorized_keys</code>.(Citation: Aqua TeamTNT August 2020)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | [TeamTNT](https://attack.mitre.org/groups/G0139) has leveraged iplogger.org to send collected data back to C2.(Citation: Aqua TeamTNT August 2020)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [TeamTNT](https://attack.mitre.org/groups/G0139) has the <code>curl</code> and <code>wget</code> commands as well as batch scripts to download new tools.(Citation: Intezer TeamTNT September 2020)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1120 | Peripheral Device Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for attached VGA devices using lspci.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [TeamTNT](https://attack.mitre.org/groups/G0139) has used open-source tools such as Weave Scope to target exposed Docker API ports and gain initial access to victim environments.(Citation: Intezer TeamTNT September 2020)(Citation: Cisco Talos Intelligence Group) [TeamTNT](https://attack.mitre.org/groups/G0139) has also targeted exposed kubelets for Kubernetes environments.(Citation: Unit 42 Hildegard Malware) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.001 | Local Account | [TeamTNT](https://attack.mitre.org/groups/G0139) has created local privileged users on victim machines.(Citation: Intezer TeamTNT September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [TeamTNT](https://attack.mitre.org/groups/G0139) has used a script that decodes a Base64-encoded version of WeaveWorks Scope.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.003 | Malicious Image | [TeamTNT](https://attack.mitre.org/groups/G0139) has relied on users to download and execute malicious Docker images.(Citation: Lacework TeamTNT May 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | [TeamTNT](https://attack.mitre.org/groups/G0139) has established tmate sessions for C2 communications.(Citation: Unit 42 Hildegard Malware)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1222.002 | Linux and Mac Permissions | [TeamTNT](https://attack.mitre.org/groups/G0139) has modified the permissions on binaries with <code>chattr</code>.(Citation: Trend Micro TeamTNT)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1496.001 | Compute Hijacking | [TeamTNT](https://attack.mitre.org/groups/G0139) has deployed XMRig Docker images to mine cryptocurrency.(Citation: Lacework TeamTNT May 2021)(Citation: Cado Security TeamTNT Worm August 2020) [TeamTNT](https://attack.mitre.org/groups/G0139) has also infected Docker containers and Kubernetes clusters with XMRig, and used RainbowMiner and lolMiner for mining cryptocurrency.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for security products on infected machines.(Citation: ATT TeamTNT Chimaera September 2020)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.002 | Systemd Service | [TeamTNT](https://attack.mitre.org/groups/G0139) has established persistence through the creation of a cryptocurrency mining system service using <code>systemctl</code>.(Citation: Trend Micro TeamTNT)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [TeamTNT](https://attack.mitre.org/groups/G0139) has used malware that adds cryptocurrency miners as a service.(Citation: ATT TeamTNT Chimaera September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [TeamTNT](https://attack.mitre.org/groups/G0139) has added batch scripts to the startup folder.(Citation: ATT TeamTNT Chimaera September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for unsecured AWS credentials and Docker API credentials.(Citation: Cado Security TeamTNT Worm August 2020)(Citation: Trend Micro TeamTNT)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.004 | Private Keys | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for unsecured SSH keys.(Citation: Cado Security TeamTNT Worm August 2020)(Citation: Trend Micro TeamTNT) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.005 | Cloud Instance Metadata API | [TeamTNT](https://attack.mitre.org/groups/G0139) has queried the AWS instance metadata service for credentials.(Citation: Trend Micro TeamTNT)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.003 | Systemctl | [TeamTNT](https://attack.mitre.org/groups/G0139) has created system services to execute cryptocurrency mining software.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [TeamTNT](https://attack.mitre.org/groups/G0139) has obtained domains to host their payloads.(Citation: Palo Alto Black-T October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [TeamTNT](https://attack.mitre.org/groups/G0139) has developed custom malware such as [Hildegard](https://attack.mitre.org/software/S0601).(Citation: Unit 42 Hildegard Malware) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.001 | Scanning IP Blocks | [TeamTNT](https://attack.mitre.org/groups/G0139) has scanned specific lists of target IP addresses.(Citation: Trend Micro TeamTNT) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | [TeamTNT](https://attack.mitre.org/groups/G0139) has scanned for vulnerabilities in IoT devices and other related resources such as the Docker API.(Citation: Trend Micro TeamTNT) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [TeamTNT](https://attack.mitre.org/groups/G0139) has uploaded backdoored Docker images to Docker Hub.(Citation: Lacework TeamTNT May 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1609 | Container Administration Command | [TeamTNT](https://attack.mitre.org/groups/G0139) executed [Hildegard](https://attack.mitre.org/software/S0601) through the kubelet API run command and by executing commands on running containers.(Citation: Unit 42 Hildegard Malware) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1610 | Deploy Container | [TeamTNT](https://attack.mitre.org/groups/G0139) has deployed different types of containers into victim environments to facilitate execution.(Citation: Intezer TeamTNT September 2020)(Citation: Trend Micro TeamTNT) [TeamTNT](https://attack.mitre.org/groups/G0139) has also transferred cryptocurrency mining software to Kubernetes clusters discovered within local IP address ranges.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1611 | Escape to Host | [TeamTNT](https://attack.mitre.org/groups/G0139) has deployed privileged containers that mount the filesystem of victim machine.(Citation: Intezer TeamTNT September 2020)(Citation: Aqua TeamTNT August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1613 | Container and Resource Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has checked for running containers with <code>docker ps</code> and for specific container names with <code>docker inspect</code>.(Citation: Trend Micro TeamTNT) [TeamTNT](https://attack.mitre.org/groups/G0139) has also searched for Kubernetes pods running in a local network.(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1680 | Local Storage Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for disk partition and logical volume information.(Citation: ATT TeamTNT Chimaera September 2020)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [TeamTNT](https://attack.mitre.org/groups/G0139) has disabled and uninstalled security tools such as Alibaba, Tencent, and BMC cloud monitoring agents on cloud-based infrastructure.(Citation: ATT TeamTNT Chimaera September 2020)(Citation: Cisco Talos Intelligence Group) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.006 | Clear Linux or Mac System Logs | [TeamTNT](https://attack.mitre.org/groups/G0139) has removed system logs from <code>/var/log/syslog</code>.(Citation: Aqua TeamTNT August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | [TeamTNT](https://attack.mitre.org/groups/G0139) has disabled <code>iptables</code>.(Citation: Aqua TeamTNT August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 4件
- IOC観測: 8件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 13件（`artifacts.csv`）

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
| source--teamtnt--13da4afb2e7269be | teamtnt |  | 不明 | actor_profile/evidence/teamtnt.csv | structured-data | TLP:CLEAR | 中 |
| source--teamtnt--06723a89ecf7d74d | Cloud Native Threat Report 2021 |  | 2021 | summary/2021/Cloud_Native_Threat_Report_2021.pdf | report | TLP:CLEAR | 中 |
| source--teamtnt--f3c625fea1cd334a | Google Cybersecurity Action Team Threat Horizons Report#4 |  | 不明 | summary/2022/Google_Cybersecurity_Action_Team_Threat_Horizons_Report#4.pdf | report | TLP:CLEAR | 中 |
| source--teamtnt--b8235ac10a2acd91 | XForce Threat Intelligence 2022 |  | 2022 | summary/2022/XForce_Threat_Intelligence_2022.pdf | report | TLP:CLEAR | 中 |
| source--teamtnt--19cf92dd5c4ee0f5 | rpt toward a new momentum trend micro security predictions for 2022 |  | 2022 | summary/2022/rpt-toward-a-new-momentum-trend-micro-security-predictions-for-2022.pdf | report | TLP:CLEAR | 中 |
| source--teamtnt--55801a20e41e69f6 | Cloud Security Risk Report 2025 |  | 2025 | summary/2026/Cloud_Security_Risk_Report_2025.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
