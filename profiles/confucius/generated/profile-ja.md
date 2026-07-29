# Confucius 脅威アクタープロファイル

- プロファイルID: `actor--confucius`
- 状態: draft
- 更新日時: 2026-07-29T15:36:10Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Confuciusの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Confucius**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Confucius APT | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Patchwork | related-to | Security researchers have noted similarities between [Confucius](https://attack.mitre.org/groups/G0142) and [Patchwork](https://attack.mitre.org/groups/G0040), particularly in their respective custom malware code and targets.(Citation: TrendMicro Confucius APT Feb 2018)(Citation: TrendMicro Confucius APT Aug 2021)(Citation: Uptycs Confucius APT Jan 2021) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Confucius](https://attack.mitre.org/groups/G0142) is a cyber espionage group that has primarily targeted military personnel, high-profile personalities, business persons, and government organizations in South Asia since at least 2013. Security researchers have noted similarities between [Confucius](https://attack.mitre.org/groups/G0142) and [Patchwork](https://attack.mitre.org/groups/G0040), particularly in their respective custom malware code and targets.(Citation: TrendMicro Confucius APT Feb 2018)(Citation: TrendMicro Confucius APT Aug 2021)(Citation: Uptycs Confucius APT Jan 2021) |
| Capability | WarzoneRAT |
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
| etda-threat-group-cards | Confucius | canonical-name | 高 | India | https://unit42.paloaltonetworks.com/unit42-confucius-says-malware-families-get-further-by-abusing-legitimate-websites/<br>https://documents.trendmicro.com/assets/research-deciphering-confucius-cyberespionage-operations.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Confucius&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Confucius - G0142 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0142<br>https://www.trendmicro.com/en_us/research/18/b/deciphering-confucius-cyberespionage-operations.html<br>https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html |
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
| malware--warzonerat | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) is a malware-as-a-service remote access tool (RAT) written in C++ that has been publicly available for purchase since at least late 2018.(Citation: Check Point Warzone Feb 2020)(Citation: Uptycs Warzone UAC Bypass November 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Confuciusハッカーが新たなWooperStealerとAnondoorマルウェアでパキスタンを攻撃 | phishing-campaign | 2025-07 | 2025-07 | 2025-10-03 | target--activity-rule--country--67ce22b843f136bff928 |  | ttp--activity-rule--5b28d97244888a45be87, ttp--activity-rule--d73305668f0a6f75ed97 | victim--activity-rule--a4fdf571878c0d84fab9 | スパイ集団Confuciusがフィッシングでパキスタンを標的化し、WooperStealerとAnondoorを投入。2013年以降活動。 2024年12月は.PPSXを開かせDLLサイドロードでWooperStealerを実行、感染を広げたとFortinetが報告。 2025年3月以降は.LNKを用いて悪性DLLを起動し情報窃取、8月の.LNKではAnondoor展開に切り替え。 Anondoorは外部C2へ端末情報を送信し、コマンド実行や画面取得、Chromeパスワード窃取などを実施。 KnownSecが2025年7月にAnondoor使用を観測。難読化とDLLサイドロードで検知回避する適応力が指摘。 | 高 | `source--daily-1020ead2bd9b87a29746` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | パキスタン | 活動「Confuciusハッカーが新たなWooperStealerとAnondoorマルウェアでパキスタンを攻撃」の記述で標的として明示された国・地域。 | 2025-07 | 2025-07 | 中 | `source--daily-1020ead2bd9b87a29746` |
| sectors | 防衛・軍事 | [Confucius](https://attack.mitre.org/groups/G0142) is a cyber espionage group that has primarily targeted military personnel, high-profile personalities, business persons, and government organizations in South Asia since at least 2013. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | [Confucius](https://attack.mitre.org/groups/G0142) is a cyber espionage group that has primarily targeted military personnel, high-profile personalities, business persons, and government organizations in South Asia since at least 2013. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Confuciusハッカーが新たなWooperStealerとAnondoorマルウェアでパキスタンを攻撃 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--67ce22b843f136bff928 |  | ttp--activity-rule--5b28d97244888a45be87, ttp--activity-rule--d73305668f0a6f75ed97 | エンドポイント | credential-theft: Anondoorは外部C2へ端末情報を送信し、コマンド実行や画面取得、Chromeパスワード窃取などを実施。 | 2025-07 | 2025-07 | 2025-10-03 | 高 | `source--daily-1020ead2bd9b87a29746` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1555.003 | Credentials from Web Browsers | Anondoorは外部C2へ端末情報を送信し、コマンド実行や画面取得、Chromeパスワード窃取などを実施。 |  | activity--daily-824400f9d449ce9f1dcc | 2025-07 | 2025-07 | 中 | `source--daily-1020ead2bd9b87a29746` |
| Stealth | T1027 | Obfuscated Files or Information | 難読化とDLLサイドロードで検知回避する適応力が指摘。 |  | activity--daily-824400f9d449ce9f1dcc | 2025-07 | 2025-07 | 中 | `source--daily-1020ead2bd9b87a29746` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [Confucius](https://attack.mitre.org/groups/G0142) has exfiltrated stolen files to its C2 server.(Citation: TrendMicro Confucius APT Aug 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Confucius](https://attack.mitre.org/groups/G0142) has created scheduled tasks to maintain persistence on a compromised host.(Citation: TrendMicro Confucius APT Aug 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Confucius](https://attack.mitre.org/groups/G0142) has used PowerShell to execute malicious files and payloads.(Citation: TrendMicro Confucius APT Aug 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [Confucius](https://attack.mitre.org/groups/G0142) has used VBScript to execute malicious code.(Citation: TrendMicro Confucius APT Feb 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Confucius](https://attack.mitre.org/groups/G0142) has used HTTP for C2 communications.(Citation: Uptycs Confucius APT Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Confucius](https://attack.mitre.org/groups/G0142) has used a file stealer that checks the Document, Downloads, Desktop, and Picture folders for documents and images with specific extensions.(Citation: TrendMicro Confucius APT Aug 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Confucius](https://attack.mitre.org/groups/G0142) has downloaded additional files and payloads onto a compromised host following initial access.(Citation: Uptycs Confucius APT Jan 2021)(Citation: TrendMicro Confucius APT Aug 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [Confucius](https://attack.mitre.org/groups/G0142) has used a file stealer to steal documents and images with the following extensions: txt, pdf, png, jpg, doc, xls, xlm, odp, ods, odt, rtf, ppt, xlsx, xlsm, docx, pptx, and jpeg.(Citation: TrendMicro Confucius APT Aug 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [Confucius](https://attack.mitre.org/groups/G0142) has exploited Microsoft Office vulnerabilities, including CVE-2015-1641, CVE-2017-11882, and CVE-2018-0802.(Citation: Uptycs Confucius APT Jan 2021)(Citation: TrendMicro Confucius APT Feb 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [Confucius](https://attack.mitre.org/groups/G0142) has lured victims into clicking on a malicious link sent through spearphishing.(Citation: TrendMicro Confucius APT Aug 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Confucius](https://attack.mitre.org/groups/G0142) has lured victims to execute malicious attachments included in crafted spearphishing emails related to current topics.(Citation: Uptycs Confucius APT Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | [Confucius](https://attack.mitre.org/groups/G0142) has used mshta.exe to execute malicious VBScript.(Citation: TrendMicro Confucius APT Feb 2018)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1221 | Template Injection | [Confucius](https://attack.mitre.org/groups/G0142) has used a weaponized Microsoft Word document with an embedded RTF exploit.(Citation: Uptycs Confucius APT Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Confucius](https://attack.mitre.org/groups/G0142) has dropped malicious files into the startup folder `%AppData%\Microsoft\Windows\Start Menu\Programs\Startup` on a compromised host in order to maintain persistence.(Citation: Uptycs Confucius APT Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Confucius](https://attack.mitre.org/groups/G0142) has crafted and sent victims malicious attachments to gain initial access.(Citation: Uptycs Confucius APT Jan 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [Confucius](https://attack.mitre.org/groups/G0142) has sent malicious links to victims through email campaigns.(Citation: TrendMicro Confucius APT Aug 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Confucius](https://attack.mitre.org/groups/G0142) has exfiltrated victim data to cloud storage service accounts.(Citation: TrendMicro Confucius APT Feb 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | [Confucius](https://attack.mitre.org/groups/G0142) has obtained cloud storage service accounts to host stolen data.(Citation: TrendMicro Confucius APT Feb 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1680 | Local Storage Discovery | [Confucius](https://attack.mitre.org/groups/G0142) has used a file stealer that can examine system drives, including those other than the C drive.(Citation: TrendMicro Confucius APT Aug 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 59件
- IOC観測: 81件
- 複数攻撃で観測: 0件
- 要レビュー候補: 35件
- 非IOC artifact観測: 64件（`artifacts.csv`）

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
| source--confucius--a8091dfddcd96a77 | OperationTibbar A retaliatory targeted attack from SouthAsian APT Group Confucius |  | 不明 | Confucius/OperationTibbar-A-retaliatory-targeted-attack-from-SouthAsian-APT-Group-Confucius.pdf | report | TLP:CLEAR | 中 |
| source--confucius--fd2f4344e5283c41 | README |  | 不明 | Confucius/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--daily-1020ead2bd9b87a29746 | Confuciusハッカーが新たなWooperStealerとAnondoorマルウェアでパキスタンを攻撃 | thehackernews.com | 2025-10-03 | https://thehackernews.com/2025/10/confucius-hackers-hit-pakistan-with-new.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
