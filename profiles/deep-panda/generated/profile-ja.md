# Deep Panda 脅威アクタープロファイル

- プロファイルID: `actor--deep-panda`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Deep Pandaの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Deep Panda**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Black Vine | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| KungFu Kittens | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| PinkPanther | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Shell Crew | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| WebMasters | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | Actor-specific reporting explicitly describes espionage or intelligence collection. | 高 | `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description; not inferred from country or state sponsorship. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| APT19 | overlaps-with | 共有alias: APT19 | 低 | `source--mitre-attack-19-2` |
| Hurricane Panda | overlaps-with | 共有alias: Black Vine | 低 | `source--mitre-attack-19-2` |
| Winnti Group | overlaps-with | 共有alias: Winnti Group | 低 | `source--mitre-attack-19-2` |
| APT19 | related-to | (Citation: FireEye APT19) Some analysts track [APT19](https://attack.mitre.org/groups/G0073) and [Deep Panda](https://attack.mitre.org/groups/G0009) as the same group, but it is unclear from open source information if the groups are the same. | 中 | `source--mitre-attack-19-2` |

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
| etda-threat-group-cards | APT 19, Deep Panda, C0d0so0 | canonical-name | 高 | China | https://apt.etda.or.th/cgi-bin/showcard.cgi?g=APT+19%2C+Deep+Panda%2C+C0d0so0&n=1 |
| etda-threat-group-cards | Turbine Panda, APT 26, Shell Crew, WebMasters, KungFu Kittens | multiple-name-intersection | 高 | China | https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2014/h12756-wp-shell-crew.pdf<br>https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-black-vine-cyberespionage-group.pdf<br>https://www.crowdstrike.com/resources/wp-content/brochures/reports/huge-fan-of-your-work-intelligence-report.pdf |
| etda-threat-group-cards | Winnti Group, Wicked Panda | single-alias-intersection | 中 | China | https://blog.trendmicro.com/trendlabs-security-intelligence/pigs-malware-examining-possible-member-winnti-group/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>https://401trg.com/burning-umbrella/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Checkered Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Leopard Typhoon | single-alias-intersection | 中 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT19 | canonical-name | 高 | CN, China | http://cybercampaigns.net/wp-content/uploads/2013/06/Deep-Panda.pdf<br>https://docs.huihoo.com/rsaconference/usa-2014/anf-t07b-the-art-of-attribution-identifying-and-pursuing-your-cyber-adversaries-final.pdf<br>https://www.cfr.org/interactive/cyber-operations/deep-panda |
| misp-microsoft-activity-group | Checkered Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Leopard Typhoon | single-alias-intersection | 中 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Deep Panda - G0009 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0009<br>https://web.archive.org/web/20170823094836/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-black-vine-cyberespionage-group.pdf<br>https://web.archive.org/web/20171017072306/https://icitech.org/icit-brief-chinas-espionage-dynasty-economic-death-by-a-thousand-cuts/ |
| misp-mitre-enterprise-intrusion-set | Winnti Group - G0044 | single-alias-intersection | 中 |  | http://www.symantec.com/connect/blogs/suckfly-revealing-secret-life-your-code-signing-certificates<br>https://401trg.github.io/pages/burning-umbrella.html<br>https://attack.mitre.org/groups/G0044 |
| misp-mitre-enterprise-intrusion-set | APT19 - G0073 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0073<br>https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/<br>https://web.archive.org/web/20171017072306/https://icitech.org/icit-brief-chinas-espionage-dynasty-economic-death-by-a-thousand-cuts/ |
| misp-mitre-intrusion-set | Deep Panda - G0009 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0009<br>https://web.archive.org/web/20170823094836/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-black-vine-cyberespionage-group.pdf<br>https://web.archive.org/web/20171017072306/https://icitech.org/icit-brief-chinas-espionage-dynasty-economic-death-by-a-thousand-cuts/ |
| misp-mitre-intrusion-set | Winnti Group - G0044 | single-alias-intersection | 中 |  | http://www.symantec.com/connect/blogs/suckfly-revealing-secret-life-your-code-signing-certificates<br>https://401trg.github.io/pages/burning-umbrella.html<br>https://attack.mitre.org/groups/G0044 |
| misp-mitre-intrusion-set | APT19 - G0073 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0073<br>https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/<br>https://web.archive.org/web/20171017072306/https://icitech.org/icit-brief-chinas-espionage-dynasty-economic-death-by-a-thousand-cuts/ |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | APT19 | single-alias-intersection | 中 | CN |  |
| misp-tidal-groups | Deep Panda | canonical-name | 高 | CN |  |
| misp-tidal-groups | Winnti Group | single-alias-intersection | 中 | CN |  |

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
| malware--derusbi | Derusbi | [Derusbi](https://attack.mitre.org/software/S0021) is malware used by multiple Chinese APT groups.(Citation: Novetta-Axiom)(Citation: ThreatConnect Anthem) Both Windows and Linux variants have been observed.(Citation: Fidelis Turbo) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--mivast | Mivast | [Mivast](https://attack.mitre.org/software/S0080) is a backdoor that has been used by [Deep Panda](https://attack.mitre.org/groups/G0009). It was reportedly used in the Anthem breach. (Citation: Symantec Black Vine) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--sakula | Sakula | [Sakula](https://attack.mitre.org/software/S0074) is a remote access tool (RAT) that first surfaced in 2012 and was used in intrusions throughout 2015. (Citation: Dell Sakula) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--streamex | StreamEx | [StreamEx](https://attack.mitre.org/software/S0142) is a malware family that has been used by [Deep Panda](https://attack.mitre.org/groups/G0009) since at least 2015. In 2016, it was distributed via legitimate compromised Korean websites. (Citation: Cylance Shell Crew Feb 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--tasklist | Tasklist | The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし

OPM; Anthem Hack

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 政府・行政 | [Deep Panda](https://attack.mitre.org/groups/G0009) is a suspected Chinese threat group known to target many industries, including government, defense, financial, and telecommunications. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | 金融 | [Deep Panda](https://attack.mitre.org/groups/G0009) is a suspected Chinese threat group known to target many industries, including government, defense, financial, and telecommunications. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | 防衛・軍事 | [Deep Panda](https://attack.mitre.org/groups/G0009) is a suspected Chinese threat group known to target many industries, including government, defense, financial, and telecommunications. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | 情報通信 | [Deep Panda](https://attack.mitre.org/groups/G0009) is a suspected Chinese threat group known to target many industries, including government, defense, financial, and telecommunications. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1018 | Remote System Discovery | [Deep Panda](https://attack.mitre.org/groups/G0009) has used ping to identify other machines of interest.(Citation: Alperovitch 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [Deep Panda](https://attack.mitre.org/groups/G0009) uses net.exe to connect to network shares using <code>net use</code> commands with compromised credentials.(Citation: Alperovitch 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1027.005 | Indicator Removal from Tools | [Deep Panda](https://attack.mitre.org/groups/G0009) has updated and modified its malware, resulting in different hash values that evade detection.(Citation: Symantec Black Vine) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1047 | Windows Management Instrumentation | The [Deep Panda](https://attack.mitre.org/groups/G0009) group is known to utilize WMI for lateral movement.(Citation: Alperovitch 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1057 | Process Discovery | [Deep Panda](https://attack.mitre.org/groups/G0009) uses the Microsoft [Tasklist](https://attack.mitre.org/software/S0057) utility to list processes running on systems.(Citation: Alperovitch 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.001 | PowerShell | [Deep Panda](https://attack.mitre.org/groups/G0009) has used PowerShell scripts to download and execute programs in memory, without writing to disk.(Citation: Alperovitch 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1218.010 | Regsvr32 | [Deep Panda](https://attack.mitre.org/groups/G0009) has used regsvr32.exe to execute a server variant of [Derusbi](https://attack.mitre.org/software/S0021) in victim networks.(Citation: RSA Shell Crew) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence | T1505.003 | Web Shell | [Deep Panda](https://attack.mitre.org/groups/G0009) uses Web shells on publicly accessible Web servers to access victim networks.(Citation: CrowdStrike Deep Panda Web Shells) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1546.008 | Accessibility Features | [Deep Panda](https://attack.mitre.org/groups/G0009) has used the sticky-keys technique to bypass the RDP login screen on remote systems during intrusions.(Citation: RSA Shell Crew) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1564.003 | Hidden Window | [Deep Panda](https://attack.mitre.org/groups/G0009) has used <code>-w hidden</code> to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows by setting the WindowStyle parameter to hidden. (Citation: Alperovitch 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 3件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- 4 alias lead(s) remain non-canonical pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--deep-panda--5bb4298934a9762d | deep panda |  | 不明 | actor_profile/evidence/deep-panda.csv | structured-data | TLP:CLEAR | 中 |
| source--deep-panda--1d4c45b999835d77 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--deep-panda--7d52890c8255cf26 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--deep-panda--1f1ded92d4cd6d38 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--deep-panda--31c6d0557aedb86d | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--deep-panda--723e42022b3b84c3 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--deep-panda--0f3347e7c87dcb50 | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--deep-panda--1c0bdd899a50feb8 | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--deep-panda--e58111dd26ac06f8 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--deep-panda--a399e3de5f968aa1 | 004 |  | 不明 | summary/UNREDACTEDMagazine/004.pdf | report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
