# Storm-0501 脅威アクタープロファイル

- プロファイルID: `actor--storm-0501`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Storm-0501の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Storm-0501**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

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
| Adversary | [Storm-0501](https://attack.mitre.org/groups/G1053) is a financially motivated cyber criminal group that uses commodity and open-source tools to conduct ransomware operations. [Storm-0501](https://attack.mitre.org/groups/G1053) has been active since 2021 and has previously been affiliated with Sabbath Ransomware and other Ransomware-as-a-Service (RaaS) variants such as Hive, [BlackCat](https://attack.mitre.org/software/S1068), Hunters International, [LockBit 3.0](https://attack.mitre.org/software/S1202), and [Embargo](https://attack.mitre.org/software/S1247) ransomware.(Citation: Avertium Storm-0501 Sabbath Ransomware Arcane January 2022)(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024)(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025)(Citation: Google Mandiant Storm-0501 Sabbath Ransomware November 2021) |
| Capability | Embargo, Cobalt Strike, Net, Impacket, AADInternals, Tasklist, Rclone, Nltest |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-0501 | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Storm-0501 | canonical-name | 高 |  | https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/ |
| misp-microsoft-activity-group | Storm-0501 | canonical-name | 高 |  | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Storm-0501 - G1053 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1053<br>https://cloud.google.com/blog/topics/threat-intelligence/sabbath-ransomware-affiliate/<br>https://www.avertium.com/resources/threat-reports/in-depth-look-at-sabbath-ransomware-gang |
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
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--embargo | Embargo | [Embargo](https://attack.mitre.org/software/S1247) is a ransomware variant written in Rust that has been active since at least May 2024.(Citation: Cyble Embargo Ransomware May 2024)(Citation: ESET Embargo Ransomware October 2024)  [Embargo](https://attack.mitre.org/software/S1247) ransomware operations are associated with “double extortion” ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid.(Citation: Cyble Embargo Ransomware May 2024)(Citation: ESET Embargo Ransomware October 2024)  [Embargo](https://attack.mitre.org/software/S1247) ransomware has been known to be delivered through a loader known as MDeployer which also leverages a malware component known as MS4Killer that facilitates termination of processes operating on the victim hosts.(Citation: ESET Embargo Ransomware October 2024) [Embargo](https://attack.mitre.org/software/S1247) is also reportedly a Ransomware as a Service (RaaS).(Citation: ESET Embargo Ransomware October 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--aadinternals | AADInternals | [AADInternals](https://attack.mitre.org/software/S0677) is a PowerShell-based framework for administering, enumerating, and exploiting Azure Active Directory. The tool is publicly available on GitHub.(Citation: AADInternals Github)(Citation: AADInternals Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tasklist | Tasklist | The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--rclone | Rclone | [Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation: DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nltest | Nltest | [Nltest](https://attack.mitre.org/software/S0359) is a Windows command-line utility used to list domain controllers and enumerate domain trusts.(Citation: Nltest Manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Embargoランサムウェア、クラウド環境への攻撃を強化 | ransomware-extortion | 不明 | 不明 | 2024-09-29 |  | malware--embargo |  | victim--activity-rule--b78c2a719aac8707e619 | Embargoランサムウェアのアフィリエイトである攻撃グループStorm-0501は、ハイブリッドクラウド環境を標的にした新たな戦術を採用。 資格情報の悪用や特権アカウントの利用を通じてクラウド環境へのアクセスを獲得し、データを盗み、ランサムウェアペイロードを実行することを目的としている。 初期アクセスの取得方法は、侵害された、または購入した資格情報を使用、または既知の脆弱性を悪用すること。 アクセスを取得した後、攻撃者は、Microsoft Entraテナント内に新しいフェデレーションドメインを作成することにより、永続的なバックドアを配置。 攻撃者は、被害者のオンプレミスおよびクラウド環境にEmbargoランサムウェアを展開するか、後のためにバックドアアクセスを維持。 | 中 | `source--daily-a7defc5bd3e885aefd88` |
| Storm-0501ハッカー、クラウドでのランサムウェア型攻撃へ移行 | ransomware-extortion | 不明 | 不明 | 2025-08-29 |  |  | ttp--activity-rule--9536da68a35c9d55182e | victim--activity-rule--d585ab724da24035a5c1 | MicrosoftはStorm-0501が端末暗号化からクラウド中心の身代金攻撃へ移行と警告。 クラウド機能を悪用し、窃取・バックアップ破壊・新しいKey Vault鍵で暗号化して恐喝。 DefenderのギャップでAD/Entra侵害、DSAを窃取して悪用し、AzureHoundで列挙、MFAがないグローバル管理者アカウント(GA)を奪取。 悪性フェデレーションドメインで永続化し、elevateAccess操作でOwner権限を取得。 スナップショット等を削除後、Teamsで身代金要求。検知・ハンティング情報も提示。 | 高 | `source--daily-3f6df09902adf66bfcb4` |



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Embargoランサムウェア、クラウド環境への攻撃を強化 | 非公開 | aggregate | multiple-organizations | reported |  | malware--embargo |  | クラウド／SaaS | encryption: Embargoランサムウェア、クラウド環境への攻撃を強化 | 不明 | 不明 | 2024-09-29 | 中 | `source--daily-a7defc5bd3e885aefd88` |
| 被害事例: Storm-0501ハッカー、クラウドでのランサムウェア型攻撃へ移行 | 非公開 | anonymous | unknown | reported |  |  | ttp--activity-rule--9536da68a35c9d55182e | エンドポイント, クラウド／SaaS | encryption: Storm-0501ハッカー、クラウドでのランサムウェア型攻撃へ移行 | 不明 | 不明 | 2025-08-29 | 高 | `source--daily-3f6df09902adf66bfcb4` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Impact | T1486 | Data Encrypted for Impact | Storm-0501ハッカー、クラウドでのランサムウェア型攻撃へ移行 MicrosoftはStorm-0501が端末暗号化からクラウド中心の身代金攻撃へ移行と警告。 |  | activity--daily-4bee6f1f25cef5b69398 | 不明 | 不明 | 中 | `source--daily-3f6df09902adf66bfcb4` |
| Credential Access | T1003 | OS Credential Dumping | [Storm-0501](https://attack.mitre.org/groups/G1053) has used the SecretsDump module within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.006 | DCSync | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized DCSync to extract credentials from victims.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.006 | Windows Remote Management | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized the post-exploitation tool known as Evil-WinRM that uses PowerShell over Windows Remote Management (WinRM) for remote code execution.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.007 | Cloud Services | [Storm-0501](https://attack.mitre.org/groups/G1053) has used compromised Entra Connect Sync Server to move laterally within the victim environment.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | [Storm-0501](https://attack.mitre.org/groups/G1053) has used Themida to pack [Cobalt Strike](https://attack.mitre.org/software/S0154) payloads.(Citation: Google Mandiant Storm-0501 Sabbath Ransomware November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized [Rclone](https://attack.mitre.org/software/S1040) masqueraded as svhost.exe and scvhost.exe.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Storm-0501](https://attack.mitre.org/groups/G1053) had used a scheduled task named “SysUpdate” that was registered via GPO on devices in the network to distribute the [Embargo](https://attack.mitre.org/software/S1247) ransomware.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has discovered running processes through `tasklist.exe`.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged PowerShell to execute commands and scripts.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024)(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.009 | Cloud API | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged Cloud CLI to execute commands and exfiltrate data from compromised environments.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.004 | Cloud Accounts | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged compromised accounts to access Microsoft Entra Connect, which was used to synchronize on-premises identities and Microsoft Entra identities, allowing users to sign into both environments with the same password.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) [Storm-0501](https://attack.mitre.org/groups/G1053) has also used the victim Global Administrator account that lacked any registered MFA method to access victim cloud environments.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged Storage Account Access Keys within the victim environment.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged native Windows tools and commands such as `systeminfo` and open-source tools including OSQuery and ossec-win32 to query details about the endpoint.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized an obfuscated version of the Active Directory reconnaissance tool ADRecon.ps1 (obfs.ps1 or recon.ps1) to discover domain accounts.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.004 | Cloud Account | [Storm-0501](https://attack.mitre.org/groups/G1053) has conducted enumeration of users, roles, and resources within victim Azure tenants using the tool Azurehound.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.001 | Additional Cloud Credentials | [Storm-0501](https://attack.mitre.org/groups/G1053) has reset the password of identified administrator accounts that lack MFA and registered their own MFA method.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.003 | Additional Cloud Roles | [Storm-0501](https://attack.mitre.org/groups/G1053) has elevated their access to Azure resources using `Microsoft.Authorization/elevateAccess/action` and `Microsoft.Authorization/roleAssignments/write` operations to gain User Access Administrator and Owner Azure roles over the victims’ Azure subscriptions.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged brute force attacks to obtain credentials.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Storm-0501](https://attack.mitre.org/groups/G1053) has exploited N-day vulnerabilities associated with public facing services to gain initial access to victim environments to include Zoho ManageEngine (CVE-2022-47966), Citrix NetScaler “Citrix Bleed” (CVE-2023-4966), and Adobe ColdFusion 2016 (CVE-2023-29300 or CVE-2023-38203).(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.010 | Regsvr32 | [Storm-0501](https://attack.mitre.org/groups/G1053) has launched [Cobalt Strike](https://attack.mitre.org/software/S0154) Beacon files using regsvr32.exe.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [Storm-0501](https://attack.mitre.org/groups/G1053) has launched [Cobalt Strike](https://attack.mitre.org/software/S0154) Beacon files with rundll32.exe.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219.002 | Remote Desktop Software | [Storm-0501](https://attack.mitre.org/groups/G1053) has used legitimate remote monitoring and management (RMM) tools including AnyDesk, NinjaOne, and Level.io.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has used Windows native utility [Nltest](https://attack.mitre.org/software/S0359) `nltest.exe` for discovery.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Privilege Escalation | T1484.001 | Group Policy Modification | [Storm-0501](https://attack.mitre.org/groups/G1053) distributed Group Policy Objects to tamper with security products.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Privilege Escalation | T1484.002 | Trust Modification | [Storm-0501](https://attack.mitre.org/groups/G1053) created a new federated domain within the victim Microsoft Entra tenant using Global Administrator level access to establish a persistent backdoor for later use.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024)(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1485 | Data Destruction | [Storm-0501](https://attack.mitre.org/groups/G1053) has destroyed data and backup files.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | [Storm-0501](https://attack.mitre.org/groups/G1053) has encrypted files in victim environments using ransomware as a service (RaaS) including Sabbath, Hive, [BlackCat](https://attack.mitre.org/software/S1068), Hunters International, [LockBit 3.0](https://attack.mitre.org/software/S1202) and [Embargo](https://attack.mitre.org/software/S1247) ransomware.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1490 | Inhibit System Recovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has deleted snapshots, restore points, storage accounts, and backup services to prevent remediation and restoration.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) [Storm-0501](https://attack.mitre.org/groups/G1053) has also impacted Azure resources through the targeting of `Microsoft.Compute/snapshots/delete`,<br>`Microsoft.Compute/restorePointCollections/delete`,<br>`Microsoft.Storage/storageAccounts/delete`, and <br>`Microsoft.RecoveryServices/Vaults/backupFabrics/protectionContainers/delete`.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has detected endpoint security solutions using `sc query sense` and `sc query windefend`.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1526 | Cloud Service Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has discovered the victim environment’s protections to include Azure policies, resource locks, and Azure Storage immutability policies.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1530 | Data from Cloud Storage | [Storm-0501](https://attack.mitre.org/groups/G1053) had modified Azure Storage account resources through the `Microsoft.Storage/storageAccounts/write` operation to expose non-remotely accessible accounts for data exfiltration.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1537 | Transfer Data to Cloud Account | [Storm-0501](https://attack.mitre.org/groups/G1053) has copied data from the victims environment to their own infrastructure leveraging AzCopy CLI.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.004 | Private Keys | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged the Azure Owner role to access and steal the Storage Account Access keys using the `Microsoft.Storage/storageAccounts/listkeys/action` operation.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.005 | Password Managers | [Storm-0501](https://attack.mitre.org/groups/G1053) has stolen credentials contained in the password manager Keepass by utilizing Find-KeePassConfig.ps1.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.006 | Cloud Secrets Management Stores | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized Azure Key Vault to store the encryption key using the operation `Microsoft.KeyVault/Vaults/write`.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Defense Impairment, Persistence | T1556.009 | Conditional Access Policies | [Storm-0501](https://attack.mitre.org/groups/G1053) has registered their own MFA method, and leveraged a victim hybrid joined server to circumvent Conditional Access Policies.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Storm-0501](https://attack.mitre.org/groups/G1053) has exfiltrated stolen data to the MEGA file sharing site.(Citation: Google Mandiant Storm-0501 Sabbath Ransomware November 2021) [Storm-0501](https://attack.mitre.org/groups/G1053) has also utilized [Rclone](https://attack.mitre.org/software/S1040) to exfiltrate data from victim environments to cloud storage such as MegaSync.(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) [Storm-0501](https://attack.mitre.org/groups/G1053) has exfiltrated data to their own infrastructure utilizing AzCopy Command-Line tool (CLI).(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1578.003 | Delete Cloud Instance | [Storm-0501](https://attack.mitre.org/groups/G1053) has conducted mass deletion of cloud data stores and resources from Azure subscriptions.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1580 | Cloud Infrastructure Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has enumerated compromised cloud environments to identify critical assets, data stores, and back resources.(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.003 | Digital Certificates | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized their own self-signed TLS certificate “Microsoft IT TLS CA 5” with their infrastructure.(Citation: Google Mandiant Storm-0501 Sabbath Ransomware November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.006 | Vulnerabilities | [Storm-0501](https://attack.mitre.org/groups/G1053) has obtained capabilities to exploit N-day vulnerabilities associated with public facing services to gain initial access to victim environments to include Zoho ManageEngine (CVE-2022-47966), Citrix NetScaler “Citrix Bleed” (CVE-2023-4966), and Adobe ColdFusion 2016 (CVE-2023-29300 or CVE-2023-38203).(Citation: Microsoft Storm-501 Sabbath Ransomware Embargo September 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1614.001 | System Language Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has identified system language codes on a compromised host to determine if the victim falls under a non-supported language code that is prohibited for targeting, including victims associated with Russia and other Commonwealth of Independent States (CIS) that may draw attention of law enforcement in countries where the ransomware operator or affiliates may reside/operate from.(Citation: Avertium Storm-0501 Sabbath Ransomware Arcane January 2022)(Citation: Google Mandiant Storm-0501 Sabbath Ransomware November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | [Storm-0501](https://attack.mitre.org/groups/G1053) has engaged in double-extortion ransomware, exfiltrating data and directly contacting victims when the primary organization refuses to pay along with posting data on their data leak sites.(Citation: Avertium Storm-0501 Sabbath Ransomware Arcane January 2022)(Citation: Microsoft Storm-0501 Embargo Ransomware August 2025)(Citation: Google Mandiant Storm-0501 Sabbath Ransomware November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 10件（`artifacts.csv`）

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
| source--daily-3f6df09902adf66bfcb4 | Storm-0501ハッカー、クラウドでのランサムウェア型攻撃へ移行 | bleepingcomputer.com | 2025-08-29 | https://www.bleepingcomputer.com/news/security/storm-0501-hackers-shift-to-ransomware-attacks-in-the-cloud/ | osint-report | TLP:CLEAR | 中 |
| source--daily-a7defc5bd3e885aefd88 | Embargoランサムウェア、クラウド環境への攻撃を強化 | bleepingcomputer.com | 2024-09-29 | https://www.bleepingcomputer.com/news/security/embargo-ransomware-escalates-attacks-to-cloud-environments/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--storm-0501--0a15d9e88139faba | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--storm-0501--0d1acae0bd717d55 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--storm-0501--3ceaa5aa4393c11f | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--storm-0501--5e4e96bf9e2532d1 | threat horizons report h1 2025 |  | 2025 | summary/2025/threat_horizons_report_h1_2025.pdf | report | TLP:CLEAR | 中 |
| source--storm-0501--9dca41b1465ff529 | storm 0501 |  | 不明 | actor_profile/evidence/storm-0501.csv | structured-data | TLP:CLEAR | 中 |
| source--storm-0501--b8e6cf9fc5201b4c | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--storm-0501--c9befc46d5a04a83 | 2026 safebreach state of the breach report final 1 |  | 2026 | summary/2026/2026_safebreach_state_of_the_breach_report_final-1.pdf | report | TLP:CLEAR | 中 |
| source--storm-0501--d9ec7370b268af85 | Cloud Security Risk Report 2025 |  | 2025 | summary/2026/Cloud_Security_Risk_Report_2025.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
