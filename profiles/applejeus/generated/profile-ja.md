# AppleJeus 脅威アクタープロファイル

- プロファイルID: `actor--applejeus`
- 状態: draft
- 更新日時: 2026-07-29T23:11:59Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

AppleJeusの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **AppleJeus**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Citrine Sleet | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Gleaming Pisces | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC1720 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC4736 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Lazarus Group | related-to | Associated with the broader [Lazarus Group](https://attack.mitre.org/groups/G0032) umbrella of actors, [AppleJeus](https://attack.mitre.org/groups/G1049) has been active since at least 2018 and is closely aligned in resources with TEMP.hermit, another DPRK-affiliated group under the same umbrella.(Citation: dtex DPRK 2025 structure ITworkers) The group’s primary mission is to generate and launder revenue to provide financial support to the government. | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [AppleJeus](https://attack.mitre.org/groups/G1049) is a North Korean state-sponsored threat group attributed to the Reconnaissance General Bureau. Associated with the broader [Lazarus Group](https://attack.mitre.org/groups/G0032) umbrella of actors, [AppleJeus](https://attack.mitre.org/groups/G1049) has been active since at least 2018 and is closely aligned in resources with TEMP.hermit, another DPRK-affiliated group under the same umbrella.(Citation: dtex DPRK 2025 structure ITworkers) The group’s primary mission is to generate and launder revenue to provide financial support to the government. [AppleJeus](https://attack.mitre.org/groups/G1049) primarily targets the cryptocurrency industry and is most notably responsible for the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057).(Citation: Mandiant 3cx UNC4736 2023) The group traditionally deploys malicious cryptocurrency software in combination with [Phishing](https://attack.mitre.org/techniques/T1566). From these compromised environments, it selectively deploys additional backdoors to enable extended operations against high-value financial targets.(Citation: Mandiant DPRK Groups 2023)(Citation: JPCert Blog Laz Subgroups 2025) |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Lazarus Group, Hidden Cobra, Labyrinth Chollima | multiple-name-intersection | 高 | North Korea | https://blog.malwarebytes.com/threat-analysis/2019/03/the-advanced-persistent-threat-files-lazarus-group/<br>https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/a-look-into-the-lazarus-groups-operations<br>https://www.kaspersky.com/about/press-releases/2017_chasing-lazarus-a-hunt-for-the-infamous-hackers-to-prevent-large-bank-robberies |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Citrine Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Lazarus Group | single-alias-intersection | 中 | KP, Korea (Democratic People's Republic of) | https://threatpost.com/operation-blockbuster-coalition-ties-destructive-attacks-to-lazarus-group/116422/<br>https://www.us-cert.gov/ncas/alerts/TA17-164A<br>https://www.us-cert.gov/ncas/alerts/TA17-318A |
| misp-threat-actor | UNC4736 | single-alias-intersection | 中 | KP | https://www.mandiant.com/resources/blog/3cx-software-supply-chain-compromise |
| misp-microsoft-activity-group | Citrine Sleet | single-alias-intersection | 中 | KP, North Korea | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | AppleJeus - G1049 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1049<br>https://blogs.jpcert.or.jp/en/2025/03/classifying-lazaruss-subgroup.html<br>https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise/ |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Operation Sharpshooter | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| STARDUST CHOLLIMA | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| TraderTraitor | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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
| tool--mitre--s1144 | FRP | [FRP](https://attack.mitre.org/software/S1144), which stands for Fast Reverse Proxy, is an openly available tool that is capable of exposing a server located behind a firewall or Network Address Translation (NAT) to the Internet. [FRP](https://attack.mitre.org/software/S1144) can support multiple protocols including TCP, UDP, and HTTP(S) and has been abused by threat actors to proxy command and control communications.(Citation: FRP GitHub)(Citation: Joint Cybersecurity Advisory Volt Typhoon June 2023)(Citation: RedCanary Mockingbird May 2020)(Citation: DFIR Phosphorus November 2021) | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |

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
| 3CX Supply Chain Attack | campaign | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 2026-05-12 | target--activity-rule--sector--b94dc560a327b601965d, target--mitre-group--sector--f85697f31d3eefe544e2 |  | ttp--mitre-campaign--00eebce179e2cc165a78, ttp--mitre-campaign--09b1c7c970cc6f0872ff, ttp--mitre-campaign--10162a98ebfac9199a1f, ttp--mitre-campaign--1eee9d018fec2af13386, ttp--mitre-campaign--213481447859524a9328, ttp--mitre-campaign--271a72b9c2a22725acff, ttp--mitre-campaign--39b87e2e673dd6758c97, ttp--mitre-campaign--464d5726f874a68d2ff3, ttp--mitre-campaign--4fec03052d9bb90bcfcc, ttp--mitre-campaign--53a86942be3f4c2beffa, ttp--mitre-campaign--84a8e41beba9ba2a8ecb, ttp--mitre-campaign--863977544862a6feb9d7, ttp--mitre-campaign--8e86c6b7197ec50ac3de, ttp--mitre-campaign--aab01ff9f91ce4d15c34, ttp--mitre-campaign--adf5756d9d7c4a3ebe51, ttp--mitre-campaign--b5a6e63f8effa5428825, ttp--mitre-campaign--b69f659ac2baa6116cd9, ttp--mitre-campaign--e1007fd2d70a43c93a3c, ttp--mitre-campaign--f06ef908333d43453295, ttp--mitre-campaign--f0c2354d4975290b9f03, ttp--mitre-campaign--f434cc8e6bdd6b0a6530, ttp--mitre-campaign--fe00acecd59b2d85e57e | victim--activity-rule--92a04f97301418051a53 | The [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057) was the first publicly reported case of one supply chain compromise triggering another, leading to a cascading, two-stage intrusion. The initial supply chain attack began when a 3CX employee downloaded and executed a trojanized, end-of-life version of the X_Trader trading software from Trading Technologies. This provided UNC4736, a threat cluster associated with [AppleJeus](https://attack.mitre.org/groups/G1049), access to the 3CX environment. From there UNC4736 compromised the Windows and macOS build environments used to distribute the 3CX desktop application to their customers.(Citation: Mandiant 3cx UNC4736 2023) While 3CX serves more than 600,000 customers and 12 million users, only a subset of systems were affected. Subsequent targeting focused on victims in the defense and cryptocurrency sectors, where attackers deployed secondary payloads such as Gopuram for credential theft and persistence.(Citation: Kaspersky 3CX Gopuram 2023) The campaign began in late 2022 and was disrupted after security vendors publicly reported the compromise in March 2023.(Citation: 3cx official statement 2023)(Citation: Krebs 3cx overview 2023) | 高 | `source--mitre-attack-19-1` |
| Radiant、5,000万ドルの暗号通貨強奪を北朝鮮ハッカーと結びつける | malware-campaign | 不明 | 不明 | 2024-12-10 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--932f4928d5e1ec28e2df |  |  | victim--activity-rule--83f649cfc55e69ff542f | Radiant Capitalは、10月16日のサイバー攻撃で5,000万ドルの暗号通貨が盗まれたと発表。 サイバーセキュリティ企業Mandiantの調査により、攻撃者は北朝鮮の国家支援ハッカー「Citrine Sleet」（別名UNC4736、AppleJeus）であると特定。 攻撃は、3人の信頼された開発者のデバイスにマルウェアを感染させ、正規の署名を収集して不正な取引を実行する手法で行われた。 ハッカーは、ルーチンのマルチシグネチャプロセスを悪用し、トランザクションエラーを装って有効な署名を収集し、ArbitrumおよびBSC市場から資金を窃取。 米国政府は以前から、北朝鮮のハッカーが暗号通貨企業を標的にして資金を窃取し、国家活動を支援していると警告している。 攻撃は2024年9月11日に始まり、Radiantの開発者が元請負業者を装ったTelegramメッセージを受信し、悪意のあるZIPファイルをダウンロードするように仕向けられた。このZIPファイルには、「InletDrift」という名前のmacOSマルウェアがあった。 | 中 | `source--daily-f645f7df90b96e0f1b18` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イスラエル | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インド | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エクアドル | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてエクアドルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | グアテマラ | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてグアテマラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チリ | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてチリが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | バングラデシュ | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてバングラデシュが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | メキシコ | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてメキシコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 南アフリカ | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国として南アフリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 日本 | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 活動「Radiant、5,000万ドルの暗号通貨強奪を北朝鮮ハッカーと結びつける」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-f645f7df90b96e0f1b18`, `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 香港 | 構造化OSINTの被害国フィールドでAppleJeusの標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中南米 | エクアドル、グアテマラ、チリ、ブラジル、メキシコで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 全世界 | 構造化OSINTの被害地域フィールドでAppleJeusの標的範囲として全世界が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、メキシコ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-f645f7df90b96e0f1b18`, `source--target-audit-etda-threat-group-cards` |
| regions | 南アジア | インド、バングラデシュで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南米 | エクアドル、チリ、ブラジルで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | 中国、台湾、日本、韓国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | タイ、フィリピン、ベトナムで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ポーランド、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | オランダ、ドイツ、フランス、ベルギー、ポーランド、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | IT・ソフトウェア | 活動「Radiant、5,000万ドルの暗号通貨強奪を北朝鮮ハッカーと結びつける」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-f645f7df90b96e0f1b18` |
| sectors | 防衛・軍事 | 活動「3CX Supply Chain Attack」の記述で標的として明示された産業。 | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 中 | `source--mitre-attack-19-1` |
| sectors | 金融 | From these compromised environments, it selectively deploys additional backdoors to enable extended operations against high-value financial targets.(Citation: Mandiant DPRK Groups 2023)(Citation: JPCert Blog Laz Subgroups 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 暗号資産・Web3 | [AppleJeus](https://attack.mitre.org/groups/G1049) primarily targets the cryptocurrency industry and is most notably responsible for the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057).(Citation: Mandiant 3cx UNC4736 2023) The group traditionally deploys malicious cryptocurrency software in combination with [Phishing](https://attack.mitre.org/techniques/T1566). | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Radiant、5,000万ドルの暗号通貨強奪を北朝鮮ハッカーと結びつける | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--932f4928d5e1ec28e2df |  |  |  |  | 不明 | 不明 | 2024-12-10 | 中 | `source--daily-f645f7df90b96e0f1b18` |
| 被害事例: 3CX Supply Chain Attack | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--b94dc560a327b601965d, target--mitre-group--sector--f85697f31d3eefe544e2 |  | ttp--mitre-campaign--00eebce179e2cc165a78, ttp--mitre-campaign--09b1c7c970cc6f0872ff, ttp--mitre-campaign--10162a98ebfac9199a1f, ttp--mitre-campaign--1eee9d018fec2af13386, ttp--mitre-campaign--213481447859524a9328, ttp--mitre-campaign--271a72b9c2a22725acff, ttp--mitre-campaign--39b87e2e673dd6758c97, ttp--mitre-campaign--464d5726f874a68d2ff3, ttp--mitre-campaign--4fec03052d9bb90bcfcc, ttp--mitre-campaign--53a86942be3f4c2beffa, ttp--mitre-campaign--84a8e41beba9ba2a8ecb, ttp--mitre-campaign--863977544862a6feb9d7, ttp--mitre-campaign--8e86c6b7197ec50ac3de, ttp--mitre-campaign--aab01ff9f91ce4d15c34, ttp--mitre-campaign--adf5756d9d7c4a3ebe51, ttp--mitre-campaign--b5a6e63f8effa5428825, ttp--mitre-campaign--b69f659ac2baa6116cd9, ttp--mitre-campaign--e1007fd2d70a43c93a3c, ttp--mitre-campaign--f06ef908333d43453295, ttp--mitre-campaign--f0c2354d4975290b9f03, ttp--mitre-campaign--f434cc8e6bdd6b0a6530, ttp--mitre-campaign--fe00acecd59b2d85e57e |  | supply-chain: 3CX Supply Chain Attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 2026-05-12 | 高 | `source--mitre-attack-19-1` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1071.001 | Web Protocols | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049)'s COLDCAT C2 leverages cookie headers to contain data over HTTPS. Cookies also contain hardcoded variables `__tutma` or `__tutmc` in the payload's HTTPS request.(Citation: Mandiant 3cx UNC4736 2023)(Citation: Unit42 3cx supply chain 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1559 | Inter-Process Communication | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049)'s VEILEDSIGNAL creates and listens on a Windows named pipe to exchange messages between modules.(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049)'s VEILEDSIGNAL communication module supports three commands to conduct the following actions: send implant data, execute shellcode, and terminate itself.(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | During [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) has gained access to the 3CX corporate environment through legitimate VPN credentials.(Citation: 3cx official statement 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.016 | Installer Packages | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) added a malicious .dylib file to a .dmg installer package for the macOS 3CX application.(Citation: Unit42 3cx supply chain 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) compromised the `www.tradingtechnologies[.]com` website hosting a hidden IFRAME to exploit visitors, two months before the site was known to deliver a compromised version of the X_TRADER software package.(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1620 | Reflective Code Loading | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) leverages the publicly available open-source project DAVESHELL to convert PE-COFF files to position-independent code to reflectively load the payload into memory.(Citation: Mandiant 3cx UNC4736 2023)(Citation: Daveshell sRDI GitHub shell code loader) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) leveraged ICONICSTEALER to steal browser information to include browser history located on the infected host.(Citation: Volexity 3CX Supply Chain Compromise AppleJeus IconicStealer March 2023)(Citation: Mandiant 3cx UNC4736 2023)(Citation: Trend Micro 3CX AppleJeus ICONICSTEALER March 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.007 | Msiexec | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) delivered components using a Windows Installer package (.msi). The MSI installer extracted several files and executed the 3CXDesktopApp.exe, which loaded the malicious library file ffmpeg.dll.(Citation: Unit42 3cx supply chain 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049)'s VEILEDSIGNAL uses process injection to inject the C2 communication module code in the first found process instance of Chrome, Firefox, or Edge web browsers. It also monitors the established named pipe and re-injects the C2 communication module if necessary.(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.002 | Portable Executable Injection | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) uses the SigFlip tool to inject arbitrary code without affecting or breaking the file's signature.(Citation: GitHub SigFlip opensource tool)(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) payloads use AES-256 GCM cipher to encrypt data to include ICONICSTEALER and VEILEDSIGNAL.(Citation: Volexity 3CX Supply Chain Compromise AppleJeus IconicStealer March 2023)(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) leveraged the Chrome vulnerability, CVE-2022-0609, in combination with a [Drive-by Compromise](https://attack.mitre.org/techniques/T1189) website.(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) encrypts its dynamic library files (.dll) using RC4, and when loaded only decrypts specific portions of the file using the key `3jB(2bsG#@c7`.(Citation: Unit42 3cx supply chain 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.015 | Electron Applications | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) leveraged the 3CX application's electron framework to execute its malicious libraries under the official 3CX electron application.(Citation: Unit42 3cx supply chain 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) splits functionally across multiple .dll files using export functions, such as DLLGetClassObject, to execute code from an embedded .dll file within another .dll file. [AppleJeus](https://attack.mitre.org/groups/G1049) has also used DLL search order hijacking via the IKEEXT service, running with LocalSystem privileges, to load the TAXHAUL DLL for persistence.(Citation: Unit42 3cx supply chain 2023)(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) first compromised an “end-of-life" trading software application which was downloaded and executed inside the 3CX enterprise environment. The second compromise modified the Windows and macOS build environments used to distribute the 3CX software to their customer base.(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.009 | Embedded Payloads | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) uses embedded .dll as apart of a chained delivery mechanism to invoke the COM class factory.(Citation: Unit42 3cx supply chain 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.004 | Launch Daemon | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) installs a Launch Daemon to execute the POOLRAT macOS backdoor software.(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | Although the X_TRADER platform was reportedly discontinued in 2020, it was still available for download from the legitimate Trading Technologies website in 2022. During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) used a code signing certificate to digitally sign the malicious software with an expiration date set to October 2022. This file was signed with the subject “Trading Technologies International, Inc” and contained the executable file Setup.exe, also signed with the same digital certificate.(Citation: Mandiant 3cx UNC4736 2023)(Citation: 3cx official statement 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.001 | Dead Drop Resolver | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049) leveraged a GitHub repository to host icon files containing the command and control URL.(Citation: Unit42 3cx supply chain 2023)(Citation: Mandiant 3cx UNC4736 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1678 | Delay Execution | During the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057), [AppleJeus](https://attack.mitre.org/groups/G1049)'s software generates a randomly selected date that is between 1-4 weeks in the future. This timestamp is then checked against the current time of the compromised machine, and the malware will sleep until that time is encountered.(Citation: Unit42 3cx supply chain 2023) |  | activity--3cx-supply-chain-attack | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | [AppleJeus](https://attack.mitre.org/groups/G1049) has used spearphishing emails to distribute malicious payloads.(Citation: dtex DPRK 2025 structure ITworkers) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | [AppleJeus](https://attack.mitre.org/groups/G1049) has targeted the cryptocurrency industry with the goal of stealing digital assets.(Citation: Mandiant DPRK Groups 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 84件（`artifacts.csv`）

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
| source--applejeus--00a6486816050b51 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--09d7c9a46f9d6193 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--0e13b86d117533be | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--11eecd7bc046b964 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--20545ea2e414402a | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--2c3875edf437d32b | Dream Job Campaign |  | 不明 | lazarus/Dream-Job-Campaign.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--360fff7f63ffb03c | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--applejeus--44c7ca0cab019d23 | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--4ac4c38ded7903e2 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--50bbc5ff9b7c43f0 | multiple campaigns of the Lazarus group and their connections |  | 不明 | lazarus/multiple campaigns of the Lazarus group and their connections.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--53a55fb8b8c47aeb | konni threat insight paper triple threat N Korea aligned TA406 steals scams spies |  | 不明 | konni/konni-threat-insight-paper-triple-threat-N-Korea-aligned-TA406-steals-scams-spies.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--55753821d8e9785a | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--5e1bdc358cbf325b | Blurred Lines of Cyber Threat Attribution |  | 不明 | International Strategic/Korea/ Blurred-Lines-of-Cyber-Threat-Attribution.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--62358c65b873eb55 | kaspersky ics cert lazarus targets defense industry with threatneedle en 20210225 |  | 2021-02-25 | lazarus/kaspersky-ics-cert-lazarus-targets-defense-industry-with-threatneedle-en-20210225.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--6ee8d02ff0668468 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--721829f759b32d33 | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--842144722ffec290 | 2022 Yearbook of APT group Analysis |  | 2022 | summary/2023/2022 Yearbook of APT group Analysis.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--868f81b0e798b812 | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--9242cd7af5ccb5b0 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--949fcdd4db2f5cff | The Lazarus Constellation |  | 不明 | lazarus/The_Lazarus_Constellation.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--a8ea13d9767203dc | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--b33828eedd3c6e22 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--b6740c4ccfa1c71a | 2026 Mid year Blockchain Security and AML Report |  | 2026 | summary/2026/2026 Mid-year Blockchain Security and AML Report.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--c47e2b21577e983f | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--ccee8dd6cc668e73 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--d13cc73cd3f9745f | applejeus |  | 不明 | actor_profile/evidence/applejeus.csv | structured-data | TLP:CLEAR | 中 |
| source--applejeus--d45c0b5342dc3f98 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--e02cad3035fecb76 | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--applejeus--ec8f2f2be49c9846 | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--f41bf6d2b1b91d22 | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--f4eb431117358cfc | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--fa072972102e0db5 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--daily-f645f7df90b96e0f1b18 | Radiant、5,000万ドルの暗号通貨強奪を北朝鮮ハッカーと結びつける | bleepingcomputer.com | 2024-12-10 | https://www.bleepingcomputer.com/news/security/radiant-links-50-million-crypto-heist-to-north-korean-hackers/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
