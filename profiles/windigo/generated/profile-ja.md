# Windigo 脅威アクタープロファイル

- プロファイルID: `actor--windigo`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Windigoの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Windigo**
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
| Adversary | The [Windigo](https://attack.mitre.org/groups/G0124) group has been operating since at least 2011, compromising thousands of Linux and Unix servers using the [Ebury](https://attack.mitre.org/software/S0377) SSH backdoor to create a spam botnet. Despite law enforcement intervention against the creators, [Windigo](https://attack.mitre.org/groups/G0124) operators continued updating [Ebury](https://attack.mitre.org/software/S0377) through 2019.(Citation: ESET Windigo Mar 2014)(Citation: CERN Windigo June 2019) |
| Capability | Ebury |
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
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Windigo - G0124 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0124<br>https://security.web.cern.ch/advisories/windigo/windigo.shtml<br>https://www.welivesecurity.com/2014/03/18/operation-windigo-the-vivisection-of-a-large-linux-server-side-credential-stealing-malware-campaign/ |
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
| malware--ebury | Ebury | [Ebury](https://attack.mitre.org/software/S0377) is an OpenSSH backdoor and credential stealer targeting Linux servers and container hosts developed by [Windigo](https://attack.mitre.org/groups/G0124). [Ebury](https://attack.mitre.org/software/S0377) is primarily installed through modifying shared libraries (`.so` files) executed by the legitimate OpenSSH program. First seen in 2009, [Ebury](https://attack.mitre.org/software/S0377) has been used to maintain a botnet of servers, deploy additional malware, and steal cryptocurrency wallets, credentials, and credit card details.(Citation: ESET Ebury Feb 2014)(Citation: BleepingComputer Ebury March 2017)(Citation: ESET Ebury Oct 2017)(Citation: ESET Ebury May 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to gather credentials in files left on disk by OpenSSH backdoors.(Citation: ESET ForSSHe December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | [Windigo](https://attack.mitre.org/groups/G0124) has used a Perl script for information gathering.(Citation: ESET ForSSHe December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to detect which Linux distribution and version is currently installed on the system.(Citation: ESET ForSSHe December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to check for the presence of files created by OpenSSH backdoors.(Citation: ESET ForSSHe December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | [Windigo](https://attack.mitre.org/groups/G0124) has delivered a generic Windows proxy Win32/Glubteta.M. [Windigo](https://attack.mitre.org/groups/G0124) has also used multiple reverse proxy chains as part of their C2 infrastructure.(Citation: ESET Windigo Mar 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | [Windigo](https://attack.mitre.org/groups/G0124) has distributed Windows malware via drive-by downloads.(Citation: ESET Windigo Mar 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518 | Software Discovery | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to detect installed software on targeted systems.(Citation: ESET ForSSHe December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 8件（`artifacts.csv`）

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
| source--windigo--212f761cc601a3e5 | windigo |  | 不明 | actor_profile/evidence/windigo.csv | structured-data | TLP:CLEAR | 中 |
| source--windigo--75fd1df34b37d9d0 | sednit update analysis zebrocy |  | 不明 | APT28/history-report-pdf/sednit-update-analysis-zebrocy_.pdf | report | TLP:CLEAR | 中 |
| source--windigo--c71a50b68b154334 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--windigo--8d34216249e080cd | eset threat report h12024 |  | 不明 | summary/2024/eset-threat-report-h12024.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
