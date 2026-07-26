# Lazarus Group 脅威アクタープロファイル

プロファイルID: `actor--lazarus`  
状態: draft  
更新日時: 2026-07-26T05:28:44Z  
構造バージョン: 1.0.0

## エグゼクティブサマリー

Lazarus Groupの標準化プロファイル。リポジトリ内の専用資料27件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Lazarus Group**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Diamond Sleet | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Guardians of Peace | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| HIDDEN COBRA | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Labyrinth Chollima | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| NICKEL ACADEMY | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ZINC | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Group 77 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 3; mapping requires review. |
| Hastati Group | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 3; mapping requires review. |
| Bureau 121 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 3; mapping requires review. |
| Unit 121 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 3; mapping requires review. |
| Whois Hacking Team | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 3; mapping requires review. |
| NewRomanic Cyber Army Team | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 3; mapping requires review. |
| Appleworm | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 3; mapping requires review. |
| G0032 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 3; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the North Korea worksheet.

- 国: North Korea
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
| Andariel | related-to | MITRE considers Andariel a subset of Lazarus Group; U.S. Treasury also describes Andariel as a Lazarus subgroup controlled by the RGB. | 高 | `source--mitre-live-andariel-2024`, `source--treasury-dprk-groups-2019` |
| APT38 | overlaps-with | Government sources connect Bluenoroff/APT38 and Lazarus under the RGB and a common conspiracy, while industry reporting preserves APT38 as a financially focused cluster. | 高 | `source--treasury-dprk-groups-2019`, `source--doj-dprk-conspiracy-2021` |
| APT37 | overlaps-with | North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name [Lazarus Group](https://attack.mitre.org/groups/G0032) instead of tracking clusters or subgroups. | 高 | `source--mitre-attack-19-1` |
| Kimsuky | overlaps-with | DPRK threat actor cluster boundaries overlap in open source reporting, with some security researchers consolidating all attributed North Korean state-sponsored cyber activity under [Lazarus Group](https://attack.mitre.org/groups/G0032), rather than tracking operationally distinct subgroups. | 高 | `source--mitre-attack-19-1` |
| Sharpshooter | overlaps-with | Though overlaps between this adversary and [Lazarus Group](https://attack.mitre.org/groups/G0032) have been noted, definitive links have not been established.(Citation: McAfee Sharpshooter December 2018) | 高 | `source--mitre-attack-19-1` |
| Moonstone Sleet | overlaps-with | The group previously overlapped significantly with another North Korean-linked entity, [Lazarus Group](https://attack.mitre.org/groups/G0032), but has differentiated its tradecraft since 2023. | 高 | `source--mitre-attack-19-1` |
| AppleJeus | related-to | Associated with the broader [Lazarus Group](https://attack.mitre.org/groups/G0032) umbrella of actors, [AppleJeus](https://attack.mitre.org/groups/G1049) has been active since at least 2018 and is closely aligned in resources with TEMP.hermit, another DPRK-affiliated group under the same umbrella.(Citation: dtex DPRK 2025 structure ITworkers) The group’s primary mission is to generate and launder revenue to provide financial support to the government. | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Lazarus Group](https://attack.mitre.org/groups/G0032) is a North Korean state-sponsored cyber threat group attributed to the Reconnaissance General Bureau (RGB). (Citation: US-CERT HIDDEN COBRA June 2017) (Citation: Treasury North Korean Cyber Groups September 2019) [Lazarus Group](https://attack.mitre.org/groups/G0032) has been active since at least 2009 and is reportedly responsible for the November 2014 destructive wiper attack on Sony Pictures Entertainment, identified by Novetta as part of Operation Blockbuster. Malware used by [Lazarus Group](https://attack.mitre.org/groups/G0032) correlates to other reported campaigns, including Operation Flame, Operation 1Mission, Operation Troy, DarkSeoul, and Ten Days of Rain.(Citation: Novetta Blockbuster)<br><br>North Korea’s cyber operations have shown a consistent pattern of adaptation, forming and reorganizing units as national priorities shift. These units frequently share personnel, infrastructure, malware, and tradecraft, making it difficult to attribute specific operations with high confidence. Public reporting often uses “Lazarus Group” as an umbrella term for multiple North Korean cyber operators conducting espionage, destructive attacks, and financially motivated campaigns.(Citation: Mandiant DPRK Laz Org Breakdown 2022)(Citation: Mandiant DPRK Groups 2023)(Citation: JPCert Blog Laz Subgroups 2025)<br><br> |
| Capability | BLINDINGCAN, Proxysvc, KEYMARBLE, ThreatNeedle, Bankshot, AuditCred, Dacls, HOPLIGHT, Volgmer, WannaCry, TYPEFRAME, TAINTEDSCRIBE, MagicRAT, RATANKBA, BADCALL, Cryptoistic, HotCroissant, HARDRAIN, AppleJeus, ECCENTRICBANDWAGON, Dtrack, FALLCHILL, Tdrop, Tdrop2, Troy, Destover, FallChill RAT, Hawup, Manuscrypt, WolfRAT, SheepRAT, HtDnDownLoader, RawDisk, netsh, Responder, route |
| Infrastructure |  |
| Victim | Believed to be responsible for Dark Seoul, Ten Days of Rain, the Sony Pictures Entertainment attack, the SWIFT-related bank heists, and WannaCry. Known to the U.S. government as Hidden Cobra. Targeting also BitCoin Exchanges, financial sector, technology/engineering sector |
| Socio-political | North Korea |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Covellite | single-alias-intersection | 中 | North Korea | https://dragos.com/resource/covellite/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Covellite&n=1 |
| etda-threat-group-cards | Lazarus Group, Hidden Cobra, Labyrinth Chollima | canonical-name | 高 | North Korea | https://blog.malwarebytes.com/threat-analysis/2019/03/the-advanced-persistent-threat-files-lazarus-group/<br>https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/a-look-into-the-lazarus-groups-operations<br>https://www.kaspersky.com/about/press-releases/2017_chasing-lazarus-a-hunt-for-the-infamous-hackers-to-prevent-large-bank-robberies |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Citrine Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Diamond Sleet | multiple-name-intersection | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Jade Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Moonstone Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Lazarus Group | canonical-name | 高 | KP, Korea (Democratic People's Republic of) | https://threatpost.com/operation-blockbuster-coalition-ties-destructive-attacks-to-lazarus-group/116422/<br>https://www.us-cert.gov/ncas/alerts/TA17-164A<br>https://www.us-cert.gov/ncas/alerts/TA17-318A |
| misp-microsoft-activity-group | Citrine Sleet | single-alias-intersection | 中 | KP, North Korea | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Diamond Sleet | multiple-name-intersection | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Jade Sleet | single-alias-intersection | 中 | KP, North Korea | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Moonstone Sleet | single-alias-intersection | 中 | KP, North Korea | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Lazarus Group - G0032 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0032<br>https://www.us-cert.gov/ncas/alerts/TA17-164A<br>https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf |
| misp-mitre-intrusion-set | Lazarus Group - G0032 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0032<br>https://blogs.jpcert.or.jp/en/2025/03/classifying-lazaruss-subgroup.html<br>https://blogs.microsoft.com/on-the-issues/2017/12/19/microsoft-facebook-disrupt-zinc-malware-attack-protect-customers-internet-ongoing-cyberthreats/ |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Operation Sharpshooter | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| STARDUST CHOLLIMA | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| TraderTraitor | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--applejeus | AppleJeus | [AppleJeus](https://attack.mitre.org/software/S0584) is a family of downloaders initially discovered in 2018 embedded within trojanized cryptocurrency applications. [AppleJeus](https://attack.mitre.org/software/S0584) has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032), targeting companies in the energy, finance, government, industry, technology, and telecommunications sectors, and several countries including the United States, United Kingdom, South Korea, Australia, Brazil, New Zealand, and Russia. [AppleJeus](https://attack.mitre.org/software/S0584) has been used to distribute the [FALLCHILL](https://attack.mitre.org/software/S0181) RAT.(Citation: CISA AppleJeus Feb 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--auditcred | AuditCred | [AuditCred](https://attack.mitre.org/software/S0347) is a malicious DLL that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032) during their 2018 attacks.(Citation: TrendMicro Lazarus Nov 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--badcall | BADCALL | [BADCALL](https://attack.mitre.org/software/S0245) is a Trojan malware variant used by the group [Lazarus Group](https://attack.mitre.org/groups/G0032). (Citation: US-CERT BADCALL) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--bankshot | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) is a remote access tool (RAT) that was first reported by the Department of Homeland Security in December of 2017. In 2018, [Lazarus Group](https://attack.mitre.org/groups/G0032) used the [Bankshot](https://attack.mitre.org/software/S0239) implant in attacks against the Turkish financial sector. (Citation: McAfee Bankshot) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--blindingcan | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) is a remote access Trojan that has been used by the North Korean government since at least early 2020 in cyber operations against defense, engineering, and government organizations in Western Europe and the US.(Citation: US-CERT BLINDINGCAN Aug 2020)(Citation: NHS UK BLINDINGCAN Aug 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cryptoistic | Cryptoistic | [Cryptoistic](https://attack.mitre.org/software/S0498) is a backdoor, written in Swift, that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032).(Citation: SentinelOne Lazarus macOS July 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--dacls | Dacls | [Dacls](https://attack.mitre.org/software/S0497) is a multi-platform remote access tool used by [Lazarus Group](https://attack.mitre.org/groups/G0032) since at least December 2019.(Citation: TrendMicro macOS Dacls May 2020)(Citation: SentinelOne Lazarus macOS July 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--daily-841eaf454386945cebf3 | InvisibleFerret | tech-memo日次IOCでLazarus Groupによる使用が報告されたマルウェア。 | 2026-05-13 | 2026-05-13 | 中 | `source--daily-e91cff6491073bc4c828` |
| malware--daily-cb8206bbfbe60297e4ec | BeaverTail | tech-memo日次IOCでLazarus Groupによる使用が報告されたマルウェア。 | 2026-05-13 | 2026-05-13 | 中 | `source--daily-e91cff6491073bc4c828` |
| malware--destover | Destover | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--dtrack | Dtrack | [Dtrack](https://attack.mitre.org/software/S0567) is spyware that was discovered in 2019 and has been used against Indian financial institutions, research facilities, and the Kudankulam Nuclear Power Plant. [Dtrack](https://attack.mitre.org/software/S0567) shares similarities with the DarkSeoul campaign, which was attributed to [Lazarus Group](https://attack.mitre.org/groups/G0032). (Citation: Kaspersky Dtrack)(Citation: Securelist Dtrack)(Citation: Dragos WASSONITE)(Citation: CyberBit Dtrack)(Citation: ZDNet Dtrack) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--eccentricbandwagon | ECCENTRICBANDWAGON | [ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) is a remote access Trojan (RAT) used by North Korean cyber actors that was first identified in August 2020. It is a reconnaissance tool--with keylogging and screen capture functionality--used for information gathering on compromised systems.(Citation: CISA EB Aug 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--fallchill | FALLCHILL | [FALLCHILL](https://attack.mitre.org/software/S0181) is a RAT that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032) since at least 2016 to target the aerospace, telecommunications, and finance industries. It is usually dropped by other [Lazarus Group](https://attack.mitre.org/groups/G0032) malware or delivered when a victim unknowingly visits a compromised website. (Citation: US-CERT FALLCHILL Nov 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--fallchill-rat | FallChill RAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--hardrain | HARDRAIN | [HARDRAIN](https://attack.mitre.org/software/S0246) is a Trojan malware variant reportedly used by the North Korean government. (Citation: US-CERT HARDRAIN March 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hawup | Hawup | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--hoplight | HOPLIGHT | [HOPLIGHT](https://attack.mitre.org/software/S0376) is a backdoor Trojan that has reportedly been used by the North Korean government.(Citation: US-CERT HOPLIGHT Apr 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hotcroissant | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) is a remote access trojan (RAT) attributed by U.S. government entities to malicious North Korean government cyber activity, tracked collectively as HIDDEN COBRA.(Citation: US-CERT HOTCROISSANT February 2020) [HotCroissant](https://attack.mitre.org/software/S0431) shares numerous code similarities with [Rifdoor](https://attack.mitre.org/software/S0433).(Citation: Carbon Black HotCroissant April 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--htdndownloader | HtDnDownLoader | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--keymarble | KEYMARBLE | [KEYMARBLE](https://attack.mitre.org/software/S0271) is a Trojan that has reportedly been used by the North Korean government. (Citation: US-CERT KEYMARBLE Aug 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--magicrat | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) is a remote access tool developed in C++ and exclusively used by the [Lazarus Group](https://attack.mitre.org/groups/G0032) threat actor in operations. [MagicRAT](https://attack.mitre.org/software/S1182) allows for arbitrary command execution on victim machines and provides basic remote access functionality.(Citation: Cisco MagicRAT 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--manuscrypt | Manuscrypt | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--proxysvc | Proxysvc | [Proxysvc](https://attack.mitre.org/software/S0238) is a malicious DLL used by [Lazarus Group](https://attack.mitre.org/groups/G0032) in a campaign known as Operation GhostSecret. It has appeared to be operating undetected since 2017 and was mostly observed in higher education organizations. The goal of [Proxysvc](https://attack.mitre.org/software/S0238) is to deliver additional payloads to the target and to maintain control for the attacker. It is in the form of a DLL that can also be executed as a standalone process. (Citation: McAfee GhostSecret) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ratankba | RATANKBA | [RATANKBA](https://attack.mitre.org/software/S0241) is a remote controller tool used by [Lazarus Group](https://attack.mitre.org/groups/G0032). [RATANKBA](https://attack.mitre.org/software/S0241) has been used in attacks targeting financial institutions in Poland, Mexico, Uruguay, the United Kingdom, and Chile. It was also seen used against organizations related to telecommunications, management consulting, information technology, insurance, aviation, and education. [RATANKBA](https://attack.mitre.org/software/S0241) has a graphical user interface to allow the attacker to issue jobs to perform on the infected machines. (Citation: Lazarus RATANKBA) (Citation: RATANKBA) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sheeprat | SheepRAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--taintedscribe | TAINTEDSCRIBE | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) is a fully-featured beaconing implant integrated with command modules used by [Lazarus Group](https://attack.mitre.org/groups/G0032). It was first reported in May 2020.(Citation: CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--tdrop | Tdrop | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--tdrop2 | Tdrop2 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--threatneedle | ThreatNeedle | [ThreatNeedle](https://attack.mitre.org/software/S0665) is a backdoor that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032) since at least 2019 to target cryptocurrency, defense, and mobile gaming organizations.  It is considered to be an advanced cluster of [Lazarus Group](https://attack.mitre.org/groups/G0032)'s Manuscrypt (a.k.a. NukeSped) malware family.(Citation: Kaspersky ThreatNeedle Feb 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--troy | Troy | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--typeframe | TYPEFRAME | [TYPEFRAME](https://attack.mitre.org/software/S0263) is a remote access tool that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032). (Citation: US-CERT TYPEFRAME June 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--volgmer | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) is a backdoor Trojan designed to provide covert access to a compromised system. It has been used since at least 2013 to target the government, financial, automotive, and media industries. Its primary delivery mechanism is suspected to be spearphishing. (Citation: US-CERT Volgmer Nov 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--wannacry | WannaCry | [WannaCry](https://attack.mitre.org/software/S0366) is ransomware that was first seen in a global attack during May 2017, which affected more than 150 countries. It contains worm-like features to spread itself across a computer network using the SMBv1 exploit EternalBlue.(Citation: LogRhythm WannaCry)(Citation: US-CERT WannaCry 2017)(Citation: Washington Post WannaCry 2017)(Citation: FireEye WannaCry 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--wolfrat | WolfRAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--rawdisk | RawDisk | [RawDisk](https://attack.mitre.org/software/S0364) is a legitimate commercial driver from the EldoS Corporation that is used for interacting with files, disks, and partitions. The driver allows for direct modification of data on a local computer's hard drive. In some cases, the tool can enact these raw disk modifications from user-mode processes, circumventing Windows operating system security features.(Citation: EldoS RawDisk ITpro)(Citation: Novetta Blockbuster Destructive Malware) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netsh | netsh | [netsh](https://attack.mitre.org/software/S0108) is a scripting utility used to interact with networking components on local or remote systems. (Citation: TechNet Netsh) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--responder | Responder | Responder is an open source tool used for LLMNR, NBT-NS and MDNS poisoning, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication. (Citation: GitHub Responder) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--route | route | [route](https://attack.mitre.org/software/S0103) can be used to find or change information within the local system IP routing table. (Citation: TechNet Route) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Applejeus | operation | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Blockbuster | operation | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Dark Seoul | operation | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Dream Job | operation | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Inception | operation | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| KuCoin Hack | operation | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| NorthStar | operation | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| ThreatNeedle | operation | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Operation Dream Job | campaign | 2019-09-01T04:00:00.000Z | 2020-08-01T04:00:00.000Z | [Operation Dream Job](https://attack.mitre.org/campaigns/C0022) was a cyber espionage operation likely conducted by [Lazarus Group](https://attack.mitre.org/groups/G0032) that targeted the defense, aerospace, government, and other sectors in the United States, Israel, Australia, Russia, and India. In at least one case, the cyber actors tried to monetize their network access to conduct a business email compromise (BEC) operation. In 2020, security researchers noted overlapping TTPs, to include fake job lures and code similarities, between [Operation Dream Job](https://attack.mitre.org/campaigns/C0022), Operation North Star, and Operation Interception; by 2022 security researchers described [Operation Dream Job](https://attack.mitre.org/campaigns/C0022) as an umbrella term covering both Operation Interception and Operation North Star.(Citation: ClearSky Lazarus Aug 2020)(Citation: McAfee Lazarus Jul 2020)(Citation: ESET Lazarus Jun 2020)(Citation: The Hacker News Lazarus Aug 2022) | 高 | `source--mitre-attack-19-1` |
| Lazarus GroupがGit Hooksを使ってマルウェアを隠蔽 | reported-activity | 2026-05-13 | 2026-05-13 | OpenSourceMalwareは、DPRKのContagious Interview / TaskJackerキャンペーンの新手口を報告した。 攻撃者は従来の.vscode/tasks.jsonやpackage.json postinstallではなく、Git hooks内にStage-2ローダーを隠している。 悪性の.githooks/pre-commitはOSを判定し、precommit.vercel.appから環境別ペイロードを取得して実行する。 macOS/Linuxではシェルスクリプト、WindowsのGit Bash/MSYS/Cygwinではcmd.exe対応ペイロードが配信される。 最終的にInvisibleFerretやBeaverTail系のインプラントで暗号資産ウォレットや認証情報を窃取する。 | 中 | `source--daily-e91cff6491073bc4c828` |

Blockbuster; Dark Seoul; Applejeus; Inception; NorthStar; Dream Job; KuCoin Hack; ThreatNeedle

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Finance | Targeting text indicates the Finance sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1001.003 | Protocol or Service Impersonation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1002 | MITRE ATT&CK T1002 | Using file hosting services like DropBox and OneDrive Procedures Obfuscated Files or Information - T1027 Sending decoy file Technique Data Compressed –T1002 Archives (WinRAR or 7- ZIP) Procedures Virtualization/Sandbox Evasion: System Checks – T1497 Anti VM Technique + Tool Exploitation Exfiltration Over C2 Channel – T1041 Template Injection – T1221 Template injection - downloading files from C2 Tool |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Credential Access | T1003.001 | LSASS Memory | vilege escalation to root 40 Exploitation of ‘Printnightmare’ vulnerability (CVE- 2021-34527) to execute ord.dll with SYSTEM privileges - CREDENTIAL ACCESS T1003.001 LSASS Memory cmd.exe /C c:\windows\ system32\rundll32.exe C:\windows\System32\ comsvcs.dll, MiniDump 680 Use of DumpLsass hacking tool to create a dump of hashes which can then be moved elsewhere for hashes to be extracted using Mimikatz C:\windows\temp\mmc. dat full > C:\W |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486`, `source--lazarus--5dbd54be61ed2947` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | dify Registry Credential Access T1557.001 LLMNR/NBT-NS Poisoning and SMB Relay Discovery T1135 T1057 T1016 T1033 T1049 T1082 T1083 T1007 Network Share Discovery Process Discovery System Network Configuration Discovery System Owner/User Discovery System Network Connections Discovery System Information Discovery File and Directory Discovery System Service Discovery |  |  | 不明 | 不明 | 中 | `source--lazarus--f6685ba8150b853c` |
| Command And Control | T1008 | Fallback Channels | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--ff5ba7d73371b72f`, `source--mitre-attack-19-1` |
| Discovery | T1010 | Application Window Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5cb141837fab1486`, `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5cb141837fab1486`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | p\[a-zA-Z]{8} Query default name server for supplied host/ domain name cmd.exe /C nslookup [hostname.fqdn] > C:\ WINDOWS\Temp\[a-zA-Z] {8}.tmp 2>&1 DISCOVERY T1018 Remote System Discovery List computer accounts in Active Directory , returning IP address, OS, and OS Service Pack level cmd.exe /C powershell Get-ADComputer -Filter * -Properties ipv4Address, OperatingSystem, Operat- ingSystemServicePack > C:\ Windows\Temp\[a-zA-Z]{8}. tmp |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Exfiltration | T1020 | Automated Exfiltration | mooth Operator contains multiple C2 servers and randomly chooses a new server from the list for each beacon, if one fails it will try another. Exfiltration T1020 Automated Exfiltration Smooth Operator exfiltrates automatically collected data, not over the existing C2 channel. |  |  | 不明 | 不明 | 中 | `source--lazarus--ff5ba7d73371b72f` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5cb141837fab1486`, `source--lazarus--5dbd54be61ed2947`, `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.005 | VNC | bypass certain controls T1021.001 Remote Services: Remote Desktop Protocol RDP was used to laterally move around the target network using valid accounts T1021.005 Remote Services: VNC VNC was leveraged to laterally move across some hosts during the attack T1083 File and Directory Discovery The threat actor was observed searching for key files of interest that contained credentials, architecture information or sensitive financial data T |  |  | 不明 | 不明 | 中 | `source--lazarus--5dbd54be61ed2947` |
| Stealth | T1027 | Obfuscated Files or Information | cquire and/or use 3rd party software services – T1308 Using file hosting services like DropBox and OneDrive Procedures Obfuscated Files or Information - T1027 Sending decoy file Technique Data Compressed –T1002 Archives (WinRAR or 7- ZIP) Procedures Virtualization/Sandbox Evasion: System Checks – T1497 Anti VM Technique + Tool Exploitation Exfiltration Over C2 Channel – T1041 Template Injection – T1221 Template injection |  |  | 不明 | 不明 | 中 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--3c464a6b801a4714` |
| Stealth | T1027.002 | Software Packing | the attack T1055.002 Process Injection: Portable Executable Injection Some of the malware implants had PE injection capability to load additional payloads T1027.002 Obfuscated Files or Information: Software Packing The malware samples were packed with VMProtect or Themida T1112 Modify Registry Various registry entries were modified to install persistence or change settings of security controls T1003.001 OS Credential Dumping: LSASS M |  |  | 不明 | 不明 | 中 | `source--lazarus--5dbd54be61ed2947` |
| Stealth | T1027.007 | Dynamic API Resolution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.009 | Embedded Payloads | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5cb141837fab1486`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Stealth | T1036.003 | Rename Legitimate Utilities | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5cb141837fab1486`, `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1037 | Boot or Logon Initialization Scripts | ERSISTENCE T1505.003 Server Software, Component - Web Shell Multiple Web Shells utilized. These have been listed and described in this report - PERSISTENCE T1037 .005 Boot or Logon Initialization Scripts - Startup Items Create a service which will run acres.exe automatically at startup sc create RegistryCheck type= own type= interact start= auto error= ignore binpath= "cmd /K start c:\ windows\temp\acres.exe" PERSISTENCE T1053.005 |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--3c464a6b801a4714`, `source--lazarus--5cb141837fab1486`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--mitre-attack-19-1` |
| Exfiltration | T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5cb141837fab1486`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5cb141837fab1486`, `source--lazarus--5dbd54be61ed2947`, `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--3c464a6b801a4714`, `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.002 | Portable Executable Injection | attack T1070.004 Indicator Removal on Host: File Deletion Malware samples and other forensic evidence was deleted across multiple hosts during the attack T1055.002 Process Injection: Portable Executable Injection Some of the malware implants had PE injection capability to load additional payloads T1027.002 Obfuscated Files or Information: Software Packing The malware samples were packed with VMProtect or Themida T1112 Modify Regist |  |  | 不明 | 不明 | 中 | `source--lazarus--5dbd54be61ed2947` |
| Collection, Credential Access | T1056.001 | Keylogging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5cb141837fab1486`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | ATION LIMITED” code signing certificate - INITIAL ACCESS T1190 Exploit Public Facing Application Compromise of CVE-2022-27925 and CVE-2022-37042 - EXECUTION T1059 Command and Scripting Interpreter Use of WMI and PowerShell to interact with host, interactive shells also used for manual execution of commands - EXECUTION T1569.002 System Services – Service Execution, S0357 Software - Impacket ‘atexec’ module of Impacket to proxy comman |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5dbd54be61ed2947`, `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5dbd54be61ed2947`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5dbd54be61ed2947`, `source--mitre-attack-19-1` |
| Execution, Stealth | T1064 | Scripting | e – Information is provided to the recipient only, and may not be distributed outside the initial exchange 13 \| P a g e Operation ‘Dream Job’ Scripting - T1064 User Execution: Malicious File – T1204.002 Visual Basic Macro code – Embedded in a DOC / DOTM file Tool Web Service – T1102 Communication with C2 Techniques User Execution: Malicious File – T1204.002 Exploitation for Client Execution – T1203 Modified Sumarta PDF |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Discovery | T1069.002 | Domain Groups | up parameters Discovery T1087.001 Account Discovery: Local Account The Lazarus Group collects information about users using the net user and net group commands T1069.002 Permission Groups Discovery: Domain Groups The Lazarus Group uses the adfind utility to retrieve information from Active Directory T1016 System Network Configuration Discovery The Lazarus Group collects information about the network settings of the infected computer T1135 Networ |  |  | 不明 | 不明 | 中 | `source--lazarus--09f2fa073008f6e1` |
| Stealth | T1070 | Indicator Removal | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1070.001 | MITRE ATT&CK T1070.001 | xecution: Security Support Provider The main malware implants were executed and persisted through being loaded as an security support provider in lsass.exe T1070.001 Indicator Removal on Host: Clear Windows Event Logs Event logs were manipulated and deleted across multiple hosts during the attack T1070.004 Indicator Removal on Host: File Deletion Malware samples and other forensic evidence was deleted across multiple hosts during the |  |  | 不明 | 不明 | 中 | `source--lazarus--5dbd54be61ed2947` |
| Uncategorized | T1070.002 | MITRE ATT&CK T1070.002 | tart Execution: Registry Run Keys / Startup Folder Privilege Escalation T1543.003 Create or Modify System Process: Windows Service Defense Evasion T1140 T1070.002 T1070.003 T1070.004 T1036.003 T1036.004 T1112 Deobfuscate/Decode Files or Information Clear Linux or Mac System Logs Clear Command History File Deletion Masquerading: Rename System Utilities Masquerading: Masquerade Task or Service Modify Reg |  |  | 不明 | 不明 | 中 | `source--lazarus--f6685ba8150b853c` |
| Stealth | T1070.003 | Clear Command History | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5cb141837fab1486`, `source--lazarus--5dbd54be61ed2947`, `source--lazarus--f6685ba8150b853c`, `source--lazarus--ff5ba7d73371b72f`, `source--mitre-attack-19-1` |
| Stealth | T1070.006 | Timestomp | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.007 | Clear Network Connection History and Configurations | Temp\[a-zA-Z]{8}.tmp 2>&1 Deletion of temporary files cmd.exe /C del /f /q /a c:\ windows\temp\*.tmp > C:\ Windows\Temp\[a-zA-Z]{8}. tmp 2>&1 DEFENSE EVASION T1070.007 Indicator Removal – Clear Network Connection History and Configurations "Microsoft-Windows-TerminalServices- RemoteConnectionManager/Admin" cleared by "support" account - deletion of RDP logs - PERSISTENCE T1136 Create Account Created accounts detailed in report - 18 Documen |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Command And Control | T1071 | Application Layer Protocol | %TEMP%\temp\netstat.res COMMAND AND CONTROL S0154 Software – Cobalt Strike Communication with two known Cobalt Strike hosts observed - COMMAND AND CONTROL T1071 Application Layer Protocol Secure Shell protocol used - COMMAND AND CONTROL T1090.002 Proxy - External Proxy C2 behavior suggests a small number of C2 servers connecting via multiple relays/endpoints. Some C2 servers appear to themselves be compromised victims - COMMAND AN |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--3c464a6b801a4714`, `source--lazarus--5cb141837fab1486`, `source--lazarus--5dbd54be61ed2947`, `source--lazarus--f6685ba8150b853c`, `source--lazarus--ff5ba7d73371b72f`, `source--mitre-attack-19-1` |
| Collection | T1074 | Data Staged | ionality of DTrack info stealer , which adds data to a password protected archive file then moves the file to a hardcoded internal staging point - COLLECTION T1074 Data staged locally on devices in archive files, in some cases those archives were then moved to an internal staging point. - COLLECTION T1119 DTrack automatically gathers data on the local system using legitimate windows commands such as systeminfo, netstat and tasklist. cm |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Collection | T1074.001 | Local Data Staging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5cb141837fab1486`, `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | Mitre ATT&CK Techniques ID Name Description T1566.003 Phishing: Spearphishing via Service A malicious document was sent via LinkedIn to a target employee T1078.002 Valid Accounts Various domain accounts were used to execute commands and laterally move around the target network T1218.005 Signed Binary Proxy Execution: Mshta A malicious mshta command was executed as a result of the phishing document being interacted with T1059.001 Comm |  |  | 不明 | 不明 | 中 | `source--lazarus--5dbd54be61ed2947` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5cb141837fab1486`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5cb141837fab1486`, `source--lazarus--5dbd54be61ed2947`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Discovery | T1087 | Account Discovery | Display the folder structure of the d: drive and pipe output to the temp folder cmd.exe /C cd d:\ & tree d: > C:\Windows\Temp\[a-zA-Z] {8}.tmp 2>&1 DISCOVERY T1087 .002 Account Discovery - Domain Account Querying members of the Domain Admins group with the built in Windows net command. As well as net group, the threat actor used net user and net share to gather information cmd.exe /C net group / domain Domain Admins" > C:\Windows\Tem |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Discovery | T1087.001 | Local Account | Binary Proxy Execution: Rundll32 A malicious DLL is launched via rundll32.exe with an indication of the exported function and with startup parameters Discovery T1087.001 Account Discovery: Local Account The Lazarus Group collects information about users using the net user and net group commands T1069.002 Permission Groups Discovery: Domain Groups The Lazarus Group uses the adfind utility to retrieve information from Active Directory T1016 System |  |  | 不明 | 不明 | 中 | `source--lazarus--09f2fa073008f6e1` |
| Command And Control | T1090.001 | Internal Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5cb141837fab1486`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Command And Control | T1090.002 | External Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5cb141837fab1486`, `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098 | Account Manipulation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | ion ‘Dream Job’ Scripting - T1064 User Execution: Malicious File – T1204.002 Visual Basic Macro code – Embedded in a DOC / DOTM file Tool Web Service – T1102 Communication with C2 Techniques User Execution: Malicious File – T1204.002 Exploitation for Client Execution – T1203 Modified Sumarta PDF reader Tool Hijack Execution Flow: DLL Search Order Hijacking – T1574.001 DBLL Dropper Tool Hide Artifacts: Hidden Files and |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Command And Control | T1102.002 | Bidirectional Communication | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1104 | Multi-Stage Channels | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5cb141837fab1486`, `source--mitre-attack-19-1` |
| Credential Access | T1110.003 | Password Spraying | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | alation T1543.003 Create or Modify System Process: Windows Service Defense Evasion T1140 T1070.002 T1070.003 T1070.004 T1036.003 T1036.004 T1112 Deobfuscate/Decode Files or Information Clear Linux or Mac System Logs Clear Command History File Deletion Masquerading: Rename System Utilities Masquerading: Masquerade Task or Service Modify Registry Credential Access T1557.001 LLMNR/NBT-NS Poisoning and S |  |  | 不明 | 不明 | 中 | `source--lazarus--5dbd54be61ed2947`, `source--lazarus--f6685ba8150b853c` |
| Collection | T1114.002 | Remote Email Collection | ollowing compromise - base.jsp - Second webshell installed by actors - skin.dat - Webshell on Zimbra server , used for initial exfiltration of data COLLECTION T1114.002 Used pre-existing mailbox backup script on Zimbra mail server to copy all emails to a single file, then exfiltrated the file - COLLECTION T1560 Creation of skin.dat data dump archive and functionality of DTrack info stealer , which adds data to a password protected archive f |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Collection | T1119 | Automated Collection | ly on execution. T1497.003 Virtualization/Sandbox Evasion: Time Based Evasion Smooth Operator sleeps for, at minimum, a week before beaconing. Collection T1119 Automated Collection Smooth Operator stages collect data from the victim machine to be included in a beacon or exfiltration. Command and Control T1071.001 Application Layer Protocol: Web Protocols Smooth Operator command and control is over HTTPS. T1008 Fallback Channe |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486`, `source--lazarus--ff5ba7d73371b72f` |
| Discovery | T1124 | System Time Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.002 | Non-Standard Encoding | emote Services: SMB/Windows Admin Shares The Lazarus Group uses compromised legitimate privileged accounts to move laterally on the network Command And Control T1132.002 Data Encoding: Non-Standard Encoding The Lazarus Group uses its own data encryption algorithm to communicate with the C2 T1071.001 Application Layer Protocol: Web Protocols The Lazarus Group's malware uses the standard HTTP protocol to connect to the C2 10. IOCs File name MD5 SH |  |  | 不明 | 不明 | 中 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--f6685ba8150b853c` |
| Privilege Escalation, Stealth | T1134.002 | Create Process with Token | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | n from Active Directory T1016 System Network Configuration Discovery The Lazarus Group collects information about the network settings of the infected computer T1135 Network Share Discovery The Lazarus Group uses the SMBMap utility to discover shared folders within the network T1012 Query Registry The Lazarus Group uses the reg.exe utility to get information from the registry T1033 System Owner/User Discovery The Lazarus Group collects infor |  |  | 不明 | 不明 | 中 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--f6685ba8150b853c` |
| Persistence | T1136 | Create Account | rsistence T1543.003 Create or Modify System Process: Windows Service To gain persistence on a host, the Lazarus Group creates services using the sc.exe utility T1136 Create Account The Lazarus Group creates local administrator accounts T1547.009 Boot or Logon Autostart Execution: Shortcut Modification To gain persistence on a host, the Lazarus Group places a shortcut in the startup folder Defense Evasion T1027 Obfuscated Files or Information |  |  | 不明 | 不明 | 中 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5cb141837fab1486` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--f6685ba8150b853c`, `source--lazarus--ff5ba7d73371b72f`, `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | Signing Certificates Several binaries deployed by the threat actor were signed with a “LAMERA CORPORATION LIMITED” code signing certificate - INITIAL ACCESS T1190 Exploit Public Facing Application Compromise of CVE-2022-27925 and CVE-2022-37042 - EXECUTION T1059 Command and Scripting Interpreter Use of WMI and PowerShell to interact with host, interactive shells also used for manual execution of commands - EXECUTION T1569.002 System |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Initial Access | T1195.001 | Compromise Software Dependencies and Development Tools | k, a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. Tactic ID Technique Procedure Initial Access T1195.001 Supply Chain Compromise: Compromise Software Dependencies and Development Tools Smooth Operator is distributed via legitimate channels as trojanised, signed and notarized 3CX software. Persistence T1554 Compromise Client Software Binary Smooth Operator runs as part of |  |  | 不明 | 不明 | 中 | `source--lazarus--ff5ba7d73371b72f` |
| Stealth | T1202 | Indirect Command Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--3c464a6b801a4714`, `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--3c464a6b801a4714`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Stealth | T1218 | System Binary Proxy Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5dbd54be61ed2947`, `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | ifacts: Hidden Files and Directories – T1564 Boot or Logon AutoStart Execution: Shortcut Modification – T1547.009 LNK file Tool Remote Access Software – T1219 Similarity with Bankshot – S0239 RATzarus Tool Remote Access Software – T1219 Credentials from Password Stores: Credentials from Web Browsers - T1555.003 Open source tools such as Wake-On-Lan, Responder.py and ChromePass Tool |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Stealth | T1221 | Template Injection | Virtualization/Sandbox Evasion: System Checks – T1497 Anti VM Technique + Tool Exploitation Exfiltration Over C2 Channel – T1041 Template Injection – T1221 Template injection - downloading files from C2 Tool |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Uncategorized | T1268 | MITRE ATT&CK T1268 | rocedures Kill Chain Phase Build social network persona – T1341 Social media impersonation – LinkedIn Technique Intrusion Conduct social engineering – T1268 User Execution: Malicious File – T1204.002 Social engineering methods – communication with the victim, phone calls, WhatsApp’s conversations Technique Phishing: Spear phishing Attachment – T1566.001 Spear phishing Technique Adversary OPSEC – TA0021 Acquire and/or |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Uncategorized | T1308 | MITRE ATT&CK T1308 | nique Phishing: Spear phishing Attachment – T1566.001 Spear phishing Technique Adversary OPSEC – TA0021 Acquire and/or use 3rd party software services – T1308 Using file hosting services like DropBox and OneDrive Procedures Obfuscated Files or Information - T1027 Sending decoy file Technique Data Compressed –T1002 Archives (WinRAR or 7- ZIP) Procedures Virtualization/Sandbox Evasion: System Checks – T1497 Anti VM Techniq |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Uncategorized | T1341 | MITRE ATT&CK T1341 | mpaign and those used by the Lazarus espionage group. MITRE ATT&CK Title Techniques, Tools and Procedures Kill Chain Phase Build social network persona – T1341 Social media impersonation – LinkedIn Technique Intrusion Conduct social engineering – T1268 User Execution: Malicious File – T1204.002 Social engineering methods – communication with the victim, phone calls, WhatsApp’s conversations Technique Phishing: Spear phi |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Impact | T1485 | Data Destruction | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1489 | Service Stop | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1491.001 | Internal Defacement | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | ation - T1027 Sending decoy file Technique Data Compressed –T1002 Archives (WinRAR or 7- ZIP) Procedures Virtualization/Sandbox Evasion: System Checks – T1497 Anti VM Technique + Tool Exploitation Exfiltration Over C2 Channel – T1041 Template Injection – T1221 Template injection - downloading files from C2 Tool |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Discovery, Stealth | T1497.003 | Time Based Checks | s well as tasking responses. T1070.004 Indicator Removal: File Deletion Smooth Operator’s second-stage deletes itself from disk immediately on execution. T1497.003 Virtualization/Sandbox Evasion: Time Based Evasion Smooth Operator sleeps for, at minimum, a week before beaconing. Collection T1119 Automated Collection Smooth Operator stages collect data from the victim machine to be included in a beacon or exfiltration. Command and |  |  | 不明 | 不明 | 中 | `source--lazarus--ff5ba7d73371b72f` |
| Persistence | T1505.003 | Web Shell | - Impacket ‘atexec’ module of Impacket to proxy command execution on hosts - EXECUTION T1106 Native API Use of WinExec API to execute commands - PERSISTENCE T1505.003 Server Software, Component - Web Shell Multiple Web Shells utilized. These have been listed and described in this report - PERSISTENCE T1037 .005 Boot or Logon Initialization Scripts - Startup Items Create a service which will run acres.exe automatically at startup sc cr |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Impact | T1529 | System Shutdown/Reboot | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Stealth | T1542.003 | Bootkit | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--3c464a6b801a4714`, `source--lazarus--5dbd54be61ed2947`, `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.005 | Security Support Provider | istence during the attack T1053.005 Scheduled Task/Job: Scheduled Task Scheduled tasks were primarily used to remotely install persistence on target hosts T1547.005 Boot or Logon Autostart Execution: Security Support Provider The main malware implants were executed and persisted through being loaded as an security support provider in lsass.exe T1070.001 Indicator Removal on Host: Clear Windows Event Logs Event logs were manipulated a |  |  | 不明 | 不明 | 中 | `source--lazarus--5dbd54be61ed2947` |
| Persistence, Privilege Escalation | T1547.009 | Shortcut Modification | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--3c464a6b801a4714`, `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | ersistence or change settings of security controls T1003.001 OS Credential Dumping: LSASS Memory Mimikatz was used to dump credentials out of LSASS memory T1552.001 Unsecured Credentials: Credentials In Files Credentials were accessed from text files on user desktops to access and bypass certain controls T1021.001 Remote Services: Remote Desktop Protocol RDP was used to laterally move around the target network using valid accounts T |  |  | 不明 | 不明 | 中 | `source--lazarus--5dbd54be61ed2947` |
| Defense Impairment | T1553 | Subvert Trust Controls | ame or Location Listed files on the Zimbra server were named to match a pre-existing, legitimate directory within the same parent directory DEFENSE EVASION T1553 Subvert Trust Controls – Code Signing Several binaries deployed by the threat actor were signed with a “LAMERA CORPORATION LIMITED” code signing certificate - DEFENSE EVASION T1070.004 Indicator Removal – File Deletion Deletion of temporary files cmd.exe /C net use \[Intern |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Defense Impairment | T1553.002 | Code Signing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1554 | Compromise Host Software Binary | e Dependencies and Development Tools Smooth Operator is distributed via legitimate channels as trojanised, signed and notarized 3CX software. Persistence T1554 Compromise Client Software Binary Smooth Operator runs as part of the 3CX software. Defence Evasion T1140 Deobfuscate/Decode Files or Information Smooth Operator uses a custom algorithm to obfuscate data exfiltrated over the C2 channel. Smooth Operator deobfuscates da |  |  | 不明 | 不明 | 中 | `source--lazarus--ff5ba7d73371b72f` |
| Credential Access | T1555.003 | Credentials from Web Browsers | e – T1219 Similarity with Bankshot – S0239 RATzarus Tool Remote Access Software – T1219 Credentials from Password Stores: Credentials from Web Browsers - T1555.003 Open source tools such as Wake-On-Lan, Responder.py and ChromePass Tool |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Credential Access, Defense Impairment, Persistence | T1556 | Modify Authentication Process | an then be moved elsewhere for hashes to be extracted using Mimikatz C:\windows\temp\mmc. dat full > C:\Windows\ Temp\[a-zA-Z]{8}.tmp 2>&1 CREDENTIAL ACCESS T1556 Modify Authentication Process /opt/zimbra/jetty_base/webapps/zimbra/public/ login.jsp File modified to log credentials to text file at /opt/zimbra/jetty_base/webapps/zimbra/public/ temp/zlog.txt - Configure device to store credentials in memory , making it pos-sible to extrac |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Collection, Credential Access | T1557.001 | Name Resolution Poisoning and SMB Relay | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Collection | T1560 | Archive Collected Data | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--5cb141837fab1486`, `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | LAZARUS TARGETS DEFENSE INDUSTRY WITH THREATNEEDLE 24 © 2021 AO KASPERSKY LAB Lateral Movement T1021.002 SMB/Windows Admin Shares Collection T1560.001 Archive Collected Data: Archive via Utility Command and Control T1071.001 T1132.002 T1104 T1572 T1090.001 Application Layer Protocol: Web Protocols Non-Standard Encoding Multi-Stage Channels Protocol Tunneling Internal Proxy Exfiltration T1041 E |  |  | 不明 | 不明 | 中 | `source--lazarus--f6685ba8150b853c` |
| Collection | T1560.002 | Archive via Library | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.003 | Archive via Custom Method | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--3c464a6b801a4714`, `source--mitre-attack-19-1` |
| Impact | T1561.001 | Disk Content Wipe | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1561.002 | Disk Structure Wipe | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564 | Hide Artifacts | d Sumarta PDF reader Tool Hijack Execution Flow: DLL Search Order Hijacking – T1574.001 DBLL Dropper Tool Hide Artifacts: Hidden Files and Directories – T1564 Boot or Logon AutoStart Execution: Shortcut Modification – T1547.009 LNK file Tool Remote Access Software – T1219 Similarity with Bankshot – S0239 RATzarus Tool Remote Access Software – T1219 Credentials from Password Stores: Credentials from Web Browsers - T1555.003 |  |  | 不明 | 不明 | 中 | `source--lazarus--3c464a6b801a4714` |
| Stealth | T1564.001 | Hidden Files and Directories | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--3c464a6b801a4714`, `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--3c464a6b801a4714`, `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--f6685ba8150b853c`, `source--mitre-attack-19-1` |
| Initial Access | T1566.003 | Spearphishing via Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--09f2fa073008f6e1`, `source--lazarus--5dbd54be61ed2947`, `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | Command and Scripting Interpreter Use of WMI and PowerShell to interact with host, interactive shells also used for manual execution of commands - EXECUTION T1569.002 System Services – Service Execution, S0357 Software - Impacket ‘atexec’ module of Impacket to proxy command execution on hosts - EXECUTION T1106 Native API Use of WinExec API to execute commands - PERSISTENCE T1505.003 Server Software, Component - Web Shell Multiple Web S |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486`, `source--lazarus--f6685ba8150b853c` |
| Command And Control | T1571 | Non-Standard Port | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | 021.002 SMB/Windows Admin Shares Collection T1560.001 Archive Collected Data: Archive via Utility Command and Control T1071.001 T1132.002 T1104 T1572 T1090.001 Application Layer Protocol: Web Protocols Non-Standard Encoding Multi-Stage Channels Protocol Tunneling Internal Proxy Exfiltration T1041 Exfiltration Over C2 Channel |  |  | 不明 | 不明 | 中 | `source--lazarus--f6685ba8150b853c` |
| Command And Control | T1573.001 | Symmetric Cryptography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--lazarus--3c464a6b801a4714`, `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.013 | KernelCallbackTable | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.004 | Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587 | Develop Capabilities | TTP Summary Tactic Technique Description Activity RESOURCE DEVELOPMENT T1587 .002 Code Signing Certificates Several binaries deployed by the threat actor were signed with a “LAMERA CORPORATION LIMITED” code signing certificate - INITIAL ACCESS T1190 Exploit Public Facing Application Compromise of CVE-2022-27925 and CVE-2022-37042 - EXECUTION T1059 C |  |  | 不明 | 不明 | 中 | `source--lazarus--5cb141837fab1486` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.004 | Digital Certificates | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591 | Gather Victim Org Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1620 | Reflective Code Loading | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1680 | Local Storage Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686.003 | Windows Host Firewall | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1358件
- IOC観測: 1599件
- 複数攻撃で観測: 5件
- 要レビュー候補: 441件
- 非IOC artifact観測: 1139件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| MITRE considers Andariel a subset of Lazarus Group; U.S. Treasury also describes Andariel as a Lazarus subgroup controlled by the RGB. | 高 | `source--mitre-live-andariel-2024`, `source--treasury-dprk-groups-2019` | verification_status=supported; Lazarus is also used as a broad umbrella label in some reporting, so operation-level attribution should retain the Andariel label where supported. The sources warn that DPRK cluster boundaries overlap; subgroup status does not imply identical tooling across all Lazarus activity. |
| Government sources connect Bluenoroff/APT38 and Lazarus under the RGB and a common conspiracy, while industry reporting preserves APT38 as a financially focused cluster. | 高 | `source--treasury-dprk-groups-2019`, `source--doj-dprk-conspiracy-2021` | verification_status=partially-supported; APT38, Bluenoroff, and Lazarus have vendor-dependent scopes; exact equivalence should not be asserted. The DOJ's common-conspiracy framing is organizational/legal and does not prove identical operational clustering. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-e91cff6491073bc4c828 | Lazarus GroupがGit Hooksを使ってマルウェアを隠蔽 | opensourcemalware.com | 2026-05-13 | https://opensourcemalware.com/blog/dprk-git-hooks-malware | osint-report | TLP:CLEAR | 中 |
| source--doj-dprk-conspiracy-2021 | Three North Korean Military Hackers Indicted in Wide-Ranging Scheme | U.S. Department of Justice | 2021-02-17 | https://www.justice.gov/archives/opa/pr/three-north-korean-military-hackers-indicted-wide-ranging-scheme-commit-cyberattacks-and | government-legal-announcement | TLP:CLEAR | 高 |
| source--lazarus--09f2fa073008f6e1 | Lazarus Group Recruitment  Threat Hunters vs Head Hunters |  | 不明 | lazarus/Lazarus Group Recruitment_ Threat Hunters vs Head Hunters.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--344872736951fe87 | The Lazarus Constellation |  | 不明 | lazarus/The_Lazarus_Constellation.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--359aa58eb2a1e6b4 | uscert |  | 不明 | lazarus/uscert.txt | text-data | TLP:CLEAR | 中 |
| source--lazarus--3c464a6b801a4714 | Dream Job Campaign |  | 不明 | lazarus/Dream-Job-Campaign.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--5b1c7d47526d5157 | 20231013 Lazarus OP.Dream Magic |  | 2023-10-13 | lazarus/20231013_Lazarus_OP.Dream_Magic.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--5b95fa78159c9c68 | README |  | 不明 | lazarus/3CXSupplyChain/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--lazarus--5cb141837fab1486 | WithSecure Lazarus No Pineapple Threat Intelligence Report 2023 |  | 2023 | lazarus/WithSecure-Lazarus-No-Pineapple-Threat-Intelligence-Report-2023.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--5dbd54be61ed2947 | lazarus threat intel report2 |  | 不明 | lazarus/lazarus-threat-intel-report2.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--7c567ac63290b31d | readme |  | 不明 | lazarus/fudmodule/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--lazarus--8a3370396148b3b6 | C2 Communication of ThreatNeedle |  | 不明 | lazarus/C2_Communication_of_ThreatNeedle.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--8d1165d6beead3f1 | README |  | 不明 | lazarus/sample/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--lazarus--8d4e53b5d503643d | readme |  | 不明 | lazarus/Andariel/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--lazarus--962cd7ac434e73dc | The Nightmare of Global Cryptocurrency Companies DangerousPassword of the APT Organization |  | 不明 | lazarus/The Nightmare of Global Cryptocurrency Companies DangerousPassword of the APT Organization.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--9e1ae3ccdafbc023 | multiple campaigns of the Lazarus group and their connections |  | 不明 | lazarus/multiple campaigns of the Lazarus group and their connections.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--a1bebb55574a6a4f | VB2022 Lazarus and BYOVD evil to the Windows core |  | 2022 | lazarus/fudmodule/VB2022-Lazarus-and-BYOVD-evil-to-the-Windows-core.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--a533f6aafc93c41e | Analysis Report on Lazarus Groups Rootkit Attack Using BYOVD Sep 22 2022 |  | 2022 | lazarus/fudmodule/Analysis-Report-on-Lazarus-Groups-Rootkit-Attack-Using-BYOVD_Sep-22-2022.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--ac9aba9cb92fd0a4 | README |  | 不明 | lazarus/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--lazarus--af801ed889f0a493 | WithSecure Andariel 2025 |  | 2025 | lazarus/Andariel/WithSecure_Andariel_2025.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--bbedb175d650814c | CryptoCore Lazarus Clearsky |  | 不明 | lazarus/CryptoCore-Lazarus-Clearsky.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--bc30b9b90499e90d | Operation Blockbuster Report |  | 不明 | lazarus/Operation-Blockbuster-Report.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--c328e6a5abab4da3 | Updated MATA attacks Eastern Europe full report ENG |  | 不明 | lazarus/MATA/Updated-MATA-attacks-Eastern-Europe_full-report_ENG.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--d2f4388a1f1d2f60 | Operation Marstech Mayhem Report 021025 03 |  | 不明 | lazarus/Operation-Marstech-Mayhem-Report_021025_03.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--d5a205340378d346 | 2024 10 14 Lazarus InvisibleFerret |  | 2024-10-14 | lazarus/2024-10-14 Lazarus InvisibleFerret.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--d972bdf63d7812e9 | Asia 24 Camastra FromBYOVDtoa0dayUnveilingAdvancedExploitsinCyberRecruitingScams |  | 不明 | lazarus/fudmodule/Asia-24-Camastra-FromBYOVDtoa0dayUnveilingAdvancedExploitsinCyberRecruitingScams.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--e8bdd16ec6041a6c | readme |  | 不明 | lazarus/MATA/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--lazarus--f6685ba8150b853c | kaspersky ics cert lazarus targets defense industry with threatneedle en 20210225 |  | 2021-02-25 | lazarus/kaspersky-ics-cert-lazarus-targets-defense-industry-with-threatneedle-en-20210225.pdf | report | TLP:CLEAR | 中 |
| source--lazarus--ff5ba7d73371b72f | NCSC MAR Smooth Operator |  | 不明 | lazarus/3CXSupplyChain/NCSC_MAR-Smooth-Operator.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-live-andariel-2024 | Andariel, Group G0138 | MITRE ATT&CK | 2024-09-12 | https://attack.mitre.org/groups/G0138/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--treasury-dprk-groups-2019 | Treasury Sanctions North Korean State-Sponsored Malicious Cyber Groups | U.S. Department of the Treasury | 2019-09-13 | https://home.treasury.gov/news/press-releases/sm774 | government-designation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
