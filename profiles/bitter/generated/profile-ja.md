# BITTER 脅威アクタープロファイル

- プロファイルID: `actor--bitter`
- 状態: draft
- 更新日時: 2026-07-29T23:11:59Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

BITTERの標準化プロファイル。リポジトリ内の専用資料8件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **BITTER**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| T-APT-17 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| APT-C-08 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 63; mapping requires review. |
| Manling Flower (Manlinghua) | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 63; mapping requires review. |
| offshore APT organization from South Asia | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 63; mapping requires review. |

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
| Adversary | [BITTER](https://attack.mitre.org/groups/G1002) is a suspected South Asian cyber espionage threat group that has been active since at least 2013. [BITTER](https://attack.mitre.org/groups/G1002) has targeted government, energy, and engineering organizations in Pakistan, China, Bangladesh, and Saudi Arabia.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) |
| Capability | ZxxZ, BitterRAT, ArtraDownloader, SlideRAT |
| Infrastructure |  |
| Victim | Pakistan, Saudi Arabia, PRC |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Bitter | canonical-name | 高 | [South Asia] | https://unit42.paloaltonetworks.com/multiple-artradownloader-variants-used-by-bitter-to-target-pakistan/<br>https://www.proofpoint.com/us/blog/threat-insight/bitter-end-unraveling-eight-years-espionage-antics-part-one<br>https://www.threatray.com/blog/the-bitter-end-unraveling-eight-years-of-espionage-antics-part-two |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | HAZY TIGER | canonical-name | 高 | IN | https://www.bitdefender.com/files/News/CaseStudies/study/352/Bitdefender-PR-Whitepaper-BitterAPT-creat4571-en-EN-GenericUse.pdf<br>https://mp.weixin.qq.com/s/8j_rHA7gdMxY1_X8alj8Zg<br>https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/cyber-year-in-retrospect/yir-cyber-threats-report-download.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | BITTER - G1002 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1002<br>https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html<br>https://www.forcepoint.com/blog/x-labs/bitter-targeted-attack-against-pakistan |
| misp-360net | 蔓灵花 - APT-C-08 | single-alias-intersection | 中 | india | https://apt.360.net/report/apts/5.html |

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
| malware--artradownloader | ArtraDownloader | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--bitterrat | BitterRAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sliderat | SlideRAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--zxxz | ZxxZ | [ZxxZ](https://attack.mitre.org/software/S1013) is a trojan written in Visual C++ that has been used by [BITTER](https://attack.mitre.org/groups/G1002) since at least August 2021, including against Bangladeshi government personnel.(Citation: Cisco Talos Bitter Bangladesh May 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Bitterハッカーグループ、サイバー作戦を拡大 | phishing-campaign | 不明 | 不明 | 2025-06-06 | target--mitre-group--country--7cc14f1275a45f6b7435, target--mitre-group--sector--45b05f79fd85ee2358d0 | malware--artradownloader, malware--zxxz | ttp--activity-rule--06fd46886e579b783e5a | victim--activity-rule--508a2f4c32d7ef8c0bbc | Bitter（別名TA397）は、インド政府の利益に沿った情報収集を目的とする国家支援のハッカーグループと評価されている。 同グループは、南アジアの政府機関や外交機関を主な標的としており、中国、サウジアラビア、南米、トルコなどにも攻撃を拡大している。 攻撃手法は、163[.]com、126[.]com、ProtonMailなどからのスピアフィッシングメールを使用し、マルウェアを含む添付ファイルを送信する。 使用されるマルウェアには、WmRAT、MiyaRAT、KugelBlitz、BDarkRAT、ArtraDownloader、MuuyDownloader（ZxxZ）などが含まれる。 Bitterは、他国の政府や外交機関になりすまし、マルウェアを拡散する手法を用いており、標的のネットワークに対して追加のペイロードを展開する。 | 高 | `source--daily-d3ece976544c2d6909ce` |
| 'Bitter'サイバースパイ、新たなMiyaRATマルウェアで防衛組織を標的に | phishing-campaign | 不明 | 不明 | 2024-12-19 | target--activity-rule--sector--b94dc560a327b601965d, target--mitre-group--sector--45b05f79fd85ee2358d0 |  | ttp--activity-rule--772f5d41013df2be715c, ttp--activity-rule--907ca6412a3b822a13c2, ttp--activity-rule--ad9fc7270c8c42da0122, ttp--activity-rule--e0f8b1e9d8bb8e85fe7b, ttp--activity-rule--e63d3626e7d5417a6e78 | victim--activity-rule--c0e702423a9d88afe0ac | サイバースパイ集団「Bitter」が、新たなマルウェア「MiyaRAT」を使用し、トルコの防衛組織を標的に攻撃を行っている。 攻撃は、投資プロジェクトに関する内容のスピアフィッシングメールから始まり、RARアーカイブを添付している。 アーカイブ内のLNKファイルを開くと、PowerShellコードが実行され、MiyaRATが展開される。 マルウェアは、「DsSvcCleanup」という名前のスケジュールタスクが作成され、17分ごとに悪意のあるcurlコマンドを実行。 MiyaRATは、システム情報の収集、スクリーンショットの取得、キーロギングなどの機能を持つ。 Bitterは、2013年から活動している南アジアのサイバースパイ集団で、主にアジアの政府や重要組織を標的としている。 | 高 | `source--daily-f0b4d93d130c33f27095` |
| BITTERのその先：BITTER APTに関連するハック・フォー・ハイヤー作戦が中東・北アフリカの市民社会を標的に | phishing-campaign | 不明 | 不明 | 2026-04-15 | target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--mitre-group--sector--45b05f79fd85ee2358d0 |  |  | victim--activity-rule--85aa4730c9f9c6b836c9 | Lookoutは、Access Nowの調査協力を通じて、中東の市民社会関係者を狙う継続的なスピアフィッシングとAndroidスパイウェア配布を分析し、2022年以降続く諜報活動と評価した。 Android向けProSpyはSignal、ToTok、Botimを装い、連絡先、SMS、端末情報、文書、画像、音声、動画、アーカイブ、バックアップなどを収集してC2へ送信する。 攻撃は偽のSNS・メッセージ相手やApple Supportを装う接触から始まり、iOS利用者にはiCloudやSignal連携のフィッシング、Android利用者には悪性APK配布が使われた。 研究では複数のC2、配布サイト、フィッシング基盤が確認され、被害対象にはエジプトやレバノンの市民社会関係者のほか、政府関係者とみられる標的も含まれる。 Lookoutは、被害者像、インフラ、マルウェアの共通点から、この活動を南アジア系BITTER APTと関係するハック・フォー・ハイヤー作戦の可能性が高いと中程度の確度で評価した。 | 高 | `source--daily-1dd0fd6a374bf37bcc74` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | 構造化OSINTの被害国フィールドでBITTERの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エジプト | 活動「BITTERのその先：BITTER APTに関連するハック・フォー・ハイヤー作戦が中東・北アフリカの市民社会を標的に」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-1dd0fd6a374bf37bcc74` |
| countries | サウジアラビア | Targeting text mentions saudi arabia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--daily-d3ece976544c2d6909ce`, `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 活動「Bitterハッカーグループ、サイバー作戦を拡大」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-d3ece976544c2d6909ce`, `source--daily-f0b4d93d130c33f27095` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでBITTERの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | バングラデシュ | MITRE ATT&CKのGroup概要でBITTERの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | Targeting text mentions pakistan. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | レバノン | 活動「BITTERのその先：BITTER APTに関連するハック・フォー・ハイヤー作戦が中東・北アフリカの市民社会を標的に」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-1dd0fd6a374bf37bcc74` |
| countries | 中国 | [BITTER](https://attack.mitre.org/groups/G1002) has targeted government, energy, and engineering organizations in Pakistan, China, Bangladesh, and Saudi Arabia.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) | 不明 | 不明 | 高 | `source--daily-d3ece976544c2d6909ce`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | アジア | 活動「Bitterハッカーグループ、サイバー作戦を拡大」の記述で標的地域としてアジアが明示されている。 | 不明 | 不明 | 中 | `source--daily-d3ece976544c2d6909ce`, `source--daily-f0b4d93d130c33f27095` |
| regions | アフリカ | 活動「BITTERのその先：BITTER APTに関連するハック・フォー・ハイヤー作戦が中東・北アフリカの市民社会を標的に」の記述で標的地域としてアフリカが明示されている。 | 不明 | 不明 | 中 | `source--daily-1dd0fd6a374bf37bcc74` |
| regions | 中東 | 活動「BITTERのその先：BITTER APTに関連するハック・フォー・ハイヤー作戦が中東・北アフリカの市民社会を標的に」の記述で標的地域として中東が明示されている。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--daily-1dd0fd6a374bf37bcc74`, `source--daily-d3ece976544c2d6909ce`, `source--daily-f0b4d93d130c33f27095`, `source--target-audit-etda-threat-group-cards` |
| regions | 北アフリカ | 活動「BITTERのその先：BITTER APTに関連するハック・フォー・ハイヤー作戦が中東・北アフリカの市民社会を標的に」の記述で標的地域として北アフリカが明示されている。 | 不明 | 不明 | 中 | `source--daily-1dd0fd6a374bf37bcc74` |
| regions | 南アジア | 活動「Bitterハッカーグループ、サイバー作戦を拡大」の記述で標的地域として南アジアが明示されている。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--daily-d3ece976544c2d6909ce`, `source--daily-f0b4d93d130c33f27095`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | 南米 | 活動「Bitterハッカーグループ、サイバー作戦を拡大」の記述で標的地域として南米が明示されている。 | 不明 | 不明 | 中 | `source--daily-d3ece976544c2d6909ce` |
| regions | 欧州 | トルコ、ドイツで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-d3ece976544c2d6909ce`, `source--daily-f0b4d93d130c33f27095`, `source--target-audit-misp-threat-actor` |
| sectors | 防衛・軍事 | 活動「'Bitter'サイバースパイ、新たなMiyaRATマルウェアで防衛組織を標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-f0b4d93d130c33f27095` |
| sectors | 非営利・市民社会 | 活動「BITTERのその先：BITTER APTに関連するハック・フォー・ハイヤー作戦が中東・北アフリカの市民社会を標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-1dd0fd6a374bf37bcc74` |
| sectors | 政府・行政 | [BITTER](https://attack.mitre.org/groups/G1002) has targeted government, energy, and engineering organizations in Pakistan, China, Bangladesh, and Saudi Arabia.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) | 不明 | 不明 | 高 | `source--daily-1dd0fd6a374bf37bcc74`, `source--daily-d3ece976544c2d6909ce`, `source--daily-f0b4d93d130c33f27095`, `source--mitre-attack-19-1` |
| sectors | エネルギー | [BITTER](https://attack.mitre.org/groups/G1002) has targeted government, energy, and engineering organizations in Pakistan, China, Bangladesh, and Saudi Arabia.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 製造・産業 | [BITTER](https://attack.mitre.org/groups/G1002) has targeted government, energy, and engineering organizations in Pakistan, China, Bangladesh, and Saudi Arabia.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Bitterハッカーグループ、サイバー作戦を拡大 | 非公開 | anonymous | unknown | reported | target--mitre-group--country--7cc14f1275a45f6b7435, target--mitre-group--sector--45b05f79fd85ee2358d0 | malware--artradownloader, malware--zxxz | ttp--activity-rule--06fd46886e579b783e5a | メール／メールアカウント | espionage: Bitter（別名TA397）は、インド政府の利益に沿った情報収集を目的とする国家支援のハッカーグループと評価されている。 | 不明 | 不明 | 2025-06-06 | 高 | `source--daily-d3ece976544c2d6909ce` |
| 被害事例: BITTERのその先：BITTER APTに関連するハック・フォー・ハイヤー作戦が中東・北アフリカの市民社会を標的に | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--mitre-group--sector--45b05f79fd85ee2358d0 |  |  | エンドポイント, モバイル端末 |  | 不明 | 不明 | 2026-04-15 | 高 | `source--daily-1dd0fd6a374bf37bcc74` |
| 被害事例: 'Bitter'サイバースパイ、新たなMiyaRATマルウェアで防衛組織を標的に | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--b94dc560a327b601965d, target--mitre-group--sector--45b05f79fd85ee2358d0 |  | ttp--activity-rule--772f5d41013df2be715c, ttp--activity-rule--907ca6412a3b822a13c2, ttp--activity-rule--ad9fc7270c8c42da0122, ttp--activity-rule--e0f8b1e9d8bb8e85fe7b, ttp--activity-rule--e63d3626e7d5417a6e78 | メール／メールアカウント |  | 不明 | 不明 | 2024-12-19 | 高 | `source--daily-f0b4d93d130c33f27095` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1566.001 | Spearphishing Attachment | 攻撃手法は、163[.]com、126[.]com、ProtonMailなどからのスピアフィッシングメールを使用し、マルウェアを含む添付ファイルを送信する。 |  | activity--daily-3d87dd146a5797f63b60 | 不明 | 不明 | 中 | `source--daily-d3ece976544c2d6909ce` |
| Collection | T1560.001 | Archive via Utility | 攻撃は、投資プロジェクトに関する内容のスピアフィッシングメールから始まり、RARアーカイブを添付している。 |  | activity--daily-6408cf1dda686dc502da | 不明 | 不明 | 中 | `source--daily-f0b4d93d130c33f27095` |
| Collection | T1113 | Screen Capture | MiyaRATは、システム情報の収集、スクリーンショットの取得、キーロギングなどの機能を持つ。 |  | activity--daily-6408cf1dda686dc502da | 不明 | 不明 | 中 | `source--daily-f0b4d93d130c33f27095` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | マルウェアは、「DsSvcCleanup」という名前のスケジュールタスクが作成され、17分ごとに悪意のあるcurlコマンドを実行。 |  | activity--daily-6408cf1dda686dc502da | 不明 | 不明 | 中 | `source--daily-f0b4d93d130c33f27095` |
| Initial Access | T1566.001 | Spearphishing Attachment | 攻撃は、投資プロジェクトに関する内容のスピアフィッシングメールから始まり、RARアーカイブを添付している。 |  | activity--daily-6408cf1dda686dc502da | 不明 | 不明 | 中 | `source--daily-f0b4d93d130c33f27095` |
| Discovery | T1082 | System Information Discovery | MiyaRATは、システム情報の収集、スクリーンショットの取得、キーロギングなどの機能を持つ。 |  | activity--daily-6408cf1dda686dc502da | 不明 | 不明 | 中 | `source--daily-f0b4d93d130c33f27095` |
| Stealth | T1027.013 | Encrypted/Encoded File | [BITTER](https://attack.mitre.org/groups/G1002) has used a RAR SFX dropper to deliver malware.(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [BITTER](https://attack.mitre.org/groups/G1002) has disguised malware as a Windows Security update service.(Citation: Cisco Talos Bitter Bangladesh May 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [BITTER](https://attack.mitre.org/groups/G1002) has used scheduled tasks for persistence and execution.(Citation: Cisco Talos Bitter Bangladesh May 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [BITTER](https://attack.mitre.org/groups/G1002) has exploited CVE-2021-1732 for privilege escalation.(Citation: DBAPPSecurity BITTER zero-day Feb 2021)(Citation: Microsoft CVE-2021-1732 Feb 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [BITTER](https://attack.mitre.org/groups/G1002) has used HTTP POST requests for C2.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | /iMessage delivery T1539 Steal Web Session Cookie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious Link Phishing link click |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Command And Control | T1095 | Non-Application Layer Protocol | [BITTER](https://attack.mitre.org/groups/G1002) has used TCP for C2 communications.(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [BITTER](https://attack.mitre.org/groups/G1002) has downloaded additional malware and tools onto a compromised host.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1111 | Multi-Factor Authentication Interception | hnique ID Technique Name Usage T1566.002 Spearphishing Link WhatsApp/iMessage delivery T1539 Steal Web Session Cookie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious Link Phishing link click |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Execution | T1203 | Exploitation for Client Execution | [BITTER](https://attack.mitre.org/groups/G1002) has exploited Microsoft Office vulnerabilities CVE-2012-0158, CVE-2017-11882, CVE-2018-0798, and CVE-2018-0802.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | okie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious Link Phishing link click |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Execution | T1204.002 | Malicious File | [BITTER](https://attack.mitre.org/groups/G1002) has attempted to lure victims into opening malicious attachments delivered via spearphishing.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1539 | Steal Web Session Cookie | .]com iMessage phishing sender MITRE ATT&CK Mapping Technique ID Technique Name Usage T1566.002 Spearphishing Link WhatsApp/iMessage delivery T1539 Steal Web Session Cookie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious Link Phishing link click |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Execution | T1559.002 | Dynamic Data Exchange | [BITTER](https://attack.mitre.org/groups/G1002) has executed OLE objects using Microsoft Equation Editor to download and run malicious payloads.(Citation: Cisco Talos Bitter Bangladesh May 2022)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [BITTER](https://attack.mitre.org/groups/G1002) has sent spearphishing emails with a malicious RTF document or Excel spreadsheet.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | 40 Email Addresses Email Usage idapple[.]review@icloud[.]com iMessage phishing sender MITRE ATT&CK Mapping Technique ID Technique Name Usage T1566.002 Spearphishing Link WhatsApp/iMessage delivery T1539 Steal Web Session Cookie 10-year tracking cookie T1111 Multi-Factor Authentication Interception Real-time 2FA relay T1078 Valid Accounts iCloud account takeover T1204.001 User Execution: Malicious |  |  | 不明 | 不明 | 中 | `source--bitter--2cfec8a10f89e0b3` |
| Command And Control | T1568 | Dynamic Resolution | [BITTER](https://attack.mitre.org/groups/G1002) has used DDNS for C2 communications.(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573 | Encrypted Channel | [BITTER](https://attack.mitre.org/groups/G1002) has encrypted their C2 communications.(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [BITTER](https://attack.mitre.org/groups/G1002) has registered a variety of domains to host malicious payloads and for C2.(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [BITTER](https://attack.mitre.org/groups/G1002) has obtained tools such as PuTTY for use in their operations.(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [BITTER](https://attack.mitre.org/groups/G1002) has registered domains to stage payloads.(Citation: Forcepoint BITTER Pakistan Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 422件
- IOC観測: 571件
- 複数攻撃で観測: 0件
- 要レビュー候補: 46件
- 非IOC artifact観測: 51件（`artifacts.csv`）

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
| source--bitter--2cfec8a10f89e0b3 | Rotten Apple An Invasive Threat Actor Targeting Civil Society in Lebanon |  | 不明 | bitter/2026/Rotten-Apple_-An-Invasive-Threat-Actor-Targeting-Civil-Society-in-Lebanon.pdf | report | TLP:CLEAR | 中 |
| source--bitter--4b3b9e7d26c1cf64 | Quarterly Adversarial Threat Report Q2 2022 |  | 2022 | bitter/2022/Quarterly-Adversarial-Threat-Report-Q2-2022.pdf | report | TLP:CLEAR | 中 |
| source--bitter--717acb7afca6cd59 | README |  | 不明 | bitter/2022/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--bitter--88ab3c36687131db | readme |  | 不明 | bitter/2026/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--bitter--97af4adeea02b675 | Android Bitter ioc |  | 不明 | bitter/2020/Android-Bitter-ioc.txt | text-data | TLP:CLEAR | 中 |
| source--bitter--9de41446a9a72262 | Bitdefender PR Whitepaper BitterAPT creat4571 en EN GenericUse |  | 不明 | bitter/2020/Bitdefender-PR-Whitepaper-BitterAPT-creat4571-en-EN-GenericUse.pdf | report | TLP:CLEAR | 中 |
| source--bitter--d98102cdd748dedd | Espionage for repression forensic analysis of a cross border hack for hire campaign targeting civil society in MENA 2026 |  | 2026 | bitter/2026/Espionage-for-repression-forensic-analysis-of-a-cross-border-hack-for-hire-campaign-targeting-civil-society-in-MENA-2026.pdf | report | TLP:CLEAR | 中 |
| source--bitter--f28edd1d5cabb4e9 | Inf |  | 不明 | bitter/Inf.MD | repository-notes | TLP:CLEAR | 中 |
| source--daily-1dd0fd6a374bf37bcc74 | BITTERのその先：BITTER APTに関連するハック・フォー・ハイヤー作戦が中東・北アフリカの市民社会を標的に | lookout.com | 2026-04-15 | https://www.lookout.com/threat-intelligence/article/bitter-hack-for-hire | osint-report | TLP:CLEAR | 中 |
| source--daily-d3ece976544c2d6909ce | Bitterハッカーグループ、サイバー作戦を拡大 | thehackernews.com | 2025-06-06 | https://thehackernews.com/2025/06/bitter-hacker-group-expands-cyber.html | osint-report | TLP:CLEAR | 中 |
| source--daily-f0b4d93d130c33f27095 | 'Bitter'サイバースパイ、新たなMiyaRATマルウェアで防衛組織を標的に | bleepingcomputer.com | 2024-12-19 | https://www.bleepingcomputer.com/news/security/bitter-cyberspies-target-defense-orgs-with-new-miyarat-malware/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
