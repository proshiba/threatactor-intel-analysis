# RedEcho 脅威アクタープロファイル

- プロファイルID: `actor--redecho`
- 状態: draft
- 更新日時: 2026-07-29T15:20:23Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

RedEchoの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **RedEcho**
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

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| APT41 | overlaps-with | [RedEcho](https://attack.mitre.org/groups/G1042) overlaps with various other PRC-linked threat groups, such as [APT41](https://attack.mitre.org/groups/G0096), and is linked to [ShadowPad](https://attack.mitre.org/software/S0596) malware use through shared infrastructure.(Citation: RecordedFuture RedEcho 2021)(Citation: RecordedFuture RedEcho 2022) | 高 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [RedEcho](https://attack.mitre.org/groups/G1042) is a People’s Republic of China-related threat actor associated with long-running intrusions in Indian critical infrastructure entities. [RedEcho](https://attack.mitre.org/groups/G1042) overlaps with various other PRC-linked threat groups, such as [APT41](https://attack.mitre.org/groups/G0096), and is linked to [ShadowPad](https://attack.mitre.org/software/S0596) malware use through shared infrastructure.(Citation: RecordedFuture RedEcho 2021)(Citation: RecordedFuture RedEcho 2022) |
| Capability | ShadowPad |
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
| etda-threat-group-cards | RedEcho | canonical-name | 高 | China | https://go.recordedfuture.com/redecho-insikt-group-report<br>https://therecord.media/redecho-group-parks-domains-after-public-exposure/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=RedEcho&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | RedEcho | canonical-name | 高 |  | https://www.recordedfuture.com/redecho-targeting-indian-power-sector/<br>https://therecord.media/redecho-group-parks-domains-after-public-exposure/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | RedEcho - G1042 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1042<br>https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf<br>https://go.recordedfuture.com/hubfs/reports/ta-2022-0406.pdf |
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
| malware--shadowpad | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) is a modular backdoor that was first identified in a supply chain compromise of the NetSarang software in mid-July 2017. The malware was originally thought to be exclusively used by [APT41](https://attack.mitre.org/groups/G0096), but has since been observed to be used by various Chinese threat activity groups. (Citation: Recorded Future RedEcho Feb 2021)(Citation: Securelist ShadowPad Aug 2017)(Citation: Kaspersky ShadowPad Aug 2017)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1071.001 | Web Protocols | [RedEcho](https://attack.mitre.org/groups/G1042) network activity is associated with SSL traffic via TCP 443 and proxied HTTP traffic over non-standard ports.(Citation: RecordedFuture RedEcho 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1568 | Dynamic Resolution | [RedEcho](https://attack.mitre.org/groups/G1042) used dynamic DNS domains associated with malicious infrastructure.(Citation: RecordedFuture RedEcho 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [RedEcho](https://attack.mitre.org/groups/G1042) has used non-standard ports such as TCP 8080 for HTTP communication.(Citation: RecordedFuture RedEcho 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.002 | Asymmetric Cryptography | [RedEcho](https://attack.mitre.org/groups/G1042) uses SSL for network communication.(Citation: RecordedFuture RedEcho 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [RedEcho](https://attack.mitre.org/groups/G1042) has registered domains spoofing Indian critical infrastructure entities.(Citation: RecordedFuture RedEcho 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 10件（`artifacts.csv`）

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
| source--redecho--4a282ff8f30b9f93 | redecho |  | 不明 | actor_profile/evidence/redecho.csv | structured-data | TLP:CLEAR | 中 |
| source--redecho--677a92c5fbf0701e | RedFoxtrot group |  | 不明 | International Strategic/China/RedFoxtrot_group.pdf | report | TLP:CLEAR | 中 |
| source--redecho--d5e724439603a585 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
