# TA558 脅威アクタープロファイル

- プロファイルID: `actor--ta558`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

TA558の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA558**
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
| etda-threat-group-cards | TA558 | canonical-name | 高 |  | https://www.proofpoint.com/us/blog/threat-insight/reservations-requested-ta558-targets-hospitality-and-travel<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=TA558&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA558 | canonical-name | 高 |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
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
| SteganoAmor攻撃が全世界の320の組織を標的に | malware-campaign | 不明 | 不明 | 2024-04-16 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--570d54d1d21fab6540a9 |  |  | victim--activity-rule--8806ce9d668d7aa5df22 | SteganoAmorは画像内に隠された悪意あるコードを利用 TA558グループによる攻撃。様々な分野や国に影響を与えた320以上の攻撃が行われた TA558は、2018年から活動しており、標的は主にラテンアメリカのホスピタリティ関連組織 Microsoft Officeの脆弱性CVE-2017-11882を悪用 様々なマルウェアが配布される、AgentTeslaやFormBookなど | 中 | `source--daily-09539f0db091b1cf7875` |
| TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開 | phishing-campaign | 不明 | 不明 | 2025-09-18 | target--activity-rule--sector--570d54d1d21fab6540a9 |  | ttp--activity-rule--72ed5e8ff59e9c3432cb | victim--activity-rule--61a6a8dfac5c5f1df7ae | 脅威グループTA558（KasperskyはRevengeHotelsとして追跡）が、ブラジルやスペイン語圏のホテルを狙いRATを配布。 2025年夏に観測。請求書や予約・採用通知を装うフィッシングで、ポルトガル語／スペイン語メールから感染を誘導。 LLM生成と推測されるコメント多めのJSローダーとPowerShellダウンローダーで最終的にVenom RATを展開。 Venom RATは窃取・リバースプロキシ・アンチキル・永続化を備え、特権化やDefender停止、USB経由拡散にも対応。 目的はホテルシステムやオンライン旅行代理店(OTA)（例: Booking[.]com）に保管された宿泊客のクレジットカード情報の窃取。 | 高 | `source--daily-f057489c6a517d53de51` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| SteganoAmor攻撃が全世界の320の組織を標的に | TA558 | 情報なし | 情報なし | 情報なし | 米国, 小売・ホスピタリティ | 被害事例: SteganoAmor攻撃が全世界の320の組織を標的に | 中 |
| TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開 | TA558 | 情報なし | T1090 Proxy | 情報なし | 小売・ホスピタリティ | 被害事例: TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アルジェリア | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてアルジェリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アルゼンチン | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてアルゼンチンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インド | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インドネシア | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウルグアイ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてウルグアイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エクアドル | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてエクアドルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | グアテマラ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてグアテマラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | コスタリカ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてコスタリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | コロンビア | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてコロンビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スペイン | 活動「TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-f057489c6a517d53de51`, `source--target-audit-etda-threat-group-cards` |
| countries | スロベニア | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてスロベニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | セルビア | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてセルビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チェコ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてチェコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チリ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてチリが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドミニカ共和国 | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてドミニカ共和国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 活動「TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-f057489c6a517d53de51`, `source--target-audit-etda-threat-group-cards` |
| countries | ブルガリア | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてブルガリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ペルー | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてペルーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポルトガル | 活動「TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-f057489c6a517d53de51` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | メキシコ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてメキシコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モロッコ | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてモロッコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ルーマニア | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてルーマニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | レバノン | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてレバノンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでTA558の標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 北マケドニア | 構造化OSINTの被害国フィールドでTA558の標的・被害国として北マケドニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 活動「SteganoAmor攻撃が全世界の320の組織を標的に」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-09539f0db091b1cf7875`, `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでTA558の標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | アフリカ | アルジェリア、モロッコで確認された標的・被害事例をアフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中南米 | アルゼンチン、ウルグアイ、エクアドル、グアテマラ、コスタリカ、コロンビア、チリ、ドミニカ共和国、ブラジル、ペルー、メキシコで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-f057489c6a517d53de51`, `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | トルコ、レバノンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 全世界 | 活動「SteganoAmor攻撃が全世界の320の組織を標的に」の記述で標的地域として全世界が明示されている。 | 不明 | 不明 | 中 | `source--daily-09539f0db091b1cf7875` |
| regions | 北アフリカ | アルジェリア、モロッコで確認された標的・被害事例を北アフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | メキシコ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-09539f0db091b1cf7875`, `source--target-audit-etda-threat-group-cards` |
| regions | 南アジア | インド、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南欧 | スペイン、スロベニア、セルビア、ポルトガル、北マケドニアで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-f057489c6a517d53de51`, `source--target-audit-etda-threat-group-cards` |
| regions | 南米 | アルゼンチン、ウルグアイ、エクアドル、コロンビア、チリ、ブラジル、ペルーで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-f057489c6a517d53de51`, `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | インドネシア、タイで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | チェコ、ブルガリア、ポーランド、ルーマニア、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | スペイン、スロベニア、セルビア、チェコ、トルコ、ドイツ、ブルガリア、ポルトガル、ポーランド、ルーマニア、北マケドニアで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-f057489c6a517d53de51`, `source--target-audit-etda-threat-group-cards` |
| sectors | 小売・ホスピタリティ | 活動「SteganoAmor攻撃が全世界の320の組織を標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-09539f0db091b1cf7875`, `source--daily-f057489c6a517d53de51` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--570d54d1d21fab6540a9 |  | ttp--activity-rule--72ed5e8ff59e9c3432cb | メール／メールアカウント, OT／ICS |  | 不明 | 不明 | 2025-09-18 | 高 | `source--daily-f057489c6a517d53de51` |
| 被害事例: SteganoAmor攻撃が全世界の320の組織を標的に | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--570d54d1d21fab6540a9 |  |  |  |  | 不明 | 不明 | 2024-04-16 | 中 | `source--daily-09539f0db091b1cf7875` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1090 | Proxy | Venom RATは窃取・リバースプロキシ・アンチキル・永続化を備え、特権化やDefender停止、USB経由拡散にも対応。 |  | activity--daily-9d2d6ad9320182983777 | 不明 | 不明 | 中 | `source--daily-f057489c6a517d53de51` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 5件（`artifacts.csv`）

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
| source--daily-09539f0db091b1cf7875 | SteganoAmor攻撃が全世界の320の組織を標的に | bleepingcomputer.com | 2024-04-16 | https://www.bleepingcomputer.com/news/security/new-steganoamor-attacks-use-steganography-to-target-320-orgs-globally/ | osint-report | TLP:CLEAR | 中 |
| source--daily-f057489c6a517d53de51 | TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開 | thehackernews.com | 2025-09-18 | https://thehackernews.com/2025/09/ta558-uses-ai-generated-scripts-to.html | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta558--4fa855b571aca4ba | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--ta558--748588cb3831785d | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--ta558--c50b7358c4f07d6d | ta558 |  | 不明 | actor_profile/evidence/ta558.csv | structured-data | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
