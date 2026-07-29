# Calypso 脅威アクタープロファイル

- プロファイルID: `actor--calypso`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Calypsoの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Calypso**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Comment Crew | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Links to Skyipot | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Mirage | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Pitty Tiger | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Comment Panda | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 3; mapping requires review. |
| PLA Unit 61398 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 3; mapping requires review. |
| TG-8223 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 3; mapping requires review. |
| APT1 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 3; mapping requires review. |
| BrownFox | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 3; mapping requires review. |
| Group 3 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 3; mapping requires review. |
| GIF89a, ShadyRAT, Shanghai Group, Byzantine Candor | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 3; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
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
| APT1 | overlaps-with | 共有alias: Comment Crew | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Ke3chang | overlaps-with | 共有alias: Mirage | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| PittyTiger | overlaps-with | 共有alias: Pitty Tiger, PittyTiger | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | WEBC2, BISCUIT and many others |
| Infrastructure |  |
| Victim | U.S. cybersecurity firm Mandiant, later purchased by FireEye, released a report in February 2013 that exposed one of China's cyber espionage units, Unit 61398. The group, which FireEye called APT1, is a unit within China's People's Liberation Army (PLA) that has been linked to a wide range of cyber operations targeting U.S. private sector entities for espionage purposes. The comprehensive report detailed evidence connecting APT1 and the PLA, offered insight into APT1's operational malware and methodologies, and provided timelines of the espionage it conducted. |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Calypso | canonical-name | 高 | China | https://www.ptsecurity.com/ww-en/analytics/calypso-apt-2019/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Calypso&n=1 |
| etda-threat-group-cards | Comment Crew, APT 1 | multiple-name-intersection | 高 | China | https://www.symantec.com/connect/blogs/apt1-qa-attacks-comment-crew<br>https://en.wikipedia.org/wiki/PLA_Unit_61398<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Comment+Crew%2C+APT+1&n=1 |
| etda-threat-group-cards | PittyTiger, Pitty Panda | single-alias-intersection | 中 | China | https://apt.etda.or.th/cgi-bin/showcard.cgi?g=PittyTiger%2C+Pitty+Panda&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Nylon Typhoon | single-alias-intersection | 中 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT1 | multiple-name-intersection | 高 | CN, China | https://en.wikipedia.org/wiki/PLA_Unit_61398<br>http://intelreport.mandiant.com/Mandiant_APT1_Report.pdf<br>https://www.cfr.org/interactive/cyber-operations/pla-unit-61398 |
| misp-threat-actor | APT15 | single-alias-intersection | 中 | CN, China | https://www.fireeye.com/blog/threat-research/2014/09/forced-to-adapt-xslcmd-backdoor-now-on-os-x.html<br>http://arstechnica.com/security/2015/04/elite-cyber-crime-group-strikes-back-after-attack-by-rival-apt-gang/<br>https://github.com/nccgroup/Royal_APT |
| misp-threat-actor | Calypso | canonical-name | 高 | CN | https://www.ptsecurity.com/upload/corporate/ru-ru/analytics/calypso-apt-2019-rus.pdf<br>https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/<br>https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html |
| misp-microsoft-activity-group | Nylon Typhoon | single-alias-intersection | 中 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | PittyTiger - G0011 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0011<br>http://blog.cassidiancybersecurity.com/post/2014/07/The-Eye-of-the-Tiger2<br>https://www.fireeye.com/blog/threat-research/2014/07/spy-of-the-tiger.html |
| misp-mitre-enterprise-intrusion-set | APT1 - G0006 | multiple-name-intersection | 高 |  | https://attack.mitre.org/wiki/Group/G0006<br>https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf |
| misp-mitre-intrusion-set | APT1 - G0006 | multiple-name-intersection | 高 |  | http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf<br>https://attack.mitre.org/groups/G0006<br>https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf |
| misp-mitre-intrusion-set | Ke3chang - G0004 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0004<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/ |
| misp-mitre-intrusion-set | PittyTiger - G0011 | single-alias-intersection | 中 |  | https://airbus-cyber-security.com/the-eye-of-the-tiger/<br>https://attack.mitre.org/groups/G0011<br>https://www.fireeye.com/blog/threat-research/2014/07/spy-of-the-tiger.html |
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
| malware--biscuit-and-many-others | BISCUIT and many others | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--webc2 | WEBC2 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| 中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化 | cyber-espionage | 不明 | 不明 | 2026-05-22 | target--activity-rule--sector--97fa6f38a056d42117be |  | ttp--activity-rule--20b1bae9b0c6bca32748, ttp--activity-rule--7f1ef34595aa281d7470, ttp--activity-rule--b2ce07fcea1c942aa118 | victim--activity-rule--72a9b284ae5c1aa7f781 | 中国系サイバースパイ活動が、Linux向けShowboatとWindows向けJFMBackdoorで通信事業者を標的化。 活動は少なくとも2022年半ばから続き、アジア太平洋と中東の組織を狙い、Calypso(別名、Red Lamassu)に帰属。 攻撃者は複数の通信事業者風ドメインを用意し、標的組織になりすますインフラを使用していた。 Showboatはモジュール式のフレームワークで、侵害後の永続化、情報収集、ファイル転送、プロセス隠蔽、SOCKS5プロキシ機能を備える。 JFMBackdoorは多機能な諜報用マルウェアで、DLLサイドローディングで読み込まれ、リバースシェル、ファイル操作、画面取得、痕跡削除などが可能。 | 中 | `source--daily-350d930382dd3ed9f923` |
| GhostNet | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

