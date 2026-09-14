# UNC5792 脅威アクタープロファイル

- プロファイルID: `actor--unc5792`
- 状態: draft
- 更新日時: 2026-09-10T22:21:37Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC5792はロシアを拠点とする脅威クラスタで、暗号化メッセージングアプリ利用者の通信内容取得を目的とする活動が観測されている。FBIとCISAの共同PSAは、Signalのサポート窓口を装って復旧キーを詐取し過去の会話を閲覧する手口を警告し、この活動がUNC5792およびUNC4221として公に追跡されていると述べる。GTIGは別途、AIモデルを組み込んだ自動ボットでTelegramチャンネルを解析し、ロシア当局の関心事項に沿う情報を構造化報告として出力させる試みを報告している。

## アクター名とAlias

- 正規名: **UNC5792**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: likely

Aliasなし

## 帰属

GTIGは2026-09-08の報告で本クラスタを「UNC5792—a Russia-based threat group」と記述する。FBI・CISAの共同PSA(2026-06-26)は、Signalの復旧キーを狙う当該フィッシング活動をロシア情報機関に関連するものとして警告し、「To date, this activity has been publicly tracked as UNC5792 and UNC4221.」と述べる。PSAは追跡名を付与した組織を明示していない。特定の政府機関への所属を確定する記述は、確認したいずれの資料にもない。

