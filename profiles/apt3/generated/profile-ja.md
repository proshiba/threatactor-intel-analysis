# APT3 脅威アクタープロファイル

- プロファイルID: `actor--apt3`
- 状態: draft
- 更新日時: 2026-07-29T23:13:53Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

APT3の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT3**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Buckeye | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Gothic Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Pirpi | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TG-0110 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Threat Group-0110 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UPS Team | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UPS | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 5; mapping requires review. |
| Group 6 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 5; mapping requires review. |
| Boyusec – the Guangzhou Boyu Information Technology Company, Ltd | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 5; mapping requires review. |

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
| Adversary | [APT3](https://attack.mitre.org/groups/G0022) is a China-based threat group that researchers have attributed to China's Ministry of State Security.(Citation: FireEye Clandestine Wolf)(Citation: Recorded Future APT3 May 2017) This group is responsible for the campaigns known as Operation Clandestine Fox, Operation Clandestine Wolf, and Operation Double Tap.(Citation: FireEye Clandestine Wolf)(Citation: FireEye Operation Double Tap) As of June 2015, the group appears to have shifted from targeting primarily US victims to primarily political organizations in Hong Kong.(Citation: Symantec Buckeye) |
| Capability | RemoteCMD, SHOTPUT, PlugX, OSInfo, Pirpi, PlugX/Sogu, Kaba, Cookie Cutter, many 0days: IE, Firefox, and Flash, SportLoader, Shadow Brokers exploits, DoublePulsar, Bemstour, Filensfer, LaZagne, schtasks |
| Infrastructure |  |
| Victim | This threat actor targets and compromises entities in the defense, construction, technology, and transportation sectors. Up until 2015, it was primarily focused on U.S. and UK entities, but it shifted to Hong Kongâ€“based targets afterward. Aerospace and Defence; Construction and Engineering; Energy; High Tech; Nonprofit; Telecommunications; Transportation |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 3, Gothic Panda, Buckeye | canonical-name | 高 | China | https://intrusiontruth.wordpress.com/2017/05/09/apt3-is-boyusec-a-chinese-intelligence-contractor/<br>https://www.recordedfuture.com/chinese-mss-behind-apt3/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=APT+3%2C+Gothic+Panda%2C+Buckeye&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Brocade Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT3 | canonical-name | 高 | CN, China | https://www.fireeye.com/blog/threat-research/2015/06/operation-clandestine-wolf-adobe-flash-zero-day.html<br>https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong<br>https://www.cfr.org/interactive/cyber-operations/apt-3 |
| misp-microsoft-activity-group | Brocade Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | APT3 - G0022 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0022<br>https://www.fireeye.com/blog/threat-research/2015/06/operation-clandestine-wolf-adobe-flash-zero-day.html<br>https://www.recordedfuture.com/chinese-mss-behind-apt3/ |
| misp-mitre-intrusion-set | APT3 - G0022 | mitre-external-id | 高 |  | http://pwc.blogs.com/cyber_security_updates/2015/07/pirpi-scanbox.html<br>https://attack.mitre.org/groups/G0022<br>https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong |
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
| malware--remotecmd | RemoteCMD | [RemoteCMD](https://attack.mitre.org/software/S0166) is a custom tool used by [APT3](https://attack.mitre.org/groups/G0022) to execute commands on a remote system similar to SysInternal's PSEXEC functionality. (Citation: Symantec Buckeye) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--shotput | SHOTPUT | [SHOTPUT](https://attack.mitre.org/software/S0063) is a custom backdoor used by [APT3](https://attack.mitre.org/groups/G0022). (Citation: FireEye Clandestine Wolf) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--plugx | PlugX | [PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.(Citation: Lastline PlugX Analysis)(Citation: FireEye Clandestine Fox Part 2)(Citation: New DragonOK)(Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--osinfo | OSInfo | [OSInfo](https://attack.mitre.org/software/S0165) is a custom tool used by [APT3](https://attack.mitre.org/groups/G0022) to do internal discovery on a victim's computer and network. (Citation: Symantec Buckeye) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pirpi | Pirpi | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--plugx-sogu | PlugX/Sogu | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--kaba | Kaba | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cookie-cutter | Cookie Cutter | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--many-0days-ie | many 0days: IE | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--firefox | Firefox | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--and-flash | and Flash | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sportloader | SportLoader | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--shadow-brokers-exploits | Shadow Brokers exploits | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--doublepulsar | DoublePulsar | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--bemstour | Bemstour | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--filensfer | Filensfer | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--schtasks | schtasks | [schtasks](https://attack.mitre.org/software/S0111) is used to schedule execution of programs or scripts on a Windows system to run at a specific date and time. (Citation: TechNet Schtasks) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Clandestine Wolf | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Double Tap | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Clandestine Wolf | APT3 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Double Tap | APT3 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

Double Tap; Clandestine Wolf

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イタリア | 構造化OSINTの被害国フィールドでAPT3の標的・被害国としてイタリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スウェーデン | 構造化OSINTの被害国フィールドでAPT3の標的・被害国としてスウェーデンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでAPT3の標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでAPT3の標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでAPT3の標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ルクセンブルク | 構造化OSINTの被害国フィールドでAPT3の標的・被害国としてルクセンブルクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | for the campaigns known as Operation Clandestine Fox, Operation Clandestine Wolf, and Operation Double Tap.(Citation: FireEye Clandestine Wolf)(Citation: FireEye Operation Double Tap) As of June 2015, the group appears to have shifted from targeting primarily US victims to primarily political organizations in Hong Kong.(Citation: Symantec Buckeye) | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | レビュー済みアクターマッピングの標的欄に記録された英国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 香港 | MITRE ATT&CKのGroup概要でAPT3の標的国として明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | フィリピン、ベトナムで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | イタリア、スウェーデン、ベルギー、ルクセンブルク、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Energy | Targeting text indicates the Energy sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Nonprofit and Civil Society | Targeting text indicates the Nonprofit and Civil Society sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [APT3](https://attack.mitre.org/groups/G0022) has used a tool to dump credentials by injecting itself into lsass.exe and triggering with the argument "dig."(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [APT3](https://attack.mitre.org/groups/G0022) will identify Microsoft Office documents on the victim's computer.(Citation: aptsim) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | A keylogging tool used by [APT3](https://attack.mitre.org/groups/G0022) gathers network information from the victim, including the MAC address, IP address, WINS, DHCP server, and gateway.(Citation: Symantec Buckeye)(Citation: evolution of pirpi) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can detect the existence of remote systems.(Citation: Symantec Buckeye)(Citation: FireEye Clandestine Fox) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [APT3](https://attack.mitre.org/groups/G0022) enables the Remote Desktop Protocol for persistence.(Citation: aptsim) [APT3](https://attack.mitre.org/groups/G0022) has also interacted with compromised systems to browse and copy files through RDP sessions.(Citation: Twitter Cglyer Status Update APT3 eml) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [APT3](https://attack.mitre.org/groups/G0022) will copy files over to Windows Admin Shares (like ADMIN$) as part of lateral movement.(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | [APT3](https://attack.mitre.org/groups/G0022) obfuscates files or information to help evade defensive measures.(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | [APT3](https://attack.mitre.org/groups/G0022) has been known to pack their tools.(Citation: APT3 Adversary Emulation Plan)(Citation: FireEye Clandestine Wolf)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.005 | Indicator Removal from Tools | [APT3](https://attack.mitre.org/groups/G0022) has been known to remove indicators of compromise from tools.(Citation: APT3 Adversary Emulation Plan) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | An [APT3](https://attack.mitre.org/groups/G0022) downloader uses the Windows command <code>"cmd.exe" /C whoami</code> to verify that it is running with the elevated privileges of “System.”(Citation: FireEye Operation Double Tap) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.010 | Masquerade Account Name | [APT3](https://attack.mitre.org/groups/G0022) has been known to create or enable accounts, such as <code>support_388945a0</code>.(Citation: aptsim) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [APT3](https://attack.mitre.org/groups/G0022) has a tool that exfiltrates data over the C2 channel.(Citation: FireEye Clandestine Fox) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can enumerate current network connections.(Citation: Symantec Buckeye)(Citation: FireEye Clandestine Fox)(Citation: evolution of pirpi) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | An [APT3](https://attack.mitre.org/groups/G0022) downloader creates persistence by creating the following scheduled task: <code>schtasks /create /tn "mysc" /tr C:\Users\Public\test.exe /sc ONLOGON /ru "System"</code>.(Citation: FireEye Operation Double Tap) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [APT3](https://attack.mitre.org/groups/G0022) has used a keylogging tool that records keystrokes in encrypted files.(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can list out currently running processes.(Citation: FireEye Clandestine Fox)(Citation: evolution of pirpi) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [APT3](https://attack.mitre.org/groups/G0022) has used PowerShell on victim systems to download and run payloads after exploitation.(Citation: FireEye Operation Double Tap) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | An [APT3](https://attack.mitre.org/groups/G0022) downloader uses the Windows command <code>"cmd.exe" /C whoami</code>. The group also uses a tool to execute commands on remote computers.(Citation: FireEye Operation Double Tap)(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069 | Permission Groups Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can enumerate the permissions associated with Windows groups.(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can delete files.(Citation: FireEye Clandestine Fox) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [APT3](https://attack.mitre.org/groups/G0022) has been known to stage files for exfiltration in a single location.(Citation: aptsim) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [APT3](https://attack.mitre.org/groups/G0022) leverages valid accounts after gaining credentials for use within the victim domain.(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can obtain information about the local system.(Citation: Symantec Buckeye)(Citation: evolution of pirpi) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that looks for files and directories on the local file system.(Citation: FireEye Clandestine Fox)(Citation: evolution of pirpi) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | [APT3](https://attack.mitre.org/groups/G0022) has used a tool that can obtain info about local and global group users, power users, and administrators.(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.002 | External Proxy | An [APT3](https://attack.mitre.org/groups/G0022) downloader establishes SOCKS5 connections for its initial C2.(Citation: FireEye Operation Double Tap) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1095 | Non-Application Layer Protocol | An [APT3](https://attack.mitre.org/groups/G0022) downloader establishes SOCKS5 connections for its initial C2.(Citation: FireEye Operation Double Tap) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.007 | Additional Local or Domain Groups | [APT3](https://attack.mitre.org/groups/G0022) has been known to add created accounts to local admin groups to maintain elevated access.(Citation: aptsim) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1104 | Multi-Stage Channels | An [APT3](https://attack.mitre.org/groups/G0022) downloader first establishes a SOCKS5 connection to 192.157.198[.]103 using TCP port 1913; once the server response is verified, it then requests a connection to 192.184.60[.]229 on TCP port 81.(Citation: FireEye Operation Double Tap) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can copy files to remote machines.(Citation: FireEye Clandestine Fox) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.002 | Password Cracking | [APT3](https://attack.mitre.org/groups/G0022) has been known to brute force password hashes to be able to leverage plain text credentials.(Citation: APT3 Adversary Emulation Plan) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.001 | Local Account | [APT3](https://attack.mitre.org/groups/G0022) has been known to create or enable accounts, such as <code>support_388945a0</code>.(Citation: aptsim) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [APT3](https://attack.mitre.org/groups/G0022) has exploited the Adobe Flash Player vulnerability CVE-2015-3113 and Internet Explorer vulnerability CVE-2014-1776.(Citation: FireEye Clandestine Wolf)(Citation: FireEye Clandestine Fox) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [APT3](https://attack.mitre.org/groups/G0022) has lured victims into clicking malicious links delivered through spearphishing.(Citation: FireEye Clandestine Wolf) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can run DLLs.(Citation: FireEye Clandestine Fox) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [APT3](https://attack.mitre.org/groups/G0022) has a tool that creates a new service for persistence.(Citation: FireEye Operation Double Tap) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.008 | Accessibility Features | [APT3](https://attack.mitre.org/groups/G0022) replaces the Sticky Keys binary <code>C:\Windows\System32\sethc.exe</code> for persistence.(Citation: aptsim) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [APT3](https://attack.mitre.org/groups/G0022) places scripts in the startup folder for persistence.(Citation: FireEye Operation Double Tap) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can locate credentials in files on the file system such as those from Firefox or Chrome.(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [APT3](https://attack.mitre.org/groups/G0022) has used tools to dump passwords from browsers.(Citation: Symantec Buckeye) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [APT3](https://attack.mitre.org/groups/G0022) has used tools to compress data before exfilling it.(Citation: aptsim) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.003 | Hidden Window | [APT3](https://attack.mitre.org/groups/G0022) has been known to use <code>-WindowStyle Hidden</code> to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows.(Citation: FireEye Operation Double Tap) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [APT3](https://attack.mitre.org/groups/G0022) has sent spearphishing emails containing malicious links.(Citation: FireEye Clandestine Wolf) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [APT3](https://attack.mitre.org/groups/G0022) has been known to side load DLLs with a valid version of Chrome with one of their tools.(Citation: FireEye Clandestine Fox)(Citation: FireEye Clandestine Fox Part 2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

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
| source--apt3--ff658cd42d6da71c | README |  | 不明 | APT3/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
