# Ajax Security Team 脅威アクタープロファイル

- プロファイルID: `actor--ajax-security-team`
- 状態: draft
- 更新日時: 2026-07-29T23:13:53Z
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
| AjaxTM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Flying Kitten | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Operation Saffron Rose | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Operation Woolen-Goldfish | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Rocket Kitten | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TEMP.Beanie | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 16; mapping requires review. |
| Saffron Rose | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 16; mapping requires review. |
| Group 26 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 16; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

未評価

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Ajax Security Team](https://attack.mitre.org/groups/G0130) is a group that has been active since at least 2010 and believed to be operating out of Iran. By 2014 [Ajax Security Team](https://attack.mitre.org/groups/G0130) transitioned from website defacement operations to malware-based cyber espionage campaigns targeting the US defense industrial base and Iranian users of anti-censorship technologies.(Citation: FireEye Operation Saffron Rose 2013) |
| Capability | GHOLE / Core Impact, CWoolger, FireMalv, .NETWoolger, MPK, Open source tools, Puppy RAT, MagicHound.Leash (IRC Bot), PowGoop (Downloader.Covic), sqlmap, Havij |
| Infrastructure |  |
| Victim | Saudi Arabia, Israel, US, Iran, high ranking defense officials, embassies of various target countries, notable Iran researchers, human rights activists, media and journalists, academic institutions and various scholars, including scientists in the fields of physics and nuclear sciences. It seeks out material related to diplomacy, defense, security, journalism, and human rights for espionage purposes. |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Flying Kitten, Ajax Security Team | canonical-name | 高 | Iran | https://www.crowdstrike.com/blog/cat-scratch-fever-crowdstrike-tracks-newly-reported-iranian-actor-flying-kitten/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Flying+Kitten%2C+Ajax+Security+Team&n=1 |
| etda-threat-group-cards | Magic Hound, APT 35, Cobalt Illusion, Charming Kitten | single-alias-intersection | 中 | Iran | https://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf<br>https://en.wikipedia.org/wiki/Charming_Kitten<br>https://vblocalhost.com/uploads/VB2021-Haeghebaert.pdf |
| etda-threat-group-cards | Rocket Kitten, Newscaster, NewsBeef | single-alias-intersection | 中 | Iran | https://securelist.com/freezer-paper-around-free-meat/74503/<br>https://blog.checkpoint.com/wp-content/uploads/2015/11/rocket-kitten-report.pdf<br>https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp-the-spy-kittens-are-back.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Flying Kitten | canonical-name | 高 | IR, Iran (Islamic Republic of) | https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-operation-saffron-rose.pdf<br>https://www.crowdstrike.com/blog/cat-scratch-fever-crowdstrike-tracks-newly-reported-iranian-actor-flying-kitten/<br>https://www.cfr.org/interactive/cyber-operations/saffron-rose |
| misp-threat-actor | Rocket Kitten | multiple-name-intersection | 高 | IR, Iran (Islamic Republic of) | https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/operation-woolen-goldfish-when-kittens-go-phishing<br>https://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp-the-spy-kittens-are-back.pdf<br>http://www.clearskysec.com/thamar-reservoir/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Magic Hound - G0059 | canonical-name | 高 |  | https://attack.mitre.org/wiki/Group/G0059<br>https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/ |
| misp-mitre-intrusion-set | Ajax Security Team - G0130 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0130<br>https://blog.checkpoint.com/wp-content/uploads/2015/11/rocket-kitten-report.pdf<br>https://documents.trendmicro.com/assets/wp/wp-operation-woolen-goldfish.pdf |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Cleaver | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--ghole-core-impact | GHOLE / Core Impact | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cwoolger | CWoolger | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--firemalv | FireMalv | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--netwoolger | .NETWoolger | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--mpk | MPK | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--open-source-tools | Open source tools | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--puppy-rat | Puppy RAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--magichound-leash-irc-bot | MagicHound.Leash (IRC Bot) | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--powgoop-downloader-covic | PowGoop (Downloader.Covic) | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--sqlmap | sqlmap | [sqlmap](https://attack.mitre.org/software/S0225) is an open source penetration testing tool that can be used to automate the process of detecting and exploiting SQL injection flaws. (Citation: sqlmap Introduction) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--havij | Havij | [Havij](https://attack.mitre.org/software/S0224) is an automatic SQL Injection tool distributed by the Iranian ITSecTeam security company. Havij has been used by penetration testers and adversaries. (Citation: Check Point Havij Analysis) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thamar Reservoir | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Woolen Goldfish | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Thamar Reservoir | Ajax Security Team | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Woolen Goldfish | Ajax Security Team | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

Woolen Goldfish; Thamar Reservoir

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | イエメン | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてイエメンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | イスラエル | Targeting text mentions israel. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-misp-threat-actor` |
| countries | イラク | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてイラクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | イラン | Targeting text mentions iran. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-misp-threat-actor` |
| countries | エジプト | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてエジプトが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | カナダ | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | クウェート | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてクウェートが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | サウジアラビア | Targeting text mentions saudi arabia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-misp-threat-actor` |
| countries | シリア | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてシリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | トルコ | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ベネズエラ | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてベネズエラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ヨルダン | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国としてヨルダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 米国 | By 2014 [Ajax Security Team](https://attack.mitre.org/groups/G0130) transitioned from website defacement operations to malware-based cyber espionage campaigns targeting the US defense industrial base and Iranian users of anti-censorship technologies.(Citation: FireEye Operation Saffron Rose 2013) | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでAjax Security Teamの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 中東 | アラブ首長国連邦、イエメン、イスラエル、イラク、イラン、クウェート、サウジアラビア、シリア、トルコ、ヨルダンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-misp-threat-actor` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | トルコ、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| sectors | 製造・産業 | By 2014 [Ajax Security Team](https://attack.mitre.org/groups/G0130) transitioned from website defacement operations to malware-based cyber espionage campaigns targeting the US defense industrial base and Iranian users of anti-censorship technologies.(Citation: FireEye Operation Saffron Rose 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Education and Research | Targeting text indicates the Education and Research sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Media | Targeting text indicates the Media sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Nonprofit and Civil Society | Targeting text indicates the Nonprofit and Civil Society sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection, Credential Access | T1056.001 | Keylogging | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used CWoolger and MPK, custom-developed malware, which recorded all keystrokes on an infected system.(Citation: Check Point Rocket Kitten) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used Wrapper/Gholee, custom-developed malware, which downloaded additional malware to the infected system.(Citation: Check Point Rocket Kitten) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has lured victims into executing malicious files.(Citation: FireEye Operation Saffron Rose 2013) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used FireMalv custom-developed malware, which collected passwords from the Firefox browser storage.(Citation: Check Point Rocket Kitten) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used personalized spearphishing attachments.(Citation: Check Point Rocket Kitten) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.003 | Spearphishing via Service | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used various social media channels to spearphish victims.(Citation: FireEye Operation Saffron Rose 2013) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 26件（`artifacts.csv`）

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
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
