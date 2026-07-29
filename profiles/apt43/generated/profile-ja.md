# APT43 脅威アクタープロファイル

- プロファイルID: `actor--apt43`
- 状態: review
- 更新日時: 2026-07-27T11:17:22Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

APT43の標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT43**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Kimsuky | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Kimsuki | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 6; mapping requires review. |
| Velvet Chollima | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 6; mapping requires review. |
| Thallium | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 6; mapping requires review. |
| CloudDragon | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 6; mapping requires review. |
| TA406 (Proofpoint) | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 6; mapping requires review. |
| G0094 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 6; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the North Korea worksheet.

- 国: North Korea
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
| Kimsuky | overlaps-with | 共有alias: Kimsuky | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Kimsuky | overlaps-with | MITRE treats APT43 as an associated Kimsuky group name, while Mandiant defines APT43 using its own collection scope. The overlap is well supported, but exact one-to-one identity is not. | 高 | `source--mitre-live-kimsuky-2026`, `source--mandiant-apt43-2023` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | KPortScan, PsExec, Procdump, Mimikatz, Eternal suite of exploits, NirSoft MailPassView/Network Password Recovery/Remote Desktop PassView/SniffPass/WebBrowserPassView, Mechanical, Grease, KGH_SPY |
| Infrastructure |  |
| Victim | This threat actor targets South Korean think tanks, industry, nuclear power operators, and the Ministry of Unification for espionage purposes. |
| Socio-political | North Korea |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Kimsuky, Velvet Chollima | canonical-name | 高 | North Korea | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://securityintelligence.com/media/recent-activity-from-itg16-a-north-korean-threat-group/<br>https://us-cert.cisa.gov/ncas/alerts/aa20-301a |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Emerald Sleet | multiple-name-intersection | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Opal Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Ruby Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Kimsuky | canonical-name | 高 | KP, Korea (Democratic People's Republic of) | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://www.cfr.org/interactive/cyber-operations/kimsuky<br>https://www.pwc.co.uk/issues/cyber-security-data-privacy/research/tracking-kimsuky-north-korea-based-cyber-espionage-group-part-2.html |
| misp-threat-actor | APT43 | canonical-name | 高 |  | https://www.mandiant.com/resources/blog/apt43-north-korea-cybercrime-espionage<br>https://mandiant.widen.net/s/zvmfw5fnjs/apt43-report |
| misp-microsoft-activity-group | Emerald Sleet | multiple-name-intersection | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Opal Sleet | canonical-name | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Ruby Sleet | single-alias-intersection | 中 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Kimsuky - G0094 | canonical-name | 高 |  | https://asert.arbornetworks.com/stolen-pencil-campaign-targets-academia/<br>https://attack.mitre.org/groups/G0094<br>https://blog.alyac.co.kr/2234 |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Opal Sleet | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Ruby Sleet | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--eternal-suite-of-exploits | Eternal suite of exploits | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--grease | Grease | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--kgh-spy | KGH_SPY | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--kportscan | KPortScan | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--mechanical | Mechanical | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--mimikatz | Mimikatz | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--nirsoft-mailpassview-network-password-recovery-remote-desktop-passview-sniffpass-webbrowserpassview | NirSoft MailPassView/Network Password Recovery/Remote Desktop PassView/SniffPass/WebBrowserPassView | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--procdump | Procdump | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--psexec | PsExec | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| capability--apt43-public-llm-access | Access to Public LLM Tools | GTIG detected APT43 actors accessing multiple publicly available LLM tools. The source did not establish what APT43 intended to do with them. | 不明 | 2025-01-29 | 高 | `source--gtig-apt43-llm-access-2025` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| FBI、KimsukyがQRコードを使って米国組織をフィッシングしていると警告 | phishing-campaign | 不明 | 不明 | 2026-01-10 | FBIは北朝鮮系APT「Kimsuky（APT43）」が、悪性QRコード付きスピアフィッシング（Quishing）を米国組織へ行っていると警告。 対象は北朝鮮関連の政策・研究に関わるNGO、シンクタンク、学術機関、戦略アドバイザリ、政府組織などとされる。 QRをスマホで読ませてメール防御を迂回し、偽ログイン等へ誘導して資格情報やセッショントークン窃取→MFA回避に繋げる手口。 2025年5〜6月に、アンケート／セキュアドライブ／会議登録を装い、攻撃者管理インフラ経由で偽Microsoft 365等へ誘導した事例を提示。 対策として、QRコード教育、送信元検証、MDM導入、フィッシング耐性MFAの徹底、スキャン後の監視・通報を推奨。 | 中 | `source--daily-4c3098e731ae81f16008` |
| 北朝鮮のハッカー、弱いDMARCメールポリシーを悪用 | phishing-campaign | 不明 | 不明 | 2024-05-04 | NSAとFBIは、北朝鮮APT43が弱いDMARCポリシーが設定されているドメインを悪用していると警告。 弱いDMARCポリシーが設定されているドメインから偽のメールを送信することで、攻撃者は偽のメールを信頼できるソースから送信されたように見せかける。 情報収集を目的としたスピアフィッシングキャンペーンが実施されている。 攻撃は日本、韓国、米国、その他の国々のシンクタンクや研究センター、報道機関を標的としている。 「v=DMARC1; p=reject;」または「v=DMARC1; p=quarantine;」などのDMARCポリシーで、なりすましメールの送信に悪用されるのを防止することが推奨されている。 | 中 | `source--daily-251ff3261ef519dfe8d5` |
| 北朝鮮系ハッカーが「ClickFix」を悪用し、暗号資産の偽求人でBeaverTailを配布 | campaign | 不明 | 不明 | 2025-09-22 | 北朝鮮関係者がClickFix誘導を用い、BeaverTailとInvisibleFerretを偽求人経由で配布する手口が確認された。 従来の開発者狙いから、暗号資産・小売のマーケ/トレーダー職志望者へ標的を拡大し、Vercel製偽採用サイトを配布基盤に利用。 OS別コマンド実行を促す偽マイク障害表示で、シェル/VBスクリプト経由の軽量版BeaverTailを展開するのが特徴。 2025年5月後半の波では、pkgやPyInstallerで作成したWindows/macOS/Linux向けバイナリ化版の投入が観測された。 この攻撃キャンペーンに時期を合わせ、北朝鮮と連携するKimsuky (別名 APT43)による2つの攻撃キャンペーンも観測されている。 | 中 | `source--daily-dddef70e68c0dc59a5d3` |
| 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | malware-campaign | 不明 | 不明 | 2024-08-06 | 北朝鮮のハッカーグループがVPNのアップデートの脆弱性を悪用し、マルウェアをインストール。 攻撃者はKimsukyとAndariel（APT43とAPT45）で、韓国の産業機密を狙う。 VPNソフトウェアの通信プロトコルの脆弱性を悪用し、更新プログラムを置き換えてトロイの木馬化。遠隔操作用のDoraRATをインストール。 攻撃は産業機器や設計文書の盗難を目的としている。 NCSCが警告を発表し、セキュリティ対策を推奨。 | 中 | `source--daily-444c87a0051642065f55` |

