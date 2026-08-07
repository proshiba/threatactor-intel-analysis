# APT37 脅威アクタープロファイル

- プロファイルID: `actor--apt37`
- 状態: draft
- 更新日時: 2026-08-07T10:35:22Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

APT37の標準化プロファイル。リポジトリ内の専用資料14件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT37**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Group123 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ScarCruft | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| InkySquid | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Reaper | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Ricochet Chollima | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TEMP.Reaper | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Red Eyes | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 4; mapping requires review. |
| Venus 121 <br>(금성121) | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 4; mapping requires review. |
| THALLIUM | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 4; mapping requires review. |
| G0067 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 4; mapping requires review. |

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
| Lazarus Group | overlaps-with | North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name [Lazarus Group](https://attack.mitre.org/groups/G0032) instead of tracking clusters or subgroups. | 高 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [APT37](https://attack.mitre.org/groups/G0067) is a North Korean state-sponsored cyber espionage group that has been active since at least 2012. The group has targeted victims primarily in South Korea, but also in Japan, Vietnam, Russia, Nepal, China, India, Romania, Kuwait, and other parts of the Middle East. [APT37](https://attack.mitre.org/groups/G0067) has also been linked to the following campaigns between 2016-2018: Operation Daybreak, Operation Erebus, Golden Time, Evil New Year, Are you Happy?, FreeMilk, North Korean Human Rights, and Evil New Year 2018.(Citation: FireEye APT37 Feb 2018)(Citation: Securelist ScarCruft Jun 2016)(Citation: Talos Group123)<br><br>North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name [Lazarus Group](https://attack.mitre.org/groups/G0032) instead of tracking clusters or subgroups. |
| Capability | DOGCALL, HAPPYWORK, KARAE, SLOWDRIFT, SHUTTERSPEED, WINERACK, NavRAT, POORAIM, ROKRAT, CORALDECK, BLUELIGHT, Final1stspy, Cobalt Strike, SOUNDWAVE, ZUMKONG, RICECURRY, MILKDROP, GELCAPSULE, RUHAPPY, Flash Exploit CVE-2016-4117, KEVDROID, BabyShark, KimJongRAT, GOLDBACKDOOR |
| Infrastructure |  |
| Victim | Primarily South Korea – though also Japan, Vietnam and the Middle East – in various industry verticals, including chemicals, electronics, manufacturing, aerospace, automotive, and healthcare; Scarcruft Tracking: Russia, Nepal, South Korea, China, India, Kuwait and Romania |
| Socio-political | North Korea |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Kimsuky, Velvet Chollima | single-alias-intersection | 中 | North Korea | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://securityintelligence.com/media/recent-activity-from-itg16-a-north-korean-threat-group/<br>https://us-cert.cisa.gov/ncas/alerts/aa20-301a |
| etda-threat-group-cards | Reaper, APT 37, Ricochet Chollima, ScarCruft | canonical-name | 高 | North Korea | https://www2.fireeye.com/rs/848-DID-242/images/rpt_APT37.pdf<br>https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html<br>https://threatpost.com/scarcruft-apt-group-used-latest-flash-zero-day-in-two-dozen-attacks/118642/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Emerald Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Kimsuky | single-alias-intersection | 中 | KP, Korea (Democratic People's Republic of) | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://www.cfr.org/interactive/cyber-operations/kimsuky<br>https://www.pwc.co.uk/issues/cyber-security-data-privacy/research/tracking-kimsuky-north-korea-based-cyber-espionage-group-part-2.html |
| misp-threat-actor | APT37 | canonical-name | 高 | KP, Korea (Democratic People's Republic of) | https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/<br>https://www.fireeye.com/blog/threat-research/2018/02/apt37-overlooked-north-korean-actor.html<br>https://www2.fireeye.com/rs/848-DID-242/images/rpt_APT37.pdf |
| misp-microsoft-activity-group | Emerald Sleet | single-alias-intersection | 中 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | APT37 - G0067 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0067<br>https://www2.fireeye.com/rs/848-DID-242/images/rpt%20APT37.pdf<br>https://securelist.com/operation-daybreak/75100/ |
| misp-mitre-intrusion-set | APT37 - G0067 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0067<br>https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html<br>https://securelist.com/operation-daybreak/75100/ |
| misp-mitre-intrusion-set | Kimsuky - G0094 | single-alias-intersection | 中 |  | https://asert.arbornetworks.com/stolen-pencil-campaign-targets-academia/<br>https://attack.mitre.org/groups/G0094<br>https://blog.alyac.co.kr/2234 |
| misp-360net | ScarCruft - APT-C-28 | single-alias-intersection | 中 | korea | https://apt.360.net/report/apts/79.html |

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
| malware--babyshark | BabyShark | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--bluelight | BLUELIGHT | [BLUELIGHT](https://attack.mitre.org/software/S0657) is a remote access Trojan used by [APT37](https://attack.mitre.org/groups/G0067) that was first observed in early 2021.(Citation: Volexity InkySquid BLUELIGHT August 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--coraldeck | CORALDECK | [CORALDECK](https://attack.mitre.org/software/S0212) is an exfiltration tool used by [APT37](https://attack.mitre.org/groups/G0067). (Citation: FireEye APT37 Feb 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--daily-397062646adc91061d4a | BirdCall | APT37との直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 2024 | 2026-05-05 | 高 | `source--daily-4961e6946e3ccac84312`, `source--daily-68fe928d58956df4f752`, `source--daily-b232a8993d5d82211f66` |
| malware--daily-c07163c7c1b6cc1b80eb | NarwhalRAT | APT37との直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 不明 | 中 | `source--daily-82bdd80456957234d81b` |
| malware--dogcall | DOGCALL | [DOGCALL](https://attack.mitre.org/software/S0213) is a backdoor used by [APT37](https://attack.mitre.org/groups/G0067) that has been used to target South Korean government and military organizations in 2017. It is typically dropped using a Hangul Word Processor (HWP) exploit. (Citation: FireEye APT37 Feb 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--final1stspy | Final1stspy | [Final1stspy](https://attack.mitre.org/software/S0355) is a dropper family that has been used to deliver [DOGCALL](https://attack.mitre.org/software/S0213).(Citation: Unit 42 Nokki Oct 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--flash-exploit-cve-2016-4117 | Flash Exploit CVE-2016-4117 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--gelcapsule | GELCAPSULE | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--goldbackdoor | GOLDBACKDOOR | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--happywork | HAPPYWORK | [HAPPYWORK](https://attack.mitre.org/software/S0214) is a downloader used by [APT37](https://attack.mitre.org/groups/G0067) to target South Korean government and financial victims in November 2016. (Citation: FireEye APT37 Feb 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--karae | KARAE | [KARAE](https://attack.mitre.org/software/S0215) is a backdoor typically used by [APT37](https://attack.mitre.org/groups/G0067) as first-stage malware. (Citation: FireEye APT37 Feb 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--kevdroid | KEVDROID | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--kimjongrat | KimJongRAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--milkdrop | MILKDROP | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--navrat | NavRAT | [NavRAT](https://attack.mitre.org/software/S0247) is a remote access tool designed to upload, download, and execute files. It has been observed in attacks targeting South Korea. (Citation: Talos NavRAT May 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pooraim | POORAIM | [POORAIM](https://attack.mitre.org/software/S0216) is a backdoor used by [APT37](https://attack.mitre.org/groups/G0067) in campaigns since at least 2014. (Citation: FireEye APT37 Feb 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ricecurry | RICECURRY | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--rokrat | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) is a cloud-based remote access tool (RAT) used by [APT37](https://attack.mitre.org/groups/G0067) to target victims in South Korea. [APT37](https://attack.mitre.org/groups/G0067) has used ROKRAT during several campaigns from 2016 through 2021.(Citation: Talos ROKRAT)(Citation: Talos Group123)(Citation: Volexity InkySquid RokRAT August 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ruhappy | RUHAPPY | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--shutterspeed | SHUTTERSPEED | [SHUTTERSPEED](https://attack.mitre.org/software/S0217) is a backdoor used by [APT37](https://attack.mitre.org/groups/G0067). (Citation: FireEye APT37 Feb 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--slowdrift | SLOWDRIFT | [SLOWDRIFT](https://attack.mitre.org/software/S0218) is a backdoor used by [APT37](https://attack.mitre.org/groups/G0067) against academic and strategic victims in South Korea. (Citation: FireEye APT37 Feb 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--soundwave | SOUNDWAVE | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--winerack | WINERACK | [WINERACK](https://attack.mitre.org/software/S0219) is a backdoor used by [APT37](https://attack.mitre.org/groups/G0067). (Citation: FireEye APT37 Feb 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--zumkong | ZUMKONG | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| Are you Happy? | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| JPEG を武器化する北朝鮮の APT37：多段階攻撃によりmspaint などのプロセスに悪意のコードを挿入 | infrastructure-operation | 不明 | 不明 | 2025-08-16 | target--country--south-korea | malware--rokrat | ttp--activity-rule--c668e54ddd027a2bc60b | victim--activity-rule--7d94c1412e3341c2d087 | 北朝鮮APT37が主に韓国を標的としたキャンペーンで、JPEGに隠したRoKRAT新亜種でWindowsを侵害する攻撃を展開。 ZIP内LNKがバッチでPowerShell起動→XOR復号→シェルコード実行の多段手口。 mspaint.exe/notepad.exeへコード注入し、ファイルレス化で検知を回避。 Dropbox/Yandex等クラウドAPIを悪用し、配布・C2・窃取データ送信を隠蔽。 対策はEDR、ユーザー訓練・端末管理、クラウド通信の能動監視。 | 高 | `source--daily-468e8f8090fe0064b1c4` |
| Microsoftを装うフィッシングとデッドドロップC2を悪用するAPT37 NarwhalRATの分析 | phishing-campaign | 不明 | 不明 | 2026-06-16 |  | malware--daily-c07163c7c1b6cc1b80eb | ttp--activity-rule--3adf302f3671ba0415ec, ttp--activity-rule--651e8c74dca3cb33f22a |  | Geniansは、Microsoftアカウントチームを装うスピアフィッシングで配布されるPythonベースのNarwhalRATを分析した。 攻撃はZIP内の悪性LNKから始まり、PowerShell、BAT、curl、公式Python埋め込み版を悪用して多段階感染を行う。 NarwhalRATはキーロギング、画面キャプチャ、USBデータ収集、マイク録音、ファイル操作、リモートコマンド実行機能を持つ。 C2は韓国の中継サーバーとpCloud APIを組み合わせた二重構造で、デッドドロップResolverとして正規クラウドを利用する。 TTP、韓国ユーザー向けの偽装、pCloud利用、過去事例との類似性から、APT37関連活動との関連が示唆されている。 | 中 | `source--daily-82bdd80456957234d81b` |
| Microsoft、ゼロデイ悪用のWindows LNK脆弱性を「緩和」 | reported-activity | 不明 | 不明 | 2025-12-04 |  |  |  |  | Microsoftは、国家支援/犯罪集団が悪用するWindows LNKのゼロデイ(CVE-2025-9491)に対し静かに「緩和」を実施。 脆弱性はLNKのTarget欄に空白を詰め引数を隠し実行させる手口で、利用者がLNKを開く操作を誘導されると成立。 攻撃者はメールで遮断される.LNKをZIP等に同梱して配布し、Ursnif・Gh0st RAT・TrickBot・PlugXなどを投下。 Trend Microは少なくとも11の国家系/犯罪集団（Mustang PandaやAPT37等）が悪用と報告、欧州外交官標的の事例も。 11月更新でTarget全表示に変更されたが完全修正ではなく、0patchが長文Target検知・警告の非公式修正を提供。 | 中 | `source--daily-79fb3689c96eb2761182` |
| ScarCruftハッカー、ゲームプラットフォーム経由でAndroidマルウェアBirdCallを配布 | malware-campaign | 2024 | 2026-05-05 | 2026-05-06 | target--activity-rule--country--f0d8df51439c4d0f3a05 | malware--daily-397062646adc91061d4a, malware--rokrat |  | victim--activity-rule--edba50549fb5c44ad984 | 北朝鮮系APT37/ScarCruftは、ビデオゲーム基盤を侵害し、Android版BirdCallバックドアを配布した。 ESETによると、攻撃はYanbian地域の朝鮮民族コミュニティや北朝鮮脱北者を狙ったものとみられる。 sqgame系サイト上のAndroidゲームAPKがトロイの木馬化され、Windows更新経路ではRokRAT経由でBirdCallが展開された。 Android版BirdCallは連絡先、通話履歴、SMS、端末情報、文書、画像、秘密鍵を収集し、スクリーンショットや録音も行う。 Android版は2024年10月ごろ作成され、少なくとも7バージョンが確認され、2024年末ごろから攻撃が継続していた可能性がある。 | 高 | `source--daily-4961e6946e3ccac84312`, `source--daily-68fe928d58956df4f752`, `source--daily-b232a8993d5d82211f66` |
| 北朝鮮ハッカー、新たな「VeilShell」バックドアを使用したステルス攻撃を実施 | phishing-campaign | 不明 | 不明 | 2024-10-04 |  |  | ttp--activity-rule--2a1ce1684d6f7a91220b | victim--activity-rule--18860e466b214b6d3f98 | 北朝鮮のAPT37ハッカーグループが新たなバックドア「VeilShell」を使用し、カンボジアなど東南アジア諸国を標的にした。 VeilShellは、データ窃取や遠隔操作を可能にするPowerShellベースのマルウェア。 複数のステルス技術を使用し、持続的な攻撃を実行。 この活動はSHROUDED#SLEEPと名付けられており、Securonixは、InkySquid、Reaper、RedEyes、Ricochet Chollima、Ruby Sleet、ScarCruftとしても知られるAPT37の仕業であると考えている。 攻撃チェーンは、フィッシングメールで開始し、AppDomainManagerインジェクションと呼ばれる攻撃手法が用いられた。流れは以下。 lnk > powershell > d.exe+dll(load by AppDomainManager) > js > powershell(veilshell) | 中 | `source--daily-f00592605535c739c5c3` |
| 北朝鮮のハッカー、偽の求人面接を通じてmacOS向けにFERRETマルウェアを展開 | malware-campaign | 不明 | 不明 | 2025-02-05 | target--activity-rule--sector--63c9fa67327d005b07b7 |  |  | victim--activity-rule--fda753ceec6db594850c | 北朝鮮の脅威アクターが、偽の求人面接を装い、macOS向けのFERRETマルウェアを配布。 被害者は、仮想会議用ソフトウェアのインストールや更新を要求するエラーが表示。これに促され、悪意のあるソフトウェアをダウンロード。 この攻撃は、JavaScriptベースのBeaverTailマルウェアをドロップし、さらにPython製のバックドアであるInvisibleFerretを展開。 攻撃者は、LinkedIn上でリクルーターを装い、ターゲットにビデオ評価を完了するよう促す。 最終的に、Golangベースのバックドアと情報窃取ツールをドロップし、MetaMaskウォレットから資金を盗むことを目的としている。 BeaverTailマルウェアを含む悪意のあるnpmパッケージ（postcss-optimizer）も確認されている。このパッケージは、Windows、macOS、Linuxシステムを感染させることができ、非常に人気なpostcssライブラリを模倣 | 中 | `source--daily-5be59ed011b127efaaf3` |
| APT37がGoogleのFind Hubを悪用、Android端末を遠隔初期化する攻撃 | phishing-campaign | 不明 | 不明 | 2025-11-12 | target--country--south-korea |  |  | victim--activity-rule--5c6a103acdc9c5f18de0 | 北朝鮮系がGoogleのFind Hubを悪用し、標的のAndroid端末の位置把握とリモート初期化で痕跡消去を行う。 攻撃は主に韓国人を狙い、KakaoTalkで接触後、国税庁や警察を装うフィッシングと署名MSIでPCにRATを導入。 AutoIT経由で持続化とC2通信を設定し、Remcos/Quasar/RftRATでGoogleやNaver資格情報を奪取して設定変更。 奪取したGoogleアカウントでFind Hubにログインし、GPSを確認した上で端末を複数回ワイプし、回復や警告を妨害。 被害者のKakaoTalk PCセッションを乗っ取り、連絡先へ拡散。対策は2段階認証/パスキーや送信者の電話確認等。 | 高 | `source--daily-24c4e22a7b0cd08d6063` |
| APT37のハッカーが新たなマルウェアでエアギャップネットワークに侵入 | infrastructure-operation | 不明 | 不明 | 2026-02-28 |  | malware--bluelight |  |  | 北朝鮮系APT37（ScarCruft等）が「Ruby Jumper」作戦で、新ツールにより隔離環境と接続環境間のデータ移送を実現 侵入は悪意あるWindowsショートカット（LNK）を起点にPowerShellを実行し、デコイ文書で注意をそらしつつペイロードを展開 RESTLEAFがZoho WorkDriveを使うC2でシェルコードを取得し、次段のRubyローダーSNAKEDROPPERをダウンロードさせる Ruby 3.3.0環境をUSB関連ユーティリティを偽装したusbspeed.exeとしてインストールし、正規のoperating_system.rbを改ざんしてタスクrubyupdatecheckで自動実行させる THUMBSBDがUSBに隠し領域を作って双方向の中継点化、VIRUSTASKがLNK置換で拡散し、FOOTWINE/BLUELIGHTで監視・窃取を行う | 高 | `source--daily-98a40a134fc3127db612` |
| Erebus | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Evil New Year | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Evil New Year 2018 | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| FreeMilk | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Golden Time | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| North Korean Human Rights | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Operation Earth Kitsune | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Are you Happy? | APT37 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| JPEG を武器化する北朝鮮の APT37：多段階攻撃によりmspaint などのプロセスに悪意のコードを挿入 | APT37 | ROKRAT | T1102.003 One-Way Communication | 情報なし | 韓国 | 被害事例: JPEG を武器化する北朝鮮の APT37：多段階攻撃によりmspaint などのプロセスに悪意のコードを挿入 | 高 |
| Microsoftを装うフィッシングとデッドドロップC2を悪用するAPT37 NarwhalRATの分析 | APT37 | NarwhalRAT | T1059.001 PowerShell, T1059.006 Python | 情報なし | 情報なし | 情報なし | 中 |
| Microsoft、ゼロデイ悪用のWindows LNK脆弱性を「緩和」 | APT37 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| ScarCruftハッカー、ゲームプラットフォーム経由でAndroidマルウェアBirdCallを配布 | APT37 | BirdCall, ROKRAT | 情報なし | 情報なし | 北朝鮮 | 被害事例: ScarCruftハッカー、ゲームプラットフォーム経由でAndroidマルウェアBirdCallを配布 | 高 |
| 北朝鮮ハッカー、新たな「VeilShell」バックドアを使用したステルス攻撃を実施 | APT37 | 情報なし | T1059.001 PowerShell | 情報なし | 情報なし | 被害事例: 北朝鮮ハッカー、新たな「VeilShell」バックドアを使用したステルス攻撃を実施 | 中 |
| 北朝鮮のハッカー、偽の求人面接を通じてmacOS向けにFERRETマルウェアを展開 | APT37 | 情報なし | 情報なし | 情報なし | 暗号資産・Web3 | 被害事例: 北朝鮮のハッカー、偽の求人面接を通じてmacOS向けにFERRETマルウェアを展開 | 中 |
| APT37がGoogleのFind Hubを悪用、Android端末を遠隔初期化する攻撃 | APT37 | 情報なし | 情報なし | 情報なし | 韓国 | 被害事例: APT37がGoogleのFind Hubを悪用、Android端末を遠隔初期化する攻撃 | 高 |
| APT37のハッカーが新たなマルウェアでエアギャップネットワークに侵入 | APT37 | BLUELIGHT | 情報なし | 情報なし | 情報なし | 情報なし | 高 |
| Erebus | APT37 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Evil New Year | APT37 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Evil New Year 2018 | APT37 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| FreeMilk | APT37 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Golden Time | APT37 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| North Korean Human Rights | APT37 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Operation Earth Kitsune | APT37 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

Erebus; Golden Time; Evil New Year; Are you Happy?; FreeMilk; North Korean Human Rights; Evil New Year 2018; Operation Earth Kitsune

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | Targeting text mentions india. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | カンボジア | 活動「北朝鮮ハッカー、新たな「VeilShell」バックドアを使用したステルス攻撃を実施」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-f00592605535c739c5c3`, `source--target-audit-etda-threat-group-cards` |
| countries | クウェート | MITRE ATT&CKのGroup概要でAPT37の標的国として明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでAPT37の標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チェコ | 構造化OSINTの被害国フィールドでAPT37の標的・被害国としてチェコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ネパール | MITRE ATT&CKのGroup概要でAPT37の標的国として明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | Targeting text mentions vietnam. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでAPT37の標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ラオス | 構造化OSINTの被害国フィールドでAPT37の標的・被害国としてラオスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ルーマニア | Targeting text mentions romania. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | Targeting text mentions russia. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | Targeting text mentions china. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | 北朝鮮 | 活動「ScarCruftハッカー、ゲームプラットフォーム経由でAndroidマルウェアBirdCallを配布」の記述で標的として明示された国・地域。 | 2024 | 2026-05-05 | 中 | `source--daily-4961e6946e3ccac84312`, `source--daily-68fe928d58956df4f752`, `source--daily-b232a8993d5d82211f66` |
| countries | 日本 | Targeting text mentions japan. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 米国 | 構造化OSINTの被害国フィールドでAPT37の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 構造化OSINTの被害国フィールドでAPT37の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | Targeting text mentions south korea. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--daily-24c4e22a7b0cd08d6063`, `source--daily-468e8f8090fe0064b1c4`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 香港 | 構造化OSINTの被害国フィールドでAPT37の標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | アジア | 活動「北朝鮮ハッカー、新たな「VeilShell」バックドアを使用したステルス攻撃を実施」の記述で標的地域としてアジアが明示されている。 | 不明 | 不明 | 中 | `source--daily-f00592605535c739c5c3` |
| regions | 中東 | レビュー済みアクターマッピングの標的欄に記録された中東を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 南アジア | 活動「北朝鮮ハッカー、新たな「VeilShell」バックドアを使用したステルス攻撃を実施」の記述で標的地域として南アジアが明示されている。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--daily-f00592605535c739c5c3`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | 中国、北朝鮮、日本、韓国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--daily-24c4e22a7b0cd08d6063`, `source--daily-468e8f8090fe0064b1c4`, `source--daily-4961e6946e3ccac84312`, `source--daily-68fe928d58956df4f752`, `source--daily-b232a8993d5d82211f66`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | 活動「北朝鮮ハッカー、新たな「VeilShell」バックドアを使用したステルス攻撃を実施」の記述で標的地域として東南アジアが明示されている。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--daily-f00592605535c739c5c3`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東欧 | チェコ、ポーランド、ルーマニア、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | 活動「Microsoft、ゼロデイ悪用のWindows LNK脆弱性を「緩和」」の記述で標的地域として欧州が明示されている。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--daily-79fb3689c96eb2761182`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| sectors | 暗号資産・Web3 | 活動「北朝鮮のハッカー、偽の求人面接を通じてmacOS向けにFERRETマルウェアを展開」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5be59ed011b127efaaf3` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Healthcare | Targeting text indicates the Healthcare sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 北朝鮮ハッカー、新たな「VeilShell」バックドアを使用したステルス攻撃を実施 | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--activity-rule--2a1ce1684d6f7a91220b | メール／メールアカウント | data-theft: VeilShellは、データ窃取や遠隔操作を可能にするPowerShellベースのマルウェア。 | 不明 | 不明 | 2024-10-04 | 中 | `source--daily-f00592605535c739c5c3` |
| 被害事例: APT37がGoogleのFind Hubを悪用、Android端末を遠隔初期化する攻撃 | 非公開 | aggregate | multiple-organizations | reported | target--country--south-korea |  |  | エンドポイント, モバイル端末 |  | 不明 | 不明 | 2025-11-12 | 高 | `source--daily-24c4e22a7b0cd08d6063` |
| 被害事例: JPEG を武器化する北朝鮮の APT37：多段階攻撃によりmspaint などのプロセスに悪意のコードを挿入 | 非公開 | aggregate | multiple-organizations | reported | target--country--south-korea | malware--rokrat | ttp--activity-rule--c668e54ddd027a2bc60b | エンドポイント, クラウド／SaaS |  | 不明 | 不明 | 2025-08-16 | 高 | `source--daily-468e8f8090fe0064b1c4` |
| 被害事例: ScarCruftハッカー、ゲームプラットフォーム経由でAndroidマルウェアBirdCallを配布 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--f0d8df51439c4d0f3a05 | malware--daily-397062646adc91061d4a, malware--rokrat |  | エンドポイント, モバイル端末 |  | 2024 | 2026-05-05 | 2026-05-06 | 高 | `source--daily-4961e6946e3ccac84312`, `source--daily-68fe928d58956df4f752`, `source--daily-b232a8993d5d82211f66` |
| 被害事例: 北朝鮮のハッカー、偽の求人面接を通じてmacOS向けにFERRETマルウェアを展開 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--63c9fa67327d005b07b7 |  |  | ネットワーク機器 |  | 不明 | 不明 | 2025-02-05 | 中 | `source--daily-5be59ed011b127efaaf3` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.001 | PowerShell | lnk > powershell > d.exe+dll(load by AppDomainManager) > js > powershell(veilshell) |  | activity--daily-99c12226cea0199fb84b | 不明 | 不明 | 中 | `source--daily-f00592605535c739c5c3` |
| Execution | T1059.001 | PowerShell | 攻撃はZIP内の悪性LNKから始まり、PowerShell、BAT、curl、公式Python埋め込み版を悪用して多段階感染を行う。 |  | activity--daily-3678a940d72c4fad1a5d | 不明 | 不明 | 中 | `source--daily-82bdd80456957234d81b` |
| Execution | T1059.006 | Python | Geniansは、Microsoftアカウントチームを装うスピアフィッシングで配布されるPythonベースのNarwhalRATを分析した。 | malware--daily-c07163c7c1b6cc1b80eb | activity--daily-3678a940d72c4fad1a5d | 不明 | 不明 | 中 | `source--daily-82bdd80456957234d81b` |
| Command And Control | T1102.003 | One-Way Communication | Dropbox/Yandex等クラウドAPIを悪用し、配布・C2・窃取データ送信を隠蔽。 |  | activity--daily-04c3bda3362bec6cbbe7 | 不明 | 不明 | 中 | `source--daily-468e8f8090fe0064b1c4` |
| Collection | T1005 | Data from Local System | [APT37](https://attack.mitre.org/groups/G0067) has collected data from victims' local systems.(Citation: FireEye APT37 Feb 2018) |  |  | 不明 | 不明 | 高 | `source--apt37--4b34b22806460897`, `source--mitre-attack-19-1` |
| Discovery | T1010 | Application Window Discovery | 129 Obfuscated Files or Information T1027 Indicator Removal from Tools T1027.005 Hidden Window T1564.003 Keylogging T1056.001 Application Window Discovery T1010 Query Registry T1012 |  |  | 不明 | 不明 | 中 | `source--apt37--32d6af5670be4ea3` |
| Discovery | T1012 | Query Registry | or Information T1027 Indicator Removal from Tools T1027.005 Hidden Window T1564.003 Keylogging T1056.001 Application Window Discovery T1010 Query Registry T1012 |  |  | 不明 | 不明 | 中 | `source--apt37--32d6af5670be4ea3` |
| Collection | T1025 | Data from Removable Media | exfiltrates it. Data from Removable Media T1025 FadeStealer collects information on removable storage devices, compresses the logs, and exfiltrates them to the C2 server. Archive via Utility T1560.001 FadeStealer uses rar.exe to compress stolen logs before exfiltration. Command and Control Web Protocol T1071.0 |  |  | 不明 | 不明 | 中 | `source--apt37--8c7b4ab3309be364` |
| Stealth | T1027 | Obfuscated Files or Information | [APT37](https://attack.mitre.org/groups/G0067) obfuscates strings and payloads.(Citation: Talos Group123)(Citation: Securelist ScarCruft May 2019)(Citation: Volexity InkySquid RokRAT August 2021) |  |  | 不明 | 不明 | 高 | `source--apt37--32d6af5670be4ea3`, `source--apt37--8c7b4ab3309be364`, `source--apt37--e0b524fc6f94c455`, `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | [APT37](https://attack.mitre.org/groups/G0067) uses steganography to send images to users that are embedded with shellcode.(Citation: Talos Group123)(Citation: Securelist ScarCruft May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.005 | Indicator Removal from Tools | and and Scripting Interpreter T1059 Windows Command Shell T1059.003 Shared Modules T1129 Obfuscated Files or Information T1027 Indicator Removal from Tools T1027.005 Hidden Window T1564.003 Keylogging T1056.001 Application Window Discovery T1010 Query Registry T1012 |  |  | 不明 | 不明 | 中 | `source--apt37--32d6af5670be4ea3` |
| Exfiltration | T1029 | Scheduled Transfer | l payloads. Bidirectional Communication T1102.002 NubSpy receives commands and sends results via the PubNub API. Exfiltration Scheduled Transfer T1029 LightPeek is registered in the task scheduler to periodically capture and upload screenshots to the C2 server. Exfiltration Over C2 Channel T1041 FadeStealer and LightPeek both transmit stolen data to the C2 server. Impact Data Encrypted for Impact T1486 VCD Ra |  |  | 不明 | 不明 | 中 | `source--apt37--8c7b4ab3309be364` |
| Discovery | T1033 | System Owner/User Discovery | [APT37](https://attack.mitre.org/groups/G0067) identifies the victim username.(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--apt37--8c7b4ab3309be364`, `source--mitre-attack-19-1` |
| Stealth | T1036.001 | Invalid Code Signature | [APT37](https://attack.mitre.org/groups/G0067) has signed its malware with an invalid digital certificates listed as “Tencent Technology (Shenzhen) Company Limited.”(Citation: Securelist ScarCruft Jun 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery Collection T1119 Automated Collection Exfiltration T1041 Exfiltration Over C2 Channel [표 10] MITRE ATT&CK, Tactics and Techniques 17 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge 18 https://attack.mitre.org/groups/G0067/ |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897`, `source--apt37--8c7b4ab3309be364`, `source--apt37--f8dde9641e96c02a` |
| Uncategorized | T1045 | MITRE ATT&CK T1045 | 1027) Input Capture (T1119) Web Service (T1102) Command-Line Interface (T1059) Process Injection (T1055) Automated Collection (T1056) Software Packing (T1045) |  |  | 不明 | 不明 | 中 | `source--apt37--e0b524fc6f94c455` |
| Uncategorized | T1050 | MITRE ATT&CK T1050 | Access Execution Persistence Defense Evasion Collection Command and Control Spearphishing Attachment (T1193) Execution through Module Load (T1129) New Service (T1050) Obfuscated Files or Information (T1027) Input Capture (T1119) Web Service (T1102) Command-Line Interface (T1059) Process Injection (T1055) Automated Collection (T1056) Software Packing (T1045) |  |  | 不明 | 不明 | 中 | `source--apt37--e0b524fc6f94c455` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [APT37](https://attack.mitre.org/groups/G0067) has created scheduled tasks to run malicious scripts on a compromised host.(Citation: Volexity InkySquid RokRAT August 2021) |  |  | 不明 | 不明 | 高 | `source--apt37--8c7b4ab3309be364`, `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | [APT37](https://attack.mitre.org/groups/G0067) injects its malware variant, [ROKRAT](https://attack.mitre.org/software/S0240), into the cmd.exe process.(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--apt37--e0b524fc6f94c455`, `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.002 | Portable Executable Injection | s CommandShell T1059.007 CommandandScriptingInterpreter:JavaScriptT1203 Exploitationfor Client Execution T1204.002 User Execution:Malicious File DefenseEvasion T1055.002 Process Injection:PortableExecutableInjection T1070.004 Indicator Removal:FileDeletionT1140 Deobfuscate/DecodeFiles or Information Discovery T1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1005 DatafromLocal SystemCommandandControl T1071.001 Applicatio |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897` |
| Privilege Escalation, Stealth | T1055.013 | Process Doppelgänging | OR-obfuscated VCD Ransomware and executes it in memory. File Deletion T1070.004 The ransomware deletes itself after execution. Process Doppelgänging T1055.013 TxPyLoader uses the Transacted Hollowing technique to inject malicious payloads into legitimate processes. Hidden Window T1564.003 The Rust version of CHILLYCHINO executes commands received from the attacker while keeping the window hidden. Discovery File and Direct |  |  | 不明 | 不明 | 中 | `source--apt37--8c7b4ab3309be364` |
| Collection, Credential Access | T1056 | Input Capture | scated Files or Information (T1027) Input Capture (T1119) Web Service (T1102) Command-Line Interface (T1059) Process Injection (T1055) Automated Collection (T1056) Software Packing (T1045) |  |  | 不明 | 不明 | 中 | `source--apt37--e0b524fc6f94c455` |
| Collection, Credential Access | T1056.001 | Keylogging | mmand Shell T1059.003 Shared Modules T1129 Obfuscated Files or Information T1027 Indicator Removal from Tools T1027.005 Hidden Window T1564.003 Keylogging T1056.001 Application Window Discovery T1010 Query Registry T1012 |  |  | 不明 | 不明 | 中 | `source--apt37--32d6af5670be4ea3`, `source--apt37--8c7b4ab3309be364` |
| Discovery | T1057 | Process Discovery | [APT37](https://attack.mitre.org/groups/G0067)'s Freenki malware lists running processes using the Microsoft Windows API.(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--apt37--f8dde9641e96c02a`, `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | [APT37](https://attack.mitre.org/groups/G0067) has used Ruby scripts to execute payloads.(Citation: Volexity InkySquid RokRAT August 2021) |  |  | 不明 | 不明 | 高 | `source--apt37--32d6af5670be4ea3`, `source--apt37--e0b524fc6f94c455`, `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | unts T1583.006 AcquireInfrastructure:WebServices Initial Access T1566.001 Phishing:SpearphishingAttachment T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.007 CommandandScriptingInterpreter:JavaScriptT1203 Exploitationfor Client Execution T1204.002 User Execution:Malicious File DefenseEvasion T1055.002 Process Injection:Po |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897`, `source--apt37--8c7b4ab3309be364` |
| Execution | T1059.002 | AppleScript | r Information: Spearphishing Link T1589 Gather Victim Identity Information: Credentials Initial Access T1566.002 Phishing: Spearphishing Link Execution T1059.002 Command and Scripting Interpreter: AppleScript T1204.002 User Execution: Malicious File Persistence T1547.015 Boot or Logon Autostart Execution: Login Items T1569.001 System Services: Launchctl Defense Evasion T1070.004 Indicator Removal: File Deletion T1564.001 Hid |  |  | 不明 | 不明 | 中 | `source--apt37--f8dde9641e96c02a` |
| Execution | T1059.003 | Windows Command Shell | [APT37](https://attack.mitre.org/groups/G0067) has used the command-line interface.(Citation: FireEye APT37 Feb 2018)(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--apt37--32d6af5670be4ea3`, `source--apt37--4b34b22806460897`, `source--apt37--8c7b4ab3309be364`, `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [APT37](https://attack.mitre.org/groups/G0067) executes shellcode and a VBA script to decode Base64 strings.(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | [APT37](https://attack.mitre.org/groups/G0067) has used Python scripts to execute payloads.(Citation: Volexity InkySquid RokRAT August 2021) |  |  | 不明 | 不明 | 高 | `source--apt37--8c7b4ab3309be364`, `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | 03 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.007 CommandandScriptingInterpreter:JavaScriptT1203 Exploitationfor Client Execution T1204.002 User Execution:Malicious File DefenseEvasion T1055.002 Process Injection:PortableExecutableInjection T1070.004 Indicator Removal:FileDeletionT1140 Deobfuscate/DecodeFiles or Information Dis |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897` |
| Stealth | T1070.004 | File Deletion | er Execution: Malicious File Persistence T1547.015 Boot or Logon Autostart Execution: Login Items T1569.001 System Services: Launchctl Defense Evasion T1070.004 Indicator Removal: File Deletion T1564.001 Hide Artifacts: Hidden Files and Directories Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery Collection T1119 Automated Collection Exfiltration T1041 Exfiltration Over C |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897`, `source--apt37--8c7b4ab3309be364`, `source--apt37--f8dde9641e96c02a` |
| Command And Control | T1071.001 | Web Protocols | [APT37](https://attack.mitre.org/groups/G0067) uses HTTPS to conceal C2 communications.(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--apt37--4b34b22806460897`, `source--apt37--8c7b4ab3309be364`, `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [APT37](https://attack.mitre.org/groups/G0067) collects the computer name, the BIOS model, and execution path.(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--apt37--4b34b22806460897`, `source--apt37--f8dde9641e96c02a`, `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | tor Removal: File Deletion T1564.001 Hide Artifacts: Hidden Files and Directories Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery Collection T1119 Automated Collection Exfiltration T1041 Exfiltration Over C2 Channel [표 10] MITRE ATT&CK, Tactics and Techniques 17 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge 18 https://attack.mitre.org/groups/G0067 |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897`, `source--apt37--8c7b4ab3309be364`, `source--apt37--f8dde9641e96c02a` |
| Command And Control | T1102 | Web Service | hishing Attachment (T1193) Execution through Module Load (T1129) New Service (T1050) Obfuscated Files or Information (T1027) Input Capture (T1119) Web Service (T1102) Command-Line Interface (T1059) Process Injection (T1055) Automated Collection (T1056) Software Packing (T1045) |  |  | 不明 | 不明 | 中 | `source--apt37--e0b524fc6f94c455` |
| Command And Control | T1102.002 | Bidirectional Communication | [APT37](https://attack.mitre.org/groups/G0067) leverages social networking sites and cloud platforms (AOL, Twitter, Yandex, Mediafire, pCloud, Dropbox, and Box) for C2.(Citation: FireEye APT37 Feb 2018)(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--apt37--8c7b4ab3309be364`, `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [APT37](https://attack.mitre.org/groups/G0067) has downloaded second stage malware from compromised websites.(Citation: FireEye APT37 Feb 2018)(Citation: Securelist ScarCruft May 2019)(Citation: Volexity InkySquid BLUELIGHT August 2021)(Citation: Volexity InkySquid RokRAT August 2021) |  |  | 不明 | 不明 | 高 | `source--apt37--8c7b4ab3309be364`, `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | [APT37](https://attack.mitre.org/groups/G0067) leverages the Windows API calls: VirtualAlloc(), WriteProcessMemory(), and CreateRemoteThread() for process injection.(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | uter name and user name. Collection Keylogging T1056.001 FadeStealer compresses keystroke logs and exfiltrates them to the C2 server. Screen Capture T1113 Both LightPeek and FadeStealer capture screenshots and transmit them to the C2 server. Audio Capture T1123 FadeStealer records audio from the target's microphone and 35 |  |  | 不明 | 不明 | 中 | `source--apt37--8c7b4ab3309be364` |
| Collection | T1119 | Automated Collection | tifacts: Hidden Files and Directories Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery Collection T1119 Automated Collection Exfiltration T1041 Exfiltration Over C2 Channel [표 10] MITRE ATT&CK, Tactics and Techniques 17 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge 18 https://attack.mitre.org/groups/G0067/ |  |  | 不明 | 不明 | 中 | `source--apt37--e0b524fc6f94c455`, `source--apt37--f8dde9641e96c02a` |
| Discovery | T1120 | Peripheral Device Discovery | [APT37](https://attack.mitre.org/groups/G0067) has a Bluetooth device harvester, which uses Windows Bluetooth APIs to find information on connected Bluetooth devices. (Citation: Securelist ScarCruft May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1123 | Audio Capture | [APT37](https://attack.mitre.org/groups/G0067) has used an audio capturing utility known as SOUNDWAVE that captures microphone input.(Citation: FireEye APT37 Feb 2018) |  |  | 不明 | 不明 | 高 | `source--apt37--8c7b4ab3309be364`, `source--mitre-attack-19-1` |
| Execution | T1129 | Shared Modules | Data/goldll/proc.php MITRE ATT&CK Technique Name Technique ID Command and Scripting Interpreter T1059 Windows Command Shell T1059.003 Shared Modules T1129 Obfuscated Files or Information T1027 Indicator Removal from Tools T1027.005 Hidden Window T1564.003 Keylogging T1056.001 Application Window Discovery T1010 Query Registry T1012 |  |  | 不明 | 不明 | 中 | `source--apt37--32d6af5670be4ea3`, `source--apt37--e0b524fc6f94c455` |
| Command And Control | T1132.001 | Standard Encoding | ol Web Protocol T1071.001 CHILLYCHINO communicates with the C2 server via HTTP/S to receive commands and transmit execution results. Standard Encoding T1132.001 Both LightPeek and CHILLYCHINO apply Base64 encoding when sending data to the C2 server. Ingress Tool Transfer T1105 The attacker executes curl commands to download additional payloads. Bidirectional Communication T1102.002 NubSpy receives commands and sends resul |  |  | 不明 | 不明 | 中 | `source--apt37--8c7b4ab3309be364` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | xecution T1204.002 User Execution:Malicious File DefenseEvasion T1055.002 Process Injection:PortableExecutableInjection T1070.004 Indicator Removal:FileDeletionT1140 Deobfuscate/DecodeFiles or Information Discovery T1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1005 DatafromLocal SystemCommandandControl T1071.001 ApplicationLayer Protocol:WebProtocols Exfiltration T1041 ExfiltrationOver C2Channel T1567.002 Exfiltr |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897`, `source--apt37--8c7b4ab3309be364` |
| Initial Access | T1189 | Drive-by Compromise | [APT37](https://attack.mitre.org/groups/G0067) has used strategic web compromises, particularly of South Korean websites, to distribute malware. The group has also used torrent file-sharing sites to more indiscriminately disseminate malware to victims. As part of their compromises, the group has used a Javascript based profiler called RICECURRY to profile a victim's web browser and deliver malicious code accordingly.(Citation: Securelist ScarCruft Jun 2016)(Citation: FireEye APT37 Feb 2018)(Citation: Volexity InkySquid BLUELIGHT August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1193 | MITRE ATT&CK T1193 | ersarial Tactics, Techniques & Common Knowledge. Initial Access Execution Persistence Defense Evasion Collection Command and Control Spearphishing Attachment (T1193) Execution through Module Load (T1129) New Service (T1050) Obfuscated Files or Information (T1027) Input Capture (T1119) Web Service (T1102) Command-Line Interface (T1059) Process Injection (T1055) Automated Collection (T1056) Software Packing (T1045) |  |  | 不明 | 不明 | 中 | `source--apt37--e0b524fc6f94c455` |
| Execution | T1203 | Exploitation for Client Execution | [APT37](https://attack.mitre.org/groups/G0067) has used exploits for Flash Player (CVE-2016-4117, CVE-2018-4878), Word (CVE-2017-0199), Internet Explorer (CVE-2020-1380 and CVE-2020-26411), and Microsoft Edge (CVE-2021-26411) for execution.(Citation: Securelist ScarCruft Jun 2016)(Citation: FireEye APT37 Feb 2018)(Citation: Talos Group123)(Citation: Volexity InkySquid BLUELIGHT August 2021) |  |  | 不明 | 不明 | 高 | `source--apt37--4b34b22806460897`, `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [APT37](https://attack.mitre.org/groups/G0067) has sent spearphishing attachments attempting to get a user to open them.(Citation: FireEye APT37 Feb 2018) |  |  | 不明 | 不明 | 高 | `source--apt37--4b34b22806460897`, `source--apt37--8c7b4ab3309be364`, `source--apt37--f8dde9641e96c02a`, `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | server. Exfiltration Over C2 Channel T1041 FadeStealer and LightPeek both transmit stolen data to the C2 server. Impact Data Encrypted for Impact T1486 VCD Ransomware encrypts files using a hybrid encryption scheme combining RSA and AES-256-CBC. 36 |  |  | 不明 | 不明 | 中 | `source--apt37--8c7b4ab3309be364` |
| Impact | T1529 | System Shutdown/Reboot | [APT37](https://attack.mitre.org/groups/G0067) has used malware that will issue the command <code>shutdown /r /t 1</code> to reboot a system after wiping its MBR.(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [APT37](https://attack.mitre.org/groups/G0067)'s has added persistence via the Registry key <code>HKCU\Software\Microsoft\CurrentVersion\Run\</code>.(Citation: FireEye APT37 Feb 2018)(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--apt37--8c7b4ab3309be364`, `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.015 | Login Items | 002 Phishing: Spearphishing Link Execution T1059.002 Command and Scripting Interpreter: AppleScript T1204.002 User Execution: Malicious File Persistence T1547.015 Boot or Logon Autostart Execution: Login Items T1569.001 System Services: Launchctl Defense Evasion T1070.004 Indicator Removal: File Deletion T1564.001 Hide Artifacts: Hidden Files and Directories Discovery T1057 Process Discovery T1082 System Information Discove |  |  | 不明 | 不明 | 中 | `source--apt37--f8dde9641e96c02a` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | [APT37](https://attack.mitre.org/groups/G0067) has a function in the initial dropper to bypass Windows UAC in order to execute the next payload with higher privileges.(Citation: Securelist ScarCruft May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [APT37](https://attack.mitre.org/groups/G0067) has used a credential stealer known as ZUMKONG that can harvest usernames and passwords stored in browsers.(Citation: FireEye APT37 Feb 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.002 | Dynamic Data Exchange | [APT37](https://attack.mitre.org/groups/G0067) has used Windows DDE for execution of commands and a malicious VBS.(Citation: Securelist ScarCruft Jun 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | dia T1025 FadeStealer collects information on removable storage devices, compresses the logs, and exfiltrates them to the C2 server. Archive via Utility T1560.001 FadeStealer uses rar.exe to compress stolen logs before exfiltration. Command and Control Web Protocol T1071.001 CHILLYCHINO communicates with the C2 server via HTTP/S to receive commands and transmit execution results. Standard Encoding T1132.001 Both LightPeek |  |  | 不明 | 不明 | 中 | `source--apt37--8c7b4ab3309be364` |
| Impact | T1561.002 | Disk Structure Wipe | [APT37](https://attack.mitre.org/groups/G0067) has access to destructive malware that is capable of overwriting a machine's Master Boot Record (MBR).(Citation: FireEye APT37 Feb 2018)(Citation: Talos Group123) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | 47.015 Boot or Logon Autostart Execution: Login Items T1569.001 System Services: Launchctl Defense Evasion T1070.004 Indicator Removal: File Deletion T1564.001 Hide Artifacts: Hidden Files and Directories Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery Collection T1119 Automated Collection Exfiltration T1041 Exfiltration Over C2 Channel [표 10] MITRE ATT&CK, Tactics and Te |  |  | 不明 | 不明 | 中 | `source--apt37--f8dde9641e96c02a` |
| Stealth | T1564.003 | Hidden Window | eter T1059 Windows Command Shell T1059.003 Shared Modules T1129 Obfuscated Files or Information T1027 Indicator Removal from Tools T1027.005 Hidden Window T1564.003 Keylogging T1056.001 Application Window Discovery T1010 Query Registry T1012 |  |  | 不明 | 不明 | 中 | `source--apt37--32d6af5670be4ea3`, `source--apt37--8c7b4ab3309be364` |
| Initial Access | T1566.001 | Spearphishing Attachment | [APT37](https://attack.mitre.org/groups/G0067) delivers malware using spearphishing emails with malicious HWP attachments.(Citation: FireEye APT37 Feb 2018)(Citation: Talos Group123)(Citation: Securelist ScarCruft May 2019) |  |  | 不明 | 不明 | 高 | `source--apt37--4b34b22806460897`, `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | ue Description Reconnaissance T1598.003 Phishing for Information: Spearphishing Link T1589 Gather Victim Identity Information: Credentials Initial Access T1566.002 Phishing: Spearphishing Link Execution T1059.002 Command and Scripting Interpreter: AppleScript T1204.002 User Execution: Malicious File Persistence T1547.015 Boot or Logon Autostart Execution: Login Items T1569.001 System Services: Launchctl Defense Evasion T1070. |  |  | 不明 | 不明 | 中 | `source--apt37--649e5a3ce38b5fef`, `source--apt37--f8dde9641e96c02a` |
| Initial Access | T1566.003 | Spearphishing via Service | rceDevelopment T1585.002 EstablishAccounts:Email Accounts T1583.006 AcquireInfrastructure:WebServices Initial Access T1566.001 Phishing:SpearphishingAttachment T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.007 CommandandScriptingInterpreter:JavaScriptT1203 Exploitationfor Client Execution T1204.002 User Execution:Malicio |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897`, `source--apt37--649e5a3ce38b5fef` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | yDiscoveryCollection T1005 DatafromLocal SystemCommandandControl T1071.001 ApplicationLayer Protocol:WebProtocols Exfiltration T1041 ExfiltrationOver C2Channel T1567.002 ExfiltrationOver WebService:ExfiltrationtoCloudStorage[표8-1] MITREATT&CK, Tactics andTechniques Genians SecurityCenter 51 |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897` |
| Execution | T1569.001 | Launchctl | mand and Scripting Interpreter: AppleScript T1204.002 User Execution: Malicious File Persistence T1547.015 Boot or Logon Autostart Execution: Login Items T1569.001 System Services: Launchctl Defense Evasion T1070.004 Indicator Removal: File Deletion T1564.001 Hide Artifacts: Hidden Files and Directories Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery Collection T1119 Aut |  |  | 不明 | 不明 | 中 | `source--apt37--f8dde9641e96c02a` |
| Resource Development | T1583.006 | Web Services | c Technique Description Reconnaissance T1598.002 Phishingfor Information:SpearphishingAttachment ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1583.006 AcquireInfrastructure:WebServices Initial Access T1566.001 Phishing:SpearphishingAttachment T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.007 Commandand |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897`, `source--apt37--8c7b4ab3309be364` |
| Resource Development | T1584.004 | Server | dure) Resource Development Web Services T1583.006 The ScarCruft group uses the PubNub real-time messaging API for command and control (C2). Server T1584.004 Malware is distributed through compromised South Korean websites. Malware T1587.001 Custom-built malware is crafted and distributed according to the target profile. Execution Malicious File T1204.002 The compressed archive includes an LNK file with a topic designe |  |  | 不明 | 不明 | 中 | `source--apt37--8c7b4ab3309be364` |
| Resource Development | T1585.002 | Email Accounts | ator of Attack)8.1. MITREATT&CKMatrix Tactic Technique Description Reconnaissance T1598.002 Phishingfor Information:SpearphishingAttachment ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1583.006 AcquireInfrastructure:WebServices Initial Access T1566.001 Phishing:SpearphishingAttachment T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterprete |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897`, `source--apt37--649e5a3ce38b5fef` |
| Resource Development | T1585.003 | Cloud Accounts | on: Spearphishing Attachment T1598.003 Phishing for Information: Spearphishing Link Resource Development T1585.002 Establish Accounts: Email Accounts T1585.003 Establish Accounts: Cloud Accounts Initial Access T1566.002 Phishing: Spearphishing Link T1566.003 Phishing: Spearphishing via Service [표 06] MITRE ATT&CK, Tactics and Techniques 9 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge 10 APT37 Group |  |  | 不明 | 不明 | 中 | `source--apt37--649e5a3ce38b5fef` |
| Resource Development | T1587.001 | Malware | Nub real-time messaging API for command and control (C2). Server T1584.004 Malware is distributed through compromised South Korean websites. Malware T1587.001 Custom-built malware is crafted and distributed according to the target profile. Execution Malicious File T1204.002 The compressed archive includes an LNK file with a topic designed to lure the victim into clicking, which drops additional scripts. PowerShell T1059. |  |  | 不明 | 不明 | 中 | `source--apt37--8c7b4ab3309be364` |
| Reconnaissance | T1589 | Gather Victim Identity Information | a. MITRE ATT&CK17 Matrix - APT3718 Group Descriptions Tactic Technique Description Reconnaissance T1598.003 Phishing for Information: Spearphishing Link T1589 Gather Victim Identity Information: Credentials Initial Access T1566.002 Phishing: Spearphishing Link Execution T1059.002 Command and Scripting Interpreter: AppleScript T1204.002 User Execution: Malicious File Persistence T1547.015 Boot or Logon Autostart Execution: Lo |  |  | 不明 | 不明 | 中 | `source--apt37--f8dde9641e96c02a` |
| Reconnaissance | T1598.002 | Spearphishing Attachment | Threat IntelligenceReport 8. 공격지표(Indicator of Attack)8.1. MITREATT&CKMatrix Tactic Technique Description Reconnaissance T1598.002 Phishingfor Information:SpearphishingAttachment ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1583.006 AcquireInfrastructure:WebServices Initial Access T1566.001 Phishing:SpearphishingAttachment T1566.003 Phishing:SpearphishingviaService Execution T1059.001 Com |  |  | 不明 | 不明 | 中 | `source--apt37--4b34b22806460897`, `source--apt37--649e5a3ce38b5fef` |
| Reconnaissance | T1598.003 | Spearphishing Link | 1 08. 공격 지표 (Indicator of Attack) a. MITRE ATT&CK17 Matrix - APT3718 Group Descriptions Tactic Technique Description Reconnaissance T1598.003 Phishing for Information: Spearphishing Link T1589 Gather Victim Identity Information: Credentials Initial Access T1566.002 Phishing: Spearphishing Link Execution T1059.002 Command and Scripting Interpreter: AppleScript T1204.002 User Execution: Malicious File Persiste |  |  | 不明 | 不明 | 中 | `source--apt37--649e5a3ce38b5fef`, `source--apt37--f8dde9641e96c02a` |

## IOC／artifact概要

- IOC値: 361件
- IOC観測: 480件
- 複数攻撃で観測: 0件
- 要レビュー候補: 66件
- 非IOC artifact観測: 363件（`artifacts.csv`）

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
| source--apt37--1d95f4aeb39f3651 | Stairwell threat report The ink stained trail of GOLDBACKDOOR |  | 不明 | group123/Stairwell-threat-report-The-ink-stained-trail-of-GOLDBACKDOOR.pdf | report | TLP:CLEAR | 中 |
| source--apt37--32d6af5670be4ea3 | Chinotto Backdoor Technical Analysis of the APT Reapers Powerful |  | 不明 | group123/Chinotto_Backdoor_Technical_Analysis_of_the_APT_Reapers_Powerful.pdf | report | TLP:CLEAR | 中 |
| source--apt37--3960850deb0fd588 | Dragon Messenger APT Group123 |  | 不明 | group123/Dragon Messenger_APT_Group123.pdf | report | TLP:CLEAR | 中 |
| source--apt37--46d1184d8464a1e7 | special ioc |  | 不明 | group123/special-ioc.txt | text-data | TLP:CLEAR | 中 |
| source--apt37--4b34b22806460897 | 20231229 threat inteligence report market |  | 2023-12-29 | group123/20231229_threat_inteligence_report_market.pdf | report | TLP:CLEAR | 中 |
| source--apt37--55e1e08f054cc33d | README |  | 不明 | group123/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--apt37--649e5a3ce38b5fef | 2023 Group123 threat inteligence report BitB |  | 2023 | group123/2023_Group123_threat_inteligence_report_BitB.pdf | report | TLP:CLEAR | 中 |
| source--apt37--8c7b4ab3309be364 | ScarCruft’s New Language Whispering in PubNub, Crafting Backdoor in Rust, Striking with Ransomware |  | 不明 | group123/ScarCruft’s New Language_Whispering in PubNub, Crafting Backdoor in Rust, Striking with Ransomware.pdf | report | TLP:CLEAR | 中 |
| source--apt37--9e553e6cdd33b310 | ScarCruft (APT37) active in South Korea |  | 不明 | group123/ScarCruft (APT37) active in South Korea.pdf | report | TLP:CLEAR | 中 |
| source--apt37--b2b14c4d8c08d493 | ESRC 1808 TLP White IR002 RocketMan English |  | 不明 | group123/ESRC-1808-TLP-White-IR002_RocketMan_English.pdf | report | TLP:CLEAR | 中 |
| source--apt37--d92d0649e1fbc17f | README |  | 不明 | group123/IEexploit202212sample/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--apt37--e0b524fc6f94c455 | apt37newyear |  | 不明 | group123/apt37newyear.pdf | report | TLP:CLEAR | 中 |
| source--apt37--f532fa1ec3d0ac93 | (전체본)공개보고서 OperationCodeonToast |  | 不明 | group123/(전체본)공개보고서-OperationCodeonToast.pdf | report | TLP:CLEAR | 中 |
| source--apt37--f8dde9641e96c02a | 20230620 threat inteligence report apt37 macos |  | 2023-06-20 | group123/20230620_threat_inteligence_report_apt37_macos.pdf | report | TLP:CLEAR | 中 |
| source--daily-24c4e22a7b0cd08d6063 | APT37がGoogleのFind Hubを悪用、Android端末を遠隔初期化する攻撃 | bleepingcomputer.com | 2025-11-12 | https://www.bleepingcomputer.com/news/security/apt37-hackers-abuse-google-find-hub-in-android-data-wiping-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-468e8f8090fe0064b1c4 | JPEG を武器化する北朝鮮の APT37：多段階攻撃によりmspaint などのプロセスに悪意のコードを挿入 | iototsecnews.jp | 2025-08-16 | https://iototsecnews.jp/2025/08/04/apt37-hackers-weaponizes-jpeg-files-to-attack-windows-systems-leveraging-mspaint-exe/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4961e6946e3ccac84312 | ScarCruftハッカー、ゲームプラットフォーム経由でAndroidマルウェアBirdCallを配布 | welivesecurity.com | 2026-05-06 | https://www.welivesecurity.com/en/eset-research/rigged-game-scarcruft-compromises-gaming-platform-supply-chain-attack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-5be59ed011b127efaaf3 | 北朝鮮のハッカー、偽の求人面接を通じてmacOS向けにFERRETマルウェアを展開 | thehackernews.com | 2025-02-05 | https://thehackernews.com/2025/02/north-korean-hackers-deploy-ferret.html | osint-report | TLP:CLEAR | 中 |
| source--daily-68fe928d58956df4f752 | ScarCruftハッカー、ゲームプラットフォーム経由でAndroidマルウェアBirdCallを配布 — IOC補助資料 | raw.githubusercontent.com | 不明 | https://raw.githubusercontent.com/eset/malware-ioc/master/scarcruft/samples.md5 | osint-report | TLP:CLEAR | 中 |
| source--daily-79fb3689c96eb2761182 | Microsoft、ゼロデイ悪用のWindows LNK脆弱性を「緩和」 | bleepingcomputer.com | 2025-12-04 | https://www.bleepingcomputer.com/news/microsoft/microsoft-mitigates-windows-lnk-flaw-exploited-as-zero-day/ | osint-report | TLP:CLEAR | 中 |
| source--daily-82bdd80456957234d81b | Microsoftを装うフィッシングとデッドドロップC2を悪用するAPT37 NarwhalRATの分析 | genians.co.kr | 2026-06-16 | https://www.genians.co.kr/en/blog/threat_intelligence/narwhalrat | osint-report | TLP:CLEAR | 中 |
| source--daily-98a40a134fc3127db612 | APT37のハッカーが新たなマルウェアでエアギャップネットワークに侵入 | bleepingcomputer.com | 2026-02-28 | https://www.bleepingcomputer.com/news/security/apt37-hackers-use-new-malware-to-breach-air-gapped-networks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-b232a8993d5d82211f66 | ScarCruftハッカー、ゲームプラットフォーム経由でAndroidマルウェアBirdCallを配布 — IOC補助資料 | raw.githubusercontent.com | 不明 | https://raw.githubusercontent.com/eset/malware-ioc/master/scarcruft/samples.sha256 | osint-report | TLP:CLEAR | 中 |
| source--daily-f00592605535c739c5c3 | 北朝鮮ハッカー、新たな「VeilShell」バックドアを使用したステルス攻撃を実施 | thehackernews.com | 2024-10-04 | https://thehackernews.com/2024/10/north-korean-hackers-using-new.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
