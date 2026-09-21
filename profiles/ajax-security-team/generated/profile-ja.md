# Ajax Security Team 脅威アクタープロファイル

- プロファイルID: `actor--ajax-security-team`
- 状態: draft
- 更新日時: 2026-09-21T04:18:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Ajax Security Teamの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Ajax Security Team**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| AjaxTM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Flying Kitten | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Operation Saffron Rose | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Operation Woolen-Goldfish | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Rocket Kitten | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |

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
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Flying Kitten, Ajax Security Team | canonical-name | 高 | Iran | https://www.crowdstrike.com/blog/cat-scratch-fever-crowdstrike-tracks-newly-reported-iranian-actor-flying-kitten/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Flying+Kitten%2C+Ajax+Security+Team&n=1 |
| etda-threat-group-cards | Rocket Kitten, Newscaster, NewsBeef | single-alias-intersection | 中 | Iran | https://securelist.com/freezer-paper-around-free-meat/74503/<br>https://blog.checkpoint.com/wp-content/uploads/2015/11/rocket-kitten-report.pdf<br>https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp-the-spy-kittens-are-back.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Flying Kitten | canonical-name | 高 | IR, Iran (Islamic Republic of) | https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-operation-saffron-rose.pdf<br>https://www.crowdstrike.com/blog/cat-scratch-fever-crowdstrike-tracks-newly-reported-iranian-actor-flying-kitten/<br>https://www.cfr.org/interactive/cyber-operations/saffron-rose |
| misp-threat-actor | Rocket Kitten | multiple-name-intersection | 高 | IR, Iran (Islamic Republic of) | https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/operation-woolen-goldfish-when-kittens-go-phishing<br>https://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp-the-spy-kittens-are-back.pdf<br>http://www.clearskysec.com/thamar-reservoir/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Ajax Security Team - G0130 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0130<br>https://blog.checkpoint.com/wp-content/uploads/2015/11/rocket-kitten-report.pdf<br>https://documents.trendmicro.com/assets/wp/wp-operation-woolen-goldfish.pdf |
| misp-mitre-intrusion-set | Ajax Security Team - G0130 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0130<br>https://blog.checkpoint.com/wp-content/uploads/2015/11/rocket-kitten-report.pdf<br>https://documents.trendmicro.com/assets/wp/wp-operation-woolen-goldfish.pdf |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Ajax Security Team | canonical-name | 高 |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| CHRYSENE | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Charming Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Cleaver | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Clever Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Flying Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| OilRig | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Rocket Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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
| tool--havij | Havij | [Havij](https://attack.mitre.org/software/S0224) is an automatic SQL Injection tool distributed by the Iranian ITSecTeam security company. Havij has been used by penetration testers and adversaries. (Citation: Check Point Havij Analysis) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--sqlmap | sqlmap | [sqlmap](https://attack.mitre.org/software/S0225) is an open source penetration testing tool that can be used to automate the process of detecting and exploiting SQL injection flaws. (Citation: sqlmap Introduction) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

Woolen Goldfish; Thamar Reservoir

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イラン | Targeting text mentions iran. | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--mitre-attack-19-2` |
| countries | 米国 | By 2014 [Ajax Security Team](https://attack.mitre.org/groups/G0130) transitioned from website defacement operations to malware-based cyber espionage campaigns targeting the US defense industrial base and Iranian users of anti-censorship technologies.(Citation: FireEye Operation Saffron Rose 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | 製造・産業 | By 2014 [Ajax Security Team](https://attack.mitre.org/groups/G0130) transitioned from website defacement operations to malware-based cyber espionage campaigns targeting the US defense industrial base and Iranian users of anti-censorship technologies.(Citation: FireEye Operation Saffron Rose 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--mitre-attack-19-1`, `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection, Credential Access | T1056.001 | Keylogging | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used CWoolger and MPK, custom-developed malware, which recorded all keystrokes on an infected system.(Citation: Check Point Rocket Kitten) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used Wrapper/Gholee, custom-developed malware, which downloaded additional malware to the infected system.(Citation: Check Point Rocket Kitten) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has lured victims into executing malicious files.(Citation: FireEye Operation Saffron Rose 2013) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used FireMalv custom-developed malware, which collected passwords from the Firefox browser storage.(Citation: Check Point Rocket Kitten) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used personalized spearphishing attachments.(Citation: Check Point Rocket Kitten) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.003 | Spearphishing via Service | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used various social media channels to spearphish victims.(Citation: FireEye Operation Saffron Rose 2013) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 6件
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
| source--ajax-security-team--ce2a919899d79edc | ajax security team |  | 不明 | actor_profile/evidence/ajax-security-team.csv | structured-data | TLP:CLEAR | 中 |
| source--ajax-security-team--7cd053af6e0fe5c6 | apt28 |  | 不明 | APT28/history-report-pdf/apt28.pdf | report | TLP:CLEAR | 中 |
| source--ajax-security-team--4c67387bc1a9ece8 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--ajax-security-team--927fe369a8a6c1bb | README |  | 不明 | International Strategic/Iran/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--ajax-security-team--d9cd1a07693b461f | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--ajax-security-team--60ec2656ce2a9c7e | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--ajax-security-team--4dd0c4f8ab744483 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--ajax-security-team--2efbf4f5c0fea832 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