GhostNet

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イスラエル | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | インド | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ウクライナ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてウクライナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カザフスタン | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてカザフスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | キルギス | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてキルギスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | シンガポール | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてシンガポールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | スイス | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてスイスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | タイ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ノルウェー | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてノルウェーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | フランス | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベラルーシ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてベラルーシが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | モンゴル | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてモンゴルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ルクセンブルク | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてルクセンブルクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ロシア | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | Targeting text mentions china. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 南アフリカ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国として南アフリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 日本 | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 米国 | レビュー済みアクターマッピングの標的欄に記録された米国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中央アジア | カザフスタン、キルギスで確認された標的・被害事例を中央アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | アラブ首長国連邦、イスラエル、トルコで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南アジア | アフガニスタン、インドで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東アジア | モンゴル、中国、台湾、日本、韓国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | シンガポール、タイ、ベトナムで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東欧 | ウクライナ、ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | ウクライナ、スイス、トルコ、ノルウェー、フランス、ベラルーシ、ベルギー、ルクセンブルク、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 情報通信 | 活動「中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-350d930382dd3ed9f923` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--97fa6f38a056d42117be |  | ttp--activity-rule--20b1bae9b0c6bca32748, ttp--activity-rule--7f1ef34595aa281d7470, ttp--activity-rule--b2ce07fcea1c942aa118 |  | espionage: 中国系サイバースパイ活動が、Linux向けShowboatとWindows向けJFMBackdoorで通信事業者を標的化。 | 不明 | 不明 | 2026-05-22 | 中 | `source--daily-350d930382dd3ed9f923` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1090 | Proxy | Showboatはモジュール式のフレームワークで、侵害後の永続化、情報収集、ファイル転送、プロセス隠蔽、SOCKS5プロキシ機能を備える。 |  | activity--daily-651f2178af4ab3c90c96 | 不明 | 不明 | 中 | `source--daily-350d930382dd3ed9f923` |
| Discovery | T1083 | File and Directory Discovery | JFMBackdoorは多機能な諜報用マルウェアで、DLLサイドローディングで読み込まれ、リバースシェル、ファイル操作、画面取得、痕跡削除などが可能。 |  | activity--daily-651f2178af4ab3c90c96 | 不明 | 不明 | 中 | `source--daily-350d930382dd3ed9f923` |
| Execution, Stealth | T1574.001 | DLL | JFMBackdoorは多機能な諜報用マルウェアで、DLLサイドローディングで読み込まれ、リバースシェル、ファイル操作、画面取得、痕跡削除などが可能。 |  | activity--daily-651f2178af4ab3c90c96 | 不明 | 不明 | 中 | `source--daily-350d930382dd3ed9f923` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 55件（`artifacts.csv`）

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
| source--calypso--0e7e4f509f2d953e | 200407 MWB COVID White Paper Final |  | 2004-07 | COVID/200407-MWB-COVID-White-Paper_Final.pdf | report | TLP:CLEAR | 中 |
| source--calypso--2e8dcdc34e3d8a19 | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--calypso--3a2fabd4303aaf44 | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--calypso--3c36875326389864 | calypso |  | 不明 | actor_profile/evidence/calypso.csv | structured-data | TLP:CLEAR | 中 |
| source--calypso--4122cc635cc78682 | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--calypso--4d8d55f96e9fdb8f | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--calypso--4ed45b721c043e96 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--calypso--572db5bc0325ab0e | 2021 Vulnerability Landscape |  | 2021 | summary/2022/2021 Vulnerability Landscape.pdf | report | TLP:CLEAR | 中 |
| source--calypso--5a96fdf874b38e48 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--calypso--5cf6cac8ca43bf04 | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--calypso--5df2ed07b29f5b9b | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--calypso--623eb96ebf0ea82b | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--calypso--8977615ec58b186c | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--calypso--a663e4b258965c58 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--calypso--cbe1bfe741302951 | 2024 Malicious Infrastructure Report |  | 2024 | summary/2025/2024 Malicious Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--calypso--e04640fed1c55bf5 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--daily-350d930382dd3ed9f923 | 中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化 | lumen.com | 2026-05-22 | https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 不明 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
