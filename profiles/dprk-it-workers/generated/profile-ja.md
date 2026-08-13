# DPRK IT Worker Schemes 脅威アクタープロファイル

- プロファイルID: `actor--dprk-it-workers`
- 状態: draft
- 更新日時: 2026-08-13T11:03:44Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

DPRK IT Worker Schemesの標準化プロファイル。リポジトリ内の専用資料8件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **DPRK IT Worker Schemes**
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
| financial-gain | Financially motivated intrusion or fraud. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--dprk-it-workers-anydesk | AnyDesk | リモートデスクトップの正規製品。ITワーカーが業務環境へ接続する経路として使用が確認された。 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| tool--dprk-it-workers-google-remote-desktop | Google Remote Desktop | リモートデスクトップの正規サービス。VDIへの接続に使用された。 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| tool--dprk-it-workers-astrillvpn | AstrillVPN | 商用VPNサービス。実際の所在地を秘匿してVDIへ接続するために使用された。 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| tool--dprk-it-workers-chatgpt | ChatGPT | コーディング支援と技術的な質問への回答に使用された生成AIサービス。 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| tool--dprk-it-workers-gemini | Google Gemini | 文書偽造、とりわけ身分証明書の加工に使用された生成AIサービス。 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |

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
| 偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測 | cyber-espionage | 不明 | 不明 | 2026-08-10 | target--activity-rule--sector--4221b5fbb827488c6eaa, target--dprk-it-workers--sector--cryptocurrency, target--dprk-it-workers--sector--information-technology |  | ttp--dprk-it-workers-anyrun2-t1078, ttp--dprk-it-workers-anyrun2-t1090, ttp--dprk-it-workers-anyrun2-t1219, ttp--dprk-it-workers-anyrun2-t1585, ttp--dprk-it-workers-anyrun2-t1656 | victim--activity-rule--53b06986d70b4343e693 | ANY.RUNの研究者が偽のDeFi企業Ballena Azul LTD(Blue Whale LTD)を設立し、北朝鮮関連Famous Chollimaと疑われるITワーカー3名(Angelo Espree、Jack Anderson、Lucas Theo)を実際に採用して、内部から業務活動を観測した調査報告。第1弾に続く第2弾にあたる。ITワーカーは偽造・窃取した身分証明書、SSN、銀行口座を用いてリモート採用に応募し、正規従業員として組織内部へ入り込もうとしていた。採用後はGoogle Remote Desktop、AnyDesk、AstrillVPN、VPSを利用してVDIへ接続し、ChatGPTをコーディングと技術的な質問への回答に、Google Geminiを身分証明書を含む文書の偽造に、ライブ翻訳ツールを面接時の受け答えに利用していた。ANY.RUNはFamous Chollimaの目的を短期的な侵入ではなく、従業員として長期間アクセスし、ソースコード、知的財産、業務プロセスへ接触しながら給与を北朝鮮へ還流することであると評価している。調査では北朝鮮が運用するVPS、AstrillVPNの出口ノード、暗号資産ウォレットが特定され、複数のITワーカーが連携して運用している実態が示された。 | 高 | `source--anyrun-it-workers-part-two-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測 | DPRK IT Worker Schemes | 情報なし | T1078 Valid Accounts, T1090 Proxy, T1219 Remote Access Tools, T1585 Establish Accounts, T1656 Impersonation | 情報なし | 金融, 暗号資産・DeFi, リモート採用を行うIT・ソフトウェア開発企業 | 被害事例: 偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 金融 | 活動「偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--anyrun-it-workers-part-two-2026` |
| sectors | 暗号資産・DeFi | 研究者が設立した偽のDeFiスタートアップに応募・就労した事例。ANY.RUNはFamous Chollimaの狙いを、ソースコード、知的財産、業務プロセスへの長期的な接触と、給与の北朝鮮への還流であると記載している。 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| sectors | リモート採用を行うIT・ソフトウェア開発企業 | ANY.RUNは「Their goal is simple: get hired by Western companies」と記載し、リモート採用を通じて正規従業員として組織内部へ入り込むことを目的とすると評価している。 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--4221b5fbb827488c6eaa, target--dprk-it-workers--sector--cryptocurrency, target--dprk-it-workers--sector--information-technology |  | ttp--dprk-it-workers-anyrun2-t1078, ttp--dprk-it-workers-anyrun2-t1090, ttp--dprk-it-workers-anyrun2-t1219, ttp--dprk-it-workers-anyrun2-t1585, ttp--dprk-it-workers-anyrun2-t1656 | VPN／リモートアクセス機器, 開発環境／ソースコード |  | 不明 | 不明 | 2026-08-10 | 高 | `source--anyrun-it-workers-part-two-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Persistence | T1078 | Valid Accounts | 採用によって正規従業員として付与されたアカウントと権限を用い、短期的な侵入ではなく長期の内部滞在としてソースコード、知的財産、業務プロセスへ接触した。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Command and Control | T1090 | Proxy | AstrillVPNの出口ノードと北朝鮮が運用するVPSを経由して接続し、実際の所在地を秘匿した。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Command and Control | T1219 | Remote Access Tools | Google Remote DesktopおよびAnyDeskを用いて業務用のVDI環境へ接続した。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Resource Development | T1585 | Establish Accounts | 応募用の人物像とそれに紐づく口座・連絡手段を用意し、採用選考を通過できる体裁を整えた。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Defense Evasion | T1656 | Impersonation | 偽造または窃取した身分証明書、社会保障番号(SSN)、銀行口座を用いて別人になりすまし、Angelo Espree(スマートコントラクト開発者)、Jack Anderson(フロントエンド開発者)、Lucas Theo(バックエンド開発者)としてリモート職へ応募・採用された。偽装身分はテキサス、ニューヨーク、カリフォルニアの所在を主張していた。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Collection | T1005 | Data from Local System | 1 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Discovery | T1016 | System Network Configuration Discovery | Use of systeminfo to obtain system information T1016 — System Network Configuration Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” T1614 — System Location Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” Command and Control T1219 — Remote Access |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Stealth | T1027.013 | Encrypted/Encoded File | es: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltrati |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | rotocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Execution | T1059.006 | Python | Initial Access : Spearphishing Attachment T1566.001 Phishing: Spearphishing via Service T1566.003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.00 |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Execution | T1059.007 | JavaScript | ishing: Spearphishing via Service T1566.003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Command And Control | T1071.001 | Web Protocols | 027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Command And Control | T1071.002 | File Transfer Protocols | Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Discovery | T1082 | System Information Discovery | 003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encod |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250`, `source--dprk-it-workers--bc62b8e29937a263` |
| Discovery | T1083 | File and Directory Discovery | 003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Command And Control | T1090 | Proxy | Search Engines Mass search for developers on GitHub Initial Access T1566 — Phishing Mass phishing via GitHub pull requests targeting developers Defense Evasion T1090 — Proxy Use of AstrillVPN to hide real location Discovery T1082 — System Information Discovery Use of DXDIAG to obtain system information 2025/12/25 09:52 Smile, You’re on Camera: A Live Stream from Inside Lazarus Group’s IT Workers Scheme \| by ANY.RUN \| Dec, 2025 \| Medium https |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Execution | T1204.002 | Malicious File | re Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Tran |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Command And Control | T1219 | Remote Access Tools | ation”, “where is my ip” T1614 — System Location Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” Command and Control T1219 — Remote Access Software Use of AnyDesk Use of Google Remote Desktop T1090 — Proxy Use of AstrillVPN Written by ANY.RUN 185 followers · 2 following Empowering businesses with proactive security solutions: Interactive Sandbox, TI Lookup and Feeds. Sign up: https://app.any.run#reg |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Credential Access | T1555.003 | Credentials from Web Browsers | e Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071. |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Collection | T1560.001 | Archive via Utility | cated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Rec |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Initial Access | T1566 | Phishing | d Pro Vercel Calendly TTPs / ATT&CK Reconnaissance T1593.002 — Search Open Websites/Domains: Search Engines Mass search for developers on GitHub Initial Access T1566 — Phishing Mass phishing via GitHub pull requests targeting developers Defense Evasion T1090 — Proxy Use of AstrillVPN to hide real location Discovery T1082 — System Information Discovery Use of DXDIAG to obtain system information 2025/12/25 09:52 Smile, You’re on Camera: A Live |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Initial Access | T1566.001 | Spearphishing Attachment | CYBER THREAT ANALYSIS Appendix C MITRE ATT&CK Techniques Tactic: Technique ATT&CK Code Initial Access : Spearphishing Attachment T1566.001 Phishing: Spearphishing via Service T1566.003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infras |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Initial Access | T1566.003 | Spearphishing via Service | ITRE ATT&CK Techniques Tactic: Technique ATT&CK Code Initial Access : Spearphishing Attachment T1566.001 Phishing: Spearphishing via Service T1566.003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Pa |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Resource Development | T1583.001 | Domains | Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Disc |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Resource Development | T1583.004 | Server | Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Arch |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Reconnaissance | T1593.002 | Search Engines | Slack Telegram Online platforms: Github LinkedIn ZipRecruiter Bold Pro Vercel Calendly TTPs / ATT&CK Reconnaissance T1593.002 — Search Open Websites/Domains: Search Engines Mass search for developers on GitHub Initial Access T1566 — Phishing Mass phishing via GitHub pull requests targeting developers Defense Evasion T1090 — Proxy Use of AstrillVPN to hide real location Discovery T1082 — System Informat |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Discovery | T1614 | System Location Discovery | fo to obtain system information T1016 — System Network Configuration Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” T1614 — System Location Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” Command and Control T1219 — Remote Access Software Use of AnyDesk Use of Google Remote Desktop T1090 — Proxy Use of AstrillVPN Written by ANY.RUN 185 followers · 2 follow |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |

