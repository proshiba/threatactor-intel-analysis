# Sandworm Team 脅威アクタープロファイル

- プロファイルID: `actor--sandworm`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Sandworm Teamの標準化プロファイル。リポジトリ内の専用資料15件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Sandworm Team**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT44 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| BlackEnergy (Group) | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ELECTRUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| FROZENBARENTS | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| IRIDIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| IRON VIKING | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Quedagh | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Seashell Blizzard | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Telebots | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Voodoo Bear | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| APT28 | cooperates-with | Some Sandworm/GRU Unit 74455 operations were conducted with assistance from APT28/GRU Unit 26165. | 高 | `source--mitre-live-sandworm-2024` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Sandworm Team](https://attack.mitre.org/groups/G0034) is a destructive threat group that has been attributed to Russia's General Staff Main Intelligence Directorate (GRU) Main Center for Special Technologies (GTsST) military unit 74455.(Citation: US District Court Indictment GRU Unit 74455 October 2020)(Citation: UK NCSC Olympic Attacks October 2020) This group has been active since at least 2009.(Citation: iSIGHT Sandworm 2014)(Citation: CrowdStrike VOODOO BEAR)(Citation: USDOJ Sandworm Feb 2020)(Citation: NCSC Sandworm Feb 2020)<br><br>In October 2020, the US indicted six GRU Unit 74455 officers associated with [Sandworm Team](https://attack.mitre.org/groups/G0034) for the following cyber operations: the 2015 and 2016 attacks against Ukrainian electrical companies and government organizations, the 2017 worldwide [NotPetya](https://attack.mitre.org/software/S0368) attack, targeting of the 2017 French presidential campaign, the 2018 [Olympic Destroyer](https://attack.mitre.org/software/S0365) attack against the Winter Olympic Games, the 2018 operation against the Organisation for the Prohibition of Chemical Weapons, and attacks against the country of Georgia in 2018 and 2019.(Citation: US District Court Indictment GRU Unit 74455 October 2020)(Citation: UK NCSC Olympic Attacks October 2020) Some of these were conducted with the assistance of GRU Unit 26165, which is also referred to as [APT28](https://attack.mitre.org/groups/G0007).(Citation: US District Court Indictment GRU Oct 2018) |
| Capability | AcidRain, Exaramel for Windows, Exaramel for Linux, Prestige, Bad Rabbit, GreyEnergy, Olympic Destroyer, P.A.S. Webshell, AcidPour, BlackEnergy, NotPetya, VPNFilter, Industroyer2, Kapeka, Cobalt Strike, Cyclops Blink, Neo-reGeorg, KillDisk, Industroyer, Net, Impacket, Empire, PoshC2, Mimikatz, Invoke-PSImage, SDelete, PsExec |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Energetic Bear, Dragonfly | single-alias-intersection | 中 | Russia | https://www.symantec.com/blogs/threat-intelligence/dragonfly-energy-sector-cyber-attacks<br>https://www.kaspersky.com/resource-center/threats/crouching-yeti-energetic-bear-malware-threat<br>https://www.sans.org/reading-room/whitepapers/ICS/impact-dragonfly-malware-industrial-control-systems-36672 |
| etda-threat-group-cards | Iridium | single-alias-intersection | 中 | Iran | https://hub.packtpub.com/resecurity-reports-iriduim-behind-citrix-data-breach-200-government-agencies-oil-and-gas-companies-and-technology-companies-also-targeted/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Iridium&n=1 |
| etda-threat-group-cards | Sandworm Team, Iron Viking, Voodoo Bear | canonical-name | 高 | Russia | https://blog.trendmicro.com/trendlabs-security-intelligence/timeline-of-sandworm-attacks/<br>https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-january-voodoo-bear/<br>https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/ |
| etda-threat-group-cards | TeleBots | single-alias-intersection | 中 | Russia | https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/<br>https://blog.trendmicro.com/trendlabs-security-intelligence/timeline-of-sandworm-attacks/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=TeleBots&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Seashell Blizzard | multiple-name-intersection | 高 | Russia | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Sandworm | multiple-name-intersection | 高 | RU, Russian Federation | https://dragos.com/blog/crashoverride/CrashOverride-01.pdf<br>https://www.us-cert.gov/ncas/alerts/TA17-163A<br>https://ics.sans.org/blog/2016/01/09/confirmation-of-a-coordinated-attack-on-the-ukrainian-power-grid |
| misp-threat-actor | IRIDIUM | single-alias-intersection | 中 | IR | https://www.nbcnews.com/politics/national-security/iranian-backed-hackers-stole-data-major-u-s-government-contractor-n980986<br>https://threatpost.com/ranian-apt-6tb-data-citrix/142688/<br>https://hub.packtpub.com/resecurity-reports-iriduim-behind-citrix-data-breach-200-government-agencies-oil-and-gas-companies-and-technology-companies-also-targeted/ |
| misp-microsoft-activity-group | Seashell Blizzard | multiple-name-intersection | 高 | RU, Russia | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Sandworm Team - G0034 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0034<br>https://www.fireeye.com/blog/threat-research/2016/01/ukraine-and-sandworm-team.html |
| misp-mitre-intrusion-set | Sandworm Team - G0034 | mitre-external-id | 高 |  | https://2017-2021.state.gov/the-united-states-condemns-russian-cyber-attack-against-the-country-of-georgia/index.html<br>https://attack.mitre.org/groups/G0034<br>https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| GreyEnergy | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--acidrain | AcidRain | [AcidRain](https://attack.mitre.org/software/S1125) is an ELF binary targeting modems and routers using MIPS architecture.(Citation: AcidRain JAGS 2022) [AcidRain](https://attack.mitre.org/software/S1125) is associated with the ViaSat KA-SAT communication outage that took place during the initial phases of the 2022 full-scale invasion of Ukraine. Analysis indicates overlap with another network device-targeting malware, VPNFilter, associated with [Sandworm Team](https://attack.mitre.org/groups/G0034).(Citation: AcidRain JAGS 2022) US and European government sources linked [AcidRain](https://attack.mitre.org/software/S1125) to Russian government entities, while Ukrainian government sources linked [AcidRain](https://attack.mitre.org/software/S1125) specifically to [Sandworm Team](https://attack.mitre.org/groups/G0034).(Citation: AcidRain State Department 2022)(Citation: Vincens AcidPour 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--exaramel-for-windows | Exaramel for Windows | [Exaramel for Windows](https://attack.mitre.org/software/S0343) is a backdoor used for targeting Windows systems. The Linux version is tracked separately under [Exaramel for Linux](https://attack.mitre.org/software/S0401).(Citation: ESET TeleBots Oct 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--exaramel-for-linux | Exaramel for Linux | [Exaramel for Linux](https://attack.mitre.org/software/S0401) is a backdoor written in the Go Programming Language and compiled as a 64-bit ELF binary. The Windows version is tracked separately under [Exaramel for Windows](https://attack.mitre.org/software/S0343).(Citation: ESET TeleBots Oct 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--prestige | Prestige | [Prestige](https://attack.mitre.org/software/S1058) ransomware has been used by [Sandworm Team](https://attack.mitre.org/groups/G0034) since at least March 2022, including against transportation and related logistics industries in Ukraine and Poland in October 2022.(Citation: Microsoft Prestige ransomware October 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--bad-rabbit | Bad Rabbit | [Bad Rabbit](https://attack.mitre.org/software/S0606) is a self-propagating ransomware that affected the Ukrainian transportation sector in 2017. [Bad Rabbit](https://attack.mitre.org/software/S0606) has also targeted organizations and consumers in Russia. (Citation: Secure List Bad Rabbit)(Citation: ESET Bad Rabbit)(Citation: Dragos Apr 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--greyenergy | GreyEnergy | [GreyEnergy](https://attack.mitre.org/software/S0342) is a backdoor written in C and compiled in Visual Studio. [GreyEnergy](https://attack.mitre.org/software/S0342) shares similarities with the [BlackEnergy](https://attack.mitre.org/software/S0089) malware and is thought to be the successor of it.(Citation: ESET GreyEnergy Oct 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--olympic-destroyer | Olympic Destroyer | [Olympic Destroyer](https://attack.mitre.org/software/S0365) is malware that was used by [Sandworm Team](https://attack.mitre.org/groups/G0034) against the 2018 Winter Olympics, held in Pyeongchang, South Korea. The main purpose of the malware was to render infected computer systems inoperable. The malware leverages various native Windows utilities and API calls to carry out its destructive tasks. [Olympic Destroyer](https://attack.mitre.org/software/S0365) has worm-like features to spread itself across a computer network in order to maximize its destructive impact.(Citation: Talos Olympic Destroyer 2018)(Citation: US District Court Indictment GRU Unit 74455 October 2020)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--p-a-s-webshell | P.A.S. Webshell | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) is a publicly available multifunctional PHP webshell in use since at least 2016 that provides remote access and execution on target web servers.(Citation: ANSSI Sandworm January 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--acidpour | AcidPour | [AcidPour](https://attack.mitre.org/software/S1167) is a variant of [AcidRain](https://attack.mitre.org/software/S1125) designed to impact a wider range of x86 architecture Linux devices. [AcidPour](https://attack.mitre.org/software/S1167) is an x86 ELF binary that expands on the targeted devices and locations in [AcidRain](https://attack.mitre.org/software/S1125) by including items such as Unsorted Block Image (UBI), Deice Mapper (DM), and various flash memory references. Based on this expanded targeting, [AcidPour](https://attack.mitre.org/software/S1167) can impact a variety of device types including IoT, networking, and ICS embedded device types.(Citation: SentinelOne AcidPour 2024) [AcidPour](https://attack.mitre.org/software/S1167) is a wiping payload associated with the [Sandworm Team](https://attack.mitre.org/groups/G0034) threat actor, and potentially linked to attacks against Ukrainian internet service providers (ISPs) in 2023.(Citation: CERT-UA TelecomAttack 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--blackenergy | BlackEnergy | [BlackEnergy](https://attack.mitre.org/software/S0089) is a malware toolkit that has been used by both criminal and APT actors. It dates back to at least 2007 and was originally designed to create botnets for use in conducting Distributed Denial of Service (DDoS) attacks, but its use has evolved to support various plug-ins. It is well known for being used during the confrontation between Georgia and Russia in 2008, as well as in targeting Ukrainian institutions. Variants include BlackEnergy 2 and BlackEnergy 3. (Citation: F-Secure BlackEnergy 2014) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--notpetya | NotPetya | [NotPetya](https://attack.mitre.org/software/S0368) is malware that was used by [Sandworm Team](https://attack.mitre.org/groups/G0034) in a worldwide attack starting on June 27, 2017. While [NotPetya](https://attack.mitre.org/software/S0368) appears as a form of ransomware, its main purpose was to destroy data and disk structures on compromised systems; the attackers never intended to make the encrypted data recoverable. As such, [NotPetya](https://attack.mitre.org/software/S0368) may be more appropriately thought of as a form of wiper malware. [NotPetya](https://attack.mitre.org/software/S0368) contains worm-like features to spread itself across a computer network using the SMBv1 exploits EternalBlue and EternalRomance.(Citation: Talos Nyetya June 2017)(Citation: US-CERT NotPetya 2017)(Citation: ESET Telebots June 2017)(Citation: US District Court Indictment GRU Unit 74455 October 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--vpnfilter | VPNFilter | [VPNFilter](https://attack.mitre.org/software/S1010) is a multi-stage, modular platform with versatile capabilities to support both intelligence-collection and destructive cyber attack operations. [VPNFilter](https://attack.mitre.org/software/S1010) modules such as its packet sniffer ('ps') can collect traffic that passes through an infected device, allowing the theft of website credentials and monitoring of Modbus SCADA protocols. (Citation: William Largent June 2018) (Citation: Carl Hurd March 2019) [VPNFilter](https://attack.mitre.org/software/S1010) was assessed to be replaced by [Sandworm Team](https://attack.mitre.org/groups/G0034) with [Cyclops Blink](https://attack.mitre.org/software/S0687) starting in 2019.(Citation: NCSC CISA Cyclops Blink Advisory February 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--industroyer2 | Industroyer2 | [Industroyer2](https://attack.mitre.org/software/S1072) is a compiled and static piece of malware that has the ability to communicate over the IEC-104 protocol. It is similar to the IEC-104 module found in [Industroyer](https://attack.mitre.org/software/S0604). Security researchers assess that [Industroyer2](https://attack.mitre.org/software/S1072) was designed to cause impact to high-voltage electrical substations. The initial [Industroyer2](https://attack.mitre.org/software/S1072) sample was compiled on 03/23/2022 and scheduled to execute on 04/08/2022, however it was discovered before deploying, resulting in no impact.(Citation: Industroyer2 Blackhat ESET) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--kapeka | Kapeka | Kapeka is a backdoor written in C++ used against victims in Eastern Europe since at least mid-2022. Kapeka has technical overlaps with [Exaramel for Windows](https://attack.mitre.org/software/S0343) and [Prestige](https://attack.mitre.org/software/S1058) malware variants, both of which are linked to [Sandworm Team](https://attack.mitre.org/groups/G0034). Kapeka may have been used in advance of [Prestige](https://attack.mitre.org/software/S1058) deployment in late 2022.(Citation: WithSecure Kapeka 2024)(Citation: Microsoft KnuckleTouch 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cyclops-blink | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) is a modular malware that has been used in widespread campaigns by [Sandworm Team](https://attack.mitre.org/groups/G0034) since at least 2019 to target Small/Home Office (SOHO) network devices, including WatchGuard and Asus. [Cyclops Blink](https://attack.mitre.org/software/S0687) is assessed to be a replacement for [VPNFilter](https://attack.mitre.org/software/S1010), a similar platform targeting network devices.(Citation: NCSC Cyclops Blink February 2022)(Citation: NCSC CISA Cyclops Blink Advisory February 2022)(Citation: Trend Micro Cyclops Blink March 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--neo-regeorg | Neo-reGeorg | [Neo-reGeorg](https://attack.mitre.org/software/S1189) is an open-source web shell designed as a restructuring of [reGeorg](https://attack.mitre.org/software/S1187) with improved usability, security, and fixes for exising [reGeorg](https://attack.mitre.org/software/S1187) bugs.(Citation: GitHub Neo-reGeorg 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--killdisk | KillDisk | [KillDisk](https://attack.mitre.org/software/S0607) is a disk-wiping tool designed to overwrite files with random data to render the OS unbootable. It was first observed as a component of [BlackEnergy](https://attack.mitre.org/software/S0089) malware during cyber attacks against Ukraine in 2015. [KillDisk](https://attack.mitre.org/software/S0607) has since evolved into stand-alone malware used by a variety of threat actors against additional targets in Europe and Latin America; in 2016 a ransomware component was also incorporated into some [KillDisk](https://attack.mitre.org/software/S0607) variants.(Citation: KillDisk Ransomware)(Citation: ESEST Black Energy Jan 2016)(Citation: Trend Micro KillDisk 1)(Citation: Trend Micro KillDisk 2) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--industroyer | Industroyer | [Industroyer](https://attack.mitre.org/software/S0604) is a sophisticated malware framework designed to cause an impact to the working processes of Industrial Control Systems (ICS), specifically components used in electrical substations.(Citation: ESET Industroyer) [Industroyer](https://attack.mitre.org/software/S0604) was used in the attacks on the Ukrainian power grid in December 2016.(Citation: Dragos Crashoverride 2017) This is the first publicly known malware specifically designed to target and impact operations in the electric grid.(Citation: Dragos Crashoverride 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--poshc2 | PoshC2 | [PoshC2](https://attack.mitre.org/software/S0378) is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in [PowerShell](https://attack.mitre.org/techniques/T1059/001). Although [PoshC2](https://attack.mitre.org/software/S0378) is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.(Citation: GitHub PoshC2) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--invoke-psimage | Invoke-PSImage | [Invoke-PSImage](https://attack.mitre.org/software/S0231) takes a PowerShell script and embeds the bytes of the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this case will dump the passwords. (Citation: GitHub Invoke-PSImage) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--sdelete | SDelete | [SDelete](https://attack.mitre.org/software/S0195) is an application that securely deletes data in a way that makes it unrecoverable. It is part of the Microsoft Sysinternals suite of tools. (Citation: Microsoft SDelete July 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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
| 2015 Ukraine Electric Power Attack | campaign | 2015-12-01T05:00:00.000Z | 2016-01-01T05:00:00.000Z | 2026-05-12 | [2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028) was a [Sandworm Team](https://attack.mitre.org/groups/G0034) campaign during which they used [BlackEnergy](https://attack.mitre.org/software/S0089) (specifically BlackEnergy3) and [KillDisk](https://attack.mitre.org/software/S0607) to target and disrupt transmission and distribution substations within the Ukrainian power grid. This campaign was the first major public attack conducted against the Ukrainian power grid by Sandworm Team. | 高 | `source--mitre-attack-19-1` |
| 2016 Ukraine Electric Power Attack | campaign | 2016-12-01T05:00:00.000Z | 2016-12-01T05:00:00.000Z | 2026-05-12 | [2016 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0025) was a [Sandworm Team](https://attack.mitre.org/groups/G0034) campaign during which they used [Industroyer](https://attack.mitre.org/software/S0604) malware to target and disrupt distribution substations within the Ukrainian power grid. This campaign was the second major public attack conducted against Ukraine by [Sandworm Team](https://attack.mitre.org/groups/G0034).(Citation: ESET Industroyer)(Citation: Dragos Crashoverride 2018) | 高 | `source--mitre-attack-19-1` |
| 2022 Ukraine Electric Power Attack | campaign | 2022-06-01T04:00:00.000Z | 2022-10-01T04:00:00.000Z | 2026-05-12 | The [2022 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0034) was a [Sandworm Team](https://attack.mitre.org/groups/G0034) campaign that used a combination of GOGETTER, Neo-REGEORG, [CaddyWiper](https://attack.mitre.org/software/S0693), and living of the land (LotL) techniques to gain access to a Ukrainian electric utility to send unauthorized commands from their SCADA system.(Citation: Mandiant-Sandworm-Ukraine-2022)(Citation: Dragos-Sandworm-Ukraine-2022)  | 高 | `source--mitre-attack-19-1` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Uncategorized | T0807 | MITRE ATT&CK T0807 | BB) instance for the targeted substations and executed a malicious Supervisory Control Implementation Language (SCIL) script via the native scilc.exe utility (T0807, T0871). This utility is an interpreter for the proprietary SCIL language which allows operators to automate interactions with the MicroSCADA environment. While unable to retrieve the malicious script due to anti-forensic measures employed by the attackers, Mandiant assessed |  |  | 不明 | 不明 | 中 | `source--sandworm--2adea979b20316b9` |
| Uncategorized | T0831 | MITRE ATT&CK T0831 | due to anti-forensic measures employed by the attackers, Mandiant assessed that it likely consisted of a series of commands to open circuit breakers (T0855, T0831) which MicroSCADA would translate to telecontrol commands to the RTU, for instance via IEC-104/101. In the paragraphs below, we compare this LotL approach to the manual HMI interaction of the 2015 Sandworm attacks on Ukraine and the custom malware approach of the original In |  |  | 不明 | 不明 | 中 | `source--sandworm--2adea979b20316b9` |
| Uncategorized | T0855 | MITRE ATT&CK T0855 | s script due to anti-forensic measures employed by the attackers, Mandiant assessed that it likely consisted of a series of commands to open circuit breakers (T0855, T0831) which MicroSCADA would translate to telecontrol commands to the RTU, for instance via IEC-104/101. In the paragraphs below, we compare this LotL approach to the manual HMI interaction of the 2015 Sandworm attacks on Ukraine and the custom malware approach of the ori |  |  | 不明 | 不明 | 中 | `source--sandworm--2adea979b20316b9` |
| Uncategorized | T0871 | MITRE ATT&CK T0871 | tance for the targeted substations and executed a malicious Supervisory Control Implementation Language (SCIL) script via the native scilc.exe utility (T0807, T0871). This utility is an interpreter for the proprietary SCIL language which allows operators to automate interactions with the MicroSCADA environment. While unable to retrieve the malicious script due to anti-forensic measures employed by the attackers, Mandiant assessed that it |  |  | 不明 | 不明 | 中 | `source--sandworm--2adea979b20316b9` |
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.003 | NTDS | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1008 | Fallback Channels | ommand messages use a custom binary scheme to encode the specific command to be executed, as well as any command parameters required. Command And Control T1008 Fallback Channels Cyclops Blink randomly selects a C2 server from contained lists of IPv4 addresses and port numbers. Command And Control T1071.001 Application Layer Protocol: Web Protocols Cyclops Blink can download files via HTTP or HTTPS. Command And Control T1573 |  |  | 不明 | 不明 | 中 | `source--sandworm--fdb4da28a4829992` |
| Discovery | T1018 | Remote System Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1020 | Automated Exfiltration | this malware providing a local Socks connection for db. T1219 Remote Access Software Infamous Chisel - db provides a SSH server and client. Exfiltration T1020 Automated Exfiltration Infamous Chisel - netd automatically exfiltrates files at regular intervals. T1029 Scheduled Transfer Infamous Chisel - netd automatically exfiltrates files at regular intervals. Impact T1489 Service Stop Infamous Chisel - netd replaces the legitimat |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1029 | Scheduled Transfer | provides a SSH server and client. Exfiltration T1020 Automated Exfiltration Infamous Chisel - netd automatically exfiltrates files at regular intervals. T1029 Scheduled Transfer Infamous Chisel - netd automatically exfiltrates files at regular intervals. Impact T1489 Service Stop Infamous Chisel - netd replaces the legitimate netd. |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--f57b4a29ba056879` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--fdb4da28a4829992` |
| Persistence, Privilege Escalation | T1037.004 | RC Scripts | Execution T1059.004 Command and Scripting Interpreter: Unix Shell Cyclops Blink executes downloaded files using the Linux API function execlp. Persistence T1037.004 Boot or Logon Initialization Scripts: RC Scripts Cyclops Blink is executed on device startup, using a modified S51armled RC script. Persistence T1542.001 Pre-OS Boot: System Firmware Cyclops Blink maintains persistence throughout the legitimate device firmware update p |  |  | 不明 | 不明 | 中 | `source--sandworm--fdb4da28a4829992` |
| Credential Access, Discovery | T1040 | Network Sniffing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--59be55a65f44dc2d` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--fdb4da28a4829992` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | 17 Execut on T1059.003 Command and Scr pt ng Interpreter: W ndows Command Shell Pers stence T1547.001 Boot or Logon Autostart Execut on: Reg stry Run Keys / Startup Folder D scovery T1082 System Informat on D scovery Defense Evas on T1112 Mod fy Reg stry Defense Evas on T1218.011 System B nary Proxy E |  |  | 不明 | 不明 | 中 | `source--sandworm--f57b4a29ba056879` |
| Execution | T1059.004 | Unix Shell | ramework, a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. Tactic ID Technique Procedure Execution T1059.004 Command and Scripting Interpreter: Unix Shell Cyclops Blink executes downloaded files using the Linux API function execlp. Persistence T1037.004 Boot or Logon Initialization Scripts: RC Scripts Cyclops Blink is executed on device startup, using a modified S51armled RC |  |  | 不明 | 不明 | 中 | `source--sandworm--fdb4da28a4829992` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--f57b4a29ba056879`, `source--sandworm--fdb4da28a4829992` |
| Execution, Lateral Movement | T1072 | Software Deployment Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | Tactic ID Technique Procedure T1074.001 Data Staged: Local Data Staging Infamous Chisel - netd creates multiple temporary files in the system to hold collected information. T1114.001 Email Collection: Local Email Collection Infamous Chisel - netd exfiltrates files from application and data directories contain |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--f57b4a29ba056879`, `source--sandworm--fdb4da28a4829992` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.003 | Email Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | Shell Pers stence T1547.001 Boot or Logon Autostart Execut on: Reg stry Run Keys / Startup Folder D scovery T1082 System Informat on D scovery Defense Evas on T1112 Mod fy Reg stry Defense Evas on T1218.011 System B nary Proxy Execut on: Rundll32 Defense Evas on T1036 Masquerad ng Command and Control T1071.001 Appl cat on Layer Protocol: Web Protocols M tre Attack Understand ng the 'Kapeka' Backdoor: Deta led Analys s by APT44 |  |  | 不明 | 不明 | 中 | `source--sandworm--f57b4a29ba056879` |
| Collection | T1114.001 | Local Email Collection | Procedure T1074.001 Data Staged: Local Data Staging Infamous Chisel - netd creates multiple temporary files in the system to hold collected information. T1114.001 Email Collection: Local Email Collection Infamous Chisel - netd exfiltrates files from application and data directories containing communication data. Command and Control T1437 (Mobile) Application Layer Protocol Infamous Chisel - db provides SCP functionality. T15 |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Command And Control | T1132.001 | Standard Encoding | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.002 | Non-Standard Encoding | squerade as a Linux kernel thread. Discovery T1082 System Information Discovery Cyclops Blink regularly queries device information. Command And Control T1132.002 Data Encoding: Non- Standard Encoding Cyclops Blink command messages use a custom binary scheme to encode the specific command to be executed, as well as any command parameters required. Command And Control T1008 Fallback Channels Cyclops Blink randomly selects a C2 serv |  |  | 不明 | 不明 | 中 | `source--sandworm--fdb4da28a4829992` |
| Initial Access, Persistence | T1133 | External Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195 | Supply Chain Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.006 | Databases | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--f57b4a29ba056879` |
| Command And Control | T1219 | Remote Access Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1398 | MITRE ATT&CK T1398 | on real-world observations. Tactic ID Technique Procedure Execution T1569 System Services Infamous Chisel - netd replaces the legitimate netd. Persistence T1398 (Mobile) Boot or Logon Initialization Scripts Infamous Chisel - netd replaces the legitimate netd. T1625 (Mobile) Hijack Execution Flow Infamous Chisel - netd replaces the legitimate netd and is executed by init inheriting root privileges. Privilege Escalation T16 |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1406 | MITRE ATT&CK T1406 | vice. Defence Evasion T1629 (Mobile) Impair Defenses Infamous Chisel - netd checks that it is executed by init and at the path for the legitimate netd. T1406 (Mobile) Obfuscated Files or Information Infamous Chisel - blob decompresses executables from bzip archives. Credential Access T1557 Adversary-in-the- Middle Infamous Chisel - mDNSResponder is deployed alongside this malware and could potentially be used for DNS po |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1418 | MITRE ATT&CK T1418 | etd enumerates multiple data directories to discover files of interest. T1430 (Mobile) Location Tracking Infamous Chisel - netd collects GPS information. T1418 (Mobile) Software Discovery Infamous Chisel - netd collects a list of installed packages. T1426 (Mobile) System Information Discovery Infamous Chisel - netd collects various system information such as the Android ID and other hardware information. T1422 (Mobile) Sys |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1420 | MITRE ATT&CK T1420 | niffing Infamous Chisel - tcpdump is deployed alongside this malware and has the ability to sniff network interfaces and monitor network traffic. Discovery T1420 (Mobile) File and Directory Discovery Infamous Chisel - netd enumerates multiple data directories to discover files of interest. T1430 (Mobile) Location Tracking Infamous Chisel - netd collects GPS information. T1418 (Mobile) Software Discovery Infamous Chisel - netd |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1421 | MITRE ATT&CK T1421 | her hardware information. T1422 (Mobile) System Network Configuration Discovery Infamous Chisel - netd collects IP interface configuration information. T1421 (Mobile) System Network Connections Discovery Infamous Chisel - netd performs IP scanning of the local network to discover other devices. Collection T1533 (Mobile) Data from Local System Infamous Chisel - netd automatically collects files from the local system based |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1422 | MITRE ATT&CK T1422 | (Mobile) System Information Discovery Infamous Chisel - netd collects various system information such as the Android ID and other hardware information. T1422 (Mobile) System Network Configuration Discovery Infamous Chisel - netd collects IP interface configuration information. T1421 (Mobile) System Network Connections Discovery Infamous Chisel - netd performs IP scanning of the local network to discover other devices. C |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1426 | MITRE ATT&CK T1426 | Tracking Infamous Chisel - netd collects GPS information. T1418 (Mobile) Software Discovery Infamous Chisel - netd collects a list of installed packages. T1426 (Mobile) System Information Discovery Infamous Chisel - netd collects various system information such as the Android ID and other hardware information. T1422 (Mobile) System Network Configuration Discovery Infamous Chisel - netd collects IP interface configuration i |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1430 | MITRE ATT&CK T1430 | raffic. Discovery T1420 (Mobile) File and Directory Discovery Infamous Chisel - netd enumerates multiple data directories to discover files of interest. T1430 (Mobile) Location Tracking Infamous Chisel - netd collects GPS information. T1418 (Mobile) Software Discovery Infamous Chisel - netd collects a list of installed packages. T1426 (Mobile) System Information Discovery Infamous Chisel - netd collects various system inf |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1437 | MITRE ATT&CK T1437 | Local Email Collection Infamous Chisel - netd exfiltrates files from application and data directories containing communication data. Command and Control T1437 (Mobile) Application Layer Protocol Infamous Chisel - db provides SCP functionality. T1521 (Mobile) Encrypted Channel Infamous Chisel - td is deployed alongside this malware providing a Tor hidden service relaying connections to SSH program. T1572 Protocol Tunnelling |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Impact | T1485 | Data Destruction | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1489 | Service Stop | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--59be55a65f44dc2d` |
| Impact | T1490 | Inhibit System Recovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1491.002 | External Defacement | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1499 | Endpoint Denial of Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1521 | MITRE ATT&CK T1521 | ctories containing communication data. Command and Control T1437 (Mobile) Application Layer Protocol Infamous Chisel - db provides SCP functionality. T1521 (Mobile) Encrypted Channel Infamous Chisel - td is deployed alongside this malware providing a Tor hidden service relaying connections to SSH program. T1572 Protocol Tunnelling Infamous Chisel - td is deployed alongside this malware providing a local Socks connection for |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1533 | MITRE ATT&CK T1533 | 421 (Mobile) System Network Connections Discovery Infamous Chisel - netd performs IP scanning of the local network to discover other devices. Collection T1533 (Mobile) Data from Local System Infamous Chisel - netd automatically collects files from the local system based on a predefined list of file extensions. |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Credential Access | T1539 | Steal Web Session Cookie | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Stealth | T1542.001 | System Firmware | T1037.004 Boot or Logon Initialization Scripts: RC Scripts Cyclops Blink is executed on device startup, using a modified S51armled RC script. Persistence T1542.001 Pre-OS Boot: System Firmware Cyclops Blink maintains persistence throughout the legitimate device firmware update process. This is achieved by patching the firmware when it is downloaded to the device. Defence Evasion T1562.004 Impair Defenses: Disable or Modify Syste |  |  | 不明 | 不明 | 中 | `source--sandworm--fdb4da28a4829992` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | 17 Execut on T1059.003 Command and Scr pt ng Interpreter: W ndows Command Shell Pers stence T1547.001 Boot or Logon Autostart Execut on: Reg stry Run Keys / Startup Folder D scovery T1082 System Informat on D scovery Defense Evas on T1112 Mod fy Reg stry Defense Evas on T1218.011 System B nary Proxy Execut on: Rundll32 Defense Evas on T1036 Masquerad ng Command and Control T1071 |  |  | 不明 | 不明 | 中 | `source--sandworm--f57b4a29ba056879` |
| Credential Access | T1555.003 | Credentials from Web Browsers | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1557 | Adversary-in-the-Middle | legitimate netd. T1406 (Mobile) Obfuscated Files or Information Infamous Chisel - blob decompresses executables from bzip archives. Credential Access T1557 Adversary-in-the- Middle Infamous Chisel - mDNSResponder is deployed alongside this malware and could potentially be used for DNS poisoning. T1634 (Mobile) Credentials from Password Store Infamous Chisel - netd scrapes multiple files containing credentials and key in |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Impact | T1561.002 | Disk Structure Wipe | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1562.004 | MITRE ATT&CK T1562.004 | throughout the legitimate device firmware update process. This is achieved by patching the firmware when it is downloaded to the device. Defence Evasion T1562.004 Impair Defenses: Disable or Modify System Firewall Cyclops Blink modifies the Linux iptables firewall to enable C2 communication via a stored list of port numbers. Defence Evasion T1036.005 Masquerading: Match Legitimate Name or Location Cyclops Blink renames its run |  |  | 不明 | 不明 | 中 | `source--sandworm--fdb4da28a4829992` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569 | System Services | ramework, a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. Tactic ID Technique Procedure Execution T1569 System Services Infamous Chisel - netd replaces the legitimate netd. Persistence T1398 (Mobile) Boot or Logon Initialization Scripts Infamous Chisel - netd replaces the legitimate netd. T1625 (Mobile) Hijack Execution Flow Infamous Chisel - netd replaces the legitima |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Lateral Movement | T1570 | Lateral Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--sandworm--fdb4da28a4829992` |
| Command And Control | T1572 | Protocol Tunneling | 521 (Mobile) Encrypted Channel Infamous Chisel - td is deployed alongside this malware providing a Tor hidden service relaying connections to SSH program. T1572 Protocol Tunnelling Infamous Chisel - td is deployed alongside this malware providing a local Socks connection for db. T1219 Remote Access Software Infamous Chisel - db provides a SSH server and client. Exfiltration T1020 Automated Exfiltration Infamous Chisel - netd au |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Command And Control | T1573.002 | Asymmetric Cryptography | bers. Command And Control T1071.001 Application Layer Protocol: Web Protocols Cyclops Blink can download files via HTTP or HTTPS. Command And Control T1573.002 Encrypted Channel: Asymmetric Cryptography Cyclops Blink C2 messages are individually encrypted using AES-256- CBC and sent underneath TLS. OpenSSL library functions are used to encrypt each message using a randomly generated key and IV, which are then encrypted using a |  |  | 不明 | 不明 | 中 | `source--sandworm--fdb4da28a4829992` |
| Resource Development | T1583 | Acquire Infrastructure | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.004 | Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.004 | Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.005 | Botnet | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.001 | Social Media Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.006 | Vulnerabilities | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.003 | Employee Names | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1590.001 | Domain Properties | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591.002 | Business Relationships | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1592.002 | Software | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1593 | Search Open Websites/Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1594 | Search Victim-Owned Websites | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1625 | MITRE ATT&CK T1625 | netd replaces the legitimate netd. Persistence T1398 (Mobile) Boot or Logon Initialization Scripts Infamous Chisel - netd replaces the legitimate netd. T1625 (Mobile) Hijack Execution Flow Infamous Chisel - netd replaces the legitimate netd and is executed by init inheriting root privileges. Privilege Escalation T1626 (Mobile) Abuse Elevation Control Mechanism Infamous Chisel - netd executes shell scripts as the root us |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1626 | MITRE ATT&CK T1626 | ile) Hijack Execution Flow Infamous Chisel - netd replaces the legitimate netd and is executed by init inheriting root privileges. Privilege Escalation T1626 (Mobile) Abuse Elevation Control Mechanism Infamous Chisel - netd executes shell scripts as the root user of the device. Defence Evasion T1629 (Mobile) Impair Defenses Infamous Chisel - netd checks that it is executed by init and at the path for the legitimate netd. |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1629 | MITRE ATT&CK T1629 | alation T1626 (Mobile) Abuse Elevation Control Mechanism Infamous Chisel - netd executes shell scripts as the root user of the device. Defence Evasion T1629 (Mobile) Impair Defenses Infamous Chisel - netd checks that it is executed by init and at the path for the legitimate netd. T1406 (Mobile) Obfuscated Files or Information Infamous Chisel - blob decompresses executables from bzip archives. Credential Access T1557 |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |
| Uncategorized | T1634 | MITRE ATT&CK T1634 | cess T1557 Adversary-in-the- Middle Infamous Chisel - mDNSResponder is deployed alongside this malware and could potentially be used for DNS poisoning. T1634 (Mobile) Credentials from Password Store Infamous Chisel - netd scrapes multiple files containing credentials and key information. T1040 Network Sniffing Infamous Chisel - tcpdump is deployed alongside this malware and has the ability to sniff network interfaces and moni |  |  | 不明 | 不明 | 中 | `source--sandworm--59be55a65f44dc2d` |

## IOC／artifact概要

- IOC値: 422件
- IOC観測: 595件
- 複数攻撃で観測: 0件
- 要レビュー候補: 169件
- 非IOC artifact観測: 183件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Some Sandworm/GRU Unit 74455 operations were conducted with assistance from APT28/GRU Unit 26165. | 高 | `source--mitre-live-sandworm-2024` | verification_status=supported; The actors are attributed to distinct GRU units and must remain separate profiles. Shared operations do not support treating Sandworm and APT28 as aliases. |

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
| source--sandworm--8aa1794a01d51cc2 | sandworm |  | 不明 | International Strategic/Russia/Vulkan/sandworm.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--eb0dcd21cb3aa0c2 | Appendix Cyclops Blink Sets Sights on ASUS Routers |  | 不明 | Sandworm/Appendix_Cyclops Blink Sets Sights on ASUS Routers.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--2adea979b20316b9 | Clearing the Fog of War A Critical Analysis of Recent Energy Sector Attacks in Denmark and Ukraine |  | 不明 | Sandworm/Clearing the Fog of War A Critical Analysis of Recent Energy Sector Attacks in Denmark and Ukraine.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--fdb4da28a4829992 | Cyclops Blink Malware Analysis Report |  | 不明 | Sandworm/Cyclops-Blink-Malware-Analysis-Report.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--7f18ee389ba2a468 | WithSecure Research Kapeka |  | 不明 | Sandworm/Kapeka/WithSecure-Research-Kapeka.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--7f18ad8ab97f3968 | readme |  | 不明 | Sandworm/Kapeka/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--sandworm--f57b4a29ba056879 | understanding the kapeka backdoor detailed analysis by apt44 |  | 不明 | Sandworm/Kapeka/understanding-the-kapeka-backdoor-detailed-analysis-by-apt44.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--59be55a65f44dc2d | NCSC MAR Infamous Chisel |  | 不明 | Sandworm/NCSC-MAR-Infamous-Chisel.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--ac2c6a3184a4292f | README |  | 不明 | Sandworm/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--sandworm--7c913e63df1a9288 | SBU exposes russian intelligence attempts to penetrate Armed Forces' planning operations system |  | 不明 | Sandworm/SBU exposes russian intelligence attempts to penetrate Armed Forces' planning operations system.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--7242692ba7f0cc0e | Validation script Cyclops Blink Sets Sights on Asus Routers n2HqxTq |  | 不明 | Sandworm/Validation-script_Cyclops-Blink-Sets-Sights-on-Asus-Routers-n2HqxTq.txt | text-data | TLP:CLEAR | 中 |
| source--sandworm--df3f2d7392535669 | apt44 unearthing sandworm |  | 不明 | Sandworm/apt44-unearthing-sandworm.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--58b66a6fb6164000 | russia nexus uac 0113 emulating telecommunication providers in ukraine |  | 不明 | Sandworm/russia-nexus-uac-0113-emulating-telecommunication-providers-in-ukraine.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--835e9fa20fa7983b | sektorcert angrebet mod dansk kritisk infrastruktur tlp clear en |  | 不明 | Sandworm/sektorcert-angrebet-mod-dansk-kritisk-infrastruktur-tlp-clear-en.pdf | report | TLP:CLEAR | 中 |
| source--sandworm--b5eb4f53e1b7a3d0 | Активність угруповання |  | 不明 | Sandworm/Активність угруповання.pdf | report | TLP:CLEAR | 中 |
| source--mitre-live-sandworm-2024 | Sandworm Team, Group G0034 | MITRE ATT&CK | 2024-12-04 | https://attack.mitre.org/groups/G0034/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
