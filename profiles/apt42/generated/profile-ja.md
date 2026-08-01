# APT42 脅威アクタープロファイル

- プロファイルID: `actor--apt42`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

APT42の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT42**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Charming Kitten | overlaps-with | While there are behavior and software overlaps between [Magic Hound](https://attack.mitre.org/groups/G0059) and [APT42](https://attack.mitre.org/groups/G1044), they appear to be distinct entities and are tracked as separate entities by their originating vendor. | 高 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [APT42](https://attack.mitre.org/groups/G1044) is an Iranian-sponsored threat group that conducts cyber espionage and surveillance.(Citation: Mandiant APT42-charms) The group primarily focuses on targets in the Middle East region, but has targeted a variety of industries and countries since at least 2015.(Citation: Mandiant APT42-charms) [APT42](https://attack.mitre.org/groups/G1044) starts cyber operations through spearphishing emails and/or the PINEFLOWER Android malware, then monitors and collects information from the compromised systems and devices.(Citation: Mandiant APT42-charms) Finally, [APT42](https://attack.mitre.org/groups/G1044) exfiltrates data using native features and open-source tools.(Citation: Mandiant APT42-untangling) <br><br>[APT42](https://attack.mitre.org/groups/G1044) activities have been linked to [Magic Hound](https://attack.mitre.org/groups/G0059) by other commercial vendors. While there are behavior and software overlaps between [Magic Hound](https://attack.mitre.org/groups/G0059) and [APT42](https://attack.mitre.org/groups/G1044), they appear to be distinct entities and are tracked as separate entities by their originating vendor.  |
| Capability | NICECURL, TAMECAT |
| Infrastructure |  |
| Victim | Western think tanks, researchers, journalists, current Western government officials, former Iranian government officials, and the Iranian diaspora abroad |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 42 | canonical-name | 高 | Iran | https://www.mandiant.com/media/17826<br>https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=APT+42&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT42 | canonical-name | 高 | IR, Iran (Islamic Republic of) | https://www.mandiant.com/resources/blog/apt42-charms-cons-compromises<br>https://services.google.com/fh/files/misc/tool-of-first-resort-israel-hamas-war-cyber.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | APT42 - G1044 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1044<br>https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations<br>https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| APT35 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Charming Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--nicecurl | NICECURL | [NICECURL](https://attack.mitre.org/software/S1192) is a VBScript-based backdoor used by [APT42](https://attack.mitre.org/groups/G1044) to download additional modules.(Citation: Mandiant APT42-untangling) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--tamecat | TAMECAT | [TAMECAT](https://attack.mitre.org/software/S1193) is a malware that is used by [APT42](https://attack.mitre.org/groups/G1044) to execute PowerShell or C# content.(Citation: Mandiant APT42-untangling)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | phishing-campaign | 不明 | 不明 | 2026-02-13 | target--activity-rule--country--72caf60a2fbce4a1be7a |  |  | victim--activity-rule--8d9f800c14d1007aa798 | Google Threat Intelligence Group（GTIG）は、国家支援型ハッカーがGeminiを攻撃の全段階で悪用していると述べた。 中国（APT31/Temp.HEX）、イラン（APT42）、北朝鮮（UNC2970）、ロシアの活動が、標的調査やOSINTに使われた。 Geminiはプロファイリング、フィッシング文面生成、翻訳、コーディング、脆弱性テスト、C2開発、データ持ち出しの補助に使われた。 既存マルウェアへの機能追加にも悪用が見られ、CoinBaitやHonestCueでAI生成の痕跡が示された（PoCではGemini APIでC#生成）。 Googleは悪用に紐づくアカウント/インフラを無効化し、Gemini分類器の防御強化と安全対策（ガードレール）を継続的に検証している。 | 中 | `source--daily-2cce580b31452f445118` |
| Google、57以上の国家支援型脅威グループがAIをサイバー作戦に利用していると報告 | phishing-campaign | 不明 | 不明 | 2025-01-31 | target--activity-rule--sector--b94dc560a327b601965d |  |  | victim--activity-rule--d615c41a7c601d64d3ee | Googleの報告によれば、中国、イラン、北朝鮮、ロシアに関連する57以上の脅威アクターが、AI技術をサイバーおよび情報作戦に利用しています。 これらの脅威アクターは、AIを用いて主にリサーチ、コードのトラブルシューティング、コンテンツの作成やローカライズを行っています。 イランのAPTアクターがGeminiの最も頻繁な利用者であり、APT42というハッキンググループは、この国のハッカーによるGemini利用の30%以上を占めています。 各アクターの利用状況 イランのAPT42は、フィッシングキャンペーンの作成、防衛専門家や組織の偵察、サイバーセキュリティ関連のコンテンツ生成にAIを活用しています。 中国のAPTグループは、偵察、コードのトラブルシューティング、ネットワーク内での横移動や権限昇格、データの抽出、検知回避の手法をAIで研究しています。 | 中 | `source--daily-e07d98b8e6a40e245f21` |
| イランのハッカーがジャーナリストになりすまし、バックドアマルウェアを配布 | phishing-campaign | 不明 | 不明 | 2024-05-06 |  |  |  |  | イランのAPT42、ジャーナリストになりすましマルウェアを配布。 メディア組織を偽装し、信頼を築いてから悪意あるリンクを送信。 被害者は文書をクリックすると偽のログインページに誘導される。 認証情報とMFAトークンが盗まれ、企業ネットワークに侵入される。 APT42はクラウドツールのビルトイン機能を利用して行動を隠蔽。 | 中 | `source--daily-0917cfe45c04f45174f4` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | APT42 | 情報なし | 情報なし | 情報なし | ロシア | 被害事例: Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | 中 |
| Google、57以上の国家支援型脅威グループがAIをサイバー作戦に利用していると報告 | APT42 | 情報なし | 情報なし | 情報なし | 防衛・軍事 | 被害事例: Google、57以上の国家支援型脅威グループがAIをサイバー作戦に利用していると報告 | 中 |
| イランのハッカーがジャーナリストになりすまし、バックドアマルウェアを配布 | APT42 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでAPT42の標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | 構造化OSINTの被害国フィールドでAPT42の標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | イタリア | 構造化OSINTの被害国フィールドでAPT42の標的・被害国としてイタリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イラン | レビュー済みアクターマッピングの標的欄に記録されたイランを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ウクライナ | 構造化OSINTの被害国フィールドでAPT42の標的・被害国としてウクライナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでAPT42の標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ノルウェー | 構造化OSINTの被害国フィールドでAPT42の標的・被害国としてノルウェーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブルガリア | 構造化OSINTの被害国フィールドでAPT42の標的・被害国としてブルガリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでAPT42の標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 活動「Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-2cce580b31452f445118` |
| countries | 米国 | 構造化OSINTの被害国フィールドでAPT42の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでAPT42の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | MITRE ATT&CKのGroup概要でAPT42の標的範囲として中東が明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東欧 | ウクライナ、ブルガリア、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-2cce580b31452f445118`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | 構造化OSINTの被害地域フィールドでAPT42の標的範囲として欧州が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 防衛・軍事 | 活動「Google、57以上の国家支援型脅威グループがAIをサイバー作戦に利用していると報告」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-e07d98b8e6a40e245f21` |
| sectors | Education and Research | Targeting text indicates the Education and Research sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Media | Targeting text indicates the Media sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--72caf60a2fbce4a1be7a |  |  |  | data-theft: Geminiはプロファイリング、フィッシング文面生成、翻訳、コーディング、脆弱性テスト、C2開発、データ持ち出しの補助に使われた。 | 不明 | 不明 | 2026-02-13 | 中 | `source--daily-2cce580b31452f445118` |
| 被害事例: Google、57以上の国家支援型脅威グループがAIをサイバー作戦に利用していると報告 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--b94dc560a327b601965d |  |  |  |  | 不明 | 不明 | 2025-01-31 | 中 | `source--daily-e07d98b8e6a40e245f21` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1016 | System Network Configuration Discovery | [APT42](https://attack.mitre.org/groups/G1044) has used malware, such as GHAMBAR and POWERPOST, to collect network information.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [APT42](https://attack.mitre.org/groups/G1044) has masqueraded the VINETHORN payload as a VPN application.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [APT42](https://attack.mitre.org/groups/G1044) has used Windows Management Instrumentation (WMI) to query anti-virus products.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [APT42](https://attack.mitre.org/groups/G1044) has used scheduled tasks for persistence.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056 | Input Capture | [APT42](https://attack.mitre.org/groups/G1044) has used credential harvesting websites.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [APT42](https://attack.mitre.org/groups/G1044) has used custom malware to log keystrokes.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [APT42](https://attack.mitre.org/groups/G1044) has downloaded and executed PowerShell payloads.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [APT42](https://attack.mitre.org/groups/G1044) has used a VBScript to query anti-virus products.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070 | Indicator Removal | [APT42](https://attack.mitre.org/groups/G1044) has cleared Chrome browser history.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.008 | Clear Mailbox Data | [APT42](https://attack.mitre.org/groups/G1044) has deleted login notification emails and has cleared the Sent folder to cover their tracks.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [APT42](https://attack.mitre.org/groups/G1044) has used tools such as [NICECURL](https://attack.mitre.org/software/S1192) with command and control communication taking place over HTTPS.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [APT42](https://attack.mitre.org/groups/G1044) has used malware, such as GHAMBAR and POWERPOST, to collect system information.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | [APT42](https://attack.mitre.org/groups/G1044) has used the PowerShell-based POWERPOST script to collect local account names from the victim machine.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | [APT42](https://attack.mitre.org/groups/G1044) has used various links, such as links with typo-squatted domains, links to Dropbox files and links to fake Google sites, in spearphishing operations.(Citation: Mandiant APT42-untangling)(Citation: Mandiant APT42-charms)(Citation: TAG APT42)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1111 | Multi-Factor Authentication Interception | [APT42](https://attack.mitre.org/groups/G1044) has intercepted SMS-based one-time passwords and has set up two-factor authentication.(Citation: Mandiant APT42-charms) Additionally, [APT42](https://attack.mitre.org/groups/G1044) has used cloned or fake websites to capture MFA tokens.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [APT42](https://attack.mitre.org/groups/G1044) has modified Registry keys to maintain persistence.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [APT42](https://attack.mitre.org/groups/G1044) has used malware, such as GHAMBAR and POWERPOST, to take screenshots.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding |  [APT42](https://attack.mitre.org/groups/G1044) has encoded C2 traffic with Base64.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | summary/2023/2022_APT_TRENDS_INSIGHT_REPORT.pdf {"page": 7} APT42 后门 NA 10 T1190 Windows MSDT 远程代码执行漏洞 CVE-2022-30190 系统漏洞 攻击公开暴露应用并植入后门 NA 11 T1190 Windows 脚本语言远程代码执行漏洞 CVE-2022-41128 系统漏洞 攻击公开暴露应用并植入后门 APT37 12 T1190 Apache log4j2 远程代码执行漏洞 CVE-2021-44228 应用程序漏洞 攻击公开暴露应用并植入后门 Lazarus/APT42 13 T1190 Atlassian Conﬂuence Server 远程代码执行漏洞 CVE-2022-26134 应用程序漏洞 攻 |  |  | 不明 | 不明 | 中 | `source--apt42--ecc18e15a462bb18` |
| Discovery | T1518.001 | Security Software Discovery | [APT42](https://attack.mitre.org/groups/G1044) has used Windows Management Instrumentation (WMI) to check for anti-virus products.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1530 | Data from Cloud Storage | [APT42](https://attack.mitre.org/groups/G1044) has collected data from Microsoft 365 environments.(Citation: Mandiant APT42-untangling)(Citation: Mandiant APT42-charms)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1539 | Steal Web Session Cookie | [APT42](https://attack.mitre.org/groups/G1044) has used custom malware to steal login and cookie data from common browsers.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547 | Boot or Logon Autostart Execution | [APT42](https://attack.mitre.org/groups/G1044) has modified the Registry to maintain persistence.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [APT42](https://attack.mitre.org/groups/G1044) has used custom malware to steal credentials.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [APT42](https://attack.mitre.org/groups/G1044) has sent spearphishing emails containing malicious links.(Citation: Mandiant APT42-charms)(Citation: Mandiant APT42-untangling)(Citation: TAG APT42)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.002 | Asymmetric Cryptography | [APT42](https://attack.mitre.org/groups/G1044) has used tools such as [NICECURL](https://attack.mitre.org/software/S1192) with command and control communication taking place over HTTPS.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [APT42](https://attack.mitre.org/groups/G1044) has registered domains, several of which masqueraded as news outlets and login services, for use in operations.(Citation: Mandiant APT42-charms)(Citation: TAG APT42)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [APT42](https://attack.mitre.org/groups/G1044) has used anonymized infrastructure and Virtual Private Servers (VPSs) to interact with the victim’s environment.(Citation: Mandiant APT42-charms)(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [APT42](https://attack.mitre.org/groups/G1044) has created email accounts to use in spearphishing operations.(Citation: TAG APT42) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [APT42](https://attack.mitre.org/groups/G1044) has used built-in features in the Microsoft 365 environment and publicly available tools to avoid detection.(Citation: Mandiant APT42-untangling)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [APT42](https://attack.mitre.org/groups/G1044) has used its infrastructure for C2 and for staging the VINETHORN payload, which masqueraded as a VPN application.(Citation: Mandiant APT42-charms)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1682 | Query Public AI Services | APT42 has leveraged LLMs to search for official emails to build target lists, and conduct reconnaissance on potential business partners.(Citation: GTIG AI Threat Tracker) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | [APT42](https://attack.mitre.org/groups/G1044) has impersonated legitimate people in phishing emails to gain credentials.(Citation: Mandiant APT42-charms)(Citation: TAG APT42)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 11件
- IOC観測: 13件
- 複数攻撃で観測: 0件
- 要レビュー候補: 5件
- 非IOC artifact観測: 63件（`artifacts.csv`）

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
| source--apt42--2078dca3cd426c7e | 2024 Threat Intelligence Annual Report |  | 2024 | summary/2025/2024 Threat Intelligence Annual Report.pdf | report | TLP:CLEAR | 中 |
| source--apt42--33ba52f45c44e462 | Hurdling Over Hazards  Multifaceted Threats to the Paris Olympics |  | 不明 | summary/2024/Hurdling Over Hazards- Multifaceted Threats to the Paris Olympics.pdf | report | TLP:CLEAR | 中 |
| source--apt42--440a66631095dbd9 | 2024 Malicious Infrastructure Report |  | 2024 | summary/2025/2024 Malicious Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--apt42--4bffb0efe850e284 | tool of first resort israel hamas war cyber |  | 不明 | summary/2024/tool-of-first-resort-israel-hamas-war-cyber.pdf | report | TLP:CLEAR | 中 |
| source--apt42--56e8403dbc9b7d0f | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--apt42--6ea6e14a0e0f30bd | APT42 Crooked Charms Cons and Compromises |  | 不明 | International Strategic/Iran/APT42_Crooked_Charms_Cons_and_Compromises.pdf | report | TLP:CLEAR | 中 |
| source--apt42--814428b19142a33f | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--apt42--8472b6c5ed1c9838 | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--apt42--87fb5f1954a13770 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--apt42--8f20da920924c83f | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--apt42--9b1a00940e03a197 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--apt42--a232571b2948f15f | advances in threat actor usage of ai tools en |  | 不明 | AISecurity/2025/advances-in-threat-actor-usage-of-ai-tools-en.pdf | report | TLP:CLEAR | 中 |
| source--apt42--a4a6e63e2bb65225 | 2023 08 10 cyber brief no 01 2023 |  | 2023-08-10 | Charming Kitten/2023-08-10-cyber-brief-no-01-2023.pdf | report | TLP:CLEAR | 中 |
| source--apt42--a643f50007e75c47 | 2022 APT TRENDS INSIGHT REPORT |  | 2022 | summary/2023/2022_APT_TRENDS_INSIGHT_REPORT.pdf | report | TLP:CLEAR | 中 |
| source--apt42--acbc1743b53b9755 | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--apt42--ad9096318467e19f | README |  | 不明 | Charming Kitten/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--apt42--adb6e441076585e5 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--apt42--c697e07bc1679075 | 2025 Year in Review  Malicious Infrastructure |  | 2025 | summary/2026/2025 Year in Review- Malicious Infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--apt42--cc95678909a4127c | MacMalware 2023 |  | 2023 | summary/2024/MacMalware_2023.pdf | report | TLP:CLEAR | 中 |
| source--apt42--d2db0dd0581a14eb | CERTFR 2025 CTI 004 |  | 2025 | summary/2025/CERTFR-2025-CTI-004.pdf | report | TLP:CLEAR | 中 |
| source--apt42--eaa58a8e923ef829 | national cyber threat assessment 2025 2026 e |  | 不明 | International Strategic/Canada/national-cyber-threat-assessment-2025-2026-e.pdf | report | TLP:CLEAR | 中 |
| source--apt42--ecc18e15a462bb18 | apt42 |  | 不明 | actor_profile/evidence/apt42.csv | structured-data | TLP:CLEAR | 中 |
| source--apt42--fc48efe82bca8147 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--daily-0917cfe45c04f45174f4 | イランのハッカーがジャーナリストになりすまし、バックドアマルウェアを配布 | bleepingcomputer.com | 2024-05-06 | https://www.bleepingcomputer.com/news/security/iranian-hackers-pose-as-journalists-to-push-backdoor-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-2cce580b31452f445118 | Google、ハッカーがGemini AIを攻撃の全段階で悪用していると指摘 | bleepingcomputer.com | 2026-02-13 | https://www.bleepingcomputer.com/news/security/google-says-hackers-are-abusing-gemini-ai-for-all-attacks-stages/ | osint-report | TLP:CLEAR | 中 |
| source--daily-e07d98b8e6a40e245f21 | Google、57以上の国家支援型脅威グループがAIをサイバー作戦に利用していると報告 | thehackernews.com | 2025-01-31 | https://thehackernews.com/2025/01/google-over-57-nation-state-threat.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
