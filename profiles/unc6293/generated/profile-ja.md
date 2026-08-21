# UNC6293 脅威アクタープロファイル

- プロファイルID: `actor--unc6293`
- 状態: draft
- 更新日時: 2026-08-21T01:45:24Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC6293はGTIGが追跡するロシア関連の脅威クラスタで、米国務省職員を装ったapp passwordフィッシングとOAuthフィッシングにより、ロシアに批判的な著名個人のアカウントを侵害する初期アクセス活動を行う。GTIGはmoderate confidenceでICE RELIC(旧APT29)のサブクラスタと評価している。

## アクター名とAlias

- 正規名: **UNC6293**
- 初回観測: 2025-06
- 最終観測: 2026-06
- 活動状態: yes

Aliasなし

## 帰属

GTIGは「GTIG assesses with high confidence that these three threat clusters - UNC6293, UNC7005, and UNC5976 - possess a Russian nexus, based on high-level targeting patterns, phishing themes, and shared operational techniques」と、UNC6293を含む3クラスタのロシア関連性をhigh confidenceで評価している。一方で個別のロシア情報機関への帰属は行っておらず、UNC6293とICE RELIC(旧APT29)の関係は「moderate confidence」にとどまる。GTIG自身の表現も「suspected Russian cyber espionage threat clusters」である。本プロファイルでは国レベルの帰属をロシアとして採用し、スポンサー種別と具体的な機関帰属は確定していないものとして扱う。

- 国: Russia
- スポンサー種別: state
- 確度: 中
- 証拠: `source--gtig-going-with-the-flows-2026`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | GTIGはUNC6293を「suspected Russian cyber espionage」クラスタの一つとして扱い、ロシアにとって関心の対象となる個人のアカウント侵害を目的とする初期アクセス活動と説明している。 | 中 | `source--gtig-going-with-the-flows-2026` | 一次資料の明示記述に基づく。金銭目的の記述は原文にない。 |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| actor--apt29 | part-of | GTIGは「We assess with moderate confidence that UNC6293 is a sub cluster of ICE RELIC (formerly APT29) responsible for initial access operations」と述べ、UNC6293をICE RELIC(旧APT29)の初期アクセス担当サブクラスタと評価している。また「several high-level TTPs used by UNC6293 and UNC7005 harken back to older, attributed ICE RELIC phishing operations between 2021 and 2024」として、標的業種(学術、NGO、外交、防衛)と地域の重なり、外交行事の招待やワインに関する特定の題材の再利用を根拠に挙げている。 | 中 | `source--gtig-going-with-the-flows-2026` |
| actor--unc7005 | shares-targeting-with | GTIGはUNC7005について「Although this group shares many high-level similarities with UNC6293, including targeting overlaps, we are tracking it separately due to its lower sophistication and poor operational security, infrastructure with divergent characteristics, and incorporation of malware」と述べ、標的の重なりを認めつつ別クラスタとして追跡している。2026年5月下旬のUNC7005の作戦で使われた攻撃者メールアドレスは、2025年6月のUNC6293の作戦で使われたものとほぼ同一であった。 | 中 | `source--gtig-going-with-the-flows-2026` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | UNC6293。GTIGがmoderate confidenceでICE RELIC(旧APT29)の初期アクセス担当サブクラスタと評価するロシア関連の脅威クラスタ。 |
| Capability | 固有マルウェアの記載はない。app passwordフィッシングによる2要素認証回避と、正規OAuth認証フローを悪用した検証コード／URLの窃取を主な能力とする。囮は画面写真を含むPDF文書。 |
| Infrastructure | 米国務省を装う認証フォームやOAuthフィッシングページを設置した攻撃者管理ドメイン(dosportal[.]app、foreignrelations[.]us)。GTIGは保有インフラの規模について「the volume of infrastructure that they use is still limited in comparison to other Russian espionage operations」と述べている。 |
| Victim | ロシアに批判的な著名個人。1回あたり5名未満の小規模な標的選定で、外交や今後の会議・会合を題材とする。 |
| Socio-political | GTIGはUNC6293を含む3クラスタについて「possess a Russian nexus」とhigh confidenceで評価し、ロシアにとって関心の対象となる個人を狙う諜報目的の活動と位置付けている。 |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UNC6293 | canonical-name | 高 | RU | https://cloud.google.com/blog/topics/threat-intelligence/creative-phishing-academics-critics-of-russia |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
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