2025年1月、GTIGはAPT43関係者が複数の公開LLMツールへアクセスしていた証拠を報告した。ただし目的は不明であり、特定の攻撃工程での利用を示す情報ではない。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1007 | System Service Discovery | b Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Dir |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1010 | Application Window Discovery | munication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Dis |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1012 | Query Registry | sfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T161 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1016 | System Network Configuration Discovery | Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language D |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Exfiltration | T1020 | Automated Exfiltration | BA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 Brute Force T1555.003 Credentials from Web Browsers |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1027 | Obfuscated Files or Information | 43.003 Windows Service T15 47.001: Registry Run Keys / Startup Folder T15 47.004 Winlogon Helper DLL T15 47.009 Shortcut Modification Defense Evasion T1027 Obfuscated Files or Information T1027.001 Binary Padding T1027.002 Software Packing T1027.005 Indicator Removal from Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Inj |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1027.001 | Binary Padding | egistry Run Keys / Startup Folder T15 47.004 Winlogon Helper DLL T15 47.009 Shortcut Modification Defense Evasion T1027 Obfuscated Files or Information T1027.001 Binary Padding T1027.002 Software Packing T1027.005 Indicator Removal from Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Inje |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1027.002 | Software Packing | Folder T15 47.004 Winlogon Helper DLL T15 47.009 Shortcut Modification Defense Evasion T1027 Obfuscated Files or Information T1027.001 Binary Padding T1027.002 Software Packing T1027.005 Indicator Removal from Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Ex |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1027.005 | Indicator Removal from Tools | elper DLL T15 47.009 Shortcut Modification Defense Evasion T1027 Obfuscated Files or Information T1027.001 Binary Padding T1027.002 Software Packing T1027.005 Indicator Removal from Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1027.009 | Embedded Payloads | ation Defense Evasion T1027 Obfuscated Files or Information T1027.001 Binary Padding T1027.002 Software Packing T1027.005 Indicator Removal from Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T11 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1033 | System Owner/User Discovery | covery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1036 | Masquerading | Obfuscated Files or Information T1027.001 Binary Padding T1027.002 Software Packing T1027.005 Indicator Removal from Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1036.001 | Invalid Code Signature | rmation T1027.001 Binary Padding T1027.002 Software Packing T1027.005 Indicator Removal from Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manip |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1036.007 | Double File Extension | T1027.002 Software Packing T1027.005 Indicator Removal from Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Dec |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1047 | Windows Management Instrumentation | astructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 Windows Management Instrumentation T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitatio |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 Windows Management Instrumentation T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Privilege Escalation, Stealth | T1055 | Process Injection | 7.005 Indicator Removal from Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T121 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | Tools T1027.009 Embedded Payloads T1036 Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtuali |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Privilege Escalation, Stealth | T1055.003 | Thread Execution Hijacking | Masquerading T1036.001 Invalid Code Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System C |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Collection, Credential Access | T1056.001 | Keylogging | on Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Archive Collected Data T1560.001 Archive via Utility T echnical Annex: MITRE ATT&CK |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1057 | Process Discovery | very T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1059 | Command and Scripting Interpreter | icates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 Windows Management Instrumentation T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1059.003 | Windows Command Shell | t Execution T1047 Windows Management Instrumentation T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocol |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1059.005 | Visual Basic | nagement Instrumentation T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Mul |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1059.007 | JavaScript | T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1070.004 | File Deletion | de Signature T1036.007 Double File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1070.006 | Timestomp | uble File Extension T1055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Si |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Command And Control | T1071.001 | Web Protocols | Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discove |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Command And Control | T1071.004 | DNS | itation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Serv |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1082 | System Information Discovery | Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from I |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1083 | File and Directory Discovery | y T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Arch |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1087 | Account Discovery | Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Archive Collected Data T1560.001 Archive v |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Command And Control | T1090.003 | Multi-hop Proxy | t Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T10 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Command And Control | T1095 | Non-Application Layer Protocol | cious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Wind |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Command And Control | T1102 | Web Service | 2 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Command And Control | T1102.002 | Bidirectional Communication | mmand and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configurati |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Command And Control | T1105 | Ingress Tool Transfer | ocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Ow |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Credential Access | T1110 | Brute Force | Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 Brute Force T1555.003 Credentials from Web Browsers |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Defense Impairment, Persistence | T1112 | Modify Registry | 055 Process Injection T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Collection | T1113 | Screen Capture | File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Archive Collected Data T1560.001 Archive via Utility T echnical Annex: MITRE ATT&CK |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Collection | T1115 | Clipboard Data | ery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Archive Collected Data T1560.001 Archive via Utility T echnical Annex: MITRE ATT&CK |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1129 | Shared Modules | ask T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Laye |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Command And Control | T1132.001 | Standard Encoding | Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process D |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Privilege Escalation, Stealth | T1134 | Access Token Manipulation | T1055.001 Dynamic-link Library Injection T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Persistence | T1137 | Office Application Startup | 14 MANDIANT APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations Persistence T1137 Office Application Startup T1505.00 Web Shell T1543.003 Windows Service T15 47.001: Registry Run Keys / Startup Folder T15 47.004 Winlogon Helper DLL T15 47.009 Shortcut Modification Defense Evasion T1027 Obfuscated Files or Information T1027.001 Binary P |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | ction T1055.003 Thread Execution Hijacking T1070.004 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective C |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1203 | Exploitation for Client Execution | Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1204.001 | Malicious Link | T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T110 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1204.002 | Malicious File | Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transf |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Collection | T1213 | Data from Information Repositories | overy T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Archive Collected Data T1560.001 Archive via Utility T echnical Annex: MITRE ATT&CK |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1218.005 | Mshta | 4 File Deletion T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Impact | T1489 | Service Stop | Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 Brute Force T1555.003 Credentials from Web Browsers |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | T1070.006 Timestomp T1112 Modify Registry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service St |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery, Stealth | T1497.001 | System Checks | egistry T1134 Access Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltra |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Persistence | T1505 | Server Software Component | 14 MANDIANT APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations Persistence T1137 Office Application Startup T1505.00 Web Shell T1543.003 Windows Service T15 47.001: Registry Run Keys / Startup Folder T15 47.004 Winlogon Helper DLL T15 47.009 Shortcut Modification Defense Evasion T1027 Obfuscated Files or Information T1027.001 Binary Padding T1027.002 Software Packing T1 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1518 | Software Discovery | m Owner/User Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Archive Collected Data T1560.001 Archive via Utility T echnical Annex: |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Impact | T1529 | System Shutdown/Reboot | Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 Brute Force T1555.003 Credentials from Web Browsers |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | 14 MANDIANT APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations Persistence T1137 Office Application Startup T1505.00 Web Shell T1543.003 Windows Service T15 47.001: Registry Run Keys / Startup Folder T15 47.004 Winlogon Helper DLL T15 47.009 Shortcut Modification Defense Evasion T1027 Obfuscated Files or Information T1027.001 Binary Padding T1027.002 Software Packing T1027.005 Indicator Removal |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | Token Manipulation T1140 Deobfuscate/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Defense Impairment | T1553.002 | Code Signing | e/Decode Files or Information T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Credential Access | T1555.003 | Credentials from Web Browsers | pact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 Brute Force T1555.003 Credentials from Web Browsers |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Collection | T1560 | Archive Collected Data | System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Archive Collected Data T1560.001 Archive via Utility T echnical Annex: MITRE ATT&CK |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Collection | T1560.001 | Archive via Utility | on T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Archive Collected Data T1560.001 Archive via Utility T echnical Annex: MITRE ATT&CK |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1564.003 | Hidden Window | ation T1218.005 Mshta T1497 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 Brute Force T1555.00 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1564.007 | VBA Stomping | 97 Virtualization/Sandbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 Brute Force T1555.003 Credentials from Web Br |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Initial Access | T1566 | Phishing | 13 MANDIANT APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations Initial Access T1566 Phishing T1566.001 Spearphishing Attachment T1566.002 Spearphishing Link Resource Development T1583.003 Virtual Private Server T1584 Compromise Infrastructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digit |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Initial Access | T1566.001 | Spearphishing Attachment | 13 MANDIANT APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations Initial Access T1566 Phishing T1566.001 Spearphishing Attachment T1566.002 Spearphishing Link Resource Development T1583.003 Virtual Private Server T1584 Compromise Infrastructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Initial Access | T1566.002 | Spearphishing Link | 13 MANDIANT APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations Initial Access T1566 Phishing T1566.001 Spearphishing Attachment T1566.002 Spearphishing Link Resource Development T1583.003 Virtual Private Server T1584 Compromise Infrastructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Execution | T1569.002 | Service Execution | l Basic T1059.007 JavaScript T1129 Shared Modules T1203 Exploitation for Client Execution T1204.001 Malicious Link T1204.002 Malicious File T1569.002 Service Execution Command and Control T1071.001 Web Protocols T1071.004 DNS T1090.003 Multi-hop Proxy T1095 Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard E |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Command And Control | T1573.002 | Asymmetric Cryptography | Non-Application Layer Protocol T1102 Web Service T1102.002 Bidirectional Communication T1105 Ingress Tool Transfer T1132.001 Standard Encoding T1573.002 Asymmetric Cryptography Discovery T1007 System Service Discovery T1010 Application Window Discovery T1012 Query Registry T1016 System Network Configuration Discovery T1033 System Owner/User Discovery T1057 Process Discovery T1082 System Inf |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Resource Development | T1583.003 | Virtual Private Server | ime to Fund Espionage Operations Initial Access T1566 Phishing T1566.001 Spearphishing Attachment T1566.002 Spearphishing Link Resource Development T1583.003 Virtual Private Server T1584 Compromise Infrastructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 Windows Management Instrumentation T1053.005 Sche |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Resource Development | T1584 | Compromise Infrastructure | itial Access T1566 Phishing T1566.001 Spearphishing Attachment T1566.002 Spearphishing Link Resource Development T1583.003 Virtual Private Server T1584 Compromise Infrastructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 Windows Management Instrumentation T1053.005 Scheduled Task T1059 Command |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Resource Development | T1588.003 | Code Signing Certificates | 6.001 Spearphishing Attachment T1566.002 Spearphishing Link Resource Development T1583.003 Virtual Private Server T1584 Compromise Infrastructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 Windows Management Instrumentation T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: Pow |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Resource Development | T1588.004 | Digital Certificates | 002 Spearphishing Link Resource Development T1583.003 Virtual Private Server T1584 Compromise Infrastructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 Windows Management Instrumentation T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Sh |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Resource Development | T1608.003 | Install Digital Certificate | Development T1583.003 Virtual Private Server T1584 Compromise Infrastructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 Windows Management Instrumentation T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T105 |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Resource Development | T1608.005 | Link Target | Server T1584 Compromise Infrastructure T1588.003 Code Signing Certificates T1588.004 Digital Certificates T1608.003 Install Digital Certificate T1608.005 Link Target Execution T1047 Windows Management Instrumentation T1053.005 Scheduled Task T1059 Command and Scripting Interpreter T1059.00: PowerShell T1059.003 Windows Command Shell T1059.005 Visual Basic T1059.007 JavaScript T1129 Shared M |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery | T1614.001 | System Language Discovery | Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1087 Account Discovery T1518 Software Discovery T1614.001 System Language Discovery Collection T1056.001 Keylogging T1113 Screen Capture T1115 Clipboard Data T1213 Data from Information Repositories T1560 Archive Collected Data T1560.001 Archive via Utility T echnical Annex: MITRE ATT&CK |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Stealth | T1620 | Reflective Code Loading | ndbox Evasion T1497.001 System Checks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 Brute Force T1555.003 Credentials from Web Browsers |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |
| Discovery, Stealth | T1622 | Debugger Evasion | cks T1548.002: Bypass User Account Control T1553.002 Code Signing T1564.003 Hidden Window T1564.007 VBA Stomping T1620: Reflective Code Loading T1622 Debugger Evasion Impact T1489 Service Stop T1529 System Shutdown/Reboot Exfiltration T1020 Automated Exfiltration Credential Access: T1110 Brute Force T1555.003 Credentials from Web Browsers |  |  | 不明 | 不明 | 中 | `source--apt43--d022e60103e01413` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 17件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| APT43 had access to multiple public LLM services by the reporting period, but available evidence does not support a specific operational-use claim. | 高 | `source--gtig-apt43-llm-access-2025` |  |
| MITRE treats APT43 as an associated Kimsuky group name, while Mandiant defines APT43 using its own collection scope. The overlap is well supported, but exact one-to-one identity is not. | 高 | `source--mitre-live-kimsuky-2026`, `source--mandiant-apt43-2023` | verification_status=partially-supported; Vendor collection boundaries differ; do not replace both profiles with a single exact alias record. The sources support overlap but do not establish that every APT43 observation belongs to the narrower Kimsuky activity set. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- {'statement': "The intended purpose and operational impact of APT43's LLM access remain unknown.", 'confidence': 'high', 'evidence_refs': ['source--gtig-apt43-llm-access-2025'], 'analyst_notes': "Do not generalize the report's broader North Korean use cases to APT43 without actor-specific evidence."}

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--apt43--93a774e52c160a9a | README |  | 不明 | APT43/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--apt43--d022e60103e01413 | APT43 Report |  | 不明 | APT43/APT43 Report.pdf | report | TLP:CLEAR | 中 |
| source--daily-251ff3261ef519dfe8d5 | 北朝鮮のハッカー、弱いDMARCメールポリシーを悪用 | bleepingcomputer.com | 2024-05-04 | https://www.bleepingcomputer.com/news/security/nsa-warns-of-north-korean-hackers-exploiting-weak-dmarc-email-policies/ | osint-report | TLP:CLEAR | 中 |
| source--daily-444c87a0051642065f55 | 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | bleepingcomputer.com | 2024-08-06 | https://www.bleepingcomputer.com/news/security/north-korean-hackers-exploit-vpn-update-flaw-to-install-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4c3098e731ae81f16008 | FBI、KimsukyがQRコードを使って米国組織をフィッシングしていると警告 | bleepingcomputer.com | 2026-01-10 | https://www.bleepingcomputer.com/news/security/fbi-warns-about-kimsuky-hackers-using-qr-codes-to-phish-us-orgs/ | osint-report | TLP:CLEAR | 中 |
| source--daily-dddef70e68c0dc59a5d3 | 北朝鮮系ハッカーが「ClickFix」を悪用し、暗号資産の偽求人でBeaverTailを配布 | thehackernews.com | 2025-09-22 | https://thehackernews.com/2025/09/dprk-hackers-use-clickfix-to-deliver.html | osint-report | TLP:CLEAR | 中 |
| source--gtig-apt43-llm-access-2025 | Adversarial Misuse of Generative AI | Google Threat Intelligence Group | 2025-01-29 | https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai | vendor-research | TLP:CLEAR | 高 |
| source--mandiant-apt43-2023 | APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations | Mandiant | 2023-03-28 | https://cloud.google.com/blog/topics/threat-intelligence/apt43-north-korea-cybercrime-espionage/ | vendor-research | TLP:CLEAR | 高 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-live-kimsuky-2026 | Kimsuky, Group G0094 | MITRE ATT&CK | 2026-04-23 | https://attack.mitre.org/groups/G0094/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
