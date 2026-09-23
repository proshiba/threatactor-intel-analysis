# Darkhotel 脅威アクタープロファイル

- プロファイルID: `actor--darkhotel`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Darkhotelの標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Darkhotel**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT-C-06 | 360高级威胁研究院 / 360威胁情报中心 | overlapping | 高 | `source--360-apt-c-06-darkhotel-kctv-lure-2026` | 360の一次資料は記事名と本文でAPT-C-06（Darkhotel）と併記し、既知のDarkhotel沿革も説明する。360内の呼称対応は明示されるが、cross-vendorの収集境界が完全一致するとは限らないためscopeはoverlappingとする。 |
| DUBNIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Zigzag Hail | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | Actor-specific reporting explicitly describes espionage or intelligence collection. | 高 | `source--mitre-attack-19-1`, `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description; not inferred from country or state sponsorship. |

## 他アクターとの関係

確認された関係なし

## 関連する企業・個人

関連エンティティなし

### エンティティ関係

確認された関係なし

### 法的措置

確認された法的措置なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | DarkHotel | canonical-name | 高 | South Korea | https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070901/darkhotelappendixindicators_kl.pdf<br>https://www.securityweek.com/darkhotel-apt-uses-new-methods-target-politicians |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Zigzag Hail | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | DarkHotel | canonical-name | 高 | KR, Korea (Republic of) | https://securelist.com/blog/research/71713/darkhotels-attacks-in-2015/<br>https://blogs.technet.microsoft.com/mmpc/2016/06/09/reverse-engineering-dubnium-2<br>https://securelist.com/blog/research/66779/the-darkhotel-apt/ |
| misp-microsoft-activity-group | DUBNIUM | canonical-name | 高 |  | https://securelist.com/blog/research/71713/darkhotels-attacks-in-2015/<br>https://blogs.technet.microsoft.com/mmpc/2016/06/09/reverse-engineering-dubnium-2<br>https://blogs.technet.microsoft.com/mmpc/2016/06/20/reverse-engineering-dubniums-flash-targeting-exploit/ |
| misp-microsoft-activity-group | Zigzag Hail | canonical-name | 高 | KR | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Darkhotel - G0012 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0012<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf |
| misp-mitre-intrusion-set | Darkhotel - G0012 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0012<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf |
| misp-360net | Darkhotel - APT-C-06 | single-alias-intersection | 中 | southKorea | https://apt.360.net/report/apts/97.html<br>https://apt.360.net/report/apts/3.html |
| misp-tidal-groups | Darkhotel | canonical-name | 高 |  |  |

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

未確認

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| APT-C-06（Darkhotel）が北朝鮮関連の囮を利用して実施した最近の攻撃活動の分析 | phishing-campaign | 2026-04 | 2026-05 | 2026-08-12 |  |  | ttp--activity-rule--234a71d43cad975ee342 |  | APT-C-06（Darkhotel）は2026年4月、北朝鮮中央テレビをリアルタイム視聴するアプリの解説文書を囮に、利用者へ悪意あるアプリの導入を誘導した。 5月末には同じアプリを含む圧縮ファイルをフィッシングメールで配布し、MSIからVBScriptとPowerShellを利用する攻撃チェーンへ発展した。 第1段階MSIは2つのスケジュールタスクを作成し、tp.ps1による永続化・次段階MSIの取得と、自身の削除処理を実行する。 第2段階MSIの一部は悪意あるDLLを読み込み、ChaCha20で外部ファイルとShellcodeを復号して実行するが、最終Shellcodeの機能は未解明である。 2025年以降のDarkhotelではPowerShellがダウンロードや永続化に高頻度で使われており、今回も多数の標的が確認されたが実際のコード実行は比較的少なかった。 | 高 | `source--360-apt-c-06-darkhotel-kctv-lure-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| APT-C-06（Darkhotel）が北朝鮮関連の囮を利用して実施した最近の攻撃活動の分析 | Darkhotel | 情報なし | T1053.005 Scheduled Task | 情報なし | 情報なし | 情報なし | 高 |

