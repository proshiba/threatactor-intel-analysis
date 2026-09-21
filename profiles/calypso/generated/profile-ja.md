# Calypso 脅威アクタープロファイル

- プロファイルID: `actor--calypso`
- 状態: draft
- 更新日時: 2026-09-21T04:35:02Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

PwCとLumenの一次資料でRed Lamassu（Calypso）の通信事業者標的活動とShowboat／JFMBackdoorの利用を確認したプロファイル。

## アクター名とAlias

- 正規名: **Calypso**
- 初回観測: 2019
- 最終観測: 2026-05-12
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Red Lamassu | PwC Threat Intelligence | exact | 高 | `source--pwc-red-lamassu-jfmbackdoor-2026` | PwC explicitly calls Red Lamassu a.k.a. Calypso. |

## 帰属

PwC describes Red Lamassu (Calypso) as a China-based threat actor, likely operating from Sichuan Province. This does not establish state sponsorship.

- 国: China
- スポンサー種別: unknown
- 確度: 高
- 証拠: `source--pwc-red-lamassu-jfmbackdoor-2026`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | PwC states that Red Lamassu uses persistent access for long-term intelligence collection. | 高 | `source--pwc-red-lamassu-jfmbackdoor-2026` | Actor-specific vendor reporting; not inferred from geography. |

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
| etda-threat-group-cards | Calypso | canonical-name | 高 | China | https://www.ptsecurity.com/ww-en/analytics/calypso-apt-2019/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Calypso&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Calypso | canonical-name | 高 | CN | https://www.ptsecurity.com/upload/corporate/ru-ru/analytics/calypso-apt-2019-rus.pdf<br>https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/<br>https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
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
| malware--showboat | Showboat | Modular Linux post-exploitation framework with remote shell, file-transfer, process-hiding, persistence, and SOCKS5 proxy functions. | 2022 | 2026-04 | 高 | `source--daily-350d930382dd3ed9f923`, `source--pwc-red-lamassu-jfmbackdoor-2026` |
| malware--jfmbackdoor | JFMBackdoor | Windows backdoor delivered through DLL side-loading with shell, file, proxy, screenshot, service, registry, and self-removal functions. | 2025-07 | 2025-10 | 高 | `source--pwc-red-lamassu-jfmbackdoor-2026` |

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
| Red LamassuによるShowboat／JFMBackdoor通信事業者侵入活動 | cyber-espionage | 2022 | 2026-04 | 2026-05-21 | target--activity-rule--sector--210dddb39397dbe50e91, target--targeting-audit--country--3ca3d60e45034ec96db8, target--targeting-audit--country--9bd6c490d9ab834d3cb1, target--targeting-audit--region--36e323894552b9e99bb2 | malware--jfmbackdoor, malware--showboat |  | victim--activity-rule--72a9b284ae5c1aa7f781 | PwCはRed Lamassu（別名Calypso）を追跡し、アジアの通信・政府組織を標的にしていると報告した。PwCが確認した2025年7月から10月の公開ディレクトリには、WindowsバックドアJFMBackdoorと、LumenがShowboatと命名したLinuxマルウェアが共存した。LumenはShowboat関連活動を少なくとも2022年半ばから追跡し、アフガニスタンとアゼルバイジャンの被害通信を確認した。 | 高 | `source--daily-350d930382dd3ed9f923`, `source--pwc-red-lamassu-jfmbackdoor-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Red LamassuによるShowboat／JFMBackdoor通信事業者侵入活動 | Calypso | JFMBackdoor, Showboat | 情報なし | 情報なし | 政府・行政, アゼルバイジャン, アフガニスタン, アジア | 被害事例: Red LamassuによるShowboat／JFMBackdoor通信事業者侵入活動 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アゼルバイジャン | 活動「Red LamassuによるShowboat／JFMBackdoor通信事業者侵入活動」の記述で標的・被害国として明示されている。 | 2022 | 2026-04 | 中 | `source--daily-350d930382dd3ed9f923`, `source--pwc-red-lamassu-jfmbackdoor-2026` |
| countries | アフガニスタン | 活動「Red LamassuによるShowboat／JFMBackdoor通信事業者侵入活動」の記述で標的・被害国として明示されている。 | 2022 | 2026-04 | 中 | `source--daily-350d930382dd3ed9f923`, `source--pwc-red-lamassu-jfmbackdoor-2026` |
| regions | アジア | 活動「Red LamassuによるShowboat／JFMBackdoor通信事業者侵入活動」の記述で標的地域としてアジアが明示されている。 | 2022 | 2026-04 | 中 | `source--daily-350d930382dd3ed9f923`, `source--pwc-red-lamassu-jfmbackdoor-2026` |
| sectors | 政府・行政 | 活動「Red LamassuによるShowboat／JFMBackdoor通信事業者侵入活動」の記述で標的として明示された産業。 | 2022 | 2026-04 | 中 | `source--daily-350d930382dd3ed9f923`, `source--pwc-red-lamassu-jfmbackdoor-2026` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Red LamassuによるShowboat／JFMBackdoor通信事業者侵入活動 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91 | malware--jfmbackdoor, malware--showboat |  |  |  | 2022 | 2026-04 | 2026-05-21 | 高 | `source--daily-350d930382dd3ed9f923`, `source--pwc-red-lamassu-jfmbackdoor-2026` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 4件
- IOC観測: 4件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 1件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Calypso is retained as a separate espionage cluster; PwC explicitly uses Red Lamassu as an alternate name, while Bronze Medley remains an aggregation lead. | 高 | `source--pwc-red-lamassu-jfmbackdoor-2026` | APT1/Comment Crew, Mirage, and Pitty Tiger are not aliases. |

### 情報ギャップ

- Bronze Medley equivalence still requires the original SecureWorks source.
- State sponsorship remains unknown.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- 1 alias lead(s) remain non-canonical pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--calypso--0e7e4f509f2d953e | 200407 MWB COVID White Paper Final |  | 2004-07 | COVID/200407-MWB-COVID-White-Paper_Final.pdf | report | TLP:CLEAR | 中 |
| source--calypso--2e8dcdc34e3d8a19 | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--calypso--3a2fabd4303aaf44 | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--calypso--3c36875326389864 | calypso |  | 不明 | actor_profile/evidence/calypso.csv | structured-data | TLP:CLEAR | 中 |
| source--calypso--4122cc635cc78682 | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--calypso--4d8d55f96e9fdb8f | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--calypso--4ed45b721c043e96 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--calypso--572db5bc0325ab0e | 2021 Vulnerability Landscape |  | 2021 | summary/2022/2021 Vulnerability Landscape.pdf | report | TLP:CLEAR | 中 |
| source--calypso--5a96fdf874b38e48 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--calypso--5cf6cac8ca43bf04 | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--calypso--5df2ed07b29f5b9b | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--calypso--623eb96ebf0ea82b | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--calypso--8977615ec58b186c | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--calypso--a663e4b258965c58 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--calypso--cbe1bfe741302951 | 2024 Malicious Infrastructure Report |  | 2024 | summary/2025/2024 Malicious Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--calypso--e04640fed1c55bf5 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--daily-350d930382dd3ed9f923 | Introducing Showboat: A new malware family taunts defenses and targets international telecom firms | Lumen Black Lotus Labs | 2026-05-21 | https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms | vendor-technical-report | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--pwc-red-lamassu-jfmbackdoor-2026 | Open Directory, Open Season: Inside Red Lamassu's JFMBackdoor | PwC Threat Intelligence | 2026-05-21 | https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html | vendor-technical-report | TLP:CLEAR | 高 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。 2026-09 entity review: removed APT1/Comment Crew, Mirage, Pitty Tiger alias contamination and workbook-only GhostNet/software mappings.
