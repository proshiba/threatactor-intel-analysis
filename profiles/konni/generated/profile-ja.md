# Konni 脅威アクタープロファイル

- プロファイルID: `actor--konni`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Konniの標準化プロファイル。リポジトリ内の専用資料7件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Konni**
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
| microsoft-threat-actor-mapping | Opal Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Opal Sleet | canonical-name | 高 | KP | https://nsfocusglobal.com/the-new-apt-group-darkcasino-and-the-global-surge-in-winrar-0-day-exploits/<br>https://paper.seebug.org/3031/<br>https://www.rewterz.com/rewterz-news/rewterz-threat-alert-konni-apt-group-active-iocs-11 |
| misp-microsoft-activity-group | Opal Sleet | canonical-name | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

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
| Google広告を悪用しEndRATを配布する新たなスピアフィッシング攻撃 | phishing-campaign | 不明 | 不明 | 2026-01-20 |  |  | ttp--activity-rule--8874df6d75dd53844b7d |  | 韓国組織を狙うKonni APTの作戦「Poseidon」が確認され、Google広告基盤を悪用してEndRATを配布するスピアフィッシングを実施。 メール内の偽装URLはad.doubleclick.net経由の正規広告トラフィックに見せかけ、侵害WordPressへ誘導して不正ZIPを取得させる。 ZIP内のLNKがAutoItスクリプトを起動し、PDF風に偽装してメモリ上にEndRAT系RATをロード、追加操作なしで感染を成立。 不可視テキストのパディングでAI検知を回避し、や1×1ピクセルの透過画像を使って開封を追跡、C2識別子「endServer9688」「endClient9688」など内部アーティファクトも確認。 攻撃者は北朝鮮人権団体や金融機関への成りすましで信用を獲得し、取引確認書や通知文書に偽装した誘導を行う。 | 中 | `source--daily-04ea119cefbe5973a36c` |
| 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | phishing-campaign | 不明 | 不明 | 2025-05-14 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a, target--activity-rule--country--f0d8df51439c4d0f3a05, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--4a21572c08119350dbce, ttp--activity-rule--a99b07bd6fac90ad2cf9 | victim--activity-rule--2e0d34b8d92fddc23fdc | 北朝鮮支援のハッカーグループ「Konni（TA406）」が、ウクライナ政府機関を標的に情報収集活動を実施。 フィッシングメールでシンクタンクを装い、政治・軍事イベントに関するリンクを送信。 リンク先でパスワード付きRARファイルを配布し、PowerShellスクリプトで感染させる。 攻撃の目的は、北朝鮮軍のウクライナ派遣に伴うリスク評価とロシアからの追加要請の可能性を分析すること。 攻撃には、偽のMicrosoftセキュリティ警告を用いた認証情報の収集も含まれる。 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析 | phishing-campaign | 不明 | 不明 | 2026-03-17 | target--activity-rule--sector--d406c8e5b7fa7aeff7d2 |  | ttp--activity-rule--d913e43869f268f61241, ttp--activity-rule--fa5094b7781f1eaa6aed | victim--activity-rule--624fced7f6106b0b0296 | Geniansは、北朝鮮人権講師の任命通知を装うスピアフィッシングから始まるKonniグループの多段階攻撃を分析し、初期侵入から二次拡散までの流れを整理した。 受信者が文書に見せかけた悪性LNKを実行すると、PowerShellが埋め込みデータを復号して偽装PDFを展開し、C2から追加ペイロードを取得して永続化する。 C2からはAutoIT3.exeとPDFに偽装したAutoItScriptがダウンロード及び実行される。 解析の結果EndRAT系の挙動が確認され、さらにEndRAT・RftRAT・RemcosRATの複数RATが段階的に展開されていた。 攻撃者は侵害端末上のKakaoTalk PCセッションに不正アクセスし、友だち一覧から選んだ相手へ北朝鮮関連の誘引ファイルを再送して信頼連鎖で拡散した。 記事は、単一IOCの遮断だけでは不十分であり、LNK実行後の異常プロセス、永続化、情報窃取、メッセンジャー悪用をEDRで相関検知すべきだと強調する。 | 高 | `source--daily-22cb41823695505fc8c4` |
| Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に | infrastructure-operation | 不明 | 不明 | 2026-01-26 | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df |  | ttp--activity-rule--7f8cf8af7ca879bb493f, ttp--activity-rule--e73e2a355fda877065d3 | victim--activity-rule--3313dadf412423edd869 | 北朝鮮系Konni（Opal Sleet/TA406）がAI生成と見られるPowerShellマルウェアでブロックチェーン開発者・技術者を標的化。 Check Point分析では日本・豪州・インド由来の検体が確認され、APACを中心とする最近の活動とされる。 攻撃はDiscordホストのリンクからZIPを配布、PDFおとりと悪性LNKで開始しPowerShellローダでDOCXとCABを展開。 CABにはPSバックドア・2つのBAT・UAC回避用実行ファイルが含まれ、OneDrive偽装のタスクでXOR暗号化スクリプトを定期実行・痕跡削除。 バックドアは難読化されC2と定期通信、整然としたコメントやUUID記述からAI支援生成の痕跡が示唆されKonniに帰属。 | 高 | `source--daily-96093ec62047a80740ea` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Google広告を悪用しEndRATを配布する新たなスピアフィッシング攻撃 | Konni | 情報なし | T1036 Masquerading | 情報なし | 情報なし | 情報なし | 中 |
| 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | Konni | 情報なし | T1566.002 Spearphishing Link, T1059.001 PowerShell | 情報なし | ウクライナ, ロシア, 北朝鮮, 政府・行政, 防衛・軍事, 教育・研究 | 被害事例: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 中 |
| KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析 | Konni | 情報なし | T1105 Ingress Tool Transfer, T1036 Masquerading | 情報なし | 非営利・市民社会 | 被害事例: KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析 | 高 |
| Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に | Konni | 情報なし | T1053.005 Scheduled Task, T1027 Obfuscated Files or Information | 情報なし | 暗号資産・Web3, IT・ソフトウェア | 被害事例: Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ウクライナ | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| countries | ロシア | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| countries | 北朝鮮 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-04ea119cefbe5973a36c`, `source--daily-a70f8f04454a7b9e932e` |
| regions | 東欧 | ウクライナ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| sectors | 政府・行政 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| sectors | 暗号資産・Web3 | 活動「Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-96093ec62047a80740ea` |
| sectors | IT・ソフトウェア | 活動「Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-96093ec62047a80740ea` |
| sectors | 防衛・軍事 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| sectors | 非営利・市民社会 | 活動「KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-22cb41823695505fc8c4` |
| sectors | 教育・研究 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a, target--activity-rule--country--f0d8df51439c4d0f3a05, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--4a21572c08119350dbce, ttp--activity-rule--a99b07bd6fac90ad2cf9 | メール／メールアカウント | espionage: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 不明 | 不明 | 2025-05-14 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| 被害事例: Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df |  | ttp--activity-rule--7f8cf8af7ca879bb493f, ttp--activity-rule--e73e2a355fda877065d3 |  |  | 不明 | 不明 | 2026-01-26 | 高 | `source--daily-96093ec62047a80740ea` |
| 被害事例: KonniグループによるスピアフィッシングとKakaoTalk連動型脅威キャンペーンの分析 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--d406c8e5b7fa7aeff7d2 |  | ttp--activity-rule--d913e43869f268f61241, ttp--activity-rule--fa5094b7781f1eaa6aed | エンドポイント |  | 不明 | 不明 | 2026-03-17 | 高 | `source--daily-22cb41823695505fc8c4` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1566.002 | Spearphishing Link | フィッシングメールでシンクタンクを装い、政治・軍事イベントに関するリンクを送信。 |  | activity--daily-4c04ed57332555303c93 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | CABにはPSバックドア・2つのBAT・UAC回避用実行ファイルが含まれ、OneDrive偽装のタスクでXOR暗号化スクリプトを定期実行・痕跡削除。 |  | activity--daily-647f622408c58cbd428c | 不明 | 不明 | 中 | `source--daily-96093ec62047a80740ea` |
| Stealth | T1036 | Masquerading | ZIP内のLNKがAutoItスクリプトを起動し、PDF風に偽装してメモリ上にEndRAT系RATをロード、追加操作なしで感染を成立。 |  | activity--daily-23024095c33771cf0ad3 | 不明 | 不明 | 中 | `source--daily-04ea119cefbe5973a36c` |
| Execution | T1059.001 | PowerShell | リンク先でパスワード付きRARファイルを配布し、PowerShellスクリプトで感染させる。 |  | activity--daily-4c04ed57332555303c93 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| Command And Control | T1105 | Ingress Tool Transfer | 受信者が文書に見せかけた悪性LNKを実行すると、PowerShellが埋め込みデータを復号して偽装PDFを展開し、C2から追加ペイロードを取得して永続化する。 |  | activity--daily-5ff1d091898ba9ae1303 | 不明 | 不明 | 中 | `source--daily-22cb41823695505fc8c4` |
| Stealth | T1027 | Obfuscated Files or Information | バックドアは難読化されC2と定期通信、整然としたコメントやUUID記述からAI支援生成の痕跡が示唆されKonniに帰属。 |  | activity--daily-647f622408c58cbd428c | 不明 | 不明 | 中 | `source--daily-96093ec62047a80740ea` |
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

- IOC値: 169件
- IOC観測: 252件
- 複数攻撃で観測: 0件
- 要レビュー候補: 15件
- 非IOC artifact観測: 289件（`artifacts.csv`）

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

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