## IOC／artifact概要

- IOC値: 159件
- IOC観測: 164件
- 複数攻撃で観測: 0件
- 要レビュー候補: 50件
- 非IOC artifact観測: 63件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| DPRK ITワーカーはリモート採用を通じて正規従業員として企業内部へ入り込み、生成AIを身分偽造・コーディング・面接時の翻訳へ活用している。 | 高 | `source--anyrun-it-workers-part-two-2026` | ANY.RUNが偽企業を設立して3名を実際に採用し、内部から直接観測した報告に基づく。 |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--dprk-it-workers--94775915798a421c | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--b57b6250dea995f1 | DeceptiveDevelopment and North Korean IT workers from primitive crypto theft to sophisticated AI based deception |  | 不明 | CyberMerceNary/ITWorker/DeceptiveDevelopment-and-North-Korean-IT-workers-from-primitive-crypto-theft-to-sophisticated-AI-based-deception.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--bc62b8e29937a263 | Inside the ScamNorth Korea’s IT Worker Threat |  | 不明 | CyberMerceNary/ITWorker/Inside the ScamNorth Korea’s IT Worker Threat.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--a08fdc503ef8f9a4 | JOINT CSA DPRK SOCIAL ENGINEERING |  | 不明 | CyberMerceNary/ITWorker/JOINT_CSA_DPRK_SOCIAL_ENGINEERING.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--e7356e8e649de477 | OFSI Advisory on North Korean IT Workers |  | 不明 | CyberMerceNary/ITWorker/OFSI_Advisory_on_North_Korean_IT_Workers.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--15da1b5bbfbc5250 | Smile, You’re on Camera  A Live Stream from Inside Lazarus Group’s IT Workers Scheme |  | 不明 | CyberMerceNary/ITWorker/Smile, You’re on Camera_ A Live Stream from Inside Lazarus Group’s IT Workers Scheme.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--eb29460df938ef81 | north korean scammers are posing as it freelancers here's how you can protect your business |  | 不明 | CyberMerceNary/ITWorker/north-korean-scammers-are-posing-as-it-freelancers_-here's-how-you-can-protect-your-business.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--769f09c40948bde0 | readme |  | 不明 | CyberMerceNary/ITWorker/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--anyrun-it-workers-part-two-2026 | Smile, You're on Camera! Part 2: Hiring Lazarus APT IT Workers at a Fake DeFi Startup | ANY.RUN | 2026-08-10 | https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation-part-two/ | primary-report | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
