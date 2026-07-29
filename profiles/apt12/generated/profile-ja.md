# APT12 脅威アクタープロファイル

- プロファイルID: `actor--apt12`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

APT12の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT12**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BeeBus | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Calc Team | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Crimson Iron | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DNSCalc | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DynCalc | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Group 22 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| IXESHE | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Numbered Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TG-2754 (tentative) | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DynCalc, Crimson Iron, DNSCalc | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 6; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
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
| Adversary | [APT12](https://attack.mitre.org/groups/G0005) is a threat group that has been attributed to China. The group has targeted a variety of victims including but not limited to media outlets, high-tech companies, and multiple governments.(Citation: Meyers Numbered Panda) |
| Capability | Ixeshe, RIPTIDE, Etumbot, Hightide, ThreeByte, Waterspout, Mswab, Gh0st, ShowNews, 3001, HTRAN |
| Infrastructure |  |
| Victim | This threat actor targets organizations in Japan, Taiwan, and elsewhere in East Asiaâ€”including electronics manufacturers and telecommunications companiesâ€”for espionage purposes. |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 12, Numbered Panda | canonical-name | 高 | China | https://www.crowdstrike.com/blog/whois-numbered-panda/<br>https://www.fireeye.com/blog/threat-research/2014/09/darwins-favorite-apt-group-2.html<br>https://en.wikipedia.org/wiki/Numbered_Panda |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Hexagon Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT12 | canonical-name | 高 | CN, China | http://www.crowdstrike.com/blog/whois-numbered-panda/<br>https://www.cfr.org/interactive/cyber-operations/apt-12<br>https://www.fireeye.com/blog/threat-research/2014/09/darwins-favorite-apt-group-2.html |
| misp-microsoft-activity-group | Hexagon Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | APT12 - G0005 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0005<br>http://www.crowdstrike.com/blog/whois-numbered-panda/ |
| misp-mitre-intrusion-set | APT12 - G0005 | mitre-external-id | 高 |  | http://www.crowdstrike.com/blog/whois-numbered-panda/<br>https://attack.mitre.org/groups/G0005<br>https://www.fireeye.com/blog/threat-research/2014/09/darwins-favorite-apt-group-2.html |
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
| malware--ixeshe | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) is a malware family that has been used since at least 2009 against targets in East Asia. (Citation: Moran 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--riptide | RIPTIDE | [RIPTIDE](https://attack.mitre.org/software/S0003) is a proxy-aware backdoor used by [APT12](https://attack.mitre.org/groups/G0005). (Citation: Moran 2014) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--etumbot | Etumbot | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--hightide | Hightide | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--threebyte | ThreeByte | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--waterspout | Waterspout | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--mswab | Mswab | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--gh0st | Gh0st | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--shownews | ShowNews | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--3001 | 3001 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--htran | HTRAN | [HTRAN](https://attack.mitre.org/software/S0040) is a tool that proxies connections through intermediate hops and aids users in disguising their true geographical location. It can be used by adversaries to hide their location when interacting with the victim networks. (Citation: Operation Quantum Entanglement)(Citation: NCSC Joint Report Public Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| countries | Taiwan | Targeting text mentions taiwan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Japan | Targeting text mentions japan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1102.002 | Bidirectional Communication | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1568.003 | DNS Calculation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 25件（`artifacts.csv`）

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
| source--apt12--e281ecf881367ac6 | apt12 |  | 不明 | actor_profile/evidence/apt12.csv | structured-data | TLP:CLEAR | 中 |
| source--apt12--5742cbd0ea82de03 | apt28 |  | 不明 | APT28/history-report-pdf/apt28.pdf | report | TLP:CLEAR | 中 |
| source--apt12--9310c54491c4665c | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--apt12--845b3c79afc4a8e9 | A three beat waltz The ecosystem behind Chinese state sponsored cyber threats |  | 不明 | International Strategic/China/A-three-beat-waltz-The-ecosystem-behind-Chinese-state-sponsored-cyber-threats.pdf | report | TLP:CLEAR | 中 |
| source--apt12--8d790302d3040a5f | Raport analize Teknikat Taktikat Procedurat per sulmuesit Iraniane |  | 不明 | International Strategic/Iran/Raport-analize-Teknikat-Taktikat-Procedurat-per-sulmuesit-Iraniane.pdf | report | TLP:CLEAR | 中 |
| source--apt12--9dc1354aae60c647 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--apt12--51d1ebc43214abda | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--apt12--c46905379dd2d5d3 | Dream Job Campaign |  | 不明 | lazarus/Dream-Job-Campaign.pdf | report | TLP:CLEAR | 中 |
| source--apt12--c9ecab067672af17 | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--apt12--3083edc8610674fb | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
