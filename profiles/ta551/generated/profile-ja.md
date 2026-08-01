# TA551 脅威アクタープロファイル

- プロファイルID: `actor--ta551`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

TA551の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA551**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| GOLD CABIN | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Shathak | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the Russia worksheet.

- 国: Russia
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [TA551](https://attack.mitre.org/groups/G0127) is a financially-motivated threat group that has been active since at least 2018. (Citation: Secureworks GOLD CABIN) The group has primarily targeted English, German, Italian, and Japanese speakers through email-based malware distribution campaigns. (Citation: Unit 42 TA551 Jan 2021) |
| Capability | Ursnif, IcedID, Valak, QakBot, Sliver |
| Infrastructure |  |
| Victim |  |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | TA551, Shathak | canonical-name | 高 | Russia | https://unit42.paloaltonetworks.com/ta551-shathak-icedid/<br>https://unit42.paloaltonetworks.com/valak-evolution/<br>https://github.com/pan-unit42/iocs/tree/master/TA551 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | GOLD CABIN | canonical-name | 高 |  | https://www.secureworks.com/research/threat-profiles/gold-cabin<br>https://attack.mitre.org/groups/G0127/<br>https://unit42.paloaltonetworks.com/atoms/monsterlibra/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | TA551 - G0127 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0127<br>https://unit42.paloaltonetworks.com/ta551-shathak-icedid/<br>https://unit42.paloaltonetworks.com/valak-evolution/ |
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
| malware--ursnif | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) is a banking trojan and variant of the Gozi malware observed being spread through various automated exploit kits, [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001)s, and malicious links.(Citation: NJCCIC Ursnif Sept 2016)(Citation: ProofPoint Ursnif Aug 2016) [Ursnif](https://attack.mitre.org/software/S0386) is associated primarily with data theft, but variants also include components (backdoors, spyware, file injectors, etc.) capable of a wide variety of behaviors.(Citation: TrendMicro Ursnif Mar 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--icedid | IcedID | [IcedID](https://attack.mitre.org/software/S0483) is a modular banking malware designed to steal financial information that has been observed in the wild since at least 2017.  [IcedID](https://attack.mitre.org/software/S0483)  has been downloaded by [Emotet](https://attack.mitre.org/software/S0367) in multiple campaigns.(Citation: IBM IcedID November 2017)(Citation: Juniper IcedID June 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--valak | Valak | [Valak](https://attack.mitre.org/software/S0476) is a multi-stage modular malware that can function as a standalone information stealer or downloader, first observed in 2019 targeting enterprises in the US and Germany.(Citation: Cybereason Valak May 2020)(Citation: Unit 42 Valak July 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--qakbot | QakBot | [QakBot](https://attack.mitre.org/software/S0650) is a modular banking trojan that has been used primarily by financially-motivated actors since at least 2007. [QakBot](https://attack.mitre.org/software/S0650) is continuously maintained and developed and has evolved from an information stealer into a delivery agent for ransomware, most notably [ProLock](https://attack.mitre.org/software/S0654) and [Egregor](https://attack.mitre.org/software/S0554).(Citation: Trend Micro Qakbot December 2020)(Citation: Red Canary Qbot)(Citation: Kaspersky QakBot September 2021)(Citation: ATT QakBot April 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--sliver | Sliver | [Sliver](https://attack.mitre.org/software/S0633) is an open source, cross-platform, red team command and control (C2) framework written in Golang. [Sliver](https://attack.mitre.org/software/S0633) includes its own package manager, "armory," for staging and downloading additional tools and payloads to the primary C2 framework.(Citation: Bishop Fox Sliver Framework August 2019)(Citation: Cybereason Sliver Undated) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イタリア | (Citation: Secureworks GOLD CABIN) The group has primarily targeted English, German, Italian, and Japanese speakers through email-based malware distribution campaigns. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | ドイツ | (Citation: Secureworks GOLD CABIN) The group has primarily targeted English, German, Italian, and Japanese speakers through email-based malware distribution campaigns. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | 日本 | (Citation: Secureworks GOLD CABIN) The group has primarily targeted English, German, Italian, and Japanese speakers through email-based malware distribution campaigns. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 欧州 | イタリア、ドイツで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.003 | Steganography | [TA551](https://attack.mitre.org/groups/G0127) has hidden encoded data for malware DLLs in a PNG.(Citation: Unit 42 TA551 Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [TA551](https://attack.mitre.org/groups/G0127) has used obfuscated variable names in a JavaScript configuration file.(Citation: Unit 42 Valak July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [TA551](https://attack.mitre.org/groups/G0127) has masked malware DLLs as dat and jpg files.(Citation: Unit 42 TA551 Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--ta551--a793ec3f0d3326bb` |
| Stealth | T1036.003 | Rename Legitimate Utilities | summary/2021/2021-Threat-Detection-Report.pdf {"page": 2} TA551 64 #9 T1569 System Services 69 T1569.002 Service Execution 70 #10 T1036 Masquerading 73 T1036.003 Rename System Utilities 74 #1 TA551 79 #2 Cobalt Strike 84 #3 Qbot 88 #4 IcedID 92 #5 Mimikatz 96 #6 Shlayer 100 #7 Dridex 103 #8 Emotet 107 #9 TrickBot |  |  | 不明 | 不明 | 中 | `source--ta551--a793ec3f0d3326bb` |
| Execution | T1059.003 | Windows Command Shell | [TA551](https://attack.mitre.org/groups/G0127) has used <code>cmd.exe</code> to execute commands.(Citation: Unit 42 TA551 Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [TA551](https://attack.mitre.org/groups/G0127) has used HTTP for C2 communications.(Citation: Unit 42 Valak July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [TA551](https://attack.mitre.org/groups/G0127) has retrieved DLLs and installer binaries for malware execution from C2.(Citation: Unit 42 TA551 Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | [TA551](https://attack.mitre.org/groups/G0127) has used encoded ASCII text for initial C2 communications.(Citation: Unit 42 Valak July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [TA551](https://attack.mitre.org/groups/G0127) has prompted users to enable macros within spearphishing attachments to install malware.(Citation: Unit 42 TA551 Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | [TA551](https://attack.mitre.org/groups/G0127) has used mshta.exe to execute malicious payloads.(Citation: Unit 42 TA551 Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--ta551--a793ec3f0d3326bb` |
| Stealth | T1218.010 | Regsvr32 | [TA551](https://attack.mitre.org/groups/G0127) has used regsvr32.exe to load malicious DLLs.(Citation: Unit 42 Valak July 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [TA551](https://attack.mitre.org/groups/G0127) has used rundll32.exe to load malicious DLLs.(Citation: Unit 42 TA551 Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [TA551](https://attack.mitre.org/groups/G0127) has sent spearphishing attachments with password protected ZIP files.(Citation: Unit 42 Valak July 2020)(Citation: Unit 42 TA551 Jan 2021)(Citation: Secureworks GOLD CABIN) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1568.002 | Domain Generation Algorithms | [TA551](https://attack.mitre.org/groups/G0127) has used a DGA to generate URLs from executed macros.(Citation: Unit 42 TA551 Jan 2021)(Citation: Secureworks GOLD CABIN) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569 | System Services | summary/2021/2021-Threat-Detection-Report.pdf {"page": 2} TA551 64 #9 T1569 System Services 69 T1569.002 Service Execution 70 #10 T1036 Masquerading 73 T1036.003 Rename System Utilities 74 #1 TA551 79 #2 Cobalt Strike 84 #3 Qbot 88 #4 IcedID 92 #5 Mimikatz 96 #6 Shlayer 100 #7 Dridex 103 #8 Emotet 107 #9 TrickBot |  |  | 不明 | 不明 | 中 | `source--ta551--a793ec3f0d3326bb` |
| Execution | T1569.002 | Service Execution | summary/2021/2021-Threat-Detection-Report.pdf {"page": 2} TA551 64 #9 T1569 System Services 69 T1569.002 Service Execution 70 #10 T1036 Masquerading 73 T1036.003 Rename System Utilities 74 #1 TA551 79 #2 Cobalt Strike 84 #3 Qbot 88 #4 IcedID 92 #5 Mimikatz 96 #6 Shlayer 100 #7 Dridex 103 #8 Emotet 107 #9 TrickBot |  |  | 不明 | 不明 | 中 | `source--ta551--a793ec3f0d3326bb` |
| Reconnaissance | T1589.002 | Email Addresses | [TA551](https://attack.mitre.org/groups/G0127) has used spoofed company emails that were acquired from email clients on previously infected hosts to target other individuals.(Citation: Unit 42 TA551 Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 10件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 34件（`artifacts.csv`）

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
| source--ta551--a793ec3f0d3326bb | ta551 |  | 不明 | actor_profile/evidence/ta551.csv | structured-data | TLP:CLEAR | 中 |
| source--ta551--17d0644c5653d776 | 2021 Threat Detection Report |  | 2021 | summary/2021/2021-Threat-Detection-Report.pdf | report | TLP:CLEAR | 中 |
| source--ta551--60000b3add4c5855 | Looking back on the incidents in 2020 JPCERT en |  | 2020 | summary/2021/Looking back on the incidents in 2020_JPCERT_en.pdf | report | TLP:CLEAR | 中 |
| source--ta551--fe9b71a4f92cc1ee | 2021 Adversary Infrastructure Report |  | 2021 | summary/2022/2021 Adversary Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--ta551--e0ab9a1bb7e06337 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--ta551--262b580cdbb20b55 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
