# Thrip 脅威アクタープロファイル

- プロファイルID: `actor--thrip`
- 状態: draft
- 更新日時: 2026-09-21T04:35:03Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Thripの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Thrip**
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
| espionage | Actor-specific reporting explicitly describes espionage or intelligence collection. | 高 | `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description; not inferred from country or state sponsorship. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Lotus Blossom | overlaps-with | MITRE ATT&CK 19.2 tracks Lotus Blossom (G0030) and Thrip (G0076) as separate Groups even though Thrip remains an associated name in the Lotus Blossom record; the shared name is therefore an overlap signal, not a safe exact alias. | 高 | `source--mitre-attack-19-2` |

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
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Lotus Blossom, Spring Dragon, Thrip | canonical-name | 高 | China | https://blog.talosintelligence.com/lotus-blossom-espionage-group/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Lotus+Blossom%2C+Spring+Dragon%2C+Thrip&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Thrip | canonical-name | 高 | Unknown | https://www.cfr.org/interactive/cyber-operations/thrip<br>https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets<br>https://attack.mitre.org/groups/G0076/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Lotus Blossom - G0030 | canonical-name | 高 |  | https://attack.mitre.org/groups/G0030<br>https://blog.talosintelligence.com/lotus-blossom-espionage-group/<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
| misp-mitre-enterprise-intrusion-set | Thrip - G0076 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0076<br>https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets |
| misp-mitre-intrusion-set | Lotus Blossom - G0030 | canonical-name | 高 |  | https://attack.mitre.org/groups/G0030<br>https://blog.talosintelligence.com/lotus-blossom-espionage-group/<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
| misp-mitre-intrusion-set | Thrip - G0076 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0076<br>https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Thrip | canonical-name | 高 |  |  |

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
| malware--catchamas | Catchamas | [Catchamas](https://attack.mitre.org/software/S0261) is a Windows Trojan that steals information from compromised systems. (Citation: Symantec Catchamas April 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| countries | 米国 | [Thrip](https://attack.mitre.org/groups/G0076) is an espionage group that has targeted satellite communications, telecoms, and defense contractor companies in the U.S. and Southeast Asia. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | 情報通信 | [Thrip](https://attack.mitre.org/groups/G0076) is an espionage group that has targeted satellite communications, telecoms, and defense contractor companies in the U.S. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | 防衛・軍事 | [Thrip](https://attack.mitre.org/groups/G0076) is an espionage group that has targeted satellite communications, telecoms, and defense contractor companies in the U.S. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Exfiltration | T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | [Thrip](https://attack.mitre.org/groups/G0076) has used WinSCP to exfiltrate data from a targeted organization over FTP.(Citation: Symantec Thrip June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.001 | PowerShell | [Thrip](https://attack.mitre.org/groups/G0076) leveraged PowerShell to run commands to download payloads, traverse the compromised networks, and carry out reconnaissance.(Citation: Symantec Thrip June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1219.002 | Remote Desktop Software | [Thrip](https://attack.mitre.org/groups/G0076) used a cloud-based remote access software called LogMeIn for their attacks.(Citation: Symantec Thrip June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.002 | Tool | [Thrip](https://attack.mitre.org/groups/G0076) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002) and [PsExec](https://attack.mitre.org/software/S0029).(Citation: Symantec Thrip June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--thrip--eb918c7d46e2db59 | thrip |  | 不明 | actor_profile/evidence/thrip.csv | structured-data | TLP:CLEAR | 中 |
| source--thrip--77e521f6d2989620 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--thrip--4a95391670719719 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--thrip--e73612f117feae5e | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--thrip--9afb6e4805b599d4 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--thrip--0f77f3578e8e651c | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--thrip--34f68bfd5684921c | search |  | 不明 | ui/api/v1/search.json | structured-data | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
