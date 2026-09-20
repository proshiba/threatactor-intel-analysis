# UNC4899 脅威アクタープロファイル

- プロファイルID: `actor--unc4899`
- 状態: draft
- 更新日時: 2026-09-20T07:40:51Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC4899の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC4899**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| TraderTraitor | SentinelOne | overlapping | 中 | `source--sentinelone-tradertraitor-terraform-2026` | SentinelOneは2026-09-18の報告で「the financially motivated DPRK state-sponsored Lazarus subgroup TraderTraitor (aka UNC4899, PUKCHONG, Jade Sleet)」と併記する。ベンダーによる呼称の対応付けであり、クラスタ境界の同一性を確定する記述ではないため scope は overlapping とした。 |
| PUKCHONG | SentinelOne | overlapping | 中 | `source--sentinelone-tradertraitor-terraform-2026` | 同上の併記による。命名元はRecorded Futureだが本走査では同社原典を未確認であり、SentinelOne経由の対応付けにとどまる。 |
| Jade Sleet | SentinelOne | overlapping | 中 | `source--sentinelone-tradertraitor-terraform-2026` | 同上の併記による。命名元はMicrosoftだが本走査では同社原典を未確認であり、SentinelOne経由の対応付けにとどまる。 |

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
| Lazarus Group | part-of | SentinelOneは2026-09-18の報告で当該アクターを「the financially motivated DPRK state-sponsored Lazarus subgroup TraderTraitor」と記述し、Lazarus Groupの下位グループと位置付ける。 | 中 | `source--sentinelone-tradertraitor-terraform-2026` |

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
- 調査日時: 2026-09-19T01:10:23Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Lazarus Group, Hidden Cobra, Labyrinth Chollima | canonical-name | 高 | North Korea | https://blog.malwarebytes.com/threat-analysis/2019/03/the-advanced-persistent-threat-files-lazarus-group/<br>https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/a-look-into-the-lazarus-groups-operations<br>https://www.kaspersky.com/about/press-releases/2017_chasing-lazarus-a-hunt-for-the-infamous-hackers-to-prevent-large-bank-robberies |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TraderTraitor | canonical-name | 高 | KP | https://www.mandiant.com/resources/blog/north-korea-supply-chain<br>https://us-cert.cisa.gov/ncas/alerts/aa22-108a<br>https://www.mandiant.com/resources/blog/north-korea-cyber-structure-alignment-2023 |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Lazarus Group | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--flatroof | FLATROOF | macOS向けバックドア。LayerZero侵害で最初に観測され、2026年3月のITサービス事業者の侵害でも同一検体が確認された。被害端末では ~/Library/com.apple.iTunesCloud/SystemUpdate として配置され、technicais.sytes[.]net をC2とする。 | 2026-03-18 | 2026-06-17 | 中 | `source--sentinelone-tradertraitor-terraform-2026` |
| malware--roofdeck | ROOFDECK | macOS向けバックドア。コマンドは運用者の秘密鍵で署名され、埋め込み公開鍵で完全性を検証してから実行される。ディレクトリ・ファイル操作に関する一般的なシェルコマンドを自前で再実装する。被害端末では ~/Library/com.apple.internal.ck/iSync として配置され、storage.hubpage[.]cloud および grenight[.]com をC2とする。 | 2026-03-18 | 2026-06-17 | 中 | `source--sentinelone-tradertraitor-terraform-2026` |

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
| 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | phishing-campaign | 不明 | 不明 | 2024-06-15 |  |  |  |  | 北朝鮮のハッカーが、ブラジルのフィンテック企業を標的に洗練されたフィッシング攻撃を実行。 UNC4899（Jade Sleet）がPythonアプリをトロイの木馬化し、SNSで標的に接触し、GitHubプロジェクトを通じてマルウェアを配布。 有名な暗号通貨企業を装う求人でフィッシング。無害なPDFが添付されている。ターゲットが求人に反応したら追加のPDFを送る。 PDFで、スキルに関するアンケートと、GitHubからプロジェクトをダウンロードして、コーディング課題を完了するように要求。このプロジェクトにマルウェアが仕込まれている。 他の北朝鮮グループも同様の手法を使用し、フィッシングメールで悪意のあるソフトウェアを配信。 | 中 | `source--daily-eba291a90b11ea99ea6e` |
| 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | infrastructure-operation | 不明 | 不明 | 2025-04-16 | target--activity-rule--sector--932f4928d5e1ec28e2df |  | ttp--activity-rule--5287d9830bb2ca5ae994 | victim--activity-rule--a255592b2e5fc1bdeb05 | 北朝鮮と関連があるとされるハッカーグループ「Slow Pisces」（別名：Jade Sleet、PUKCHONG、TraderTraitor、UNC4899）は、暗号通貨開発者を標的にしたマルウェアキャンペーンを実施。 LinkedInを通じて開発者に接触し、偽の求人情報やコーディング課題を装ってマルウェアを配布。 被害者は、GitHub上のトロイの木馬化されたPythonプロジェクトをダウンロード・実行するよう誘導され、これにより「RN Loader」および「RN Stealer」と呼ばれるマルウェアに感染。 「RN Stealer」はmacOSシステム上で機密情報（iCloudキーチェーン、SSHキー、AWS/Kubernetes/Google Cloudの設定ファイルなど）を収集。 攻撃は多段階で行われ、C2サーバーは被害者のIPアドレスや地理情報などに基づいてペイロードの配信を制御。 コード実行には、`yaml.load()`や`ejs.render()`などの手法を用いて検出を回避。 | 中 | `source--daily-744b9664f686bf2ed5cd` |
| 偽の求人コーディング課題と悪性Terraform lockファイルによるmacOSバックドア展開 | intrusion | 2026-03-18 | 2026-06-17 | 2026-09-18 | target--activity-rule--sector--63c9fa67327d005b07b7 | malware--flatroof, malware--roofdeck |  | victim--activity-rule--ec91e5726221209970c4, victim--unc4899-it-services-india-2026 | SentinelOneは2026年4月に公表されたLayerZero侵害(KelpDAOから2億9,200万米ドル相当の暗号資産が窃取された事案)で最初に観測されたmacOSバックドア FLATROOF(別名 macOS.Gaslight)と ROOFDECK を手掛かりに自社テレメトリを探索し、暗号資産と無関係な追加の被害組織を特定した。被害者はインドに所在するITサービス事業者で、侵害を受けた端末1台はDevOps担当者が日常利用する開発端末であり、クラウド資格情報とソースコード管理へのアクセスを保持していた。初期侵入は偽の求人面接を装った社会工学であり、攻撃者は標的企業の求職者へ接触し、インフラ関連のコーディング課題を装った GitHub リポジトリ(Northwind-IAC、novacart-interview、terraform-candidate-repo など)を実行させる。リポジトリには攻撃者が管理するTerraform provider レジストリ(registry.hashicorp-aws[.]com、registry.hashicorp-aws[.]io、registry.hashicorp-terraform[.]io)を指す悪性の .terraform.lock.hcl が含まれ、terraform init の実行でマルウェアが取得される。両バックドアは2026-03-18から端末上に存在し、3月29日に開発者がCursorでワークスペースを開いた際にビーコンが開始した。その後2026-06-01までgrenight[.]comへの断続的なビーコンが観測され、6月17日にloginwindowバイナリがゴミ箱へ移動された。SentinelOneは本被害組織について、最終的に侵入を維持するだけの価値が得られなかったと評価している。 | 中 | `source--sentinelone-tradertraitor-terraform-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | UNC4899 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | UNC4899 | 情報なし | T1083 File and Directory Discovery | 情報なし | IT・ソフトウェア | 被害事例: 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | 中 |
| 偽の求人コーディング課題と悪性Terraform lockファイルによるmacOSバックドア展開 | UNC4899 | FLATROOF, ROOFDECK | 情報なし | 情報なし | 暗号資産・Web3 | 被害事例: 偽の求人コーディング課題と悪性Terraform lockファイルによるmacOSバックドア展開, 被害事例: インドのITサービス事業者に対するmacOSバックドア侵入 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イスラエル | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インド | 活動「偽の求人コーディング課題と悪性Terraform lockファイルによるmacOSバックドア展開」の記述で標的・被害国として明示されている。 | 2026-03-18 | 2026-06-17 | 中 | `source--sentinelone-tradertraitor-terraform-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | エクアドル | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてエクアドルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | グアテマラ | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてグアテマラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チリ | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてチリが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | バングラデシュ | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてバングラデシュが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 活動「北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-eba291a90b11ea99ea6e`, `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | メキシコ | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてメキシコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 南アフリカ | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国として南アフリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 日本 | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 香港 | 構造化OSINTの被害国フィールドでUNC4899の標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中南米 | エクアドル、グアテマラ、チリ、ブラジル、メキシコで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-eba291a90b11ea99ea6e`, `source--target-audit-etda-threat-group-cards` |
| regions | 全世界 | 構造化OSINTの被害地域フィールドでUNC4899の標的範囲として全世界が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、メキシコ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南アジア | インド、バングラデシュで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--sentinelone-tradertraitor-terraform-2026`, `source--target-audit-etda-threat-group-cards` |
| regions | 南米 | エクアドル、チリ、ブラジルで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-eba291a90b11ea99ea6e`, `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | 中国、北朝鮮、台湾、日本、韓国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-744b9664f686bf2ed5cd`, `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | タイ、フィリピン、ベトナムで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ポーランド、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | オランダ、ドイツ、フランス、ベルギー、ポーランド、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | 暗号資産・Web3 | 活動「偽の求人コーディング課題と悪性Terraform lockファイルによるmacOSバックドア展開」の記述で標的として明示された産業。 | 2026-03-18 | 2026-06-17 | 中 | `source--sentinelone-tradertraitor-terraform-2026` |
| sectors | IT・ソフトウェア | 活動「北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-744b9664f686bf2ed5cd` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--932f4928d5e1ec28e2df |  | ttp--activity-rule--5287d9830bb2ca5ae994 | サーバー, クラウド／SaaS, 開発環境／ソースコード |  | 不明 | 不明 | 2025-04-16 | 中 | `source--daily-744b9664f686bf2ed5cd` |
| 被害事例: 偽の求人コーディング課題と悪性Terraform lockファイルによるmacOSバックドア展開 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--63c9fa67327d005b07b7 | malware--flatroof, malware--roofdeck |  | エンドポイント, クラウド／SaaS, 開発環境／ソースコード |  | 2026-03-18 | 2026-06-17 | 2026-09-18 | 中 | `source--sentinelone-tradertraitor-terraform-2026` |
| 被害事例: インドのITサービス事業者に対するmacOSバックドア侵入 | 非公開 | anonymous | organization | confirmed |  | malware--flatroof, malware--roofdeck |  | 開発環境／ソースコード, クラウド／SaaS |  | 2026-03-18 | 2026-06-17 | 2026-09-18 | 中 | `source--sentinelone-tradertraitor-terraform-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1083 | File and Directory Discovery | 「RN Stealer」はmacOSシステム上で機密情報（iCloudキーチェーン、SSHキー、AWS/Kubernetes/Google Cloudの設定ファイルなど）を収集。 |  | activity--daily-db38d43f17473660e294 | 不明 | 不明 | 中 | `source--daily-744b9664f686bf2ed5cd` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 17件（`artifacts.csv`）

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
| source--daily-744b9664f686bf2ed5cd | 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | thehackernews.com | 2025-04-16 | https://thehackernews.com/2025/04/crypto-developers-targeted-by-python.html | osint-report | TLP:CLEAR | 中 |
| source--daily-eba291a90b11ea99ea6e | 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | thehackernews.com | 2024-06-15 | https://thehackernews.com/2024/06/north-korean-hackers-target-brazilian.html | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc4899--028ff7267b0d9392 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--0ff0d325de512842 | 2024 Blockchain Security and AML Annual Report(EN) |  | 2024 | summary/2025/2024-Blockchain-Security-and-AML-Annual-Report(EN).pdf | report | TLP:CLEAR | 中 |
| source--unc4899--1390332551d8c3af | advances in threat actor usage of ai tools en |  | 不明 | AISecurity/2025/advances-in-threat-actor-usage-of-ai-tools-en.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--2246c521b1b228d1 | unc4899 |  | 不明 | actor_profile/evidence/unc4899.csv | structured-data | TLP:CLEAR | 中 |
| source--unc4899--3e59f7f25cb2d69e | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--49cddfde804b2b45 | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--79cdef4e25eb8cd8 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--b5b8dda7301c9303 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--d91b559d4a2e0f1b | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--e1520dd17d1e4dfd | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--sentinelone-tradertraitor-terraform-2026 | Don't Call Us, We'll Call Your APIs \| TraderTraitor Backdoors Resurface on Victim With No Crypto Ties | SentinelLabs (SentinelOne) | 2026-09-18 | https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/ | vendor-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
