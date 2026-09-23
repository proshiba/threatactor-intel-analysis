# Molerats 脅威アクタープロファイル

- プロファイルID: `actor--molerats`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Moleratsの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Molerats**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Gaza Cybergang | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Operation Molerats | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |

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
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Molerats, Extreme Jackal, Gaza Cybergang | canonical-name | 高 | [Gaza] | https://www.sentinelone.com/labs/gaza-cybergang-unified-front-targeting-hamas-opposition/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Molerats%2C+Extreme+Jackal%2C+Gaza+Cybergang&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Molerats | canonical-name | 高 | PS, Palestine | https://www.fireeye.com/blog/threat-research/2013/08/operation-molerats-middle-east-cyber-attacks-using-poison-ivy.html<br>https://ti.360.net/blog/articles/suspected-molerats-new-attack-in-the-middle-east/<br>https://ti.360.net/blog/articles/suspected-molerats-new-attack-in-the-middle-east-en/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Molerats - G0021 | mitre-external-id | 高 |  | http://www.clearskysec.com/wp-content/uploads/2016/06/Operation-DustySky2_-6.2016_TLP_White.pdf<br>https://attack.mitre.org/groups/G0021<br>https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/ |
| misp-mitre-intrusion-set | Molerats - G0021 | mitre-external-id | 高 |  | http://www.clearskysec.com/wp-content/uploads/2016/06/Operation-DustySky2_-6.2016_TLP_White.pdf<br>https://attack.mitre.org/groups/G0021<br>https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/ |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Molerats | canonical-name | 高 |  |  |

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
| malware--dropbook | DropBook | [DropBook](https://attack.mitre.org/software/S0547) is a Python-based backdoor compiled with PyInstaller.(Citation: Cybereason Molerats Dec 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--dustysky | DustySky | [DustySky](https://attack.mitre.org/software/S0062) is multi-stage malware written in .NET that has been used by [Molerats](https://attack.mitre.org/groups/G0021) since May 2015. (Citation: DustySky) (Citation: DustySky2)(Citation: Kaspersky MoleRATs April 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--molenet | MoleNet | [MoleNet](https://attack.mitre.org/software/S0553) is a downloader tool with backdoor capabilities that has been observed in use since at least 2019.(Citation: Cybereason Molerats Dec 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--poisonivy | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) is a popular remote access tool (RAT) that has been used by many groups.(Citation: FireEye Poison Ivy)(Citation: Symantec Elderwood Sept 2012)(Citation: Symantec Darkmoon Aug 2005) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--sharpstage | SharpStage | [SharpStage](https://attack.mitre.org/software/S0546) is a .NET malware with backdoor capabilities.(Citation: Cybereason Molerats Dec 2020)(Citation: BleepingComputer Molerats Dec 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--spark | Spark | <br>[Spark](https://attack.mitre.org/software/S0543) is a Windows backdoor and has been in use since as early as 2017.(Citation: Unit42 Molerat Mar 2020)  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

Molerats; DustySky; TopHat

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | The group's victims have primarily been in the Middle East, Europe, and the United States.(Citation: DustySky)(Citation: DustySky2)(Citation: Kaspersky MoleRATs April 2019)(Citation: Cybereason Molerats Dec 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| regions | 中東 | MITRE ATT&CKのGroup概要でMoleratsの標的範囲として中東が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| regions | 欧州 | MITRE ATT&CKのGroup概要でMoleratsの標的範囲として欧州が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.015 | Compression | [Molerats](https://attack.mitre.org/groups/G0021) has delivered compressed executables within ZIP files to victims.(Citation: Kaspersky MoleRATs April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Molerats](https://attack.mitre.org/groups/G0021) has created scheduled tasks to persistently run VBScripts.(Citation: Unit42 Molerat Mar 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1057 | Process Discovery | [Molerats](https://attack.mitre.org/groups/G0021) actors obtained a list of active processes on the victim and sent them to C2 servers.(Citation: DustySky) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.001 | PowerShell | [Molerats](https://attack.mitre.org/groups/G0021) used PowerShell implants on target machines.(Citation: Kaspersky MoleRATs April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.005 | Visual Basic | [Molerats](https://attack.mitre.org/groups/G0021) used various implants, including those built with VBScript, on target machines.(Citation: Kaspersky MoleRATs April 2019)(Citation: Unit42 Molerat Mar 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.007 | JavaScript | [Molerats](https://attack.mitre.org/groups/G0021) used various implants, including those built with JS, on target machines.(Citation: Kaspersky MoleRATs April 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [Molerats](https://attack.mitre.org/groups/G0021) used executables to download malicious files from different sources.(Citation: Kaspersky MoleRATs April 2019)(Citation: Unit42 Molerat Mar 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Molerats](https://attack.mitre.org/groups/G0021) decompresses ZIP files once on the victim machine.(Citation: Kaspersky MoleRATs April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.001 | Malicious Link | [Molerats](https://attack.mitre.org/groups/G0021) has sent malicious links via email trick users into opening a RAR archive and running an executable.(Citation: Kaspersky MoleRATs April 2019)(Citation: Unit42 Molerat Mar 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [Molerats](https://attack.mitre.org/groups/G0021) has sent malicious files via email that tricked users into clicking Enable Content to run an embedded macro and to download malicious archives.(Citation: Kaspersky MoleRATs April 2019)(Citation: Unit42 Molerat Mar 2020)(Citation: Cybereason Molerats Dec 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1218.007 | Msiexec | [Molerats](https://attack.mitre.org/groups/G0021) has used msiexec.exe to execute an MSI payload.(Citation: Unit42 Molerat Mar 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Molerats](https://attack.mitre.org/groups/G0021) saved malicious files within the AppData and Startup folders to maintain persistence.(Citation: Kaspersky MoleRATs April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1553.002 | Code Signing | [Molerats](https://attack.mitre.org/groups/G0021) has used forged Microsoft code-signing certificates on malware.(Citation: FireEye Operation Molerats) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [Molerats](https://attack.mitre.org/groups/G0021) used the public tool BrowserPasswordDump10 to dump passwords saved in browsers on victims.(Citation: DustySky) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Molerats](https://attack.mitre.org/groups/G0021) has sent phishing emails with malicious Microsoft Word and PDF attachments.(Citation: Kaspersky MoleRATs April 2019)(Citation: Unit42 Molerat Mar 2020)(Citation: Cybereason Molerats Dec 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.002 | Spearphishing Link | [Molerats](https://attack.mitre.org/groups/G0021) has sent phishing emails with malicious links included.(Citation: Kaspersky MoleRATs April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--molerats--9c84c225d4443807 | README |  | 不明 | Molerats/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--molerats--4f02c9f4ca6dd789 | Welcome Chat |  | 不明 | Molerats/Welcome-Chat.txt | text-data | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
