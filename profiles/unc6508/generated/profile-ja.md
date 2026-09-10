# UNC6508 脅威アクタープロファイル

- プロファイルID: `actor--unc6508`
- 状態: draft
- 更新日時: 2026-09-10T22:21:38Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC6508は、北米の医学研究機関・学術機関・軍関連衛生機関を狙うPRC系の諜報クラスタである。外部公開されたREDCapサーバーを侵入面とし、専用バックドアINFINITEREDでアップグレードをまたぐ永続化と資格情報収集を行い、メールのコンテンツコンプライアンス規則を悪用して関心分野のメールを外部へBCC転送する。収集目標には人工知能、無人機システム、攻撃的サイバー計画といった国防関連研究が含まれ、専有AI研究とモデルを重点的に狙う。侵害環境上にオープンウェイトモデルを展開して商用AI APIの監視を回避する手口も観測されている。

## アクター名とAlias

- 正規名: **UNC6508**
- 初回観測: 2023-09
- 最終観測: 2025-11
- 活動状態: likely

Aliasなし

## 帰属

GTIGは2026-06-15の報告で「GTIG attributes this activity to UNC6508 with high confidence.」と述べ、根拠としてキャンペーン間のインフラ重複、REDCapサーバー上でのINFINITEREDバックドアの一貫した使用、医学研究および防衛分野への特異的な標的選択を挙げている。動機については「We assess UNC6508 is an espionage motivated threat cluster, with priorities that align with historic PRC state-sponsored espionage trends and intelligence collection requirements.」として、PRCの国家支援型諜報の傾向および情報収集要求と優先度が整合すると評価する。特定の政府機関・企業への帰属は行われていない。

- 国: China
- スポンサー種別: state-sponsored
- 確度: 高
- 証拠: `source--gtig-unc6508-medical-research-2026`, `source--gtig-adversarial-ai-2026`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | 北米の医学研究・学術・軍関連衛生機関から、分子探索、臨床薬剤試験、公衆衛生政策、軍の即応性、人工知能、無人機システム、攻撃的サイバー計画に関する研究情報を継続的に収集する。 | 高 | `source--gtig-unc6508-medical-research-2026` | GTIGは「We assess UNC6508 is an espionage motivated threat cluster, with priorities that align with historic PRC state-sponsored espionage trends and intelligence collection requirements.」と評価している。 |
| technology-acquisition | 専有AI研究とモデルの取得を明確な目標とする。侵害環境上にオープンウェイトモデルを展開し、商用AI APIの監視を回避しつつ被害組織の計算資源を流用する。 | 中 | `source--gtig-adversarial-ai-2026` | GTIG 2026-09-08に基づく。ローカルLLM展開は原文が suspected と留保しているため確度はmediumとする。 |

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

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--infinitered | INFINITERED | REDCapサーバーを対象とするPHP製の多機能バックドア。ドロッパーはREDCapのアップグレード処理へ介入し、GUID区切り子 b49e334d-9c01-463e-9bc5-00a6920fb66e を目印に新バージョンへコードを再注入して永続化する。資格情報ハーベスタはログインのPOSTから利用者名とパスワードを取得し、接頭辞 xc32038474a を持つセッションIDでREDCapデータベースへ暗号化して保存する。バックドア本体はHTTP Cookie「REDCAP-TOKEN」をC2チャネルとし、任意コマンド実行(00)、ファイルアップロード(02)、窃取資格情報の取得(03)と削除(04)、任意SQL実行(05)、任意ファイルのダウンロードに対応する。 | 2023-12 | 2025-11 | 高 | `source--gtig-unc6508-medical-research-2026` |

### ツール

