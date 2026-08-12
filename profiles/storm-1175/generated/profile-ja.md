# Storm-1175 脅威アクタープロファイル

- プロファイルID: `actor--storm-1175`
- 状態: draft
- 更新日時: 2026-08-12T01:51:59Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Storm-1175の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Storm-1175**
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
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-1175 | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Storm-1175 | canonical-name | 高 | CN | https://www.microsoft.com/en-us/security/blog/2025/10/06/investigating-active-exploitation-of-cve-2025-10035-goanywhere-managed-file-transfer-vulnerability/ |
| misp-microsoft-activity-group | Storm-1175 | canonical-name | 高 | CN | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
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
| malware--daily-a4bc802d0acb6f9da9b3 | StormEncryptor | Storm-1175との直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 2026-08-02 | 2026-08-02 | 高 | `source--daily-b76705cd3ccd88a20697` |

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
| Microsoft、Medusaランサムウェアのアフィリエイトをゼロデイ攻撃と関連付け | ransomware-extortion | 不明 | 不明 | 2026-04-07 |  |  |  | victim--activity-rule--469e30e58089a636de26 | Microsoft は、Medusa ランサムウェアの展開で知られる中国拠点の金銭目的グループ Storm-1175 が、n-day と zero-day を高速に悪用していると報告した。 同グループは新規脆弱性の武器化が非常に速く、場合によっては公開前の週から悪用し、初期侵入から数日、時に24時間以内に暗号化まで進むとされる。 攻撃では複数の脆弱性を連鎖利用し、新規ユーザー作成、RMM 導入、認証情報窃取、セキュリティ機能停止を経て、ランサムウェア投下とデータ流出に至る。 具体例として、GoAnywhere MFT の CVE-2025-10035 を修正前から1週間超悪用し、SmarterMail の CVE-2026-23760 もゼロデイとして利用したと記載されている。 さらに Exchange、PaperCut、Ivanti、ScreenConnect、TeamCity、SimpleHelp、CrushFTP、SmarterMail、BeyondTrust など計10製品超の脆弱性悪用が確認された。 Storm-1175は、公開資産の脆弱性を特定する能力に長けており、エクスプロイトブローカーなどを通じて高度な開発能力やリソースへのアクセスを得ている可能性があると分析されている。 | 中 | `source--daily-6d966f0f2bd59b705455` |
| 新たなStormEncryptorランサムウェア、元Medusaアフィリエイトが使用 | ransomware-extortion | 2026-08-02 | 2026-08-02 | 2026-08-11 |  | malware--daily-a4bc802d0acb6f9da9b3 | ttp--activity-rule--930a84def0728e17de5d, ttp--activity-rule--b66518744de700598f4d | victim--activity-rule--a6c8bb210ab26d8f527e | Microsoftは、金銭目的の攻撃者Storm-1175が2026年8月2日から新型ランサムウェア「StormEncryptor」を展開していると確認した。 最近の攻撃では、N-able N-centralの認証回避脆弱性CVE-2026-18577を初期侵入に悪用した可能性が高いと評価されている。 侵入後はAnyDeskやSimpleHelpで遠隔操作し、Advanced IP Scannerで探索、MimikatzでLSASSから認証情報を窃取する。 StormEncryptorはファイルへ「.encrypted」を付けて暗号化し、3日以内の身代金交渉を要求し、応じなければ窃取データを公開すると脅迫する。 Storm-1175は初期侵入からデータ窃取、ランサムウェア展開まで数日以内と速く、従来使用していたMedusaからStormEncryptorへ移行した。 | 高 | `source--daily-b76705cd3ccd88a20697` |
| Microsoft：重大なGoAnywhere脆弱性がランサムウェア攻撃で悪用 | ransomware-extortion | 不明 | 不明 | 2025-10-07 |  |  |  | victim--activity-rule--381a605f874c19b7c2ce | FortraのGoAnywhere MFTに最大深刻度のCVE-2025-10035（License Servletの不正デシリアライズ）が存在しリモートエクスプロイト可能。 MicrosoftはMedusaのアフィリエイト「Storm-1175」による悪用を確認、9月11日以降継続し9月10日からのゼロデイ疑いも報告。 侵入後はSimpleHelp/MeshAgentで持続化、Netscanとmstsc.exeで偵察・横展開し、Rcloneで持ち出し後にMedusaで暗号化。 Shadowserverは500超のGoAnywhereインスタンス露出を観測、何件が修正済みかは不明。 Fortraは9月18日に修正提供。Microsoft/Fortraは更新適用とログで"SignedObject.getObject"のスタックトレース確認を推奨。 | 中 | `source--daily-d32841215eeaadd319dd` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Microsoft、Medusaランサムウェアのアフィリエイトをゼロデイ攻撃と関連付け | Storm-1175 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: Microsoft、Medusaランサムウェアのアフィリエイトをゼロデイ攻撃と関連付け | 中 |
| 新たなStormEncryptorランサムウェア、元Medusaアフィリエイトが使用 | Storm-1175 | StormEncryptor | T1486 Data Encrypted for Impact, T1219.002 Remote Desktop Software | 情報なし | 情報なし | 被害事例: 新たなStormEncryptorランサムウェア、元Medusaアフィリエイトが使用 | 高 |
| Microsoft：重大なGoAnywhere脆弱性がランサムウェア攻撃で悪用 | Storm-1175 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: Microsoft：重大なGoAnywhere脆弱性がランサムウェア攻撃で悪用 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | シリア | 活動「Microsoft：重大なGoAnywhere脆弱性がランサムウェア攻撃で悪用」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-d32841215eeaadd319dd` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Microsoft：重大なGoAnywhere脆弱性がランサムウェア攻撃で悪用 | 非公開 | anonymous | unknown | reported |  |  |  | サーバー | encryption: Microsoft：重大なGoAnywhere脆弱性がランサムウェア攻撃で悪用 | 不明 | 不明 | 2025-10-07 | 中 | `source--daily-d32841215eeaadd319dd` |
| 被害事例: Microsoft、Medusaランサムウェアのアフィリエイトをゼロデイ攻撃と関連付け | 非公開 | aggregate | multiple-organizations | reported |  |  |  |  | data-theft: 攻撃では複数の脆弱性を連鎖利用し、新規ユーザー作成、RMM 導入、認証情報窃取、セキュリティ機能停止を経て、ランサムウェア投下とデータ流出に至る。<br>credential-theft: 攻撃では複数の脆弱性を連鎖利用し、新規ユーザー作成、RMM 導入、認証情報窃取、セキュリティ機能停止を経て、ランサムウェア投下とデータ流出に至る。<br>encryption: Microsoft、Medusaランサムウェアのアフィリエイトをゼロデイ攻撃と関連付け | 不明 | 不明 | 2026-04-07 | 中 | `source--daily-6d966f0f2bd59b705455` |
| 被害事例: 新たなStormEncryptorランサムウェア、元Medusaアフィリエイトが使用 | 非公開 | anonymous | unknown | reported |  | malware--daily-a4bc802d0acb6f9da9b3 | ttp--activity-rule--930a84def0728e17de5d, ttp--activity-rule--b66518744de700598f4d |  | data-theft: Storm-1175は初期侵入からデータ窃取、ランサムウェア展開まで数日以内と速く、従来使用していたMedusaからStormEncryptorへ移行した。<br>credential-theft: 侵入後はAnyDeskやSimpleHelpで遠隔操作し、Advanced IP Scannerで探索、MimikatzでLSASSから認証情報を窃取する。<br>encryption: 新たなStormEncryptorランサムウェア、元Medusaアフィリエイトが使用 | 2026-08-02 | 2026-08-02 | 2026-08-11 | 高 | `source--daily-b76705cd3ccd88a20697` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Impact | T1486 | Data Encrypted for Impact | StormEncryptorはファイルへ「.encrypted」を付けて暗号化し、3日以内の身代金交渉を要求し、応じなければ窃取データを公開すると脅迫する。 | malware--daily-a4bc802d0acb6f9da9b3 | activity--daily-612ec3618eed5cfcdbb9 | 2026-08-02 | 2026-08-02 | 中 | `source--daily-b76705cd3ccd88a20697` |
| Command And Control | T1219.002 | Remote Desktop Software | 侵入後はAnyDeskやSimpleHelpで遠隔操作し、Advanced IP Scannerで探索、MimikatzでLSASSから認証情報を窃取する。 |  | activity--daily-612ec3618eed5cfcdbb9 | 2026-08-02 | 2026-08-02 | 中 | `source--daily-b76705cd3ccd88a20697` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 4件（`artifacts.csv`）

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
| source--daily-6d966f0f2bd59b705455 | Microsoft、Medusaランサムウェアのアフィリエイトをゼロデイ攻撃と関連付け | bleepingcomputer.com | 2026-04-07 | https://www.bleepingcomputer.com/news/security/microsoft-links-medusa-ransomware-affiliate-to-zero-day-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-b76705cd3ccd88a20697 | 新たなStormEncryptorランサムウェア、元Medusaアフィリエイトが使用 | bsky.app | 2026-08-11 | https://bsky.app/profile/threatintel.microsoft.com/post/3msjiybnb252n | osint-report | TLP:CLEAR | 中 |
| source--daily-d32841215eeaadd319dd | Microsoft：重大なGoAnywhere脆弱性がランサムウェア攻撃で悪用 | bleepingcomputer.com | 2025-10-07 | https://www.bleepingcomputer.com/news/security/microsoft-critical-goanywhere-bug-exploited-in-ransomware-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--storm-1175--0a35c08ece7004b4 | Microsoft Digital Defense Report 2025 |  | 2025 | summary/2025/Microsoft-Digital-Defense-Report-2025.pdf | report | TLP:CLEAR | 中 |
| source--storm-1175--3a67199fb3ac6578 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--storm-1175--75a712cbf9d9c02b | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--storm-1175--beaa23509b63caea | storm 1175 |  | 不明 | actor_profile/evidence/storm-1175.csv | structured-data | TLP:CLEAR | 中 |
| source--storm-1175--db483ee73553439a | 2024 Annual Cybersecurity Vulnerability Threat Landscape Research Report |  | 2024 | summary/2025/2024_Annual_Cybersecurity_Vulnerability_Threat_Landscape_Research_Report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
