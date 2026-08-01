# Inception 脅威アクタープロファイル

- プロファイルID: `actor--inception`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Inceptionの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Inception**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Blue Odin | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Cloud Atlas | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Inception Framework | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| MITRE: G0100 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the Russia worksheet.

- 国: Russia
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Inception](https://attack.mitre.org/groups/G0100) is a cyber espionage group active since at least 2014. The group has targeted multiple industries and governmental entities primarily in Russia, but has also been active in the United States and throughout Europe, Asia, Africa, and the Middle East.(Citation: Unit 42 Inception November 2018)(Citation: Symantec Inception Framework March 2018)(Citation: Kaspersky Cloud Atlas December 2014) |
| Capability | PowerShower, VBShower, LaZagne |
| Infrastructure |  |
| Victim | This threat actor targets governments and diplomatic organizations for espionage purposes. Suspected Operator in Ukraine working for Russia or its allies. |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Inception Framework, Cloud Atlas | multiple-name-intersection | 高 | Russia | https://www.symantec.com/connect/blogs/blue-coat-exposes-inception-framework-very-sophisticated-layered-malware-attack-targeted-milit<br>https://www.akamai.com/uk/en/multimedia/documents/white-paper/upnproxy-blackhat-proxies-via-nat-injections-white-paper.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Inception+Framework%2C+Cloud+Atlas&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Inception Framework | multiple-name-intersection | 高 | RU, Russian Federation | https://www.cfr.org/interactive/cyber-operations/inception-framework<br>https://web.archive.org/web/20160710180729/https://www.bluecoat.com/security-blog/2014-12-09/blue-coat-exposes-%E2%80%9C-inception-framework%E2%80%9D-very-sophisticated-layered-malware<br>https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2015/Inception_APT_Analysis_Bluecoat.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Inception - G0100 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0100<br>https://securelist.com/cloud-atlas-redoctober-apt-is-back-in-style/68083/<br>https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies |
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
| malware--powershower | PowerShower | [PowerShower](https://attack.mitre.org/software/S0441) is a PowerShell backdoor used by [Inception](https://attack.mitre.org/groups/G0100) for initial reconnaissance and to download and execute second stage payloads.(Citation: Unit 42 Inception November 2018)(Citation: Kaspersky Cloud Atlas August 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--vbshower | VBShower | [VBShower](https://attack.mitre.org/software/S0442) is a backdoor that has been used by [Inception](https://attack.mitre.org/groups/G0100) since at least 2019. [VBShower](https://attack.mitre.org/software/S0442) has been used as a downloader for second stage payloads, including [PowerShower](https://attack.mitre.org/software/S0441).(Citation: Kaspersky Cloud Atlas August 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Cloud Atlas | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Red October | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Cloud Atlas | Inception | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Red October | Inception | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

Red October; Cloud Atlas

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アゼルバイジャン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてアゼルバイジャンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アルメニア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてアルメニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イタリア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてイタリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イラン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてイランが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | インド | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | インドネシア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウガンダ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてウガンダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウクライナ | Targeting text mentions ukraine. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ウズベキスタン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてウズベキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オマーン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてオマーンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストリア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてオーストリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カザフスタン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてカザフスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | カタール | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてカタールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | キプロス | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてキプロスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | キルギス | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてキルギスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ギリシャ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてギリシャが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ケニア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてケニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | サウジアラビア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてサウジアラビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ジョージア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてジョージアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スイス | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてスイスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スリナム | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてスリナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | スロベニア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてスロベニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タジキスタン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてタジキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タンザニア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてタンザニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チェコ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてチェコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | トルクメニスタン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてトルクメニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | トルコ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パラグアイ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてパラグアイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ベネズエラ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてベネズエラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベラルーシ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてベラルーシが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ポルトガル | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてポルトガルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | モザンビーク | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてモザンビークが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モルドバ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてモルドバが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モロッコ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてモロッコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ヨルダン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてヨルダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | リトアニア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてリトアニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ルーマニア | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてルーマニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | レバノン | 構造化OSINTの被害国フィールドでInceptionの標的・被害国としてレバノンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | Targeting text mentions russia. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 南アフリカ | 構造化OSINTの被害国フィールドでInceptionの標的・被害国として南アフリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 米国 | The group has targeted multiple industries and governmental entities primarily in Russia, but has also been active in the United States and throughout Europe, Asia, Africa, and the Middle East.(Citation: Unit 42 Inception November 2018)(Citation: Symantec Inception Framework March 2018)(Citation: Kaspersky Cloud Atlas December 2014) | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでInceptionの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | アジア | MITRE ATT&CKのGroup概要でInceptionの標的範囲としてアジアが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | アフリカ | MITRE ATT&CKのGroup概要でInceptionの標的範囲としてアフリカが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | コーカサス | アゼルバイジャン、アルメニア、ジョージアで確認された標的・被害事例をコーカサスとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 中南米 | スリナム、パラグアイ、ブラジル、ベネズエラで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 中央アジア | ウズベキスタン、カザフスタン、キルギス、タジキスタン、トルクメニスタンで確認された標的・被害事例を中央アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 中東 | アラブ首長国連邦、イラン、オマーン、カタール、サウジアラビア、トルコ、ヨルダン、レバノンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南アジア | アフガニスタン、インド、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南欧 | イタリア、キプロス、ギリシャ、スロベニア、ポルトガルで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南米 | スリナム、パラグアイ、ブラジル、ベネズエラで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | インドネシア、ベトナム、マレーシアで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東欧 | ウクライナ、チェコ、ベラルーシ、モルドバ、ルーマニア、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | MITRE ATT&CKのGroup概要でInceptionの標的範囲として欧州が明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | iscovering rogue Mimikatz processes can be tricky because, since its inception, defenders have only had to worry about detecting compiled binaries. Nowadays, l T1003.001: LSASS Memory |  |  | 不明 | 不明 | 中 | `source--inception--f1cfea69304ea1b6` |
| Collection | T1005 | Data from Local System | [Inception](https://attack.mitre.org/groups/G0100) used a file hunting plugin to collect .txt, .pdf, .xls or .doc files from the infected host.(Citation: Kaspersky Cloud Atlas August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Inception](https://attack.mitre.org/groups/G0100) has encrypted malware payloads dropped on victim machines with AES and RC4 encryption.(Citation: Kaspersky Cloud Atlas December 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [Inception](https://attack.mitre.org/groups/G0100) has used a reconnaissance module to identify active processes and other associated loaded modules.(Citation: Symantec Inception Framework March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Inception](https://attack.mitre.org/groups/G0100) has used PowerShell to execute malicious commands and payloads.(Citation: Unit 42 Inception November 2018)(Citation: Kaspersky Cloud Atlas December 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [Inception](https://attack.mitre.org/groups/G0100) has used VBScript to execute malicious commands and payloads.(Citation: Unit 42 Inception November 2018)(Citation: Kaspersky Cloud Atlas December 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.002 | Domain Groups | [Inception](https://attack.mitre.org/groups/G0100) has used specific malware modules to gather domain membership.(Citation: Symantec Inception Framework March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Inception](https://attack.mitre.org/groups/G0100) has used HTTP, HTTPS, and WebDav in network communications.(Citation: Kaspersky Cloud Atlas December 2014)(Citation: Unit 42 Inception November 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Inception](https://attack.mitre.org/groups/G0100) has used a reconnaissance module to gather information about the operating system and hardware on the infected host.(Citation: Symantec Inception Framework March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Inception](https://attack.mitre.org/groups/G0100) used a file listing plugin to collect information about file and directories both on local and remote drives.(Citation: Symantec Inception Framework March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.003 | Multi-hop Proxy | [Inception](https://attack.mitre.org/groups/G0100) used chains of compromised routers to proxy C2 communications between them and cloud service providers.(Citation: Symantec Inception Framework March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | [Inception](https://attack.mitre.org/groups/G0100) has incorporated at least five different cloud service providers into their C2 infrastructure including CloudMe.(Citation: Kaspersky Cloud Atlas December 2014)(Citation: Symantec Inception Framework March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [Inception](https://attack.mitre.org/groups/G0100) has exploited CVE-2012-0158, CVE-2014-1761, CVE-2017-11882 and CVE-2018-0802 for execution.(Citation: Kaspersky Cloud Atlas August 2019)(Citation: Kaspersky Cloud Atlas December 2014)(Citation: Symantec Inception Framework March 2018)(Citation: Unit 42 Inception November 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Inception](https://attack.mitre.org/groups/G0100) lured victims into clicking malicious files for machine reconnaissance and to execute malware.(Citation: Kaspersky Cloud Atlas December 2014)(Citation: Kaspersky Cloud Atlas August 2019)(Citation: Symantec Inception Framework March 2018)(Citation: Unit 42 Inception November 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | [Inception](https://attack.mitre.org/groups/G0100) has used malicious HTA files to drop and execute malware.(Citation: Kaspersky Cloud Atlas August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.010 | Regsvr32 | [Inception](https://attack.mitre.org/groups/G0100) has ensured persistence at system boot by setting the value <code>regsvr32 %path%\ctfmonrn.dll /s</code>.(Citation: Kaspersky Cloud Atlas December 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1221 | Template Injection | [Inception](https://attack.mitre.org/groups/G0100) has used decoy documents to load malicious remote payloads via HTTP.(Citation: Unit 42 Inception November 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518 | Software Discovery | [Inception](https://attack.mitre.org/groups/G0100) has enumerated installed software on compromised systems.(Citation: Symantec Inception Framework March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Inception](https://attack.mitre.org/groups/G0100) has maintained persistence by modifying Registry run key value <br> <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\</code>.(Citation: Kaspersky Cloud Atlas December 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [Inception](https://attack.mitre.org/groups/G0100) used a browser plugin to steal passwords and sessions from Internet Explorer, Chrome, Opera, Firefox, Torch, and Yandex.(Citation: Symantec Inception Framework March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Inception](https://attack.mitre.org/groups/G0100) has used weaponized documents attached to spearphishing emails for reconnaissance and initial compromise.(Citation: Kaspersky Cloud Atlas December 2014)(Citation: Symantec Inception Framework March 2018)(Citation: Unit 42 Inception November 2018)(Citation: Kaspersky Cloud Atlas August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | [Inception](https://attack.mitre.org/groups/G0100) has encrypted network communications with AES.(Citation: Kaspersky Cloud Atlas December 2014) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Inception](https://attack.mitre.org/groups/G0100) has obtained and used open-source tools such as [LaZagne](https://attack.mitre.org/software/S0349).(Citation: Kaspersky Cloud Atlas August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 69件（`artifacts.csv`）

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
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--inception--f1cfea69304ea1b6 | inception |  | 不明 | actor_profile/evidence/inception.csv | structured-data | TLP:CLEAR | 中 |
| source--inception--70f51bafa5a1cabb | hunting cobaltstrike beacons in the dark |  | 不明 | APT-hunting/hunting-cobaltstrike-beacons-in-the-dark.pdf | report | TLP:CLEAR | 中 |
| source--inception--5e52347f5ce0893a | eset sednit part1 |  | 不明 | APT28/history-report-pdf/eset-sednit-part1.pdf | report | TLP:CLEAR | 中 |
| source--inception--b5a1d59d283bf876 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--inception--6fb226834cf8d6e3 | Report Notes of Cyber inspector |  | 不明 | Anonymous/RussiaUkrainewar/Report_Notes_of_Cyber_inspector_.pdf | report | TLP:CLEAR | 中 |
| source--inception--93001a40d9ca5e16 | cyberespionage gamaredon way |  | 不明 | Gamaredon/cyberespionage-gamaredon-way.pdf | report | TLP:CLEAR | 中 |
| source--inception--52ebc507b55028b9 | ACT1072452023ENGLISH |  | 不明 | Intellexa/Predator Files/ACT1072452023ENGLISH.pdf | report | TLP:CLEAR | 中 |
| source--inception--43dde95e67a38a5e | national cyber threat assessment 2025 2026 e |  | 不明 | International Strategic/Canada/national-cyber-threat-assessment-2025-2026-e.pdf | report | TLP:CLEAR | 中 |
| source--inception--b36148c25d898e41 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--inception--87144c6f17587dcd | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--inception--c25afd32373c27ef | 2022 INTERNET CRIME REPORT |  | 2022 | cybercrime/2023/2022 INTERNET CRIME REPORT.pdf | report | TLP:CLEAR | 中 |
| source--inception--b0adfa5e32c0b743 | Stairwell threat report The ink stained trail of GOLDBACKDOOR |  | 不明 | group123/Stairwell-threat-report-The-ink-stained-trail-of-GOLDBACKDOOR.pdf | report | TLP:CLEAR | 中 |
| source--inception--5218a4a3eb41bce0 | 20250507 TLP CLEAR NP SGDSN VIGINUM Technical report Storm 1516 |  | 2025-05-07 | information_operations/2025/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Technical report_Storm-1516.pdf | report | TLP:CLEAR | 中 |
| source--inception--a0ef8cb3860e6489 | RagaSerpent SideWinder Adjacent Tax Audit Cluster MultiCountry Targeted Chain |  | 不明 | sidewinder/RagaSerpent SideWinder-Adjacent Tax Audit Cluster MultiCountry Targeted Chain.pdf | report | TLP:CLEAR | 中 |
| source--inception--974bc284efbf1d4b | ESET Threat Report Q22020 |  | 不明 | summary/2020/ESET_Threat_Report_Q22020.pdf | report | TLP:CLEAR | 中 |
| source--inception--6fe0d186cf6867a7 | 2021 Threat Detection Report |  | 2021 | summary/2021/2021-Threat-Detection-Report.pdf | report | TLP:CLEAR | 中 |
| source--inception--23e37be662997391 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--inception--a5341843b0593b8f | ACD6 full report |  | 不明 | summary/2023/ACD6-full-report.pdf | report | TLP:CLEAR | 中 |
| source--inception--5a42b5ae6e675dfd | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--inception--796c9955489ab951 | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--inception--7359b2b3030c01a0 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--inception--4611805fad19b5b3 | kaspersky ics cert apt attacks on industrial organizations in h2 2022 en |  | 2022 | summary/2023/kaspersky-ics-cert-apt-attacks-on-industrial-organizations-in-h2-2022-en.pdf | report | TLP:CLEAR | 中 |
| source--inception--20796ce33526d9cb | positive research 2023 eng |  | 2023 | summary/2023/positive-research-2023-eng.pdf | report | TLP:CLEAR | 中 |
| source--inception--447207206a144096 | GRIT Ransomware Annual Report 2023 |  | 2023 | summary/2024/GRIT_Ransomware_Annual_Report_2023.pdf | report | TLP:CLEAR | 中 |
| source--inception--7f612d71e40a5558 | Recordedfuture 2023 Annual Report ta 2024 0321 |  | 2023 | summary/2024/Recordedfuture 2023 Annual Report ta-2024-0321.pdf | report | TLP:CLEAR | 中 |
| source--inception--7758458d1af794d8 | eset threat report h22024 |  | 不明 | summary/2024/eset-threat-report-h22024.pdf | report | TLP:CLEAR | 中 |
| source--inception--79bb0068646f38fa | 2024 Malicious Infrastructure Report |  | 2024 | summary/2025/2024 Malicious Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--inception--0f06772ae8aede50 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--inception--caa4c89d3d6eae22 | 2025 Cost of Insider Risks Global Report by Ponemon and DTEX |  | 2025 | summary/2025/2025_Cost_of_Insider_Risks_Global_Report_by_Ponemon_and_DTEX.pdf | report | TLP:CLEAR | 中 |
| source--inception--67bb7e636abb43a9 | Futuriom AI Clouds GPU Clouds |  | 不明 | summary/2025/Futuriom-AI-Clouds-GPU-Clouds.pdf | report | TLP:CLEAR | 中 |
| source--inception--1baaa268fd002a51 | NCSC Cyber Threat Report 2024 FINAL |  | 2024 | summary/2025/NCSC-Cyber-Threat-Report-2024-FINAL.pdf | report | TLP:CLEAR | 中 |
| source--inception--c0af277287ced945 | Security Navigator 2026 |  | 2026 | summary/2025/Security_Navigator_2026.pdf | report | TLP:CLEAR | 中 |
| source--inception--128a66053fcad29e | DFIR otchet za polnyy 2025 final |  | 2025 | summary/2026/DFIR_otchet_za_polnyy_2025_final.pdf | report | TLP:CLEAR | 中 |
| source--inception--1e751d28b9621976 | 004 |  | 不明 | summary/UNREDACTEDMagazine/004.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
