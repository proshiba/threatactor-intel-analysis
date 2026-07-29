# BackdoorDiplomacy 脅威アクタープロファイル

- プロファイルID: `actor--backdoordiplomacy`
- 状態: draft
- 更新日時: 2026-07-29T23:11:59Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

BackdoorDiplomacyの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **BackdoorDiplomacy**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| CloudComputating | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Quarian | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Ke3chang | overlaps-with | 共有alias: BackdoorDiplomacy | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) is a cyber espionage threat group that has been active since at least 2017. [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has targeted Ministries of Foreign Affairs and telecommunication companies in Africa, Europe, the Middle East, and Asia.(Citation: ESET BackdoorDiplomacy Jun 2021) |
| Capability | Turian, China Chopper, Quarian, Follina, Mimikatz, NBTscan, QuasarRAT |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Ke3chang, Vixen Panda, APT 15, GREF, Playful Dragon | canonical-name | 高 | China | https://github.com/nccgroup/Royal_APT<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Ke3chang%2C+Vixen+Panda%2C+APT+15%2C+GREF%2C+Playful+Dragon&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | BackdoorDiplomacy | canonical-name | 高 |  | https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | BackdoorDiplomacy - G0135 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0135<br>https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/ |
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
| malware--turian | Turian | [Turian](https://attack.mitre.org/software/S0647) is a backdoor that has been used by [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) to target Ministries of Foreign Affairs, telecommunication companies, and charities in Africa, Europe, the Middle East, and Asia. First reported in 2021, [Turian](https://attack.mitre.org/software/S0647) is likely related to Quarian, an older backdoor that was last observed being used in 2013 against diplomatic targets in Syria and the United States.(Citation: ESET BackdoorDiplomacy Jun 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--china-chopper | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.(Citation: Lee 2013) It has been used by several threat groups.(Citation: Dell TG-3390)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Rapid7 HAFNIUM Mar 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--quarian | Quarian | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--follina | Follina | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nbtscan | NBTscan | [NBTscan](https://attack.mitre.org/software/S0590) is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)(Citation: Symantec Waterbug Jun 2019)(Citation: FireEye APT39 Jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--quasarrat | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) is an open-source, remote access tool that has been publicly available on GitHub since at least 2014. [QuasarRAT](https://attack.mitre.org/software/S0262) is developed in the C# language.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

活動履歴なし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アルゼンチン | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてアルゼンチンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アルバニア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてアルバニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イタリア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてイタリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イラン | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてイランが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | インド | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インドネシア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウズベキスタン | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてウズベキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | エクアドル | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてエクアドルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エジプト | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてエジプトが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エルサルバドル | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてエルサルバドルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カザフスタン | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてカザフスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カタール | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてカタールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ガーナ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてガーナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | クウェート | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてクウェートが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | クロアチア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてクロアチアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | グアテマラ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてグアテマラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | コロンビア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてコロンビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | サウジアラビア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてサウジアラビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | シリア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてシリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ジャマイカ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてジャマイカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ジョージア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてジョージアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | スイス | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてスイスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スリランカ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてスリランカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | スロバキア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてスロバキアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スーダン | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてスーダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | チェコ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてチェコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チリ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてチリが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トリニダード・トバゴ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてトリニダード・トバゴが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドミニカ共和国 | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてドミニカ共和国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ナイジェリア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてナイジェリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ナミビア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてナミビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ハンガリー | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてハンガリーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | バルバドス | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてバルバドスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パナマ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてパナマが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブルガリア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてブルガリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブータン | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてブータンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベネズエラ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてベネズエラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ペルー | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてペルーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ホンジュラス | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてホンジュラスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ボスニア・ヘルツェゴビナ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてボスニア・ヘルツェゴビナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポルトガル | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてポルトガルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | マリ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてマリが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | メキシコ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてメキシコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モンテネグロ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてモンテネグロが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | リビア | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国としてリビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 中国 | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 南アフリカ | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国として南アフリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 構造化OSINTの被害国フィールドでBackdoorDiplomacyの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | アフリカ | MITRE ATT&CKのGroup概要でBackdoorDiplomacyの標的範囲としてアフリカが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 中南米 | アルゼンチン、エクアドル、エルサルバドル、グアテマラ、コロンビア、ジャマイカ、チリ、トリニダード・トバゴ、ドミニカ共和国、バルバドス、パナマ、ブラジル、ベネズエラ、ペルー、ホンジュラス、メキシコで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中央アジア | ウズベキスタン、カザフスタンで確認された標的・被害事例を中央アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 中東 | アラブ首長国連邦、イラン、カタール、クウェート、サウジアラビア、シリア、トルコで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 北アフリカ | エジプト、リビアで確認された標的・被害事例を北アフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 北米 | メキシコ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南アジア | アフガニスタン、インド、スリランカ、パキスタン、ブータンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南欧 | アルバニア、イタリア、クロアチア、ボスニア・ヘルツェゴビナ、ポルトガル、モンテネグロで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南米 | アルゼンチン、エクアドル、コロンビア、チリ、ブラジル、ベネズエラ、ペルーで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | インドネシア、マレーシアで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | スロバキア、チェコ、ハンガリー、ブルガリア、ポーランドで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | MITRE ATT&CKのGroup概要でBackdoorDiplomacyの標的範囲として欧州が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 政府・行政 | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has targeted Ministries of Foreign Affairs and telecommunication companies in Africa, Europe, the Middle East, and Asia.(Citation: ESET BackdoorDiplomacy Jun 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 情報通信 | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has targeted Ministries of Foreign Affairs and telecommunication companies in Africa, Europe, the Middle East, and Asia.(Citation: ESET BackdoorDiplomacy Jun 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027 | Obfuscated Files or Information | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has obfuscated tools and malware it uses with VMProtect.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has disguised their backdoor droppers with naming conventions designed to blend into normal operations.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has dropped implants in folders named for legitimate software.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used SMBTouch, a vulnerability scanner, to determine whether a target is vulnerable to EternalBlue malware.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used NetCat and PortQry  to enumerate network connections and display the status of related TCP and UDP ports.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has dropped legitimate software onto a compromised host and used it to execute malicious DLLs.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has copied files of interest to the main drive's recycle bin.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1095 | Non-Application Layer Protocol | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used EarthWorm for network tunneling with a SOCKS5 server and port transfer functionalities.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has downloaded additional files and tools onto a compromised host.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1120 | Peripheral Device Discovery | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used an executable to detect removable media, such as USB flash drives.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has exploited CVE-2020-5902, an F5 BIP-IP vulnerability, to drop a Linux backdoor. [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has also exploited mis-configured Plesk servers.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has used web shells to establish an initial foothold and for lateral movement within a victim's system.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has executed DLL search order hijacking.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has obtained and used leaked malware, including DoublePulsar, EternalBlue, EternalRocks, and EternalSynergy, in its operations.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has obtained a variety of open-source reconnaissance and red team tools for discovery and lateral movement.(Citation: ESET BackdoorDiplomacy Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 30件（`artifacts.csv`）

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
| source--backdoordiplomacy--f46ed235e8b395b4 | backdoordiplomacy |  | 不明 | actor_profile/evidence/backdoordiplomacy.csv | structured-data | TLP:CLEAR | 中 |
| source--backdoordiplomacy--3c6d0cb63e45f121 | Charting China’s Climb as a Leading Global Cyber Power |  | 不明 | International Strategic/China/Charting China’s Climb as a Leading Global Cyber Power.pdf | report | TLP:CLEAR | 中 |
| source--backdoordiplomacy--a82b9f9edbe1bb43 | Raport analize Teknikat Taktikat Procedurat per sulmuesit Iraniane |  | 不明 | International Strategic/Iran/Raport-analize-Teknikat-Taktikat-Procedurat-per-sulmuesit-Iraniane.pdf | report | TLP:CLEAR | 中 |
| source--backdoordiplomacy--927ab894b471ae9e | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--backdoordiplomacy--a9bf283a4e78a9a1 | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--backdoordiplomacy--3dc321536399d35c | eset apt activity report q42022 q12023 |  | 不明 | summary/2023/eset_apt_activity_report_q42022_q12023.pdf | report | TLP:CLEAR | 中 |
| source--backdoordiplomacy--32a778357ba98fd6 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--backdoordiplomacy--404cfa7b84ab5a5f | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--backdoordiplomacy--692c95c243473867 | 2024 Malicious Infrastructure Report |  | 2024 | summary/2025/2024 Malicious Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--backdoordiplomacy--60438de54dfa19a5 | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
