# Andariel 脅威アクタープロファイル

- プロファイルID: `actor--andariel`
- 状態: draft
- 更新日時: 2026-07-27T11:17:21Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Andarielの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Andariel**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Onyx Sleet | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| PLUTONIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Silent Chollima | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| G0138 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 5; mapping requires review. |

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
| Lazarus Group | part-of | MITRE considers Andariel a subset of Lazarus Group; U.S. Treasury also describes Andariel as a Lazarus subgroup controlled by the RGB. | 高 | `source--mitre-live-andariel-2024`, `source--treasury-dprk-groups-2019` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Andariel](https://attack.mitre.org/groups/G0138) is a North Korean state-sponsored threat group that has been active since at least 2009. [Andariel](https://attack.mitre.org/groups/G0138) has primarily focused its operations--which have included destructive attacks--against South Korean government agencies, military organizations, and a variety of domestic companies; they have also conducted cyber financial operations against ATMs, banks, and cryptocurrency exchanges. [Andariel](https://attack.mitre.org/groups/G0138)'s notable activity includes Operation Black Mine, Operation GoldenAxe, and Campaign Rifle.(Citation: FSI Andariel Campaign Rifle July 2017)(Citation: IssueMakersLab Andariel GoldenAxe May 2017)(Citation: AhnLab Andariel Subgroup of Lazarus June 2018)(Citation: TrendMicro New Andariel Tactics July 2018)(Citation: CrowdStrike Silent Chollima Adversary September 2021)<br><br>[Andariel](https://attack.mitre.org/groups/G0138) is considered a sub-set of [Lazarus Group](https://attack.mitre.org/groups/G0032), and has been attributed to North Korea's Reconnaissance General Bureau.(Citation: Treasury North Korean Cyber Groups September 2019)<br><br>North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name [Lazarus Group](https://attack.mitre.org/groups/G0032) instead of tracking clusters or subgroups. |
| Capability | Rifdoor, gh0st RAT, Phandoor |
| Infrastructure |  |
| Victim | Information gathering and profit |
| Socio-political | North Korea |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Andariel, Silent Chollima | canonical-name | 高 | North Korea | https://asec.ahnlab.com/en/56405/<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-207a<br>https://cloud.google.com/blog/topics/threat-intelligence/apt45-north-korea-digital-military-machine |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Onyx Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Silent Chollima | canonical-name | 高 | KP | https://docs.huihoo.com/rsaconference/usa-2014/anf-t07b-the-art-of-attribution-identifying-and-pursuing-your-cyber-adversaries-final.pdf<br>https://www.microsoft.com/en-us/security/blog/2023/10/18/multiple-north-korean-threat-actors-exploiting-the-teamcity-cve-2023-42793-vulnerability/ |
| misp-threat-actor | Lazarus Group | canonical-name | 高 | KP, Korea (Democratic People's Republic of) | https://threatpost.com/operation-blockbuster-coalition-ties-destructive-attacks-to-lazarus-group/116422/<br>https://www.us-cert.gov/ncas/alerts/TA17-164A<br>https://www.us-cert.gov/ncas/alerts/TA17-318A |
| misp-microsoft-activity-group | Onyx Sleet | canonical-name | 高 | KP, North Korea | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Andariel - G0138 | mitre-external-id | 高 |  | http://www.issuemakerslab.com/research3/<br>https://adversary.crowdstrike.com/en-US/adversary/silent-chollima/<br>https://attack.mitre.org/groups/G0138 |
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
| malware--gh0st-rat | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) is a remote access tool (RAT). The source code is public and it has been used by multiple groups.(Citation: FireEye Hacking Team)(Citation: Arbor Musical Chairs Feb 2018)(Citation: Nccgroup Gh0st April 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--phandoor | Phandoor | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--rifdoor | Rifdoor | [Rifdoor](https://attack.mitre.org/software/S0433) is a remote access trojan (RAT) that shares numerous code similarities with [HotCroissant](https://attack.mitre.org/software/S0431).(Citation: Carbon Black HotCroissant April 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| Andarielハッカー、韓国の機関を新しいDora RATマルウェアで標的 | malware-campaign | 不明 | 不明 | 2024-06-04 | 北朝鮮関連のアクターAndarielが新しいGo言語ベースのDora RATマルウェアを使用。 韓国の教育機関、製造業、建設業をターゲットにした攻撃で利用された。 この攻撃は、脆弱なApache Tomcatサーバーを攻撃してマルウェアを配布。 Dora RATはリバースシェルやファイルダウンロード/アップロードが可能な単純なマルウェアの一種。 有効な証明書で署名されたDora RATが確認された。英国のソフトウェア開発者からの有効な証明書で署名されていた。 | 高 | `source--daily-cecaacd0e1f99bf64539` |
| Andarielハッカーグループ、米国組織への金融攻撃に注力 | ransomware-extortion | 不明 | 不明 | 2024-10-03 | 北朝鮮のAndarielグループが米国の組織に対して金融目的の攻撃を開始。 DtrackやNukebotなどのバックドアツールを使用し、攻撃を試みたが、ランサムウェアの展開は失敗。 攻撃は金銭的な目的である可能性が高い。 Symantecによると、このグループは米国で組織に対する恐喝攻撃を仕掛けることを続けている可能性が高い。 AndarielはLazarusグループの一部とされ、2019年以降、主にスパイ活動を行っていた。比較的最近の動向として金銭目的の攻撃も行っている。 | 高 | `source--daily-d2af83b6cab76368c85d` |
| 北朝鮮政府ハッカー、Playランサムウェア攻撃に関連 | ransomware-extortion | 不明 | 不明 | 2024-10-31 | 北朝鮮のハッカーグループAndarielがPlayランサムウェア攻撃に関与 複数のネットワークを侵害し、MimikatzやSliverなどのツールや、Andariel独自の情報窃取マルウェアであるDTrackを利用 2024年9月のインシデントで証拠が発見され、アフィリエイトかIABとしての関係が疑われる 侵入後、Playランサムウェアの展開が3ヶ月だった。 攻撃目的はサイバースパイ活動および資金調達などの可能性がある。 RaaSを利用し、制裁逃れを図っている可能性が示唆される | 中 | `source--daily-1147479b46313418b844` |
| 北朝鮮のハッキンググループが韓国の防衛請負業者を侵害 | malware-campaign | 不明 | 不明 | 2024-04-24 | 北朝鮮のハッキンググループが韓国の防衛産業を標的に 韓国警察の報告書では、Lazarus, Andariel, Kimsukyが関与している3つのインシデントを記載 ターゲットまたはその下請け組織のネットワークの脆弱性を利用しマルウェアを植え付ける インシデントの1つでは、データの抜き取りとクラウドサーバへの転送が行われた 韓国警察は、多要素認証の導入・外国からのIPアクセスのブロックなどのセキュリティ強化を勧めている | 中 | `source--daily-b9be11e58ab6c82617ab` |
| 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | malware-campaign | 不明 | 不明 | 2024-08-06 | 北朝鮮のハッカーグループがVPNのアップデートの脆弱性を悪用し、マルウェアをインストール。 攻撃者はKimsukyとAndariel（APT43とAPT45）で、韓国の産業機密を狙う。 VPNソフトウェアの通信プロトコルの脆弱性を悪用し、更新プログラムを置き換えてトロイの木馬化。遠隔操作用のDoraRATをインストール。 攻撃は産業機器や設計文書の盗難を目的としている。 NCSCが警告を発表し、セキュリティ対策を推奨。 | 中 | `source--daily-444c87a0051642065f55` |
| ハッカー、WindowsのRIDハイジャックを利用して隠れた管理者アカウントを作成 | malware-campaign | 不明 | 不明 | 2025-01-26 | 北朝鮮のハッカーグループAndarielが、WindowsのRIDハイジャック技術を使用し、低権限のアカウントを管理者権限に昇格させる攻撃を実施。 RIDハイジャックでは、低権限アカウントのRIDを管理者アカウントのRID（通常は500）に変更し、Windowsに管理者として認識させる。 この攻撃を行うには、最初にシステムへの侵入とSYSTEM権限の取得が必要。 攻撃者は、カスタムマルウェアやオープンソースツールを使用して、この攻撃を実行。 AhnLabの研究者は、この攻撃を北朝鮮のLazarusグループに関連するAndarielグループによるものと特定。 RIDハイジャッキングは、少なくとも2018年から知られており、以前から持続的な攻撃手法として認識されている。 | 中 | `source--daily-a36638e8716771007cc7` |
| DesertWolf | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| INITROY | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Mayday | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Sony | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Vanxatm | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| XEDA | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

DesertWolf; Vanxatm; Mayday; INITROY; XEDA; Sony

## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | w backdoor written in Go that we named ApolonTroy, based on strings found in the malware body. We also noticed that this group uses a variety of SOCKS proxies (T1090 [39]), including |  |  | 不明 | 不明 | 中 | `source--andariel--d8b5468150bbcc71` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | summary/2023/eset_apt_activity_report_t32022.pdf {"page": 9} Andariel Andariel Finally, we covered a campaign by Andariel, using a recent RCE vulnerability (T1190 [37]) against Confluence (CVE-2022-26134 [38]) to compromise an organization based in South Korea. This campaign used Andariel’s Tige |  |  | 不明 | 不明 | 中 | `source--andariel--d8b5468150bbcc71` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--andariel--d8b5468150bbcc71`, `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1590.005 | IP Addresses | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1592.002 | Software | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 6件
- IOC観測: 6件
- 複数攻撃で観測: 0件
- 要レビュー候補: 6件
- 非IOC artifact観測: 159件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| MITRE considers Andariel a subset of Lazarus Group; U.S. Treasury also describes Andariel as a Lazarus subgroup controlled by the RGB. | 高 | `source--mitre-live-andariel-2024`, `source--treasury-dprk-groups-2019` | verification_status=supported; Lazarus is also used as a broad umbrella label in some reporting, so operation-level attribution should retain the Andariel label where supported. The sources warn that DPRK cluster boundaries overlap; subgroup status does not imply identical tooling across all Lazarus activity. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--andariel--003e6e7235dd0b18 | readme |  | 不明 | summary/2024/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--andariel--01baffee65b61160 | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--andariel--06befef99b97990e | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--andariel--0ab64c32fed0c1e2 | The Lazarus Constellation |  | 不明 | lazarus/The_Lazarus_Constellation.pdf | report | TLP:CLEAR | 中 |
| source--andariel--17c66e445bbff587 | eset threat report h22024 |  | 不明 | summary/2024/eset-threat-report-h22024.pdf | report | TLP:CLEAR | 中 |
| source--andariel--25068ad538a6f882 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--andariel--2898f01b59b0d0f9 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--andariel--28bf9e8edbad5ea2 | eset apt activity report t32022 |  | 不明 | summary/2023/eset_apt_activity_report_t32022.pdf | report | TLP:CLEAR | 中 |
| source--andariel--29893e0bc8aee5ff | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--andariel--29f1ac892500da4d | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--andariel--2e330fbe37e80bdf | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--andariel--308c1cede67db8ba | eset apt activity report q4 2025 q1 2026 |  | 2025 | summary/2026/eset-apt-activity-report-q4-2025-q1-2026.pdf | report | TLP:CLEAR | 中 |
| source--andariel--43edff068441d484 | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--andariel--5005c5040b8c0231 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--andariel--554a96ad68fe3664 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--andariel--5722978c97c5b2c3 | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--andariel--5751a4b2400edf27 | kaspersky ics cert apt attacks on industrial organizations in h2 2022 en |  | 2022 | summary/2023/kaspersky-ics-cert-apt-attacks-on-industrial-organizations-in-h2-2022-en.pdf | report | TLP:CLEAR | 中 |
| source--andariel--58def7c5728472a3 | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--andariel--59cd94daefd3a78a | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--andariel--59fa299f5c811fbf | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--andariel--5dd536201314dc3a | North Korea’s Cyber Strategy |  | 不明 | International Strategic/Korea/North Korea’s Cyber Strategy.pdf | report | TLP:CLEAR | 中 |
| source--andariel--5f7cd2fb92322a87 | 20231013 Lazarus OP.Dream Magic |  | 2023-10-13 | lazarus/20231013_Lazarus_OP.Dream_Magic.pdf | report | TLP:CLEAR | 中 |
| source--andariel--613d127a6cc5ed3e | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--andariel--6297cb4399689e5a | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--andariel--64dd6ad3eaeb24bc | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--andariel--6914f46b1320f4d5 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--andariel--6cd27f0ea4c9c4bb | eset apt activity report q4 2023 q1 2024 |  | 2023 | summary/2024/eset-apt-activity-report-q4-2023-q1-2024.pdf | report | TLP:CLEAR | 中 |
| source--andariel--780281b12cecb8f4 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--andariel--7aa0c7490c79b91a | Global APT Research Report for the first half of 2021 360 |  | 2021 | summary/2021/Global APT Research Report for the first half of 2021-360.pdf | report | TLP:CLEAR | 中 |
| source--andariel--80cb29d55d4e4f50 | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--andariel--84506015726833ce | 2025 dia statement for the record |  | 2025 | International Strategic/USA/2025/2025_dia_statement_for_the_record.pdf | report | TLP:CLEAR | 中 |
| source--andariel--8a762d3c860f5b06 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--andariel--8a939799db78807f | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--andariel--931b4a8425a5c143 | HJS Crypto Currency Report web final |  | 不明 | summary/2026/HJS-Crypto-Currency-Report-web-final.pdf | report | TLP:CLEAR | 中 |
| source--andariel--9a562d1daa757028 | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--andariel--9ec7ebfb86c2b419 | SixMap Research Energy Sector Exposure Assessment |  | 不明 | summary/2025/SixMap-Research_Energy-Sector-Exposure-Assessment.pdf | report | TLP:CLEAR | 中 |
| source--andariel--a11a2cf94b820fe2 | eset apt activity report q2 2025 q3 2025 |  | 2025 | summary/2025/eset-apt-activity-report-q2-2025-q3-2025.pdf | report | TLP:CLEAR | 中 |
| source--andariel--a46a50622040e7c1 | 2023 Network Vulnerability Situation Research Report |  | 2023 | summary/2024/2023 Network Vulnerability Situation Research Report.pdf | report | TLP:CLEAR | 中 |
| source--andariel--a4be2e796f8b317c | eset apt activity report q42022 q12023 |  | 不明 | summary/2023/eset_apt_activity_report_q42022_q12023.pdf | report | TLP:CLEAR | 中 |
| source--andariel--a5ac56ffc0cff043 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--andariel--ae884a91170d58f1 | WithSecure Lazarus No Pineapple Threat Intelligence Report 2023 |  | 2023 | lazarus/WithSecure-Lazarus-No-Pineapple-Threat-Intelligence-Report-2023.pdf | report | TLP:CLEAR | 中 |
| source--andariel--c3bebd29c1e66aa8 | Semiannual+Ransomware+Report+ +H1+2024 |  | 2024 | cybercrime/2024/Semiannual+Ransomware+Report+-+H1+2024.pdf | report | TLP:CLEAR | 中 |
| source--andariel--c8e97d02b2bb5252 | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--andariel--ca8fb65c8226c803 | Blurred Lines of Cyber Threat Attribution |  | 不明 | International Strategic/Korea/ Blurred-Lines-of-Cyber-Threat-Attribution.pdf | report | TLP:CLEAR | 中 |
| source--andariel--cb1568c0bd15be5c | DeceptiveDevelopment and North Korean IT workers from primitive crypto theft to sophisticated AI based deception |  | 不明 | CyberMerceNary/ITWorker/DeceptiveDevelopment-and-North-Korean-IT-workers-from-primitive-crypto-theft-to-sophisticated-AI-based-deception.pdf | report | TLP:CLEAR | 中 |
| source--andariel--d0c01d59e1e94686 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--andariel--d2aa525a6225f1b3 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--andariel--d49bc49296900911 | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--andariel--d8080195ad4d0b47 | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--andariel--d8b5468150bbcc71 | andariel |  | 不明 | actor_profile/evidence/andariel.csv | structured-data | TLP:CLEAR | 中 |
| source--andariel--ed26b01dcad72357 | CrowdStrikeGlobalThreatReport2025 |  | 2025 | summary/2025/CrowdStrikeGlobalThreatReport2025.pdf | report | TLP:CLEAR | 中 |
| source--andariel--f267789fed1a6863 | Microsoft Digital Defense Report 2022 |  | 2022 | summary/2022/Microsoft Digital Defense Report 2022.pdf | report | TLP:CLEAR | 中 |
| source--andariel--f5a88429d0aa6ff9 | WithSecure Andariel 2025 |  | 2025 | lazarus/Andariel/WithSecure_Andariel_2025.pdf | report | TLP:CLEAR | 中 |
| source--daily-1147479b46313418b844 | 北朝鮮政府ハッカー、Playランサムウェア攻撃に関連 | bleepingcomputer.com | 2024-10-31 | https://www.bleepingcomputer.com/news/security/north-korean-govt-hackers-linked-to-play-ransomware-attack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-444c87a0051642065f55 | 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | bleepingcomputer.com | 2024-08-06 | https://www.bleepingcomputer.com/news/security/north-korean-hackers-exploit-vpn-update-flaw-to-install-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-a36638e8716771007cc7 | ハッカー、WindowsのRIDハイジャックを利用して隠れた管理者アカウントを作成 | bleepingcomputer.com | 2025-01-26 | https://www.bleepingcomputer.com/news/security/hackers-use-windows-rid-hijacking-to-create-hidden-admin-account/ | osint-report | TLP:CLEAR | 中 |
| source--daily-b9be11e58ab6c82617ab | 北朝鮮のハッキンググループが韓国の防衛請負業者を侵害 | bleepingcomputer.com | 2024-04-24 | https://www.bleepingcomputer.com/news/security/dprk-hacking-groups-breach-south-korean-defense-contractors/ | osint-report | TLP:CLEAR | 中 |
| source--daily-cecaacd0e1f99bf64539 | Andarielハッカー、韓国の機関を新しいDora RATマルウェアで標的 | thehackernews.com | 2024-06-04 | https://thehackernews.com/2024/06/andariel-hackers-target-south-korean.html | osint-report | TLP:CLEAR | 中 |
| source--daily-d2af83b6cab76368c85d | Andarielハッカーグループ、米国組織への金融攻撃に注力 | thehackernews.com | 2024-10-03 | https://thehackernews.com/2024/10/andariel-hacker-group-shifts-focus-to.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-live-andariel-2024 | Andariel, Group G0138 | MITRE ATT&CK | 2024-09-12 | https://attack.mitre.org/groups/G0138/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--treasury-dprk-groups-2019 | Treasury Sanctions North Korean State-Sponsored Malicious Cyber Groups | U.S. Department of the Treasury | 2019-09-13 | https://home.treasury.gov/news/press-releases/sm774 | government-designation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
