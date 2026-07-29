# Contagious Interview 脅威アクタープロファイル

- プロファイルID: `actor--contagious-interview`
- 状態: draft
- 更新日時: 2026-07-27T11:17:23Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Contagious Interviewの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Contagious Interview**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DeceptiveDevelopment | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DEV#POPPER | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Gwisin Gang | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| PurpleBravo | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TAG-121 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Tenacious Pungsan | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Contagious Interview](https://attack.mitre.org/groups/G1052) is a North Korea–aligned threat group active since 2023. The group conducts both cyberespionage and financially motivated operations, including the theft of cryptocurrency and user credentials. [Contagious Interview](https://attack.mitre.org/groups/G1052) targets Windows, Linux, and macOS systems, with a particular focus on individuals engaged in software development and cryptocurrency-related activities. (Citation: Validin Contagious Interview North Korea ClickFix January 2025)(Citation: Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: Datadog Contagious Interview Tenacious Pungsan October 2024)(Citation: Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025)(Citation: ESET Contagious Interview BeaverTail InvisibleFerret February 2025)(Citation: Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023)(Citation: PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024) |
| Capability | InvisibleFerret, HexEval Loader, BeaverTail, XORIndex Loader |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Operation Contagious Interview | multiple-name-intersection | 高 | North Korea | https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/<br>https://www.knowbe4.com/hubfs/North-Korean-Fake-Employees-Are-Everywhere-WP_EN-us.pdf<br>https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | WageMole | single-alias-intersection | 中 | KP | https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/<br>https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/<br>https://www.trendmicro.com/en_us/research/25/d/russian-infrastructure-north-korean-cybercrime.html |
| misp-threat-actor | Contagious Interview | canonical-name | 高 |  | https://about.gitlab.com/blog/gitlab-threat-intelligence-reveals-north-korean-tradecraft/<br>https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/<br>https://www.microsoft.com/en-us/security/blog/2026/03/11/contagious-interview-malware-delivered-through-fake-developer-job-interviews/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Contagious Interview - G1052 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1052<br>https://reports.dtexsystems.com/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf<br>https://securitylabs.datadoghq.com/articles/tenacious-pungsan-dprk-threat-actor-contagious-interview/ |
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
| malware--beavertail | BeaverTail | [BeaverTail](https://attack.mitre.org/software/S1246) is a malware that has both a JavaScript and C++ variant.  Active since 2022, [BeaverTail](https://attack.mitre.org/software/S1246) is capable of stealing logins from browsers and serves as a downloader for second stage payloads. [BeaverTail](https://attack.mitre.org/software/S1246) has previously been leveraged by North Korea-affiliated actors identified as DeceptiveDevelopment or [Contagious Interview](https://attack.mitre.org/groups/G1052). [BeaverTail](https://attack.mitre.org/software/S1246) has been delivered to victims through code repository sites and has been embedded within malicious attachments.(Citation: PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023)(Citation: Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: ESET Contagious Interview BeaverTail InvisibleFerret February 2025)(Citation: Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hexeval-loader | HexEval Loader | [HexEval Loader](https://attack.mitre.org/software/S1249) is a hex-encoded loader that collects host data, decodes follow-on scripts and acts as a downloader for the [BeaverTail](https://attack.mitre.org/software/S1246) malware.  [HexEval Loader](https://attack.mitre.org/software/S1249) was first reported in April 2025.  [HexEval Loader](https://attack.mitre.org/software/S1249) has previously been leveraged by North Korea-affiliated threat actors identified as [Contagious Interview](https://attack.mitre.org/groups/G1052).  [HexEval Loader](https://attack.mitre.org/software/S1249) has been delivered to victims through code repository sites utilizing typosquatting naming conventions of various npm packages.(Citation: Socket Contagious Interview NPM April 2025)(Citation: Socket BeaverTail XORIndex HexEval Contagious Interview July 2025)(Citation: Socket HexEval BeaverTail Contagious Interview June 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--invisibleferret | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) is a modular python malware that is leveraged for data exfiltration and remote access capabilities.(Citation: ESET Contagious Interview BeaverTail InvisibleFerret February 2025)(Citation: Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023)   [InvisibleFerret](https://attack.mitre.org/software/S1245) consists of four modules: main, payload, browser, and AnyDesk.(Citation: ESET Contagious Interview BeaverTail InvisibleFerret February 2025)  [InvisibleFerret](https://attack.mitre.org/software/S1245) malware has been leveraged by North Korea-affiliated threat actors identified as DeceptiveDevelopment or [Contagious Interview](https://attack.mitre.org/groups/G1052) since 2023.(Citation: Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025)(Citation: Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023)(Citation: PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024)  [InvisibleFerret](https://attack.mitre.org/software/S1245) has historically been introduced to the victim environment through the use of the [BeaverTail](https://attack.mitre.org/software/S1246) malware.(Citation: Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: ESET Contagious Interview BeaverTail InvisibleFerret February 2025)(Citation: Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023)(Citation: PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--xorindex-loader | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) is a XOR-encoded loader that collects host data, decodes follow-on scripts and acts as a downloader for the [BeaverTail](https://attack.mitre.org/software/S1246) malware.  [XORIndex Loader](https://attack.mitre.org/software/S1248) was first reported in June 2025.  [XORIndex Loader](https://attack.mitre.org/software/S1248) has been leveraged by North Korea-affiliated threat actors identified as [Contagious Interview](https://attack.mitre.org/groups/G1052).  [XORIndex Loader](https://attack.mitre.org/software/S1248) has been delivered to victims through code repository sites utilizing typo squatting naming conventions of various npm packages.(Citation: Socket BeaverTail XORIndex HexEval Contagious Interview July 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| 35のnpmパッケージを使用してマルウェアを拡散する新たな“偽の面接”キャンペーン | malware-campaign | 不明 | 不明 | 2025-06-26 | 北朝鮮の“Contagious Interview”キャンペーンが35個の悪質npmパッケージで開発者を標的化 Socket Threat ResearchがBeaverTailインフォスティーラーとInvisibleFerretバックドアを検出 24アカウントから公開、累計4,000回超ダウンロード、6パッケージが現存 これらのパッケージの多くは、タイポスクワッティング（スペルミスを利用して正規のパッケージを装うこと）や既知の信頼できるライブラリを模倣 攻撃者はLinkedInで面接を偽装しGoogle Docs経由でテスト課題と共にパッケージを配布 求職者は、コードをコンテナ化された環境ではなく、自身のOS上で実行するように圧力をかけられることが多く、画面共有中に実行を促されることもある | 中 | `source--daily-2a32ed98e1bd6d1661b4` |
| FlexibleFerretマルウェアの攻撃が続く | malware-campaign | 不明 | 不明 | 2025-11-26 | Jamf Threat Labsは、DPRK系とされるFlexibleFerretが偽の採用評価サイトでmacOSの資格情報窃取を行う手口を解析。 求人ページのJSがcurl実行を誘導し/var/tmp/macpatch.shを取得、LaunchAgent作成などで永続化する多段感染へ移行。 おとりの「MediaPatcher」がChrome風PW入力を表示し、content[.]dropboxapi[.]comへ送信、api[.]ipify[.]orgでIP取得。 最終段はGo製CDriversバックドアが95[.]169[.]180[.]140:8080へ接続し、情報収集・転送・コマンド実行を行う。 IoCには偽求人ドメインと配布URLが列挙。面接課題での端末コマンド実行指示は高リスクとして停止・報告を周知。 | 中 | `source--daily-25f950d9ddf02f2d5ba4` |
| 北朝鮮の Contagious Interview キャンペーンが5つのエコシステムへ拡大し、段階的な RAT ペイロードを配布 | campaign | 不明 | 不明 | 2026-04-09 | Socket は、Contagious Interview に結び付く北朝鮮系活動として、npm・PyPI・Go Modules・Rust・PHP を含む5系統にまたがる悪性パッケージ群を確認した。 各パッケージは debug や license などの正規開発ツールを装い、通常メソッドの裏で downloadUrl を取得し、ZIP や base64 の第2段階ペイロードを配信した。 主目的は資格情報、ブラウザデータ、パスワードマネージャー情報、暗号資産ウォレットの窃取で、RAT を伴う情報窃取活動として設計されていた。 特に Windows 寄りの license-utils-kitなどは、リモートシェル、キーロギング、ブラウザ窃取、AnyDesk 展開、機密ファイル収集まで可能な後続インプラントを含んでいた。 攻撃者は golangorg や aokisasakidev など複数の GitHub ペルソナを使い分け、一部パッケージは削除済みだが、執筆時点でなお残存しているものもあった。 | 高 | `source--daily-828c717719b991a7c676` |
| 北朝鮮のハッカー、継続中の攻撃キャンペーンでXORIndexマルウェアを用いnpmレジストリに大量の不正パッケージを公開 | infrastructure-operation | 不明 | 不明 | 2025-07-16 | Contagious Interviewキャンペーンの北朝鮮系攻撃者が67個の悪意あるnpmパッケージを公開。XORIndexという新たなローダーも発見された。 これらは計17,000以上のダウンロードを獲得し、先月の35パッケージ（HexEvalローダー）攻撃を拡大。 悪意あるパッケージはJavaScriptローダーBeaverTailでブラウザや暗号ウォレットからデータ窃取、InvisibleFerretを展開。 XORIndexは第1世代の試作から第3世代でシステム偵察・ステルス機能を追加し、C2にビークン送信。 2023年末に公開以来、開発者を装う演出でサプライチェーン攻撃を継続的に実行中。 | 中 | `source--daily-d00e6abeb3390b2c40e7` |
| 北朝鮮ハッカー、偽の仮想通貨企業と偽就職面接でマルウェアを拡散 | malware-campaign | 不明 | 不明 | 2025-04-26 | 北朝鮮支援のグループが偽の仮想通貨企業を設立し、就職面接を装いマルウェアを拡散。 BlockNovas、Angeloper、SoftGlideの3社を使い、BeaverTailなど複数マルウェアを配布。 マルウェアはシステム情報収集やリバースシェル作成、ブラウザデータ窃取が可能。 ロシアのIPレンジを使い活動を匿名化し、米FBIはBlockNovasドメインを押収。 活動の背後にはAIツールを利用した偽プロファイル作成も含まれる。 | 中 | `source--daily-cf8c33fcf3e4b3907567` |
| 北朝鮮のハッカーが悪意のあるnpmパッケージで開発者を標的に | malware-campaign | 不明 | 不明 | 2024-08-31 | 北朝鮮のハッカーが、npmレジストリに悪意のあるパッケージを公開し、開発者を標的に。 マルウェア「InvisibleFerret」は、仮想通貨ウォレットのデータを窃取し、持続的なアクセスを確立。 攻撃は8月12日から27日の間に確認され、「temp-etherscan-api」「ethersscan-api」「telegram-con」「helmet-validate」「qq-console」という名称のパッケージが使用された。 これらの攻撃は「Contagious Interview」作戦の一環とされる。CrowdStrikeはこの活動を「Famous Chollima」として追跡中。 攻撃目的は主に金銭だが、機密情報の窃取が目的であったケースもある | 中 | `source--daily-b84641d39a296b1d232d` |
| 北朝鮮系ハッカー、BeaverTailとOtterCookieを統合した高度なJSマルウェアを展開 | infrastructure-operation | 不明 | 不明 | 2025-10-18 | 北朝鮮系「Contagious Interview」集団がBeaverTailとOtterCookieの機能を収斂、進化させたJS系マルウェア運用が確認。 OtterCookieはキー入力記録・画面撮影モジュールを新搭載し、取得データをC2へ送信する改良版（v5）が観測された。 Google/MandiantはEtherHidingでBSCやEthereumから次段階ペイロード取得と報告し、国家支援勢力の初事例と位置づけ。 スリランカ企業の端末で感染を確認。偽求人の課題でBitbucket配布のNode.jsアプリ「Chessfi」を導入させたのが起点。 npmには8/20公開の悪性依存「node-nvm-ssh」が混入し6日後に削除、計306回ダウンロード。VS Code拡張やQt派生など多様な配布形態も示唆。 | 中 | `source--daily-e8f48a18d1cc39fa808c` |
| 北朝鮮ハッカー、JSONサービスを秘匿型マルウェア配信経路に転用 | infrastructure-operation | 不明 | 不明 | 2025-11-15 | NVISOの報告に基づき、「Contagious Interview」作戦がJSONストレージを悪用し、隠密にペイロードを配信とTHNが報道。 攻撃者はLinkedIn等で開発者に接触し、GitHub/GitLab/Bitbucketのデモ取得を装いトロイ化プロジェクトを配布。 プロジェクト内の“.config.env”にBase64偽API鍵を埋め込み、実態はJSON Keeperやnpoint.io等の次段URLを指す。 取得されたBeaverTailが情報窃取やInvisibleFerret投下、さらにPastebin経由のTsunamiKit取得など機能が観測。 ESETは9月にTsunamiKit等を確認；.onionのC2は現在オフラインで、広範な開発者狙いが継続と結論。 | 中 | `source--daily-cdb23aca8de000a4d647` |
| PolinRider：北朝鮮関連のサプライチェーン攻撃キャンペーンがオープンソースエコシステム全体へ拡大 | infrastructure-operation | 不明 | 不明 | 2026-07-02 | Socketは、npm、Packagist、Go modules、Chrome拡張にまたがるPolinRiderの悪性リリース162件を確認した。 本キャンペーンは北朝鮮関連のContagious Interview／Famous Chollima活動クラスタに関連付けられている。 攻撃者は正規リポジトリを侵害し、難読化JavaScriptローダーを設定ファイルや偽の.woff2ファイルに隠す。 VS Codeのtasks.jsonなどを悪用して開発環境でローダーを実行し、二段階目ペイロードを取得・復号・実行する。 観測されたペイロードにはDEV#POPPERとOmniStealerが含まれ、認証情報窃取やC2通信などの機能を持つ。 | 中 | `source--daily-93581ba9dc03b85be996` |
| 新しい「OtterCookie」マルウェアが偽の求人を通じて開発者をバックドア化 | infrastructure-operation | 不明 | 不明 | 2024-12-27 | 北朝鮮の攻撃者が「OtterCookie」マルウェアを使い、開発者を標的にした「Contagious Interview」キャンペーンを展開。 OtterCookieはNode.jsプロジェクトやnpmパッケージ、最近ではQtやElectronアプリケーションを介して拡散。 OtterCookieはSocket.IO WebSocketツールを使用してコマンド＆コントロール（C2）インフラストラクチャとの安全な通信を確立し、リモートシェルコマンドを受信。 マルウェアは暗号通貨ウォレットの鍵や機密データを盗むコマンドが観測した。 標的の環境調査や情報窃取を進め、さらなる侵入を目指す行動が観察。 偽求人を介した攻撃手法の多様化が進んでいる。 | 中 | `source--daily-47e80e1dc37b49447e5b` |
| 北朝鮮系ハッカーが「ClickFix」を悪用し、暗号資産の偽求人でBeaverTailを配布 | campaign | 不明 | 不明 | 2025-09-22 | 北朝鮮関係者がClickFix誘導を用い、BeaverTailとInvisibleFerretを偽求人経由で配布する手口が確認された。 従来の開発者狙いから、暗号資産・小売のマーケ/トレーダー職志望者へ標的を拡大し、Vercel製偽採用サイトを配布基盤に利用。 OS別コマンド実行を促す偽マイク障害表示で、シェル/VBスクリプト経由の軽量版BeaverTailを展開するのが特徴。 2025年5月後半の波では、pkgやPyInstallerで作成したWindows/macOS/Linux向けバイナリ化版の投入が観測された。 この攻撃キャンペーンに時期を合わせ、北朝鮮と連携するKimsuky (別名 APT43)による2つの攻撃キャンペーンも観測されている。 | 中 | `source--daily-dddef70e68c0dc59a5d3` |
| OtterCookie v4、VM検出とChrome・MetaMaskの認証情報窃取機能を追加 | malware-campaign | 不明 | 不明 | 2025-05-12 | 北朝鮮の攻撃キャンペン「Contagious Interview」が、マルウェア「OtterCookie」のv3およびv4を2025年2月と4月に展開。 v4では、Google ChromeやBraveブラウザ、MetaMask、iCloud Keychainからの認証情報窃取機能が追加。 仮想環境（VMware、VirtualBox、Microsoft、QEMU）での実行を検出し、解析を回避する機能を搭載。 マルウェアは、npmパッケージ、GitHub/Bitbucketのリポジトリ、偽のビデオ会議アプリを通じて配布。 「DriverMinUpdate.app」などの偽アプリを用いたmacOS向けの情報窃取も確認されている。 | 中 | `source--daily-56f1f7edcfb3f507fe75` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.003 | Mail Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.004 | Malicious Copy and Paste | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.005 | Malicious Library | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219.002 | Remote Desktop Software | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1480 | Execution Guardrails | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.001 | Launch Agent | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.004 | Unix Shell Configuration Modification | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.013 | XDG Autostart Entries | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.001 | Keychain | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.003 | Spearphishing via Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567 | Exfiltration Over Web Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583 | Acquire Infrastructure | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585 | Establish Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587 | Develop Capabilities | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.007 | Artificial Intelligence | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1593 | Search Open Websites/Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1593.001 | Social Media | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1593.003 | Code Repositories | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1681 | Search Threat Vendor Data | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1683.001 | Written Content | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1683.002 | Audio-Visual Content | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 3件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 64件（`artifacts.csv`）

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
| source--contagious-interview--061e3eec2559cac7 | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--0a4af9158c781f8e | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--0b363923530f4f4d | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--14550d87803a3543 | contagious interview |  | 不明 | actor_profile/evidence/contagious-interview.csv | structured-data | TLP:CLEAR | 中 |
| source--contagious-interview--20b01df622602c7e | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--322767d7060d5ded | DeceptiveDevelopment and North Korean IT workers from primitive crypto theft to sophisticated AI based deception |  | 不明 | CyberMerceNary/ITWorker/DeceptiveDevelopment-and-North-Korean-IT-workers-from-primitive-crypto-theft-to-sophisticated-AI-based-deception.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--51c6cb79504d7c03 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--65b059f582eb5acb | Smile, You’re on Camera  A Live Stream from Inside Lazarus Group’s IT Workers Scheme |  | 不明 | CyberMerceNary/ITWorker/Smile, You’re on Camera_ A Live Stream from Inside Lazarus Group’s IT Workers Scheme.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--770f2e8cde0a3578 | eset apt activity report q2 2025 q3 2025 |  | 2025 | summary/2025/eset-apt-activity-report-q2-2025-q3-2025.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--7c451a6da2de1856 | eset apt activity report q4 2025 q1 2026 |  | 2025 | summary/2026/eset-apt-activity-report-q4-2025-q1-2026.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--848eb97f8e531a97 | Booz Allen Hamilton |  | 不明 | AISecurity/2026/Booz Allen Hamilton.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--9b0d1ce3ffa71416 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--9dfb82eeadbe6886 | eset threat report h22025 |  | 不明 | summary/2025/eset-threat-report-h22025.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--a6c38631793a3535 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--bac1102ac7c5f0b9 | Inside the ScamNorth Korea’s IT Worker Threat |  | 不明 | CyberMerceNary/ITWorker/Inside the ScamNorth Korea’s IT Worker Threat.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--bb52cd6ee339d2e7 | 2025 Year in Review  Malicious Infrastructure |  | 2025 | summary/2026/2025 Year in Review- Malicious Infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--c543cad730a42fed | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--f488db60801250db | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--contagious-interview--fea0ffb36c7936d4 | eset threat report h12025 |  | 不明 | summary/2025/eset-threat-report-h12025.pdf | report | TLP:CLEAR | 中 |
| source--daily-25f950d9ddf02f2d5ba4 | FlexibleFerretマルウェアの攻撃が続く | jamf.com | 2025-11-26 | https://www.jamf.com/blog/flexibleferret-malware-continues-to-adapt/ | osint-report | TLP:CLEAR | 中 |
| source--daily-2a32ed98e1bd6d1661b4 | 35のnpmパッケージを使用してマルウェアを拡散する新たな“偽の面接”キャンペーン | bleepingcomputer.com | 2025-06-26 | https://www.bleepingcomputer.com/news/security/new-wave-of-fake-interviews-use-35-npm-packages-to-spread-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-47e80e1dc37b49447e5b | 新しい「OtterCookie」マルウェアが偽の求人を通じて開発者をバックドア化 | bleepingcomputer.com | 2024-12-27 | https://www.bleepingcomputer.com/news/security/new-ottercookie-malware-used-to-backdoor-devs-in-fake-job-offers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-56f1f7edcfb3f507fe75 | OtterCookie v4、VM検出とChrome・MetaMaskの認証情報窃取機能を追加 | thehackernews.com | 2025-05-12 | https://thehackernews.com/2025/05/ottercookie-v4-adds-vm-detection-and.html | osint-report | TLP:CLEAR | 中 |
| source--daily-828c717719b991a7c676 | 北朝鮮の Contagious Interview キャンペーンが5つのエコシステムへ拡大し、段階的な RAT ペイロードを配布 | socket.dev | 2026-04-09 | https://socket.dev/blog/contagious-interview-campaign-spreads-across-5-ecosystems | osint-report | TLP:CLEAR | 中 |
| source--daily-93581ba9dc03b85be996 | PolinRider：北朝鮮関連のサプライチェーン攻撃キャンペーンがオープンソースエコシステム全体へ拡大 | socket.dev | 2026-07-02 | https://socket.dev/blog/polinrider-north-korea-linked-supply-chain-campaign-expands | osint-report | TLP:CLEAR | 中 |
| source--daily-b84641d39a296b1d232d | 北朝鮮のハッカーが悪意のあるnpmパッケージで開発者を標的に | thehackernews.com | 2024-08-31 | https://thehackernews.com/2024/08/north-korean-hackers-target-developers.html | osint-report | TLP:CLEAR | 中 |
| source--daily-cdb23aca8de000a4d647 | 北朝鮮ハッカー、JSONサービスを秘匿型マルウェア配信経路に転用 | thehackernews.com | 2025-11-15 | https://thehackernews.com/2025/11/north-korean-hackers-turn-json-services.html | osint-report | TLP:CLEAR | 中 |
| source--daily-cf8c33fcf3e4b3907567 | 北朝鮮ハッカー、偽の仮想通貨企業と偽就職面接でマルウェアを拡散 | thehackernews.com | 2025-04-26 | https://thehackernews.com/2025/04/north-korean-hackers-spread-malware-via.html | osint-report | TLP:CLEAR | 中 |
| source--daily-d00e6abeb3390b2c40e7 | 北朝鮮のハッカー、継続中の攻撃キャンペーンでXORIndexマルウェアを用いnpmレジストリに大量の不正パッケージを公開 | thehackernews.com | 2025-07-16 | https://thehackernews.com/2025/07/north-korean-hackers-flood-npm-registry.html | osint-report | TLP:CLEAR | 中 |
| source--daily-dddef70e68c0dc59a5d3 | 北朝鮮系ハッカーが「ClickFix」を悪用し、暗号資産の偽求人でBeaverTailを配布 | thehackernews.com | 2025-09-22 | https://thehackernews.com/2025/09/dprk-hackers-use-clickfix-to-deliver.html | osint-report | TLP:CLEAR | 中 |
| source--daily-e8f48a18d1cc39fa808c | 北朝鮮系ハッカー、BeaverTailとOtterCookieを統合した高度なJSマルウェアを展開 | thehackernews.com | 2025-10-18 | https://thehackernews.com/2025/10/north-korean-hackers-combine-beavertail.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
