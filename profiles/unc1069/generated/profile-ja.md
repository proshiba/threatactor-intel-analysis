# UNC1069 脅威アクタープロファイル

- プロファイルID: `actor--unc1069`
- 状態: draft
- 更新日時: 2026-07-27T11:04:37Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

UNC1069の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC1069**
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
| microsoft-threat-actor-mapping | Sapphire Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | UNC1069 | canonical-name | 高 | KP | https://www.mandiant.com/resources/blog/north-korea-cyber-structure-alignment-2023<br>https://www.spixnet.com/cybersecurity-blog/2023/04/03/newly-exposed-apt43-hacking-group-targeting-us-orgs-since-2018/<br>https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools/ |
| misp-microsoft-activity-group | Sapphire Sleet | canonical-name | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| 北朝鮮系脅威アクターが、サプライチェーン攻撃で広く使われるAxios NPMパッケージを侵害 | infrastructure-operation | 不明 | 不明 | 2026-04-02 | Google Threat Intelligence Groupは2026年3月31日、axiosの保守者アカウント侵害により、悪性依存関係`plain-crypto-js`が1.14.1と0.30.4へ混入したサプライチェーン攻撃を確認した。 インストール時に`postinstall`で`setup.js`が密かに実行され、Windows、macOS、Linux向けにWAVESHAPER.V2バックドアを展開する仕組みだと説明している。 攻撃では保守者メールが攻撃者管理アカウントへ変更され、難読化ドロッパーはC2と通信しつつ、自削除や`package.json`復元で痕跡隠しも試みる。 GTIGはWAVESHAPER.V2やインフラの一致から、2018年以降活動する金銭目的の北朝鮮系脅威アクターUNC1069による活動と評価している。 防御策として、危険版への更新回避、安全版への固定、`plain-crypto-js`の監査、影響ホスト隔離、資格情報ローテーション、C2遮断を勧告している。 | 中 | `source--daily-4105305f46ca812b4f99` |
| OpenAI、Axios攻撃がコード署名ワークフローに及んだためmacOS証明書をローテーション | intrusion | 不明 | 不明 | 2026-04-14 | OpenAI は、2026年3月31日に GitHub Actions ワークフローが改ざん版 Axios 1.14.1 を実行したことを受け、macOS 用コード署名証明書のローテーションを開始した。 当該ワークフローは ChatGPT Desktop、Codex、Codex CLI、Atlas などの macOS アプリ署名用証明書へアクセスできたため、同社は証明書流出の証拠がなくても予防的に失効対応を進めている。 OpenAI は外部調査会社と調査を行い、証明書露出や悪性ソフト署名への悪用、ユーザーデータ侵害、知的財産侵害、ソフト改ざんの証拠は見つからなかったとしている。 ただし旧証明書が攻撃者に渡っていれば、OpenAI 正規署名に見える macOS アプリを作られる恐れがあるため、Apple と連携して旧証明書での今後の notarization を防ぐとしている。 影響は macOS アプリに限定され、Web、iOS、Android、Windows、Linux、ならびにユーザーアカウント、パスワード、API キーには影響せず、旧版は2026年5月8日以降に動作停止し得る。 | 中 | `source--daily-cad9400150d21f1c1004` |
| 北朝鮮ハッカー、新しいmacOSマルウェアで暗号資産窃取攻撃 | infrastructure-operation | 不明 | 不明 | 2026-02-11 | 北朝鮮系ハッカーが、AI生成動画とClickFix手口で暗号資産業界を狙い、macOS/Windowsへマルウェアを配布。 被害者はTelegramで暗号資産企業幹部の乗っ取られたアカウントから接触され、Calendly経由で偽Zoom会議へ誘導。 深層偽造（ディープフェイク）映像と「音声不具合」詐称で、Webページ上のコマンド実行を促し感染チェーンを開始。 AppleScript実行の痕跡後にMach-Oを展開し、WAVESHAPER等7種のmacOSマルウェアでC2通信や追加ペイロード実行を実施。 DEEPBREATHはTCC回避でKeychain等を窃取し、目的は暗号資産窃取と被害者情報を使った将来の詐欺/誘導の強化とされる。 | 中 | `source--daily-16dc3c27175f6cbffe47` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 14件（`artifacts.csv`）

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
| source--daily-16dc3c27175f6cbffe47 | 北朝鮮ハッカー、新しいmacOSマルウェアで暗号資産窃取攻撃 | bleepingcomputer.com | 2026-02-11 | https://www.bleepingcomputer.com/news/security/north-korean-hackers-use-new-macos-malware-in-crypto-theft-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4105305f46ca812b4f99 | 北朝鮮系脅威アクターが、サプライチェーン攻撃で広く使われるAxios NPMパッケージを侵害 | cloud.google.com | 2026-04-02 | https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package?hl=en | osint-report | TLP:CLEAR | 中 |
| source--daily-cad9400150d21f1c1004 | OpenAI、Axios攻撃がコード署名ワークフローに及んだためmacOS証明書をローテーション | bleepingcomputer.com | 2026-04-14 | https://www.bleepingcomputer.com/news/security/openai-rotates-macos-certs-after-axios-attack-hit-code-signing-workflow/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc1069--0d8521c75c02d612 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--unc1069--35553542d95bc7d4 | APT43 Report |  | 不明 | APT43/APT43 Report.pdf | report | TLP:CLEAR | 中 |
| source--unc1069--3efeebd6ff3109ca | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc1069--618b6f01896a6355 | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--unc1069--82ddbf136068121c | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--unc1069--84dd08998dd65094 | advances in threat actor usage of ai tools en |  | 不明 | AISecurity/2025/advances-in-threat-actor-usage-of-ai-tools-en.pdf | report | TLP:CLEAR | 中 |
| source--unc1069--a8ecf781c48045b5 | eset apt activity report q4 2025 q1 2026 |  | 2025 | summary/2026/eset-apt-activity-report-q4-2025-q1-2026.pdf | report | TLP:CLEAR | 中 |
| source--unc1069--e5ffd49d89d7dcfd | unc1069 |  | 不明 | actor_profile/evidence/unc1069.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
