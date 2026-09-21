# NetTraveler 脅威アクタープロファイル

- プロファイルID: `actor--nettraveler`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

NetTravelerは少なくとも2004年から2013年にかけて40か国・350件超の高位標的を侵害したサイバースパイ活動集合である。同名ツールキットを別マルウェア実体として記録し、Dantiとの関係はKasperskyの低確度な接続疑義に限定する。

## アクター名とAlias

- 正規名: **NetTraveler**
- 初回観測: 2004
- 最終観測: 2013-06-04
- 活動状態: unknown

Aliasなし

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | Kaspersky explicitly describes the activity as cyber espionage and documents theft of sensitive technical and government information. | 高 | `source--kaspersky-nettraveler-2013` | Motivation is source-stated; sponsorship remains unknown. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| actor--danti | related-to | KasperskyはDantiの起源を不明とした上で、NetTravelerおよびDragonOKとの接続可能性を疑っていると記述した。 | 低 | `source--kaspersky-q2-2016-danti` |

## 関連する企業・個人

関連エンティティなし

### エンティティ関係

確認された関係なし

### 法的措置

確認された法的措置なし

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
| etda-threat-group-cards | NetTraveler, APT 21, Hammer Panda | canonical-name | 高 | China | https://www.kaspersky.com/about/press-releases/2013_kaspersky-lab-uncovers--operation-nettraveler--a-global-cyberespionage-campaign-targeting-government-affiliated-organizations-and-research-institutes<br>https://www.proofpoint.com/us/threat-insight/post/nettraveler-apt-targets-russian-european-interests<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=NetTraveler%2C+APT+21%2C+Hammer+Panda&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT21 | canonical-name | 高 | CN, China | https://securelist.com/blog/research/35936/nettraveler-is-running-red-star-apt-attacks-compromise-high-profile-victims/<br>https://www.cfr.org/interactive/cyber-operations/nettraveler<br>https://www.kaspersky.com/about/press-releases/2013_kaspersky-lab-uncovers--operation-nettraveler--a-global-cyberespionage-campaign-targeting-government-affiliated-organizations-and-research-institutes |
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
| malware--nettraveler | NetTraveler | NetTravelerグループが監視、キーロギング、ファイル窃取、追加マルウェア導入に使用した同名ツールキット。 | 2005 | 2013-06-04 | 高 | `source--kaspersky-nettraveler-2013` |

### ツール

未確認

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| vulnerability--cve-2010-3333 | CVE-2010-3333 | Patched Microsoft Office vulnerability used in malicious spearphishing attachments during NetTraveler operations. | 不明 | 2013-06-04 | 高 | `source--kaspersky-nettraveler-2013` |
| vulnerability--cve-2012-0158 | CVE-2012-0158 | Patched Microsoft Office vulnerability used in malicious spearphishing attachments during NetTraveler operations. | 不明 | 2013-06-04 | 高 | `source--kaspersky-nettraveler-2013` |

### 運用能力

