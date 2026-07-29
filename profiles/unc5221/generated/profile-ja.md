# UNC5221 脅威アクタープロファイル

- プロファイルID: `actor--unc5221`
- 状態: draft
- 更新日時: 2026-07-29T15:36:12Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC5221の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC5221**
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
| etda-threat-group-cards | UNC5221, UTA0178 | canonical-name | 高 | China | https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day<br>https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/<br>https://www.volexity.com/blog/2024/01/15/ivanti-connect-secure-vpn-exploitation-goes-global/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UTA0178 | canonical-name | 高 | CN | https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/<br>https://www.rewterz.com/rewterz-news/rewterz-threat-advisory-ivanti-vpn-zero-days-weaponized-by-unc5221-threat-actors-to-deploy-multiple-malware-families-active-iocs/<br>https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| UNC5337 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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
| CISA、RESURGEマルウェアがIvantiデバイスで休眠する可能性を警告 | malware-campaign | 不明 | 不明 | 2026-02-28 |  |  |  |  | CISAはCVE-2025-0282を突くゼロデイで侵害されたIvanti Connect Secure向けRESURGEの新情報を公開 更新内容は、機器上で長期間検知されにくい「潜伏」と、ネットワーク層の回避・認証手口に焦点を当てている Mandiantは本脆弱性が2024年12月中旬以降、中国関連のUNC5221によりゼロデイ悪用されたと報告 RESURGEは外向きビーコンせず特定のTLS流入を待機し、CRC32フィンガープリントと偽Ivanti証明書で通信相手を識別する CISAは「接続が試みられるまで休眠し得る」ため未検知感染の可能性を警告し、更新IoCでの検出・除去を促した | 中 | `source--daily-ba66767df3d87f8e056a` |
| Ivanti、3月中旬以降悪用されたConnect Secureのゼロデイ脆弱性を修正 | cyber-espionage | 不明 | 不明 | 2025-04-04 |  |  | ttp--activity-rule--d804599bbb259da95aad |  | IvantiはConnect Secureのリモートコード実行（RCE）脆弱性CVE-2025-22457を修正 この脆弱性はスタックベースのバッファオーバーフローに起因 Pulse Connect Secure 9.1x、Ivanti Connect Secure 22.7R2.5以前、Policy Secure、Neurons for ZTAゲートウェイに影響 2月11日にリリースされたバージョン22.7R2.6で修正済み 中国関連のサイバースパイグループUNC5221が3月中旬以降、この脆弱性を悪用してTRAILBLAZE（インメモリドロッパー）とBRUSHFIRE（パッシブバックドア）などのマルウェアを展開 | 中 | `source--daily-91b63e035fe4123d4de8` |
| Google：Brickstormマルウェアが1年以上にわたり米国組織のデータを窃取 | cyber-espionage | 不明 | 不明 | 2025-09-25 |  |  |  | victim--activity-rule--f34bbd1142d16c42d677 | Googleは、技術・法律・SaaS・BPO分野の米組織を主に標的とした、UNC5221によるBrickstormを使った長期スパイ活動を確認し、継続的なデータ窃取を報告。 BrickstormはGo製バックドアで、Webサーバ/ファイル操作/ドロッパ/SOCKS中継/シェル実行など多機能に振る舞う。 平均潜伏は393日。EDR非対応のvCenter/ESXi等に常駐し、CloudflareやHeroku風トラフィックでC2通信を偽装。 初期侵入はエッジデバイスのゼロデイ悪用が濃厚。vCenterに「Bricksteal」を導入し資格情報収集、VM複製やSSH有効化で横展開。 目的はEntra ID経由のメール流出。UNC5221に紐付けられ、Mandiantが検出スクリプト公開も限界（検出保証なし等）を明記。 | 中 | `source--daily-851d3853332e52ad741a` |
| Ivanti EPMMの脆弱性、政府機関への侵入に中国系ハッカーが悪用 | intrusion | 2025-05-15 | 2025-05-15 | 2025-05-23 |  |  |  | victim--activity-rule--2777d9aa01e356b0a630 | 中国系ハッカーが、Ivanti Endpoint Manager Mobile（EPMM）のリモートコード実行脆弱性（CVE-2025-4428）を悪用。 この脆弱性は、特別に細工されたAPIリクエストにより、バージョン12.5.0.0以前のEPMMでコード実行が可能。 Ivantiは、認証バイパスの脆弱性（CVE-2025-4427）とともに、2025年5月13日にこれらの脆弱性を修正。 EclecticIQの研究者は、2025年5月15日以降、CVE-2025-4428が広範に悪用されていることを確認。 攻撃は、Ivanti製品のゼロデイ脆弱性を専門とするUNC5221と呼ばれるグループによるものとされる。 | 中 | `source--daily-9c44f6340b9488e0ae9a` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Ivanti EPMMの脆弱性、政府機関への侵入に中国系ハッカーが悪用 | 非公開 | anonymous | unknown | reported |  |  |  | エンドポイント |  | 2025-05-15 | 2025-05-15 | 2025-05-23 | 中 | `source--daily-9c44f6340b9488e0ae9a` |
| 被害事例: Google：Brickstormマルウェアが1年以上にわたり米国組織のデータを窃取 | 非公開 | aggregate | multiple-organizations | reported |  |  |  | メール／メールアカウント | data-theft: Google：Brickstormマルウェアが1年以上にわたり米国組織のデータを窃取<br>espionage: Googleは、技術・法律・SaaS・BPO分野の米組織を主に標的とした、UNC5221によるBrickstormを使った長期スパイ活動を確認し、継続的なデータ窃取を報告。 | 不明 | 不明 | 2025-09-25 | 中 | `source--daily-851d3853332e52ad741a` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1190 | Exploit Public-Facing Application | IvantiはConnect Secureのリモートコード実行（RCE）脆弱性CVE-2025-22457を修正 この脆弱性はスタックベースのバッファオーバーフローに起因 Pulse Connect Secure 9.1x、Ivanti Connect Secure 22.7R2.5以前、Policy Secure、Neurons for ZTAゲートウェイに影響 2月11日にリリースされたバージョン22.7R2.6で修正済み 中国関連のサイバースパイグループUNC5221が3月中旬以降、この脆弱性を悪用してTRAILBLAZE（インメモリドロッパー）とBRUSHFIRE（パッシブバックドア）などのマルウェアを展開 |  | activity--daily-2f66c9c7118896c3d86d | 不明 | 不明 | 中 | `source--daily-91b63e035fe4123d4de8` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 30件（`artifacts.csv`）

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
| source--daily-851d3853332e52ad741a | Google：Brickstormマルウェアが1年以上にわたり米国組織のデータを窃取 | bleepingcomputer.com | 2025-09-25 | https://www.bleepingcomputer.com/news/security/google-brickstorm-malware-used-to-steal-us-orgs-data-for-over-a-year/ | osint-report | TLP:CLEAR | 中 |
| source--daily-91b63e035fe4123d4de8 | Ivanti、3月中旬以降悪用されたConnect Secureのゼロデイ脆弱性を修正 | bleepingcomputer.com | 2025-04-04 | https://www.bleepingcomputer.com/news/security/ivanti-patches-connect-secure-zero-day-exploited-since-mid-march/ | osint-report | TLP:CLEAR | 中 |
| source--daily-9c44f6340b9488e0ae9a | Ivanti EPMMの脆弱性、政府機関への侵入に中国系ハッカーが悪用 | bleepingcomputer.com | 2025-05-23 | https://www.bleepingcomputer.com/news/security/ivanti-epmm-flaw-exploited-by-chinese-hackers-to-breach-govt-agencies/ | osint-report | TLP:CLEAR | 中 |
| source--daily-ba66767df3d87f8e056a | CISA、RESURGEマルウェアがIvantiデバイスで休眠する可能性を警告 | bleepingcomputer.com | 2026-02-28 | https://www.bleepingcomputer.com/news/security/cisa-warns-that-resurge-malware-can-be-dormant-on-ivanti-devices/ | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc5221--0f7d918e38c7c2d3 | cybersecurity forecast 2026 en |  | 2026 | summary/2025/cybersecurity-forecast-2026-en.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--18058cb4e929ed14 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--28ac6a664c181814 | eset apt activity report q4 2025 q1 2026 |  | 2025 | summary/2026/eset-apt-activity-report-q4-2025-q1-2026.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--2e8489379d918e15 | security perspectives on security for the board ed9 |  | 不明 | summary/2025/security-perspectives-on-security-for-the-board-ed9.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--307ffc9c1df10ad9 | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--361256722e4754af | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--38ded5f477438ae9 | Dragos 2026 OT Cybersecurity Report A Year in Review |  | 2026 | OT/Dragos-2026-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--4b3968d25ea102bc | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--5193215d691fb506 | article |  | 不明 | kimsuky/APTDown/article.txt | text-data | TLP:CLEAR | 中 |
| source--unc5221--575c7e64fdd13e9a | 2025 Year in Review  Malicious Infrastructure |  | 2025 | summary/2026/2025 Year in Review- Malicious Infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--7041904425b4d7e1 | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--993f95ce09dc4e0b | SixMap Research Energy Sector Exposure Assessment |  | 不明 | summary/2025/SixMap-Research_Energy-Sector-Exposure-Assessment.pdf | report | TLP:CLEAR | 中 |
| source--unc5221--b2f42356a5b0d760 | unc5221 |  | 不明 | actor_profile/evidence/unc5221.csv | structured-data | TLP:CLEAR | 中 |
| source--unc5221--bac10c3e8714d8ca | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
