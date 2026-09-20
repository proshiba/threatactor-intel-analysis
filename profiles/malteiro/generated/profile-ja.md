# Malteiro 脅威アクタープロファイル

- プロファイルID: `actor--malteiro`
- 状態: draft
- 更新日時: 2026-09-20T13:48:12Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Malteiroの標準化プロファイル。リポジトリ内の専用資料0件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Malteiro**
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
| financial-gain | Financially motivated intrusion or fraud. | 高 | `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Malteiro](https://attack.mitre.org/groups/G1026) is a financially motivated criminal group that is likely based in Brazil and has been active since at least November 2019. The group operates and distributes the [Mispadu](https://attack.mitre.org/software/S1122)  banking trojan via a Malware-as-a-Service (MaaS) business model. [Malteiro](https://attack.mitre.org/groups/G1026) mainly targets victims throughout Latin America (particularly Mexico) and Europe (particularly Spain and Portugal).(Citation: SCILabs Malteiro 2021) |
| Capability | Mispadu |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-09-20T13:47:46Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Malteiro | canonical-name | 高 |  | https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/<br>https://blog.scilabs.mx/cyber-threat-profile-malteiro/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Malteiro - G1026 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1026<br>https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/ |
| misp-mitre-intrusion-set | Malteiro - G1026 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1026<br>https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/ |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Malteiro | canonical-name | 高 | BR |  |

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
| malware--mispadu | Mispadu | [Mispadu](https://attack.mitre.org/software/S1122) is a banking trojan written in Delphi that was first observed in 2019 and uses a Malware-as-a-Service (MaaS) business model.(Citation: ESET Security Mispadu Facebook Ads 2019)(Citation: SCILabs Malteiro 2021) This malware is operated, managed, and sold by the [Malteiro](https://attack.mitre.org/groups/G1026) cybercriminal group.(Citation: SCILabs Malteiro 2021) [Mispadu](https://attack.mitre.org/software/S1122) has mainly been used to target victims in Brazil and Mexico, and has also had confirmed operations throughout Latin America and Europe.(Citation: SCILabs Malteiro 2021)(Citation: SCILabs URSA/Mispadu Evolution 2023)(Citation: Segurança Informática URSA Sophisticated Loader 2020)  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| countries | メキシコ | MITRE ATT&CKのGroup概要でMalteiroの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| regions | 中南米 | MITRE ATT&CKのGroup概要でMalteiroの標的範囲として中南米が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| regions | 欧州 | MITRE ATT&CKのGroup概要でMalteiroの標的範囲として欧州が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.013 | Encrypted/Encoded File | [Malteiro](https://attack.mitre.org/groups/G1026) has used scripts encoded in Base64 certificates to distribute malware to victims.(Citation: SCILabs Malteiro Threat Overlap 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | [Malteiro](https://attack.mitre.org/groups/G1026) has injected [Mispadu](https://attack.mitre.org/software/S1122)’s DLL into a process.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.005 | Visual Basic | [Malteiro](https://attack.mitre.org/groups/G1026) has utilized a dropper containing malicious VBS scripts.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1082 | System Information Discovery | [Malteiro](https://attack.mitre.org/groups/G1026) collects the machine information, system architecture, the OS version, computer name, and Windows product name.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Malteiro](https://attack.mitre.org/groups/G1026) has the ability to deobfuscate downloaded files prior to execution.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [Malteiro](https://attack.mitre.org/groups/G1026) has relied on users to execute .zip file attachments containing malicious URLs.(Citation: SCILabs Malteiro 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1518.001 | Security Software Discovery | [Malteiro](https://attack.mitre.org/groups/G1026) collects the installed antivirus on the victim machine.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1555 | Credentials from Password Stores | [Malteiro](https://attack.mitre.org/groups/G1026) has obtained credentials from mail clients via NirSoft MailPassView.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [Malteiro](https://attack.mitre.org/groups/G1026) has stolen credentials stored in the victim’s browsers via software tool NirSoft WebBrowserPassView.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Malteiro](https://attack.mitre.org/groups/G1026) has sent spearphishing emails containing malicious .zip files.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1614.001 | System Language Discovery | [Malteiro](https://attack.mitre.org/groups/G1026) will terminate [Mispadu](https://attack.mitre.org/software/S1122)'s infection process if the language of the victim machine is not Spanish or Portuguese.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1657 | Financial Theft | [Malteiro](https://attack.mitre.org/groups/G1026) targets organizations in a wide variety of sectors via the use of [Mispadu](https://attack.mitre.org/software/S1122) banking trojan with the goal of financial theft.(Citation: SCILabs Malteiro 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
