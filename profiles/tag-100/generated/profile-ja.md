# TAG-100 脅威アクタープロファイル

- プロファイルID: `actor--tag-100`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

TAG-100の標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TAG-100**
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
| etda-threat-group-cards | TAG-100 | canonical-name | 高 | China | https://go.recordedfuture.com/hubfs/reports/cta-2024-0716.pdf<br>https://www.microsoft.com/en-us/security/blog/2024/11/22/microsoft-shares-latest-intelligence-on-north-korean-and-chinese-threat-actors-at-cyberwarcon/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=TAG-100&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-2077 | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Storm-2077 | canonical-name | 高 | CN | https://www.microsoft.com/en-us/security/blog/2024/11/22/microsoft-shares-latest-intelligence-on-north-korean-and-chinese-threat-actors-at-cyberwarcon/<br>https://www.recordedfuture.com/research/tag-100-uses-open-source-tools-in-suspected-global-espionage-campaign<br>https://thehackernews.com/2025/09/chinese-hackers-rednovember-target.html |
| misp-microsoft-activity-group | Storm-2077 | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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

未確認

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
| 中国系ハッカー「RedNovember」がPanteganaとCobalt Strikeで世界の政府を標的に | infrastructure-operation | 2024-06 | 2025-07 | 2025-09-25 | target--activity-rule--sector--210dddb39397dbe50e91 |  |  | victim--activity-rule--75984dc07e4edbef70d3 | Recorded FutureはTAG-100を「RedNovember」と命名、MicrosoftはStorm-2077として追跡。中国国家支援と評価。 2024年6月〜2025年7月にエッジデバイスを狙い侵入、Go製PanteganaやCobalt Strike、Spark RATを用いたと報告。 既知脆弱性を武器化しCheck Point/Cisco/Citrix/F5/Fortinet/Ivanti/PA/SonicWall製品から初期侵入。 ExpressVPNやWarp VPNでインフラを管理、LESLIELOADER変種でBeacon/RAT起動。政府・防衛・法律分野に拡大。 中米・米国・台湾・韓国などで活動。中国訪問前の南米政府のOWA狙いなど地政学的意図が示唆。 | 中 | `source--daily-86f6aba61d69ac9dcac7` |
| TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施 | cyber-espionage | 不明 | 不明 | 2024-07-19 | target--activity-rule--sector--210dddb39397dbe50e91 |  |  | victim--activity-rule--9e892f3b23fa5df3a882 | TAG-100はオープンソースツールを用いて世界中の政府および民間組織を標的にしたサイバースパイ活動を展開。 攻撃はCitrix、F5、Zimbra、Microsoft Exchangeなどの既知の脆弱性を悪用。 2024-4-16から、Palo Alto Networks GlobalProtectの脆弱性（CVE-2024-3400）を悪用した攻撃を広範に行っている。これはエクスプロイトが公開されてすぐ開始された。 攻撃の一環としてPantegana、Spark RAT、Cobalt Strike Beaconを展開。 攻撃対象はアフリカ、アジア、北米、南米、オセアニアなどの広範な業界を攻撃。対象には日本も含まれる。 | 高 | `source--daily-5867c0ebb17c5df135a7` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 中国系ハッカー「RedNovember」がPanteganaとCobalt Strikeで世界の政府を標的に | TAG-100 | 情報なし | 情報なし | 情報なし | 政府・行政 | 被害事例: 中国系ハッカー「RedNovember」がPanteganaとCobalt Strikeで世界の政府を標的に | 中 |
| TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施 | TAG-100 | 情報なし | 情報なし | 情報なし | 政府・行政 | 被害事例: TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イタリア | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてイタリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インドネシア | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カンボジア | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてカンボジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | キューバ | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてキューバが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ジブチ | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてジブチが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドミニカ共和国 | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてドミニカ共和国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィジー | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてフィジーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ボリビア | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてボリビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 日本 | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 構造化OSINTの被害国フィールドでTAG-100の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | アジア | 活動「TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施」の記述で標的地域としてアジアが明示されている。 | 不明 | 不明 | 中 | `source--daily-5867c0ebb17c5df135a7` |
| regions | アフリカ | 活動「TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施」の記述で標的地域としてアフリカが明示されている。 | 不明 | 不明 | 中 | `source--daily-5867c0ebb17c5df135a7` |
| regions | オセアニア | 活動「TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施」の記述で標的地域としてオセアニアが明示されている。 | 不明 | 不明 | 中 | `source--daily-5867c0ebb17c5df135a7` |
| regions | 中南米 | キューバ、ドミニカ共和国、ボリビアで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | 活動「TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施」の記述で標的地域として北米が明示されている。 | 不明 | 不明 | 中 | `source--daily-5867c0ebb17c5df135a7` |
| regions | 南米 | 活動「TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施」の記述で標的地域として南米が明示されている。 | 不明 | 不明 | 中 | `source--daily-5867c0ebb17c5df135a7` |
| regions | 東アジア | 台湾、日本で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | インドネシア、カンボジア、ベトナム、マレーシアで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | イタリア、オランダ、フランス、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | 政府・行政 | 活動「中国系ハッカー「RedNovember」がPanteganaとCobalt Strikeで世界の政府を標的に」の記述で標的として明示された産業。 | 2024-06 | 2025-07 | 中 | `source--daily-5867c0ebb17c5df135a7`, `source--daily-86f6aba61d69ac9dcac7` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 中国系ハッカー「RedNovember」がPanteganaとCobalt Strikeで世界の政府を標的に | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--210dddb39397dbe50e91 |  |  | VPN／リモートアクセス機器 |  | 2024-06 | 2025-07 | 2025-09-25 | 中 | `source--daily-86f6aba61d69ac9dcac7` |
| 被害事例: TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91 |  |  |  | espionage: TAG-100はオープンソースツールを用いて世界中の政府および民間組織を標的にしたサイバースパイ活動を展開。 | 不明 | 不明 | 2024-07-19 | 高 | `source--daily-5867c0ebb17c5df135a7` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.009 | Embedded Payloads | .002 Initial Access:Exploit Public-FacingApplication T1190 DefenseEvasion:ProcessInjection T1055 DefenseEvasion:ObfuscatedFilesor Information: EmbeddedPayloads T1027.009 DefenseEvasion:ObfuscatedFilesor Information: Encrypted/EncodedFile T1027.013 CommandandControl:ApplicationLayer Protocol: WebProtocols T1071 CommandandControl:WebService: Bidirectional Communication T1102.002 10 CTA 2024 0716 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--tag-100--586f62006ec23725` |
| Stealth | T1027.013 | Encrypted/Encoded File | essInjection T1055 DefenseEvasion:ObfuscatedFilesor Information: EmbeddedPayloads T1027.009 DefenseEvasion:ObfuscatedFilesor Information: Encrypted/EncodedFile T1027.013 CommandandControl:ApplicationLayer Protocol: WebProtocols T1071 CommandandControl:WebService: Bidirectional Communication T1102.002 10 CTA 2024 0716 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--tag-100--586f62006ec23725` |
| Privilege Escalation, Stealth | T1055 | Process Injection | T1583.003 Reconnaissance: ActiveScanning: VulnerabilityScanning T1595.002 Initial Access:Exploit Public-FacingApplication T1190 DefenseEvasion:ProcessInjection T1055 DefenseEvasion:ObfuscatedFilesor Information: EmbeddedPayloads T1027.009 DefenseEvasion:ObfuscatedFilesor Information: Encrypted/EncodedFile T1027.013 CommandandControl:ApplicationLayer Protocol: WebProtocols T1071 CommandandControl:WebService: Bidirectional Communication T1102. |  |  | 不明 | 不明 | 中 | `source--tag-100--586f62006ec23725` |
| Command And Control | T1071 | Application Layer Protocol | eddedPayloads T1027.009 DefenseEvasion:ObfuscatedFilesor Information: Encrypted/EncodedFile T1027.013 CommandandControl:ApplicationLayer Protocol: WebProtocols T1071 CommandandControl:WebService: Bidirectional Communication T1102.002 10 CTA 2024 0716 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--tag-100--586f62006ec23725` |
| Command And Control | T1102.002 | Bidirectional Communication | tion: Encrypted/EncodedFile T1027.013 CommandandControl:ApplicationLayer Protocol: WebProtocols T1071 CommandandControl:WebService: Bidirectional Communication T1102.002 10 CTA 2024 0716 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--tag-100--586f62006ec23725` |
| Initial Access | T1190 | Exploit Public-Facing Application | Infrastructure: Virtual PrivateServer T1583.003 Reconnaissance: ActiveScanning: VulnerabilityScanning T1595.002 Initial Access:Exploit Public-FacingApplication T1190 DefenseEvasion:ProcessInjection T1055 DefenseEvasion:ObfuscatedFilesor Information: EmbeddedPayloads T1027.009 DefenseEvasion:ObfuscatedFilesor Information: Encrypted/EncodedFile T1027.013 CommandandControl:ApplicationLayer Protocol: WebProtocols T1071 CommandandControl:WebServi |  |  | 不明 | 不明 | 中 | `source--tag-100--586f62006ec23725` |
| Resource Development | T1583.003 | Virtual Private Server | CYBERTHREATANALYSIS AppendixB—MITREATT&CKTechniques Tactic:Technique ATT&CKCode ResourceDevelopment: AcquireInfrastructure: Virtual PrivateServer T1583.003 Reconnaissance: ActiveScanning: VulnerabilityScanning T1595.002 Initial Access:Exploit Public-FacingApplication T1190 DefenseEvasion:ProcessInjection T1055 DefenseEvasion:ObfuscatedFilesor Information: EmbeddedPayloads T1027.009 DefenseEvasion:ObfuscatedFilesor Information: Encr |  |  | 不明 | 不明 | 中 | `source--tag-100--586f62006ec23725` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | s Tactic:Technique ATT&CKCode ResourceDevelopment: AcquireInfrastructure: Virtual PrivateServer T1583.003 Reconnaissance: ActiveScanning: VulnerabilityScanning T1595.002 Initial Access:Exploit Public-FacingApplication T1190 DefenseEvasion:ProcessInjection T1055 DefenseEvasion:ObfuscatedFilesor Information: EmbeddedPayloads T1027.009 DefenseEvasion:ObfuscatedFilesor Information: Encrypted/EncodedFile T1027.013 CommandandControl:ApplicationLayer P |  |  | 不明 | 不明 | 中 | `source--tag-100--586f62006ec23725` |

## IOC／artifact概要

- IOC値: 19件
- IOC観測: 20件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
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
| source--daily-5867c0ebb17c5df135a7 | TAG-100：新たな脅威アクターがオープンソースツールを使用して広範な攻撃を実施 | thehackernews.com | 2024-07-19 | https://thehackernews.com/2024/07/tag-100-new-threat-actor-uses-open.html | osint-report | TLP:CLEAR | 中 |
| source--daily-86f6aba61d69ac9dcac7 | 中国系ハッカー「RedNovember」がPanteganaとCobalt Strikeで世界の政府を標的に | thehackernews.com | 2025-09-25 | https://thehackernews.com/2025/09/chinese-hackers-rednovember-target.html | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--tag-100--586f62006ec23725 | TAG 100 Uses Open Source Tools in Suspected Global Espionage Campaign |  | 不明 | UNC****/TAG-*/TAG-100 Uses Open-Source Tools in Suspected Global Espionage Campaign.pdf | report | TLP:CLEAR | 中 |
| source--tag-100--58c7040aa9d9e524 | readme |  | 不明 | UNC****/TAG-*/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
