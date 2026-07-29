# Cellebrite 脅威アクタープロファイル

- プロファイルID: `actor--cellebrite`
- 状態: draft
- 更新日時: 2026-07-29T15:36:10Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Cellebriteの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Cellebrite**
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

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| commercial | Commercial offensive-security or surveillance operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

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

- 判定: `no-match`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
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
| Google、攻撃で悪用されたAndroidゼロデイを含む60以上の脆弱性を修正 | reported-activity | 不明 | 不明 | 2025-04-08 |  |  |  |  | Googleは2025年4月のAndroidセキュリティアップデートで62件の脆弱性を修正。 修正された中には、攻撃で悪用された2件のゼロデイ脆弱性が含まれる。 1つ目はLinuxカーネルのUSBオーディオドライバにおける高リスクの特権昇格脆弱性（CVE-2024-53197）。 2つ目はAndroidカーネルの情報漏洩脆弱性（CVE-2024-53150）。 CVE-2024-53197は、イスラエルのデジタルフォレンジック企業Cellebriteが開発したゼロデイエクスプロイトチェーンの一部として、セルビア当局が押収したAndroidデバイスのロック解除に悪用された。 | 中 | `source--daily-a2ace93812b6d990cbcf` |
| セルビア警察、Cellebriteのゼロデイ攻撃を使用してAndroid携帯をアンロック | cyber-espionage | 不明 | 不明 | 2025-03-01 | target--activity-rule--sector--d406c8e5b7fa7aeff7d2 |  |  | victim--activity-rule--8c900bbe6c6c673f6f72 | セルビア当局が、イスラエルのデジタルフォレンジック企業Cellebriteが開発したAndroidのゼロデイ攻撃を使用し、学生活動家のデバイスをアンロックし、スパイウェアのインストールを試みたと報告。 2024年半ば、Amnesty Internationalのセキュリティラボが影響を受けたデバイスのログをフォレンジック調査中に、この攻撃の使用を発見。 GoogleのThreat Analysis Group（TAG）は、Amnestyからの情報を受け取り、LinuxカーネルのUSBドライバにある3つのゼロデイ脆弱性を特定。 これらの脆弱性は、CVE-2024-53104（USBビデオクラスの脆弱性）などで、Androidデバイスのセキュリティを危険にさらす可能性がある。 CVE-2024-53104 (USBビデオクラスのエクスプロイト) CVE-2024-53197 (ALSA USBサウンドドライバのエクスプロイト) | 高 | `source--daily-beb73f1716914fd50808` |
| Google、標的型攻撃で悪用されたAndroidゼロデイ脆弱性を修正 | reported-activity | 不明 | 不明 | 2025-03-05 |  |  |  |  | Googleは2025年3月のAndroidセキュリティアップデートで、43件の脆弱性を修正し、その中には標的型攻撃で悪用された2つのゼロデイ脆弱性が含まれています。 1つ目のゼロデイ脆弱性（CVE-2024-50302）は、Linuxカーネルのヒューマンインターフェースデバイスドライバーにおける高深刻度の情報漏洩の脆弱性で、イスラエルのデジタルフォレンジック企業Cellebriteが開発したエクスプロイトチェーンの一部として、押収されたデバイスのロック解除に使用されました。 2つ目のゼロデイ脆弱性（CVE-2024-43093）は、Androidフレームワークの特権昇格の脆弱性で、ローカルの攻撃者が不正なUnicode正規化を悪用して、機密ディレクトリにアクセスできます。 Googleはこれらの脆弱性に関する修正を1月にOEMパートナーと共有し、3月のセキュリティアップデートで一般ユーザー向けに提供しました。 | 中 | `source--daily-5968af3fdd75f2b8e823` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 非営利・市民社会 | 活動「セルビア警察、Cellebriteのゼロデイ攻撃を使用してAndroid携帯をアンロック」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-beb73f1716914fd50808` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: セルビア警察、Cellebriteのゼロデイ攻撃を使用してAndroid携帯をアンロック | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--d406c8e5b7fa7aeff7d2 |  |  | モバイル端末 |  | 不明 | 不明 | 2025-03-01 | 高 | `source--daily-beb73f1716914fd50808` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 119件
- IOC観測: 134件
- 複数攻撃で観測: 0件
- 要レビュー候補: 77件
- 非IOC artifact観測: 24件（`artifacts.csv`）

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
| source--cellebrite--90a6ad972f6fa9a4 | Amnesty Cellebrite |  | 不明 | Cellebrite/Amnesty-Cellebrite.pdf | report | TLP:CLEAR | 中 |
| source--cellebrite--d3efba9fe5ded235 | readme |  | 不明 | Cellebrite/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--daily-5968af3fdd75f2b8e823 | Google、標的型攻撃で悪用されたAndroidゼロデイ脆弱性を修正 | bleepingcomputer.com | 2025-03-05 | https://www.bleepingcomputer.com/news/security/google-fixes-android-zero-days-exploited-in-targeted-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-a2ace93812b6d990cbcf | Google、攻撃で悪用されたAndroidゼロデイを含む60以上の脆弱性を修正 | bleepingcomputer.com | 2025-04-08 | https://www.bleepingcomputer.com/news/security/google-fixes-android-zero-days-exploited-in-attacks-60-other-flaws/ | osint-report | TLP:CLEAR | 中 |
| source--daily-beb73f1716914fd50808 | セルビア警察、Cellebriteのゼロデイ攻撃を使用してAndroid携帯をアンロック | bleepingcomputer.com | 2025-03-01 | https://www.bleepingcomputer.com/news/security/serbian-police-used-cellebrite-zero-day-hack-to-unlock-android-phones/ | osint-report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
