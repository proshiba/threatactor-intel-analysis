# VOID MANTICORE 脅威アクタープロファイル

- プロファイルID: `actor--void-manticore`
- 状態: draft
- 更新日時: 2026-07-29T15:38:37Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

VOID MANTICOREの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **VOID MANTICORE**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BANISHED KITTEN | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| COBALT MYSTIQUE | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Handala Hack | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| HomeLand Justice | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Karma | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Karmabelow80 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Red Sandstorm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
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
| Adversary | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) is a threat group assessed to operate on behalf of Iran’s Ministry of Intelligence and Security (MOIS).(Citation: Check Point VOID MANTICORE Handala Hack March 2026) Active since at least mid-2022, VOID MANTICORE has targeted government entities, critical infrastructure, and private sector organizations across Albania, Israel, and the United States.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) conducts destructive cyber operations, combining wiper attacks with hack-and-leak campaigns. The group has operated under multiple public-facing personas, including [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) in operations against Albania, Karma and Karma Below in campaigns targeting Israeli organizations, and Handala Hack, its current primary persona, which has claimed activity against Israeli and U.S. entities, including a March 2026 attack against Stryker Corporation.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: DOJ FBI Handala Hack March 2026)  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has been observed collaborating with Scarred Manticore, which has been linked to initial access operations preceding VOID MANTICORE’s activity.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026)  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | HomeLand Justice | canonical-name | 高 | Iran | https://www.clearskysec.com/wp-content/uploads/2024/01/No-Justice-Wiper.pdf<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=HomeLand+Justice&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Red Sandstorm | canonical-name | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | HomeLand Justice | single-alias-intersection | 中 | IR | https://www.picussecurity.com/resource/blog/cisa-alert-aa22-264a-iranian-homeland-justice-apt-groups-ttp<br>https://www.attackiq.com/2022/09/23/attack-graph-response-to-us-cert-alert-aa22-264a-iranian-state-actors-conduct-cyber-operations-against-the-government-of-albania/<br>https://www.mandiant.com/resources/blog/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against |
| misp-threat-actor | BANISHED KITTEN | multiple-name-intersection | 高 | IR, Iran (Islamic Republic of) | https://www.crowdstrike.com/adversaries/banished-kitten/<br>https://services.google.com/fh/files/misc/tool-of-first-resort-israel-hamas-war-cyber.pdf |
| misp-threat-actor | Void Manticore | canonical-name | 高 | IR | https://research.checkpoint.com/2024/bad-karma-no-justice-void-manticore-destructive-activities-in-israel/ |
| misp-microsoft-activity-group | Red Sandstorm | canonical-name | 高 | IR, Iran | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | VOID MANTICORE - G1055 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1055<br>https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment<br>https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/ |
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
| malware--mitre--s1149 | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) is a backdoor malware that was deployed during [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) along with [ROADSWEEP](https://attack.mitre.org/software/S1150) ransomware, and has been used to target Farsi and Arabic speakers since at least 2012.(Citation: Mandiant ROADSWEEP August 2022) | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--mitre--s1150 | ROADSWEEP | [ROADSWEEP](https://attack.mitre.org/software/S1150) is a ransomware that was deployed against Albanian government networks during [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) along with the [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) backdoor.(Citation: Mandiant ROADSWEEP August 2022) | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--mitre--s1151 | ZeroCleare | [ZeroCleare](https://attack.mitre.org/software/S1151) is a wiper malware that has been used in conjunction with the [RawDisk](https://attack.mitre.org/software/S0364) driver since at least 2019 by suspected Iran-nexus threat actors including activity targeting the energy and industrial sectors in the Middle East and political targets in Albania.(Citation: Microsoft Albanian Government Attacks September 2022)(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Mandiant ROADSWEEP August 2022)(Citation: IBM ZeroCleare Wiper December 2019) | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mitre--s0357 | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| tool--mitre--s0002 | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| tool--mitre--s0364 | RawDisk | [RawDisk](https://attack.mitre.org/software/S0364) is a legitimate commercial driver from the EldoS Corporation that is used for interacting with files, disks, and partitions. The driver allows for direct modification of data on a local computer's hard drive. In some cases, the tool can enact these raw disk modifications from user-mode processes, circumventing Windows operating system security features.(Citation: EldoS RawDisk ITpro)(Citation: Novetta Blockbuster Destructive Malware) | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| tool--mitre--s0095 | ftp | [ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.(Citation: Microsoft FTP)(Citation: Linux FTP) | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |

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
| BiBiワイパーの新バージョンがディスクパーティションテーブルも破壊 | disruptive-activity | 不明 | 不明 | 2024-05-21 |  |  | ttp--activity-rule--7e8a4b46dd7a5b9c6c08 | victim--activity-rule--780f3983aa8216977285 | 新バージョンのBiBi Wiperがディスクパーティションテーブルを破壊 攻撃はイスラエルとアルバニアで発生 攻撃者はイランのハッカーグループであるVoid Manticore Void Manticoreは多様な破壊ツールを使用 新バージョンはデータ復旧を困難にする | 中 | `source--daily-0d70b2cb1fe1f39ff860` |
| HomeLand Justice | campaign | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 2026-05-12 |  | malware--mitre--s1149, malware--mitre--s1150, malware--mitre--s1151 | ttp--mitre-campaign--0b06909819cd839e84b0, ttp--mitre-campaign--1c878e11ead18e81f40e, ttp--mitre-campaign--2dc048bdae2a99349345, ttp--mitre-campaign--4f51d477b36b5e65b629, ttp--mitre-campaign--4f71c64125f203d9a37f, ttp--mitre-campaign--54df018259aa6e35c62b, ttp--mitre-campaign--597459b882a6121d02a7, ttp--mitre-campaign--607435dbf03c6b447456, ttp--mitre-campaign--6c8c3e304c7675e48e94, ttp--mitre-campaign--78ac41d87ea71b009685, ttp--mitre-campaign--7a4903fb7083eaf89222, ttp--mitre-campaign--7ff1d81738bca2650c4e, ttp--mitre-campaign--832ec2838375630f20a8, ttp--mitre-campaign--848ec9aaff8809a4b504, ttp--mitre-campaign--a1bc58011dfdee5560bc, ttp--mitre-campaign--ab6d95b9c827620ecaac, ttp--mitre-campaign--b6eabbd6aa66440ec7c8, ttp--mitre-campaign--bcfba187be6a64804365, ttp--mitre-campaign--bfba86287ab509282685, ttp--mitre-campaign--c7957c8dcc59a59f32e0, ttp--mitre-campaign--cd42f684fdd7e36a6dd5, ttp--mitre-campaign--d32f2450374e9ec586b2, ttp--mitre-campaign--df58953754d2afbde180, ttp--mitre-campaign--e4822e50db468b9f83f6, ttp--mitre-campaign--ea16c435dccfb5940d11 | victim--activity-rule--1bcee2af2ddefc48d2f1 | [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) was a disruptive cyber campaign conducted by Iranian state-affiliated actors against Albanian government networks in July and September 2022. The activity combined ransomware, wiper malware, and data leak operations. Initial access for [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) was established as early as May 2021, and threat actors moved laterally, exfiltrated sensitive information, and maintained persistence for approximately 14 months prior to the destructive phase of the operation. Responsibility was claimed by the "HomeLand Justice" front, which framed the campaign as retaliation against the Mujahedeen-e Khalq (MEK), an Iranian opposition group with a presence in Albania. Multiple Iran-nexus groups are assessed to have participated in the campaign, including [HEXANE](https://attack.mitre.org/groups/G1001) who probed victim infrastructure.(Citation: Mandiant ROADSWEEP August 2022)(Citation: Microsoft Albanian Government Attacks September 2022)(Citation: CISA Iran Albanian Attacks September 2022) A second wave of attacks was launched in September 2022 using similar tactics following public attribution of the previous activity to Iran and the severing of diplomatic ties between Iran and Albania.(Citation: CISA Iran Albanian Attacks September 2022)<br><br> | 高 | `source--mitre-attack-19-1` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | uding [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) in operations against Albania, Karma and Karma Below in campaigns targeting Israeli organizations, and Handala Hack, its current primary persona, which has claimed activity against Israeli and U.S. entities, including a March 2026 attack against Stryker Corporation.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: DOJ FBI Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has been observed collaborat | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | イスラエル | istry of Intelligence and Security (MOIS).(Citation: Check Point VOID MANTICORE Handala Hack March 2026) Active since at least mid-2022, VOID MANTICORE has targeted government entities, critical infrastructure, and private sector organizations across Albania, Israel, and the United States.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) conducts destructive cyber operations, combining wiper attacks with hack-and-leak campaigns. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) is a threat group assessed to operate on behalf of Iran’s Ministry of Intelligence and Security (MOIS).(Citation: Check Point VOID MANTICORE Handala Hack March 2026) Active since at least mid-2022, VOID MANTICORE has targeted government entities, critical infrastructure, and private sector organizations across Albania, Israel, and the United States.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) conducts | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: HomeLand Justice | 非公開 | anonymous | unknown | reported |  | malware--mitre--s1149, malware--mitre--s1150, malware--mitre--s1151 | ttp--mitre-campaign--0b06909819cd839e84b0, ttp--mitre-campaign--1c878e11ead18e81f40e, ttp--mitre-campaign--2dc048bdae2a99349345, ttp--mitre-campaign--4f51d477b36b5e65b629, ttp--mitre-campaign--4f71c64125f203d9a37f, ttp--mitre-campaign--54df018259aa6e35c62b, ttp--mitre-campaign--597459b882a6121d02a7, ttp--mitre-campaign--607435dbf03c6b447456, ttp--mitre-campaign--6c8c3e304c7675e48e94, ttp--mitre-campaign--78ac41d87ea71b009685, ttp--mitre-campaign--7a4903fb7083eaf89222, ttp--mitre-campaign--7ff1d81738bca2650c4e, ttp--mitre-campaign--832ec2838375630f20a8, ttp--mitre-campaign--848ec9aaff8809a4b504, ttp--mitre-campaign--a1bc58011dfdee5560bc, ttp--mitre-campaign--ab6d95b9c827620ecaac, ttp--mitre-campaign--b6eabbd6aa66440ec7c8, ttp--mitre-campaign--bcfba187be6a64804365, ttp--mitre-campaign--bfba86287ab509282685, ttp--mitre-campaign--c7957c8dcc59a59f32e0, ttp--mitre-campaign--cd42f684fdd7e36a6dd5, ttp--mitre-campaign--d32f2450374e9ec586b2, ttp--mitre-campaign--df58953754d2afbde180, ttp--mitre-campaign--e4822e50db468b9f83f6, ttp--mitre-campaign--ea16c435dccfb5940d11 |  | encryption: The activity combined ransomware, wiper malware, and data leak operations.<br>destruction: The activity combined ransomware, wiper malware, and data leak operations. | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 2026-05-12 | 高 | `source--mitre-attack-19-1` |
| 被害事例: BiBiワイパーの新バージョンがディスクパーティションテーブルも破壊 | 非公開 | anonymous | unknown | reported |  |  | ttp--activity-rule--7e8a4b46dd7a5b9c6c08 |  | destruction: BiBiワイパーの新バージョンがディスクパーティションテーブルも破壊 | 不明 | 不明 | 2024-05-21 | 中 | `source--daily-0d70b2cb1fe1f39ff860` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Impact | T1485 | Data Destruction | BiBiワイパーの新バージョンがディスクパーティションテーブルも破壊 |  | activity--daily-d27082c5bfe4d81ba84c | 不明 | 不明 | 中 | `source--daily-0d70b2cb1fe1f39ff860` |
| Initial Access | T1190 | Exploit Public-Facing Application | For [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors exploited CVE-2019-0604 in Microsoft SharePoint for initial access.(Citation: CISA Iran Albanian Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.003 | Code Signing Certificates | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used tools with legitimate code signing certificates. (Citation: CISA Iran Albanian Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1134.001 | Token Impersonation/Theft | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used custom tooling to acquire tokens using `ImpersonateLoggedOnUser/SetThreadToken`.(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors primarily used RDP for lateral movement in the victim environment.(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used SMB for lateral movement.(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors modified and disabled components of endpoint detection and response (EDR) solutions including Microsoft Defender Antivirus.(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors dumped LSASS memory on compromised hosts.(Citation: CISA Iran Albanian Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.002 | Remote Email Collection | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors made multiple HTTP POST requests to the Exchange servers of the victim organization to transfer data.(Citation: CISA Iran Albanian Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used web shells to download files to compromised infrastructure.(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.001 | Disable or Modify Windows Event Log | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors deleted Windows events and application logs.(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used Windows batch files for persistence and execution.(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used HTTP to transfer data from compromised Exchange servers.(Citation: CISA Iran Albanian Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used a compromised Exchange account to search mailboxes and create new Exchange accounts.(Citation: CISA Iran Albanian Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors executed the Advanced Port Scanner tool on compromised systems.(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors renamed [ROADSWEEP](https://attack.mitre.org/software/S1150) to GoXML.exe and [ZeroCleare](https://attack.mitre.org/software/S1151) to cl.exe.(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Mandiant ROADSWEEP August 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used tools including Advanced Port Scanner, [Mimikatz](https://attack.mitre.org/software/S0002), and [Impacket](https://attack.mitre.org/software/S0357).(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.002 | Additional Email Delegate Permissions | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors added the `ApplicationImpersonation` management role to accounts under their control to impersonate users and take ownership of targeted mailboxes.(Citation: Microsoft Albanian Government Attacks September 2022)<br> |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Impact | T1561.002 | Disk Structure Wipe | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used a version of [ZeroCleare](https://attack.mitre.org/software/S1151) to wipe disk drives on targeted hosts.(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors initiated a process named Mellona.exe to spread the [ROADSWEEP](https://attack.mitre.org/software/S1150) file encryptor and a persistence script to a list of internal machines.(Citation: CISA Iran Albanian Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used [ROADSWEEP](https://attack.mitre.org/software/S1150) ransomware to encrypt files on targeted systems.(Citation: Mandiant ROADSWEEP August 2022)(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.003 | Email Account | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used compromised Exchange accounts to search mailboxes for administrator accounts.(Citation: CISA Iran Albanian Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.001 | Default Accounts | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used the built-in administrator account to move laterally using RDP and [Impacket](https://attack.mitre.org/software/S0357).(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used PowerShell cmdlets New-MailboxSearch and Get-Recipient for discovery.(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | For [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used .aspx webshells named pickers.aspx, error4.aspx, and ClientBin.aspx, to maintain persistence.(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | During [HomeLand Justice](https://attack.mitre.org/campaigns/C0038), threat actors used WMI to modify Windows Defender settings.(Citation: Microsoft Albanian Government Attacks September 2022) |  | activity--homeland-justice | 2021-05-01T04:00:00.000Z | 2022-09-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has dumped LSASS credentials using `comsvcs.dll` via `rundll32.exe`.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has collected cached data and files from within the victim environment.(Citation: SPECOPS Outpost24 Handala Hack Stryker March 2026)(Citation: DOJ FBI Handala Hack March 2026)(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used RDP to move laterally within the victim environment.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.015 | Compression | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has compressed their payloads by leveraging zip files.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has masqueraded as commonly used programs and services on Windows hosts.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has masqueraded malicious payloads to resemble legitimate applications.(Citation: DOJ FBI Handala Hack March 2026)(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged malicious payloads that use nomenclature associated with common applications that include Pictory, KeePass, WhatsApp, and Telegram.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) malware has exfiltrated collected data via Telegram bot C2 channels using encrypted communications.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized WMIC to log into the victim host and create a process `process call create “cmd.exe /c  copy \\?\\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\system c:\users\public”`.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized PowerShell to execute malware in victim environments.(Citation: DOJ FBI Handala Hack March 2026)(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized Python scripts to execute its malicious payloads.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized HTTPS for communication to C2 domains.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Lateral Movement | T1072 | Software Deployment Tools | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged legitimate built-in features of cloud-based management platforms to include mobile device management (MDM) and Remote Monitoring and Management (RMM) solutions.(Citation: SPECOPS Outpost24 Handala Hack Stryker March 2026)(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also initiated built-in remote wipe instructions using a privileged account within Microsoft Intune.(Citation: SPECOPS Outpost24 Handala Hack Stryker March 2026)(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074 | Data Staged | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has staged compressed files in specified locations prior to exfiltration over C2.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged valid accounts to log into VPN infrastructure.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used compromised valid credentials to gain access to management infrastructure and enterprise control systems.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also validated and tested authentication using compromised credentials prior to malicious actions.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used previously compromised Domain Administrator credentials to maintain persistent access.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.004 | Cloud Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged privileged cloud accounts to access cloud-based management consoles to include Microsoft Intune.(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also compromised existing accounts within the Microsoft Entra ID environment.(Citation: SEC 8-K Stryker Corporation Filing Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered system information and disseminated it back to C2.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized ADRecon to enumerate the active directory environment.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098 | Account Manipulation | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged access to administrative control systems to achieve disruptive effects, consistent with administrative account abuse or privilege escalation within existing access.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026)(Citation: SEC 8K Palo Alto Statement Stryker Corp Handala March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized Telegram API for C2.(Citation: DOJ FBI Handala Hack March 2026)(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has deployed additional payloads from dedicated C2 servers.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: DOJ FBI Handala Hack March 2026)(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also downloaded legitimate tools and software from publicly available services.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) had utilized VeraCrypt a legitimate disk encrypting utility that was downloaded directly from the website.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has conducted brute-force attempts against organizational VPN infrastructure.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.001 | Password Guessing | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has conducted password guessing to gain initial access.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.004 | Credential Stuffing | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized credential stuffing attacks to obtain initial access to victim environments.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has captured screen content during an active Zoom session.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.002 | Remote Email Collection | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered victim email-content from victim servers.(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) conducted large-scale data exfiltration in the Stryker operation, consistent with automated or scripted collection against enterprise systems.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1123 | Audio Capture | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered audio during a Zoom session.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1125 | Video Capture | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has collected video from compromised victim devices.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged public facing VPN infrastructure to gain initial access to victim environments.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has exploited public facing vulnerabilities within victim environments to include SharePoint CVE-2019-0604.(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has targeted IT and service providers in an effort to obtain credentials, relying largely on compromised VPN accounts for initial access.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has delivered malicious payloads that initiate through user execution to include interaction with a masqueraded file.(Citation: DOJ FBI Handala Hack March 2026)(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used trojanized application lures to induce targets into executing malware enabling persistent surveillance.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.002 | Sharepoint | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has accessed victim’s public facing SharePoint servers and exfiltrated data.(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219.002 | Remote Desktop Software | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has installed NetBird on victim devices to create a mesh network that facilitated control of several victim devices at once.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Privilege Escalation | T1484.001 | Group Policy Modification | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) had utilized Group Policy logon scripts to distribute the malicious payloads to victim devices through the execution of a batch file.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1485 | Data Destruction | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has conducted data wiping attacks on compromised systems.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: SPECOPS Outpost24 Handala Hack Stryker March 2026)(Citation: DOJ FBI Handala Hack March 2026)(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also manually deleted files from compromised hosts, to include selecting all files and then deleting them.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized legitimate disk encryption utilities to increase likelihood of encrypting system drives and reduce system recovery efforts.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1490 | Inhibit System Recovery | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has deleted virtual machines directly from the virtualization platform.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has created Windows Registry entries to autorun stage two malware payloads to maintain persistence.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.002 | Credentials in Registry | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) had exported credentials from registry hives to include those stored in HKLM.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has stored collected data in a password protected compressed file prior to exfiltration.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1561.001 | Disk Content Wipe | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized a disk wiping utility to facilitate destructive actions on victim servers.(Citation: DOJ FBI Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also utilized legitimate remote disk wiping commands.(Citation: SPECOPS Outpost24 Handala Hack Stryker March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1561.002 | Disk Structure Wipe | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has deployed custom wipers that overwrite system files and the host devices master boot records (MBR) to corrupt or destroy files.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.003 | Hidden Window | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized PowerShell scripts that run without notifying the user of its execution to include `-nop -w hidden- ep bypass -enc`.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has emailed victims threatening messages.(Citation: DOJ FBI Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used phishing as an initial access vector.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used tunneling tools to facilitate destructive attacks on compromised devices.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has registered domains for messaging purposes.(Citation: SPECOPS Outpost24 Handala Hack Stryker March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has created typosquatted domains and sub-domains in attempts to avoid detection or draw suspicion.(Citation: DOJ FBI Handala Hack March 2026)(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also purchased domains leveraging cryptocurrency platforms to include LiteCoin and Ramzinex.(Citation: DOJ FBI Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has registered and rotated domains to support public-facing dissemination infrastructure, replacing disrupted domains with new registrations.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized VPS solutions for C2.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.004 | Server | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged backend servers within Iran.(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has obtained access to commercial VPN services to launch malicious activity.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: SPECOPS Outpost24 Handala Hack Stryker March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also leveraged Starlink internet services.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has used operator-controlled Telegram bots and channels as C2 infrastructure.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has created Telegram Accounts.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also leveraged online personas such as Handala Hack, Karma, and Homeland Justice on social media to include Telegram.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: SPECOPS Outpost24 Handala Hack Stryker March 2026)(Citation: DOJ FBI Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has established and maintained social media accounts on Twitter/X and Telegram to amplify operational claims and stolen data disclosures.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has created email accounts to send threatening messages to victims to include ‘Handala_Team[@]outlook[.]com’.(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has utilized custom-malware and wipers to include BiBi Wiper.(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has developed or obtained trojanized applications used for persistent surveillance of targeted individuals.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has obtained and utilized commercial VPN services, open-source software and publicly available offensive security tools to facilitate malicious activities.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered details on their intended victims to aid in social engineering efforts for leveraging tailored themes of attacks.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has scanned victim environments for susceptibility to vulnerability exploitation.(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1651 | Cloud Administration Command | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has abused built-in remote wipe or factory reset commands to wipe devices managed within an organization’s Cloud management solution impacting laptops, servers, and mobile devices.(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has conducted data exfiltration and posted stolen information on data leak sites for the purposes of financial and political extortion.(Citation: SPECOPS Outpost24 Handala Hack Stryker March 2026)(Citation: DOJ FBI Handala Hack March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also sold stolen data to prospective buyers for cryptocurrency.(Citation: DOJ FBI Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1679 | Selective Exclusion | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has avoided interacting with specific directories in order to reduce the likelihood of detection.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has impersonated individuals familiar to the victim and technical support associated with social messaging services.(Citation: FBI IC3 Flash VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686.003 | Windows Host Firewall | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has disabled Windows Defender protections to allow for follow-on activities within the compromised host.(Citation: Check Point VOID MANTICORE Handala Hack March 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 65件（`artifacts.csv`）

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
| source--daily-0d70b2cb1fe1f39ff860 | BiBiワイパーの新バージョンがディスクパーティションテーブルも破壊 | bleepingcomputer.com | 2024-05-21 | https://www.bleepingcomputer.com/news/security/new-bibi-wiper-version-also-destroys-the-disk-partition-table/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--void-manticore--0402ab708c2b3b30 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--void-manticore--0ad84d5ffade7472 | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--15b241fd48f227db | Semiannual+Ransomware+Report+ +H1+2024 |  | 2024 | cybercrime/2024/Semiannual+Ransomware+Report+-+H1+2024.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--1cf02c350fe8a86e | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--40ac301c05170014 | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--432520f2738bbc2c | void manticore |  | 不明 | actor_profile/evidence/void-manticore.csv | structured-data | TLP:CLEAR | 中 |
| source--void-manticore--491ffb169527ff34 | Russian Ransomware C2 Network Discovered in Censys Data |  | 不明 | summary/2022/Russian Ransomware C2 Network Discovered in Censys Data.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--5f00205af443971a | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--6c4456aaa341ac6c | the rise of state sponsored hacktivism |  | 不明 | Anonymous/the-rise-of-state-sponsored-hacktivism.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--7001c6c11351daa6 | mobile APT threat report |  | 不明 | mobile-APT/mobile-APT-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--a1f77e6e9c133da5 | VB2022 Exploit archaeology a forensic history of in the wild NSO Group exploits |  | 2022 | NSOGroup/VB2022-Exploit-archaeology-a-forensic-history-of-in-the-wild-NSO-Group-exploits.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--a3e1662f3971c94c | Claude Mythos Preview System Card |  | 不明 | AISecurity/Claude Mythos Preview System Card.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--a7dc8c791d13500e | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--ae6876bd7aa0f48a | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--b9b346da5842493e | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--bede1a8da90bf2b0 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--c6ce9deb8a7e5fa5 | Public Report EN 2025 DIGITAL |  | 2025 | International Strategic/Canada/Public Report_EN_2025_DIGITAL.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--caf4bc945a22099d | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--d79d08d6c77f4ed5 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--e61cfd99872b143b | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--eb26cccb5d8b7a99 | tool of first resort israel hamas war cyber |  | 不明 | summary/2024/tool-of-first-resort-israel-hamas-war-cyber.pdf | report | TLP:CLEAR | 中 |
| source--void-manticore--ef9c292f567e0dc2 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
