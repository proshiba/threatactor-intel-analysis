# SilverTerrier 脅威アクタープロファイル

- プロファイルID: `actor--silverterrier`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

SilverTerrierの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **SilverTerrier**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Nigeria | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 50; mapping requires review. |

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
| Adversary | [SilverTerrier](https://attack.mitre.org/groups/G0083) is a Nigerian threat group that has been seen active since 2014. [SilverTerrier](https://attack.mitre.org/groups/G0083) mainly targets organizations in high technology, higher education, and manufacturing.(Citation: Unit42 SilverTerrier 2018)(Citation: Unit42 SilverTerrier 2016) |
| Capability | NETWIRE, DarkComet, NanoCore, Lokibot, Agent Tesla, Predator Pain, Pony, KeyBase, ISpySoftware, ISR Stealer, Zeus and Atmos, DarkComet and NanoCore |
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
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | SilverTerrier | canonical-name | 高 | NG | https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/Unit_42/silverterrier-next-evolution-in-nigerian-cybercrime.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | SilverTerrier - G0083 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0083<br>https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/unit42-silverterrier-rise-of-nigerian-business-email-compromise<br>https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/Unit_42/silverterrier-next-evolution-in-nigerian-cybercrime.pdf |
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
| malware--netwire | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) is a publicly available, multiplatform remote administration tool (RAT) that has been used by criminal and APT groups since at least 2012.(Citation: FireEye APT33 Sept 2017)(Citation: McAfee Netwire Mar 2015)(Citation: FireEye APT33 Webinar Sept 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--darkcomet | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) is a Windows remote administration tool and backdoor.(Citation: TrendMicro DarkComet Sept 2014)(Citation: Malwarebytes DarkComet March 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--nanocore | NanoCore | [NanoCore](https://attack.mitre.org/software/S0336) is a modular remote access tool developed in .NET that can be used to spy on victims and steal information. It has been used by threat actors since 2013.(Citation: DigiTrust NanoCore Jan 2017)(Citation: Cofense NanoCore Mar 2018)(Citation: PaloAlto NanoCore Feb 2016)(Citation: Unit 42 Gorgon Group Aug 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lokibot | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) is a widely distributed information stealer that was first reported in 2015. It is designed to steal sensitive information such as usernames, passwords, cryptocurrency wallets, and other credentials. [Lokibot](https://attack.mitre.org/software/S0447) can also create a backdoor into infected systems to allow an attacker to install additional payloads.(Citation: Infoblox Lokibot January 2019)(Citation: Morphisec Lokibot April 2020)(Citation: CISA Lokibot September 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--agent-tesla | Agent Tesla | [Agent Tesla](https://attack.mitre.org/software/S0331) is a spyware Trojan written for the .NET framework that has been observed since at least 2014.(Citation: Fortinet Agent Tesla April 2018)(Citation: Bitdefender Agent Tesla April 2020)(Citation: Malwarebytes Agent Tesla April 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--predator-pain | Predator Pain | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--pony | Pony | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--keybase | KeyBase | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--ispysoftware | ISpySoftware | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--isr-stealer | ISR Stealer | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--zeus-and-atmos | Zeus and Atmos | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--darkcomet-and-nanocore | DarkComet and NanoCore | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 教育・研究 | [SilverTerrier](https://attack.mitre.org/groups/G0083) mainly targets organizations in high technology, higher education, and manufacturing.(Citation: Unit42 SilverTerrier 2018)(Citation: Unit42 SilverTerrier 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 製造・産業 | [SilverTerrier](https://attack.mitre.org/groups/G0083) mainly targets organizations in high technology, higher education, and manufacturing.(Citation: Unit42 SilverTerrier 2018)(Citation: Unit42 SilverTerrier 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1071.001 | Web Protocols | [SilverTerrier](https://attack.mitre.org/groups/G0083) uses HTTP for C2 communications.(Citation: Unit42 SilverTerrier 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.002 | File Transfer Protocols | [SilverTerrier](https://attack.mitre.org/groups/G0083) uses FTP for C2 communications.(Citation: Unit42 SilverTerrier 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.003 | Mail Protocols | [SilverTerrier](https://attack.mitre.org/groups/G0083) uses SMTP for C2 communications.(Citation: Unit42 SilverTerrier 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | [SilverTerrier](https://attack.mitre.org/groups/G0083) targets organizations in high technology, higher education, and manufacturing for business email compromise (BEC) campaigns with the goal of financial theft.(Citation: Unit42 SilverTerrier 2018)(Citation: Unit42 SilverTerrier 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 5件（`artifacts.csv`）

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
| source--silverterrier--ac1951232182fb96 | silverterrier |  | 不明 | actor_profile/evidence/silverterrier.csv | structured-data | TLP:CLEAR | 中 |
| source--silverterrier--1edaedb8424c87d2 | 2022 unit42 incident response report final |  | 2022 | summary/2022/2022-unit42-incident-response-report-final.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
