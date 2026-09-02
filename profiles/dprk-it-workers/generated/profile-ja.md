# DPRK IT Worker Schemes 脅威アクタープロファイル

- プロファイルID: `actor--dprk-it-workers`
- 状態: draft
- 更新日時: 2026-09-02T12:58:02Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

DPRK IT Worker Schemesの標準化プロファイル。リポジトリ内の専用資料8件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **DPRK IT Worker Schemes**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Famous Chollima | CrowdStrike | exact | 中 | `source--daily-10f083232dfd566dc4f9` | CrowdStrikeのFAMOUS CHOLLIMAは、北朝鮮政権へ賃金を送金するための不正就労(リモートITワーカー)を中核とする追跡名であり、本プロファイル「DPRK IT Worker Schemes」が対象とするクラスタと実質的に同一の範囲を指す。したがってscopeはexactとする。profiles/contagious-interview 側にも同名aliasが登録されているが、そちらはscope: broaderであり、「FAMOUS CHOLLIMAはContagious Interview(偽求人面接によるマルウェア配布キャンペーン)より広い」ことを表す記録である。ここでexactを与えることで、日次キューのActorRegistryは複数プロファイル一致の場合に一意なexact一致を優先し、「Famous Chollima」の言及を本プロファイルへ解決する。運用上の振り分け基準: リモートITワーカーの不正就労・身元詐称・賃金送金を主題とする資料は本プロファイルへ、偽の採用面接やコーディング課題を用いたマルウェア配布を主題とする資料はcontagious-interviewへ割り当てる。CrowdStrikeが同一名の下にContagious Interview系の活動も併せて整理する場合がある点は、両プロファイルのalias注記として残す。exactは日次キューでの解決先を一意に定めるためのモデリング上の判断であり、個々の資料についてはAGENT.mdに従い原文で実行主体を確認したうえでレコードを採否する。 根拠資料: Huntress「Insights into Suspected DPRK Workers: Red Flags to Look Out For」(2026-08-26)は「North Korean (DPRK) remote IT workers (sometimes referred to as FAMOUS CHOLLIMA)」と記し、本プロファイルの対象とFAMOUS CHOLLIMAを同義に用いている。 |

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
| 北朝鮮（DPRK）リモートワーカー調査から得られた知見 | reported-activity | 不明 | 不明 | 2026-09-01 |  |  |  |  | Huntressは2026年、複数組織の調査を支援し、偽造・盗用した身元を使って正規従業員として採用された可能性が高い北朝鮮系リモートワーカー5人を特定した。 医療分野の3人はAstrill VPN、IPRoyal Proxy、WorkTitans B.V.などを利用し、位置情報を隠蔽していたほか、勤務時間や偽造身分証にも共通する異常が確認された。 金融分野ではPiKVMを使ったハードウェアレベルの遠隔操作、Guermok USBキャプチャカード、盗用・加工した顔写真など、過去のDPRK ITワーカー活動と重なる痕跡を確認した。 別の事例では、盗用した身元情報、Toffeeshare、VDO Ninja、音声・画面記録用Chrome拡張などを利用し、不正に雇用を得ていた可能性が高いと評価された。 Huntressは単一IOCだけではDPRK関与を証明できないため、端末、認証、ブラウザ、クラウド、勤務時間、身分証メタデータなど複数の兆候を組み合わせる必要があるとしている。 | 中 | `source--daily-10f083232dfd566dc4f9` |
| 偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測 | cyber-espionage | 不明 | 不明 | 2026-08-10 | target--activity-rule--sector--4221b5fbb827488c6eaa, target--dprk-it-workers--sector--cryptocurrency, target--dprk-it-workers--sector--information-technology |  | ttp--dprk-it-workers-anyrun2-t1078, ttp--dprk-it-workers-anyrun2-t1090, ttp--dprk-it-workers-anyrun2-t1219, ttp--dprk-it-workers-anyrun2-t1585, ttp--dprk-it-workers-anyrun2-t1656 | victim--activity-rule--53b06986d70b4343e693 | ANY.RUNの研究者が偽のDeFi企業Ballena Azul LTD(Blue Whale LTD)を設立し、北朝鮮関連Famous Chollimaと疑われるITワーカー3名(Angelo Espree、Jack Anderson、Lucas Theo)を実際に採用して、内部から業務活動を観測した調査報告。第1弾に続く第2弾にあたる。ITワーカーは偽造・窃取した身分証明書、SSN、銀行口座を用いてリモート採用に応募し、正規従業員として組織内部へ入り込もうとしていた。採用後はGoogle Remote Desktop、AnyDesk、AstrillVPN、VPSを利用してVDIへ接続し、ChatGPTをコーディングと技術的な質問への回答に、Google Geminiを身分証明書を含む文書の偽造に、ライブ翻訳ツールを面接時の受け答えに利用していた。ANY.RUNはFamous Chollimaの目的を短期的な侵入ではなく、従業員として長期間アクセスし、ソースコード、知的財産、業務プロセスへ接触しながら給与を北朝鮮へ還流することであると評価している。調査では北朝鮮が運用するVPS、AstrillVPNの出口ノード、暗号資産ウォレットが特定され、複数のITワーカーが連携して運用している実態が示された。 | 高 | `source--anyrun-it-workers-part-two-2026` |
| NKITWエコシステムの内部運用実態(役割分担・身分偽装・RB Site／NetKey／OConnect)の解明 | financial-fraud | 不明 | 不明 | 2026-03-18 | target--dprk-it-workers--region--north-america, target--dprk-it-workers--region--western-europe, target--dprk-it-workers--sector--information-technology, target--dprk-it-workers--sector--web-agency |  | ttp--activity-rule--c8e6994beb392d81aac5, ttp--dprk-it-workers-flare-nkitw-t1078, ttp--dprk-it-workers-flare-nkitw-t1219, ttp--dprk-it-workers-flare-nkitw-t1583-003, ttp--dprk-it-workers-flare-nkitw-t1585-001, ttp--dprk-it-workers-flare-nkitw-t1585-002, ttp--dprk-it-workers-flare-nkitw-t1586, ttp--dprk-it-workers-flare-nkitw-t1593-002, ttp--dprk-it-workers-flare-nkitw-t1656 | victim--activity-rule--a31956aff1a38158c5d9 | FlareとIBM X-Forceが共同で実施した、北朝鮮IT労働者(North Korean IT Worker、NKITW)エコシステムの日常運用に関する調査報告。原文は「does not focus on a specific incident or cluster of activity」と明記しており、特定の侵害事案ではなく、内部スプレッドシート、内部共有スライド、IP Messengerログ、Google Translate履歴、ブラウザ履歴といった一次資料から運用実態そのものを解明したものである。<br><br>組織構造として、NKITWエコシステムはRecruiter(候補者の選別と初回面接の録画)、Facilitator(ペルソナ作成、就職獲得、新規要員のオンボーディング、協力者との接続)、IT Worker(実務)、Collaborator／Broker(西側の身元提供者・アカウント売買)の4つの役割で構成されると評価している。FacilitatorとIT Workerの職掌は重複し、厳密には分離できない。採用面接では「C Digital LLC」というステルス期のスタートアップを名乗り、候補者へ米国の身元(profiles)を貸与すると説明する。候補者自身がDPRKのための就労と認識しているかは確認できていない。<br><br>身分偽装は、Protonmail等の捨てアドレスを起点にGmailを取得し、LinkedIn、GitHub、Upwork等へ偽プロフィールを作成する流れで行われる。顔写真は逆画像検索を避けるためAI編集され、履歴書テンプレートの改変、企業のメールアドレス書式調査に基づく偽の前職照会状の作成、偽装身分の国籍に合わせたGoogle Voice番号の使用が確認されている。フルタイム就労では本人確認と給与振込が障壁となるため、LinkedInやGitHubで勧誘した西側協力者に薬物検査、バックグラウンドチェック、I-9書類、社給端末の受領、銀行・税務情報の提供を代行させ、協力者の実機へAnyDesk等でリモート接続して就労する。フリーランス就労では検証済みアカウントを違法フォーラムやブローカーから購入する。<br><br>就労維持の局面では、Google TranslateとChatGPTが恒常的に使用される。Jiraチケットの翻訳、ChatGPTへの解法照会、回答の翻訳、Slackの翻訳、GitHubへのPull Request提出という循環が数週間から数か月続く。翻訳履歴の多くが英語から韓国語への方向であり、英語で下書きした文面を韓国語へ戻して意味を自己検証していると評価されている。最終的に成果や意思疎通の問題から解雇に至り、協力者経由での端末返送と最終給与の受領を経て、新しい身分で同じ工程を繰り返す。<br><br>内部基盤としては、北朝鮮側が運用する管理用Webプラットフォーム「RB Site」(内部アドレス 192.168.109.2、machine_info、network_reports、payment、blocked_urls等の画面)と「NetkeyRegister」(内部アドレス 172.20.100.7:8000)が特定された。FlareはRBをKorea Ryonbong General Corporationの略と中確度で評価している。端末にはDPRK製VPNのNetKey(4.1／5.0／5.1)またはOConnect(5.3／5.5／5.7／5.9.3／6.0.0)が導入され、実行パスに「STN Corp」「rb corp」が現れる。バージョンの連続性から、5.2前後でNetKeyがOConnectへ改称された可能性が高いと評価されている。内部連絡にはサーバー不要のIP Messengerが使われる。<br><br>帰属について原文は、軍需工業部、国防省、科学教育部、偵察総局など複数の政府機関・党組織・フロント企業がそれぞれITワーカーを展開しており、個々のワーカーを特定部署へ確度高く帰属させることは困難であるとしている。最優先の動機は、獲得した給与を当局へ還流させることである。原文はさらに、一部のチームがデータの持ち出しや恐喝、暗号資産の窃取にも関与すると記載している。 | 高 | `source--flare-ibm-xforce-nkitw-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 北朝鮮（DPRK）リモートワーカー調査から得られた知見 | DPRK IT Worker Schemes | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| 偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測 | DPRK IT Worker Schemes | 情報なし | T1078 Valid Accounts, T1090 Proxy, T1219 Remote Access Tools, T1585 Establish Accounts, T1656 Impersonation | 情報なし | 金融, 暗号資産・DeFi, リモート採用を行うIT・ソフトウェア開発企業 | 被害事例: 偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測 | 高 |
| NKITWエコシステムの内部運用実態(役割分担・身分偽装・RB Site／NetKey／OConnect)の解明 | DPRK IT Worker Schemes | 情報なし | T1219.002 Remote Desktop Software, T1078 Valid Accounts, T1219 Remote Access Software, T1583.003 Acquire Infrastructure: Virtual Private Server, T1585.001 Establish Accounts: Social Media Accounts, T1585.002 Establish Accounts: Email Accounts, T1586 Compromise Accounts, T1593.002 Search Open Websites/Domains: Search Engines, T1656 Impersonation | 情報なし | 北米, 西欧, リモート採用を行うIT・ソフトウェア開発企業, 受託開発を行うWebエージェンシーとそのクライアント | 被害事例: NKITWエコシステムの内部運用実態(役割分担・身分偽装・RB Site／NetKey／OConnect)の解明 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 北米 | 原文は「The North Korean regime mobilizes thousands of skilled IT professionals to infiltrate organizations across North America and Western Europe」と明示しており、就労先として狙われる地域として記録する。 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
| regions | 西欧 | 原文は「... infiltrate organizations across North America and Western Europe」と明示しており、就労先として狙われる地域として記録する。フランス人を装ったNKITWがフランス向けの履歴書を用意する例、Webエージェンシーへ就労した例が記載されている。 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
| sectors | 金融 | 活動「偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--anyrun-it-workers-part-two-2026` |
| sectors | 暗号資産・DeFi | 研究者が設立した偽のDeFiスタートアップに応募・就労した事例。ANY.RUNはFamous Chollimaの狙いを、ソースコード、知的財産、業務プロセスへの長期的な接触と、給与の北朝鮮への還流であると記載している。 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| sectors | リモート採用を行うIT・ソフトウェア開発企業 | ANY.RUNは「Their goal is simple: get hired by Western companies」と記載し、リモート採用を通じて正規従業員として組織内部へ入り込むことを目的とすると評価している。 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026`, `source--flare-ibm-xforce-nkitw-2026` |
| sectors | 受託開発を行うWebエージェンシーとそのクライアント | 原文は「Web agencies that do contract work for multiple clients are a popular choice for NKITW to apply to」と記載し、エージェンシーへ就労したNKITWがエージェンシー自身に加えてそのクライアント環境(クライアント側の社用メール、Jira、SharePoint、Shopify、CRM)にもアカウントを付与された事例を示している。1件の就労が複数の顧客組織へ波及する構造として記録する。 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 偽DeFiスタートアップBallena Azul LTDへのITワーカー3名の採用と内部観測 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--4221b5fbb827488c6eaa, target--dprk-it-workers--sector--cryptocurrency, target--dprk-it-workers--sector--information-technology |  | ttp--dprk-it-workers-anyrun2-t1078, ttp--dprk-it-workers-anyrun2-t1090, ttp--dprk-it-workers-anyrun2-t1219, ttp--dprk-it-workers-anyrun2-t1585, ttp--dprk-it-workers-anyrun2-t1656 | VPN／リモートアクセス機器, 開発環境／ソースコード |  | 不明 | 不明 | 2026-08-10 | 高 | `source--anyrun-it-workers-part-two-2026` |
| 被害事例: NKITWエコシステムの内部運用実態(役割分担・身分偽装・RB Site／NetKey／OConnect)の解明 | 非公開 | aggregate | multiple-organizations | reported | target--dprk-it-workers--region--north-america, target--dprk-it-workers--region--western-europe, target--dprk-it-workers--sector--information-technology, target--dprk-it-workers--sector--web-agency |  | ttp--activity-rule--c8e6994beb392d81aac5, ttp--dprk-it-workers-flare-nkitw-t1078, ttp--dprk-it-workers-flare-nkitw-t1219, ttp--dprk-it-workers-flare-nkitw-t1583-003, ttp--dprk-it-workers-flare-nkitw-t1585-001, ttp--dprk-it-workers-flare-nkitw-t1585-002, ttp--dprk-it-workers-flare-nkitw-t1586, ttp--dprk-it-workers-flare-nkitw-t1593-002, ttp--dprk-it-workers-flare-nkitw-t1656 | メール／メールアカウント, VPN／リモートアクセス機器, サーバー, エンドポイント, 開発環境／ソースコード | data-theft: 原文はさらに、一部のチームがデータの持ち出しや恐喝、暗号資産の窃取にも関与すると記載している。 | 不明 | 不明 | 2026-03-18 | 高 | `source--flare-ibm-xforce-nkitw-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1219.002 | Remote Desktop Software | フルタイム就労では本人確認と給与振込が障壁となるため、LinkedInやGitHubで勧誘した西側協力者に薬物検査、バックグラウンドチェック、I-9書類、社給端末の受領、銀行・税務情報の提供を代行させ、協力者の実機へAnyDesk等でリモート接続して就労する。 |  | activity--dprk-it-workers-flare-xforce-nkitw-2026 | 不明 | 不明 | 中 | `source--flare-ibm-xforce-nkitw-2026` |
| Persistence | T1078 | Valid Accounts | 採用によって正規従業員として付与されたアカウントと権限を用い、短期的な侵入ではなく長期の内部滞在としてソースコード、知的財産、業務プロセスへ接触した。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Command and Control | T1090 | Proxy | AstrillVPNの出口ノードと北朝鮮が運用するVPSを経由して接続し、実際の所在地を秘匿した。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Command and Control | T1219 | Remote Access Tools | Google Remote DesktopおよびAnyDeskを用いて業務用のVDI環境へ接続した。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Resource Development | T1585 | Establish Accounts | 応募用の人物像とそれに紐づく口座・連絡手段を用意し、採用選考を通過できる体裁を整えた。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Defense Evasion | T1656 | Impersonation | 偽造または窃取した身分証明書、社会保障番号(SSN)、銀行口座を用いて別人になりすまし、Angelo Espree(スマートコントラクト開発者)、Jack Anderson(フロントエンド開発者)、Lucas Theo(バックエンド開発者)としてリモート職へ応募・採用された。偽装身分はテキサス、ニューヨーク、カリフォルニアの所在を主張していた。 |  | activity--dprk-it-workers-ballena-azul-2026 | 不明 | 不明 | 高 | `source--anyrun-it-workers-part-two-2026` |
| Persistence | T1078 | Valid Accounts | 採用後、雇用主から正規に付与されたアカウント(社用メール、Slack、Zoom、Teams、Jira、BambooHR)で業務を継続する。受託開発を行うWebエージェンシーへ就労した場合はエージェンシーのクライアント環境にもアカウント(クライアント側の社用メール、Jira、SharePoint、Shopify、CRM)が発行され、アクセス範囲がクライアントへ拡大する。 |  | activity--dprk-it-workers-flare-xforce-nkitw-2026 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
| Command And Control | T1219 | Remote Access Software | 西側協力者が所有する米国内の実機へリモートデスクトップ接続し、そこから求職・就労する。協力者が社給ノートPCを返送しに外出する際、AnyDeskのセッションを開いたまま離席した事例が記録されている。 |  | activity--dprk-it-workers-flare-xforce-nkitw-2026 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
| Resource Development | T1583.003 | Acquire Infrastructure: Virtual Private Server | 所在地を偽装するため、なりすます地域のIPアドレスを持つクラウド上の仮想マシンで作業する。1台を複数人で共有し、同時に複数の偽装身分を運用する場合がある。 |  | activity--dprk-it-workers-flare-xforce-nkitw-2026 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
| Resource Development | T1585.001 | Establish Accounts: Social Media Accounts | LinkedIn、GitHub、Upwork等へ偽の身分でプロフィールを作成する。GitHubでは空またはboilerplateのみのリポジトリ(「nextjs-app」「flutter-app」等)とfork、AI編集した顔写真で経歴を装う。「how to create fake commit activity on GitHub」「how to get fake Github badges」の検索痕跡が確認されている。集客用の作り込んだプロフィールと、就労後の実務専用の空のプロフィールを使い分ける。 |  | activity--dprk-it-workers-flare-xforce-nkitw-2026 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
| Resource Development | T1585.002 | Establish Accounts: Email Accounts | Protonmail等の本人確認要件が緩い事業者で捨てアドレスを作成し、これを二次確認用アドレスとしてGmailアカウントを取得する。 |  | activity--dprk-it-workers-flare-xforce-nkitw-2026 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
| Resource Development | T1586 | Compromise Accounts | フリーランス系プラットフォームは本人確認と入金口座の登録を求めるため、検証済みアカウントを違法フォーラムや個別ブローカーから購入する。playerpuff.comの投稿では既知のNKITWペルソナが利益分配を条件にアカウント購入を持ちかけていた。Upworkのアカウントブローカーと本人確認をめぐって係争になった記録も確認されている。 |  | activity--dprk-it-workers-flare-xforce-nkitw-2026 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
| Reconnaissance | T1593.002 | Search Open Websites/Domains: Search Engines | なりすます人物像に合わせるため、対象国のフリーランス求人プラットフォーム、対象地域の有名大学とIT企業、企業のメールアドレス書式をGoogleで検索し、履歴書と偽の前職照会状を作成する。求人検索向けGoogle Dorkの手順を記載した内部スライドがチームへ共有されていた。 |  | activity--dprk-it-workers-flare-xforce-nkitw-2026 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
| Defense Evasion | T1656 | Impersonation | 偽名、偽の職歴、偽の推薦状で応募する。西側協力者から提供・売却された実在人物の身元を用いる場合は、氏名と連絡先だけ本人のものとし職歴・照会先・学歴を偽装する。協力者は薬物検査の受検、パスポートや運転免許の取得、バックグラウンドチェックとI-9書類の通過、社給端末の受領、銀行・税務情報の提供を代行する。顔写真は逆画像検索を避けるためAI編集され、背景画像もAIツールで加工される。面接時は偽装身分の国籍に合わせたGoogle Voice番号を用いる。 |  | activity--dprk-it-workers-flare-xforce-nkitw-2026 | 不明 | 不明 | 高 | `source--flare-ibm-xforce-nkitw-2026` |
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
| source--anyrun-it-workers-part-two-2026 | Smile, You're on Camera! Part 2: Hiring Lazarus APT IT Workers at a Fake DeFi Startup | ANY.RUN | 2026-08-10 | https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation-part-two/ | primary-report | TLP:CLEAR | 高 |
| source--daily-10f083232dfd566dc4f9 | 北朝鮮（DPRK）リモートワーカー調査から得られた知見 | huntress.com | 2026-09-01 | https://www.huntress.com/blog/huntress-dprk-remote-worker-investigation | osint-report | TLP:CLEAR | 中 |
| source--dprk-it-workers--15da1b5bbfbc5250 | Smile, You’re on Camera  A Live Stream from Inside Lazarus Group’s IT Workers Scheme |  | 不明 | CyberMerceNary/ITWorker/Smile, You’re on Camera_ A Live Stream from Inside Lazarus Group’s IT Workers Scheme.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--769f09c40948bde0 | readme |  | 不明 | CyberMerceNary/ITWorker/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--dprk-it-workers--94775915798a421c | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--a08fdc503ef8f9a4 | JOINT CSA DPRK SOCIAL ENGINEERING |  | 不明 | CyberMerceNary/ITWorker/JOINT_CSA_DPRK_SOCIAL_ENGINEERING.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--b57b6250dea995f1 | DeceptiveDevelopment and North Korean IT workers from primitive crypto theft to sophisticated AI based deception |  | 不明 | CyberMerceNary/ITWorker/DeceptiveDevelopment-and-North-Korean-IT-workers-from-primitive-crypto-theft-to-sophisticated-AI-based-deception.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--bc62b8e29937a263 | Inside the ScamNorth Korea’s IT Worker Threat |  | 不明 | CyberMerceNary/ITWorker/Inside the ScamNorth Korea’s IT Worker Threat.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--e7356e8e649de477 | OFSI Advisory on North Korean IT Workers |  | 不明 | CyberMerceNary/ITWorker/OFSI_Advisory_on_North_Korean_IT_Workers.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--eb29460df938ef81 | north korean scammers are posing as it freelancers here's how you can protect your business |  | 不明 | CyberMerceNary/ITWorker/north-korean-scammers-are-posing-as-it-freelancers_-here's-how-you-can-protect-your-business.pdf | report | TLP:CLEAR | 中 |
| source--flare-ibm-xforce-nkitw-2026 | Inside the North Korean Infiltrator Threat | Flare Research and IBM X-Force | 2026-03-18T13:00:34Z | https://flare.io/learn/resources/north-korean-infiltrator-threat | primary-report | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