未確認

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--unc6508-obfuscation-network | 難読化ネットワークによる通信元の秘匿 | 侵害済みルーター、レジデンシャルプロキシ、VPSを経由し、通信元IPを米国内に限定して地理的な異常検知を回避する。 | 不明 | 不明 | 高 | `source--gtig-unc6508-medical-research-2026` |
| opcap--unc6508-dedicated-exfil-account | 持ち出し専用アカウントの分離運用 | 自動化サービスで大量取得したGmailアカウントのうち1つをメール持ち出し専用に限定し、他用途と混在させない。 | 不明 | 不明 | 高 | `source--gtig-unc6508-medical-research-2026` |
| opcap--unc6508-downgrade-attack | 併存する旧バージョンを狙うダウングレード攻撃 | 現行版と併存して稼働する脆弱な旧バージョンのREDCapを探索し、これを侵入面として利用する。 | 不明 | 不明 | 高 | `source--gtig-unc6508-medical-research-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 専有AI研究の窃取と侵害環境上でのローカルLLM基盤展開 | cyber-espionage | 不明 | 不明 | 2026-09-08 |  |  |  |  | GTIGは本クラスタが専有AI研究を特に標的とすると述べ、加えて侵害したクラウド環境へローカルLLM基盤を展開するUNC6508の疑いのある活動を観測したと記載する。ローカルに配置したオープンウェイトモデルを用いることで商用AI APIの監視を回避しつつ、被害組織の計算資源を流用する。本クラスタはAIツールの設定・利用方法の調査を継続しており、オープンモデルのローカル利用やAIモデル自体の脆弱性の研究にも及んでいる。 | 中 | `source--gtig-adversarial-ai-2026` |
| REDCapサーバー悪用による北米の医学・防衛研究機関への長期諜報活動 | cyber-espionage | 2023-09 | 2025-11 | 2026-06-15 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--ee55e5e8faa5dd675d7b, target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--e7608f51421ca8b1e297 | malware--infinitered | ttp--activity-rule--6908a18dbde1798c1adb, ttp--activity-rule--d4828060da1abc7a42ef | victim--activity-rule--3e3b5dda438e2bf439b5 | 約26か月にわたる諜報キャンペーン。外部公開されたREDCapサーバーを悪用し、現行版と併存する脆弱な旧バージョンを探索してダウングレード攻撃を可能にする。侵入後はWebシェル help.php を設置して永続化し、内部偵察と資格情報探索を行ったうえで、侵害から約3か月後にINFINITEREDを展開する。アップグレード処理へ介入して版更新をまたぐ永続化を確立し、トロイ化した認証ファイルで資格情報を収集してドメイン管理者アカウントへ横展開する。持ち出しはメールのコンテンツコンプライアンス規則「Patroit」を作成し、地政学政策、軍事戦略、先端技術、医学研究に関する正規表現に一致したメールを攻撃者管理のGmailアドレスへ密かにBCC転送する方式である。標的は米国とカナダの著名な臨床医療機関、主要な学術研究センター、軍関連衛生機関、専門職団体、保健規制機関で、研究分野は分子探索、臨床薬剤試験、公衆衛生政策、軍の即応性、人工知能、無人機システム、攻撃的サイバー計画に及ぶ。 | 高 | `source--gtig-unc6508-medical-research-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 専有AI研究の窃取と侵害環境上でのローカルLLM基盤展開 | UNC6508 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| REDCapサーバー悪用による北米の医学・防衛研究機関への長期諜報活動 | UNC6508 | INFINITERED | T1083 File and Directory Discovery, T1505.003 Web Shell | 情報なし | 米国, カナダ, 医療・ヘルスケア, 教育・研究 | 被害事例: REDCapサーバー悪用による北米の医学・防衛研究機関への長期諜報活動 | 高 |

