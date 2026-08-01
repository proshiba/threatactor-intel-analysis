# Lotus Blossom 脅威アクタープロファイル

- プロファイルID: `actor--lotus-blossom`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Lotus Blossomの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Lotus Blossom**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Bilbug | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DRAGONFISH | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Esile | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| RADIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Raspberry Typhoon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Spring Dragon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ST Group | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Thrip | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ST Group, Esile | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 14; mapping requires review. |

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

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Raspberry Typhoon | overlaps-with | 共有alias: Lotus Blossom, LotusBlossom, RADIUM, Raspberry Typhoon | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Lotus Blossom](https://attack.mitre.org/groups/G0030) is a long-standing threat group largely targeting various entities in Asia since at least 2009. In addition to government and related targets, [Lotus Blossom](https://attack.mitre.org/groups/G0030) has also targeted entities such as digital certificate issuers.(Citation: Lotus Blossom Jun 2015)(Citation: Symantec Bilbug 2022)(Citation: Cisco LotusBlossom 2025) |
| Capability | Emissary, Hannotog, Elise, Sagerunex, Elise Backdoor, Lstudio, CVE-2017-11882, certutil, Impacket, NBTscan, Ping, AdFind |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 30, Override Panda | multiple-name-intersection | 高 | China | https://www2.fireeye.com/rs/fireye/images/rpt-apt30.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=APT+30%2C+Override+Panda&n=1 |
| etda-threat-group-cards | Lotus Blossom, Spring Dragon, Thrip | canonical-name | 高 | China | https://blog.talosintelligence.com/lotus-blossom-espionage-group/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Lotus+Blossom%2C+Spring+Dragon%2C+Thrip&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Raspberry Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | LOTUS PANDA | canonical-name | 高 | CN, China | https://securelist.com/blog/research/70726/the-spring-dragon-apt/<br>https://securelist.com/spring-dragon-updated-activity/79067/<br>https://www.cfr.org/interactive/cyber-operations/lotus-blossom |
| misp-threat-actor | Thrip | single-alias-intersection | 中 | Unknown | https://www.cfr.org/interactive/cyber-operations/thrip<br>https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets<br>https://attack.mitre.org/groups/G0076/ |
| misp-threat-actor | Raspberry Typhoon | multiple-name-intersection | 高 | CN | https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW1aFyW |
| misp-microsoft-activity-group | Raspberry Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Lotus Blossom - G0030 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0030<br>https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html |
| misp-mitre-intrusion-set | Lotus Blossom - G0030 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0030<br>https://blog.talosintelligence.com/lotus-blossom-espionage-group/<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
| misp-mitre-intrusion-set | Thrip - G0076 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0076<br>https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| LOTUS PANDA | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Raspberry Typhoon | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--emissary | Emissary | [Emissary](https://attack.mitre.org/software/S0082) is a Trojan that has been used by [Lotus Blossom](https://attack.mitre.org/groups/G0030). It shares code with [Elise](https://attack.mitre.org/software/S0081), with both Trojans being part of a malware group referred to as LStudio.(Citation: Lotus Blossom Dec 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hannotog | Hannotog | [Hannotog](https://attack.mitre.org/software/S1211) is a type of backdoor malware uniquely assoicated with [Lotus Blossom](https://attack.mitre.org/groups/G0030) operations since at least 2022.(Citation: Symantec Bilbug 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--elise | Elise | [Elise](https://attack.mitre.org/software/S0081) is a custom backdoor Trojan that appears to be used exclusively by [Lotus Blossom](https://attack.mitre.org/groups/G0030). It is part of a larger group of tools referred to as LStudio, ST Group, and APT0LSTU.(Citation: Lotus Blossom Jun 2015)(Citation: Accenture Dragonfish Jan 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sagerunex | Sagerunex | [Sagerunex](https://attack.mitre.org/software/S1210) is a malware family exclusively associated with [Lotus Blossom](https://attack.mitre.org/groups/G0030) operations, with variants existing since at least 2016. Variations of [Sagerunex](https://attack.mitre.org/software/S1210) leverage non-traditional command and control mechanisms such as various web services.(Citation: Symantec Bilbug 2022)(Citation: Cisco LotusBlossom 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--elise-backdoor | Elise Backdoor | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--lstudio | Lstudio | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2017-11882 | CVE-2017-11882 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nbtscan | NBTscan | [NBTscan](https://attack.mitre.org/software/S0590) is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)(Citation: Symantec Waterbug Jun 2019)(Citation: FireEye APT39 Jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--adfind | AdFind | [AdFind](https://attack.mitre.org/software/S0552) is a free command-line query tool that can be used for gathering information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| countries | インド | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インドネシア | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | カンボジア | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてカンボジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | サウジアラビア | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてサウジアラビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | シンガポール | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてシンガポールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ネパール | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてネパールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ブルネイ | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてブルネイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブータン | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてブータンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | マカオ | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてマカオが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ミャンマー | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてミャンマーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ラオス | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国としてラオスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 日本 | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 米国 | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 香港 | 構造化OSINTの被害国フィールドでLotus Blossomの標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | アジア | MITRE ATT&CKのGroup概要でLotus Blossomの標的範囲としてアジアが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 南アジア | インド、ネパール、ブータンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | マカオ、台湾、日本、韓国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | 構造化OSINTの被害地域フィールドでLotus Blossomの標的範囲として東南アジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 政府・行政 | In addition to government and related targets, [Lotus Blossom](https://attack.mitre.org/groups/G0030) has also targeted entities such as digital certificate issuers.(Citation: Lotus Blossom Jun 2015)(Citation: Symantec Bilbug 2022)(Citation: Cisco LotusBlossom 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1012 | Query Registry | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has run commands such as `reg query HKLM\SYSTEM\CurrentControlSet\Services\[service name]\Parameters` to verify if installed implants are running as a service.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `ipconfig` and `netstat` to gather network information on compromised hosts.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016.001 | Internet Connection Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has performed checks to determine if a victim machine is able to access the Internet.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used [Ping](https://attack.mitre.org/software/S0097) to identify remote systems.(Citation: Symantec Bilbug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used port scanners to enumerate services on remote hosts.(Citation: Symantec Bilbug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used WMI to enable lateral movement.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `netstat` to identify system network connections.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has locally staged compressed and archived data for follow-on exfiltration.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `dir` to examine the local filesystem of victim machines.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `net` to profile local system users.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used `net` commands and tools such as [AdFind](https://attack.mitre.org/software/S0552) to profile domain accounts associated with victim machines and make Active Directory queries.(Citation: Cisco LotusBlossom 2025)(Citation: Symantec Bilbug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.001 | Internal Proxy | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used publicly available tools such as the Venom proxy tool to proxy traffic out of victim environments.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.003 | Multi-hop Proxy | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used tools such as the publicly available HTran tool for proxying traffic in victim environments.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has installed tools such as [Sagerunex](https://attack.mitre.org/software/S1210) by writing them to the Windows registry.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1134 | Access Token Manipulation | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has retrieved process tokens for processes to adjust the privileges of the launch process or other items.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used tools such as [AdFind](https://attack.mitre.org/software/S0552) to make Active Directory queries.(Citation: Symantec Bilbug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1539 | Steal Web Session Cookie | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used publicly-available tools to steal cookies from browsers such as Chrome.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has configured tools such as [Sagerunex](https://attack.mitre.org/software/S1210) to run as Windows services.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used WinRAR for compressing data in RAR format.(Citation: Cisco LotusBlossom 2025)(Citation: Symantec Bilbug 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.003 | Archive via Custom Method | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used custom tools to compress and archive data on victim systems.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used publicly-available tools such as a Python-based cookie stealer for Chrome browsers, [Impacket](https://attack.mitre.org/software/S0357), and the Venom proxy tool.(Citation: Cisco LotusBlossom 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 51件（`artifacts.csv`）

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
| source--lotus-blossom--4a85f83325a9c726 | lotus blossom |  | 不明 | actor_profile/evidence/lotus-blossom.csv | structured-data | TLP:CLEAR | 中 |
| source--lotus-blossom--7c821bf60f2181b4 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--b783f581be79fdda | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--e6bc815b9aa591af | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--9a04a2809f2bcc75 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--lotus-blossom--d0f566d7555442b2 | APT blackberry mobile malware report |  | 不明 | summary/2020/APT-blackberry-mobile-malware-report.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--6766de4596f33047 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--e54d10f916fc0fcf | Microsoft Digital Defense Report 2022 |  | 2022 | summary/2022/Microsoft Digital Defense Report 2022.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--fd8c460113f606cf | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--89998e4bcd27d8d9 | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--bfb862af712c4c0d | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--c939282a2638c312 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--lotus-blossom--a3114f0fb5932e50 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
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
