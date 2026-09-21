# RTM 脅威アクタープロファイル

- プロファイルID: `actor--rtm`
- 状態: draft
- 更新日時: 2026-09-21T04:18:00Z
- 構造バージョン: 1.3.0

## エグゼクティブサマリー

RTMの標準化プロファイル。リポジトリ内の専用資料0件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **RTM**
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
| etda-threat-group-cards | RTM | canonical-name | 高 | Russia | https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=RTM&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | RTM | canonical-name | 高 |  | https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf<br>https://attack.mitre.org/groups/G0048/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | RTM - G0048 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0048<br>https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf |
| misp-mitre-intrusion-set | RTM - G0048 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0048<br>https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | RTM | canonical-name | 高 |  |  |

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
| malware--rtm | RTM | [RTM](https://attack.mitre.org/software/S0148) is custom malware written in Delphi. It is used by the group of the same name ([RTM](https://attack.mitre.org/groups/G0048)). Newer versions of the malware have been reported publicly as Redaman.(Citation: ESET RTM Feb 2017)(Citation: Unit42 Redaman January 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1102.001 | Dead Drop Resolver | [RTM](https://attack.mitre.org/groups/G0048) has used an RSS feed on Livejournal to update a list of encrypted C2 server names.(Citation: ESET RTM Feb 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1189 | Drive-by Compromise | [RTM](https://attack.mitre.org/groups/G0048) has distributed its malware via the RIG and SUNDOWN exploit kits, as well as online advertising network <code>Yandex.Direct</code>.(Citation: ESET RTM Feb 2017)(Citation: ESET Buhtrap and Buran April 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [RTM](https://attack.mitre.org/groups/G0048) has attempted to lure victims into opening e-mail attachments to execute malicious code.(Citation: Group IB RTM August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1219.002 | Remote Desktop Software | [RTM](https://attack.mitre.org/groups/G0048) has used a modified version of TeamViewer and Remote Utilities for remote access.(Citation: Group IB RTM August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [RTM](https://attack.mitre.org/groups/G0048) has used Registry run keys to establish persistence for the [RTM](https://attack.mitre.org/software/S0148) Trojan and other tools, such as a modified version of TeamViewer remote desktop software.(Citation: ESET RTM Feb 2017)(Citation: Group IB RTM August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [RTM](https://attack.mitre.org/groups/G0048) has used spearphishing attachments to distribute its malware.(Citation: Group IB RTM August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Stealth | T1574.001 | DLL | [RTM](https://attack.mitre.org/groups/G0048) has used search order hijacking to force TeamViewer to load a malicious DLL.(Citation: Group IB RTM August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
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
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
