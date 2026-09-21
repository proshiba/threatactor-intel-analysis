# Konni 脅威アクタープロファイル

- プロファイルID: `actor--konni`
- 状態: draft
- 更新日時: 2026-09-21T04:38:04Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Konni Groupは同名RATに由来する活動集合で、2014年以降の情報窃取作戦と、KONNI、NOKKI、CARROTBAT、CARROTBALL、SYSCON等の利用が報告されている。アクター名とマルウェア名を分離し、個別作戦の帰属確度を保持する。

## アクター名とAlias

- 正規名: **Konni**
- 初回観測: 2014
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
| espionage | Unit 42 describes sustained information-stealing campaigns and targeting of government and North Korea-linked individuals. | 中 | `source--unit42-fractured-statue-2020` | The operational objective is explicit; state sponsorship is not inferred. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| TA406 | overlaps-with | Proofpoint states that TA406 overlaps activity publicly tracked as Konni and Opal Sleet; Check Point directly attributes the January 2026 report's campaign to the KONNI cluster. | 中 | `source--proofpoint-ta406-konni-boundary-2025`, `source--checkpoint-konni-ai-backdoor-2026` |

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
| microsoft-threat-actor-mapping | Opal Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Opal Sleet | canonical-name | 高 | KP | https://nsfocusglobal.com/the-new-apt-group-darkcasino-and-the-global-surge-in-winrar-0-day-exploits/<br>https://paper.seebug.org/3031/<br>https://www.rewterz.com/rewterz-news/rewterz-threat-alert-konni-apt-group-active-iocs-11 |
| misp-microsoft-activity-group | Opal Sleet | canonical-name | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Kimsuky | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--carrotball | CARROTBALL | Unit 42がKonni Groupの活動で確認したCARROTBALLマルウェア。 | 2019-10 | 2019-10 | 高 | `source--unit42-fractured-statue-2020` |
| malware--carrotbat | CARROTBAT | Unit 42がKonni Groupの活動で確認したCARROTBATマルウェア。 | 2018 | 2019-10 | 高 | `source--unit42-fractured-statue-2020` |
| malware--konni | KONNI | Unit 42がKonni Groupの活動で確認したKONNIマルウェア。 | 2014 | 2017 | 中 | `source--unit42-fractured-statue-2020` |
| malware--nokki | NOKKI | Unit 42がKonni Groupの活動で確認したNOKKIマルウェア。 | 2018 | 不明 | 中 | `source--unit42-fractured-statue-2020` |
| malware--syscon | SYSCON | Unit 42がKonni Groupの活動で確認したSYSCONマルウェア。 | 2019-07 | 2019-10 | 高 | `source--unit42-fractured-statue-2020` |

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
| Google広告を悪用しEndRATを配布する新たなスピアフィッシング攻撃 | phishing-campaign | 不明 | 不明 | 2026-01-20 | target--activity-rule--country--6cb716c577f256f44a3e |  | ttp--activity-rule--8874df6d75dd53844b7d | victim--activity-rule--ee2a9cdcfc4e4e4ad73d | 韓国組織を狙うKonni APTの作戦「Poseidon」が確認され、Google広告基盤を悪用してEndRATを配布するスピアフィッシングを実施。 メール内の偽装URLはad.doubleclick.net経由の正規広告トラフィックに見せかけ、侵害WordPressへ誘導して不正ZIPを取得させる。 ZIP内のLNKがAutoItスクリプトを起動し、PDF風に偽装してメモリ上にEndRAT系RATをロード、追加操作なしで感染を成立。 不可視テキストのパディングでAI検知を回避し、や1×1ピクセルの透過画像を使って開封を追跡、C2識別子「endServer9688」「endClient9688」など内部アーティファクトも確認。 攻撃者は北朝鮮人権団体や金融機関への成りすましで信用を獲得し、取引確認書や通知文書に偽装した誘導を行う。 | 中 | `source--daily-04ea119cefbe5973a36c` |
| 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | phishing-campaign | 不明 | 不明 | 2025-05-14 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--sector--210dddb39397dbe50e91 |  | ttp--activity-rule--4a21572c08119350dbce, ttp--activity-rule--a99b07bd6fac90ad2cf9 | victim--activity-rule--2e0d34b8d92fddc23fdc | 北朝鮮支援のハッカーグループ「Konni（TA406）」が、ウクライナ政府機関を標的に情報収集活動を実施。 フィッシングメールでシンクタンクを装い、政治・軍事イベントに関するリンクを送信。 リンク先でパスワード付きRARファイルを配布し、PowerShellスクリプトで感染させる。 攻撃の目的は、北朝鮮軍のウクライナ派遣に伴うリスク評価とロシアからの追加要請の可能性を分析すること。 攻撃には、偽のMicrosoftセキュリティ警告を用いた認証情報の収集も含まれる。 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析 | phishing-campaign | 不明 | 不明 | 2026-03-17 | target--activity-rule--sector--d406c8e5b7fa7aeff7d2 |  | ttp--activity-rule--d913e43869f268f61241, ttp--activity-rule--fa5094b7781f1eaa6aed | victim--activity-rule--624fced7f6106b0b0296 | Geniansは、北朝鮮人権講師の任命通知を装うスピアフィッシングから始まるKonniグループの多段階攻撃を分析し、初期侵入から二次拡散までの流れを整理した。 受信者が文書に見せかけた悪性LNKを実行すると、PowerShellが埋め込みデータを復号して偽装PDFを展開し、C2から追加ペイロードを取得して永続化する。 C2からはAutoIT3.exeとPDFに偽装したAutoItScriptがダウンロード及び実行される。 解析の結果EndRAT系の挙動が確認され、さらにEndRAT・RftRAT・RemcosRATの複数RATが段階的に展開されていた。 攻撃者は侵害端末上のKakaoTalk PCセッションに不正アクセスし、友だち一覧から選んだ相手へ北朝鮮関連の誘引ファイルを再送して信頼連鎖で拡散した。 記事は、単一IOCの遮断だけでは不十分であり、LNK実行後の異常プロセス、永続化、情報窃取、メッセンジャー悪用をEDRで相関検知すべきだと強調する。 | 高 | `source--daily-22cb41823695505fc8c4` |
| KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布 | infrastructure-operation | 2025-10 | 不明 | 2026-01-22 | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df, target--targeting-audit--country--6f732ffcb5e7be0ccb47, target--targeting-audit--country--f63c50e68288d7ada0d3 |  |  | victim--activity-rule--3313dadf412423edd869 | Check Point Researchは、KONNIに関連付けたフィッシング活動で、ブロックチェーン関連の開発者・エンジニアを狙うおとり文書と悪性LNKを確認した。LNKはPowerShellローダから永続化・UAC回避・分析回避・C2タスク実行機能を持つPowerShellバックドアを展開する。2025年10月にアップロードされた初期亜種も確認され、検体投稿元は日本・豪州・インドを含むが、投稿元を被害国の確定値とはしない。Check PointはKONNIへ直接帰属し、ProofpointはTA406をKonni/Opal Sleet活動との重複として扱うため、TA406との完全同一性は断定しない。 | 高 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| Fractured Statueキャンペーン | phishing-campaign | 2019-07 | 2019-10 | 2020-01-23 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--210dddb39397dbe50e91 | malware--carrotbat, malware--carrotball, malware--syscon |  | victim--activity-rule--7a8170be712b1017963d | Unit 42は2019年7月から10月、米国政府機関と朝鮮半島情勢に職業上関係する米国外の外国人を標的としたスピアフィッシングを観測した。ロシア語の朝鮮半島情勢を題材に、CARROTBATまたはCARROTBALLからSYSCONを配布した。 | 中 | `source--unit42-fractured-statue-2020` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Google広告を悪用しEndRATを配布する新たなスピアフィッシング攻撃 | Konni | 情報なし | T1036 Masquerading | 情報なし | 韓国 | 被害事例: Google広告を悪用しEndRATを配布する新たなスピアフィッシング攻撃 | 中 |
| 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | Konni | 情報なし | T1566.002 Spearphishing Link, T1059.001 PowerShell | 情報なし | ウクライナ, 政府・行政 | 被害事例: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 中 |
| KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析 | Konni | 情報なし | T1105 Ingress Tool Transfer, T1036 Masquerading | 情報なし | 非営利・市民社会 | 被害事例: KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析 | 高 |
| KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布 | Konni | 情報なし | 情報なし | 情報なし | 暗号資産・Web3, IT・ソフトウェア, インド, 日本 | 被害事例: KONNIによるブロックチェーン技術者標的化 | 高 |
| Fractured Statueキャンペーン | Konni | CARROTBALL, CARROTBAT, SYSCON | 情報なし | 情報なし | 米国, 政府・行政 | 被害事例: Fractured Statueキャンペーン | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | 活動「KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布」の記述で標的・被害国として明示されている。 | 2025-10 | 不明 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| countries | ウクライナ | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| countries | 日本 | 活動「KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布」の記述で標的・被害国として明示されている。 | 2025-10 | 不明 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| countries | 米国 | 活動「Fractured Statueキャンペーン」の記述で標的として明示された国・地域。 | 2019-07 | 2019-10 | 中 | `source--unit42-fractured-statue-2020` |
| countries | 韓国 | 活動「Google広告を悪用しEndRATを配布する新たなスピアフィッシング攻撃」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-04ea119cefbe5973a36c` |
| regions | 東アジア | 日本、韓国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--daily-04ea119cefbe5973a36c`, `source--proofpoint-ta406-konni-boundary-2025` |
| sectors | 政府・行政 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された産業。 | 2019-07 | 2019-10 | 中 | `source--daily-a70f8f04454a7b9e932e`, `source--unit42-fractured-statue-2020` |
| sectors | 暗号資産・Web3 | 活動「KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布」の記述で標的として明示された産業。 | 2025-10 | 2025-10 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| sectors | IT・ソフトウェア | 活動「KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布」の記述で標的として明示された産業。 | 2025-10 | 2025-10 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| sectors | 非営利・市民社会 | 活動「KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-22cb41823695505fc8c4` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--sector--210dddb39397dbe50e91 |  | ttp--activity-rule--4a21572c08119350dbce, ttp--activity-rule--a99b07bd6fac90ad2cf9 | メール／メールアカウント | espionage: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 不明 | 不明 | 2025-05-14 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| 被害事例: KONNIによるブロックチェーン技術者標的化 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df |  |  |  |  | 2025-10 | 不明 | 2026-01-22 | 高 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| 被害事例: KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--d406c8e5b7fa7aeff7d2 |  | ttp--activity-rule--d913e43869f268f61241, ttp--activity-rule--fa5094b7781f1eaa6aed | エンドポイント |  | 不明 | 不明 | 2026-03-17 | 高 | `source--daily-22cb41823695505fc8c4` |
| 被害事例: Fractured Statueキャンペーン | 非公開 | anonymous | unknown | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--210dddb39397dbe50e91 | malware--carrotball, malware--carrotbat, malware--syscon |  | OT／ICS |  | 2019-07 | 2019-10 | 2020-01-23 | 中 | `source--unit42-fractured-statue-2020` |
| 被害事例: Google広告を悪用しEndRATを配布する新たなスピアフィッシング攻撃 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6cb716c577f256f44a3e |  | ttp--activity-rule--8874df6d75dd53844b7d | メール／メールアカウント, サーバー |  | 不明 | 不明 | 2026-01-20 | 中 | `source--daily-04ea119cefbe5973a36c` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1566.002 | Spearphishing Link | フィッシングメールでシンクタンクを装い、政治・軍事イベントに関するリンクを送信。 |  | activity--daily-4c04ed57332555303c93 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| Stealth | T1036 | Masquerading | ZIP内のLNKがAutoItスクリプトを起動し、PDF風に偽装してメモリ上にEndRAT系RATをロード、追加操作なしで感染を成立。 |  | activity--daily-23024095c33771cf0ad3 | 不明 | 不明 | 中 | `source--daily-04ea119cefbe5973a36c` |
| Execution | T1059.001 | PowerShell | リンク先でパスワード付きRARファイルを配布し、PowerShellスクリプトで感染させる。 |  | activity--daily-4c04ed57332555303c93 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| Command And Control | T1105 | Ingress Tool Transfer | 受信者が文書に見せかけた悪性LNKを実行すると、PowerShellが埋め込みデータを復号して偽装PDFを展開し、C2から追加ペイロードを取得して永続化する。 |  | activity--daily-5ff1d091898ba9ae1303 | 不明 | 不明 | 中 | `source--daily-22cb41823695505fc8c4` |
| Stealth | T1036 | Masquerading | C2からはAutoIT3.exeとPDFに偽装したAutoItScriptがダウンロード及び実行される。 |  | activity--daily-5ff1d091898ba9ae1303 | 不明 | 不明 | 中 | `source--daily-22cb41823695505fc8c4` |
| Command And Control | T1001 | Data Obfuscation | 1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques 11 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Collection | T1005 | Data from Local System | Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques 11 ATT&CK : The Adv |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Discovery | T1016 | System Network Configuration Discovery | Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Stan |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Stealth | T1027.001 | Binary Padding | Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Stealth | T1027.010 | Command Obfuscation | e T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File a |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Stealth | T1036.007 | Double File Extension | / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T100 |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | ware Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques 11 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge 12 MITRE ATT&CK Software - KONNI |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | 3 CommandandScriptingInterpreter:Windows CommandShell T1059.005 CommandandScriptingInterpreter:Visual Basic T1204.002 User Execution:Malicious File Persistence T1053.005 ScheduledTask/Job:ScheduledTask DefenseEvasion T1070.004 Indicator Removal:FileDeletionT1140 Deobfuscate/DecodeFiles or Information Discovery T1057 Process DiscoveryT1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1119 AutomatedCollectionCommandand T107 |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Discovery | T1057 | Process Discovery | scation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Execution | T1059.001 | PowerShell | cription Reconnaissance T1598.002 Phishing for Information: Spearphishing Attachment Initial Access T1566.001 Phishing: Spearphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Regis |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--9f9859221e0eb3bc` |
| Execution | T1059.003 | Windows Command Shell | on: Spearphishing Attachment Initial Access T1566.001 Phishing: Spearphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.00 |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Execution | T1059.005 | Visual Basic | arphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscat |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Stealth | T1070.004 | File Deletion | 59.005 CommandandScriptingInterpreter:Visual Basic T1204.002 User Execution:Malicious File Persistence T1053.005 ScheduledTask/Job:ScheduledTask DefenseEvasion T1070.004 Indicator Removal:FileDeletionT1140 Deobfuscate/DecodeFiles or Information Discovery T1057 Process DiscoveryT1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1119 AutomatedCollectionCommandand T1071.001 ApplicationLayer Protocol: 10 Konni 9 https://attac |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Command And Control | T1071 | Application Layer Protocol | eDeletion T1070.004SystemInformationDiscovery T1082FileandDirectoryDiscovery T1083ProcessDiscovery T1057ExfiltrationOverC2Channel T1041ApplicationLayerProtocol T1071 11 |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a` |
| Command And Control | T1071.001 | Web Protocols | s or Information Discovery T1057 Process DiscoveryT1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1119 AutomatedCollectionCommandand T1071.001 ApplicationLayer Protocol: 10 Konni 9 https://attack.mitre.org/tactics/enterprise/ Genians SecurityCenter 46 |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Discovery | T1082 | System Information Discovery | rading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Discovery | T1083 | File and Directory Discovery | Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Collection | T1119 | Automated Collection | DeletionT1140 Deobfuscate/DecodeFiles or Information Discovery T1057 Process DiscoveryT1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1119 AutomatedCollectionCommandand T1071.001 ApplicationLayer Protocol: 10 Konni 9 https://attack.mitre.org/tactics/enterprise/ Genians SecurityCenter 46 |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Command And Control | T1132.001 | Standard Encoding | Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques 11 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge 12 MITRE ATT&CK Software - K |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | bfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Cont |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Execution | T1204.002 | Malicious File | ipting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Ma |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--9f9859221e0eb3bc` |
| Discovery | T1518 | Software Discovery | tion Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/D |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Collection | T1560 | Archive Collected Data | TheKonni APTChronicle: TracingTheir Intelligence-DrivenAttackChain ArchiveCollectedData T1560 Mitigations ● Regularlyeducateandtrainemployeesabout thedangersof spear-phishingattacks.Teachthemhowtorecognizephishingattempts, especiallythoseinvolvingmaliciouslinks. Encouragea"thinkbeforeyouclick" mentalitytoreducethechancesof fallingfor theseattacks.● Implement applicationw |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a` |
| Initial Access | T1566.001 | Spearphishing Attachment | Matrix - Konni12 Group Descriptions Tactic Technique Description Reconnaissance T1598.002 Phishing for Information: Spearphishing Attachment Initial Access T1566.001 Phishing: Spearphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persi |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Initial Access | T1566.002 | Spearphishing Link | ishingfor Information:SpearphishingLink ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.005 CommandandScriptingInterpreter:Visual Basic T1204.002 User Execution:Malici |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Initial Access | T1566.003 | Spearphishing via Service | nk ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.005 CommandandScriptingInterpreter:Visual Basic T1204.002 User Execution:Malicious File Persistence T1053.005 Schedu |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Resource Development | T1585.002 | Email Accounts | ue Description Reconnaissance T1598.002 Phishingfor Information:SpearphishingAttachment T1598.003 Phishingfor Information:SpearphishingLink ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Window |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Resource Development | T1585.003 | Cloud Accounts | shingfor Information:SpearphishingAttachment T1598.003 Phishingfor Information:SpearphishingLink ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.005 CommandandScriptin |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Reconnaissance | T1598.002 | Spearphishing Attachment | 44 07. 공격 지표 (Indicator of Attack) a. MITRE ATT&CK11 Matrix - Konni12 Group Descriptions Tactic Technique Description Reconnaissance T1598.002 Phishing for Information: Spearphishing Attachment Initial Access T1566.001 Phishing: Spearphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Script |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--9f9859221e0eb3bc` |
| Reconnaissance | T1598.003 | Spearphishing Link | Matrix - MITREATT&CK Matrix- Konni GroupDescriptions 9 10 Tactic Technique Description Reconnaissance T1598.002 Phishingfor Information:SpearphishingAttachment T1598.003 Phishingfor Information:SpearphishingLink ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScripti |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |

