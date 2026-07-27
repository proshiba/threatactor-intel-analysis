# Darkhotel 脅威アクタープロファイル

- プロファイルID: `actor--darkhotel`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Darkhotelの標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Darkhotel**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DUBNIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Zigzag Hail | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Tardigrade Spider | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 81; mapping requires review. |
| Luder | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 81; mapping requires review. |
| Karba | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 81; mapping requires review. |
| Tapaoux | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 81; mapping requires review. |
| Nemim | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 81; mapping requires review. |
| Dubnium (Microsoft) | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 81; mapping requires review. |
| APT-C-06, SHADOW CRANE, T-APT-02, SIG25 (NSA), | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 81; mapping requires review. |
| Information on Chinese forum indicating group may have targeted CVE-2015-8651, most likely a South Korean actor | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 81; mapping requires review. |

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
| Adversary | [Darkhotel](https://attack.mitre.org/groups/G0012) is a suspected South Korean threat group that has targeted victims primarily in East Asia since at least 2004. The group's name is based on cyber espionage operations conducted via hotel Internet networks against traveling executives and other select guests. [Darkhotel](https://attack.mitre.org/groups/G0012) has also conducted spearphishing campaigns and infected victims through peer-to-peer and file sharing networks.(Citation: Kaspersky Darkhotel)(Citation: Securelist Darkhotel Aug 2015)(Citation: Microsoft Digital Defense FY20 Sept 2020) |
| Capability | Inexsmar, Higaisa, Win32.Karba, Win32.Pioneer, CVE-2015-8651, Asruex, CVE-2012-0158, CVE-2010-2883, CVE-2016-4171 and CVE-2018-817 |
| Infrastructure |  |
| Victim | Japan, Taiwan, China, Russia, South Korea, North Korea Government, Utilities, High-Tech, Automotive |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | DarkHotel | canonical-name | 高 | South Korea | https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070901/darkhotelappendixindicators_kl.pdf<br>https://www.securityweek.com/darkhotel-apt-uses-new-methods-target-politicians |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Zigzag Hail | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | DarkHotel | canonical-name | 高 | KR, Korea (Republic of) | https://securelist.com/blog/research/71713/darkhotels-attacks-in-2015/<br>https://blogs.technet.microsoft.com/mmpc/2016/06/09/reverse-engineering-dubnium-2<br>https://securelist.com/blog/research/66779/the-darkhotel-apt/ |
| misp-microsoft-activity-group | DUBNIUM | canonical-name | 高 |  | https://securelist.com/blog/research/71713/darkhotels-attacks-in-2015/<br>https://blogs.technet.microsoft.com/mmpc/2016/06/09/reverse-engineering-dubnium-2<br>https://blogs.technet.microsoft.com/mmpc/2016/06/20/reverse-engineering-dubniums-flash-targeting-exploit/ |
| misp-microsoft-activity-group | Zigzag Hail | canonical-name | 高 | KR | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Darkhotel - G0012 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0012<br>https://securelist.com/files/2014/11/darkhotel%20kl%2007.11.pdf |
| misp-mitre-intrusion-set | Darkhotel - G0012 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0012<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf |
| misp-360net | Darkhotel - APT-C-06 | multiple-name-intersection | 高 | southKorea | https://apt.360.net/report/apts/97.html<br>https://apt.360.net/report/apts/3.html |

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
| malware--inexsmar | Inexsmar | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--higaisa | Higaisa | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--win32-karba | Win32.Karba | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--win32-pioneer | Win32.Pioneer | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2015-8651 | CVE-2015-8651 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--asruex | Asruex | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2012-0158 | CVE-2012-0158 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2010-2883 | CVE-2010-2883 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2016-4171-and-cve-2018-817 | CVE-2016-4171 and CVE-2018-817 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| Daybreak? | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Fallout Team | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| WizardOpium | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Daybreak?; Fallout Team; WizardOpium

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | South Korea | Targeting text mentions south korea. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | North Korea | Targeting text mentions north korea. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Russia | Targeting text mentions russia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Taiwan | Targeting text mentions taiwan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Japan | Targeting text mentions japan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | China | Targeting text mentions china. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1001 | Data Obfuscation | 6 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/762.html |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection | T1005 | Data from Local System | 御见威胁情报中心 72 / 73 T1082 System Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https:/ |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1007 | System Service Discovery | TLP：WHITE 腾讯安全御见威胁情报中心 72 / 73 T1082 System Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protoc |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1024 | MITRE ATT&CK T1024 | l System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/762.html |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1027 | Obfuscated Files or Information | 0 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1035 | MITRE ATT&CK T1035 | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1036 | Masquerading | ing T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Dis |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1043 | Commonly Used Port | l Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/76 |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1046 | Network Service Discovery | Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection, Credential Access | T1056 | Input Capture | 107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection, Credential Access | T1056.001 | Keylogging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1060 | MITRE ATT&CK T1060 | T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Uncategorized | T1065 | MITRE ATT&CK T1065 | creen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/762.html |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Lateral Movement | T1080 | Taint Shared Content | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-1` |
| Uncategorized | T1085 | MITRE ATT&CK T1085 | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1 |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Initial Access, Lateral Movement | T1091 | Replication Through Removable Media | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1094 | MITRE ATT&CK T1094 | n T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/762.html |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Uncategorized | T1099 | MITRE ATT&CK T1099 | T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | taryfocus.net vachel.vicp.cc 180.150.227.24 39.109.4.143 103.81.171.157 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Uncategorized | T1107 | MITRE ATT&CK T1107 | rsistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discove |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Defense Impairment, Persistence | T1112 | Modify Registry | plication Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection | T1113 | Screen Capture | Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection | T1114 | Email Collection | Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/0 |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection | T1123 | Audio Capture | TLP：WHITE 腾讯安全御见威胁情报中心 72 / 73 T1082 System Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1124 | System Time Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1129 | Shared Modules | 180.150.227.24 39.109.4.143 103.81.171.157 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1135 | Network Share Discovery | T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Persistence | T1137 | Office Application Startup | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-1` |
| Uncategorized | T1179 | MITRE ATT&CK T1179 | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Crede |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1193 | MITRE ATT&CK T1193 | m www.phpvlan.com wiki.xxxx.com game.militaryfocus.net vachel.vicp.cc 180.150.227.24 39.109.4.143 103.81.171.157 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-1` |
| Execution | T1204 | User Execution | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T10 |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497.001 | System Checks | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497.002 | User Activity Based Checks | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1534 | Internal Spearphishing | TLP：WHITE 腾讯安全御见威胁情报中心 72 / 73 T1082 System Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Dat |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 97件
- IOC観測: 118件
- 複数攻撃で観測: 0件
- 要レビュー候補: 80件
- 非IOC artifact観測: 48件（`artifacts.csv`）

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
| source--darkhotel--6be8f2f16af88e57 | README |  | 不明 | Darkhotel/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--darkhotel--a8acea942272273e | README |  | 不明 | Darkhotel/higaisa/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--darkhotel--ce28b9f812e95fb7 | higaisa apt report |  | 不明 | Darkhotel/higaisa/higaisa_apt_report.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
