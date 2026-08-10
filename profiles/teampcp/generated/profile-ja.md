# TeamPCP 脅威アクタープロファイル

- プロファイルID: `actor--teampcp`
- 状態: draft
- 更新日時: 2026-08-10T07:33:16Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

TeamPCP(GTIG命名 UNC6780)は金銭目的のサイバー犯罪グループで、インターネットへ露出したRay、Docker、Redis、React環境をワーム型に侵害し、2026年にはGitHub ActionsとPyPIを経由するオープンソースサプライチェーン攻撃へ拡大した。Oligo Securityは基盤の連続性から活動を2020年まで遡及している。

## アクター名とAlias

- 正規名: **TeamPCP**
- 初回観測: 2020
- 最終観測: 2026-04
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| UNC6780 | Google Threat Intelligence Group | exact | 高 | `source--gtig-ai-threat-tracker-2026-05` | GTIGが「the cyber crime threat actor "TeamPCP" (aka UNC6780)」と同一主体として明記している。 |
| TA-NATALSTATUS |  | overlapping | 中 | `source--oligo-teampcp-2026` | Oligoは以前TA-NATALSTATUSとして追跡されたキャンペーンがTeamPCPと連続すると評価するが、同一運用者・密接な協力・基盤共有のいずれかまでは断定していないためexactへ強めない。 |
| IronErn |  | overlapping | 中 | `source--oligo-teampcp-2026` | GitLabアカウント運用の重複を根拠とする関連であり、同一クラスタの確定ではない。 |
| PCPCat | SentinelOne (SentinelLabs) | unknown | 低 | `source--sentinellabs-pcpjack-2026` | SentinelLabsが「early TeamPCP/PCPCat campaigns」と併記するが、対応関係の説明がないためスコープ不明として保持する。 |

## 帰属

一次資料は国家帰属を示していない。金銭目的のサイバー犯罪グループとして扱う。インフラ所在国を帰属国へ流用しない。

- 国: 不明
- スポンサー種別: criminal
- 確度: 中
- 証拠: `source--oligo-teampcp-2026`, `source--gtig-ai-threat-tracker-2026-05`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial | 資格情報・決済情報の窃取、ランサムウェア展開、恐喝グループとの提携による収益化。 | 高 | `source--oligo-teampcp-2026`, `source--sentinellabs-pcpjack-2026` |  |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | 金銭目的を公称するサイバー犯罪グループTeamPCP(GTIG命名 UNC6780)。国家帰属は不明。 |
| Capability | 露出サービスの自動探索とワーム型侵害、ShadowRay 2.0ペイロード、SANDCLOCK資格情報スティーラー、ランサムウェア、フィッシングページ。 |
| Infrastructure | masscan.cloudとnatalstatus.orgを中心とするドメイン群、/EP9ts2/や/files/という特徴的な配置パス、複数のC2 IP。 |
| Victim | インターネットへ露出したクラウド・AI基盤の運用組織、およびTrivy、Checkmarx、LiteLLM、BerriAIなどのオープンソースプロジェクト。 |
| Socio-political | 収益化のためランサムウェア・データ恐喝グループと提携する犯罪エコシステム。 |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-08-10T07:33:16Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-2999 | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | TeamPCP | canonical-name | 高 |  | https://www.trendmicro.com/en_us/research/26/c/teampcp-telnyx-attack-marks-a-shift-in-tactics.html<br>https://www.trendmicro.com/en_us/research/26/c/inside-litellm-supply-chain-compromise.html<br>https://tracebit.com/blog/detecting-cicd-supply-chain-attacks-with-canary-credentials |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--sandclock | SANDCLOCK | ビルド環境からAWSキーとGitHubトークンを窃取する資格情報スティーラー。侵害したGitHub Actionsワークフローへ埋め込まれる。 | 2026-02 | 不明 | 高 | `source--gtig-ai-threat-tracker-2026-05` |
| malware--shadowray-2-0-payloads | ShadowRay 2.0 ペイロード | 侵害したRay等のAI基盤を自己増殖型ボットネット化するペイロード群。第1段階はndt.shなどのシェルスクリプトで、リバースシェルと追加バイナリを取得する。 | 2025-06 | 不明 | 高 | `source--oligo-teampcp-2026` |

### ツール