GTIGは2026-06-15の報告で、2023年9月の最初期の侵害から2025年11月まで約26か月にわたる活動を記述した。2026-09-08のAI脅威報告では、専有AI研究の窃取という観点から本クラスタを再度取り上げている。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | カナダ | 活動「REDCapサーバー悪用による北米の医学・防衛研究機関への長期諜報活動」の記述で標的として明示された国・地域。 | 2023-09 | 2025-11 | 中 | `source--gtig-unc6508-medical-research-2026` |
| countries | 米国 | 活動「REDCapサーバー悪用による北米の医学・防衛研究機関への長期諜報活動」の記述で標的として明示された国・地域。 | 2023-09 | 2025-11 | 中 | `source--gtig-unc6508-medical-research-2026` |
| regions | 北米 | 活動「REDCapサーバー悪用による北米の医学・防衛研究機関への長期諜報活動」の記述で標的地域として北米が明示されている。 | 2023-09 | 2025-11 | 中 | `source--gtig-unc6508-medical-research-2026` |
| sectors | 医療・ヘルスケア | 活動「REDCapサーバー悪用による北米の医学・防衛研究機関への長期諜報活動」の記述で標的として明示された産業。 | 2023-09 | 2025-11 | 中 | `source--gtig-unc6508-medical-research-2026` |
| sectors | 教育・研究 | 活動「REDCapサーバー悪用による北米の医学・防衛研究機関への長期諜報活動」の記述で標的として明示された産業。 | 2023-09 | 2025-11 | 中 | `source--gtig-unc6508-medical-research-2026` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: REDCapサーバー悪用による北米の医学・防衛研究機関への長期諜報活動 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--ee55e5e8faa5dd675d7b, target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--e7608f51421ca8b1e297 | malware--infinitered | ttp--activity-rule--6908a18dbde1798c1adb, ttp--activity-rule--d4828060da1abc7a42ef | メール／メールアカウント, サーバー |  | 2023-09 | 2025-11 | 2026-06-15 | 高 | `source--gtig-unc6508-medical-research-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1083 | File and Directory Discovery | アップグレード処理へ介入して版更新をまたぐ永続化を確立し、トロイ化した認証ファイルで資格情報を収集してドメイン管理者アカウントへ横展開する。 |  | activity--unc6508--redcap-medical-research-2023-2025 | 2023-09 | 2025-11 | 中 | `source--gtig-unc6508-medical-research-2026` |
| Persistence | T1505.003 | Web Shell | 侵入後はWebシェル help.php を設置して永続化し、内部偵察と資格情報探索を行ったうえで、侵害から約3か月後にINFINITEREDを展開する。 | malware--infinitered | activity--unc6508--redcap-medical-research-2023-2025 | 2023-09 | 2025-11 | 中 | `source--gtig-unc6508-medical-research-2026` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| GTIGはインフラ重複、REDCapサーバー上でのINFINITEREDの一貫した使用、医学研究・防衛分野への特異的な標的選択を根拠に、本活動をUNC6508へ高確度で帰属している。 | 高 | `source--gtig-unc6508-medical-research-2026` | 単一ベンダーによる帰属であり、政府による帰属や起訴・制裁資料は確認できていない。 |
| 初期侵入が外部公開されたREDCapサーバーの悪用に依存しており、研究データ基盤そのものが侵入面になっている。アップグレード処理への介入により版更新をまたぐ永続化が成立する点が対処を難しくする。 | 高 | `source--gtig-unc6508-medical-research-2026` | 原文が攻撃チェーンとINFINITEREDのドロッパー実装を具体的に記述している。 |
| 専有AI研究とモデルが明確な収集目標であり、侵害環境上でのローカルLLM展開は商用AI APIの監視回避と被害組織の計算資源流用を同時に達成する。 | 中 | `source--gtig-adversarial-ai-2026` | GTIGがローカルLLM展開を suspected と留保しているため確度はmediumとする。 |

### 情報ギャップ

- GTIG 2026-06-15 報告が掲載するIOC(SHA-256 7件、IP 23.169.65.49、メールアドレス BebitaBarefoot774@gmail.com)およびホスト指標(GUID区切り子 b49e334d-9c01-463e-9bc5-00a6920fb66e、セッションID接頭辞 xc32038474a)は、本プロファイルの iocs.json / artifacts.csv へ未取込である。取込にはAGENT.mdのIOC/artifact規則に沿った観測単位の登録が必要。
- 被害組織名は原文で匿名化されており、個別の被害事例を特定できていない。
- 2025年11月以降の活動継続状況は確認できていない。

### 不確実性

- 確認できた一次資料はGTIGの2本(2026-06-15、2026-09-08)であり、いずれも同一ベンダーである。独立した別ベンダーまたは政府・CERT・法執行機関による本クラスタへの言及は得られていない。台帳の昇格閾値(独立した一次資料2本以上、または政府機関等の言及)を厳密には満たしていないが、利用者の判断でプロファイル化した。
- ローカルLLM基盤の展開はGTIGが「suspected UNC6508 activity」と留保しており、本クラスタの活動と確定していない。
- 既存の他プロファイルとの重複の有無は未確認である。GTIGは本クラスタに旧称や他ベンダー別名を示していない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--gtig-unc6508-medical-research-2026 | Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research | Google Threat Intelligence Group | 2026-06-15 | https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research | vendor-research | TLP:CLEAR | 高 |
| source--gtig-adversarial-ai-2026 | GTIG AI Threat Tracker: From Prompting to Autonomy - The Evolution of Adversarial AI | Google Threat Intelligence Group | 2026-09-08 | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai | vendor-research | TLP:CLEAR | 高 |

## 自由記述

本プロファイルは2026-09-10の日次チェックで未帰属クラスタ台帳から昇格したものであり、status は draft から開始する。
