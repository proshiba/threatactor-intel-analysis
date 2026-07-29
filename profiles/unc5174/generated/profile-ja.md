# UNC5174 脅威アクタープロファイル

- プロファイルID: `actor--unc5174`
- 状態: draft
- 更新日時: 2026-07-29T15:36:12Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC5174の標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC5174**
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
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UNC5174 | canonical-name | 高 |  | https://rhisac.org/threat-intelligence/f5-big-ip-and-screenconnect-cves/<br>https://www.mandiant.com/resources/blog/initial-access-brokers-exploit-f5-screenconnect |
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
| 中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用 | infrastructure-operation | 不明 | 不明 | 2025-04-16 | target--activity-rule--country--f35cd09db0a72555b38a, target--activity-rule--sector--210dddb39397dbe50e91 |  |  | victim--activity-rule--caea1296908bb424f92e | 中国系APTグループUNC5174がLinux向けにSNOWLIGHTマルウェアとVShellを展開 SNOWLIGHTはCベースのELF型ドロッパーで、メモリ上にVShell RATを展開 VShellはWebSocketを用いたC2通信が可能なファイルレス型RAT 攻撃には脆弱性（例：CVE-2024-8963など）を悪用して初期侵入 標的国は日本を含む20カ国以上に及び、政府・重要インフラが主な標的 | 中 | `source--daily-c5a9c42da8ab9e7b0010` |
| ランサムウェア集団、SAP NetWeaver攻撃に参入 | ransomware-extortion | 不明 | 不明 | 2025-05-15 |  |  |  | victim--activity-rule--b0587ebaf67a29526988 | SAP NetWeaverの重大な脆弱性（CVE-2025-31324）を悪用した攻撃に、RansomEXXおよびBianLianランサムウェア集団が参入。 この脆弱性は、認証なしでのファイルアップロードを可能にし、リモートコード実行を許す。 ReliaQuestの分析により、BianLianが過去に使用したC2サーバーのIPアドレスとの関連が確認された。 RansomEXXは、PipeMagicバックドアやBrute Ratel C2フレームワークを利用し、攻撃を展開。 中国のAPTグループ（Chaya_004、UNC5221、UNC5174、CL-STA-0048）も同脆弱性を悪用し、少なくとも581のSAP NetWeaverインスタンスにバックドアを設置。 | 中 | `source--daily-c8f19538293e168bddbd` |
| React2Shellの欠陥が30組織の侵害に悪用、7.7万のIPアドレスが脆弱 | intrusion | 不明 | 不明 | 2025-12-08 |  |  |  | victim--activity-rule--8d6a477bac79692c0bf5 | React2Shell（CVE-2025-55182）が公表直後から悪用され、既に30超の組織侵害と7万7,664の脆弱IPが確認。 RSCの安全でないデシリアライズが原因で、Next.js等の実装に影響し、単一HTTP要求で未認証RCEが可能。 PoC公開後にスキャンが急増し、GreyNoiseは直近24時間で181の発信元を観測、複数国からの自動化攻撃が目立つ。 侵害では偵察やAWS資格情報窃取試行、23[.]235[.]188[.]3から第2段階PS取得、Cobalt Strike設置が報告。 CISAはKEVに追加し、即時の更新・再ビルド/再デプロイとPS/シェル実行痕跡のログ確認を助言。 | 中 | `source--daily-f47a43f682d4bb61a2bc` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 日本 | 活動「中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-c5a9c42da8ab9e7b0010` |
| sectors | 政府・行政 | 活動「中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-c5a9c42da8ab9e7b0010` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: React2Shellの欠陥が30組織の侵害に悪用、7.7万のIPアドレスが脆弱 | 非公開 | aggregate | multiple-organizations | reported |  |  |  | クラウド／SaaS |  | 不明 | 不明 | 2025-12-08 | 中 | `source--daily-f47a43f682d4bb61a2bc` |
| 被害事例: ランサムウェア集団、SAP NetWeaver攻撃に参入 | 非公開 | anonymous | unknown | reported |  |  |  |  | encryption: ランサムウェア集団、SAP NetWeaver攻撃に参入 | 不明 | 不明 | 2025-05-15 | 中 | `source--daily-c8f19538293e168bddbd` |
| 被害事例: 中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--f35cd09db0a72555b38a, target--activity-rule--sector--210dddb39397dbe50e91 |  |  |  |  | 不明 | 不明 | 2025-04-16 | 中 | `source--daily-c5a9c42da8ab9e7b0010` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1105 | Ingress Tool Transfer | e_severity Low, confidence Low, tag VShell, tag RAT, updated_at 2025_08_26, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1105, mitre_technique_name Ingress_Tool_Transfer;) alert tcp $HOME_NET any -> $EXTERNAL_NET any (msg:"[NVISO] Potential VShell beacon payload request (Windows i386)"; flow:to_server,established; content:"w32 "; fast_pattern; offset:0; depth:6; stream_size:client,<=,45; flowb |  |  | 不明 | 不明 | 中 | `source--unc5174--626245061e5734b4` |
| Command And Control | T1573 | Encrypted Channel | ty Critical, confidence Medium, tag VShell, tag RAT, updated_at 2025_08_26, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1573, mitre_technique_name Encrypted_Channel;) alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"[NVISO] VShell beacon server handshake"; flow:to_client,established; content:"\|3c 00 00 00\|"; fast_pattern; offset:0; depth:4; byte_test:1,&,0x80,0x4; content:"\|20 00 00 00\|"; offse |  |  | 不明 | 不明 | 中 | `source--unc5174--626245061e5734b4` |

## IOC／artifact概要

- IOC値: 52件
- IOC観測: 79件
- 複数攻撃で観測: 0件
- 要レビュー候補: 4件
- 非IOC artifact観測: 8件（`artifacts.csv`）

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
| source--daily-c5a9c42da8ab9e7b0010 | 中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用 | thehackernews.com | 2025-04-16 | https://thehackernews.com/2025/04/chinese-hackers-target-linux-systems.html | osint-report | TLP:CLEAR | 中 |
| source--daily-c8f19538293e168bddbd | ランサムウェア集団、SAP NetWeaver攻撃に参入 | bleepingcomputer.com | 2025-05-15 | https://www.bleepingcomputer.com/news/security/ransomware-gangs-join-ongoing-sap-netweaver-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-f47a43f682d4bb61a2bc | React2Shellの欠陥が30組織の侵害に悪用、7.7万のIPアドレスが脆弱 | bleepingcomputer.com | 2025-12-08 | https://www.bleepingcomputer.com/news/security/react2shell-flaw-exploited-to-breach-30-orgs-77k-ip-addresses-vulnerable/ | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc5174--0aff60e0dfc1afff | UNC5174 |  | 不明 | UNC****/UNC5174/UNC5174.pdf | report | TLP:CLEAR | 中 |
| source--unc5174--5b9b5bec8a63548a | readme |  | 不明 | UNC****/UNC5174/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--unc5174--626245061e5734b4 | VShell |  | 不明 | UNC****/UNC5174/VShell.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
