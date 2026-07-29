# Molerats 脅威アクタープロファイル

- プロファイルID: `actor--molerats`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Moleratsの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Molerats**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Gaza Cybergang | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Operation Molerats | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Gaza Hacker Team | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Middle East row 3; mapping requires review. |
| ALUMINUM SARATOGA | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Middle East row 3; mapping requires review. |
| MITRE: G0021 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Middle East row 3; mapping requires review. |
| Gaza | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Middle East row 3; mapping requires review. |

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
| Adversary | [Molerats](https://attack.mitre.org/groups/G0021) is an Arabic-speaking, politically-motivated threat group that has been operating since 2012. The group's victims have primarily been in the Middle East, Europe, and the United States.(Citation: DustySky)(Citation: DustySky2)(Citation: Kaspersky MoleRATs April 2019)(Citation: Cybereason Molerats Dec 2020) |
| Capability | Spark, SharpStage, DropBook, DustySky, MoleNet, PoisonIvy, NeD Worm, Scote, Don’t Kill My Cat (DKMC), RTFs Exploiting CVE-2017-0199 |
| Infrastructure |  |
| Victim | Israel, Palestine, Egypt, Saudi Arabia, United Arab Emirates, Turkey, USA. (Targeted sectors include governmental and diplomatic institutions, including embassies; companies from the aerospace and defence Industries; financial institutions; journalists; software developers.<br>) |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Molerats, Extreme Jackal, Gaza Cybergang | canonical-name | 高 | [Gaza] | https://www.sentinelone.com/labs/gaza-cybergang-unified-front-targeting-hamas-opposition/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Molerats%2C+Extreme+Jackal%2C+Gaza+Cybergang&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Molerats | canonical-name | 高 | PS, Palestine | https://www.fireeye.com/blog/threat-research/2013/08/operation-molerats-middle-east-cyber-attacks-using-poison-ivy.html<br>https://ti.360.net/blog/articles/suspected-molerats-new-attack-in-the-middle-east/<br>https://ti.360.net/blog/articles/suspected-molerats-new-attack-in-the-middle-east-en/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Molerats - G0021 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0021 |
| misp-mitre-intrusion-set | Molerats - G0021 | mitre-external-id | 高 |  | http://www.clearskysec.com/wp-content/uploads/2016/06/Operation-DustySky2_-6.2016_TLP_White.pdf<br>https://attack.mitre.org/groups/G0021<br>https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/ |
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
| malware--spark | Spark | <br>[Spark](https://attack.mitre.org/software/S0543) is a Windows backdoor and has been in use since as early as 2017.(Citation: Unit42 Molerat Mar 2020)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sharpstage | SharpStage | [SharpStage](https://attack.mitre.org/software/S0546) is a .NET malware with backdoor capabilities.(Citation: Cybereason Molerats Dec 2020)(Citation: BleepingComputer Molerats Dec 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--dropbook | DropBook | [DropBook](https://attack.mitre.org/software/S0547) is a Python-based backdoor compiled with PyInstaller.(Citation: Cybereason Molerats Dec 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--dustysky | DustySky | [DustySky](https://attack.mitre.org/software/S0062) is multi-stage malware written in .NET that has been used by [Molerats](https://attack.mitre.org/groups/G0021) since May 2015. (Citation: DustySky) (Citation: DustySky2)(Citation: Kaspersky MoleRATs April 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--molenet | MoleNet | [MoleNet](https://attack.mitre.org/software/S0553) is a downloader tool with backdoor capabilities that has been observed in use since at least 2019.(Citation: Cybereason Molerats Dec 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--poisonivy | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) is a popular remote access tool (RAT) that has been used by many groups.(Citation: FireEye Poison Ivy)(Citation: Symantec Elderwood Sept 2012)(Citation: Symantec Darkmoon Aug 2005) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ned-worm | NeD Worm | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--scote | Scote | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--don-t-kill-my-cat-dkmc | Don’t Kill My Cat (DKMC) | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--rtfs-exploiting-cve-2017-0199 | RTFs Exploiting CVE-2017-0199 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| Molerats | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| DustySky | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| TopHat | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Molerats; DustySky; TopHat

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | United Arab Emirates | Targeting text mentions united arab emirates. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Saudi Arabia | Targeting text mentions saudi arabia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Turkey | Targeting text mentions turkey. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Israel | Targeting text mentions israel. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Egypt | Targeting text mentions egypt. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Finance | Targeting text indicates the Finance sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Media | Targeting text indicates the Media sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.015 | Compression | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.007 | Msiexec | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 0件（`artifacts.csv`）

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
| source--molerats--9c84c225d4443807 | README |  | 不明 | Molerats/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--molerats--4f02c9f4ca6dd789 | Welcome Chat |  | 不明 | Molerats/Welcome-Chat.txt | text-data | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
