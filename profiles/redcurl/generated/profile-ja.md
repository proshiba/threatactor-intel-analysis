# RedCurl 脅威アクタープロファイル

- プロファイルID: `actor--redcurl`
- 状態: draft
- 更新日時: 2026-07-29T15:36:11Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

RedCurlの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **RedCurl**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

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
| Adversary | [RedCurl](https://attack.mitre.org/groups/G1039) is a threat actor active since 2018 notable for corporate espionage targeting a variety of locations, including Ukraine, Canada and the United Kingdom, and a variety of industries, including but not limited to travel agencies, insurance companies, and banks.(Citation: group-ib_redcurl1) [RedCurl](https://attack.mitre.org/groups/G1039) is allegedly a Russian-speaking threat actor.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) The group’s operations typically start with spearphishing emails to gain initial access, then the group executes discovery and collection commands and scripts to find corporate data. The group concludes operations by exfiltrating files to the C2 servers.  |
| Capability | Powershell scripts |
| Infrastructure |  |
| Victim | Russia, ukraine, Canada, Germany, the united Kingdom, norway, mainly targeting sectors: construction companies, financial and consulting companies, retailers, banks, insurance companies, law firms, travel agencies |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | RedCurl | canonical-name | 高 |  | https://www.zdnet.com/article/redcurl-cybercrime-group-has-hacked-companies-for-three-years/<br>https://www.group-ib.com/resources/threat-research/red-curl.html<br>https://www.esentire.com/blog/unraveling-the-many-stages-and-techniques-used-by-redcurl-earthkapre-apt |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Earth Kapre | canonical-name | 高 |  | https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html<br>https://news.sophos.com/en-us/2025/12/05/sharpening-the-knife-gold-blades-strategic-evolution/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | RedCurl - G1039 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1039<br>https://www.group-ib.com/resources/research-hub/red-curl-2/<br>https://www.group-ib.com/resources/research-hub/red-curl/ |
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
| malware--powershell-scripts | Powershell scripts | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RedCurlサイバー犯罪グループがWindows PCAツールを悪用して企業スパイ活動を行う | phishing-campaign | 不明 | 不明 | 2024-03-15 |  |  | ttp--activity-rule--ad60b8f605df3c8bd2b8 |  | RedCurlは正規のMicrosoft WindowsコンポーネントであるPCAを悪用 PCAを使って悪意のあるコマンドを実行し、セキュリティ制約を回避 攻撃チェーンにはフィッシングメールと偽の添付ファイルが含まれる Trend Microが詳細な攻撃手法を分析し、報告 RedCurlは複数国の企業を対象にスパイ活動を行っている | 高 | `source--daily-970254fe18c304ec58c0` |
| サイバー諜報グループ「Earth Kapre（別称：RedCurl）」の手口を解明：トレンドマイクロMDRによる分析と脅威インテリジェンスの活用 | cyber-espionage | 不明 | 不明 | 2024-04-03 |  |  |  |  | サイバー諜報グループ「Earth Kapre（別称：RedCurl）」の手口を解明：トレンドマイクロMDRによる分析と脅威インテリジェンスの活用 | 高 | `source--daily-a7ead7d250e5387d2fd8` |
| RedCurlサイバースパイ集団、Hyper-Vサーバーを暗号化するランサムウェアを作成 | ransomware-extortion | 不明 | 不明 | 2025-03-27 |  |  | ttp--activity-rule--3e969aed36a08f427741, ttp--activity-rule--5bf50c6515823fde06e4 | victim--activity-rule--561b836975c65a2b65fd | RedCurlは2018年から企業スパイ活動を行っている脅威アクターで、最近Hyper-V仮想マシンを標的とするランサムウェア「QWCrypt」を使用開始。 攻撃は、履歴書に見せかけた.IMGファイルを含むフィッシングメールから始まり、Windowsが自動的にマウントする。 マウントされたドライブ内のLNKファイルを実行すると、PowerShellスクリプトが起動し、Cobalt Strikeビーコンをダウンロードして攻撃者にリモートアクセスを提供。 攻撃者はネットワーク内を横展開し、最終的にQWCryptランサムウェアを展開してHyper-V仮想マシンを暗号化。 RedCurlは以前はデータ窃取に焦点を当てていたが、今回初めてランサムウェアを使用した。 二重脅迫のための専用リークサイトがないことから、RedCurlがランサムウェアを偽旗として使用しているのか、真の金銭目的の攻撃なのか疑問が提起されている。 | 高 | `source--daily-7ebbf6fb62e219c36773` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Canada | Targeting text mentions canada. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| countries | Germany | Targeting text mentions germany. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Norway | Targeting text mentions norway. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Russia | Targeting text mentions russia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Ukraine | Targeting text mentions ukraine. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| countries | United Kingdom | Targeting text mentions united kingdom. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | 金融 | //attack.mitre.org/groups/G1039) is a threat actor active since 2018 notable for corporate espionage targeting a variety of locations, including Ukraine, Canada and the United Kingdom, and a variety of industries, including but not limited to travel agencies, insurance companies, and banks.(Citation: group-ib_redcurl1) [RedCurl](https://attack.mitre.org/groups/G1039) is allegedly a Russian-speaking threat actor.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) The group’s operations typically start with spearphishing emails to gain initial access, then the group executes discovery and | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Finance | Targeting text indicates the Finance sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Retail and Hospitality | Targeting text indicates the Retail and Hospitality sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: RedCurlサイバースパイ集団、Hyper-Vサーバーを暗号化するランサムウェアを作成 | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--activity-rule--3e969aed36a08f427741, ttp--activity-rule--5bf50c6515823fde06e4 | メール／メールアカウント, VPN／リモートアクセス機器, サーバー | data-theft: RedCurlは以前はデータ窃取に焦点を当てていたが、今回初めてランサムウェアを使用した。<br>encryption: RedCurlサイバースパイ集団、Hyper-Vサーバーを暗号化するランサムウェアを作成<br>espionage: RedCurlは2018年から企業スパイ活動を行っている脅威アクターで、最近Hyper-V仮想マシンを標的とするランサムウェア「QWCrypt」を使用開始。 | 不明 | 不明 | 2025-03-27 | 高 | `source--daily-7ebbf6fb62e219c36773` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.001 | PowerShell | マウントされたドライブ内のLNKファイルを実行すると、PowerShellスクリプトが起動し、Cobalt Strikeビーコンをダウンロードして攻撃者にリモートアクセスを提供。 |  | activity--daily-d3e416b7f22a06f08992 | 不明 | 不明 | 中 | `source--daily-7ebbf6fb62e219c36773` |
| Impact | T1486 | Data Encrypted for Impact | 攻撃者はネットワーク内を横展開し、最終的にQWCryptランサムウェアを展開してHyper-V仮想マシンを暗号化。 |  | activity--daily-d3e416b7f22a06f08992 | 不明 | 不明 | 中 | `source--daily-7ebbf6fb62e219c36773` |
| Initial Access | T1566.001 | Spearphishing Attachment | RedCurlは正規のMicrosoft WindowsコンポーネントであるPCAを悪用 PCAを使って悪意のあるコマンドを実行し、セキュリティ制約を回避 攻撃チェーンにはフィッシングメールと偽の添付ファイルが含まれる Trend Microが詳細な攻撃手法を分析し、報告 RedCurlは複数国の企業を対象にスパイ活動を行っている |  | activity--daily-82ea374adca530ce5578 | 不明 | 不明 | 中 | `source--daily-970254fe18c304ec58c0` |
| Credential Access | T1003.001 | LSASS Memory | [RedCurl](https://attack.mitre.org/groups/G1039) used [LaZagne](https://attack.mitre.org/software/S0349) to obtain passwords from memory.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [RedCurl](https://attack.mitre.org/groups/G1039) has collected data from the local disk of compromised hosts.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1020 | Automated Exfiltration | [RedCurl](https://attack.mitre.org/groups/G1039) has used batch scripts to exfiltrate data.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | [RedCurl](https://attack.mitre.org/groups/G1039) has used malware with string encryption.(Citation: therecord_redcurl) [RedCurl](https://attack.mitre.org/groups/G1039) has also encrypted data and has encoded PowerShell commands using Base64.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) [RedCurl](https://attack.mitre.org/groups/G1039) has used `PyArmor` to obfuscate code execution of [LaZagne](https://attack.mitre.org/software/S0349). (Citation: group-ib_redcurl1) Additionally, [RedCurl](https://attack.mitre.org/groups/G1039) has obfuscated downloaded files by renaming them as commonly used tools and has used `echo`, instead of file names themselves, to execute files.(Citation: trendmicro_redcurl) <br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [RedCurl](https://attack.mitre.org/groups/G1039) mimicked legitimate file names and scheduled tasks, e.g. ` MicrosoftCurrentupdatesCheck` and<br>`MdMMaintenenceTask` to mask malicious files and scheduled tasks.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1039 | Data from Network Shared Drive | [RedCurl](https://attack.mitre.org/groups/G1039) has collected data about network drives.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [RedCurl](https://attack.mitre.org/groups/G1039) has used netstat to check if port 4119 is open.(Citation: trendmicro_redcurl)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [RedCurl](https://attack.mitre.org/groups/G1039) has created scheduled tasks for persistence.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)(Citation: trendmicro_redcurl) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.002 | GUI Input Capture | [RedCurl](https://attack.mitre.org/groups/G1039) prompts the user for credentials through a Microsoft Outlook pop-up.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [RedCurl](https://attack.mitre.org/groups/G1039) has used PowerShell to execute commands and to download malware.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)(Citation: trendmicro_redcurl) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [RedCurl](https://attack.mitre.org/groups/G1039) has used the Windows Command Prompt to execute commands.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)(Citation: trendmicro_redcurl) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [RedCurl](https://attack.mitre.org/groups/G1039) has used VBScript to run malicious files.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | [RedCurl](https://attack.mitre.org/groups/G1039) has used a Python script to establish outbound communication and to execute commands using SMB port 445.(Citation: trendmicro_redcurl)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [RedCurl](https://attack.mitre.org/groups/G1039) has deleted files after execution.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)(Citation: trendmicro_redcurl) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [RedCurl](https://attack.mitre.org/groups/G1039) has used HTTP, HTTPS and Webdav protocls for C2 communications.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1080 | Taint Shared Content | [RedCurl](https://attack.mitre.org/groups/G1039) has placed modified LNK files on network drives for lateral movement.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [RedCurl](https://attack.mitre.org/groups/G1039) has collected information about the target system, such as system information and list of network connections.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [RedCurl](https://attack.mitre.org/groups/G1039) has searched for and collected files on local and network drives.(Citation: therecord_redcurl)(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | [RedCurl](https://attack.mitre.org/groups/G1039) has collected information about local accounts.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [RedCurl](https://attack.mitre.org/groups/G1039) has collected information about domain accounts using SysInternal’s AdExplorer functionality   .(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.003 | Email Account | [RedCurl](https://attack.mitre.org/groups/G1039) has collected information about email accounts.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | [RedCurl](https://attack.mitre.org/groups/G1039) has used web services to download malicious files.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.001 | Local Email Collection | [RedCurl](https://attack.mitre.org/groups/G1039) has collected emails to use in future phishing campaigns.(Citation: group-ib_redcurl1) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [RedCurl](https://attack.mitre.org/groups/G1039) has used batch scripts to collect data.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | [RedCurl](https://attack.mitre.org/groups/G1039) has gained access to a contractor to pivot to the victim’s infrastructure.(Citation: therecord_redcurl) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1202 | Indirect Command Execution | [RedCurl](https://attack.mitre.org/groups/G1039) has used pcalua.exe to obfuscate binary execution and remote connections.(Citation: trendmicro_redcurl)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [RedCurl](https://attack.mitre.org/groups/G1039) has used malicious links to infect the victim machines.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [RedCurl](https://attack.mitre.org/groups/G1039) has used malicious files to infect the victim machines.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)(Citation: trendmicro_redcurl)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [RedCurl](https://attack.mitre.org/groups/G1039) has used rundll32.exe to execute malicious files.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)(Citation: trendmicro_redcurl)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1537 | Transfer Data to Cloud Account | [RedCurl](https://attack.mitre.org/groups/G1039) has used cloud storage to exfiltrate data, in particular the megatools utilities were used to exfiltrate data to Mega, a file storage service.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [RedCurl](https://attack.mitre.org/groups/G1039) has established persistence by creating entries in `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [RedCurl](https://attack.mitre.org/groups/G1039) used [LaZagne](https://attack.mitre.org/software/S0349) to obtain passwords in files.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.002 | Credentials in Registry | [RedCurl](https://attack.mitre.org/groups/G1039) used [LaZagne](https://attack.mitre.org/software/S0349) to obtain passwords in the Registry.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2)      |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [RedCurl](https://attack.mitre.org/groups/G1039) used [LaZagne](https://attack.mitre.org/software/S0349) to obtain passwords from web browsers.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [RedCurl](https://attack.mitre.org/groups/G1039) has downloaded 7-Zip to decompress password protected archives.(Citation: trendmicro_redcurl)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | [RedCurl](https://attack.mitre.org/groups/G1039) added the “hidden” file attribute to original files, manipulating victims to click on malicious LNK files.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [RedCurl](https://attack.mitre.org/groups/G1039) has used phishing emails with malicious files to gain initial access.(Citation: group-ib_redcurl1)(Citation: trendmicro_redcurl)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [RedCurl](https://attack.mitre.org/groups/G1039) has used phishing emails with malicious links to gain initial access.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | [RedCurl](https://attack.mitre.org/groups/G1039) has used AES-128 CBC to encrypt C2 communications.(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.002 | Asymmetric Cryptography | [RedCurl](https://attack.mitre.org/groups/G1039) has used HTTPS for C2 communication.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [RedCurl](https://attack.mitre.org/groups/G1039) has created its own tools to use during operations.(Citation: therecord_redcurl) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 2件（`artifacts.csv`）

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
| source--daily-7ebbf6fb62e219c36773 | RedCurlサイバースパイ集団、Hyper-Vサーバーを暗号化するランサムウェアを作成 | bleepingcomputer.com | 2025-03-27 | https://www.bleepingcomputer.com/news/security/redcurl-cyberspies-create-ransomware-to-encrypt-hyper-v-servers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-970254fe18c304ec58c0 | RedCurlサイバー犯罪グループがWindows PCAツールを悪用して企業スパイ活動を行う | thehackernews.com | 2024-03-15 | https://thehackernews.com/2024/03/redcurl-cybercrime-group-abuses-windows.html | osint-report | TLP:CLEAR | 中 |
| source--daily-a7ead7d250e5387d2fd8 | サイバー諜報グループ「Earth Kapre（別称：RedCurl）」の手口を解明：トレンドマイクロMDRによる分析と脅威インテリジェンスの活用 | trendmicro.com | 2024-04-03 | https://www.trendmicro.com/ja_jp/research/24/d/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--redcurl--78aa91b6349af791 | redcurl |  | 不明 | actor_profile/evidence/redcurl.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
