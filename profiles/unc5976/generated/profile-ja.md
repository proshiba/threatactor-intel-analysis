# UNC5976 脅威アクタープロファイル

- プロファイルID: `actor--unc5976`
- 状態: draft
- 更新日時: 2026-08-21T01:45:24Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC5976はGTIGが2026年3月から追跡する、認証に重点を置くロシア関連の諜報クラスタである。ファイル共有を装うドメインとクラウドプロジェクトを組み合わせたOAuthフィッシングで認証トークンを自動収集し、悪性Excelプラグイン HEADRUSH も用いる。GTIGはUNC6293・UNC7005とは別クラスタと評価している。

## アクター名とAlias

- 正規名: **UNC5976**
- 初回観測: 2026-03
- 最終観測: 2026-04
- 活動状態: yes

Aliasなし

## 帰属

GTIGは「GTIG assesses with high confidence that these three threat clusters - UNC6293, UNC7005, and UNC5976 - possess a Russian nexus, based on high-level targeting patterns, phishing themes, and shared operational techniques」とhigh confidenceでロシア関連性を評価している。UNC5976については「a suspected Russian cyber espionage cluster with an authentication focus」と記述し、ICE RELIC系の2クラスタとは区別したうえで「potentially reflecting differing strategic mandates and potential alignment with alternative Russian intelligence services」と述べるにとどまり、具体的な機関への帰属は行っていない。

- 国: Russia
- スポンサー種別: state
- 確度: 中
- 証拠: `source--gtig-going-with-the-flows-2026`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | GTIGはUNC5976を「a suspected Russian cyber espionage cluster with an authentication focus」と説明し、認証トークンの窃取によるアカウント侵害を目的とする活動と位置付けている。 | 中 | `source--gtig-going-with-the-flows-2026` | 一次資料の明示記述に基づく。金銭目的の記述は原文にない。 |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| actor--unc7005 | related-to | GTIGはUNC5976について「We believe this cluster to be distinct from UNC6293 and UNC7005」「UNC5976 remains distinct from the UNC6293 and UNC7005 clusters, potentially reflecting differing strategic mandates and potential alignment with alternative Russian intelligence services」と明示的に別クラスタとしている。相違点として、事後侵害活動に住宅用プロキシーではなく専用インフラを用いること、およびICE RELIC関連クラスタよりマルウェアとツールの利用が顕著であることを挙げている。共通点は、ロシア関連性と認証フロー悪用への注力である。 | 中 | `source--gtig-going-with-the-flows-2026` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | UNC5976。GTIGが2026年3月から追跡する、認証に重点を置くロシア関連の諜報クラスタ。UNC6293およびUNC7005とは別クラスタとされ、異なるロシア情報機関との整合の可能性が指摘されている。 |
| Capability | 偽ファイル共有ページとクラウドプロジェクトを組み合わせたOAuthトークン収集の自動化。悪性Excelプラグイン HEADRUSH からHTAダウンローダーへ至る感染連鎖。事後侵害活動には住宅用プロキシーではなく専用インフラを用いる。 |
| Infrastructure | ファイル共有を思わせる名称の購入ドメインと、対応する攻撃者管理のクラウドプロジェクト。無効化後およそ3か月で少なくとも12件の新規ドメインを再構築しており、Google以外の事業者への移行が進んでいると評価されている。 |
| Victim | 軍、航空宇宙、防衛産業基盤、NGO・シンクタンク。地理的にはウクライナとアルメニアへの偏りが指摘される。HEADRUSHの配布ではウクライナの研究機関を装い、ウクライナの航空宇宙・画像関連企業が標的となった可能性がある。 |
| Socio-political | GTIGは3クラスタのロシア関連性をhigh confidenceで評価し、UNC5976については異なる戦略的任務と、別のロシア情報機関との整合の可能性を指摘している。 |

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--headrush | HEADRUSH | GTIGがHEADRUSHと命名した悪性のExcelプラグイン。2026年4月に確認された検体は最終的にHTML Application (HTA)ダウンローダーへ到達する。GTIGは当時、感染連鎖の全容を特定できなかったと述べている。 | 2026-04 | 2026-04 | 高 | `source--gtig-going-with-the-flows-2026` |