未確認

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infra--masscan-cloud | masscan.cloud / natalstatus.org 基盤 | TA-NATALSTATUS、ShadowRay 2.0、TeamPCPの各キャンペーンで再利用された中核基盤。auth、checkout、pay、mail、testなどのサブドメインが資格情報・決済フィッシングとインフラ試験に使われ、pcp.masscan.cloudはTeamPCPのTelegramチャンネルへ誘導していた。 | 2020 | 2026-04 | 高 | `source--oligo-teampcp-2026` |

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--malicious-pypi-package | 侵害済みPyPIパッケージ | 初期アクセス経路として使用される汚染されたPyPIパッケージ。 | 不明 | 不明 | 高 | `source--gtig-ai-threat-tracker-2026-05` |
| delivery--malicious-pull-request | 悪意あるプルリクエスト | オープンソースリポジトリへの悪意あるプルリクエストを起点に権限を得る。 | 不明 | 不明 | 高 | `source--gtig-ai-threat-tracker-2026-05` |

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--worm-style-mass-exploitation | ワーム型の大量侵害 | 露出サービスを自動探索し、侵害先から次の対象へ自己増殖的に拡散する。 | 不明 | 不明 | 高 | `source--oligo-teampcp-2026` |
| opcap--ransomware-partnership | 恐喝グループとの提携 | 窃取した資格情報とデータをランサムウェア・データ恐喝グループとの提携で収益化する。SentinelLabsはVECTランサムウェアグループとの提携表明を記載している。 | 不明 | 不明 | 高 | `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |
| opcap--long-term-reverse-shell | 長期的なリバースシェル維持 | 侵害したRayクラスタへ長期間リバースシェルを維持する。 | 不明 | 不明 | 高 | `source--oligo-teampcp-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 新たなインテリジェンスがTeamPCPとShadowRay 2.0を関連付け、活動を2020年まで遡及 | infrastructure-operation | 2020 | 2026-04 | 2026-08-08 |  |  | ttp--teampcp-t1059-004-ndt-sh, ttp--teampcp-t1190-exposed-services, ttp--teampcp-t1486-ransomware | victim--activity-rule--829e65b1ac18ce5ea420, victim--teampcp-exposed-cloud-services | Oligo Securityは、ShadowRay 2.0でAI基盤を自己増殖型ボットネット化した攻撃主体をTeamPCPと評価し、活動を少なくとも2020年まで遡った。 TA-NATALSTATUS、IronErn、TeamPCPの間でドメイン、C2、マルウェア配置パス、ステージング手法などが重複し、継続的な運用基盤が確認された。 攻撃者はRay、Docker、Redis、Reactなどの公開サービスを自動・ワーム型で侵害し、2026年にはGitHubやGitLabを狙うサプライチェーン攻撃へ拡大した。 2025年には侵害したRayクラスタへ長期間リバースシェルを維持し、GitLabのIronErn関連アカウントも同一IPから管理されていた。 OligoはTeamPCPを既存活動の継続または再ブランドと評価するが、同一運用者、密接な協力関係、共有基盤のどれかまでは断定していない。 | 高 | `source--daily-48f251212f832ab9b6df` |
| GitHub Actions・PyPIを経由したオープンソースサプライチェーン侵害 | supply-chain-cybercrime | 2026-02 | 2026-03 | 2026-05-11 |  | malware--sandclock | ttp--teampcp-t1195-002-oss-supply-chain, ttp--teampcp-t1552-001-build-secrets | victim--activity-rule--36589755fc4094ee8555, victim--teampcp-oss-projects-2026 | TeamPCPはGitHubリポジトリと関連するGitHub Actionsを侵害し、Trivy脆弱性スキャナー、Checkmarx、LiteLLM、BerriAIを含む複数のサプライチェーン侵害に関与したと表明した。初期アクセスは侵害済みPyPIパッケージと悪意あるプルリクエストを経由し、ビルド環境からAWSキーとGitHubトークンを窃取するSANDCLOCK資格情報スティーラーを埋め込んだ。窃取した資格情報はランサムウェアやデータ恐喝グループとの提携で収益化されている。 | 高 | `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 新たなインテリジェンスがTeamPCPとShadowRay 2.0を関連付け、活動を2020年まで遡及 | TeamPCP | ShadowRay 2.0 ペイロード | T1059.004 Unix Shell, T1190 Exploit Public-Facing Application, T1486 Data Encrypted for Impact | masscan.cloud / natalstatus.org 基盤 | 情報なし | 被害事例: 新たなインテリジェンスがTeamPCPとShadowRay 2.0を関連付け、活動を2020年まで遡及, インターネットへ露出したRay/Docker/Redis/React環境(集約) | 高 |
| GitHub Actions・PyPIを経由したオープンソースサプライチェーン侵害 | TeamPCP | SANDCLOCK | T1195.002 Compromise Software Supply Chain, T1552.001 Credentials In Files | masscan.cloud / natalstatus.org 基盤 | 情報なし | 被害事例: GitHub Actions・PyPIを経由したオープンソースサプライチェーン侵害, Trivy / Checkmarx / LiteLLM / BerriAI | 高 |

2025年後半にTeamPCPとして公然化した。2026年2月から3月にかけてTrivy、Checkmarx、LiteLLM、BerriAIのサプライチェーン侵害に関与したと表明し、2026年8月にOligoがTA-NATALSTATUSおよびIronErnとの連続性と2020年までの遡及を報告した。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 全世界 | 一次資料は特定国を標的条件として挙げず、インターネットへ露出したサービスとオープンソース配布網を対象としている。 | 不明 | 不明 | 中 | `source--oligo-teampcp-2026`, `source--gtig-ai-threat-tracker-2026-05` |
| sectors | クラウド・AI基盤運用 | Ray、Kubernetes、Docker、Redisなどの運用環境が侵害対象として明示されている。 | 不明 | 不明 | 高 | `source--oligo-teampcp-2026`, `source--sentinellabs-pcpjack-2026` |
| sectors | フィンテック | Oligo資料がフィンテックアプリケーションを標的技術・分野として挙げている。 | 不明 | 不明 | 中 | `source--oligo-teampcp-2026` |
| sectors | オープンソースソフトウェア | Trivy、Checkmarx、LiteLLM、BerriAIなどの配布網が侵害対象として明示されている。 | 不明 | 不明 | 高 | `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |

選定ロジック: 国や産業ではなく、インターネットへ露出した特定技術スタックの有無で対象を選定する。サプライチェーン段階では、広く利用される開発・セキュリティツールを選定している。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: GitHub Actions・PyPIを経由したオープンソースサプライチェーン侵害 | 非公開 | aggregate | multiple-organizations | reported |  | malware--sandclock | ttp--teampcp-t1195-002-oss-supply-chain, ttp--teampcp-t1552-001-build-secrets | エンドポイント, クラウド／SaaS, 開発環境／ソースコード | credential-theft: 初期アクセスは侵害済みPyPIパッケージと悪意あるプルリクエストを経由し、ビルド環境からAWSキーとGitHubトークンを窃取するSANDCLOCK資格情報スティーラーを埋め込んだ。<br>encryption: 窃取した資格情報はランサムウェアやデータ恐喝グループとの提携で収益化されている。 | 2026-02 | 2026-03 | 2026-05-11 | 高 | `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |
| 被害事例: 新たなインテリジェンスがTeamPCPとShadowRay 2.0を関連付け、活動を2020年まで遡及 | 非公開 | anonymous | unknown | reported |  |  | ttp--teampcp-t1059-004-ndt-sh, ttp--teampcp-t1190-exposed-services, ttp--teampcp-t1486-ransomware | エンドポイント, 開発環境／ソースコード | supply-chain: 攻撃者はRay、Docker、Redis、Reactなどの公開サービスを自動・ワーム型で侵害し、2026年にはGitHubやGitLabを狙うサプライチェーン攻撃へ拡大した。 | 2020 | 2026-04 | 2026-08-08 | 高 | `source--daily-48f251212f832ab9b6df` |
| インターネットへ露出したRay/Docker/Redis/React環境(集約) | 非公開 | aggregate | multiple-organizations | reported |  | malware--shadowray-2-0-payloads | ttp--teampcp-t1190-exposed-services, ttp--teampcp-t1059-004-ndt-sh | Rayクラスタ, Redisサーバー, Dockerホスト, Kubernetes環境 | account-compromise: 侵害環境へのリバースシェルによる長期的な支配。<br>credential-theft: クラウド資格情報の窃取。<br>encryption: ランサムウェア展開による暗号化。 | 2020 | 2026-04 | 2026-08-05 | 高 | `source--oligo-teampcp-2026` |
| Trivy、Checkmarx、LiteLLM、BerriAI | Trivy / Checkmarx / LiteLLM / BerriAI | named | multiple-organizations | reported |  | malware--sandclock | ttp--teampcp-t1195-002-oss-supply-chain, ttp--teampcp-t1552-001-build-secrets | GitHubリポジトリ, GitHub Actionsワークフロー, PyPIパッケージ | supply-chain: オープンソース配布物とCIワークフローの汚染。<br>credential-theft: ビルド環境からのAWSキーとGitHubトークンの窃取。 | 2026-02 | 2026-03 | 2026-05-11 | 中 | `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.004 | Unix Shell | 侵害したRayクラスタへ第1段階シェルスクリプトndt.shを配信して実行し、リバースシェルと追加ペイロードを取得する。 |  | activity--daily-5aa545c901df820c7aa2 | 2025-06 | 不明 | 高 | `source--oligo-teampcp-2026` |
| Initial Access | T1190 | Exploit Public-Facing Application | Ray、Docker、Redis、Reactなどインターネットへ露出したサービスを自動・ワーム型で侵害する。 |  | activity--daily-5aa545c901df820c7aa2 | 2020 | 2026-04 | 高 | `source--oligo-teampcp-2026` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | 侵害済みPyPIパッケージと悪意あるプルリクエストを起点にGitHubリポジトリとGitHub Actionsを侵害し、配布物へ悪性コードを埋め込む。 |  | activity--teampcp-oss-supply-chain-2026 | 2026-02 | 2026-03 | 高 | `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |
| Impact | T1486 | Data Encrypted for Impact | 侵害したクラウド環境でランサムウェアを展開し、恐喝グループとの提携で収益化する。 |  | activity--daily-5aa545c901df820c7aa2 | 不明 | 不明 | 高 | `source--oligo-teampcp-2026`, `source--sentinellabs-pcpjack-2026` |
| Credential Access | T1552.001 | Credentials In Files | SANDCLOCK資格情報スティーラーをビルド環境へ埋め込み、AWSキーとGitHubトークンを窃取する。 | malware--sandclock | activity--teampcp-oss-supply-chain-2026 | 2026-02 | 不明 | 高 | `source--gtig-ai-threat-tracker-2026-05` |

## IOC／artifact概要

- IOC値: 23件
- IOC観測: 23件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| TeamPCPは金銭目的のサイバー犯罪グループであり、露出サービスの大量侵害とオープンソースサプライチェーン攻撃を併用する。 | 高 | `source--oligo-teampcp-2026`, `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |  |
| TeamPCPの運用はTA-NATALSTATUSおよびIronErnとして追跡された活動と基盤・配置パス・アカウント運用の面で連続している。 | 中 | `source--oligo-teampcp-2026` | Oligoは同一運用者と断定していない。 |
| UNC6780はGoogle Threat Intelligence GroupによるTeamPCPの別称である。 | 高 | `source--gtig-ai-threat-tracker-2026-05` |  |