## IOC／artifact概要

- IOC値: 268件
- IOC観測: 409件
- 複数攻撃で観測: 0件
- 要レビュー候補: 15件
- 非IOC artifact観測: 282件（`artifacts.csv`）

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
| source--daily-04ea119cefbe5973a36c | Google広告を悪用しEndRATを配布する新たなスピアフィッシング攻撃 | cybersecuritynews.com | 2026-01-20 | https://cybersecuritynews.com/new-spear-phishing-attack-abusing-google-ads/ | osint-report | TLP:CLEAR | 中 |
| source--daily-22cb41823695505fc8c4 | KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析 | genians.co.kr | 2026-03-17 | https://www.genians.co.kr/en/blog/threat_intelligence/kakaotalk | osint-report | TLP:CLEAR | 中 |
| source--daily-96093ec62047a80740ea | Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に | bleepingcomputer.com | 2026-01-26 | https://www.bleepingcomputer.com/news/security/konni-hackers-target-blockchain-engineers-with-ai-built-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-a70f8f04454a7b9e932e | 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | bleepingcomputer.com | 2025-05-14 | https://www.bleepingcomputer.com/news/security/north-korea-ramps-up-cyberspying-in-ukraine-to-assess-war-risk/ | osint-report | TLP:CLEAR | 中 |
| source--konni--079e51a056632f53 | 20230727 threat inteligence report Konni |  | 2023-07-27 | konni/20230727_threat_inteligence_report_Konni.pdf | report | TLP:CLEAR | 中 |
| source--konni--2ab1db8e5d0c048a | konni ioclist 202111 |  | 2021-11 | konni/konni_ioclist_202111.csv | structured-data | TLP:CLEAR | 中 |
| source--konni--5b6e99ac261cea7a | konni threat insight paper triple threat N Korea aligned TA406 steals scams spies |  | 不明 | konni/konni-threat-insight-paper-triple-threat-N-Korea-aligned-TA406-steals-scams-spies.pdf | report | TLP:CLEAR | 中 |
| source--konni--8c179de8de042c5a | the konni apt chronicle tracing their intelligence driven attack chain |  | 不明 | konni/the-konni-apt-chronicle-tracing-their-intelligence-driven-attack-chain.pdf | report | TLP:CLEAR | 中 |
| source--konni--9f9859221e0eb3bc | 20230926 threat inteligence report konniapt |  | 2023-09-26 | konni/20230926_threat_inteligence_report_konniapt.pdf | report | TLP:CLEAR | 中 |
| source--konni--a7ca5a441a2a4faf | ReadME |  | 不明 | konni/ReadME.md | repository-notes | TLP:CLEAR | 中 |
| source--konni--e22c456560b2d889 | bluesky |  | 不明 | konni/bluesky.txt | text-data | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unit42-fractured-statue-2020 | The Fractured Statue Campaign: U.S. Government Agency Targeted in Spear-Phishing Attacks | Palo Alto Networks Unit 42 | 2020-01-23 | https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/ | vendor-research | TLP:CLEAR | 高 |
| source--checkpoint-konni-ai-backdoor-2026 | KONNI Adopts AI to Generate PowerShell Backdoors | Check Point Research | 2026-01-22 | https://research.checkpoint.com/2026/konni-targets-developers-with-ai-malware/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--proofpoint-ta406-konni-boundary-2025 | TA406 Pivots to the Front | Proofpoint Threat Research | 2025-05-13 | https://www.proofpoint.com/us/blog/threat-insight/ta406-pivots-front | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