### ツール

未確認

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infra--unc5976-file-sharing-phishing-domains | ファイル共有を装うOAuthフィッシングドメインとクラウドプロジェクト | UNC5976はファイル共有を思わせる名称のドメインを購入し、対応するクラウドプロジェクトを作成する。ドメインは偽のファイル共有ページを提供し、数秒後にログインダイアログを表示する。標的が認証すると、認証トークンをURLから取得して保存する悪性スクリプトを設置したクラウドプロジェクトのURLへリダイレクトされる。GTIGによる初回の発見と無効化からおよそ3か月のうちに、少なくとも12件の新規ドメインと関連インフラが作成された。GTIGは、UNC5976がフィッシングインフラの一部をGoogle以外の事業者へ移行しつつあると評価している。 | 2026-03 | 不明 | 高 | `source--gtig-going-with-the-flows-2026` |

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--unc5976-oauth-token-harvesting | クラウド基盤を悪用したOAuthトークン収集の自動化 | 正規のOAuthログイン画面へ誘導したうえで、攻撃者が管理するクラウドプロジェクトへリダイレクトし、URLから認証トークンを取得して運用者が後から回収できるよう保存する。 | 2026-03 | 不明 | 高 | `source--gtig-going-with-the-flows-2026` |
| opcap--unc5976-dedicated-post-compromise-infrastructure | 事後侵害活動への専用インフラの使用 | GTIGは「UNC5976 uses dedicated infrastructure for post-compromise activity rather than residential proxies」と述べ、ICE RELIC関連クラスタとの運用上の相違点として挙げている。 | 不明 | 不明 | 中 | `source--gtig-going-with-the-flows-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UNC5976によるHEADRUSH Excelプラグインの配布 | malware-campaign | 2026-04 | 2026-04 | 2026-08-20 | target--activity-rule--country--36f1b9323d5faab92f39 | malware--headrush |  | victim--activity-rule--64ea35238544ea80078e | 2026年4月、GTIGはUNC5976が悪性のExcelプラグインHEADRUSHを配布する事例を確認した。確認された検体は最終的にHTML Application (HTA)ダウンローダーへ到達する。配布には、ウクライナの研究機関を装うドメインが用いられた。GTIGは、ウクライナの航空宇宙・画像関連企業が標的となった可能性があるとし、当時は感染連鎖の全容を特定できなかったと述べている。 | 高 | `source--gtig-going-with-the-flows-2026` |
| UNC5976による偽ファイル共有ページを用いたOAuthトークン窃取 | phishing-campaign | 2026-03 | 不明 | 2026-08-20 |  |  |  | victim--activity-rule--afdf3cb80ab11953526e | GTIGは2026年3月からUNC5976のOAuth関連活動の追跡を開始した。UNC5976はファイル共有を思わせる名称のドメインを購入し、対応するクラウドプロジェクトを作成したうえで、偽のファイル共有ページを設置する。標的がページを数秒閲覧するとログインダイアログが表示され、「Continue with Google」を押すと正規のGoogle OAuthログイン画面へ誘導される。認証後は攻撃者が管理するクラウドプロジェクトのURLへリダイレクトされ、そこに設置された悪性スクリプトがURLから認証トークンを取得して運用者が後から回収できるよう保存する。GTIGによる初回の発見と無効化からおよそ3か月のうちに少なくとも12件の新規ドメインと関連インフラが作成され、GTIGはこれらのクラウドプロジェクトの無効化とフィッシング活動の妨害を行った。GTIGは現在、UNC5976がフィッシングインフラの一部をGoogle以外の事業者へ移行しつつあると評価している。 | 高 | `source--gtig-going-with-the-flows-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| UNC5976によるHEADRUSH Excelプラグインの配布 | UNC5976 | HEADRUSH | 情報なし | 情報なし | ウクライナ | 被害事例: UNC5976によるHEADRUSH Excelプラグインの配布 | 高 |
| UNC5976による偽ファイル共有ページを用いたOAuthトークン窃取 | UNC5976 | 情報なし | 情報なし | ファイル共有を装うOAuthフィッシングドメインとクラウドプロジェクト | 情報なし | 被害事例: UNC5976による偽ファイル共有ページを用いたOAuthトークン窃取 | 高 |

