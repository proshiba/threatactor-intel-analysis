# BlackTech 脅威アクタープロファイル

- プロファイルID: `actor--blacktech`
- 状態: draft
- 更新日時: 2026-07-27T11:04:30Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

BlackTechの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **BlackTech**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Palmerworm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Phantom of Routers | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Unknown row 27; mapping requires review. |
| G0098 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Unknown row 27; mapping requires review. |

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
| Adversary | [BlackTech](https://attack.mitre.org/groups/G0098) is a suspected Chinese cyber espionage group that has primarily targeted organizations in East Asia--particularly Taiwan, Japan, and Hong Kong--and the US since at least 2013. [BlackTech](https://attack.mitre.org/groups/G0098) has used a combination of custom malware, dual-use tools, and living off the land tactics to compromise media, construction, engineering, electronics, and financial company networks.(Citation: TrendMicro BlackTech June 2017)(Citation: Symantec Palmerworm Sep 2020)(Citation: Reuters Taiwan BlackTech August 2020) |
| Capability | Flagpro, TSCookie, Kivars, PLEAD, Waterbear, BendyBear, PsExec |
| Infrastructure |  |
| Victim | targets in East Asia, particularly Taiwan, and occasionally, Japan and Hong Kong |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | BlackTech, Circuit Panda, Radio Panda | canonical-name | 高 | China | https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/<br>https://www.trendmicro.com/en_us/research/24/d/earth-hundun-waterbear-deuterbear.html<br>https://www.trendmicro.com/en_us/research/24/e/earth-hundun-2.html |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Canary Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | BlackTech | canonical-name | 高 | CN | https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/<br>https://www.welivesecurity.com/2018/07/09/certificates-stolen-taiwanese-tech-companies-plead-malware-campaign/<br>https://www.welivesecurity.com/2019/05/14/plead-malware-mitm-asus-webstorage/ |
| misp-microsoft-activity-group | Canary Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | BlackTech - G0098 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0098<br>https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/<br>https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/palmerworm-blacktech-espionage-apt |
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
| malware--bendybear | BendyBear | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--flagpro | Flagpro | [Flagpro](https://attack.mitre.org/software/S0696) is a Windows-based, first-stage downloader that has been used by [BlackTech](https://attack.mitre.org/groups/G0098) since at least October 2020. It has primarily been used against defense, media, and communications companies in Japan.(Citation: NTT Security Flagpro new December 2021)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--kivars | Kivars | [Kivars](https://attack.mitre.org/software/S0437) is a modular remote access tool (RAT), derived from the Bifrost RAT, that was used by [BlackTech](https://attack.mitre.org/groups/G0098) in a 2010 campaign.(Citation: TrendMicro BlackTech June 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--plead | PLEAD | [PLEAD](https://attack.mitre.org/software/S0435) is a remote access tool (RAT) and downloader used by [BlackTech](https://attack.mitre.org/groups/G0098) in targeted attacks in East Asia including Taiwan, Japan, and Hong Kong.(Citation: TrendMicro BlackTech June 2017)(Citation: JPCert PLEAD Downloader June 2018) [PLEAD](https://attack.mitre.org/software/S0435) has also been referred to as [TSCookie](https://attack.mitre.org/software/S0436), though more recent reporting indicates likely separation between the two. [PLEAD](https://attack.mitre.org/software/S0435) was observed in use as early as March 2017.(Citation: JPCert TSCookie March 2018)(Citation: JPCert PLEAD Downloader June 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--tscookie | TSCookie | [TSCookie](https://attack.mitre.org/software/S0436) is a remote access tool (RAT) that has been used by [BlackTech](https://attack.mitre.org/groups/G0098) in campaigns against Japanese targets.(Citation: JPCert TSCookie March 2018)(Citation: JPCert BlackTech Malware September 2019). [TSCookie](https://attack.mitre.org/software/S0436) has been referred to as [PLEAD](https://attack.mitre.org/software/S0435) though more recent reporting indicates a separation between the two.(Citation: JPCert PLEAD Downloader June 2018)(Citation: JPCert BlackTech Malware September 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--waterbear | Waterbear | [Waterbear](https://attack.mitre.org/software/S0579) is modular malware attributed to [BlackTech](https://attack.mitre.org/groups/G0098) that has been used primarily for lateral movement, decrypting, and triggering payloads and is capable of hiding network behaviors.(Citation: Trend Micro Waterbear December 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| 中国関連のハッカー、二段階感染戦術を採用しDeuterbear RATを展開 | infrastructure-operation | 不明 | 不明 | 2024-05-18 | 中国関連のBlackTechハッカーグループがDeuterbear RATを使用 DeuterbearはWaterbearから進化したマルウェアで、Asia-Pacific地域を標的 二段階の感染戦術を採用し、持続性を確立 Waterbear RATモジュールは攻撃者が制御するインフラストラクチャから2回取得 1回目: Waterbear ダウンローダーをダウンロードし動かす 2回目: ダウンロード済みのWaterbearから新たなWaterbearをダウンロードして実行 | 中 | `source--daily-718b90e4e11c27f888d6` |
| BlackTech: テクノロジー、研究、政府部門を標的にした新しいツール「Deuterbear」 | infrastructure-operation | 不明 | 不明 | 2024-04-20 | BlackTechがアジア太平洋地域の技術、研究、政府部門を攻撃。 新しいバックドア「Deuterbear」を使用し、偽装技術を駆使。 このグループは中国に関連しており、2007年から活動を続けている。 ルーターファームウェアを改変し、侵害活動を隠蔽。 ネットワーク内での持続的なアクセスを目指し、C2サーバーと通信。 | 高 | `source--daily-1dfee7d2a70ba1432540` |
| PLEAD | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Shrouded Crossbow | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Waterbear | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

PLEAD; Shrouded Crossbow; Waterbear

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Hong Kong | Targeting text mentions hong kong. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Taiwan | Targeting text mentions taiwan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Japan | Targeting text mentions japan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Lateral Movement | T1021.001 | Remote Desktop Protocol | ) products. Common methods of persistence on a host include NetCat shells, modifying the victim registry [T1112] to enable the remote desktop protocol (RDP) [T1021.001], and secure shell (SSH) [T1021.004]. The actors have also used SNScan for enumeration [TA0007], and a local file transfer protocol (FTP) server [T1071.002] to move data through the victim network. For additional examples of malicious cyber actors living off the land, see Peo |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Lateral Movement | T1021.004 | SSH | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--blacktech--24eb19b60ca5a2a3`, `source--mitre-attack-19-1` |
| Stealth | T1036.002 | Right-to-Left Override | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.002 | File Transfer Protocols | [T1021.001], and secure shell (SSH) [T1021.004]. The actors have also used SNScan for enumeration [TA0007], and a local file transfer protocol (FTP) server [T1071.002] to move data through the victim network. For additional examples of malicious cyber actors living off the land, see People's Republic of China State- Sponsored Cyber Actor Living off the Land to Evade Detection. [2] Pivoting from international subsidiaries The PRC-linked Bl |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Command And Control | T1090 | Proxy | : File Transfer Protocols T1071.002 BlackTech actors use FTP to move data through a victim’s network or to deliver scripts for compromising routers. Proxy T1090 BlackTech actors use compromised routers to proxy traffic. |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Command And Control | T1090.002 | External Proxy | their infrastructure for proxying traffic [TA0011], blending in with corporate network traffic, and pivoting to other victims on the same corporate network [T1090.002]. Maintaining access via stealthy router backdoors BlackTech has targeted and exploited various brands and versions of router devices. TTPs against routers enable the actors to conceal configuration changes, hide commands, and disable logging while BlackTech actors conduct |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Execution | T1106 | Native API | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | de detection by endpoint detection and response (EDR) products. Common methods of persistence on a host include NetCat shells, modifying the victim registry [T1112] to enable the remote desktop protocol (RDP) [T1021.001], and secure shell (SSH) [T1021.004]. The actors have also used SNScan for enumeration [TA0007], and a local file transfer protocol (FTP) server [T1071.002] to move data through the victim network. For additional example |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | and tailored persistence mechanisms for compromising routers. These TTPs allow the actors to disable logging [T1562] and abuse trusted domain relationships [T1199] to pivot between international subsidiaries and domestic headquarters’ networks. Observable TTPs BlackTech cyber actors use custom malware payloads and remote access tools (RATs) to target victims’ operating systems. The actors have used a range of custom malware families |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control, Persistence, Stealth | T1205 | Traffic Signaling | ng variations of a customized firmware backdoor [T1542.004]. The backdoor functionality is enabled and disabled through specially crafted TCP or UDP packets [T1205]. This TTP is not solely limited to Cisco routers, and similar techniques could be used to enable backdoors in other network equipment. In some cases, BlackTech actors replace the firmware for certain Cisco IOS®-based routers with malicious firmware. Although BlackTech actor |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Persistence, Stealth | T1542.004 | ROMMONkit | ber Actors Hide in Router Firmware TLP:CLEAR TLP:CLEAR 4 actors have compromised several Cisco® routers using variations of a customized firmware backdoor [T1542.004]. The backdoor functionality is enabled and disabled through specially crafted TCP or UDP packets [T1205]. This TTP is not solely limited to Cisco routers, and similar techniques could be used to enable backdoors in other network equipment. In some cases, BlackTech actors re |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Defense Impairment | T1553.002 | Code Signing | Firmware TLP:CLEAR TLP:CLEAR 3 sign the malicious payloads, which make them appear legitimate and therefore more difficult for security software to detect [T1553.002]. BlackTech actors use living off the land TTPs to blend in with normal operating system and network activities, allowing them to evade detection by endpoint detection and response (EDR) products. Common methods of persistence on a host include NetCat shells, modifying the v |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Defense Impairment | T1553.006 | Code Signing Policy Modification | dified, unsigned bootloader and modified, unsigned firmware [T1601.001]. The modified bootloader enables the modified firmware to continue evading detection [T1553.006], however, it is not always necessary. BlackTech actors may also hide their presence and obfuscate changes made to compromised Cisco routers by hiding Embedded Event Manager (EEM) policies—a feature usually used in Cisco IOS to automate tasks that execute upon specified eve |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Credential Access, Defense Impairment, Persistence | T1556.004 | Network Device Authentication | irmware is used to establish persistent backdoor access [TA0003] and obfuscate future malicious activity. The modified firmware uses a built-in SSH backdoor [T1556.004], allowing BlackTech actors to maintain access to the compromised router without BlackTech connections being logged [T1562.003]. BlackTech actors bypass the router's built-in security features by first installing older legitimate firmware [T1601.002] that they then modify in |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Uncategorized | T1562 | MITRE ATT&CK T1562 | ors’ TTPs include developing customized malware and tailored persistence mechanisms for compromising routers. These TTPs allow the actors to disable logging [T1562] and abuse trusted domain relationships [T1199] to pivot between international subsidiaries and domestic headquarters’ networks. Observable TTPs BlackTech cyber actors use custom malware payloads and remote access tools (RATs) to target victims’ operating systems. The actor |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Uncategorized | T1562.001 | MITRE ATT&CK T1562.001 | he execution of other legitimate CLI commands, such as hindering forensic analysis by blocking copy, rename, and move commands for the associated EEM policy [T1562.001]. Firmware replacement process BlackTech actors utilize the following file types to compromise the router. These files are downloaded to the router via FTP or SSH. |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Uncategorized | T1562.003 | MITRE ATT&CK T1562.003 | uses a built-in SSH backdoor [T1556.004], allowing BlackTech actors to maintain access to the compromised router without BlackTech connections being logged [T1562.003]. BlackTech actors bypass the router's built-in security features by first installing older legitimate firmware [T1601.002] that they then modify in memory to allow the installation of a modified, unsigned bootloader and modified, unsigned firmware [T1601.001]. The modified b |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Uncategorized | T1562.006 | MITRE ATT&CK T1562.006 | timate commands. This policy has two functions: (1) to remove lines containing certain strings in the output of specified, legitimate Cisco IOS CLI commands [T1562.006], and (2) prevent the execution of other legitimate CLI commands, such as hindering forensic analysis by blocking copy, rename, and move commands for the associated EEM policy [T1562.001]. Firmware replacement process BlackTech actors utilize the following file types to com |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.003 | Code Signing Certificates | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--blacktech--24eb19b60ca5a2a3`, `source--mitre-attack-19-1` |
| Resource Development | T1588.004 | Digital Certificates | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1601.001 | Patch System Image | legitimate firmware [T1601.002] that they then modify in memory to allow the installation of a modified, unsigned bootloader and modified, unsigned firmware [T1601.001]. The modified bootloader enables the modified firmware to continue evading detection [T1553.006], however, it is not always necessary. BlackTech actors may also hide their presence and obfuscate changes made to compromised Cisco routers by hiding Embedded Event Manager (EEM |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |
| Defense Impairment | T1601.002 | Downgrade System Image | BlackTech connections being logged [T1562.003]. BlackTech actors bypass the router's built-in security features by first installing older legitimate firmware [T1601.002] that they then modify in memory to allow the installation of a modified, unsigned bootloader and modified, unsigned firmware [T1601.001]. The modified bootloader enables the modified firmware to continue evading detection [T1553.006], however, it is not always necessary. B |  |  | 不明 | 不明 | 中 | `source--blacktech--24eb19b60ca5a2a3` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 11件（`artifacts.csv`）

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
| source--blacktech--24eb19b60ca5a2a3 | CSA BLACKTECH HIDE IN ROUTERS TLP CLEAR |  | 不明 | Blacktech/CSA_BLACKTECH_HIDE_IN_ROUTERS_TLP-CLEAR.PDF | report | TLP:CLEAR | 中 |
| source--blacktech--8f7bfc2a1d9c653a | README |  | 不明 | Blacktech/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--daily-1dfee7d2a70ba1432540 | BlackTech: テクノロジー、研究、政府部門を標的にした新しいツール「Deuterbear」 | thehackernews.com | 2024-04-20 | https://thehackernews.com/2024/04/blacktech-targets-tech-research-and-gov.html | osint-report | TLP:CLEAR | 中 |
| source--daily-718b90e4e11c27f888d6 | 中国関連のハッカー、二段階感染戦術を採用しDeuterbear RATを展開 | thehackernews.com | 2024-05-18 | https://thehackernews.com/2024/05/china-linked-hackers-adopt-two-stage.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
