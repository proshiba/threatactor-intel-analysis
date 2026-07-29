# LAPSUS$ 脅威アクタープロファイル

- プロファイルID: `actor--lapsus`
- 状態: draft
- 更新日時: 2026-07-29T15:39:42Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

LAPSUS$の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **LAPSUS$**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DEV-0537 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Strawberry Tempest | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [LAPSUS$](https://attack.mitre.org/groups/G1004) is cyber criminal threat group that has been active since at least mid-2021. [LAPSUS$](https://attack.mitre.org/groups/G1004) specializes in large-scale social engineering and extortion operations, including destructive attacks without the use of ransomware. The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.(Citation: BBC LAPSUS Apr 2022)(Citation: MSTIC DEV-0537 Mar 2022)(Citation: UNIT 42 LAPSUS Mar 2022) |
| Capability | Mimikatz |
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
| etda-threat-group-cards | Lapsus$ | canonical-name | 高 | Brazil | https://www.flashpoint-intel.com/blog/lapsus/<br>https://www.silentpush.com/blog/lapsus-group-an-emerging-dark-net-threat-actor<br>https://krebsonsecurity.com/2022/03/a-closer-look-at-the-lapsus-data-extortion-group/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Strawberry Tempest | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | LAPSUS | canonical-name | 高 |  | https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/<br>https://blog.checkpoint.com/2022/03/07/lapsus-ransomware-gang-uses-stolen-source-code-to-disguise-malware-files-as-trustworthy-check-point-customers-remain-protected/<br>https://www.crowdstrike.com/adversaries/slippy-spider/ |
| misp-microsoft-activity-group | Strawberry Tempest | canonical-name | 高 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | LAPSUS$ - G1004 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1004<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://unit42.paloaltonetworks.com/lapsus-group/ |
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
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| 英国、主要小売業へのサイバー攻撃を受けてセキュリティ対策を共有 | ransomware-extortion | 不明 | 不明 | 2025-05-06 |  |  |  | victim--activity-rule--39b4f4ac2f7d642ba592 | M&S、Co-op、Harrodsがサイバー攻撃を受け、NCSCが全企業に対策強化を呼びかけ。 攻撃者は従業員になりすまし、ITヘルプデスクを騙して認証情報を取得。 M&Sではランサムウェアが展開され、Co-opは暗号化前に攻撃を阻止。 Harrodsは侵入の試みを確認し、アクティブな対応としてインターネットアクセスを制限。結果、侵入は確認されず。 攻撃はDragonForce作戦により行われ、Scattered SpiderやLapsus$の戦術が使用された。 NCSCは、犠牲者や法執行機関と協力して犯人を特定しようとしており、現時点では攻撃が関連しているか、単一のアクターによる組織的なキャンペーンかについては推測を避けている。 | 中 | `source--daily-4cd1fe293925310c02b7` |
| ハッカーがサポートチケットを盗み、Discordがデータ侵害を公表 | ransomware-extortion | 不明 | 不明 | 2025-10-06 |  |  |  | victim--activity-rule--a861d5e217e49abc5df1 | Discordはサードパーティのサポート業者が侵害され、サポート由来の利用者データ流出を10月4日に公表。 攻撃は9月20日に発生し、サポート/Trust & Safetyとやり取りした一部ユーザーが影響。 流出は氏名/ユーザー名/メール/連絡先、IP、サポート宛のメッセージ/添付、政府ID画像、支払いの一部情報等。 犯人は漏えいデータの公開と引き換えに身代金を要求し、金銭目的の恐喝とみられる。 Scattered Lapsus$ HuntersがZendesk侵害を主張、Discordはアクセス遮断・調査・法執行機関連携を実施。 | 中 | `source--daily-9af96d00623df591e4cf` |
| ジャガー・ランドローバー、サイバー攻撃で操業停止をさらに1週間延長 | ransomware-extortion | 不明 | 不明 | 2025-09-17 |  |  |  | victim--activity-rule--f6b8cc9fa92a36275fde | ジャガー・ランドローバーは8月末に発生したサイバー攻撃の影響で、操業停止をさらに1週間延長すると発表。 同社は9月2日に大規模障害を公表し、先週は「一部データの窃取」を認め、従業員へ出勤停止を指示。 9月16日の更新で、生産再開は少なくとも9月24日（水）まで延期し、段階的な安全再起動を進めると説明。 犯行声明はScattered Lapsus$ HuntersがTelegram上で行い、内部SAP画面やランサム展開の主張を掲示。 ただしJLRは攻撃者の特定やランサムグループの関与について声明を出していない。 | 中 | `source--daily-96306c5877ca4244921e` |
| 英国政府、サイバー攻撃後のJLRに15億ポンドのローン保証を実施 | ransomware-extortion | 不明 | 不明 | 2025-09-30 | target--activity-rule--country--f9601e2d842c9a05202b, target--mitre-group--sector--54b3bca0635944bdc12d, target--mitre-group--sector--55400c7679dae0d87f49 |  |  | victim--activity-rule--b0219a533b5e0ea063d1 | 大規模サイバー攻撃で生産停止に陥ったJLR支援のため、英国政府が15億ポンドのローン保証を決定。 保証はUK Export FinanceのEDG枠で実施、直接融資ではなく民間融資を政府が保証、返済期間は5年。 攻撃は今月公表され、ITと製造に深刻な障害を引き起こし、複数工場の停止とデータ窃取をJLRが確認。 「Scattered Lapsus$ Hunters」が犯行を主張し、SAPのHOSTSファイル画像を掲示、ランサム展開を示唆。 JLRは段階的再開を近日開始予定で、NCSCや法執行・専門家と連携。保険未締結の報道もあり。 | 中 | `source--daily-04302db7cea311067bd3` |
| ジャガー・ランドローバー、最近のサイバー攻撃でデータ窃取を確認 | ransomware-extortion | 不明 | 不明 | 2025-09-11 |  |  |  | victim--activity-rule--c0c85e4a6755ba81ab68 | JLRは最近の攻撃で「一部のデータ」流出を確認し、規制当局へ通知。 9月2日に攻撃を公表、生産は深刻に混乱。NCSCと復旧・調査継続。 影響者には適宜連絡と説明。顧客影響など詳細は未回答。 犯行主体は未特定。既知ランサム勢力の犯行声明はなし。 Telegramの“Scattered Lapsus$ Hunters”が関与・ランサム展開を主張しSAP画面を提示。 | 中 | `source--daily-fb784abeaacd66b357b3` |
| Salesforce、広範なデータ窃取攻撃に対する身代金支払いを拒否 | ransomware-extortion | 不明 | 不明 | 2025-10-09 |  |  |  | victim--activity-rule--2c8886d199308b8ed57b | Salesforceは2025年の顧客向け大規模データ窃取に関し、脅威者への交渉・支払いを行わないと通知し、漏えい予告の脅威情報も共有。 「Scattered Lapsus$ Hunters」がbreachforums[.]hnで39社を恐喝、最大約10億件のデータ公開を示唆しSalesforceに一括支払いも要求。 攻撃は二段階で、①ITサポート偽装で悪性OAuthアプリ連携→DB窃取、②8月にSalesloft/DriftのOAuthトークン悪用→CRMから流出。 資格情報やAPIトークン等が狙われ、数百社が影響とされる一方、Salesforceは支払い拒否を明言し脅迫は継続中。 リークサイトは現在停止し押収の可能性が示唆、10月10日以降はSalesloft関連被害企業への公開恐喝開始を予告。 | 中 | `source--daily-5ba304eec88672244aca` |
| ハッカーがResecurityの侵害を主張、同社は「ハニーポットだった」と反論 | intrusion | 2025-11-21 | 2025-11-21 | 2026-01-05 | target--mitre-group--sector--54b3bca0635944bdc12d |  |  | victim--activity-rule--6fbad8cb25e05525dae6 | SLH（Scattered Lapsus$ Hunters）を名乗る攻撃者が、Resecurity侵害と社内データ窃取をTelegramで主張した。 証拠として、Mattermost上の会話やPastebin担当者との連絡に見えるスクリーンショットを公開したとされる。 攻撃者は、Resecurityが流出DBと称した売買で買い手を装うソーシャルエンジニアリングを仕掛けたことへの「報復」だと説明している。 Resecurityは、本番ではなく監視用に用意した偽データ入り環境（ハニーポット）へ誘導して観測していたと反論した。 2025年11月21日に探索を検知し、12月12〜24日に18.8万回超のリクエストを観測、得た情報は法執行機関へ共有したという。 | 中 | `source--daily-b582c9da4145059382ff` |
| Scattered Lapsus$ HuntersがZendeskユーザー標的化に関与か | phishing-campaign | 不明 | 不明 | 2025-12-02 |  |  |  | victim--activity-rule--917fc1ac5ec636ef8eee | ReliaQuestは過去6か月で出現したZendesk偽装ドメイン40超を発見し、偽SSOで資格情報を窃取すると報告。 例としてznedesk[.]comやvpn-zendesk[.]comが挙げられ、正規に酷似のフィッシングページへ誘導する。 研究者は本件を西側の若年層中心集団SLSHに帰属し、ヘルプデスク偽装やMFA回避に長けると分析。 関連のSalesforce事案では盗難トークン悪用で760社＋約300社のデータ窃取が示され、手口の連続性が指摘。 近月もCRM/サポート系を狙う攻撃が継続すると警戒を促し、波及に注意が必要と結論。 | 高 | `source--daily-4f7f6beeec2ea0a99a71` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 英国 | 活動「英国政府、サイバー攻撃後のJLRに15億ポンドのローン保証を実施」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-04302db7cea311067bd3` |
| sectors | 情報通信 | The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.(Citation: BBC LAPSUS Apr 2022)(Citation: MSTIC DEV-0537 Mar 2022)(Citation: UNIT 42 LAPSUS Mar 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 教育・研究 | The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.(Citation: BBC LAPSUS Apr 2022)(Citation: MSTIC DEV-0537 Mar 2022)(Citation: UNIT 42 LAPSUS Mar 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | エネルギー | The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.(Citation: BBC LAPSUS Apr 2022)(Citation: MSTIC DEV-0537 Mar 2022)(Citation: UNIT 42 LAPSUS Mar 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 製造・産業 | The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.(Citation: BBC LAPSUS Apr 2022)(Citation: MSTIC DEV-0537 Mar 2022)(Citation: UNIT 42 LAPSUS Mar 2022) | 2025-11-21 | 2025-11-21 | 高 | `source--daily-04302db7cea311067bd3`, `source--daily-b582c9da4145059382ff`, `source--mitre-attack-19-1` |
| sectors | 政府・行政 | The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.(Citation: BBC LAPSUS Apr 2022)(Citation: MSTIC DEV-0537 Mar 2022)(Citation: UNIT 42 LAPSUS Mar 2022) | 不明 | 不明 | 高 | `source--daily-04302db7cea311067bd3`, `source--mitre-attack-19-1` |
| sectors | 医療・ヘルスケア | The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.(Citation: BBC LAPSUS Apr 2022)(Citation: MSTIC DEV-0537 Mar 2022)(Citation: UNIT 42 LAPSUS Mar 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | メディア・報道 | The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.(Citation: BBC LAPSUS Apr 2022)(Citation: MSTIC DEV-0537 Mar 2022)(Citation: UNIT 42 LAPSUS Mar 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Salesforce、広範なデータ窃取攻撃に対する身代金支払いを拒否 | 非公開 | aggregate | multiple-organizations | reported |  |  |  | クラウド／SaaS | data-theft: Salesforce、広範なデータ窃取攻撃に対する身代金支払いを拒否<br>credential-theft: 攻撃は二段階で、①ITサポート偽装で悪性OAuthアプリ連携→DB窃取、②8月にSalesloft/DriftのOAuthトークン悪用→CRMから流出。 | 不明 | 不明 | 2025-10-09 | 中 | `source--daily-5ba304eec88672244aca` |
| 被害事例: 英国、主要小売業へのサイバー攻撃を受けてセキュリティ対策を共有 | 非公開 | aggregate | multiple-organizations | reported |  |  |  |  |  | 不明 | 不明 | 2025-05-06 | 中 | `source--daily-4cd1fe293925310c02b7` |
| 被害事例: ハッカーがResecurityの侵害を主張、同社は「ハニーポットだった」と反論 | 非公開 | anonymous | unknown | reported | target--mitre-group--sector--54b3bca0635944bdc12d |  |  |  | data-theft: SLH（Scattered Lapsus$ Hunters）を名乗る攻撃者が、Resecurity侵害と社内データ窃取をTelegramで主張した。 | 2025-11-21 | 2025-11-21 | 2026-01-05 | 中 | `source--daily-b582c9da4145059382ff` |
| 被害事例: Scattered Lapsus$ HuntersがZendeskユーザー標的化に関与か | 非公開 | aggregate | multiple-organizations | reported |  |  |  | クラウド／SaaS | data-theft: 関連のSalesforce事案では盗難トークン悪用で760社＋約300社のデータ窃取が示され、手口の連続性が指摘。<br>credential-theft: 関連のSalesforce事案では盗難トークン悪用で760社＋約300社のデータ窃取が示され、手口の連続性が指摘。 | 不明 | 不明 | 2025-12-02 | 高 | `source--daily-4f7f6beeec2ea0a99a71` |
| 被害事例: ハッカーがサポートチケットを盗み、Discordがデータ侵害を公表 | ハッカーがサポートチケットを盗み | named | organization | reported |  |  |  | メール／メールアカウント | data-theft: Discordはサードパーティのサポート業者が侵害され、サポート由来の利用者データ流出を10月4日に公表。 | 不明 | 不明 | 2025-10-06 | 中 | `source--daily-9af96d00623df591e4cf` |
| 被害事例: 英国政府、サイバー攻撃後のJLRに15億ポンドのローン保証を実施 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--f9601e2d842c9a05202b, target--mitre-group--sector--54b3bca0635944bdc12d, target--mitre-group--sector--55400c7679dae0d87f49 |  |  |  | data-theft: 攻撃は今月公表され、ITと製造に深刻な障害を引き起こし、複数工場の停止とデータ窃取をJLRが確認。 | 不明 | 不明 | 2025-09-30 | 中 | `source--daily-04302db7cea311067bd3` |
| 被害事例: ジャガー・ランドローバー、最近のサイバー攻撃でデータ窃取を確認 | 非公開 | anonymous | unknown | alleged |  |  |  |  | data-theft: ジャガー・ランドローバー、最近のサイバー攻撃でデータ窃取を確認 JLRは最近の攻撃で「一部のデータ」流出を確認し、規制当局へ通知。 | 不明 | 不明 | 2025-09-11 | 中 | `source--daily-fb784abeaacd66b357b3` |
| 被害事例: ジャガー・ランドローバー、サイバー攻撃で操業停止をさらに1週間延長 | 非公開 | anonymous | unknown | alleged |  |  |  |  | data-theft: 同社は9月2日に大規模障害を公表し、先週は「一部データの窃取」を認め、従業員へ出勤停止を指示。 | 不明 | 不明 | 2025-09-17 | 中 | `source--daily-96306c5877ca4244921e` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.003 | NTDS | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used Windows built-in tool `ntdsutil` to extract the Active Directory (AD) database.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.006 | DCSync | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used DCSync attacks to gather credentials for privilege escalation routines.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [LAPSUS$](https://attack.mitre.org/groups/G1004) uploaded sensitive files, information, and credentials from a targeted organization for extortion or public release.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [LAPSUS$](https://attack.mitre.org/groups/G1004) has exploited unpatched vulnerabilities on internally accessible servers including JIRA, GitLab, and Confluence for privilege escalation.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.002 | Domain Groups | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used the AD Explorer tool to enumerate groups on a victim's network.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used compromised credentials and/or session tokens to gain access into a victim's VPN, VDI, RDP, and IAMs.(Citation: MSTIC DEV-0537 Mar 2022)(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.004 | Cloud Accounts | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used compromised credentials to access cloud assets within a target organization.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used the AD Explorer tool to enumerate users on a victim's network.(Citation: MSTIC DEV-0537 Mar 2022)(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | [LAPSUS$](https://attack.mitre.org/groups/G1004) has leverage NordVPN for its egress points when targeting intended victims.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.003 | Additional Cloud Roles | [LAPSUS$](https://attack.mitre.org/groups/G1004) has added the global admin role to accounts they have created in the targeted organization's cloud instances.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1111 | Multi-Factor Authentication Interception | [LAPSUS$](https://attack.mitre.org/groups/G1004) has replayed stolen session token and passwords to trigger simple-approval MFA prompts in hope of the legitimate user will grant necessary approval.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.003 | Email Forwarding Rule | [LAPSUS$](https://attack.mitre.org/groups/G1004) has set an Office 365 tenant level mail transport rule to send all mail in and out of the targeted organization to the newly created account.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gained access to internet-facing systems and applications, including virtual private network (VPN), remote desktop protocol (RDP), and virtual desktop infrastructure (VDI) including Citrix. (Citation: MSTIC DEV-0537 Mar 2022)(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.003 | Cloud Account | [LAPSUS$](https://attack.mitre.org/groups/G1004) has created global admin accounts in the targeted organization's cloud instances to gain persistence.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | [LAPSUS$](https://attack.mitre.org/groups/G1004) has accessed internet-facing identity providers such as Azure Active Directory and Okta to target specific organizations.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204 | User Execution | [LAPSUS$](https://attack.mitre.org/groups/G1004) has recruited target organization employees or contractors who provide credentials and approve an associated MFA prompt, or install remote management software onto a corporate workstation, allowing [LAPSUS$](https://attack.mitre.org/groups/G1004) to take control of an authenticated system.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.001 | Confluence | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched a victim's network for collaboration platforms like Confluence and JIRA to discover further high-privilege account credentials.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.002 | Sharepoint | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched a victim's network for collaboration platforms like SharePoint to discover further high-privilege account credentials.(Citation: MSTIC DEV-0537 Mar 2022)(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.003 | Code Repositories | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched a victim's network for code repositories like GitLab and GitHub to discover further high-privilege account credentials.(Citation: MSTIC DEV-0537 Mar 2022)(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.005 | Messaging Applications | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched a victim's network for organization collaboration channels like MS Teams or Slack to discover further high-privilege account credentials.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1485 | Data Destruction | [LAPSUS$](https://attack.mitre.org/groups/G1004) has deleted the target's systems and resources both on-premises and in the cloud.(Citation: MSTIC DEV-0537 Mar 2022)(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1489 | Service Stop | [LAPSUS$](https://attack.mitre.org/groups/G1004) has shut down virtual machines from within a victim's on-premise VMware ESXi infrastructure.(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1531 | Account Access Removal | [LAPSUS$](https://attack.mitre.org/groups/G1004) has removed a targeted organization's global admin accounts to lock the organization out of all access.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.008 | Chat Messages | [LAPSUS$](https://attack.mitre.org/groups/G1004) has targeted various collaboration tools like Slack, Teams, JIRA, Confluence, and others to hunt for exposed credentials to support privilege escalation and lateral movement.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [LAPSUS$](https://attack.mitre.org/groups/G1004) has obtained passwords and session tokens with the use of the Redline password stealer.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.005 | Password Managers | [LAPSUS$](https://attack.mitre.org/groups/G1004) has accessed local password managers and databases to obtain further credentials from a compromised network.(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1578.002 | Create Cloud Instance | [LAPSUS$](https://attack.mitre.org/groups/G1004) has created new virtual machines within the target's cloud environment after leveraging credential access to cloud assets.(Citation: MSTIC DEV-0537 Mar 2022)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1578.003 | Delete Cloud Instance | [LAPSUS$](https://attack.mitre.org/groups/G1004) has deleted the target's systems and resources in the cloud to trigger the organization's incident and crisis response process.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [LAPSUS$](https://attack.mitre.org/groups/G1004) has used VPS hosting providers for infrastructure.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.002 | DNS Server | [LAPSUS$](https://attack.mitre.org/groups/G1004) has reconfigured a victim's DNS records to actor-controlled domains and websites.(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | [LAPSUS$](https://attack.mitre.org/groups/G1004) has payed employees, suppliers, and business partners of target organizations for credentials.(Citation: MSTIC DEV-0537 Mar 2022)(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | [LAPSUS$](https://attack.mitre.org/groups/G1004) acquired and used the Redline password stealer in their operations.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [LAPSUS$](https://attack.mitre.org/groups/G1004) has obtained tools such as RVTools and AD Explorer for their operations.(Citation: MSTIC DEV-0537 Mar 2022)(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered detailed information of target employees to enhance their social engineering lures.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.001 | Credentials | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered user identities and credentials to gain initial access to a victim's organization; the group has also called an organization's help desk to reset a target's credentials.(Citation: MSTIC DEV-0537 Mar 2022)(Citation: NCC Group LAPSUS Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered employee email addresses, including personal accounts, for social engineering and initial access efforts.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591.002 | Business Relationships | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered detailed knowledge of an organization's supply chain relationships.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591.004 | Identify Roles | [LAPSUS$](https://attack.mitre.org/groups/G1004) has gathered detailed knowledge of team structures within a target organization.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1593.003 | Code Repositories | [LAPSUS$](https://attack.mitre.org/groups/G1004) has searched public code repositories for exposed credentials.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1597.002 | Purchase Technical Data | [LAPSUS$](https://attack.mitre.org/groups/G1004) has purchased credentials and session tokens from criminal underground forums.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.004 | Spearphishing Voice | [LAPSUS$](https://attack.mitre.org/groups/G1004) has called victims' help desk to convince the support personnel to reset a privileged account’s credentials.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1621 | Multi-Factor Authentication Request Generation | [LAPSUS$](https://attack.mitre.org/groups/G1004) has spammed target users with MFA prompts in the hope that the legitimate user will grant necessary approval.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | [LAPSUS$](https://attack.mitre.org/groups/G1004) has called victims' help desk and impersonated legitimate users with previously gathered information in order to gain access to privileged accounts.(Citation: MSTIC DEV-0537 Mar 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 72件（`artifacts.csv`）

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
| source--daily-04302db7cea311067bd3 | 英国政府、サイバー攻撃後のJLRに15億ポンドのローン保証を実施 | bleepingcomputer.com | 2025-09-30 | https://www.bleepingcomputer.com/news/security/uk-govt-backs-jlr-with-15-billion-loan-guarantee-after-cyberattack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4cd1fe293925310c02b7 | 英国、主要小売業へのサイバー攻撃を受けてセキュリティ対策を共有 | bleepingcomputer.com | 2025-05-06 | https://www.bleepingcomputer.com/news/security/uk-shares-security-tips-after-major-retail-cyberattacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4f7f6beeec2ea0a99a71 | Scattered Lapsus$ HuntersがZendeskユーザー標的化に関与か | databreachtoday.com | 2025-12-02 | https://www.databreachtoday.com/scattered-lapsus-hunters-tied-to-targeting-zendesk-users-a-30166 | osint-report | TLP:CLEAR | 中 |
| source--daily-5ba304eec88672244aca | Salesforce、広範なデータ窃取攻撃に対する身代金支払いを拒否 | bleepingcomputer.com | 2025-10-09 | https://www.bleepingcomputer.com/news/security/salesforce-refuses-to-pay-ransom-over-widespread-data-theft-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-96306c5877ca4244921e | ジャガー・ランドローバー、サイバー攻撃で操業停止をさらに1週間延長 | bleepingcomputer.com | 2025-09-17 | https://www.bleepingcomputer.com/news/security/jaguar-land-rover-extends-shutdown-after-cyberattack-by-another-week/ | osint-report | TLP:CLEAR | 中 |
| source--daily-9af96d00623df591e4cf | ハッカーがサポートチケットを盗み、Discordがデータ侵害を公表 | bleepingcomputer.com | 2025-10-06 | https://www.bleepingcomputer.com/news/security/discord-discloses-data-breach-after-hackers-steal-support-tickets/ | osint-report | TLP:CLEAR | 中 |
| source--daily-b582c9da4145059382ff | ハッカーがResecurityの侵害を主張、同社は「ハニーポットだった」と反論 | bleepingcomputer.com | 2026-01-05 | https://www.bleepingcomputer.com/news/security/hackers-claim-resecurity-hack-firm-says-it-was-a-honeypot/ | osint-report | TLP:CLEAR | 中 |
| source--daily-fb784abeaacd66b357b3 | ジャガー・ランドローバー、最近のサイバー攻撃でデータ窃取を確認 | bleepingcomputer.com | 2025-09-11 | https://www.bleepingcomputer.com/news/security/jaguar-land-rover-jlr-confirms-data-theft-after-recent-cyberattack/ | osint-report | TLP:CLEAR | 中 |
| source--lapsus--068222d971e2c65e | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--09ea6072528d92c1 | positive research 2023 eng |  | 2023 | summary/2023/positive-research-2023-eng.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--0a2fa8bd4a966156 | GRIT Ransomware Annual Report 2023 |  | 2023 | summary/2024/GRIT_Ransomware_Annual_Report_2023.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--0d0994b317b0bea6 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--lapsus--1135814e8556f75d | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--180da395433c5bf8 | KELA Telegram CEBIN |  | 不明 | cybercrime/KELA_Telegram_CEBIN.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--1a228d9b694b7069 | 2022 unit42 incident response report final |  | 2022 | summary/2022/2022-unit42-incident-response-report-final.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--32b5950c30f1cf13 | Flashpoint 2026 Global Threat Intelligence Report |  | 2026 | summary/2026/Flashpoint_2026_Global_Threat_Intelligence_Report.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--3ebf284d4a96dc59 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--3f66ee42b1f41ff9 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--54549f3625618ae2 | eset threat report h22025 |  | 不明 | summary/2025/eset-threat-report-h22025.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--595579969b605ff6 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--lapsus--807954360924339d | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--81646e8a4d8e8205 | Dragos 2026 OT Cybersecurity Report A Year in Review |  | 2026 | OT/Dragos-2026-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--8c498f41357ca82b | CyberProof 2026 Global Threat Intelligence Report |  | 2026 | summary/2026/CyberProof_2026_Global_Threat_Intelligence_Report.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--8ee834f5bdb362bb | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--9fe3d99101c34c6b | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--bf186e1922acf805 | 2022 APT Activity Analysis Report threatbook |  | 2022 | summary/2023/2022 APT Activity Analysis Report threatbook.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--c072d7baf55688e2 | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--d1e9ca670a380f3f | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--d4c0fdb6d23a2bf1 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--dfe27bb0366a43f9 | lapsus |  | 不明 | actor_profile/evidence/lapsus.csv | structured-data | TLP:CLEAR | 中 |
| source--lapsus--e0ea84159fad8d18 | ShinyHunters |  | 不明 | cybercrime/ShinyHunters/ShinyHunters.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--e91204ee5feb4994 | 005 |  | 不明 | summary/UNREDACTEDMagazine/005.pdf | report | TLP:CLEAR | 中 |
| source--lapsus--f27729bc4399695a | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
