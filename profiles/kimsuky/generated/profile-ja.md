# Kimsuky 脅威アクタープロファイル

プロファイルID: `actor--kimsuky`  
状態: review  
更新日時: 2026-07-25T14:07:08Z  
構造バージョン: 1.0.0

## エグゼクティブサマリー

Kimsukyは北朝鮮RGB傘下と評価される国家支援型サイバー諜報アクターである。政策専門家、政府、外交、軍・防衛、研究、メディアを対象に、調査とペルソナ構築を伴う信頼醸成型スピアフィッシングを行い、認証情報、メール、非公開資料を窃取する。

## アクター名とAlias

- 正規名: **Kimsuky**
- 初回観測: 2012
- 最終観測: 2025
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Emerald Sleet | Microsoft | overlapping | 高 | `source--dmarc-2024`, `source--microsoft-actor-list` | 政府共同勧告は同一活動集合として扱うが、ベンダーの収集スコープ差を考慮する。 |
| Thallium | Microsoft (legacy) | overlapping | 高 | `source--joint-csa-2023`, `source--microsoft-actor-list` |  |
| Velvet Chollima | CrowdStrike | overlapping | 高 | `source--joint-csa-2023` |  |
| Black Banshee | PwC | overlapping | 高 | `source--joint-csa-2023` |  |
| APT43 | Mandiant | broader | 中 | `source--joint-csa-2023`, `source--dmarc-2024` | APT43にはKimsukyより広い活動スコープが含まれる可能性がある。 |
| TA427 | Proofpoint | overlapping | 中 | `source--rapid7-2024` |  |
| Sparkling Pisces | Palo Alto Networks | overlapping | 中 | `source--qax-2024` |  |

## 帰属

北朝鮮の偵察総局（RGB）に従属し、2024年共同勧告は第63研究センターへの行政的従属を記載する。

