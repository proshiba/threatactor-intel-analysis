# TeamPCP 脅威アクタープロファイル

- プロファイルID: `actor--teampcp`
- 状態: draft
- 更新日時: 2026-09-21T04:18:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

TeamPCP(GTIG命名 UNC6780)は金銭目的のサイバー犯罪グループで、インターネットへ露出したRay、Docker、Redis、React環境をワーム型に侵害し、2026年にはGitHub ActionsとPyPIを経由するオープンソースサプライチェーン攻撃へ拡大した。Oligo Securityは基盤の連続性から活動を2020年まで遡及している。

## アクター名とAlias

- 正規名: **TeamPCP**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DeadCatx3 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2`, `source--mitre-attack-g1056` | Official MITRE ATT&CK associated-group name for G1056. |
| IronErn |  | overlapping | 中 | `source--oligo-teampcp-2026` | GitLabアカウント運用の重複を根拠とする関連であり、同一クラスタの確定ではない。 |
| PCPCat | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2`, `source--mitre-attack-g1056` | MITRE ATT&CK lists PCPCat as an Associated Group for G1056. ATT&CK explicitly treats associated names as overlap signals rather than exact equivalence, so this alias remains overlapping. |
| SHADOW-WATER-058 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2`, `source--mitre-attack-g1056` | Official MITRE ATT&CK associated-group name for G1056. |
| ShellForce | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2`, `source--mitre-attack-g1056` | Official MITRE ATT&CK associated-group name for G1056. |
| TA-NATALSTATUS |  | overlapping | 中 | `source--oligo-teampcp-2026` | Oligoは以前TA-NATALSTATUSとして追跡されたキャンペーンがTeamPCPと連続すると評価するが、同一運用者・密接な協力・基盤共有のいずれかまでは断定していないためexactへ強めない。 |
| UNC6780 | MITRE ATT&CK | exact | 高 | `source--mitre-attack-g1056` | GTIGが「the cyber crime threat actor "TeamPCP" (aka UNC6780)」と同一主体として明記している。 Official MITRE ATT&CK associated-group name for G1056. |

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
| financial-gain | Financially motivated intrusion or fraud. | 高 | `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description. |

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
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-2999 | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | TeamPCP | canonical-name | 高 |  | https://www.trendmicro.com/en_us/research/26/c/teampcp-telnyx-attack-marks-a-shift-in-tactics.html<br>https://www.trendmicro.com/en_us/research/26/c/inside-litellm-supply-chain-compromise.html<br>https://tracebit.com/blog/detecting-cicd-supply-chain-attacks-with-canary-credentials |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | TeamPCP - G1056 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1056<br>https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access<br>https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23 |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

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
| malware--canisterworm | CanisterWorm | [CanisterWorm](https://attack.mitre.org/software/S9042) is a self-propagating malware that has been used by [TeamPCP](https://attack.mitre.org/groups/G1056) in credential harvesting and software supply chain campaigns since at least 2026. [CanisterWorm](https://attack.mitre.org/software/S9042) has used npm credentials to infect software packages and propagate across developer ecosystems. [CanisterWorm](https://attack.mitre.org/software/S9042) has a targeted wiper component and can use decentralized C2 infrastructure implemented via an Internet Computer Protocol (ICP) blockchain canister.(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Aikido CanisterWorm MAR 2026)(Citation: Aikido TeamPCP Trivy MAR 2026) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--dustmaker | DUSTMAKER | UNC6780(TeamPCP)が用いる資格情報スティーラー。CI/CD環境で動作していることを検知するとGitHub ActionsランナーのプロセスメモリからOIDCトークンを抽出し、そのトークンでtrusted publisherとして自らを認可して、有効なSLSA Build 3の署名付き証明を伴う改ざん版パッケージを公開する。正当な署名を持つため、AIコーディングエージェントの自動信頼チェックを通過する。AIツール向けの資格情報収集や、隠しディレクトリによる防御回避を含む複数のAI関連機能を実装する。 | 不明 | 不明 | 高 | `source--gtig-adversarial-ai-2026` |
| malware--mini-shai-hulud | Mini Shai-Hulud | [Mini Shai-Hulud](https://attack.mitre.org/software/S9043) is a credential stealer and self-replicating supply chain worm, derived from [Shai-Hulud](https://attack.mitre.org/software/S9008), that has been used by [TeamPCP](https://attack.mitre.org/groups/G1056) to target Continuous Integration and Continuous Delivery/Deployment (CI/CD) workflows since at least 2026. [Mini Shai-Hulud](https://attack.mitre.org/software/S9043) can compromise credentials across multiple cloud, container, and AI configuration file paths and can use stolen npm and GitHub OIDC tokens to spread to other packages maintained by the compromised user.  [Mini Shai-Hulud](https://attack.mitre.org/software/S9043) also has a targeted wiper component and has used multiple C2 and data exfiltration mechanisms.(Citation: Wiz Mini Shai-Hulud MAY 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Hunt.io TeamPCP Toolkit MAY 2026)(Citation: Phoenix TeamPCP 20 MAY 2026)(Citation: Flashpoint Mini Shai-Hulud MAY 2026)(Citation: FBI TeamPCP JUL 2026) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--sandclock | SANDCLOCK | ビルド環境からAWSキーとGitHubトークンを窃取する資格情報スティーラー。侵害したGitHub Actionsワークフローへ埋め込まれる。 | 2026-02 | 不明 | 高 | `source--gtig-ai-threat-tracker-2026-05` |
| malware--shadowray-2-0-payloads | ShadowRay 2.0 ペイロード | 侵害したRay等のAI基盤を自己増殖型ボットネット化するペイロード群。第1段階はndt.shなどのシェルスクリプトで、リバースシェルと追加バイナリを取得する。 | 2025-06 | 不明 | 高 | `source--oligo-teampcp-2026` |
| malware--teampcp-cloud-stealer | TeamPCP Cloud Stealer | The [TeamPCP Cloud Stealer](https://attack.mitre.org/software/S9041) is a comprehensive filesystem credential stealer that can harvest, encrypt, and exfiltrate credentials from over 50 sensitive file paths across CI/CD, cloud, developer tooling, and container environments. The [TeamPCP Cloud Stealer](https://attack.mitre.org/software/S9041) was the primary payload used by [TeamPCP](https://attack.mitre.org/groups/G1056) in March 2026 during early stages of a cascading supply chain campaign targeting CI/CD workflows.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Trivy Compromise MAR 2026)(Citation: Aqua Security Blog Trivy Compromise APR 2026)(Citation: Sysdig TeamPCP MAR 2026)(Citation: Wiz TeamPCP KICS MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Google AI Threat Tracker MAY 2026)(Citation: FBI TeamPCP JUL 2026) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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
| GitHub Actions・PyPI・npm・Docker Hubを経由したオープンソースサプライチェーン侵害 | supply-chain-cybercrime | 2026-02 | 2026-03 | 2026-05-11 | target--activity-rule--sector--932f4928d5e1ec28e2df | malware--dustmaker, malware--sandclock, malware--teampcp-cloud-stealer | ttp--teampcp-t1195-002-oss-supply-chain, ttp--teampcp-t1552-001-build-secrets | victim--activity-rule--36589755fc4094ee8555, victim--teampcp-oss-projects-2026 | TeamPCPはGitHubリポジトリと関連するGitHub Actionsを侵害し、Trivy脆弱性スキャナー、Checkmarx、LiteLLM、BerriAIを含む複数のサプライチェーン侵害に関与したと表明した。初期アクセスは侵害済みPyPIパッケージと悪意あるプルリクエストを経由し、ビルド環境からAWSキーとGitHubトークンを窃取するSANDCLOCK資格情報スティーラーを埋め込んだ。窃取した資格情報はランサムウェアやデータ恐喝グループとの提携で収益化されている。GTIGの後継報告(2026-09-08)は、2026年3月以降も大規模なOSSサプライチェーン侵害が継続し、対象エコシステムがPyPIに加えnpmとDocker Hubへ広がったと記載する。侵害後は資格情報スティーラーを展開して専有データと資格情報を取得し、データの直接売却またはランサムウェア・データ恐喝グループとの提携により収益化する。AIコーディングアシスタントを標的とする手口として、侵害した正規の開発者アカウントからPyPIへ正規MCPサーバーのトロイの木馬化フォーク(tiktoken_mcp等)を公開し、公式の組織GitHubリポジトリ(azure-functions-mcp-extension等)へ悪性コードを直接注入した。これらMCPツールと連携部分をバックドア化することで、資産がダウンロードまたはクローンされる際にペイロードと悪性ワークスペースフックが開発環境へ自動的に取り込まれる。資格情報スティーラーDUSTMAKERはCI/CD環境を検知するとGitHub Actionsランナーのプロセスメモリからoidcトークンを抽出し、trusted publisherとして有効なSLSA Build 3署名付き証明を伴う改ざん版パッケージを公開するため、AIコーディングエージェントの自動信頼チェックを通過する。Mandiantが対応した事案では、TeamPCPが初期アクセスを確立した後に別の脅威アクターへアクセスを引き渡し、引き渡し先がLAPSUSブランドを用いて身代金を要求した。TeamPCPが当該企業の専有AIリポジトリに対して悪性のGitHub Actionsワークフローを作成し、恐喝側がそのAIリポジトリの複製を持ち出した証跡が示されている。 | 高 | `source--gtig-adversarial-ai-2026`, `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 新たなインテリジェンスがTeamPCPとShadowRay 2.0を関連付け、活動を2020年まで遡及 | TeamPCP | ShadowRay 2.0 ペイロード | T1059.004 Unix Shell, T1190 Exploit Public-Facing Application, T1486 Data Encrypted for Impact | masscan.cloud / natalstatus.org 基盤 | 情報なし | 被害事例: 新たなインテリジェンスがTeamPCPとShadowRay 2.0を関連付け、活動を2020年まで遡及, インターネットへ露出したRay/Docker/Redis/React環境(集約) | 高 |
| GitHub Actions・PyPI・npm・Docker Hubを経由したオープンソースサプライチェーン侵害 | TeamPCP | DUSTMAKER, SANDCLOCK, TeamPCP Cloud Stealer | T1195.002 Compromise Software Supply Chain, T1552.001 Credentials In Files | masscan.cloud / natalstatus.org 基盤 | IT・ソフトウェア | 被害事例: GitHub Actions・PyPI・npm・Docker Hubを経由したオープンソースサプライチェーン侵害, Trivy / Checkmarx / LiteLLM / BerriAI | 高 |