- 国: Russia
- スポンサー種別: state-aligned
- 確度: 中
- 証拠: `source--fbi-cisa-psa-signal-recovery-keys-2026`, `source--gtig-adversarial-ai-2026`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | 政府・軍関係者、政治家、ジャーナリスト、ウクライナの重要人物を対象に、暗号化メッセージングアプリ上の過去の会話内容を取得する。 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026` | FBI・CISA共同PSAの標的記述に基づく。個人標的型の収集活動であり、ロシアの情報要求と整合する。 |
| surveillance | ロシア当局が関心を持つ治安上の脅威や過激派コンテンツの観点から、Telegramチャンネルを継続的に監視・分類する。 | 中 | `source--gtig-adversarial-ai-2026` | GTIG 2026-09-08に基づく。侵入を伴わない公開チャンネルの監視であり、諜報とは分けて記録する。 |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| UNC4221 | taxonomy-overlaps-with | FBI・CISA共同PSA(2026-06-26)は、Signalのバックアップ復旧キーを狙う同一のフィッシング活動について「To date, this activity has been publicly tracked as UNC5792 and UNC4221.」と述べ、両方の指定子で追跡されているとする。 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## Capability

### マルウェア

未確認

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--unc5792-ai-monitoring-bot | AI連携Telegram監視ボット | Telegramチャンネルを監視する自動ボットへAIモデルを組み込んだもの。従来からTelegramボットによるチャンネル監視を行っていたが、APIキー連携の方法を調査し、メッセージを不審または中立に分類させ、構造化された報告形式で出力させる用途でAIを試用している。 | 不明 | 不明 | 中 | `source--gtig-adversarial-ai-2026` |

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
| AIを組み込んだ自動ボットによるTelegramチャンネル監視 | information-collection | 不明 | 不明 | 2026-09-08 |  |  |  |  | AIモデルを自動監視ボットへ統合し、ロシア当局が関心を持つ情報(治安上の脅威や過激派コンテンツなど)の観点からTelegramチャンネルを解析する活動。従来からTelegramボットによるチャンネル監視を行っていたが、APIキー連携の方法を調べ、メッセージを不審または中立に分類させ、構造化された報告形式で出力させる用途でAIを試用した。GoogleはGeminiの安全応答が作動したことを受け、当該活動に関連する資産を無効化する措置を取った。 | 中 | `source--gtig-adversarial-ai-2026` |
| Signalバックアップ復旧キーを狙うサポート偽装フィッシング | credential-phishing | 不明 | 不明 | 2026-06-26 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--5403aec9c83d6a925f61 |  |  | victim--activity-rule--e04e41d45e103c8fb3ad | FBIとCISAは、暗号化メッセージングアプリのサポート窓口を装うフィッシングが進化したと警告した。攻撃者は被害者にバックアップを有効化させたうえで復旧キーを送らせ、検証コードやアカウントPINと併せて詐取する。復旧キーを入手すると攻撃者は自分の端末でバックアップを復元し、過去の個人およびグループの会話を閲覧できる。標的は現職および元職の米国・各国政府関係者、軍関係者、政治家、ジャーナリスト、ウクライナの重要人物である。侵害後に同じ電話番号で新規アカウントを作成しても旧復旧キーは無効化されないため、新しい復旧キーの生成が必要である。本PSAは2026年3月の告知に対する更新であり、活動は継続中である。 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| AIを組み込んだ自動ボットによるTelegramチャンネル監視 | UNC5792 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Signalバックアップ復旧キーを狙うサポート偽装フィッシング | UNC5792 | 情報なし | 情報なし | 情報なし | ウクライナ, 米国, 政府・行政, メディア・報道 | 被害事例: Signalバックアップ復旧キーを狙うサポート偽装フィッシング | 中 |

FBI・CISAは2026年3月に最初の告知を行い、2026-06-26のPSA(I-062626-PSA)でこれを更新した。GTIGは2026-09-08のAI脅威報告で、AIを組み込んだTelegram監視の事例として本クラスタを取り上げている。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ウクライナ | 活動「Signalバックアップ復旧キーを狙うサポート偽装フィッシング」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026` |
| countries | 米国 | 活動「Signalバックアップ復旧キーを狙うサポート偽装フィッシング」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026` |
| sectors | 政府・行政 | 活動「Signalバックアップ復旧キーを狙うサポート偽装フィッシング」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026` |
| sectors | メディア・報道 | 活動「Signalバックアップ復旧キーを狙うサポート偽装フィッシング」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Signalバックアップ復旧キーを狙うサポート偽装フィッシング | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--5403aec9c83d6a925f61 |  |  | エンドポイント |  | 不明 | 不明 | 2026-06-26 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| FBIとCISAの共同PSAが本指定子を明示しており、政府・法執行機関による言及として未帰属クラスタ台帳の昇格閾値を満たす。 | 高 | `source--fbi-cisa-psa-signal-recovery-keys-2026` | 「To date, this activity has been publicly tracked as UNC5792 and UNC4221.」の一文が根拠。ただし追跡名を付与した組織は明示されていない。 |
| Signalの復旧キー窃取とTelegramチャンネルの監視は、いずれもメッセージングアプリ上の通信内容の取得を目的としており、収集対象として一貫している。 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026`, `source--gtig-adversarial-ai-2026` | 2つの活動が同一の運用単位によるものかは、いずれの資料も述べていない。共通するのは収集対象の性質である。 |
| 標的は政府・軍関係者、政治家、ジャーナリスト、ウクライナの重要人物であり、ロシアの情報要求と整合する個人標的型の収集活動である。 | 中 | `source--fbi-cisa-psa-signal-recovery-keys-2026` | PSAの標的記述に基づく。組織侵害ではなく個人アカウントを直接狙う点が特徴である。 |

### 情報ギャップ

- 両活動とも一次資料が観測期間を明示しておらず、活動期間はunknownである。first_seen / last_seen も確定できていない。
- IOCが公開されておらず、iocs.json / artifacts.csv は空である。指標による将来観測との突合ができない。
- GTIGが報告するTelegram監視活動と、PSAが警告するSignalフィッシングが同一の運用単位によるものかは、いずれの資料も述べていない。

### 不確実性

- FBI・CISAのPSAはUNC5792とUNC4221を同一活動の追跡名として併記しており、両者が同一主体か、一方が他方を包含するかは未解決である。profiles/unc4221 とは統合せず、relationships へ taxonomy-overlaps-with / scope: unknown として記録した。同じ活動が両プロファイルに存在するのはこの併記に基づく。
- PSAは追跡名を付与した組織を明示していない。UNC指定子の形式からGTIG(Mandiant)による命名と推測されるが、資料上は確認できていない。
- sponsor_typeはstate-alignedとした。ロシア情報機関との関連はPSAの活動記述に基づくもので、UNC5792という指定子と特定機関の対応を述べた資料はない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--fbi-cisa-psa-signal-recovery-keys-2026 | Russian Cyber Actors Targeting Backup Recovery Keys of Encrypted Messaging Applications (I-062626-PSA) | Federal Bureau of Investigation / Cybersecurity and Infrastructure Security Agency | 2026-06-26 | https://www.ic3.gov/PSA/2026/PSA260626 | government-advisory | TLP:CLEAR | 高 |
| source--gtig-adversarial-ai-2026 | GTIG AI Threat Tracker: From Prompting to Autonomy - The Evolution of Adversarial AI | Google Threat Intelligence Group | 2026-09-08 | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai | vendor-research | TLP:CLEAR | 高 |

## 自由記述

本プロファイルは2026-09-10の日次チェックで未帰属クラスタ台帳から昇格したものであり、status は draft から開始する。profiles/unc4221 との統合は行っていない。
