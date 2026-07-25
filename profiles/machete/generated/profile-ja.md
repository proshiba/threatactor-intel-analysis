# Machete 脅威アクタープロファイル

プロファイルID: `actor--machete`  
状態: draft  
更新日時: 2026-07-25T14:07:08Z  
構造バージョン: 1.0.0

## エグゼクティブサマリー

Macheteの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Machete**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT-C-43 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| El Machete | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Ragua | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 5; mapping requires review. |

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
| Adversary | [Machete](https://attack.mitre.org/groups/G0095) is a suspected Spanish-speaking cyber espionage group that has been active since at least 2010. It has primarily focused its operations within Latin America, with a particular emphasis on Venezuela, but also in the US, Europe, Russia, and parts of Asia. [Machete](https://attack.mitre.org/groups/G0095) generally targets high-profile organizations such as government institutions, intelligence services, and military units, as well as telecommunications and power companies.(Citation: Cylance Machete Mar 2017)(Citation: Securelist Machete Aug 2014)(Citation: ESET Machete July 2019)(Citation: 360 Machete Sep 2020) |
| Capability | Machete |
| Infrastructure |  |
| Victim | This threat actor targets military, government entities, and telecommunications providers, primarily in Latin America, for the purpose of espionage. |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | El Machete | multiple-name-intersection | 高 |  | https://securelist.com/el-machete/66108/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=El+Machete&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | El Machete | canonical-name | 高 | Unknown | https://attack.mitre.org/groups/G0095/<br>https://securelist.com/el-machete/66108/<br>https://www.cylance.com/en_us/blog/el-machete-malware-attacks-cut-through-latam.html |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Machete - G0095 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0095<br>https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/<br>https://securelist.com/el-machete/66108/ |
| misp-360net | Machete - APT-C-43 | canonical-name | 高 | namerica | https://apt.360.net/report/apts/159.html |

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
| malware--machete | Machete | [Machete](https://attack.mitre.org/software/S0409) is a cyber espionage toolset used by [Machete](https://attack.mitre.org/groups/G0095). It is a Python-based backdoor targeting Windows machines that was first observed in 2010.(Citation: ESET Machete July 2019)(Citation: Securelist Machete Aug 2014)(Citation: 360 Machete Sep 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Uncategorized | T1002 | MITRE ATT&CK T1002 | l FTP and HTTP are used for Command & Control. Exfiltration T1020 Automated Exfiltration All collected files are exfiltrated automatically to remote servers. T1002 Data Compressed Machete compresses browser’s profile data as .zip files prior to exfiltrating it. T1022 Data Encrypted Collected data is encrypted with AES before transmitting it. In some versions of the malware, it is encoded with base64 (but not encrypted). T1041 Exfiltrat |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Collection | T1005 | Data from Local System | zuelan military under attack 35 Collection T1115 Clipboard Data Clipboard data is stolen by creating an overlapped window that will listen to keyboard events. T1005 Data from Local System File system is searched for files of interest. T1025 Data from Removable Media Files are copied from newly inserted drives. T1056 Input Capture Machete logs keystrokes from the victim’s machine. T1113 Screen Capture Machete captures screenshots. T1074 Dat |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Command And Control | T1008 | Fallback Channels | and logs are stored in a temporary folder, encrypted. Command and Control T1043 Commonly Used Port Standard FTP and HTTP ports are used for communications. T1008 Fallback Channels Machete uses HTTP to exfiltrate documents if FTP is unavailable. T1105 Remote File Copy Machete can download additional files for execution on the victim’s machine. T1071 Standard Application Layer Protocol FTP and HTTP are used for Command & Control. Exfi |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Discovery | T1010 | Application Window Discovery | running processes are enumerated searching for browsers. T1217 Browser Bookmark Discovery Browser data such as bookmarks is gathered for several browsers. T1010 Application Window Discovery Window names are reported along with keylogger information. |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Exfiltration | T1020 | Automated Exfiltration | additional files for execution on the victim’s machine. T1071 Standard Application Layer Protocol FTP and HTTP are used for Command & Control. Exfiltration T1020 Automated Exfiltration All collected files are exfiltrated automatically to remote servers. T1002 Data Compressed Machete compresses browser’s profile data as .zip files prior to exfiltrating it. T1022 Data Encrypted Collected data is encrypted with AES before transmitting i |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Uncategorized | T1022 | MITRE ATT&CK T1022 | les are exfiltrated automatically to remote servers. T1002 Data Compressed Machete compresses browser’s profile data as .zip files prior to exfiltrating it. T1022 Data Encrypted Collected data is encrypted with AES before transmitting it. In some versions of the malware, it is encoded with base64 (but not encrypted). T1041 Exfiltration Over Command and Control Channel Data is exfiltrated over the same channel used for C&C. T1052 Exfi |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Collection | T1025 | Data from Removable Media | ta is stolen by creating an overlapped window that will listen to keyboard events. T1005 Data from Local System File system is searched for files of interest. T1025 Data from Removable Media Files are copied from newly inserted drives. T1056 Input Capture Machete logs keystrokes from the victim’s machine. T1113 Screen Capture Machete captures screenshots. T1074 Data Staged Files and logs are stored in a temporary folder, encrypted. Command |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Stealth | T1027 | Obfuscated Files or Information | ectories Malware files and folders are hidden for persistence. T1053 Scheduled Task All of the components are scheduled to ensure persistence. Defense Evasion T1027 Obfuscated Files or Information Python scripts are obfuscated. T1045 Software Packing Machete payload is delivered as self-extracting files. Machete downloaders are UPX packed. T1036 Masquerading File and task names try to impersonate Google Chrome, Java, Dropbox, Adobe Reade |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Exfiltration | T1029 | Scheduled Transfer | 1052 Exfiltration Over Physical Medium Data from all drives in a compromised system is copied to a removable drive if there is a special file in that drive. T1029 Scheduled Transfer Data is sent to the C&C server every 10 minutes. |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Stealth | T1036 | Masquerading | Information Python scripts are obfuscated. T1045 Software Packing Machete payload is delivered as self-extracting files. Machete downloaders are UPX packed. T1036 Masquerading File and task names try to impersonate Google Chrome, Java, Dropbox, Adobe Reader and Python executables. Credential Access T1145 Private Keys A compromised system is scanned looking for key and certificate file extensions. T1081 Credentials in Files Machete exf |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | Data Encrypted Collected data is encrypted with AES before transmitting it. In some versions of the malware, it is encoded with base64 (but not encrypted). T1041 Exfiltration Over Command and Control Channel Data is exfiltrated over the same channel used for C&C. T1052 Exfiltration Over Physical Medium Data from all drives in a compromised system is copied to a removable drive if there is a special file in that drive. T1029 Schedule |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Command And Control | T1043 | Commonly Used Port | machine. T1113 Screen Capture Machete captures screenshots. T1074 Data Staged Files and logs are stored in a temporary folder, encrypted. Command and Control T1043 Commonly Used Port Standard FTP and HTTP ports are used for communications. T1008 Fallback Channels Machete uses HTTP to exfiltrate documents if FTP is unavailable. T1105 Remote File Copy Machete can download additional files for execution on the victim’s machine. T1071 St |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Uncategorized | T1045 | MITRE ATT&CK T1045 | cheduled Task All of the components are scheduled to ensure persistence. Defense Evasion T1027 Obfuscated Files or Information Python scripts are obfuscated. T1045 Software Packing Machete payload is delivered as self-extracting files. Machete downloaders are UPX packed. T1036 Masquerading File and task names try to impersonate Google Chrome, Java, Dropbox, Adobe Reader and Python executables. Credential Access T1145 Private Keys A comp |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Discovery | T1049 | System Network Connections Discovery | oking for key and certificate file extensions. T1081 Credentials in Files Machete exfiltrates files with stored credentials for several browsers. Discovery T1049 System Network Connections Discovery Netsh command is used to list all nearby Wi-Fi networks. T1120 Peripheral Device Discovery Newly inserted devices are detected by listening for the WM_DEVICECHANGE window message. T1083 File and Directory Discovery File listings are prod |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Exfiltration | T1052 | Exfiltration Over Physical Medium | it is encoded with base64 (but not encrypted). T1041 Exfiltration Over Command and Control Channel Data is exfiltrated over the same channel used for C&C. T1052 Exfiltration Over Physical Medium Data from all drives in a compromised system is copied to a removable drive if there is a special file in that drive. T1029 Scheduled Transfer Data is sent to the C&C server every 10 minutes. |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Execution, Persistence, Privilege Escalation | T1053 | Scheduled Task/Job | ile with malicious contents. Execution T1204 User Execution Tries to get users to open links or attachments that will execute the first component of Machete. T1053 Scheduled Task Other components of Machete are executed by Windows Task Scheduler. Persistence T1158 Hidden Files and Directories Malware files and folders are hidden for persistence. T1053 Scheduled Task All of the components are scheduled to ensure persistence. Defense Eva |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056 | Input Capture | ents. T1005 Data from Local System File system is searched for files of interest. T1025 Data from Removable Media Files are copied from newly inserted drives. T1056 Input Capture Machete logs keystrokes from the victim’s machine. T1113 Screen Capture Machete captures screenshots. T1074 Data Staged Files and logs are stored in a temporary folder, encrypted. Command and Control T1043 Commonly Used Port Standard FTP and HTTP ports are used |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Discovery | T1057 | Process Discovery | are detected by listening for the WM_DEVICECHANGE window message. T1083 File and Directory Discovery File listings are produced for files to be exfiltrated. T1057 Process Discovery In the latest version, running processes are enumerated searching for browsers. T1217 Browser Bookmark Discovery Browser data such as bookmarks is gathered for several browsers. T1010 Application Window Discovery Window names are reported along with keylog |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | ses HTTP to exfiltrate documents if FTP is unavailable. T1105 Remote File Copy Machete can download additional files for execution on the victim’s machine. T1071 Standard Application Layer Protocol FTP and HTTP are used for Command & Control. Exfiltration T1020 Automated Exfiltration All collected files are exfiltrated automatically to remote servers. T1002 Data Compressed Machete compresses browser’s profile data as .zip files prior |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Collection | T1074 | Data Staged | re copied from newly inserted drives. T1056 Input Capture Machete logs keystrokes from the victim’s machine. T1113 Screen Capture Machete captures screenshots. T1074 Data Staged Files and logs are stored in a temporary folder, encrypted. Command and Control T1043 Commonly Used Port Standard FTP and HTTP ports are used for communications. T1008 Fallback Channels Machete uses HTTP to exfiltrate documents if FTP is unavailable. T1105 Remot |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Uncategorized | T1081 | MITRE ATT&CK T1081 | , Adobe Reader and Python executables. Credential Access T1145 Private Keys A compromised system is scanned looking for key and certificate file extensions. T1081 Credentials in Files Machete exfiltrates files with stored credentials for several browsers. Discovery T1049 System Network Connections Discovery Netsh command is used to list all nearby Wi-Fi networks. T1120 Peripheral Device Discovery Newly inserted devices are detected by |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Discovery | T1083 | File and Directory Discovery | o list all nearby Wi-Fi networks. T1120 Peripheral Device Discovery Newly inserted devices are detected by listening for the WM_DEVICECHANGE window message. T1083 File and Directory Discovery File listings are produced for files to be exfiltrated. T1057 Process Discovery In the latest version, running processes are enumerated searching for browsers. T1217 Browser Bookmark Discovery Browser data such as bookmarks is gathered for sever |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Command And Control | T1105 | Ingress Tool Transfer | Used Port Standard FTP and HTTP ports are used for communications. T1008 Fallback Channels Machete uses HTTP to exfiltrate documents if FTP is unavailable. T1105 Remote File Copy Machete can download additional files for execution on the victim’s machine. T1071 Standard Application Layer Protocol FTP and HTTP are used for Command & Control. Exfiltration T1020 Automated Exfiltration All collected files are exfiltrated automatically t |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Collection | T1113 | Screen Capture | interest. T1025 Data from Removable Media Files are copied from newly inserted drives. T1056 Input Capture Machete logs keystrokes from the victim’s machine. T1113 Screen Capture Machete captures screenshots. T1074 Data Staged Files and logs are stored in a temporary folder, encrypted. Command and Control T1043 Commonly Used Port Standard FTP and HTTP ports are used for communications. T1008 Fallback Channels Machete uses HTTP to exfilt |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Collection | T1115 | Clipboard Data | Machete just got sharper Venezuelan military under attack 35 Collection T1115 Clipboard Data Clipboard data is stolen by creating an overlapped window that will listen to keyboard events. T1005 Data from Local System File system is searched for files of interest. T1025 Data from Removable Media Files are copied from newly inserted drives. T1056 Input Ca |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Discovery | T1120 | Peripheral Device Discovery | with stored credentials for several browsers. Discovery T1049 System Network Connections Discovery Netsh command is used to list all nearby Wi-Fi networks. T1120 Peripheral Device Discovery Newly inserted devices are detected by listening for the WM_DEVICECHANGE window message. T1083 File and Directory Discovery File listings are produced for files to be exfiltrated. T1057 Process Discovery In the latest version, running processes ar |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Uncategorized | T1145 | MITRE ATT&CK T1145 | re UPX packed. T1036 Masquerading File and task names try to impersonate Google Chrome, Java, Dropbox, Adobe Reader and Python executables. Credential Access T1145 Private Keys A compromised system is scanned looking for key and certificate file extensions. T1081 Credentials in Files Machete exfiltrates files with stored credentials for several browsers. Discovery T1049 System Network Connections Discovery Netsh command is used to lis |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Uncategorized | T1158 | MITRE ATT&CK T1158 | ents that will execute the first component of Machete. T1053 Scheduled Task Other components of Machete are executed by Windows Task Scheduler. Persistence T1158 Hidden Files and Directories Malware files and folders are hidden for persistence. T1053 Scheduled Task All of the components are scheduled to ensure persistence. Defense Evasion T1027 Obfuscated Files or Information Python scripts are obfuscated. T1045 Software Packing Mache |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1192 | MITRE ATT&CK T1192 | ]63 • 156.67.222[.]88 • 158.69.9[.]209 • 142.44.236[.]215 • 199.79.63[.]188 • 109.61.164[.]33 MITRE ATT&CK techniques Tactic ID Name Description Initial Access T1192 Spearphishing Link Emails contain a link to download a compressed file from an external server. T1193 Spearphishing Attachment Emails contain a zipped file with malicious contents. Execution T1204 User Execution Tries to get users to open links or attachments that will exec |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Uncategorized | T1193 | MITRE ATT&CK T1193 | CK techniques Tactic ID Name Description Initial Access T1192 Spearphishing Link Emails contain a link to download a compressed file from an external server. T1193 Spearphishing Attachment Emails contain a zipped file with malicious contents. Execution T1204 User Execution Tries to get users to open links or attachments that will execute the first component of Machete. T1053 Scheduled Task Other components of Machete are executed by W |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Execution | T1204 | User Execution | a link to download a compressed file from an external server. T1193 Spearphishing Attachment Emails contain a zipped file with malicious contents. Execution T1204 User Execution Tries to get users to open links or attachments that will execute the first component of Machete. T1053 Scheduled Task Other components of Machete are executed by Windows Task Scheduler. Persistence T1158 Hidden Files and Directories Malware files and folders |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | ile listings are produced for files to be exfiltrated. T1057 Process Discovery In the latest version, running processes are enumerated searching for browsers. T1217 Browser Bookmark Discovery Browser data such as bookmarks is gathered for several browsers. T1010 Application Window Discovery Window names are reported along with keylogger information. |  |  | 不明 | 不明 | 中 | `source--machete--b272c7c9a01c76d8` |
| Stealth | T1218.007 | Msiexec | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 112件
- IOC観測: 125件
- 複数攻撃で観測: 0件
- 要レビュー候補: 68件
- 非IOC artifact観測: 88件（`artifacts.csv`）

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
| source--machete--b272c7c9a01c76d8 | ESET Machete |  | 不明 | Machete/ESET_Machete.pdf | report | TLP:CLEAR | 中 |
| source--machete--901ef02127d07093 | README |  | 不明 | Machete/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
