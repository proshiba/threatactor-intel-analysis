# Storm-2603 脅威アクタープロファイル

- プロファイルID: `actor--storm-2603`
- 状態: draft
- 更新日時: 2026-09-21T08:16:06Z
- 構造バージョン: 1.3.0

## エグゼクティブサマリー

Storm-2603の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Storm-2603**
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
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-2603 | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Storm-2603 | canonical-name | 高 | CN | https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/ |
| misp-microsoft-activity-group | Storm-2603 | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

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
| malware--warlock-ransomware | Warlock ransomware | Ransomware deployed by Storm-2603 after ToolShell exploitation. | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |

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
| Storm-2603、ToolShell悪用後にWarlockランサムウェアを展開 | ransomware-extortion | 2025-07-18 | 不明 | 2025-07-22 |  | malware--warlock-ransomware | ttp--activity-rule--af1214636f4d588f7138 |  | Microsoftは、Storm-2603が2025年7月18日以降、オンプレミスSharePointのToolShell脆弱性を悪用し、MimikatzやPsExecで横展開後、グループポリシーでWarlockランサムウェアを展開したと報告した。同時期にはLinen TyphoonとViolet Typhoonも別個に悪用しており、個別被害組織をStorm-2603へ一括帰属しない。 | 高 | `source--microsoft-toolshell-2025` |
| Storm-2603と無関係な第2主体が同居した並行侵入事例 | intrusion | 不明 | 不明 | 2026-06-22 |  |  |  |  | Microsoft DARTは、一つの被害環境でStorm-2603と無関係な第2主体が並行して活動した事例を報告した。Storm-2603側はSharePointを探索し、Velociraptor、Cloudflare Tunnel、Zoho Assist、VS Code経由SSHなどを用いて権限・永続性・遠隔アクセスを確保した。別主体のDLLサイドローディングや独自バックドアはStorm-2603の能力として扱わない。 | 高 | `source--microsoft-storm2603-parallel-intrusion-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Storm-2603、ToolShell悪用後にWarlockランサムウェアを展開 | Storm-2603 | Warlock ransomware | T1190 Exploit Public-Facing Application | 情報なし | 情報なし | 情報なし | 高 |
| Storm-2603と無関係な第2主体が同居した並行侵入事例 | Storm-2603 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 中国 | 活動「ランサムウェアグループがMicrosoft SharePointサーバーを狙う攻撃に加勢」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-0e75e392e2685f601677` |
| countries | 米国 | 活動「米国国家核安全保障局、Microsoft SharePoint攻撃で侵害」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-c9fa26bbe8d21f50b441` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1190 | Exploit Public-Facing Application | 中国拠点Storm-2603がToolShellゼロデイを用いSharePointへWarlockランサムウェアを投入 Shadowserverは脆弱な公開サーバー420台超を発見、これらの脆弱性は7月18日には実際に攻撃に悪用されていることが確認されている 侵入後Mimikatz・PsExec等で横展開しGPOで暗号化ペイロードを配布 CVE-2025-49706/49704/53770が悪用、CISAは連邦機関に即時パッチを命令 NNSAなど米政府機関や欧州中東政府も被害、Microsoftは早急な更新を勧告 |  | activity--daily-b80b607914fb7f62f988 | 不明 | 不明 | 中 | `source--daily-5c143f1d91377b49cfcc` |

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
| source--daily-0e75e392e2685f601677 | ランサムウェアグループがMicrosoft SharePointサーバーを狙う攻撃に加勢 | bleepingcomputer.com | 2025-08-05 | https://www.bleepingcomputer.com/news/security/ransomware-gangs-join-attacks-targeting-microsoft-sharepoint-servers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-5c143f1d91377b49cfcc | Microsoft: SharePointサーバーもランサムウェア攻撃の標的に | bleepingcomputer.com | 2025-07-24 | https://www.bleepingcomputer.com/news/security/microsoft-sharepoint-servers-also-targeted-in-ransomware-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-c9fa26bbe8d21f50b441 | 米国国家核安全保障局、Microsoft SharePoint攻撃で侵害 | bleepingcomputer.com | 2025-07-24 | https://www.bleepingcomputer.com/news/security/us-nuclear-weapons-agency-hacked-in-microsoft-sharepoint-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--storm-2603--358d7946c0a9352d | storm 2603 |  | 不明 | actor_profile/evidence/storm-2603.csv | structured-data | TLP:CLEAR | 中 |
| source--storm-2603--bba67560ab315d2e | UK NCC Group Cyber Threat Intelligence Report September 2025 |  | 2025 | summary/2025/UK_NCC_Group_Cyber_Threat_Intelligence_Report_September_2025_.pdf | report | TLP:CLEAR | 中 |
| source--microsoft-toolshell-2025 | Disrupting active exploitation of on-premises SharePoint vulnerabilities | Microsoft Threat Intelligence | 2025-07-22 | https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--microsoft-storm2603-parallel-intrusion-2026 | One intrusion, two cyberattackers: Uncovering parallel threat activity | Microsoft Defender Experts Cybersecurity Incident Response | 2026-06-22 | https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/ | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
