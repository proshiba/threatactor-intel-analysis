# Sea Turtle 脅威アクタープロファイル

- プロファイルID: `actor--sea-turtle`
- 状態: draft
- 更新日時: 2026-07-29T23:13:55Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Sea Turtleの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Sea Turtle**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Cosmic Wolf | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Marbled Dust | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| SILICON | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Teal Kurma | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Sea Turtle](https://attack.mitre.org/groups/G1041) is a Türkiye-linked threat actor active since at least 2017 performing espionage and service provider compromise operations against victims in Asia, Europe, and North America. [Sea Turtle](https://attack.mitre.org/groups/G1041) is notable for targeting registrars managing ccTLDs and complex DNS-based intrusions where the threat actor compromised DNS providers to hijack DNS resolution for ultimate victims, enabling [Sea Turtle](https://attack.mitre.org/groups/G1041) to spoof log in portals and other applications for credential collection.(Citation: Talos Sea Turtle 2019)(Citation: Talos Sea Turtle 2019_2)(Citation: PWC Sea Turtle 2023)(Citation: Hunt Sea Turtle 2024) |
| Capability | SnappyTCP, DNS hijacking, CVE-2009-1151, CVE-2014-6271, CVE-2017-3881, CVE-2017-6736, CVE-2017-12617, CVE-2018-0296, CVE-2018-7600, Drupalgeddon |
| Infrastructure |  |
| Victim | industries: Ministries of foreign affairs, Military organizations, Intelligence agencies, Prominent energy organizations in US, Libya, Egypt, Lebanon, UAE, Albania, Cyprus, Turkey, Iraq, Jordan, Syria, Armenia, Sweden |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Sea Turtle | canonical-name | 高 | Turkey | https://blog.talosintelligence.com/2019/04/seaturtle.html<br>https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/tortoise-and-malwahare.html<br>https://blog.strikeready.com/blog/pivoting-through-a-sea-of-indicators-to-spot-turtles/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Marbled Dust | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Sea Turtle | canonical-name | 高 | TR | https://blog.talosintelligence.com/2019/04/seaturtle.html<br>https://blog.talosintelligence.com/sea-turtle-keeps-on-swimming<br>https://www.reuters.com/article/us-cyber-attack-hijack-exclusive/exclusive-hackers-acting-in-turkeys-interests-believed-to-be-behind-recent-cyberattacks-sources-idUSKBN1ZQ10X |
| misp-microsoft-activity-group | Marbled Dust | canonical-name | 高 | TR | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Sea Turtle - G1041 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1041<br>https://blog.talosintelligence.com/sea-turtle-keeps-on-swimming/<br>https://blog.talosintelligence.com/seaturtle/ |
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
| malware--cve-2009-1151 | CVE-2009-1151 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2014-6271 | CVE-2014-6271 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2017-12617 | CVE-2017-12617 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2017-3881 | CVE-2017-3881 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2017-6736 | CVE-2017-6736 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2018-0296 | CVE-2018-0296 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2018-7600 | CVE-2018-7600 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--dns-hijacking | DNS hijacking | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--drupalgeddon | Drupalgeddon | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--snappytcp | SnappyTCP | [SnappyTCP](https://attack.mitre.org/software/S1163) is a web shell used by [Sea Turtle](https://attack.mitre.org/groups/G1041) between 2021 and 2023 against multiple victims. [SnappyTCP](https://attack.mitre.org/software/S1163) appears to be based on a public GitHub project that has since been removed from the code-sharing site. [SnappyTCP](https://attack.mitre.org/software/S1163) includes a simple reverse TCP shell for Linux and Unix environments with basic command and control capabilities.(Citation: PWC Sea Turtle 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Output Messengerのゼロデイ脆弱性がスパイ活動に悪用される | phishing-campaign | 不明 | 不明 | 2025-05-13 |  |  |  |  | トルコ支援のサイバースパイグループMarbled Dustが、Output Messengerのゼロデイ脆弱性（CVE-2025-27920）を悪用。 この脆弱性はディレクトリトラバーサルにより、認証済み攻撃者が機密ファイルにアクセス可能。 攻撃者は未更新のOutput Messenger Server Managerを標的にマルウェアを展開。 感染後、通信の傍受、ユーザーのなりすまし、内部システムへのアクセスが可能となる。 脆弱性は2024年12月に修正済みだが、未更新のシステムが依然としてリスクに晒されている。 | 中 | `source--daily-cca0fa46e5e1b4b6bc18` |
| Sea Turtle | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Output Messengerのゼロデイ脆弱性がスパイ活動に悪用される | Sea Turtle | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Sea Turtle | Sea Turtle | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

Sea Turtle

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アラブ首長国連邦 | レビュー済みアクターマッピングの標的欄に記録されたアラブ首長国連邦を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | アルバニア | Targeting text mentions albania. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | アルメニア | Targeting text mentions armenia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | イラク | Targeting text mentions iraq. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | エジプト | Targeting text mentions egypt. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでSea Turtleの標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | キプロス | レビュー済みアクターマッピングの標的欄に記録されたキプロスを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ギリシャ | 構造化OSINTの被害国フィールドでSea Turtleの標的・被害国としてギリシャが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | シリア | Targeting text mentions syria. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | スイス | 構造化OSINTの被害国フィールドでSea Turtleの標的・被害国としてスイスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スウェーデン | Targeting text mentions sweden. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | スーダン | 構造化OSINTの被害国フィールドでSea Turtleの標的・被害国としてスーダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | Targeting text mentions turkey. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでSea Turtleの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ヨルダン | Targeting text mentions jordan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | リビア | レビュー済みアクターマッピングの標的欄に記録されたリビアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | レバノン | Targeting text mentions lebanon. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | レビュー済みアクターマッピングの標的欄に記録された米国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | アフリカ | エジプト、スーダン、リビアで確認された標的・被害事例をアフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | アラブ首長国連邦、イラク、シリア、トルコ、ヨルダン、レバノンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 北アフリカ | エジプト、リビアで確認された標的・被害事例を北アフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 南欧 | アルバニア、キプロス、ギリシャで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | アルバニア、オランダ、キプロス、ギリシャ、スイス、スウェーデン、トルコ、ドイツで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Energy | Targeting text indicates the Energy sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.004 | Compile After Delivery | [Sea Turtle](https://attack.mitre.org/groups/G1041) downloaded source code files from remote addresses then compiled them locally via GCC in victim environments.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | [Sea Turtle](https://attack.mitre.org/groups/G1041) used shell scripts for post-exploitation execution in victim environments.(Citation: PWC Sea Turtle 2023)(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Sea Turtle](https://attack.mitre.org/groups/G1041) connected over TCP using HTTP to establish command and control channels.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.002 | Remote Data Staging | [Sea Turtle](https://attack.mitre.org/groups/G1041) staged collected email archives in the public web directory of a website that was accessible from the internet.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Sea Turtle](https://attack.mitre.org/groups/G1041) used compromised credentials to maintain long-term access to victim environments.(Citation: Talos Sea Turtle 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | [Sea Turtle](https://attack.mitre.org/groups/G1041) compromised cPanel accounts in victim environments.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.001 | Local Email Collection | [Sea Turtle](https://attack.mitre.org/groups/G1041) collected email archives from victim environments.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [Sea Turtle](https://attack.mitre.org/groups/G1041) has used external-facing SSH to achieve initial access to the IT environments of victim organizations.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Sea Turtle](https://attack.mitre.org/groups/G1041) gained access to victim environments by exploiting multiple known vulnerabilities over several campaigns.(Citation: Talos Sea Turtle 2019)(Citation: PWC Sea Turtle 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | [Sea Turtle](https://attack.mitre.org/groups/G1041) targeted third-party entities in trusted relationships with primary targets to ultimately achieve access at primary targets. Entities targeted included DNS registrars, telecommunication companies, and internet service providers.(Citation: Talos Sea Turtle 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [Sea Turtle](https://attack.mitre.org/groups/G1041) has used exploits for vulnerabilities such as CVE-2021-44228, CVE-2021-21974, and CVE-2022-0847 to achieve client code execution.(Citation: PWC Sea Turtle 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.006 | Databases | [Sea Turtle](https://attack.mitre.org/groups/G1041) used the tool Adminer to remotely logon to the MySQL service of victim machines.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [Sea Turtle](https://attack.mitre.org/groups/G1041) deployed the [SnappyTCP](https://attack.mitre.org/software/S1163) web shell during intrusion operations.(Citation: PWC Sea Turtle 2023)(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1557 | Adversary-in-the-Middle | [Sea Turtle](https://attack.mitre.org/groups/G1041) modified DNS records at service providers to redirect traffic from legitimate resources to [Sea Turtle](https://attack.mitre.org/groups/G1041)-controlled servers to enable adversary-in-the-middle attacks for credential capture.(Citation: Talos Sea Turtle 2019)(Citation: Talos Sea Turtle 2019_2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [Sea Turtle](https://attack.mitre.org/groups/G1041) used the tar utility to create a local archive of email data on a victim system.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.011 | Ignore Process Interrupts | [Sea Turtle](https://attack.mitre.org/groups/G1041) executed [SnappyTCP](https://attack.mitre.org/software/S1163) using the tool NoHup, which keeps the malware running on a system after exiting the shell or terminal.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | [Sea Turtle](https://attack.mitre.org/groups/G1041) used spear phishing to gain initial access to victims.(Citation: Talos Sea Turtle 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583 | Acquire Infrastructure | [Sea Turtle](https://attack.mitre.org/groups/G1041) accessed victim networks from VPN service provider networks.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [Sea Turtle](https://attack.mitre.org/groups/G1041) registered domains for authoritative name servers used in DNS hijacking activity and for command and control servers.(Citation: Talos Sea Turtle 2019_2)(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.002 | DNS Server | [Sea Turtle](https://attack.mitre.org/groups/G1041) built adversary-in-the-middle DNS servers to impersonate legitimate services that were later used to capture credentials.(Citation: Talos Sea Turtle 2019_2)(Citation: Talos Sea Turtle 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [Sea Turtle](https://attack.mitre.org/groups/G1041) created adversary-in-the-middle servers to impersonate legitimate services and enable credential capture.(Citation: Talos Sea Turtle 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.002 | DNS Server | [Sea Turtle](https://attack.mitre.org/groups/G1041) modified Name Server (NS) items to refer to [Sea Turtle](https://attack.mitre.org/groups/G1041)-controlled DNS servers to provide responses for all DNS lookups.(Citation: Talos Sea Turtle 2019)(Citation: Talos Sea Turtle 2019_2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Sea Turtle](https://attack.mitre.org/groups/G1041) has used tools such as Adminer during intrusions.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.004 | Digital Certificates | [Sea Turtle](https://attack.mitre.org/groups/G1041) created new certificates using a technique called the actors performed "certificate impersonation," a technique in which [Sea Turtle](https://attack.mitre.org/groups/G1041) obtained a certificate authority-signed X.509 certificate from another provider for the same domain imitating the one already used by the targeted organization.(Citation: Talos Sea Turtle 2019)(Citation: Talos Sea Turtle 2019_2) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.003 | Install Digital Certificate | [Sea Turtle](https://attack.mitre.org/groups/G1041) captured legitimate SSL certificates from victim organizations and installed these on [Sea Turtle](https://attack.mitre.org/groups/G1041)-controlled infrastructure to enable subsequent adversary-in-the-middle operations.(Citation: Talos Sea Turtle 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.006 | Clear Linux or Mac System Logs | [Sea Turtle](https://attack.mitre.org/groups/G1041) has overwritten Linux system logs and unsets the Bash history file (effectively removing logging) during intrusions.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1690 | Prevent Command History Logging | [Sea Turtle](https://attack.mitre.org/groups/G1041) unset the Bash and MySQL history files on victim systems.(Citation: Hunt Sea Turtle 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 1件（`artifacts.csv`）

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
| source--daily-cca0fa46e5e1b4b6bc18 | Output Messengerのゼロデイ脆弱性がスパイ活動に悪用される | bleepingcomputer.com | 2025-05-13 | https://www.bleepingcomputer.com/news/security/output-messenger-flaw-exploited-as-zero-day-in-espionage-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--sea-turtle--4e9bc8701f782970 | readme |  | 不明 | Seaturtle/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
