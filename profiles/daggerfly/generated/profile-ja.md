# Daggerfly 脅威アクタープロファイル

- プロファイルID: `actor--daggerfly`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Daggerflyの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Daggerfly**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BRONZE HIGHLAND | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Evasive Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Daggerfly](https://attack.mitre.org/groups/G1034) is a People's Republic of China-linked APT entity active since at least 2012. [Daggerfly](https://attack.mitre.org/groups/G1034) has targeted individuals, government and NGO entities, and telecommunication companies in Asia and Africa. [Daggerfly](https://attack.mitre.org/groups/G1034) is associated with exclusive use of [MgBot](https://attack.mitre.org/software/S1146) malware and is noted for several potential supply chain infection campaigns.(Citation: Symantec Daggerfly 2023)(Citation: ESET EvasivePanda 2023)(Citation: Symantec Daggerfly 2024)(Citation: ESET EvasivePanda 2024) |
| Capability | Nightdoor, PlugX, MgBot, MacMa, BITSAdmin, Reg |
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
| etda-threat-group-cards | Bronze Highland | canonical-name | 高 | China | https://www.secureworks.com/research/threat-profiles<br>https://blog.malwarebytes.com/threat-analysis/2020/07/chinese-apt-group-targets-india-and-hong-kong-using-new-variant-of-mgbot-malware/<br>https://vb2020.vblocalhost.com/uploads/VB2020-43.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | BRONZE HIGHLAND | canonical-name | 高 | CN | https://blog.malwarebytes.com/threat-analysis/2020/07/chinese-apt-group-targets-india-and-hong-kong-using-new-variant-of-mgbot-malware<br>https://vb2020.vblocalhost.com/uploads/VB2020-43.pdf<br>https://www.youtube.com/watch?v=LeKi0KfzOow&list=PLffioUnqXWkdzWcZXH-bzPVgcs2R4r7iS&index=1&t=2154s |
| misp-threat-actor | Evasive Panda | multiple-name-intersection | 高 | CN, China | https://blog.malwarebytes.com/threat-analysis/2020/07/chinese-apt-group-targets-india-and-hong-kong-using-new-variant-of-mgbot-malware/<br>https://vb2020.vblocalhost.com/uploads/VB2020-43.pdf<br>https://www.virusbulletin.com/virusbulletin/2014/02/needle-haystack |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Daggerfly - G1034 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1034<br>https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot<br>https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset |
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
| malware--macma | MacMa | [MacMa](https://attack.mitre.org/software/S1016) is a macOS-based backdoor with a large set of functionalities to control and exfiltrate files from a compromised computer. [MacMa](https://attack.mitre.org/software/S1016) has been observed in the wild since November 2021.(Citation: ESET DazzleSpy Jan 2022) [MacMa](https://attack.mitre.org/software/S1016) shares command and control and unique libraries with [MgBot](https://attack.mitre.org/software/S1146) and [Nightdoor](https://attack.mitre.org/software/S1147), indicating a relationship with the [Daggerfly](https://attack.mitre.org/groups/G1034) threat actor.(Citation: Symantec Daggerfly 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--mgbot | MgBot | [MgBot](https://attack.mitre.org/software/S1146) is a modular malware framework exclusively associated with [Daggerfly](https://attack.mitre.org/groups/G1034) operations since at least 2012. [MgBot](https://attack.mitre.org/software/S1146) was developed in C++ and features a module design with multiple available plugins that have been under active development through 2024.(Citation: Szappanos MgBot 2014)(Citation: ESET EvasivePanda 2023)(Citation: Symantec Daggerfly 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--nightdoor | Nightdoor | [Nightdoor](https://attack.mitre.org/software/S1147) is a backdoor exclusively associated with [Daggerfly](https://attack.mitre.org/groups/G1034) operations. [Nightdoor](https://attack.mitre.org/software/S1147) uses common libraries with [MgBot](https://attack.mitre.org/software/S1146) and [MacMa](https://attack.mitre.org/software/S1016), linking these malware families together.(Citation: ESET EvasivePanda 2024)(Citation: Symantec Daggerfly 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--plugx | PlugX | [PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.(Citation: Lastline PlugX Analysis)(Citation: FireEye Clandestine Fox Part 2)(Citation: New DragonOK)(Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--bitsadmin | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--reg | Reg | [Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. (Citation: Microsoft Reg)<br><br>Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. (Citation: Windows Commands JPCERT) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| 中国のサイバースパイ、新たなSSHバックドアを使用してネットワークデバイスをハッキング | cyber-espionage | 不明 | 不明 | 2025-02-05 | target--activity-rule--country--95e363d6dfa8c6f2ecbb |  | ttp--activity-rule--05c6be6b3497b5378ff5 | victim--activity-rule--a4c4ccaf269236ce161c | 中国のハッキンググループ「Evasive Panda（別名：DaggerFly）」が、ネットワーク機器のSSHデーモンにマルウェアを注入し、持続的なアクセスと隠密な操作を行っている。 この攻撃スイートは「ELF/Sshdinjector.A!tr」と名付けられ、SSHデーモンに注入されたマルウェアの集合体であり、システム偵察、資格情報の窃取、プロセス監視、リモートコマンド実行、ファイル操作などの幅広い機能を持つ。 攻撃者は、デバイスが既に感染しているか、root権限で実行されているかを確認し、条件が満たされると、SSHライブラリ（libssdh.so）などの複数のバイナリをターゲットマシンにドロップする。 このマルウェアは、C2サーバーからのコマンドを待機し、システム情報の収集やデータの外部送信などを行う。 | 中 | `source--daily-3416f994a1eefc895ed4` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | 構造化OSINTの被害国フィールドでDaggerflyの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ナイジェリア | 構造化OSINTの被害国フィールドでDaggerflyの標的・被害国としてナイジェリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでDaggerflyの標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでDaggerflyの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マカオ | 構造化OSINTの被害国フィールドでDaggerflyの標的・被害国としてマカオが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでDaggerflyの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ミャンマー | 構造化OSINTの被害国フィールドでDaggerflyの標的・被害国としてミャンマーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | 活動「中国のサイバースパイ、新たなSSHバックドアを使用してネットワークデバイスをハッキング」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-3416f994a1eefc895ed4`, `source--target-audit-etda-threat-group-cards` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでDaggerflyの標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 香港 | 構造化OSINTの被害国フィールドでDaggerflyの標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | アフリカ | 構造化OSINTの被害地域フィールドでDaggerflyの標的範囲としてアフリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | チベット | 構造化OSINTの被害地域フィールドでDaggerflyの標的範囲としてチベットが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | マカオ、中国、台湾、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-3416f994a1eefc895ed4`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | フィリピン、ベトナム、マレーシア、ミャンマーで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 政府・行政 | [Daggerfly](https://attack.mitre.org/groups/G1034) has targeted individuals, government and NGO entities, and telecommunication companies in Asia and Africa. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 非営利・市民社会 | [Daggerfly](https://attack.mitre.org/groups/G1034) has targeted individuals, government and NGO entities, and telecommunication companies in Asia and Africa. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 情報通信 | [Daggerfly](https://attack.mitre.org/groups/G1034) has targeted individuals, government and NGO entities, and telecommunication companies in Asia and Africa. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 中国のサイバースパイ、新たなSSHバックドアを使用してネットワークデバイスをハッキング | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--95e363d6dfa8c6f2ecbb |  | ttp--activity-rule--05c6be6b3497b5378ff5 | サーバー, ネットワーク機器 |  | 不明 | 不明 | 2025-02-05 | 中 | `source--daily-3416f994a1eefc895ed4` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1082 | System Information Discovery | このマルウェアは、C2サーバーからのコマンドを待機し、システム情報の収集やデータの外部送信などを行う。 |  | activity--daily-e6a1fb3331093f1f95ff | 不明 | 不明 | 中 | `source--daily-3416f994a1eefc895ed4` |
| Credential Access | T1003.002 | Security Account Manager | [Daggerfly](https://attack.mitre.org/groups/G1034) used [Reg](https://attack.mitre.org/software/S0075) to dump the Security Account Manager (SAM) hive from victim machines for follow-on credential extraction.(Citation: Symantec Daggerfly 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | [Daggerfly](https://attack.mitre.org/groups/G1034) used [Reg](https://attack.mitre.org/software/S0075) to dump the Security Account Manager (SAM), System, and Security Windows registry hives from victim machines.(Citation: Symantec Daggerfly 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.003 | Rename Legitimate Utilities | [Daggerfly](https://attack.mitre.org/groups/G1034) used a renamed version of rundll32.exe, such as "dbengin.exe" located in the `ProgramData\Microsoft\PlayReady` directory, to proxy malicious DLL execution.(Citation: Symantec Daggerfly 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Daggerfly](https://attack.mitre.org/groups/G1034) has attempted to use scheduled tasks for persistence in victim environments.(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Daggerfly](https://attack.mitre.org/groups/G1034) used PowerShell to download and execute remote-hosted files on victim systems.(Citation: Symantec Daggerfly 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Daggerfly](https://attack.mitre.org/groups/G1034) uses HTTP for command and control communication.(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Daggerfly](https://attack.mitre.org/groups/G1034) utilizes victim machine operating system information to create custom User Agent strings for subsequent command and control communication.(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Daggerfly](https://attack.mitre.org/groups/G1034) has used PowerShell and [BITSAdmin](https://attack.mitre.org/software/S0190) to retrieve follow-on payloads from external locations for execution on victim machines.(Citation: Symantec Daggerfly 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.001 | Local Account | [Daggerfly](https://attack.mitre.org/groups/G1034) created a local account on victim machines to maintain access.(Citation: Symantec Daggerfly 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | [Daggerfly](https://attack.mitre.org/groups/G1034) has used strategic website compromise for initial access against victims.(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | [Daggerfly](https://attack.mitre.org/groups/G1034) is associated with several supply chain compromises using malicious updates to compromise victims.(Citation: ESET EvasivePanda 2023)(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [Daggerfly](https://attack.mitre.org/groups/G1034) has used strategic website compromise to deliver a malicious link requiring user interaction.(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [Daggerfly](https://attack.mitre.org/groups/G1034) proxied execution of malicious DLLs through a renamed rundll32.exe binary.(Citation: Symantec Daggerfly 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | [Daggerfly](https://attack.mitre.org/groups/G1034) has used signed, but not notarized, malicious files for execution in macOS environments.(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [Daggerfly](https://attack.mitre.org/groups/G1034) has used legitimate software to side-load [PlugX](https://attack.mitre.org/software/S0013) loaders onto victim systems.(Citation: Symantec Daggerfly 2023) [Daggerfly](https://attack.mitre.org/groups/G1034) is also linked to multiple other instances of side-loading for initial loading activity.(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.004 | Server | [Daggerfly](https://attack.mitre.org/groups/G1034) compromised web servers hosting updates for software as part of a supply chain intrusion.(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.002 | Code Signing Certificates | [Daggerfly](https://attack.mitre.org/groups/G1034) created code signing certificates to sign malicious macOS files.(Citation: ESET EvasivePanda 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 4件（`artifacts.csv`）

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
| source--daggerfly--3e11c5dcad68c6cb | eset threat report h22024 |  | 不明 | summary/2024/eset-threat-report-h22024.pdf | report | TLP:CLEAR | 中 |
| source--daggerfly--70cd7602a74f3aa5 | eset apt activity report q2 2025 q3 2025 |  | 2025 | summary/2025/eset-apt-activity-report-q2-2025-q3-2025.pdf | report | TLP:CLEAR | 中 |
| source--daggerfly--8a2cb6114c21a01c | eset threat report h12024 |  | 不明 | summary/2024/eset-threat-report-h12024.pdf | report | TLP:CLEAR | 中 |
| source--daggerfly--e6cfc1fd35dfef7b | daggerfly |  | 不明 | actor_profile/evidence/daggerfly.csv | structured-data | TLP:CLEAR | 中 |
| source--daily-3416f994a1eefc895ed4 | 中国のサイバースパイ、新たなSSHバックドアを使用してネットワークデバイスをハッキング | bleepingcomputer.com | 2025-02-05 | https://www.bleepingcomputer.com/news/security/chinese-cyberspies-use-new-ssh-backdoor-in-network-device-hacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