2025年後半にTeamPCPとして公然化した。2026年2月から3月にかけてTrivy、Checkmarx、LiteLLM、BerriAIのサプライチェーン侵害に関与したと表明し、2026年8月にOligoがTA-NATALSTATUSおよびIronErnとの連続性と2020年までの遡及を報告した。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 全世界 | 一次資料は特定国を標的条件として挙げず、インターネットへ露出したサービスとオープンソース配布網を対象としている。 | 不明 | 不明 | 中 | `source--oligo-teampcp-2026`, `source--gtig-ai-threat-tracker-2026-05` |
| sectors | IT・ソフトウェア | 活動「GitHub Actions・PyPI・npm・Docker Hubを経由したオープンソースサプライチェーン侵害」の記述で標的として明示された産業。 | 2026-02 | 2026-03 | 中 | `source--gtig-adversarial-ai-2026`, `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |
| sectors | 暗号資産・Web3 | Initially focused on ransomware and cryptocurrency theft, [TeamPCP](https://attack.mitre.org/groups/G1056) shifted in early 2026 to systematic, worm-driven credential theft and software supply chain attacks targeting Continuous Integration and Continuous Delivery (CI/CD) workflows. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | クラウド・AI基盤運用 | Ray、Kubernetes、Docker、Redisなどの運用環境が侵害対象として明示されている。 | 不明 | 不明 | 高 | `source--oligo-teampcp-2026`, `source--sentinellabs-pcpjack-2026` |
| sectors | フィンテック | Oligo資料がフィンテックアプリケーションを標的技術・分野として挙げている。 | 不明 | 不明 | 中 | `source--oligo-teampcp-2026` |
| sectors | オープンソースソフトウェア | Trivy、Checkmarx、LiteLLM、BerriAIなどの配布網が侵害対象として明示されている。 | 不明 | 不明 | 高 | `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |

