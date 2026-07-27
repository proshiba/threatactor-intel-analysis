# Gelsemium 脅威アクタープロファイル

- プロファイルID: `actor--gelsemium`
- 状態: draft
- 更新日時: 2026-07-27T11:04:32Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Gelsemiumの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Gelsemium**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Chimera | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Unknown row 37; mapping requires review. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Chimera | overlaps-with | 共有alias: Gelsemium, GELSEMIUM | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Gelsemium](https://attack.mitre.org/groups/G0141) is a cyberespionage group that has been active since at least 2014, targeting governmental institutions, electronics manufacturers, universities, and religious organizations in East Asia and the Middle East.(Citation: ESET Gelsemium June 2021) |
| Capability | OwlProxy, SessionManager |
| Infrastructure |  |
| Victim | Taiwan semiconductors |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Chimera | single-alias-intersection | 中 | China | https://cycraft.com/download/%5BTLP-White%5D20200415%20Chimera_V4.1.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Chimera&n=1 |
| etda-threat-group-cards | Gelsemium | canonical-name | 高 | China | https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf<br>https://www.venustech.com.cn/uploads/2018/08/231401512426.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Gelsemium&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Gelsemium | canonical-name | 高 |  | https://www.welivesecurity.com/2021/06/09/gelsemium-when-threat-actors-go-gardening/<br>https://www.venustech.com.cn/uploads/2018/08/231401512426.pdf<br>https://hitcon.org/2016/pacific/0composition/pdf/1202/1202%20R0%200930%20an%20intelligance-driven%20approach%20to%20cyber%20defense.pdf |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Chimera - G0114 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0114<br>https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf<br>https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/ |
| misp-mitre-intrusion-set | Gelsemium - G0141 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0141<br>https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf |
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
| malware--owlproxy | OwlProxy | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sessionmanager | SessionManager | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| 中国のGelsemiumハッカー、Linux向け新マルウェア「WolfsBane」を使用 | malware-campaign | 不明 | 不明 | 2024-11-22 | 中国のサイバー攻撃グループGelsemiumが、新たなLinuxバックドア「WolfsBane」を使用。 WolfsBaneは、ドロッパー、ランチャー、バックドアから成る完全なマルウェアツール。 改変されたオープンソースのルートキットを用いて検出を回避。 マルウェアは、「.config/autostart/」に自動起動ファイル（gnome-control.desktop）を作成することで、ホストへの永続性を設定。 Windows向けマルウェア「Project Wood」と関連するLinuxマルウェア「FireWood」も発見。 APTグループがLinuxプラットフォームへの攻撃を強化する傾向が増加。 | 高 | `source--daily-c14d3c6623afcdc68bdf` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Taiwan | Targeting text mentions taiwan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 13件
- IOC観測: 14件
- 複数攻撃で観測: 0件
- 要レビュー候補: 13件
- 非IOC artifact観測: 16件（`artifacts.csv`）

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
| source--daily-c14d3c6623afcdc68bdf | 中国のGelsemiumハッカー、Linux向け新マルウェア「WolfsBane」を使用 | bleepingcomputer.com | 2024-11-22 | https://www.bleepingcomputer.com/news/security/chinese-gelsemium-hackers-use-new-wolfsbane-linux-malware/ | osint-report | TLP:CLEAR | 中 |
| source--gelsemium--0c692ac1ecc96ddf | gelsemium |  | 不明 | actor_profile/evidence/gelsemium.csv | structured-data | TLP:CLEAR | 中 |
| source--gelsemium--1d6473610154e76d | readme |  | 不明 | summary/2024/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--gelsemium--6296bb3203efe3c9 | eset threat report h22024 |  | 不明 | summary/2024/eset-threat-report-h22024.pdf | report | TLP:CLEAR | 中 |
| source--gelsemium--acdf8b3cf5b320da | TLP CLEAR CERT EU TLR 2024 v1 |  | 2024 | summary/2025/TLP-CLEAR-CERT-EU-TLR-2024-v1.pdf | report | TLP:CLEAR | 中 |
| source--gelsemium--bf1cde8e50ddfbef | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--gelsemium--e7fd88916ed46e9b | eset apt activity report q4 2023 q1 2024 |  | 2023 | summary/2024/eset-apt-activity-report-q4-2023-q1-2024.pdf | report | TLP:CLEAR | 中 |
| source--gelsemium--f0b7738950da3acb | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
