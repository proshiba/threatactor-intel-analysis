# Group5 脅威アクタープロファイル

- プロファイルID: `actor--group5`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Group5の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Group5**
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
| Adversary | [Group5](https://attack.mitre.org/groups/G0043) is a threat group with a suspected Iranian nexus, though this attribution is not definite. The group has targeted individuals connected to the Syrian opposition via spearphishing and watering holes, normally using Syrian and Iranian themes. [Group5](https://attack.mitre.org/groups/G0043) has used two commonly available remote access tools (RATs), [njRAT](https://attack.mitre.org/software/S0385) and [NanoCore](https://attack.mitre.org/software/S0336), as well as an Android RAT, DroidJack. (Citation: Citizen Lab Group5) |
| Capability | NanoCore, njRAT |
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
| etda-threat-group-cards | Group5 | canonical-name | 高 | Iran | https://www.securityweek.com/iranian-actor-group5-targeting-syrian-opposition<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Group5&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Group5 | canonical-name | 高 |  | https://www.securityweek.com/iranian-actor-group5-targeting-syrian-opposition<br>https://attack.mitre.org/groups/G0043/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Group5 - G0043 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0043<br>https://citizenlab.org/2016/08/group5-syria/ |
| misp-mitre-intrusion-set | Group5 - G0043 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0043<br>https://citizenlab.ca/2016/08/group5-syria/ |
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
| malware--nanocore | NanoCore | [NanoCore](https://attack.mitre.org/software/S0336) is a modular remote access tool developed in .NET that can be used to spy on victims and steal information. It has been used by threat actors since 2013.(Citation: DigiTrust NanoCore Jan 2017)(Citation: Cofense NanoCore Mar 2018)(Citation: PaloAlto NanoCore Feb 2016)(Citation: Unit 42 Gorgon Group Aug 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--njrat | njRAT | [njRAT](https://attack.mitre.org/software/S0385) is a remote access tool (RAT) that was first observed in 2012. It has been used by threat actors in the Middle East.(Citation: Fidelis njRAT June 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | シリア | MITRE ATT&CKのGroup概要でGroup5の標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.013 | Encrypted/Encoded File | [Group5](https://attack.mitre.org/groups/G0043) disguised its malicious binaries with several layers of obfuscation, including encrypting the files.(Citation: Citizen Lab Group5) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | Malware used by [Group5](https://attack.mitre.org/groups/G0043) is capable of capturing keystrokes.(Citation: Citizen Lab Group5) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | Malware used by [Group5](https://attack.mitre.org/groups/G0043) is capable of remotely deleting files from victims.(Citation: Citizen Lab Group5) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | Malware used by [Group5](https://attack.mitre.org/groups/G0043) is capable of watching the victim's screen.(Citation: Citizen Lab Group5) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 22件（`artifacts.csv`）

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
| source--group5--2a48266b283f8080 | group5 |  | 不明 | actor_profile/evidence/group5.csv | structured-data | TLP:CLEAR | 中 |
| source--group5--776078701fb82c78 | BlueDelta Exploits Ukrainian Government Roundcube Mail Servers to Support Espionage Activities |  | 不明 | APT28/BlueDelta Exploits Ukrainian Government Roundcube Mail Servers to Support Espionage Activities.pdf | report | TLP:CLEAR | 中 |
| source--group5--0a12d3ae7edc4037 | APT29 Adapts to Target Diplomatic Entities with GraphicalProton Malware |  | 不明 | APT29/APT29 Adapts to Target Diplomatic Entities with GraphicalProton Malware.pdf | report | TLP:CLEAR | 中 |
| source--group5--c333719dfebaee7c | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--group5--8493c4973e593553 | BlueCharlie Continues to Deploy New Infrastructure in 2023 |  | 2023 | Calisto/BlueCharlie_Continues_to_Deploy_New_Infrastructure_in_2023.pdf | report | TLP:CLEAR | 中 |
| source--group5--c7ff7eab12365b35 | The Kittens Are Back in Town Charming Kitten 2019 |  | 2019 | Charming Kitten/The-Kittens-Are-Back-in-Town-Charming-Kitten-2019.pdf | report | TLP:CLEAR | 中 |
| source--group5--52409d2d73d51c01 | TAG 74 |  | 不明 | International Strategic/China/TAG-74.pdf | report | TLP:CLEAR | 中 |
| source--group5--6e4e5b4915ed0fc3 | chinese darkweb analysis |  | 不明 | International Strategic/China/chinese_darkweb_analysis.pdf | report | TLP:CLEAR | 中 |
| source--group5--b611edc3dec22676 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--group5--df4fa953351f53ed | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--group5--c4b364f02e6886f5 | Empire Dragon |  | 不明 | information_operations/Empire_Dragon/Empire Dragon.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