2026年3月にGTIGがOAuth関連活動の追跡を開始し、無効化後およそ3か月で少なくとも12件の新規ドメインが再構築された。2026年4月にはHEADRUSH検体の配布が確認された。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アルメニア | GTIGはUNC5976について「Much of the group's geographic targeting has centered on Ukraine and Armenia」と記述し、「Its operational focus is primarily centered on the military, aerospace, defense industrial base, and NGOs/think tanks」としている。 | 不明 | 不明 | 高 | `source--gtig-going-with-the-flows-2026` |
| countries | ウクライナ | GTIGはUNC5976について「Much of the group's geographic targeting has centered on Ukraine and Armenia」と記述し、「Its operational focus is primarily centered on the military, aerospace, defense industrial base, and NGOs/think tanks」としている。 | 2026-04 | 2026-04 | 高 | `source--gtig-going-with-the-flows-2026` |

選定ロジック: 標的国・地域・業種は、GTIG原文がUNC5976について明示した記述のみから収録する。3クラスタ合算の記述、帰属国、インフラ所在国は標的として扱わない。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: UNC5976によるHEADRUSH Excelプラグインの配布 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--36f1b9323d5faab92f39 | malware--headrush |  |  |  | 2026-04 | 2026-04 | 2026-08-20 | 高 | `source--gtig-going-with-the-flows-2026` |
| 被害事例: UNC5976による偽ファイル共有ページを用いたOAuthトークン窃取 | 非公開 | anonymous | unknown | reported |  |  |  | クラウド／SaaS | data-theft: UNC5976による偽ファイル共有ページを用いたOAuthトークン窃取<br>credential-theft: UNC5976による偽ファイル共有ページを用いたOAuthトークン窃取 | 2026-03 | 不明 | 2026-08-20 | 高 | `source--gtig-going-with-the-flows-2026` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 3件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| UNC5976はUNC6293およびUNC7005とは別クラスタであり、ICE RELIC(旧APT29)へは結び付けられていない。 | 中 | `source--gtig-going-with-the-flows-2026` | GTIGが明示的に区別している。将来の誤統合を防ぐため関係として記録した。 |
| UNC5976は無効化後も短期間でインフラを再構築する運用能力を持つ。 | 高 | `source--gtig-going-with-the-flows-2026` | GTIGによる初回の発見と無効化からおよそ3か月で少なくとも12件の新規ドメインが作成されたという直接観測に基づく。 |

### 情報ギャップ

- 原文は被害組織名を明記していないため、victim_casesを構造化できていない。
- GTIGは「a much heavier malware and tooling footprint」と述べるが、本資料で具体名が示されたマルウェアはHEADRUSHのみで、ツールの具体名は示されていない。
- 再構築された12件以上のドメインの個別値は原文に列挙されておらず、IOCとして収録できていない。

### 不確実性

- GTIGは「potential alignment with alternative Russian intelligence services」と可能性を述べるにとどまり、具体的な機関は特定していない。
- HEADRUSHの配布におけるウクライナの航空宇宙・画像関連企業への攻撃は「may have targeted」であり確定していない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--gtig-going-with-the-flows-2026 | Going with the Flow(s): Distinct Clusters Target Individuals of Interest to Russia | Google Threat Intelligence Group | 2026-08-20 | https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia | vendor-research | TLP:CLEAR | 高 |

## 自由記述

2026-08-21の日次チェックで、GTIG「Going with the Flow(s)」(2026-08-20)を唯一の一次資料として新規作成した。独立した一次資料が追加された時点でstatusの見直しを行う。