Daybreak?; Fallout Team; WizardOpium

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 東アジア | MITRE ATT&CKのGroup概要でDarkhotelの標的範囲として東アジアが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | 防衛・軍事 | rkhotel](https://attack.mitre.org/groups/G0012) has also conducted spearphishing campaigns and infected victims through peer-to-peer and file sharing networks.(Citation: Kaspersky Darkhotel)(Citation: Securelist Darkhotel Aug 2015)(Citation: Microsoft Digital Defense FY20 Sept 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | 第1段階MSIは2つのスケジュールタスクを作成し、tp.ps1による永続化・次段階MSIの取得と、自身の削除処理を実行する。 |  | activity--darkhotel-kctv-lure-2026 | 2026-04 | 2026-05 | 中 | `source--360-apt-c-06-darkhotel-kctv-lure-2026` |
| Command And Control | T1001 | Data Obfuscation | 6 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/762.html |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection | T1005 | Data from Local System | 御见威胁情报中心 72 / 73 T1082 System Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https:/ |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1007 | System Service Discovery | TLP：WHITE 腾讯安全御见威胁情报中心 72 / 73 T1082 System Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protoc |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1016 | System Network Configuration Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) has collected the IP address and network adapter information from the victim’s machine.(Citation: Securelist Darkhotel Aug 2015)(Citation: Microsoft DUBNIUM July 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Uncategorized | T1024 | MITRE ATT&CK T1024 | l System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/762.html |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1027 | Obfuscated Files or Information | 0 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Darkhotel](https://attack.mitre.org/groups/G0012) has obfuscated code using RC4, XOR, and RSA.(Citation: Securelist Darkhotel Aug 2015)(Citation: Microsoft DUBNIUM July 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Uncategorized | T1035 | MITRE ATT&CK T1035 | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1036 | Masquerading | ing T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Dis |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Darkhotel](https://attack.mitre.org/groups/G0012) has used malware that is disguised as a Secure Shell (SSH) tool.(Citation: Microsoft DUBNIUM June 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1043 | Commonly Used Port | l Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/76 |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1046 | Network Service Discovery | Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection, Credential Access | T1056 | Input Capture | 107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection, Credential Access | T1056.001 | Keylogging | [Darkhotel](https://attack.mitre.org/groups/G0012) has used a keylogger.(Citation: Kaspersky Darkhotel) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1057 | Process Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) malware can collect a list of running processes on a system.(Citation: Securelist Darkhotel Aug 2015) |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-2` |
| Execution | T1059.003 | Windows Command Shell | [Darkhotel](https://attack.mitre.org/groups/G0012) has dropped an mspaint.lnk shortcut to disk which launches a shell script that downloads and executes a file.(Citation: Securelist Darkhotel Aug 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Uncategorized | T1060 | MITRE ATT&CK T1060 | T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Uncategorized | T1065 | MITRE ATT&CK T1065 | creen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/762.html |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Lateral Movement | T1080 | Taint Shared Content | [Darkhotel](https://attack.mitre.org/groups/G0012) used a virus that propagates by infecting executables stored on shared drives.(Citation: Kaspersky Darkhotel) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1082 | System Information Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) has collected the hostname, OS version, service pack version, and the processor architecture from the victim’s machine.(Citation: Securelist Darkhotel Aug 2015)(Citation: Microsoft DUBNIUM July 2016) |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-2` |
| Discovery | T1083 | File and Directory Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) has used malware that searched for files with specific patterns.(Citation: Microsoft DUBNIUM July 2016) |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-2` |
| Uncategorized | T1085 | MITRE ATT&CK T1085 | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1 |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Initial Access, Lateral Movement | T1091 | Replication Through Removable Media | [Darkhotel](https://attack.mitre.org/groups/G0012)'s selective infector modifies executables stored on removable media as a method of spreading across computers.(Citation: Kaspersky Darkhotel) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Uncategorized | T1094 | MITRE ATT&CK T1094 | n T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） https://s.tencent.com/research/report/762.html |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Uncategorized | T1099 | MITRE ATT&CK T1099 | T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Command And Control | T1105 | Ingress Tool Transfer | [Darkhotel](https://attack.mitre.org/groups/G0012) has used first-stage payloads that download additional malware from C2 servers.(Citation: Microsoft DUBNIUM June 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1106 | Native API | taryfocus.net vachel.vicp.cc 180.150.227.24 39.109.4.143 103.81.171.157 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Uncategorized | T1107 | MITRE ATT&CK T1107 | rsistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discove |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Defense Impairment, Persistence | T1112 | Modify Registry | plication Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection | T1113 | Screen Capture | Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/03/happy-new-year-wishes-from-china.ht ml 2） |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection | T1114 | Email Collection | Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考文章 1） https://malware.prevenity.com/2018/0 |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Collection | T1123 | Audio Capture | TLP：WHITE 腾讯安全御见威胁情报中心 72 / 73 T1082 System Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1124 | System Time Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) malware can obtain system time from a compromised host.(Citation: Lastline DarkHotel Just In Time Decryption Nov 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1129 | Shared Modules | 180.150.227.24 39.109.4.143 103.81.171.157 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Discovery | T1135 | Network Share Discovery | T1085 Rundll32 T1099 Timestomp Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Persistence | T1137 | Office Application Startup | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Credential Access T |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Darkhotel](https://attack.mitre.org/groups/G0012) has decrypted strings and imports using RC4 during execution.(Citation: Securelist Darkhotel Aug 2015)(Citation: Microsoft DUBNIUM July 2016) |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-2` |
| Uncategorized | T1179 | MITRE ATT&CK T1179 | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp Crede |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Initial Access | T1189 | Drive-by Compromise | [Darkhotel](https://attack.mitre.org/groups/G0012) used embedded iframes on hotel login portals to redirect selected victims to download malware.(Citation: Kaspersky Darkhotel) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Uncategorized | T1193 | MITRE ATT&CK T1193 | m www.phpvlan.com wiki.xxxx.com game.militaryfocus.net vachel.vicp.cc 180.150.227.24 39.109.4.143 103.81.171.157 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Execution | T1203 | Exploitation for Client Execution | [Darkhotel](https://attack.mitre.org/groups/G0012) has exploited Adobe Flash vulnerability CVE-2015-8651 for execution.(Citation: Microsoft DUBNIUM June 2016) |  |  | 不明 | 不明 | 高 | `source--darkhotel--ce28b9f812e95fb7`, `source--mitre-attack-19-2` |
| Execution | T1204 | User Execution | TLP：WHITE 腾讯安全御见威胁情报中心 71 / 73 T1203 Exploitation for Client Execution T1085 Rundll32 T1035 Service Execution T1204 User Execution Persistence T1179 Hooking T1137 Office Application Startup T1060 Registry Run Keys / Startup Folder Defense Evasion T1140 Deobfuscate/Decode Files or Information T1107 File Deletion T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T10 |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Execution | T1204.002 | Malicious File | [Darkhotel](https://attack.mitre.org/groups/G0012) has sent spearphishing emails in an attempt to lure users into clicking on a malicious attachments.(Citation: Securelist Darkhotel Aug 2015)(Citation: Microsoft DUBNIUM July 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | [Darkhotel](https://attack.mitre.org/groups/G0012) malware has employed just-in-time decryption of strings to evade sandbox detection.(Citation: Lastline DarkHotel Just In Time Decryption Nov 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery, Stealth | T1497.001 | System Checks | [Darkhotel](https://attack.mitre.org/groups/G0012) malware has used a series of checks to determine if it's being analyzed; checks include the length of executable names, if a filename ends with <code>.Md5.exe</code>, and if the program is executed from the root of the C:\ drive, as well as checks for sandbox-related libraries.(Citation: Lastline DarkHotel Just In Time Decryption Nov 2015)(Citation: Microsoft DUBNIUM June 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery, Stealth | T1497.002 | User Activity Based Checks | [Darkhotel](https://attack.mitre.org/groups/G0012) has used malware that repeatedly checks the mouse cursor position to determine if a real user is on the system.(Citation: Lastline DarkHotel Just In Time Decryption Nov 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1518.001 | Security Software Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) has searched for anti-malware strings and anti-virus processes running on the system.(Citation: Securelist Darkhotel Aug 2015)(Citation: Microsoft DUBNIUM June 2016)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Lateral Movement | T1534 | Internal Spearphishing | TLP：WHITE 腾讯安全御见威胁情报中心 72 / 73 T1082 System Information Discovery T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1123 Audio Capture T1005 Data from Local System T1114 Email Collection T1056 Input Capture T1113 Screen Capture Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Dat |  |  | 不明 | 不明 | 中 | `source--darkhotel--ce28b9f812e95fb7` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Darkhotel](https://attack.mitre.org/groups/G0012) has been known to establish persistence by adding programs to the Run Registry key.(Citation: Kaspersky Darkhotel) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1553.002 | Code Signing | [Darkhotel](https://attack.mitre.org/groups/G0012) has used code-signing certificates on its malware that are either forged due to weak keys or stolen. [Darkhotel](https://attack.mitre.org/groups/G0012) has also stolen certificates and signed backdoors and downloaders with them.(Citation: Kaspersky Darkhotel)(Citation: Securelist Darkhotel Aug 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Darkhotel](https://attack.mitre.org/groups/G0012) has sent spearphishing emails with malicious RAR and .LNK attachments.(Citation: Securelist Darkhotel Aug 2015)(Citation: Microsoft DUBNIUM July 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1573.001 | Symmetric Cryptography | [Darkhotel](https://attack.mitre.org/groups/G0012) has used AES-256 and 3DES for C2 communications.(Citation: Microsoft DUBNIUM July 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 101件
- IOC観測: 123件
- 複数攻撃で観測: 0件
- 要レビュー候補: 77件
- 非IOC artifact観測: 60件（`artifacts.csv`）

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
| source--360-apt-c-06-darkhotel-kctv-lure-2026 | APT-C-06（Darkhotel）近期利用朝鲜相关诱饵发起的攻击活动分析 | 360高级威胁研究院 / 360威胁情报中心 | 2026-08-12 | https://mp.weixin.qq.com/s/KrQyZ2AZn9dcL3Fqyg_y3Q | vendor-threat-research | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--darkhotel--6be8f2f16af88e57 | README |  | 不明 | Darkhotel/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--darkhotel--a8acea942272273e | README |  | 不明 | Darkhotel/higaisa/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--darkhotel--ce28b9f812e95fb7 | higaisa apt report |  | 不明 | Darkhotel/higaisa/higaisa_apt_report.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-360net | MISP 360.net suspected-victim fields | MISP Project / 360.net | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
