# UNC2970 脅威アクタープロファイル

- プロファイルID: `actor--unc2970`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC2970の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC2970**
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
| etda-threat-group-cards | Lazarus Group, Hidden Cobra, Labyrinth Chollima | canonical-name | 高 | North Korea | https://blog.malwarebytes.com/threat-analysis/2019/03/the-advanced-persistent-threat-files-lazarus-group/<br>https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/a-look-into-the-lazarus-groups-operations<br>https://www.kaspersky.com/about/press-releases/2017_chasing-lazarus-a-hunt-for-the-infamous-hackers-to-prevent-large-bank-robberies |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UNC2970 | canonical-name | 高 | KP | https://www.mandiant.com/resources/blog/lightshow-north-korea-unc2970 |
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
| 北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に | phishing-campaign | 不明 | 不明 | 2024-09-19 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--de0df51cff4adf4fc20b, target--activity-rule--country--f9601e2d842c9a05202b, target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--fb803c0a91ed53ea76f9 |  | ttp--activity-rule--9284011f4cc7699e8394 | victim--activity-rule--b694936d36ac7cdf3979 | UNC2970と呼ばれる北朝鮮のグループがエネルギーと航空宇宙企業を標的にスピアフィッシングを実施。 新たなMISTPENマルウェアを使用し、感染を広げた。 この攻撃は「Operation Dream Job」としても知られており、標的となる人物のプロフィールに合わせて修正された求人情報を装った悪意のあるZIPアーカイブファイルを送りつけるもの。 正規のPDFリーダーアプリケーションであるSumatra PDFのトロイの木馬化されたバージョンが含まれており、BURNBOOKと呼ばれるランチャーによってMISTPENが配信。 攻撃は米国、英国、ドイツなどの国で確認されている。 C2通信にMicrosoft Graphを利用。 | 中 | `source--daily-820c8bb063e8728fd388` |
| Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | phishing-campaign | 不明 | 不明 | 2026-02-13 | target--activity-rule--country--72caf60a2fbce4a1be7a |  |  | victim--activity-rule--2614e7c2a95f18b40fb4 | Google Threat Intelligence Group（GTIG）は、国家支援型ハッカーがGeminiを攻撃の全段階で悪用していると述べた。 中国（APT31/Temp.HEX）、イラン（APT42）、北朝鮮（UNC2970）、ロシアの活動が、標的調査やOSINTに使われた。 Geminiはプロファイリング、フィッシング文面生成、翻訳、コーディング、脆弱性テスト、C2開発、データ持ち出しの補助に使われた。 既存マルウェアへの機能追加にも悪用が見られ、CoinBaitやHonestCueでAI生成の痕跡が示された（PoCではGemini APIでC#生成）。 Googleは悪用に紐づくアカウント/インフラを無効化し、Gemini分類器の防御強化と安全対策（ガードレール）を継続的に検証している。 | 中 | `source--daily-2cce580b31452f445118` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に | UNC2970 | 情報なし | T1560.001 Archive via Utility | 情報なし | 米国, ドイツ, 英国, 運輸・航空・海運, 防衛・軍事, 製造・産業, エネルギー | 被害事例: 北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に | 中 |
| Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | UNC2970 | 情報なし | 情報なし | 情報なし | ロシア | 被害事例: Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イスラエル | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インド | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エクアドル | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてエクアドルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | グアテマラ | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてグアテマラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チリ | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてチリが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 活動「北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388`, `source--target-audit-etda-threat-group-cards` |
| countries | バングラデシュ | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてバングラデシュが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | メキシコ | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国としてメキシコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 活動「Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-2cce580b31452f445118`, `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 南アフリカ | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国として南アフリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 日本 | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 活動「北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388`, `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 活動「北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388`, `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 香港 | 構造化OSINTの被害国フィールドでUNC2970の標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中南米 | エクアドル、グアテマラ、チリ、ブラジル、メキシコで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 全世界 | 構造化OSINTの被害地域フィールドでUNC2970の標的範囲として全世界が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、メキシコ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388`, `source--target-audit-etda-threat-group-cards` |
| regions | 南アジア | インド、バングラデシュで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南米 | エクアドル、チリ、ブラジルで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | 中国、台湾、日本、韓国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | タイ、フィリピン、ベトナムで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ポーランド、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-2cce580b31452f445118`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | オランダ、ドイツ、フランス、ベルギー、ポーランド、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388`, `source--target-audit-etda-threat-group-cards` |
| sectors | 運輸・航空・海運 | 活動「北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388` |
| sectors | 防衛・軍事 | 活動「北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388` |
| sectors | 製造・産業 | 活動「北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388` |
| sectors | エネルギー | 活動「北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--72caf60a2fbce4a1be7a |  |  |  | data-theft: Geminiはプロファイリング、フィッシング文面生成、翻訳、コーディング、脆弱性テスト、C2開発、データ持ち出しの補助に使われた。 | 不明 | 不明 | 2026-02-13 | 中 | `source--daily-2cce580b31452f445118` |
| 被害事例: 北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--de0df51cff4adf4fc20b, target--activity-rule--country--f9601e2d842c9a05202b, target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--fb803c0a91ed53ea76f9 |  | ttp--activity-rule--9284011f4cc7699e8394 |  |  | 不明 | 不明 | 2024-09-19 | 中 | `source--daily-820c8bb063e8728fd388` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1560.001 | Archive via Utility | この攻撃は「Operation Dream Job」としても知られており、標的となる人物のプロフィールに合わせて修正された求人情報を装った悪意のあるZIPアーカイブファイルを送りつけるもの。 |  | activity--daily-2f0f09b67d0594d4f548 | 不明 | 不明 | 中 | `source--daily-820c8bb063e8728fd388` |

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
| source--daily-2cce580b31452f445118 | Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | bleepingcomputer.com | 2026-02-13 | https://www.bleepingcomputer.com/news/security/google-says-hackers-are-abusing-gemini-ai-for-all-attacks-stages/ | osint-report | TLP:CLEAR | 中 |
| source--daily-820c8bb063e8728fd388 | 北朝鮮のハッカー、エネルギーおよび航空宇宙産業を新たなMISTPENマルウェアで標的に | thehackernews.com | 2024-09-19 | https://thehackernews.com/2024/09/north-korean-hackers-target-energy-and.html | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc2970--36273ba018b91373 | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--unc2970--80013422ca71c1b1 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--unc2970--93dba0b4b3b578aa | unc2970 |  | 不明 | actor_profile/evidence/unc2970.csv | structured-data | TLP:CLEAR | 中 |
| source--unc2970--a7d42cd6f9de24e8 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--unc2970--b1174d542af4c564 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--unc2970--d6da360d6fdbce01 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