### 情報ギャップ

- 個別IOCとマルウェアファミリー名の対応が一次資料で明示されていない。
- 運用者の所在国・言語圏を示す一次資料を未取得。
- 2020年から2025年の間の個別キャンペーンを裏付ける独立資料が不足している。

### 不確実性

- Trivy侵害の時期はSentinelLabsが2026年2月、GTIGが2026年3月下旬の犯行表明としており、侵害日と表明日のどちらを指すかで記述が異なる。両論を残す。
- PCPCatとTeamPCPの対応関係が一次資料で説明されていない。
- tech-memoのIOC CSVでShai-HuludのIOCにactor=TeamPCPが付与されているが、この帰属は一次資料で確認できていないため本プロファイルへ取り込んでいない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--daily-48f251212f832ab9b6df | 新たなインテリジェンスがTeamPCPとShadowRay 2.0を関連付け、活動を2020年まで遡及 | oligo.security | 2026-08-08 | https://www.oligo.security/blog/new-intelligence-links-teampcp-to-shadowray-2-0-and-traces-activity-back-to-2020 | osint-report | TLP:CLEAR | 中 |
| source--gtig-ai-threat-tracker-2026-05 | GTIG AI Threat Tracker: Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access | Google Threat Intelligence Group | 2026-05-11 | https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access | vendor-research-report | TLP:CLEAR | 高 |
| source--oligo-teampcp-2026 | New Intelligence Links TeamPCP to ShadowRay 2.0 and Traces Activity Back to 2020 | Oligo Security | 2026-08-05 | https://www.oligo.security/blog/new-intelligence-links-teampcp-to-shadowray-2-0-and-traces-activity-back-to-2020 | vendor-research-report | TLP:CLEAR | 高 |
| source--sentinellabs-pcpjack-2026 | PCPJack \| Cloud Worm Evicts TeamPCP and Steals Credentials at Scale | SentinelOne (SentinelLabs) | 2026-05-07 | https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/ | vendor-research-report | TLP:CLEAR | 高 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

本プロファイルは2026-08-10の日次更新チェックで未一致名として検知され、独立一次資料3本の確認後に昇格した。status: draftから開始する。
