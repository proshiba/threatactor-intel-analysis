# Evilnum 脅威アクタープロファイル

- プロファイルID: `actor--evilnum`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Evilnumの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Evilnum**
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

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial-gain | Financially motivated intrusion or fraud. | 高 | `source--mitre-attack-19-1`, `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description. |

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
| etda-threat-group-cards | Evilnum | canonical-name | 高 |  | https://unit42.paloaltonetworks.com/cardinal-rat-sins-again-targets-israeli-fin-tech-firms/<br>https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/<br>https://github.com/eset/malware-ioc/tree/master/evilnum |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Evilnum | canonical-name | 高 |  | https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/<br>https://securelist.com/deathstalker-mercenary-triumvirate/98177/<br>https://securelist.com/what-did-deathstalker-hide-between-two-ferns/99616/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Evilnum - G0120 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0120<br>https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/ |
| misp-mitre-intrusion-set | Evilnum - G0120 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0120<br>https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/ |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Evilnum | canonical-name | 高 |  |  |

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
| malware--evilnum | EVILNUM | [EVILNUM](https://attack.mitre.org/software/S0568) is fully capable backdoor that was first identified in 2018. [EVILNUM](https://attack.mitre.org/software/S0568) is used by the APT group [Evilnum](https://attack.mitre.org/groups/G0120) which has the same name.(Citation: ESET EvilNum July 2020)(Citation: Prevailion EvilNum May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--more-eggs | More_eggs | [More_eggs](https://attack.mitre.org/software/S0284) is a JScript backdoor used by [Cobalt Group](https://attack.mitre.org/groups/G0080) and [FIN6](https://attack.mitre.org/groups/G0037). Its name was given based on the variable "More_eggs" being present in its code. There are at least two different versions of the backdoor being used, version 2.0 and version 4.4. (Citation: Talos Cobalt Group July 2018)(Citation: Security Intelligence More Eggs Aug 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.007 | JavaScript | [Evilnum](https://attack.mitre.org/groups/G0120) has used malicious JavaScript files on the victim's machine.(Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1070.004 | File Deletion | [Evilnum](https://attack.mitre.org/groups/G0120) has deleted files used during infection.(Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [Evilnum](https://attack.mitre.org/groups/G0120) can deploy additional components or tools as needed.(Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.001 | Malicious Link | [Evilnum](https://attack.mitre.org/groups/G0120) has sent spearphishing emails designed to trick the recipient into opening malicious shortcut links which downloads a .LNK file.(Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1219.002 | Remote Desktop Software | [EVILNUM](https://attack.mitre.org/software/S0568) has used the malware variant, TerraTV, to run a legitimate TeamViewer application to connect to compromised machines.(Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery, Stealth | T1497.001 | System Checks | [Evilnum](https://attack.mitre.org/groups/G0120) has used a component called TerraLoader to check certain hardware and file information to detect sandboxed environments. (Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1539 | Steal Web Session Cookie | [Evilnum](https://attack.mitre.org/groups/G0120) can steal cookies and session information from browsers.(Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | [Evilnum](https://attack.mitre.org/groups/G0120) has used PowerShell to bypass UAC.(Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1553.005 | Mark-of-the-Web Bypass | e": 31} Evilnum oses. In most scenarios, adversaries embed VBA content into Spearphishing Attachment [T1566.001] payloads, and execute the payload through the [T1553.005] technique to evade the Mark-of-the-Web (MOTW) controls [26]. Evilnum APT group is known for leveraging a relatively uncommon technique called the VBA code stomping [T1564.007] technique, which includes destroying the source code and storing only a compiled version of the VBA ma |  |  | 不明 | 不明 | 中 | `source--evilnum--1abbd9570b6aa88b` |
| Credential Access | T1555 | Credentials from Password Stores | [Evilnum](https://attack.mitre.org/groups/G0120) can collect email credentials from victims.(Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1564.007 | VBA Stomping | ique to evade the Mark-of-the-Web (MOTW) controls [26]. Evilnum APT group is known for leveraging a relatively uncommon technique called the VBA code stomping [T1564.007] technique, which includes destroying the source code and storing only a compiled version of the VBA macro code |  |  | 不明 | 不明 | 中 | `source--evilnum--1abbd9570b6aa88b` |
| Initial Access | T1566.001 | Spearphishing Attachment | summary/2023/RedReport2023-Picus.pdf {"page": 31} Evilnum oses. In most scenarios, adversaries embed VBA content into Spearphishing Attachment [T1566.001] payloads, and execute the payload through the [T1553.005] technique to evade the Mark-of-the-Web (MOTW) controls [26]. Evilnum APT group is known for leveraging a relatively uncommon technique called the VBA code stomping [T1564.007] technique, which includes destroying the sou |  |  | 不明 | 不明 | 中 | `source--evilnum--1abbd9570b6aa88b` |
| Initial Access | T1566.002 | Spearphishing Link | [Evilnum](https://attack.mitre.org/groups/G0120) has sent spearphishing emails containing a link to a zip file hosted on Google Drive.(Citation: ESET EvilNum July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Stealth | T1574.001 | DLL | [Evilnum](https://attack.mitre.org/groups/G0120) has used the malware variant, TerraTV, to load a malicious DLL placed in the TeamViewer directory, instead of the original Windows DLL located in a system folder.(Citation: ESET EvilNum July 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 9件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- 1 alias lead(s) remain non-canonical pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--evilnum--1abbd9570b6aa88b | evilnum |  | 不明 | actor_profile/evidence/evilnum.csv | structured-data | TLP:CLEAR | 中 |
| source--evilnum--f49271f9f937ab2f | Raport analize Teknikat Taktikat Procedurat per sulmuesit Iraniane |  | 不明 | International Strategic/Iran/Raport-analize-Teknikat-Taktikat-Procedurat-per-sulmuesit-Iraniane.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--416738688a009f23 | Unmasking VenomSpider Report Final |  | 不明 | International Strategic/Russia/GoldenChickens/Unmasking_VenomSpider_Report-Final.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--3c819fc37ed9c2d4 | Adversary Infrastructure Report 2020 |  | 2020 | summary/2021/Adversary Infrastructure Report 2020.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--ffb376a3e86d97b4 | 2021 Adversary Infrastructure Report |  | 2021 | summary/2022/2021 Adversary Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--b2f6c87b07e4f482 | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--3688ec6920b85b90 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--f65839b1088faa82 | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--4adad310fb929c4e | Global APT 2023 Mid Year Report QIANXIN |  | 2023 | summary/2023/Global APT 2023 Mid-Year Report-QIANXIN.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--60f22cf2e62d415e | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--evilnum--282132beb194d2d6 | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--9aa75c4d046cd53b | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--evilnum--d962451e1fcf7e1b | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