選定ロジック: 国や産業ではなく、インターネットへ露出した特定技術スタックの有無で対象を選定する。サプライチェーン段階では、広く利用される開発・セキュリティツールを選定している。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: GitHub Actions・PyPI・npm・Docker Hubを経由したオープンソースサプライチェーン侵害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--932f4928d5e1ec28e2df | malware--dustmaker, malware--sandclock, malware--teampcp-cloud-stealer | ttp--teampcp-t1195-002-oss-supply-chain, ttp--teampcp-t1552-001-build-secrets | サーバー, エンドポイント, クラウド／SaaS, 開発環境／ソースコード | credential-theft: 初期アクセスは侵害済みPyPIパッケージと悪意あるプルリクエストを経由し、ビルド環境からAWSキーとGitHubトークンを窃取するSANDCLOCK資格情報スティーラーを埋め込んだ。<br>encryption: 窃取した資格情報はランサムウェアやデータ恐喝グループとの提携で収益化されている。 | 2026-02 | 2026-03 | 2026-05-11 | 高 | `source--gtig-adversarial-ai-2026`, `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |
| 被害事例: 新たなインテリジェンスがTeamPCPとShadowRay 2.0を関連付け、活動を2020年まで遡及 | 非公開 | anonymous | unknown | reported |  |  | ttp--teampcp-t1059-004-ndt-sh, ttp--teampcp-t1190-exposed-services, ttp--teampcp-t1486-ransomware | エンドポイント, 開発環境／ソースコード | supply-chain: 攻撃者はRay、Docker、Redis、Reactなどの公開サービスを自動・ワーム型で侵害し、2026年にはGitHubやGitLabを狙うサプライチェーン攻撃へ拡大した。 | 2020 | 2026-04 | 2026-08-08 | 高 | `source--daily-48f251212f832ab9b6df` |
| インターネットへ露出したRay/Docker/Redis/React環境(集約) | 非公開 | aggregate | multiple-organizations | reported |  | malware--shadowray-2-0-payloads | ttp--teampcp-t1190-exposed-services, ttp--teampcp-t1059-004-ndt-sh | Rayクラスタ, Redisサーバー, Dockerホスト, Kubernetes環境 | account-compromise: 侵害環境へのリバースシェルによる長期的な支配。<br>credential-theft: クラウド資格情報の窃取。<br>encryption: ランサムウェア展開による暗号化。 | 2020 | 2026-04 | 2026-08-05 | 高 | `source--oligo-teampcp-2026` |
| Trivy、Checkmarx、LiteLLM、BerriAI | Trivy / Checkmarx / LiteLLM / BerriAI | named | multiple-organizations | reported |  | malware--sandclock | ttp--teampcp-t1195-002-oss-supply-chain, ttp--teampcp-t1552-001-build-secrets | GitHubリポジトリ, GitHub Actionsワークフロー, PyPIパッケージ | supply-chain: オープンソース配布物とCIワークフローの汚染。<br>credential-theft: ビルド環境からのAWSキーとGitHubトークンの窃取。 | 2026-02 | 2026-03 | 2026-05-11 | 中 | `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | [TeamPCP](https://attack.mitre.org/groups/G1056) has stolen source code from victim environments including Mistral AI.(Citation: Flashpoint Mini Shai-Hulud MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1027.003 | Steganography | [TeamPCP](https://attack.mitre.org/groups/G1056) has hidden malicious payloads in the frame data of WAV audio files.(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [TeamPCP](https://attack.mitre.org/groups/G1056) has cloned GitHub commit metadata including the author name, email, committer, and timestamps to use for impostor commits.(Citation: Aqua Security Blog Trivy Compromise APR 2026) [TeamPCP](https://attack.mitre.org/groups/G1056) has also used legitimate file names such as msbuild.exe and ringtone.wav to mask malicious payloads.(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.004 | Unix Shell | [TeamPCP](https://attack.mitre.org/groups/G1056) has leveraged malware capable of execution via the Linux CLI.(Citation: Hunt.io TeamPCP Toolkit MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.006 | Python | [TeamPCP](https://attack.mitre.org/groups/G1056) has poisoned PyPi packages with malicious code and has used a 13 file modular Python framework for data collection.(Citation: Hunt.io TeamPCP Toolkit MAY 2026)(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Hunt.io TeamPCP Toolkit MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.007 | JavaScript | [TeamPCP](https://attack.mitre.org/groups/G1056) has used the JavaScript runtime for malware delivery and injected malicious JavaScript into OpenVSX extensions.(Citation: Wiz TeamPCP KICS MAR 2026)(Citation: Trend Micro TeamPCP MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.013 | Container CLI/API | [TeamPCP](https://attack.mitre.org/groups/G1056) has queried the Kubernetes API for local service account tokens and has used  `kubectl` for lateral movement.(Citation: Phoenix TeamPCP 20 MAY 2026)(Citation: Wiz TeamPCP KICS MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [TeamPCP](https://attack.mitre.org/groups/G1056) has compromised credentials associated with open source security scanning tools and used them to push malicious code to all the resources the tools had access to.(Citation: Aikido TeamPCP Telnyx MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.004 | Cloud Accounts | [TeamPCP](https://attack.mitre.org/groups/G1056) has used compromised credentials for GitHub and software package repositories, including privileged service accounts, to inject malicious code into CI/CD pipelines.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Trivy Compromise MAR 2026)(Citation: Aqua Security Blog Trivy Compromise APR 2026)(Citation: Wiz TeamPCP KICS MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Wiz Mini Shai-Hulud MAY 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Phoenix TeamPCP 20 MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1098 | Account Manipulation | [TeamPCP](https://attack.mitre.org/groups/G1056) has modified settings to publish private Aqua Security repositories to GitHub as public.(Citation: Aqua Security Blog Trivy Compromise APR 2026)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [TeamPCP](https://attack.mitre.org/groups/G1056) has modified legitimate software binaries to retrieve secondary payloads from C2.(Citation: Wiz TeamPCP KICS MAR 2026)(Citation: Aikido TeamPCP Telnyx MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence | T1176.002 | IDE Extensions | [TeamPCP](https://attack.mitre.org/groups/G1056) has compromised VS Code and Open VSX IDE extensions.(Citation: Wiz TeamPCP KICS MAR 2026)(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Phoenix TeamPCP 20 MAY 2026)(Citation: Flashpoint Mini Shai-Hulud MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1190 | Exploit Public-Facing Application | [TeamPCP](https://attack.mitre.org/groups/G1056) has exploited misconfigurations in GitHub Actions and vulnerabilities such as CVE-2026-33634 in the Aqua Security Trivy scanner and CVE-2025-55182 (React2Shell) against vulnerable cloud endpoints.(Citation: Aqua Security Blog Trivy Compromise APR 2026)(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Wiz Mini Shai-Hulud MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1195.001 | Compromise Software Dependencies and Development Tools | [TeamPCP](https://attack.mitre.org/groups/G1056) has conducted coordinated supply chain attacks targeting open-source developer infrastructure including the NPM, VS Code, Docker, and PyPi ecosystems to compromise multiple software packages.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Trivy Compromise MAR 2026)(Citation: Wiz TeamPCP KICS MAR 2026)(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Wiz Mini Shai-Hulud MAY 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Hunt.io TeamPCP Toolkit MAY 2026)(Citation: Phoenix TeamPCP 20 MAY 2026)(Citation: Flashpoint Mini Shai-Hulud MAY 2026)(Citation: FBI TeamPCP JUL 2026)(Citation: Google AI Threat Tracker MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1485 | Data Destruction | [TeamPCP](https://attack.mitre.org/groups/G1056) has deployed privileged DaemonSets to delete files on Kubernetes clusters and has executed recursive file deletions on non-containerized hosts.(Citation: Palo Alto TeamPCP MAR 2026)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1486 | Data Encrypted for Impact | [TeamPCP](https://attack.mitre.org/groups/G1056) has deployed ransomware and has announced partnerships with ransomware groups including Vect and CipherForce in online criminal forums.(Citation: Palo Alto TeamPCP MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1528 | Steal Application Access Token | [TeamPCP](https://attack.mitre.org/groups/G1056) has used malware to steal access tokens from targeted cloud and developer environments.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Blog Trivy Compromise APR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: FBI TeamPCP JUL 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1543.002 | Systemd Service | [TeamPCP](https://attack.mitre.org/groups/G1056) has used the systemd user service for malware persistence in targeted environments.(Citation: Wiz TeamPCP KICS MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1546.016 | Installer Packages | [TeamPCP](https://attack.mitre.org/groups/G1056) has modified software packages with preinstall scripts to download and execute malicious payloads.(Citation: Wiz Mini Shai-Hulud MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [TeamPCP](https://attack.mitre.org/groups/G1056) has dropped malware into the Windows Startup folder to establish persistence.(Citation: Aikido TeamPCP Telnyx MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Lateral Movement | T1550.001 | Application Access Token | [TeamPCP](https://attack.mitre.org/groups/G1056) has used stolen access tokens to inject malicious code into CI/CD workflows and to exfiltrate sensitive data from cloud, developer, and container environments.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1552.004 | Private Keys | [TeamPCP](https://attack.mitre.org/groups/G1056) has used malware to extract SSH and GPG keys from victim environments.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: FBI TeamPCP JUL 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1553.002 | Code Signing | [TeamPCP](https://attack.mitre.org/groups/G1056) has compromised legitimate software release workflows resulting in malicious packages receiving legitimate project cryptographic signing.(Citation: Trend Micro TeamPCP MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1555.006 | Cloud Secrets Management Stores | [TeamPCP](https://attack.mitre.org/groups/G1056) has used malware to exfiltrate cloud secrets from targeted environments including AWS, GCP, and Azure.(Citation: Sysdig TeamPCP MAR 2026)(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: FBI TeamPCP JUL 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1564.001 | Hidden Files and Directories | [TeamPCP](https://attack.mitre.org/groups/G1056) has used a hidden .lock file to establish a 12 hour cooldown period between re-drops for installed malware.(Citation: Aikido TeamPCP Telnyx MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583 | Acquire Infrastructure | In May 2026 [TeamPCP](https://attack.mitre.org/groups/G1056) announced co-ownership of the BreachForums cybercriminal forum claiming responsibility for platform operations, dispute resolution, personnel vetting, and hosting monetary contests.(Citation: Flashpoint Mini Shai-Hulud MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583.001 | Domains | [TeamPCP](https://attack.mitre.org/groups/G1056) has registered domains resembling legitimate victim sites such as scan.aquasecurtiy[.]org, checkmarx[.]zone, and git-tanstack[.]com to mask C2 and exfiltration endpoints.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Trivy Compromise MAR 2026)(Citation: Aqua Security Blog Trivy Compromise APR 2026)(Citation: Sysdig TeamPCP MAR 2026)(Citation: Wiz TeamPCP KICS MAR 2026)(Citation: Wiz Mini Shai-Hulud MAY 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Phoenix TeamPCP 20 MAY 2026) [TeamPCP](https://attack.mitre.org/groups/G1056) has also set up a dark web leak site to post stolen data.(Citation: Palo Alto TeamPCP MAR 2026)(Citation: FBI TeamPCP JUL 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583.004 | Server | [TeamPCP](https://attack.mitre.org/groups/G1056) has leased infrastructure specifically for offensive operations including Google assets in AS396982.(Citation: Hunt.io TeamPCP Toolkit MAY 2026)(Citation: FBI TeamPCP JUL 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583.006 | Web Services | [TeamPCP](https://attack.mitre.org/groups/G1056) has set up Clouflare Tunnels for malware C2.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Blog Trivy Compromise APR 2026)(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Trend Micro TeamPCP MAY 2026) [TeamPCP](https://attack.mitre.org/groups/G1056) has also used the session messenger network for decentralized, encrypted exfiltration via  *.getsession[.]org to recipient  ID `05f9e609d79eed391015e11380dee4b5c9ead0b6e2e7f0134e6e51767a87323026`.(Citation: Wiz Mini Shai-Hulud MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1585.001 | Social Media Accounts | [TeamPCP](https://attack.mitre.org/groups/G1056) has used its own Telegram channel and X accounts @pcpcats and @xploitrsturtle2 for external communications.(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Phoenix TeamPCP 20 MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1587.001 | Malware | [TeamPCP](https://attack.mitre.org/groups/G1056) has developed and deployed custom malware including [TeamPCP Cloud Stealer](https://attack.mitre.org/software/S9041), [CanisterWorm](https://attack.mitre.org/software/S9042), and [Mini Shai-Hulud](https://attack.mitre.org/software/S9043).(Citation: Wiz Trivy Compromise MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1608.001 | Upload Malware | [TeamPCP](https://attack.mitre.org/groups/G1056) has pushed GitHub commits that modified the actions/checkout to reference an imposter commit that downloaded malicious files from attacker-controlled C2 domains.(Citation: Aqua Security Trivy Compromise MAR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1657 | Financial Theft | [TeamPCP](https://attack.mitre.org/groups/G1056) has engaged in cryptocurrency mining and theft.(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Trend Micro TeamPCP MAY 2026) [TeamPCP](https://attack.mitre.org/groups/G1056) has also partnered with ransomware and data theft extortion groups, sold leaked code, and crowdsourced supply chain compromises by open-sourcing their [Mini Shai-Hulud](https://attack.mitre.org/software/S9043) malware.(Citation: Flashpoint Mini Shai-Hulud MAY 2026)(Citation: Phoenix TeamPCP 20 MAY 2026)(Citation: FBI TeamPCP JUL 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1677 | Poisoned Pipeline Execution | [TeamPCP](https://attack.mitre.org/groups/G1056) has compromised trusted CI/CD pipelines by injecting credential-stealing payloads into legitimate workflows and software packages including open-source security tools Trivy and KICS, and AI gateway LiteLLM.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Trivy Compromise MAR 2026)(Citation: Aqua Security Trivy Compromise MAR 2026)(Citation: Aqua Security Blog Trivy Compromise APR 2026)(Citation: Sysdig TeamPCP MAR 2026)(Citation: Wiz TeamPCP KICS MAR 2026)(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Wiz Mini Shai-Hulud MAY 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Hunt.io TeamPCP Toolkit MAY 2026)(Citation: Phoenix TeamPCP 20 MAY 2026)(Citation: Flashpoint Mini Shai-Hulud MAY 2026)(Citation: FBI TeamPCP JUL 2026)(Citation: Google AI Threat Tracker MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1683.001 | Written Content | [TeamPCP](https://attack.mitre.org/groups/G1056) has created Dune-themed GitHub repositories using stolen tokens.(Citation: Wiz Mini Shai-Hulud MAY 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1684.001 | Impersonation | [TeamPCP](https://attack.mitre.org/groups/G1056) impersonated legitimate maintainers to push imposter commits to the Aquasecurity Trivy scanner GitHub repository.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Blog Trivy Compromise APR 2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.004 | Unix Shell | 侵害したRayクラスタへ第1段階シェルスクリプトndt.shを配信して実行し、リバースシェルと追加ペイロードを取得する。 |  | activity--daily-5aa545c901df820c7aa2 | 2025-06 | 不明 | 高 | `source--oligo-teampcp-2026` |
| Initial Access | T1190 | Exploit Public-Facing Application | Ray、Docker、Redis、Reactなどインターネットへ露出したサービスを自動・ワーム型で侵害する。 |  | activity--daily-5aa545c901df820c7aa2 | 2020 | 2026-04 | 高 | `source--oligo-teampcp-2026` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | 侵害済みPyPIパッケージと悪意あるプルリクエストを起点にGitHubリポジトリとGitHub Actionsを侵害し、配布物へ悪性コードを埋め込む。 |  | activity--teampcp-oss-supply-chain-2026 | 2026-02 | 2026-03 | 高 | `source--gtig-ai-threat-tracker-2026-05`, `source--sentinellabs-pcpjack-2026` |
| Impact | T1486 | Data Encrypted for Impact | 侵害したクラウド環境でランサムウェアを展開し、恐喝グループとの提携で収益化する。 |  | activity--daily-5aa545c901df820c7aa2 | 不明 | 不明 | 高 | `source--oligo-teampcp-2026`, `source--sentinellabs-pcpjack-2026` |
| Credential Access | T1552.001 | Credentials In Files | SANDCLOCK資格情報スティーラーをビルド環境へ埋め込み、AWSキーとGitHubトークンを窃取する。 | malware--sandclock | activity--teampcp-oss-supply-chain-2026 | 2026-02 | 不明 | 高 | `source--gtig-ai-threat-tracker-2026-05` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
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
- GTIG 2026-09-08 は本アクターのOSSサプライチェーン侵害が「Since March 2026」継続していると述べるが、観測終了日を明示していない。activity--teampcp-oss-supply-chain-2026 の last_observed は初報に基づく2026年3月のままであり、2026年4月以降の継続期間は一次資料で確定していない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--daily-48f251212f832ab9b6df | 新たなインテリジェンスがTeamPCPとShadowRay 2.0を関連付け、活動を2020年まで遡及 | oligo.security | 2026-08-08 | https://www.oligo.security/blog/new-intelligence-links-teampcp-to-shadowray-2-0-and-traces-activity-back-to-2020 | osint-report | TLP:CLEAR | 中 |
| source--gtig-ai-threat-tracker-2026-05 | GTIG AI Threat Tracker: Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access | Google Threat Intelligence Group | 2026-05-11 | https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access | vendor-research-report | TLP:CLEAR | 高 |
| source--oligo-teampcp-2026 | New Intelligence Links TeamPCP to ShadowRay 2.0 and Traces Activity Back to 2020 | Oligo Security | 2026-08-05 | https://www.oligo.security/blog/new-intelligence-links-teampcp-to-shadowray-2-0-and-traces-activity-back-to-2020 | vendor-research-report | TLP:CLEAR | 高 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--sentinellabs-pcpjack-2026 | PCPJack \| Cloud Worm Evicts TeamPCP and Steals Credentials at Scale | SentinelOne (SentinelLabs) | 2026-05-07 | https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/ | vendor-research-report | TLP:CLEAR | 高 |
| source--gtig-adversarial-ai-2026 | GTIG AI Threat Tracker: From Prompting to Autonomy - The Evolution of Adversarial AI | Google Threat Intelligence Group | 2026-09-08 | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai | vendor-research | TLP:CLEAR | 高 |
| source--mitre-attack-g1056 | TeamPCP, Group G1056 | MITRE ATT&CK | 2026-07-31 | https://attack.mitre.org/groups/G1056/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

本プロファイルは2026-08-10の日次更新チェックで未一致名として検知され、独立一次資料3本の確認後に昇格した。status: draftから開始する。
