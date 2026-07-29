# The White Company 脅威アクタープロファイル

- プロファイルID: `actor--white-company`
- 状態: draft
- 更新日時: 2026-07-29T15:36:13Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

The White Companyの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **The White Company**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Bahamut | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 64; mapping requires review. |
| URPAGE | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 64; mapping requires review. |
| EHDEVEL | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 64; mapping requires review. |
| WINDSHIFT | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 64; mapping requires review. |
| offshore APT organization from South Asia | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 64; mapping requires review. |

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
| Adversary | [The White Company](https://attack.mitre.org/groups/G0089) is a likely state-sponsored threat actor with advanced capabilities. From 2017 through 2018, the group led an espionage campaign called Operation Shaheen targeting government and military organizations in Pakistan.(Citation: Cylance Shaheen Nov 2018) |
| Capability | NETWIRE, Revenge RAT |
| Infrastructure |  |
| Victim | Middle Eastern human rights activists |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Bahamut | single-alias-intersection | 中 |  | https://www.bellingcat.com/news/mena/2017/06/12/bahamut-pursuing-cyber-espionage-actor-middle-east/<br>https://www.blackberry.com/us/en/forms/enterprise/bahamut-report<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Bahamut&n=1 |
| etda-threat-group-cards | The White Company | canonical-name | 高 |  | https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=The+White+Company&n=1 |
| etda-threat-group-cards | Urpage | single-alias-intersection | 中 |  | https://blog.trendmicro.com/trendlabs-security-intelligence/the-urpage-connection-to-bahamut-confucius-and-patchwork/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Urpage&n=1 |
| etda-threat-group-cards | WindShift | single-alias-intersection | 中 |  | https://unit42.paloaltonetworks.com/shifting-in-the-wind-windshift-attacks-target-middle-eastern-governments/<br>https://gsec.hitb.org/materials/sg2018/D1%20COMMSEC%20-%20In%20the%20Trails%20of%20WINDSHIFT%20APT%20-%20Taha%20Karim.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=WindShift&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Bahamut | single-alias-intersection | 中 |  | https://www.bellingcat.com/news/mena/2017/06/12/bahamut-pursuing-cyber-espionage-actor-middle-east/<br>https://www.bellingcat.com/resources/case-studies/2017/10/27/bahamut-revisited-cyber-espionage-middle-east-south-asia/ |
| misp-threat-actor | WindShift | single-alias-intersection | 中 |  | https://unit42.paloaltonetworks.com/shifting-in-the-wind-windshift-attacks-target-middle-eastern-governments/<br>https://gsec.hitb.org/materials/sg2018/D1%20COMMSEC%20-%20In%20the%20Trails%20of%20WINDSHIFT%20APT%20-%20Taha%20Karim.pdf<br>https://unit42.paloaltonetworks.com/atoms/windyphoenix/ |
| misp-threat-actor | Urpage | single-alias-intersection | 中 |  | https://www.trendmicro.com/en_us/research/18/h/the-urpage-connection-to-bahamut-confucius-and-patchwork.html |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | The White Company - G0089 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0089<br>https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517 |
| misp-mitre-intrusion-set | Windshift - G0112 | multiple-name-intersection | 高 |  | https://attack.mitre.org/groups/G0112<br>https://objective-see.com/blog/blog_0x3B.html<br>https://objective-see.com/blog/blog_0x3D.html |
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
| malware--netwire | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) is a publicly available, multiplatform remote administration tool (RAT) that has been used by criminal and APT groups since at least 2012.(Citation: FireEye APT33 Sept 2017)(Citation: McAfee Netwire Mar 2015)(Citation: FireEye APT33 Webinar Sept 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--revenge-rat | Revenge RAT | [Revenge RAT](https://attack.mitre.org/software/S0379) is a freely available remote access tool written in .NET (C#).(Citation: Cylance Shaheen Nov 2018)(Citation: Cofense RevengeRAT Feb 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| InPage zero-day | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Malicious MDM | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

InPage zero-day; Malicious MDM

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | パキスタン | From 2017 through 2018, the group led an espionage campaign called Operation Shaheen targeting government and military organizations in Pakistan.(Citation: Cylance Shaheen Nov 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 防衛・軍事 | From 2017 through 2018, the group led an espionage campaign called Operation Shaheen targeting government and military organizations in Pakistan.(Citation: Cylance Shaheen Nov 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | From 2017 through 2018, the group led an espionage campaign called Operation Shaheen targeting government and military organizations in Pakistan.(Citation: Cylance Shaheen Nov 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Nonprofit and Civil Society | Targeting text indicates the Nonprofit and Civil Society sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.002 | Software Packing | [The White Company](https://attack.mitre.org/groups/G0089) has obfuscated their payloads through packing.(Citation: Cylance Shaheen Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [The White Company](https://attack.mitre.org/groups/G0089) has the ability to delete its malware entirely from the target system.(Citation: Cylance Shaheen Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | [The White Company](https://attack.mitre.org/groups/G0089) has checked the current date on the victim system.(Citation: Cylance Shaheen Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution |  [The White Company](https://attack.mitre.org/groups/G0089) has taken advantage of a known vulnerability in Microsoft Word (CVE 2012-0158) to execute code.(Citation: Cylance Shaheen Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [The White Company](https://attack.mitre.org/groups/G0089) has used phishing lure documents that trick users into opening them and infecting their computers.(Citation: Cylance Shaheen Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [The White Company](https://attack.mitre.org/groups/G0089) has checked for specific antivirus products on the target’s computer, including Kaspersky, Quick Heal, AVG, BitDefender, Avira, Sophos, Avast!, and ESET.(Citation: Cylance Shaheen Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [The White Company](https://attack.mitre.org/groups/G0089) has sent phishing emails with malicious Microsoft Word attachments to victims.(Citation: Cylance Shaheen Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 38件
- IOC観測: 47件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 179件（`artifacts.csv`）

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
| source--white-company--6f73b0791a1ce588 | README |  | 不明 | WhiteCompany/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--white-company--9a5333b9a4ad40b4 | WhiteCompanyOperationShaheenReport |  | 不明 | WhiteCompany/WhiteCompanyOperationShaheenReport.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