未確認

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NetTraveler／Red Starサイバースパイ活動 | cyber-espionage | 2004 | 2013-06-04 | 2013-06-04 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--48cc6b4cc2919459aec9, target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--67ce22b843f136bff928, target--activity-rule--country--6cb716c577f256f44a3e, target--activity-rule--country--72caf60a2fbce4a1be7a, target--activity-rule--country--7d3fb601fc3dd41e174c, target--activity-rule--country--95e363d6dfa8c6f2ecbb, target--activity-rule--country--9e0b33ddb91d0135fb82, target--activity-rule--country--de0df51cff4adf4fc20b, target--activity-rule--country--ee55e5e8faa5dd675d7b, target--activity-rule--country--f35cd09db0a72555b38a, target--activity-rule--country--f9601e2d842c9a05202b, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--activity-rule--sector--e7608f51421ca8b1e297, target--activity-rule--sector--fb803c0a91ed53ea76f9, target--targeting-audit--country--119b0634a77613d69330, target--targeting-audit--country--2a4fa45d08ef5cbd2526, target--targeting-audit--country--2bcfe28e9c86b109f2eb, target--targeting-audit--country--441ad68212c2f542f406, target--targeting-audit--country--586767a2ca703f81684f, target--targeting-audit--country--67c0a983b51ee71168ba, target--targeting-audit--country--6ff28da594055e910861, target--targeting-audit--country--82cdc5812d8be5b98ece, target--targeting-audit--country--85491d71f6e465ac98b1, target--targeting-audit--country--8ba6c97bcb6b50c67b54, target--targeting-audit--country--a1d0ef6a976950860a50, target--targeting-audit--country--a23a84e574f57f4fb6ba, target--targeting-audit--country--a69f351616a0377b76e1, target--targeting-audit--country--a78ddb709c3b4f3dfd57, target--targeting-audit--country--ca37dd5b4e620fa9747d, target--targeting-audit--country--cc0db63fa990598a10a0, target--targeting-audit--country--e7d17cbe5e04d0e39f52 | malware--nettraveler |  | victim--activity-rule--e11c669803fb114c1d2d | Kasperskyは、モンゴル、ロシア、インド、カザフスタン、キルギス、中国、タジキスタン、韓国、スペイン、ドイツ、米国、カナダ、英国、チリ、モロッコ、ギリシャ、ベルギー、オーストリア、ウクライナ、リトアニア、ベラルーシ、オーストラリア、香港、日本、イラン、トルコ、パキスタン、タイ、カタール、ヨルダンを含む40か国で侵害を確認した。標的は政府機関、大使館、石油・ガス、研究機関、大学、防衛・軍事請負企業、活動家等で、NetTravelerマルウェアを用いて機微情報を窃取した。 | 高 | `source--kaspersky-nettraveler-2013` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| NetTraveler／Red Starサイバースパイ活動 | NetTraveler | NetTraveler | 情報なし | 情報なし | ウクライナ, インド, 米国, パキスタン, 韓国, ロシア, オーストラリア, 中国, イラン, ドイツ, カナダ, 日本, 英国, 政府・行政, 防衛・軍事, 非営利・市民社会, 教育・研究, エネルギー, オーストリア, ヨルダン, カタール, スペイン, モンゴル, タジキスタン, チリ, ベルギー, カザフスタン, リトアニア, モロッコ, ベラルーシ, ギリシャ, トルコ, 香港, キルギス, タイ | 被害事例: NetTraveler／Red Starサイバースパイ活動 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イラン | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | インド | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | ウクライナ | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | オーストラリア | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | オーストリア | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | カザフスタン | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | カタール | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | カナダ | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | キルギス | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | ギリシャ | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | スペイン | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | タイ | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | タジキスタン | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | チリ | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | トルコ | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | ドイツ | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | パキスタン | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | ベラルーシ | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | ベルギー | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | モロッコ | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | モンゴル | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | ヨルダン | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | リトアニア | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | ロシア | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | 中国 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | 日本 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | 米国 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | 英国 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | 韓国 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された国・地域。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| countries | 香港 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的・被害国として明示されている。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| regions | 中央アジア | カザフスタン、キルギス、タジキスタンで確認された標的・被害事例を中央アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--kaspersky-nettraveler-2013` |
| regions | 中東 | イラン、カタール、トルコ、ヨルダンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--kaspersky-nettraveler-2013` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--kaspersky-nettraveler-2013` |
| regions | 南アジア | インド、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--kaspersky-nettraveler-2013` |
| regions | 南欧 | ギリシャ、スペインで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--kaspersky-nettraveler-2013` |
| regions | 東アジア | モンゴル、中国、日本、韓国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--kaspersky-nettraveler-2013` |
| regions | 東欧 | ウクライナ、ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--kaspersky-nettraveler-2013` |
| regions | 欧州 | ウクライナ、オーストリア、ギリシャ、スペイン、トルコ、ドイツ、ベラルーシ、ベルギー、リトアニア、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--kaspersky-nettraveler-2013` |
| sectors | 政府・行政 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された産業。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| sectors | 防衛・軍事 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された産業。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| sectors | 非営利・市民社会 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された産業。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| sectors | 教育・研究 | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された産業。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |
| sectors | エネルギー | 活動「NetTraveler／Red Starサイバースパイ活動」の記述で標的として明示された産業。 | 2004 | 2013-06-04 | 中 | `source--kaspersky-nettraveler-2013` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: NetTraveler／Red Starサイバースパイ活動 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--48cc6b4cc2919459aec9, target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--67ce22b843f136bff928, target--activity-rule--country--6cb716c577f256f44a3e, target--activity-rule--country--72caf60a2fbce4a1be7a, target--activity-rule--country--7d3fb601fc3dd41e174c, target--activity-rule--country--95e363d6dfa8c6f2ecbb, target--activity-rule--country--9e0b33ddb91d0135fb82, target--activity-rule--country--de0df51cff4adf4fc20b, target--activity-rule--country--ee55e5e8faa5dd675d7b, target--activity-rule--country--f35cd09db0a72555b38a, target--activity-rule--country--f9601e2d842c9a05202b, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--activity-rule--sector--e7608f51421ca8b1e297, target--activity-rule--sector--fb803c0a91ed53ea76f9 | malware--nettraveler |  |  | espionage: NetTraveler／Red Starサイバースパイ活動 | 2004 | 2013-06-04 | 2013-06-04 | 高 | `source--kaspersky-nettraveler-2013` |

## MITRE ATT&CK Matrixデータ

TTPなし

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
- 2 alias lead(s) remain non-canonical pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--nettraveler--268f9b2065c15023 | nettraveler |  | 不明 | actor_profile/evidence/nettraveler.csv | structured-data | TLP:CLEAR | 中 |
| source--nettraveler--84ba259d6bd02bdd | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--nettraveler--5b4f53329b725e3c | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--nettraveler--7ca4a4874860a4d5 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--kaspersky-nettraveler-2013 | NetTraveler is Running! - Red Star APT Attacks Compromise High-Profile Victims | Kaspersky Global Research and Analysis Team | 2013-06-04 | https://securelist.com/nettraveler-is-running-red-star-apt-attacks-compromise-high-profile-victims/35936/ | vendor-research | TLP:CLEAR | 高 |
| source--kaspersky-q2-2016-danti | IT threat evolution in Q2 2016. Overview | Kaspersky | 2016-08-11 | https://securelist.com/it-threat-evolution-in-q2-2016-overview/75615/ | vendor-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