未確認

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infra--unc6293-auth-phishing-domains | UNC6293の認証フィッシングドメイン | 米国務省を装う認証フォームやOAuthフィッシングページを設置した攻撃者管理ドメイン。GTIGのIOC表はdosportal[.]appとforeignrelations[.]usをUNC6293へ帰属し、いずれもPhishing domainと説明している。foreignrelations[.]usは2026年6月のOAuthフィッシングで「verification code」を要求するページとして図示されている。 | 不明 | 不明 | 高 | `source--gtig-going-with-the-flows-2026` |

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--unc6293-app-password-phishing | app passwordフィッシングによる2要素認証回避 | 標的に特定の名称のapp password(安全性の低いアプリや端末へアクセスを許可するパスコード)を設定させ、その値を窃取することで2要素認証を経ずにアカウントへアクセスする。設定手順は画面写真を含むPDF囮文書で提示される。 | 2025-06 | 2025-10 | 高 | `source--gtig-going-with-the-flows-2026` |
| opcap--unc6293-oauth-phishing | 正規OAuth認証フローを悪用したトークン窃取 | 標的に外部プロバイダーでの正規ログインを行わせたうえで、完全なURLまたは「verification code」の共有を求め、提供された値を用いてアカウントへのアクセス権を得る。 | 2026-06 | 2026-06 | 高 | `source--gtig-going-with-the-flows-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UNC6293による国務省を装ったapp passwordフィッシング | phishing-campaign | 2025-06 | 2025-10 | 2026-08-20 |  |  |  |  | GTIGは、UNC6293が国務省の職員を装い、標的にapp passwordを設定させて2要素認証を回避するフィッシングを継続していると報告した。2025年6月に確認された初期の活動では、ms.state.govという名称のapp passwordを設定させる手順を画面写真付きのPDF囮文書で提示し、設定した値をメールで返信させていた。2025年10月にGTIGが確認した活動では、同じ画面写真とms.state.govの記載を含むPDF囮文書が使われた一方、app passwordの送信先はメールではなく正規に見えるサイト上の認証フォームへ変更されていた。標的は当該国の体制に批判的な立場をとる著名個人で、1回あたりの標的は5名未満と小規模である。囮に用いられるアプリケーション名と主題は外交、および今後の会議や会合に偏る。 | 高 | `source--gtig-going-with-the-flows-2026` |
| UNC6293によるOAuthフィッシングへの手口拡張 | phishing-campaign | 2026-06 | 2026-06 | 2026-08-20 |  |  |  |  | 2026年6月、GTIGはUNC6293が国務省を装う手口を維持したまま、OAuthフィッシングを取り入れたことを確認した。標的が外部プロバイダーで正規のログインを行った後、完全なURLまたは「verification code」を共有するよう求め、提供された検証コードによって攻撃者が当該アカウントへのアクセス権を得る。GTIGは検証コードを要求するフィッシングページをforeignrelations[.]us上で確認している。 | 高 | `source--gtig-going-with-the-flows-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| UNC6293による国務省を装ったapp passwordフィッシング | UNC6293 | 情報なし | 情報なし | UNC6293の認証フィッシングドメイン | 情報なし | 情報なし | 高 |
| UNC6293によるOAuthフィッシングへの手口拡張 | UNC6293 | 情報なし | 情報なし | UNC6293の認証フィッシングドメイン | 情報なし | 情報なし | 高 |

2025年6月にapp passwordフィッシングキャンペーンとして初めて報告され(Citizen Labも同時期に報告)、2025年10月には同一の画面写真を含むPDF囮文書を再利用しつつ、app passwordの送信先をメールから認証フォームへ変更した。2025年12月にはVolexityが外交を題材とする囮を報告している。2026年6月にはOAuthフィッシングを取り入れた。

## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 3件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| UNC6293はICE RELIC(旧APT29)の初期アクセス担当サブクラスタである可能性が高いが、確定はしていない。 | 中 | `source--gtig-going-with-the-flows-2026` | GTIGのmoderate confidence評価をそのまま反映する。APT29プロファイルへの統合は行わない。 |
| UNC6293の手口はapp passwordフィッシングからOAuthフィッシングへ拡張しており、いずれも正規の認証フローの悪用という点で一貫している。 | 高 | `source--gtig-going-with-the-flows-2026` | 2025年6月から2026年6月までのGTIGの直接観測に基づく。 |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.
- GTIG原文は被害組織名を明記していないため、victim_casesを構造化できていない。
- GTIGのIOC表はdosportal[.]appを特定の作戦へ結び付けていないため、当該ドメインのcampaign_refsは空のままである。
- GTIG原文はUNC6293の被害国・被害業種を名指ししていないため、構造化した標的国・地域・業種は存在しない。記事冒頭の「academia, aerospace and defense, governments and think tanks across Europe, as well as academia and think tanks within the United States」は3クラスタ合算の記述であり、UNC6293単独の標的として転記していない。

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- ICE RELICはGTIGによるAPT29の新呼称である。同一記事内で「formerly APT29」と明示されているが、GTIG以外のベンダーがこの呼称を採用しているかは未確認である。
- UNC6293とUNC7005は標的が重なり、2026年5月のUNC7005作戦では2025年6月のUNC6293作戦とほぼ同一の攻撃者メールアドレスが使われている。GTIGは両者を別クラスタとして追跡しており、本プロファイルもそれに従う。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--gtig-going-with-the-flows-2026 | Going with the Flow(s): Distinct Clusters Target Individuals of Interest to Russia | Google Threat Intelligence Group | 2026-08-20 | https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia | vendor-research | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc6293--4d037ea2f6e2e7ef | unc6293 |  | 不明 | actor_profile/evidence/unc6293.csv | structured-data | TLP:CLEAR | 中 |
| source--unc6293--85aadfc2c3065fd3 | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。 2026-08-21の日次チェックでGTIG「Going with the Flow(s)」(2026-08-20)を反映し、本プロファイルは初めて日付を持つ活動を得た。
