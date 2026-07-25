# Transparent Tribe 脅威アクタープロファイル

プロファイルID: `actor--transparent-tribe`  
状態: draft  
更新日時: 2026-07-25T14:07:08Z  
構造バージョン: 1.0.0

## エグゼクティブサマリー

Transparent Tribeの標準化プロファイル。リポジトリ内の専用資料4件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Transparent Tribe**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT36 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| COPPER FIELDSTONE | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Mythic Leopard | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ProjectM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Temp.Lapis | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 13; mapping requires review. |
| Green Havildar | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 13; mapping requires review. |
| APT-C-56 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 13; mapping requires review. |
| Vietnam or Pakistan | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 13; mapping requires review. |

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
| Adversary | [Transparent Tribe](https://attack.mitre.org/groups/G0134) is a suspected Pakistan-based threat group that has been active since at least 2013, primarily targeting diplomatic, defense, and research organizations in India and Afghanistan.(Citation: Proofpoint Operation Transparent Tribe March 2016)(Citation: Kaspersky Transparent Tribe August 2020)(Citation: Talos Transparent Tribe May 2021) |
| Capability | Crimson, DarkComet, ObliqueRAT, Peppy, njRAT, Crimson RAT, Limepad |
| Infrastructure |  |
| Victim | Government of India diplomatic and military |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Transparent Tribe, APT 36 | canonical-name | 高 | Pakistan | https://www.fireeye.com/blog/threat-research/2016/06/apt_group_sends_spea.html<br>https://www.crowdstrike.com/blog/adversary-of-the-month-for-may/<br>https://cyberstanc.com/blog/a-look-into-apt36-transparent-tribe/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Viridian Vortex | canonical-name | 高 | Pakistan | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Operation C-Major | canonical-name | 高 | PK, Pakistan | http://documents.trendmicro.com/assets/pdf/Indian-military-personnel-targeted-by-information-theft-campaign-cmajor.pdf<br>https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf<br>https://www.amnesty.org/en/documents/asa33/8366/2018/en/ |
| misp-microsoft-activity-group | Storm-0156 | canonical-name | 高 | PK, Pakistan | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Transparent Tribe - G0134 | mitre-external-id | 高 |  | https://adversary.crowdstrike.com/en-US/adversary/mythic-leopard/<br>https://attack.mitre.org/groups/G0134<br>https://blog.talosintelligence.com/2021/05/transparent-tribe-infra-and-targeting.html |
| misp-360net | 透明部落 - APT-C-56 | multiple-name-intersection | 高 | southeast |  |

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
| malware--crimson | Crimson | [Crimson](https://attack.mitre.org/software/S0115) is a remote access Trojan that has been used by [Transparent Tribe](https://attack.mitre.org/groups/G0134) since at least 2016.(Citation: Proofpoint Operation Transparent Tribe March 2016)(Citation: Kaspersky Transparent Tribe August 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--darkcomet | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) is a Windows remote administration tool and backdoor.(Citation: TrendMicro DarkComet Sept 2014)(Citation: Malwarebytes DarkComet March 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--obliquerat | ObliqueRAT | [ObliqueRAT](https://attack.mitre.org/software/S0644) is a remote access trojan, similar to [Crimson](https://attack.mitre.org/software/S0115), that has been in use by [Transparent Tribe](https://attack.mitre.org/groups/G0134) since at least 2020.(Citation: Talos Oblique RAT March 2021)(Citation: Talos Transparent Tribe May 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--peppy | Peppy | [Peppy](https://attack.mitre.org/software/S0643) is a Python-based remote access Trojan, active since at least 2012, with similarities to [Crimson](https://attack.mitre.org/software/S0115).(Citation: Proofpoint Operation Transparent Tribe March 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--njrat | njRAT | [njRAT](https://attack.mitre.org/software/S0385) is a remote access tool (RAT) that was first observed in 2012. It has been used by threat actors in the Middle East.(Citation: Fidelis njRAT June 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--crimson-rat | Crimson RAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--limepad | Limepad | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

| 活動 | 種別 | 初回 | 最終 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| Operation C-Major | operation | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| C0011 | campaign | 2021-12-01T06:00:00.000Z | 2022-07-01T05:00:00.000Z | [C0011](https://attack.mitre.org/campaigns/C0011) was a suspected cyber espionage campaign conducted by [Transparent Tribe](https://attack.mitre.org/groups/G0134) that targeted students at universities and colleges in India. Security researchers noted this campaign against students was a significant shift from [Transparent Tribe](https://attack.mitre.org/groups/G0134)'s historic targeting Indian government, military, and think tank personnel, and assessed it was still ongoing as of July 2022.(Citation: Cisco Talos Transparent Tribe Education Campaign July 2022)  | 高 | `source--mitre-attack-19-1` |

Operation C-Major

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | India | Targeting text mentions india. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | overy T1057 File and Directory DiscoveryDiscovery T1083 Network DiscoveryDiscovery T1016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen CaptureCollection T1113 Application Layer Protocol: Web ProtocolsCommand and Control T1071.001 Application Layer Protocol: WebSocketCommand and Control T1071.004 Ingress Tool TransferComm |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Discovery | T1016 | System Network Configuration Discovery | ryDiscovery T1082 Clipboard DataCredential Access T1115 Process DiscoveryDiscovery T1057 File and Directory DiscoveryDiscovery T1083 Network DiscoveryDiscovery T1016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen CaptureCollection T1113 Application Layer Protocol: Web ProtocolsCommand and Control T1071.001 Application Lay |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Collection | T1025 | Data from Removable Media | 016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen CaptureCollection T1113 Application Layer Protocol: Web ProtocolsCommand and Control T1071.001 Application Layer Protocol: WebSocketCommand and Control T1071.004 Ingress Tool TransferCommand and Control T1105 Non-Application Layer ProtocolCommand and Control T1095 Exfiltr |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Stealth | T1027 | Obfuscated Files or Information | raft Targeting Indian Government and Defence Create or Modify System Process: Systemd ServicePersistence T1543.002 Obfuscated/Encrypted PayloadsDefense Evasion T1027 MasqueradingDefense Evasion T1036 Deobfuscate/Decode Files or InformationDefense Evasion T1140 Credentials from Password StoresCredential Access T1555 Signed Binary Proxy ExecutionDefense Evasion https://blog.sekoia.io/transparenttribe-targets-indian-military-organisations-with- |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | nd Defence Create or Modify System Process: Systemd ServicePersistence T1543.002 Obfuscated/Encrypted PayloadsDefense Evasion T1027 MasqueradingDefense Evasion T1036 Deobfuscate/Decode Files or InformationDefense Evasion T1140 Credentials from Password StoresCredential Access T1555 Signed Binary Proxy ExecutionDefense Evasion https://blog.sekoia.io/transparenttribe-targets-indian-military-organisations-with-deskrat/#h-delivery-zip-archive ht |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | ntrol T1071.004 Ingress Tool TransferCommand and Control T1105 Non-Application Layer ProtocolCommand and Control T1095 Exfiltration Over C2 ChannelExfiltration T1041 Encrypted Channel: Asymmetric Command and Control T1573.002 Data Manipulation: Stored Data Impact T1565.001 References |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Discovery | T1057 | Process Discovery | com/PrakkiSathwik/status/2006431447759073484 T1218 System Information DiscoveryDiscovery T1082 Clipboard DataCredential Access T1115 Process DiscoveryDiscovery T1057 File and Directory DiscoveryDiscovery T1083 Network DiscoveryDiscovery T1016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen CaptureCollection T1113 Applicati |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Execution | T1059.001 | PowerShell | alicious FileInitial Access T1204.002 Command and Scripting Interpreter: Visual BasicExecution T1059.005 Command and Scripting Interpreter: PowerShellExecution T1059.001 Command and Scripting Interpreter: Unix ShellExecution T1059.004 Command and Scripting Interpreter: JavaScriptExecution T1059.007 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Persistence T1547.001 Signed Binary Proxy Execution: MshtaExecution T1218.005 |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Execution | T1059.004 | Unix Shell | preter: Visual BasicExecution T1059.005 Command and Scripting Interpreter: PowerShellExecution T1059.001 Command and Scripting Interpreter: Unix ShellExecution T1059.004 Command and Scripting Interpreter: JavaScriptExecution T1059.007 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Persistence T1547.001 Signed Binary Proxy Execution: MshtaExecution T1218.005 Tunnelling Certification Course.pdf.lnk SHA256 Type |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Execution | T1059.007 | JavaScript | erpreter: PowerShellExecution T1059.001 Command and Scripting Interpreter: Unix ShellExecution T1059.004 Command and Scripting Interpreter: JavaScriptExecution T1059.007 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Persistence T1547.001 Signed Binary Proxy Execution: MshtaExecution T1218.005 Tunnelling Certification Course.pdf.lnk SHA256 Type File Name 5ee6a5ff2e3c39cd88e9ccdc6a50b7ad 3f9c7488b |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Command And Control | T1071.001 | Web Protocols | DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen CaptureCollection T1113 Application Layer Protocol: Web ProtocolsCommand and Control T1071.001 Application Layer Protocol: WebSocketCommand and Control T1071.004 Ingress Tool TransferCommand and Control T1105 Non-Application Layer ProtocolCommand and Control T1095 Exfiltration Over C2 ChannelExfiltration T1041 Encrypted Channel: Asymmetric Command and Control T1573.002 Da |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Command And Control | T1071.004 | DNS | Screen CaptureCollection T1113 Application Layer Protocol: Web ProtocolsCommand and Control T1071.001 Application Layer Protocol: WebSocketCommand and Control T1071.004 Ingress Tool TransferCommand and Control T1105 Non-Application Layer ProtocolCommand and Control T1095 Exfiltration Over C2 ChannelExfiltration T1041 Encrypted Channel: Asymmetric Command and Control T1573.002 Data Manipulation: Stored Data Impact T1565.001 References |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Discovery | T1082 | System Information Discovery | 0836683933 https://x.com/RedDrip7/status/1999311448552710501 https://x.com/PrakkiSathwik/status/2006431447759073484 T1218 System Information DiscoveryDiscovery T1082 Clipboard DataCredential Access T1115 Process DiscoveryDiscovery T1057 File and Directory DiscoveryDiscovery T1083 Network DiscoveryDiscovery T1016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from R |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Discovery | T1083 | File and Directory Discovery | T1218 System Information DiscoveryDiscovery T1082 Clipboard DataCredential Access T1115 Process DiscoveryDiscovery T1057 File and Directory DiscoveryDiscovery T1083 Network DiscoveryDiscovery T1016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen CaptureCollection T1113 Application Layer Protocol: Web ProtocolsCommand and |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Command And Control | T1095 | Non-Application Layer Protocol | ication Layer Protocol: WebSocketCommand and Control T1071.004 Ingress Tool TransferCommand and Control T1105 Non-Application Layer ProtocolCommand and Control T1095 Exfiltration Over C2 ChannelExfiltration T1041 Encrypted Channel: Asymmetric Command and Control T1573.002 Data Manipulation: Stored Data Impact T1565.001 References |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Command And Control | T1105 | Ingress Tool Transfer | rotocol: Web ProtocolsCommand and Control T1071.001 Application Layer Protocol: WebSocketCommand and Control T1071.004 Ingress Tool TransferCommand and Control T1105 Non-Application Layer ProtocolCommand and Control T1095 Exfiltration Over C2 ChannelExfiltration T1041 Encrypted Channel: Asymmetric Command and Control T1573.002 Data Manipulation: Stored Data Impact T1565.001 References |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Collection | T1113 | Screen Capture | T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen CaptureCollection T1113 Application Layer Protocol: Web ProtocolsCommand and Control T1071.001 Application Layer Protocol: WebSocketCommand and Control T1071.004 Ingress Tool TransferCommand and Control T1105 Non-Application Layer ProtocolCommand and Control T1095 Exfiltration Over C2 ChannelExfiltrati |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Collection | T1115 | Clipboard Data | us/1999311448552710501 https://x.com/PrakkiSathwik/status/2006431447759073484 T1218 System Information DiscoveryDiscovery T1082 Clipboard DataCredential Access T1115 Process DiscoveryDiscovery T1057 File and Directory DiscoveryDiscovery T1083 Network DiscoveryDiscovery T1016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Discovery | T1120 | Peripheral Device Discovery | covery T1083 Network DiscoveryDiscovery T1016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen CaptureCollection T1113 Application Layer Protocol: Web ProtocolsCommand and Control T1071.001 Application Layer Protocol: WebSocketCommand and Control T1071.004 Ingress Tool TransferCommand and Control T1105 Non-Application Layer |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | rsistence T1543.002 Obfuscated/Encrypted PayloadsDefense Evasion T1027 MasqueradingDefense Evasion T1036 Deobfuscate/Decode Files or InformationDefense Evasion T1140 Credentials from Password StoresCredential Access T1555 Signed Binary Proxy ExecutionDefense Evasion https://blog.sekoia.io/transparenttribe-targets-indian-military-organisations-with-deskrat/#h-delivery-zip-archive https://www.seqrite.com/blog/umbrella-of-pakistani-threats-conv |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Stealth | T1218 | System Binary Proxy Execution | 895 https://x.com/G60930953/status/1999677100836683933 https://x.com/RedDrip7/status/1999311448552710501 https://x.com/PrakkiSathwik/status/2006431447759073484 T1218 System Information DiscoveryDiscovery T1082 Clipboard DataCredential Access T1115 Process DiscoveryDiscovery T1057 File and Directory DiscoveryDiscovery T1083 Network DiscoveryDiscovery T1016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Stealth | T1218.005 | Mshta | tExecution T1059.007 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Persistence T1547.001 Signed Binary Proxy Execution: MshtaExecution T1218.005 Tunnelling Certification Course.pdf.lnk SHA256 Type File Name 5ee6a5ff2e3c39cd88e9ccdc6a50b7ad 3f9c7488bfc49a6c511379aceb91725c LNK Tunnelling_Certification_Course.pdf0df9cb5b73822a8a44d0122fad943f376 a5e5d7bbb927bc86743dff0379fa3fc ELF project vijayak |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Discovery | T1518.001 | Security Software Discovery | edential Access T1115 Process DiscoveryDiscovery T1057 File and Directory DiscoveryDiscovery T1083 Network DiscoveryDiscovery T1016 Software DiscoveryDiscovery T1518.001 Data from Local SystemCollection T1005 Peripheral Device DiscoveryDiscovery T1120 Data from Removable MediaCollection T1025 Screen CaptureCollection T1113 Application Layer Protocol: Web ProtocolsCommand and Control T1071.001 Application Layer Protocol: WebSocketCommand and Cont |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Persistence, Privilege Escalation | T1543.002 | Systemd Service | ling Transparent Tribe’s (APT36) C&C and Network Tradecraft Targeting Indian Government and Defence Create or Modify System Process: Systemd ServicePersistence T1543.002 Obfuscated/Encrypted PayloadsDefense Evasion T1027 MasqueradingDefense Evasion T1036 Deobfuscate/Decode Files or InformationDefense Evasion T1140 Credentials from Password StoresCredential Access T1555 Signed Binary Proxy ExecutionDefense Evasion https://blog.sekoia.io/transpare |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | n T1059.004 Command and Scripting Interpreter: JavaScriptExecution T1059.007 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Persistence T1547.001 Signed Binary Proxy Execution: MshtaExecution T1218.005 Tunnelling Certification Course.pdf.lnk SHA256 Type File Name 5ee6a5ff2e3c39cd88e9ccdc6a50b7ad 3f9c7488bfc49a6c511379aceb91725c LNK Tunnelling_Certification_Course.pdf0df9cb5b73822a8a44d0122fad943f |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Credential Access | T1555 | Credentials from Password Stores | Evasion T1027 MasqueradingDefense Evasion T1036 Deobfuscate/Decode Files or InformationDefense Evasion T1140 Credentials from Password StoresCredential Access T1555 Signed Binary Proxy ExecutionDefense Evasion https://blog.sekoia.io/transparenttribe-targets-indian-military-organisations-with-deskrat/#h-delivery-zip-archive https://www.seqrite.com/blog/umbrella-of-pakistani-threats-converging-tactics-of-cyber-operations-targeting-india/ http |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Stealth | T1564.001 | Hidden Files and Directories | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1565.001 | Stored Data Manipulation | Control T1095 Exfiltration Over C2 ChannelExfiltration T1041 Encrypted Channel: Asymmetric Command and Control T1573.002 Data Manipulation: Stored Data Impact T1565.001 References |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Command And Control | T1568 | Dynamic Resolution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.002 | Asymmetric Cryptography | T1105 Non-Application Layer ProtocolCommand and Control T1095 Exfiltration Over C2 ChannelExfiltration T1041 Encrypted Channel: Asymmetric Command and Control T1573.002 Data Manipulation: Stored Data Impact T1565.001 References |  |  | 不明 | 不明 | 中 | `source--transparent-tribe--8c7cc7c46f9a6fd9` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.004 | Drive-by Target | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 451件
- IOC観測: 531件
- 複数攻撃で観測: 0件
- 要レビュー候補: 85件
- 非IOC artifact観測: 72件（`artifacts.csv`）

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
| source--transparent-tribe--0f08047cfac5b7bb | README |  | 不明 | APT36/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--transparent-tribe--8c7cc7c46f9a6fd9 | transparent tribe apt36 cc network tradecraft report |  | 不明 | APT36/transparent-tribe-apt36-cc-network-tradecraft-report.pdf | report | TLP:CLEAR | 中 |
| source--transparent-tribe--be73ac7ec108bc35 | README |  | 不明 | TransparentTribe/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--transparent-tribe--3fb4d998121e8765 | transparent tribe threat insight en2020 |  | 2020 | TransparentTribe/transparent-tribe-threat-insight-en2020.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
