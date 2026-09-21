# Whitefly 脅威アクタープロファイル

- プロファイルID: `actor--whitefly`
- 状態: draft
- 更新日時: 2026-09-21T04:18:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Whiteflyの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Whitefly**
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
| espionage | Actor-specific reporting explicitly describes espionage or intelligence collection. | 高 | `source--mitre-attack-19-1`, `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description; not inferred from country or state sponsorship. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Mofang | overlaps-with | 共有alias: Whitefly | 低 | `source--mitre-attack-19-2` |

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
| etda-threat-group-cards | Whitefly, Mofang | canonical-name | 高 |  | https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf<br>https://www.symantec.com/blogs/threat-intelligence/whitefly-espionage-singapore<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Whitefly%2C+Mofang&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Whitefly | canonical-name | 高 |  | https://www.symantec.com/blogs/threat-intelligence/whitefly-espionage-singapore<br>https://www.reuters.com/article/us-singapore-cyberattack/cyberattack-on-singapore-health-database-steals-details-of-1-5-million-including-pm-idUSKBN1KA14J |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Whitefly - G0107 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0107<br>https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore |
| misp-mitre-intrusion-set | Whitefly - G0107 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0107<br>https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Whitefly | canonical-name | 高 |  |  |

### 関係性候補（未統合）

候補なし

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

未確認

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

SingHealth

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | シンガポール | Targeting text mentions singapore. | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [Whitefly](https://attack.mitre.org/groups/G0107) has used [Mimikatz](https://attack.mitre.org/software/S0002) to obtain credentials.(Citation: Symantec Whitefly March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Whitefly](https://attack.mitre.org/groups/G0107) has encrypted the payload used for C2.(Citation: Symantec Whitefly March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Whitefly](https://attack.mitre.org/groups/G0107) has named the malicious DLL the same name as DLLs belonging to legitimate software from various security vendors.(Citation: Symantec Whitefly March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059 | Command and Scripting Interpreter | [Whitefly](https://attack.mitre.org/groups/G0107) has used a simple remote shell tool that will call back to the C2 server and wait for commands.(Citation: Symantec Whitefly March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [Whitefly](https://attack.mitre.org/groups/G0107) has used an open-source tool to exploit a known Windows privilege escalation vulnerability (CVE-2016-0051) on unpatched computers.(Citation: Symantec Whitefly March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [Whitefly](https://attack.mitre.org/groups/G0107) has the ability to download additional tools from the C2.(Citation: Symantec Whitefly March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [Whitefly](https://attack.mitre.org/groups/G0107) has used malicious .exe or .dll files disguised as documents or images.(Citation: Symantec Whitefly March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Stealth | T1574.001 | DLL | [Whitefly](https://attack.mitre.org/groups/G0107) has used search order hijacking to run the loader Vcrodat.(Citation: Symantec Whitefly March 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.002 | Tool | [Whitefly](https://attack.mitre.org/groups/G0107) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: Symantec Whitefly March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 3件（`artifacts.csv`）

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
| source--whitefly--18aa0cd4abbfb468 | whitefly |  | 不明 | actor_profile/evidence/whitefly.csv | structured-data | TLP:CLEAR | 中 |
| source--whitefly--28de080ba4078d78 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--whitefly--ab6826319de88654 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--whitefly--5e5ded2403418389 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
