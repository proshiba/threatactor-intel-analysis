# Moonstone Sleet 脅威アクタープロファイル

- プロファイルID: `actor--moonstone-sleet`
- 状態: draft
- 更新日時: 2026-07-29T15:29:47Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Moonstone Sleetの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Moonstone Sleet**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Storm-1789 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Lazarus Group | overlaps-with | The group previously overlapped significantly with another North Korean-linked entity, [Lazarus Group](https://attack.mitre.org/groups/G0032), but has differentiated its tradecraft since 2023. | 高 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) is a North Korean-linked threat actor executing both financially motivated attacks and espionage operations. The group previously overlapped significantly with another North Korean-linked entity, [Lazarus Group](https://attack.mitre.org/groups/G0032), but has differentiated its tradecraft since 2023. [Moonstone Sleet](https://attack.mitre.org/groups/G1036) is notable for creating fake companies and personas to interact with victim entities, as well as developing unique malware such as a variant delivered via a fully functioning game.(Citation: Microsoft Moonstone Sleet 2024) |
| Capability | Qilin |
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
| etda-threat-group-cards | Moonstone Sleet | canonical-name | 高 | North Korea | https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/<br>https://checkmarx.com/blog/a-new-north-korean-group-emerges-disrupting-the-open-source-ecosystem/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Moonstone+Sleet&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Moonstone Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Lazarus Group | canonical-name | 高 | KP, Korea (Democratic People's Republic of) | https://threatpost.com/operation-blockbuster-coalition-ties-destructive-attacks-to-lazarus-group/116422/<br>https://www.us-cert.gov/ncas/alerts/TA17-164A<br>https://www.us-cert.gov/ncas/alerts/TA17-318A |
| misp-microsoft-activity-group | Moonstone Sleet | canonical-name | 高 | KP, North Korea | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Moonstone Sleet - G1036 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1036<br>https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/ |
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
| malware--qilin | Qilin | [Qilin](https://attack.mitre.org/software/S1242) is a ransomware family operated as a ransomware-as-a-service (RaaS) that has been active since at least 2022. It includes variants written in Go and Rust capable of targeting Windows, Linux, and VMware ESXi environments. [Qilin](https://attack.mitre.org/software/S1242) shares functionality overlaps with [Black Basta](https://attack.mitre.org/software/S1070), [REvil](https://attack.mitre.org/software/S0496), and [BlackCat](https://attack.mitre.org/software/S1068) ransomware. [Qilin](https://attack.mitre.org/software/S1242) affiliates have targeted multiple entities worldwide with the majority of victims in the US, France, Canada, and the UK, primarily in the manufacturing, technology, financial services, and healthcare sectors.(Citation: Trend Micro Agenda Ransomware AUG 2022)(Citation: SentinelOne Qilin NOV 2022)(Citation: BushidoToken Qilin RaaS JUN 2024)(Citation: Sophos Qilin MSP APR 2025)(Citation: Trend Micro Agenda Ransomware OCT 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| 北朝鮮のMoonstone Sleetが悪意あるコードの配布を拡大 | reported-activity | 不明 | 不明 | 2024-06-14 |  |  |  |  | 北朝鮮のMoonstone Sleetが悪意あるnpmコードを配布。 公開レジストリでコードを拡散し、攻撃対象を拡大。 航空宇宙、教育、ソフトウェア分野を標的に。 前に観測された攻撃ではWindowsのみだったが、新たに発見されたものではLinuxシステムを攻撃するための機能が追加。 オープンソースのエコシステムに大きな脅威。 | 高 | `source--daily-9b109b5f0fe055ebeba0` |
| マイクロソフト：北朝鮮のハッカー、Qilinランサムウェア・ギャングに参加 | ransomware-extortion | 2023-12 | 2023-12 | 2025-03-08 |  | malware--qilin |  | victim--activity-rule--a8eb7df35b3e91598d43 | マイクロソフトは、北朝鮮のハッカー集団「Moonstone Sleet」が、最近の限定的な攻撃でQilinランサムウェアを展開していると報告。 Moonstone Sleetは以前は独自のカスタムランサムウェアを使用していたが、今回初めてRaaSオペレーターが開発したランサムウェアを使用。 同グループは、トロイの木馬化されたソフトウェアや偽のソフトウェア開発会社を利用し、LinkedInやフリーランスネットワーク、Telegram、メールを通じて被害者と接触。 Qilinランサムウェアは2022年8月に「Agenda」として登場し、これまでに300以上の被害者を主張。 Qilinｈ2023年12月には攻撃が活発化し、VMware ESXi仮想マシンを標的とする高度なLinuxエンクリプターも使用するようになった。 | 中 | `source--daily-79065a5586e0fb17d444` |
| マイクロソフト、北朝鮮ハッカー「Moonstone Sleet」と新しいFakePennyランサムウェアを結びつける | ransomware-extortion | 不明 | 不明 | 2024-05-29 | target--activity-rule--sector--932f4928d5e1ec28e2df |  |  | victim--activity-rule--334f2276bd544e473f73 | マイクロソフトがMoonstone Sleet(以前はStorm-17)という北朝鮮のハッカーグループをFakePennyランサムウェア攻撃に関連付けた Moonstone Sleetは財政およびサイバー諜報を目的に活動している 当初はDiamond Sleetと多くの重複があったが、その後グループは独自のインフラとツールを使用するようになった 偽のソフトウェア企業を通じて攻撃を行うことが多い 攻撃の動機は金銭的利益と見られる。ただし、このグループが以前にサイバースパイ攻撃に関与していたことから情報収集にも重点をおいていることが示唆される | 高 | `source--daily-3361ec1dff6e8d1d939e` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | IT・ソフトウェア | 活動「マイクロソフト、北朝鮮ハッカー「Moonstone Sleet」と新しいFakePennyランサムウェアを結びつける」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-3361ec1dff6e8d1d939e` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: マイクロソフト、北朝鮮ハッカー「Moonstone Sleet」と新しいFakePennyランサムウェアを結びつける | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--932f4928d5e1ec28e2df |  |  |  | encryption: マイクロソフト、北朝鮮ハッカー「Moonstone Sleet」と新しいFakePennyランサムウェアを結びつける<br>espionage: マイクロソフトがMoonstone Sleet(以前はStorm-17)という北朝鮮のハッカーグループをFakePennyランサムウェア攻撃に関連付けた Moonstone Sleetは財政およびサイバー諜報を目的に活動している 当初はDiamond Sleetと多くの重複があったが、その後グループは独自のインフラとツールを使用するようになった 偽のソフトウェア企業を通じて攻撃を行うことが多い 攻撃の動機は金銭的利益と見られる。 | 不明 | 不明 | 2024-05-29 | 高 | `source--daily-3361ec1dff6e8d1d939e` |
| 被害事例: マイクロソフト：北朝鮮のハッカー、Qilinランサムウェア・ギャングに参加 | 非公開 | aggregate | multiple-organizations | reported |  | malware--qilin |  | メール／メールアカウント | encryption: マイクロソフト：北朝鮮のハッカー、Qilinランサムウェア・ギャングに参加 | 2023-12 | 2023-12 | 2025-03-08 | 中 | `source--daily-79065a5586e0fb17d444` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) retrieved credentials from LSASS memory.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has gathered information on victim network configuration.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) delivers encrypted payloads in pieces that are then combined together to form a new portable executable (PE) file during installation.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.009 | Embedded Payloads | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) embedded payloads in trojanized software for follow-on execution.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has used encrypted payloads within files for follow-on execution and defense evasion.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) deployed various malware such as YouieLoader that can perform system user discovery actions.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used scheduled tasks for program execution during initial access to victim machines.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used curl to connect to adversary-controlled infrastructure and retrieve additional payloads.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has gathered information on victim systems.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) retrieved a final stage payload from command and control infrastructure during initial installation on victim systems.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) delivered payloads using multiple rounds of obfuscation and encoding to evade defenses and analysis.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has distributed a trojanized version of PuTTY software for initial access to victims.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) relied on users interacting with malicious files, such as a trojanized PuTTY installer, for initial execution.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) deployed malware such as YouieLoader capable of capturing victim system browser information.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has deployed ransomware in victim environments.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used registry run keys for process execution during initial victim infection.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) delivered various payloads to victims as spearphishing attachments.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.003 | Spearphishing via Service | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has used social media services to spear phish victims to deliver trojainized software.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used intermediate loader malware such as YouieLoader and SplitLoader that create malicious services.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) registered domains to develop effective personas for fake companies used in phishing activity.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) registered virtual private servers to host payloads for download.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has created social media accounts to interact with victims.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has created email accounts to interact with victims, including for phishing purposes.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587 | Develop Capabilities | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) developed malicious npm packages for delivery to or retrieval by victims.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has developed custom malware, including a malware delivery mechanism masquerading as a legitimate game.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) gathered victim email address information for follow-on phishing activity.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591 | Gather Victim Org Information | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has gathered information on victim organizations through email and social media interaction.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598 | Phishing for Information | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has interacted with victims to gather information via email.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used spearphishing messages containing items such as tracking pixels to determine if users interacted with malicious messages.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) staged malicious capabilities online for follow-on download by victims or malware.(Citation: Microsoft Moonstone Sleet 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 32件（`artifacts.csv`）

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
| source--daily-3361ec1dff6e8d1d939e | マイクロソフト、北朝鮮ハッカー「Moonstone Sleet」と新しいFakePennyランサムウェアを結びつける | bleepingcomputer.com | 2024-05-29 | https://www.bleepingcomputer.com/news/microsoft/microsoft-links-moonstone-sleet-north-korean-hackers-to-new-fakepenny-ransomware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-79065a5586e0fb17d444 | マイクロソフト：北朝鮮のハッカー、Qilinランサムウェア・ギャングに参加 | bleepingcomputer.com | 2025-03-08 | https://www.bleepingcomputer.com/news/security/microsoft-north-korean-hackers-now-deploying-qilin-ransomware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-9b109b5f0fe055ebeba0 | 北朝鮮のMoonstone Sleetが悪意あるコードの配布を拡大 | darkreading.com | 2024-06-14 | https://www.darkreading.com/cyberattacks-data-breaches/north-koreas-moonstone-sleet-widens-distribution-of-malicious-code-packages | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--moonstone-sleet--057dc52f1759be32 | moonstone sleet |  | 不明 | actor_profile/evidence/moonstone-sleet.csv | structured-data | TLP:CLEAR | 中 |
| source--moonstone-sleet--0a5c0da2f99d1612 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--0d31bb8755ee8e38 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--2783500b7b780791 | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--2c8108aa76041772 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--58b10f25387bdb3e | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--moonstone-sleet--5e75b17840f0ebd2 | eset apt activity report q2 2025 q3 2025 |  | 2025 | summary/2025/eset-apt-activity-report-q2-2025-q3-2025.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--63b1af4df502c7bd | Semiannual+Ransomware+Report+ +H1+2024 |  | 2024 | cybercrime/2024/Semiannual+Ransomware+Report+-+H1+2024.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--7cc947ab20057181 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--a6aabc99254f6193 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--b7af744c9cf11a1a | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--bc0d35bbdaf1db31 | Blurred Lines of Cyber Threat Attribution |  | 不明 | International Strategic/Korea/ Blurred-Lines-of-Cyber-Threat-Attribution.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--c1ba57476571c6de | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--d8ef2d8ed48a471e | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--moonstone-sleet--fe9810e624ede013 | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