- 国: North Korea
- スポンサー種別: state
- 確度: 高
- 証拠: `source--joint-csa-2023`, `source--dmarc-2024`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| strategic-espionage | 北朝鮮の政策・外交・軍事・核開発上の意思決定に役立つ情報を収集する。 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |  |
| credential-and-mailbox-access | 認証情報とメールボックスを窃取し、信頼関係と連絡網を次の標的への足掛かりにする。 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |  |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| APT37 | overlaps-with | 標的、誘引テーマ、ツール、インフラに重複が報告されるが、別アクターとして扱う。 | 中 | `source--darkhorse-2023`, `source--qax-2024` |
| Lazarus Group | shares-tools-with | PEBBLEDASH等の再利用はDPRK内部のツール共有または開発者再配置の可能性を示す。 | 中 | `source--blurred-attribution`, `source--qax-2024` |
| APT43 | overlaps-with | 共有alias: Kimsuky | 低 | `source--joint-csa-2023` |
| APT43 | overlaps-with | MITRE treats APT43 as an associated Kimsuky group name, while Mandiant defines APT43 using its own collection scope. The overlap is well supported, but exact one-to-one identity is not. | 高 | `source--mitre-live-kimsuky-2026`, `source--mandiant-apt43-2023` |
| Lazarus Group | overlaps-with | DPRK threat actor cluster boundaries overlap in open source reporting, with some security researchers consolidating all attributed North Korean state-sponsored cyber activity under [Lazarus Group](https://attack.mitre.org/groups/G0032), rather than tracking operationally distinct subgroups. | 高 | `source--mitre-live-kimsuky-2026` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | 北朝鮮RGB傘下。対象調査と信頼醸成型ソーシャルエンジニアリングを大規模に運用する。 |
| Capability | フィッシングキット、悪性文書、LNK/CHM/MSC、PowerShell/VBScript/JScript、独自・公開RAT、Androidマルウェア。 |
| Infrastructure | 類似ドメイン、無料メール、VPS、侵害Webサーバ、クラウドストレージ、GitHub、メールC2。 |
| Victim | 政府、外交、軍・防衛、シンクタンク、大学、研究者、メディア、原子力・航空宇宙・金融等。 |
| Socio-political | 核・ミサイル、米韓関係、対中・対露関係、制裁など時事性の高い話題を誘引に使う。 |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Kimsuky, Velvet Chollima | canonical-name | 高 | North Korea | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://securityintelligence.com/media/recent-activity-from-itg16-a-north-korean-threat-group/<br>https://us-cert.cisa.gov/ncas/alerts/aa20-301a |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Emerald Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Opal Sleet | multiple-name-intersection | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Ruby Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Kimsuky | canonical-name | 高 | KP, Korea (Democratic People's Republic of) | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://www.cfr.org/interactive/cyber-operations/kimsuky<br>https://www.pwc.co.uk/issues/cyber-security-data-privacy/research/tracking-kimsuky-north-korea-based-cyber-espionage-group-part-2.html |
| misp-threat-actor | APT43 | single-alias-intersection | 中 |  | https://www.mandiant.com/resources/blog/apt43-north-korea-cybercrime-espionage<br>https://mandiant.widen.net/s/zvmfw5fnjs/apt43-report |
| misp-microsoft-activity-group | Emerald Sleet | canonical-name | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Opal Sleet | multiple-name-intersection | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Ruby Sleet | single-alias-intersection | 中 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Kimsuky - G0094 | mitre-external-id | 高 |  | https://asert.arbornetworks.com/stolen-pencil-campaign-targets-academia/<br>https://attack.mitre.org/groups/G0094<br>https://blog.alyac.co.kr/2234 |
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
| malware--appleseed | AppleSeed | コマンド実行、収集、キー入力・画面取得、ファイル転送を行う独自バックドア。 | 2019-05-06 | 2024 | 高 | `source--operation-newton`, `source--rapid7-2024` |
| malware--alphaseed | AlphaSeed | Go製。NaverメールとChrome DevTools ProtocolをC2に利用するAppleSeed系能力。 | 2023-06 | 2024 | 高 | `source--rapid7-2024` |
| malware--babyshark | BabyShark | VBScriptを中心とする初期活動・情報収集マルウェア。 | 2018 | 2024 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |
| malware--kgh | KGH Spyware | ブラウザ、メールクライアント、資格情報等を収集し、FTP C2と遠隔コマンドを利用する。 | 2020 | 2021-07 | 高 | `source--kgh-2021` |
| malware--fastviewer | FastViewer Android Malware | Google Play同期・開発者機能の悪用で配布されたAndroidマルウェア群。 | 2022 | 2023-03-20 | 高 | `source--browser-advisory-2023` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mail-sending-program | Mail Sending Program ver10.0 | フィッシングメールの作成・送信を大規模化する運用ツール。 | 2022-08-17 | 2024 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |
| tool--remote-admin | Remote Administration Tool Set | 侵害端末への継続アクセスと手動操作に使う正規・公開ツール群。 | 2021 | 2024 | 高 | `source--covert-stalker`, `source--qax-2024` |

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infra--lookalike-domains | Lookalike Phishing Domains | ポータル、報道機関、大学、信頼サービスに似せたドメイン。 | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--dmarc-2024`, `source--rapid7-2024` |
| infra--compromised-web-servers | Compromised Web Servers | フィッシング、ペイロード、Webシェル、C2に利用する侵害済みサーバ。 | 2019 | 2024 | 高 | `source--smoke-screen`, `source--operation-newton`, `source--covert-stalker` |
| infra--cloud-code-hosting | Cloud and Code Hosting Services | 正規サービスの評判を利用した配布・C2・ステージング。 | 2020 | 2025 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |
| infra--qr-credential-phishing | QR-code Credential Phishing Infrastructure | QR codes direct targets through landing pages to actor-controlled credential harvesting pages impersonating services such as Google login. | 2025-05 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--documents-shortcuts-help-console | HWP/Office/LNK/CHM/MSC | 悪性文書、ショートカット、HTML Help、管理コンソールによる配送と実行。 | 2012 | 2025 | 高 | `source--rapid7-2024`, `source--darkhorse-2023` |

### 脆弱性

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| vulnerability--cve-2019-0708 | CVE-2019-0708 | Operation Covert StalkerでRDP脆弱システムの侵害・踏み台化に使用したと報告。 | 2022 | 2023-09 | 高 | `source--covert-stalker` |

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--trust-building-phishing | Trust-building Spearphishing | 複数回の無害な連絡で信頼を築き、後続で悪性リンクや文書を送る。 | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| Smoke Screen / Stealth Power | campaign | 2019-03 | 2019-05 | DPRK関連のHWP/DOCフィッシング、HTA、PowerShellキーロガーを伴う活動。 | 高 | `source--smoke-screen` |
| Operation Newton | campaign | 2020 | 2021-10 | 工学研究者への資格情報フィッシングからAppleSeed、Webシェル、サーバ横展開へ進む活動。 | 高 | `source--operation-newton` |
| Operation DarkHorse | campaign | 2022-02 | 2023-10-16 | VBSからJSEへ変化したCHM活動。暗号資産、金融、保険等の誘引を利用。 | 中 | `source--darkhorse-2023` |
| Browser Extension and Google Play Abuse | campaign | 2022 | 2023-03-20 | Chromium拡張でGmailを窃取し、Google Play同期機能でAndroidマルウェアを配布。 | 高 | `source--browser-advisory-2023` |
| Kimsuky QR-code Spearphishing Campaign | campaign | 2025-05 | 2025-06 | Kimsuky impersonated foreign advisers, embassy and think-tank personnel, and conference organizers. QR codes led think-tank and strategic-advisory targets to credential-harvesting infrastructure. | 高 | `source--fbi-kimsuky-quishing-2026` |

少なくとも2012年から活動。2019年のSmoke ScreenとAppleSeed、2020-2021年のOperation Newton、2022-2023年のDarkHorseとCovert Stalker、2023年のブラウザ拡張・Google Play悪用、2024年のDMARC悪用へと配送・収集能力を更新している。

2025年5月から6月、FBIはKimsukyがQRコードを用いてシンクタンクや戦略助言組織を標的にし、偽Googleログイン等で認証情報を窃取する活動を観測した。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | South Korea | 最重要の継続的対象。 | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |
| countries | Germany | 政策専門家および防衛関連。 | 2021 | 2024 | 高 | `source--browser-advisory-2023`, `source--qax-2024` |
| sectors | Government and Diplomacy | 政府、議会、外交、政策関係者。 | 2012 | 2025 | 高 | `source--joint-csa-2023` |
| sectors | Think Tanks and Academia | 政策研究、大学、学術、科学・工学研究者。 | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |
| sectors | Finance, Insurance, and Cryptocurrency | 金融契約、保険、暗号資産関連の組織と個人。 | 2022 | 2024 | 中 | `source--darkhorse-2023`, `source--qax-2024` |
| roles | Journalists and Policy Experts | DPRK政策に関する非公開見解と信頼ネットワークを持つ個人。 | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |

選定ロジック: 組織規模より、北朝鮮に関する非公開情報や信頼ネットワークへアクセスできる個人を優先する。

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Reconnaissance | T1589 | Gather Victim Identity Information | 専門家、記者、研究者、連絡先をOSINTで調査する。 |  |  | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |
| Initial Access | T1566.001 | Phishing: Spearphishing Attachment | HWP、Office、LNK、CHM、MSC、パスワード付きアーカイブを配送する。 |  | activity--smoke-screen, activity--darkhorse | 2012 | 2025 | 高 | `source--rapid7-2024`, `source--darkhorse-2023` |
| Initial Access | T1566.002 | Phishing: Spearphishing Link | 資格情報フィッシング、侵害サイト、クラウド上のペイロードへのリンクを送る。 | malware--appleseed, malware--fastviewer | activity--operation-newton, activity--browser-google-play | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--operation-newton` |
| Execution | T1059.001 | Command and Scripting Interpreter: PowerShell | 後段取得、復号、メモリ内実行、情報収集、持続化にPowerShellを使う。 |  | activity--smoke-screen, activity--darkhorse | 2019-03 | 2025 | 高 | `source--smoke-screen`, `source--rapid7-2024` |
| Persistence | T1053.005 | Scheduled Task/Job: Scheduled Task | マルウェアやスクリプトを定期実行するタスクを作成する。 | malware--appleseed |  | 2019-05-06 | 2024 | 高 | `source--operation-newton`, `source--rapid7-2024` |
| Persistence | T1505.003 | Server Software Component: Web Shell | 侵害WebサーバにPHP/JSP Webシェルを配置し、C2管理とファイル操作に使う。 |  | activity--operation-newton | 2019 | 2023-09 | 高 | `source--operation-newton`, `source--covert-stalker` |
| Collection | T1114 | Email Collection | 資格情報、ブラウザ拡張、メール転送等でメールボックス内容を窃取する。 |  | activity--browser-google-play | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--browser-advisory-2023` |
| Credential Access | T1056.003 | Input Capture: Web Portal Capture | 偽ログインページとプロキシで認証情報を窃取する。 |  | activity--operation-newton | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--operation-newton` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | HTTP、FTP、メールC2を通じて収集データを流出させる。 | malware--appleseed, malware--kgh | activity--operation-newton | 2019-05-06 | 2025 | 高 | `source--operation-newton`, `source--kgh-2021` |
| Initial Access | T1566.002 | Phishing: Spearphishing Link | Delivered QR images in targeted emails; scanning the code led the victim to a registration or secure-drive lure and onward to credential harvesting. |  | activity--kimsuky-quishing-2025 | 2025-05 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |
| Credential Access, Collection | T1056.003 | Input Capture: Web Portal Capture | A fake Google account login page collected credentials entered by targeted users. |  | activity--kimsuky-quishing-2025 | 2025-06 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |
| Lateral Movement | T1550.004 | Use Alternate Authentication Material: Web Session Cookie | The FBI attack lifecycle identifies session-token theft and MFA bypass following credential capture. |  | activity--kimsuky-quishing-2025 | 2025-05 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |
| Persistence, Privilege Escalation | T1098 | Account Manipulation | The FBI lifecycle identifies account persistence or manipulation after successful credential and session theft. |  | activity--kimsuky-quishing-2025 | 2025-05 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |

## IOC／artifact概要

- IOC値: 1235件
- IOC観測: 1527件
- 複数攻撃で観測: 1件
- 要レビュー候補: 367件
- 非IOC artifact観測: 869件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Kimsukyの中核任務は北朝鮮政権のための戦略諜報と認証情報・メール窃取である。 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |  |
| 最大の強みは高度なソーシャルエンジニアリングと信頼構築である。 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |  |
| Kimsuky added QR-code delivery to its established trust-building spearphishing and credential-theft workflow during May-June 2025. | 高 | `source--fbi-kimsuky-quishing-2026` |  |
| MITRE treats APT43 as an associated Kimsuky group name, while Mandiant defines APT43 using its own collection scope. The overlap is well supported, but exact one-to-one identity is not. | 高 | `source--mitre-live-kimsuky-2026`, `source--mandiant-apt43-2023` | verification_status=partially-supported; Vendor collection boundaries differ; do not replace both profiles with a single exact alias record. The sources support overlap but do not establish that every APT43 observation belongs to the narrower Kimsuky activity set. |

### 情報ギャップ

- ベンダー別クラスタ間の厳密な境界。
- DPRK内部でのツール共有と開発者再配置の実態。
- 一部画像主体PDFの完全なテキスト抽出。

### 不確実性

- APT37、Konni、Lazarusとの重複は同一性ではなく共有・再利用で説明できる。
- DarkHorseのKimsuky帰属には競合評価がある。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--joint-csa-2023 | North Korea Using Social Engineering to Enable Hacking of Think Tanks, Academia, and Media | FBI, DOS, NSA, NIS, NPA, MOFA | 2023-06-01 | kimsuky/Joint_CSA_NK_Using_Social_Engineering_20230531.pdf | government-advisory | TLP:CLEAR | 高 |
| source--dmarc-2024 | North Korean Actors Exploit Weak DMARC Security Policies | FBI, DOS, NSA | 2024-05-02 | kimsuky/Exploit Weak DMARC.pdf | government-advisory | TLP:CLEAR | 高 |
| source--rapid7-2024 | Kimsuky's Phishing and Payload Tactics | Rapid7 | 2024 | kimsuky/rapid7-Kimsukys-Phishing-and-Payload-Tactics_wp.pdf | vendor-report | TLP:CLEAR | 高 |
| source--operation-newton | Operation Newton: Hi Kimsuky? | Virus Bulletin | 2021-10 | kimsuky/Operation_Newton_Kimsuky-APPLE(SEED).pdf | technical-report | TLP:CLEAR | 高 |
| source--covert-stalker | Operation Covert Stalker | AhnLab | 2023-11-01 | kimsuky/20231101_Kimsuky_OP.-Covert-Stalker-EN.pdf | vendor-report | TLP:CLEAR | 高 |
| source--darkhorse-2023 | Operation DarkHorse CHM Attack Analysis | Genians | 2023-10-16 | kimsuky/20231016_threat_inteligence_report_DarkHorse.pdf | vendor-report | TLP:CLEAR | 中 |
| source--browser-advisory-2023 | Warning on KIMSUKY Cyber Actor's Recent Campaigns against Google's Browser and App Store Services | BfV and NIS | 2023-03-20 | kimsuky/kimsuky-2023-03-20-joint-cyber-security-advisory.pdf | government-advisory | TLP:CLEAR | 高 |
| source--kgh-2021 | Kimsuky New KGH Spyware Component Analysis | ThreatBook Labs | 2021-07 | kimsuky/Kimsuky-KGH.pdf | vendor-report | TLP:CLEAR | 中 |
| source--smoke-screen | Analysis of the APT Campaign Smoke Screen | ESRC | 2019-04-17 | kimsuky/Smoke Screen.pdf | vendor-report | TLP:CLEAR | 高 |
| source--microsoft-actor-list | Microsoft Threat Actor List | Microsoft-derived repository data | 不明 | microsoft-threat-actor-list.xlsx | reference-table | TLP:CLEAR | 中 |
| source--qax-2024 | Cybersecurity Threats 2024 Annual Report | QAX | 2025 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | annual-report | TLP:CLEAR | 中 |
| source--blurred-attribution | Blurred Lines of Cyber Threat Attribution | Repository source | 2025 | International Strategic/Korea/ Blurred-Lines-of-Cyber-Threat-Attribution.pdf | conference-report | TLP:CLEAR | 中 |
| source--fbi-kimsuky-quishing-2026 | North Korean Kimsuky Actors Use Malicious QR Codes to Target Organizations | Federal Bureau of Investigation / IC3 | 2026-01-08 | https://www.ic3.gov/CSA/2026/260108.pdf | government-flash | TLP:CLEAR | 高 |
| source--mitre-live-kimsuky-2026 | Kimsuky, Group G0094 | MITRE ATT&CK | 2026-04-23 | https://attack.mitre.org/groups/G0094/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mandiant-apt43-2023 | APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations | Mandiant | 2023-03-28 | https://cloud.google.com/blog/topics/threat-intelligence/apt43-north-korea-cybercrime-espionage/ | vendor-research | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

未検証リークは中核評価に使用しない。IOCとartifactは観測イベント単位で別ファイルへ保存する。
