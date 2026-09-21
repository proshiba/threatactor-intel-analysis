# DarkVishnya 脅威アクタープロファイル

- プロファイルID: `actor--darkvishnya`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

DarkVishnyaの標準化プロファイル。リポジトリ内の専用資料0件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **DarkVishnya**
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

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial-gain | Financially motivated intrusion or fraud. | 高 | `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description. |

## 他アクターとの関係

確認された関係なし

## 関連する企業・個人

関連エンティティなし

### エンティティ関係

確認された関係なし

### 法的措置

確認された法的措置なし

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
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | DarkVishnya | canonical-name | 高 |  | https://www.bleepingcomputer.com/news/security/netbooks-rpis-and-bash-bunny-gear-attacking-banks-from-the-inside/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | DarkVishnya - G0105 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0105<br>https://securelist.com/darkvishnya/89169/ |
| misp-mitre-intrusion-set | DarkVishnya - G0105 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0105<br>https://securelist.com/darkvishnya/89169/ |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | DarkVishnya | canonical-name | 高 |  |  |

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
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--winexe | Winexe | [Winexe](https://attack.mitre.org/software/S0191) is a lightweight, open source tool similar to [PsExec](https://attack.mitre.org/software/S0029) designed to allow system administrators to execute commands on remote servers. (Citation: Winexe Github Sept 2013) [Winexe](https://attack.mitre.org/software/S0191) is unique in that it is a GNU/Linux based client. (Citation: Überwachung APT28 Forfiles June 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 東欧 | MITRE ATT&CKのGroup概要でDarkVishnyaの標的範囲として東欧が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| sectors | 金融 | [DarkVishnya](https://attack.mitre.org/groups/G0105) is a financially motivated threat actor targeting financial institutions in Eastern Europe. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access, Discovery | T1040 | Network Sniffing | [DarkVishnya](https://attack.mitre.org/groups/G0105) used network sniffing to obtain login data. (Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1046 | Network Service Discovery | [DarkVishnya](https://attack.mitre.org/groups/G0105) performed port scanning to obtain the list of active services.(Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.001 | PowerShell | [DarkVishnya](https://attack.mitre.org/groups/G0105) used PowerShell to create shellcode loaders.(Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1110 | Brute Force | [DarkVishnya](https://attack.mitre.org/groups/G0105) used brute-force attack to obtain login data.(Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1135 | Network Share Discovery | [DarkVishnya](https://attack.mitre.org/groups/G0105) scanned the network for public shared folders.(Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1200 | Hardware Additions | [DarkVishnya](https://attack.mitre.org/groups/G0105) physically connected Bash Bunny, Raspberry Pi, netbooks, and inexpensive laptops to the target organization's environment to access the company’s local network.(Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1219 | Remote Access Tools | [DarkVishnya](https://attack.mitre.org/groups/G0105) used DameWare Mini Remote Control for lateral movement.(Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [DarkVishnya](https://attack.mitre.org/groups/G0105) created new services for shellcode loaders distribution.(Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1571 | Non-Standard Port | [DarkVishnya](https://attack.mitre.org/groups/G0105) used ports 5190 and 7900 for shellcode listeners, and 4444, 4445, 31337 for shellcode C2.(Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.002 | Tool | [DarkVishnya](https://attack.mitre.org/groups/G0105) has obtained and used tools such as [Impacket](https://attack.mitre.org/software/S0357), [Winexe](https://attack.mitre.org/software/S0191), and [PsExec](https://attack.mitre.org/software/S0029).(Citation: Securelist DarkVishnya Dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

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
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
