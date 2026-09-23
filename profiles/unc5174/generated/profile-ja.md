# UNC5174 脅威アクタープロファイル

- プロファイルID: `actor--unc5174`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

UNC5174の標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC5174**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| CL-STA-1015 | Palo Alto Networks Unit 42 | overlapping | 高 | `source--unit42-react2shell-cl-sta-1015-2025` | Unit 42 writes CL-STA-1015 (aka UNC5174), but this is a cross-vendor cluster mapping. It is retained as overlapping until scope stability is independently confirmed. |

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
| CL-STA-1015 | taxonomy-overlaps-with | Unit 42 maps its CL-STA-1015 activity cluster to UNC5174; the mapping is preserved as a cross-taxonomy overlap rather than a global exact identity. | 中 | `source--unit42-react2shell-cl-sta-1015-2025` |

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
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UNC5174 | canonical-name | 高 |  | https://rhisac.org/threat-intelligence/f5-big-ip-and-screenconnect-cves/<br>https://www.mandiant.com/resources/blog/initial-access-brokers-exploit-f5-screenconnect |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | UNC5174 | canonical-name | 高 |  |  |

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
| malware--snowlight | SNOWLIGHT | Linux dropper used to retrieve follow-on malware including VShell. | 不明 | 不明 | 高 | `source--unit42-react2shell-cl-sta-1015-2025` |
| malware--vshell | VShell | Remote access trojan deployed after SNOWLIGHT. | 不明 | 不明 | 高 | `source--unit42-react2shell-cl-sta-1015-2025` |

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
| 中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用 | infrastructure-operation | 不明 | 不明 | 2025-04-16 | target--activity-rule--country--f35cd09db0a72555b38a, target--activity-rule--sector--210dddb39397dbe50e91 |  |  | victim--activity-rule--caea1296908bb424f92e | 中国系APTグループUNC5174がLinux向けにSNOWLIGHTマルウェアとVShellを展開 SNOWLIGHTはCベースのELF型ドロッパーで、メモリ上にVShell RATを展開 VShellはWebSocketを用いたC2通信が可能なファイルレス型RAT 攻撃には脆弱性（例：CVE-2024-8963など）を悪用して初期侵入 標的国は日本を含む20カ国以上に及び、政府・重要インフラが主な標的 | 中 | `source--daily-c5a9c42da8ab9e7b0010` |
| ランサムウェア集団、SAP NetWeaver攻撃に参入 | ransomware-extortion | 不明 | 不明 | 2025-05-15 |  |  |  | victim--activity-rule--b0587ebaf67a29526988 | SAP NetWeaverの重大な脆弱性（CVE-2025-31324）を悪用した攻撃に、RansomEXXおよびBianLianランサムウェア集団が参入。 この脆弱性は、認証なしでのファイルアップロードを可能にし、リモートコード実行を許す。 ReliaQuestの分析により、BianLianが過去に使用したC2サーバーのIPアドレスとの関連が確認された。 RansomEXXは、PipeMagicバックドアやBrute Ratel C2フレームワークを利用し、攻撃を展開。 中国のAPTグループ（Chaya_004、UNC5221、UNC5174、CL-STA-0048）も同脆弱性を悪用し、少なくとも581のSAP NetWeaverインスタンスにバックドアを設置。 | 中 | `source--daily-c8f19538293e168bddbd` |
| CL-STA-1015／UNC5174と整合するReact2Shell後続活動 | intrusion | 不明 | 不明 | 2025-12-12 |  | malware--snowlight, malware--vshell |  |  | Unit 42はReact2Shell（CVE-2025-55182）悪用後、CL-STA-1015と高い確度で整合する活動を観測した。攻撃者はcurl/wgetでsltシェルスクリプトをファイルレス実行し、SNOWLIGHTとVShellを展開した。React2Shell全体の侵害数や脆弱ホスト数は複数主体を含むため、このクラスタ固有の被害数・標的としては記録しない。 | 中 | `source--daily-f47a43f682d4bb61a2bc`, `source--gtig-react2shell-multiple-actors-2025`, `source--unit42-react2shell-cl-sta-1015-2025` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用 | UNC5174 | 情報なし | 情報なし | 情報なし | 日本, 政府・行政 | 被害事例: 中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用 | 中 |
| ランサムウェア集団、SAP NetWeaver攻撃に参入 | UNC5174 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: ランサムウェア集団、SAP NetWeaver攻撃に参入 | 中 |
| CL-STA-1015／UNC5174と整合するReact2Shell後続活動 | UNC5174 | SNOWLIGHT, VShell | 情報なし | 情報なし | 情報なし | 情報なし | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 日本 | 活動「中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-c5a9c42da8ab9e7b0010` |
| sectors | 政府・行政 | 活動「中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-c5a9c42da8ab9e7b0010` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ランサムウェア集団、SAP NetWeaver攻撃に参入 | 非公開 | anonymous | unknown | reported |  |  |  |  | encryption: ランサムウェア集団、SAP NetWeaver攻撃に参入 | 不明 | 不明 | 2025-05-15 | 中 | `source--daily-c8f19538293e168bddbd` |
| 被害事例: 中国系ハッカーがLinuxシステムを標的にSNOWLIGHTマルウェアとVShellツールを使用 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--f35cd09db0a72555b38a, target--activity-rule--sector--210dddb39397dbe50e91 |  |  |  |  | 不明 | 不明 | 2025-04-16 | 中 | `source--daily-c5a9c42da8ab9e7b0010` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1105 | Ingress Tool Transfer | e_severity Low, confidence Low, tag VShell, tag RAT, updated_at 2025_08_26, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1105, mitre_technique_name Ingress_Tool_Transfer;) alert tcp $HOME_NET any -> $EXTERNAL_NET any (msg:"[NVISO] Potential VShell beacon payload request (Windows i386)"; flow:to_server,established; content:"w32 "; fast_pattern; offset:0; depth:6; stream_size:client,<=,45; flowb |  |  | 不明 | 不明 | 中 | `source--unc5174--626245061e5734b4` |
| Command And Control | T1573 | Encrypted Channel | ty Critical, confidence Medium, tag VShell, tag RAT, updated_at 2025_08_26, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1573, mitre_technique_name Encrypted_Channel;) alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"[NVISO] VShell beacon server handshake"; flow:to_client,established; content:"\|3c 00 00 00\|"; fast_pattern; offset:0; depth:4; byte_test:1,&,0x80,0x4; content:"\|20 00 00 00\|"; offse |  |  | 不明 | 不明 | 中 | `source--unc5174--626245061e5734b4` |

## IOC／artifact概要

- IOC値: 67件
- IOC観測: 97件
- 複数攻撃で観測: 0件
- 要レビュー候補: 4件
- 非IOC artifact観測: 6件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- React2Shell reporting contains multiple actor clusters. Unit 42 maps CL-STA-1015 to UNC5174, while GTIG separately tracks a SNOWLIGHT-using cluster as UNC6586; malware reuse alone must not merge those clusters.

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
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unit42-react2shell-cl-sta-1015-2025 | Exploitation of Critical Vulnerability in React Server Components | Palo Alto Networks Unit 42 | 2025-12-12 | https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--gtig-react2shell-multiple-actors-2025 | Multiple Threat Actors Exploit React2Shell (CVE-2025-55182) | Google Threat Intelligence Group | 2025-12-12 | https://cloud.google.com/blog/topics/threat-intelligence/threat-actors-exploit-react2shell-cve-2025-55182 | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
