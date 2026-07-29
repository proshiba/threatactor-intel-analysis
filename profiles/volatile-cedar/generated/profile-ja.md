# Volatile Cedar 脅威アクタープロファイル

- プロファイルID: `actor--volatile-cedar`
- 状態: draft
- 更新日時: 2026-07-29T23:13:55Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Volatile Cedarの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Volatile Cedar**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Lebanese Cedar | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Lebanon | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Middle East row 5; mapping requires review. |

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
| Adversary | [Volatile Cedar](https://attack.mitre.org/groups/G0123) is a Lebanese threat group that has targeted individuals, companies, and institutions worldwide. [Volatile Cedar](https://attack.mitre.org/groups/G0123) has been operating since 2012 and is motivated by political and ideological interests.(Citation: CheckPoint Volatile Cedar March 2015)(Citation: ClearSky Lebanese Cedar Jan 2021) |
| Capability | Explosive, Caterpillar WebShell, Caterpillar 2 |
| Infrastructure |  |
| Victim | USA, Canada, UK, Turkey, Lebanon and Israel. Nation-state/political-group interests |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Volatile Cedar | canonical-name | 高 | Lebanon | https://www.checkpoint.com/downloads/volatile-cedar-technical-report.pdf<br>https://securelist.com/sinkholing-volatile-cedar-dga-infrastructure/69421/<br>https://securelist.com/defttorero-tactics-techniques-and-procedures/107610/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Amethyst Rain | canonical-name | 高 | Lebanon | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Volatile Cedar | canonical-name | 高 | LB | https://blog.checkpoint.com/2015/03/31/volatilecedar/<br>https://blog.checkpoint.com/2015/06/09/new-data-volatile-cedar/<br>https://securelist.com/sinkholing-volatile-cedar-dga-infrastructure/69421/ |
| misp-threat-actor | Amethyst Rain | canonical-name | 高 | LB, Lebanon | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Amethyst Rain | canonical-name | 高 | LB, Lebanon | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Volatile Cedar - G0123 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0123<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf<br>https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf |
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
| malware--explosive | Explosive | [Explosive](https://attack.mitre.org/software/S0569) is a custom-made remote access tool used by the group [Volatile Cedar](https://attack.mitre.org/groups/G0123). It was first identified in the wild in 2015.(Citation: CheckPoint Volatile Cedar March 2015)(Citation: ClearSky Lebanese Cedar Jan 2021)   | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--caterpillar-webshell | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) is a self-developed Web Shell tool created by the group [Volatile Cedar](https://attack.mitre.org/groups/G0123).(Citation: ClearSky Lebanese Cedar Jan 2021)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--caterpillar-2 | Caterpillar 2 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでVolatile Cedarの標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | Targeting text mentions israel. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | エジプト | 構造化OSINTの被害国フィールドでVolatile Cedarの標的・被害国としてエジプトが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | Targeting text mentions canada. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | サウジアラビア | 構造化OSINTの被害国フィールドでVolatile Cedarの標的・被害国としてサウジアラビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | Targeting text mentions turkey. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | パレスチナ | 構造化OSINTの被害国フィールドでVolatile Cedarの標的・被害国としてパレスチナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ヨルダン | 構造化OSINTの被害国フィールドでVolatile Cedarの標的・被害国としてヨルダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | レバノン | Targeting text mentions lebanon. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでVolatile Cedarの標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | レビュー済みアクターマッピングの標的欄に記録された米国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | レビュー済みアクターマッピングの標的欄に記録された英国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | アラブ首長国連邦、イスラエル、サウジアラビア、トルコ、パレスチナ、ヨルダン、レバノンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | トルコ、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1105 | Ingress Tool Transfer | [Volatile Cedar](https://attack.mitre.org/groups/G0123) can deploy additional tools.(Citation: ClearSky Lebanese Cedar Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Volatile Cedar](https://attack.mitre.org/groups/G0123) has targeted publicly facing web servers, with both automatic and manual vulnerability discovery.(Citation: CheckPoint Volatile Cedar March 2015) (Citation: ClearSky Lebanese Cedar Jan 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [Volatile Cedar](https://attack.mitre.org/groups/G0123) can inject web shell code into a server.(Citation: CheckPoint Volatile Cedar March 2015)(Citation: ClearSky Lebanese Cedar Jan 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | [Volatile Cedar](https://attack.mitre.org/groups/G0123) has performed vulnerability scans of the target server.(Citation: CheckPoint Volatile Cedar March 2015)(Citation: ClearSky Lebanese Cedar Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.003 | Wordlist Scanning | [Volatile Cedar](https://attack.mitre.org/groups/G0123) has used DirBuster and GoBuster to brute force web directories and DNS subdomains.(Citation: ClearSky Lebanese Cedar Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 23件（`artifacts.csv`）

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
| source--volatile-cedar--3b09a0cf8ef081a3 | volatile cedar |  | 不明 | actor_profile/evidence/volatile-cedar.csv | structured-data | TLP:CLEAR | 中 |
| source--volatile-cedar--829a9b4c6f2cbdac | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--volatile-cedar--6f860d0b3debed90 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--volatile-cedar--ef2cf53946d56f29 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--volatile-cedar--d0e85490860680e5 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--volatile-cedar--0320924db76c2201 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
