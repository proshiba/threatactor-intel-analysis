# 日次ルーチンの設定

日次チェックは Claude のルーチン（定期実行）として回します。以下はその設定です。

GitHub Actions からも同じ内容を実行できますが、二重に確認することになるため
ワークフローは置いていません。ルーチンが動かないときの予備として決定的な検知だけを
Actions で回したい場合は、`daily_check.py` を実行して job summary へ出すだけの
ワークフローを別途用意してください。

## 設定値

| 項目 | 値 |
|---|---|
| 名前 | アクター更新チェック（日次） |
| スケジュール | 毎日 09:17 JST（UTC 指定の場合は `17 0 * * *`） |
| 実行方式 | 毎回新しいセッションを作成する |
| 通知 | プッシュ通知を有効（任意） |

毎時0分は世界中の定期実行が集中するため、分をずらしています。

## プロンプト

以下をそのまま貼り付けてください。新しいセッションで実行される前提の、
文脈に依存しない内容にしてあります。

プロンプトはルーチン設定側に保存されるため、この文書を更新してもルーチンには
反映されません。**この節を書き換えたら、ルーチン設定のプロンプトも貼り直してください。**

2026-09-17 時点で、実際に発火したプロンプトはこの節より古い版でした。
securelist.ru と「4. 未帰属クラスタの記録」の節、台帳追記のコミット許可がいずれも
欠けており、securelist.ru は3走査連続でエージェントが手動補完していました。
同じずれを繰り返さないよう、版ずれしやすい一覧はプロンプトから外し、
`config.json` の `external_sources` を唯一の正として `daily_check.py` の出力へ
転記する方式に変更しています。プロンプトの記述量は今後も増やさないでください。

---

```text
proshiba/threatactor-intel-analysis で、脅威アクタープロファイルの日次更新チェックを実行してください。

全アクタープロファイルを毎日確認するのは現実的でないため、次の2観点に絞ります。

1. 直近に活動があったアクター（過去365日）に新しい報告がないか
2. tech-memo の daily-news で言及されたアクターの活動記載

## 1. 決定的な検知

まず `git status --short` で未コミット変更がないか確認し、あれば保護してください。

次に以下を実行します。

    python3 parse-daily/daily_check.py --run-scan --top 30

これは proshiba/tech-memo の daily-news を取得し、parse-daily/state.json の
last_scanned_date 以降を走査して、確認対象を抽出します。プロファイルは変更しません。

出力の「観点1・2の交差」に挙がったアクターが最優先の確認対象です。
実行が失敗した場合は原因を報告して停止してください。

## 2. 一次情報源の確認

tech-memo に載っていない新規公開がないか、一次情報源の公開一覧を確認してください。
直近に活動があったアクターに関する新しい一次情報を優先します。

巡回対象は上記 daily_check.py の出力「確認する一次情報源」の節にすべて列挙されます。
一覧の実体は parse-daily/config.json の external_sources で、そこが唯一の正です。
このプロンプトには一覧を書きません。

検索結果のスニペットだけを根拠にせず、公開一覧と原文を確認してください
（actor_profile/OSINT_RULES.md）。結果は publisher・URL・最新の関連公開日・判定の
形式で整理してください。parse-daily/state.json の incremental_scans[].external_source_checks
と同じ形式です。

出力の一覧に載っていない情報源から新規の一次資料を見つけた場合は、その publisher と URL も
同じ形式で報告し、external_sources へ追加すべきかを提案してください。2026-09-15 の
Acronis TRU（Red Heron）が該当例です。

## 3. レビュー

新しいレコードがあれば parse-daily/output/review-queue.json の pending を
主張単位で確認してください。判断規則は parse-daily/AGENT.md に従います。

activity_claim.assessment が strong-subject / attributed-subject でも自動承認の
確定ではありません。evidence_text がアクターを実行主体としていること、同名製品・
別クラスタ・法執行記事・過去言及でないかを原文で確認してください。

法執行記事は攻撃Activityとして承認しません。ただし情報自体を破棄せず、実名の個人・
組織へ紐づく逮捕、起訴、charge、制裁をschema 1.4の
`associated_entities[].legal_actions[]`へ反映すべき候補として、対象者、法域、行為日、
公開日／unseal日との差、一次URLを報告してください。起訴・chargeは有罪認定ではなく
`alleged`です。主体や行為日が不明なら推測せずunknownとし、旧式のlaw-enforcement
Activityは作りません。このルーチンは検知専用なので、profileへの反映は提案に留めます。

日次ID (`source--daily-*` / `activity--daily-*`) は再構築対象です。法的措置や分析者が
精査した恒久Activityを日次IDの下へ追加せず、stable curated IDへ分離してください。
承認済みの日次Activity自体を恒久identityへ昇格する場合は、`review-decisions.json`へ
actor-scopedな`activity_id_override`を保存し、旧IDのprofile/IOC/artifact/manifest参照を
検証済みmigrationで一括更新します。衝突や動的入力がある場合は推測で統合せず停止します。
同一URLのcurated Sourceが既にあれば、そのIDをIOCとartifactにも再利用します。
`--rebuild-daily`の事前監査が恒久claimから日次IDへの参照を検出した場合、参照を消して
続行してはいけません。根拠をstable curated IDへ移行し、全actorの事前監査が通ってから
再構築します。rejected recordだけ、または旧台帳だけが残るactorも対象外にしません。

## 4. 未帰属クラスタの記録

既存プロファイルに一致しない名前を見つけたら、既存アクターの検証済みでない呼称
（照合語彙は検証済みaliasに絞られています）の可能性を先に確認し、次に
parse-daily/unknown-clusters.json を照合してください。判断規則は
parse-daily/AGENT.md の「アクター照合」に従います。

日次チェックは未一致の名前を2系統で報告します。どちらも確認してください。

- 「既存プロファイルに一致しない名前（IOC CSVのactor列）」: 構造化フィールド由来
- 「本文から抽出した未登録のアクター名候補」: 記事本文の実行主体表現由来

後者はIOCが公開されていない記事を拾うための系統です。2026-08-31 の走査では、
FulcrumSec による Manchester Airports Group 侵害の記事に IOC が無く IOC CSV の
actor 列に現れなかったため、前者だけでは検知できませんでした。被害組織名・製品名・
ベンダー名が混じるので、原文を確認してから判断してください。

- clusters に既出なら observations へ観測を追加し、last_seen を更新します
- excluded_name_collisions に記録済みの名称衝突は再検討しません
- どちらにも無く、原文で実体が確認できたクラスタは status: tracking で追加します

この台帳は profiles/ 配下ではないためUIには出ません。独立した一次資料が2本以上
集まった時点でプロファイル昇格を検討し、その判断は提案に留めて指示を待ってください。

台帳への追記と、その追記のみを含むコミットは許可されています。

## 5. 報告

結果を日本語で簡潔に報告してください。

- 新しい報告が0件なら、その旨を1〜2文で述べるだけで構いません
- 該当があれば、アクター名・記事・判定理由と、採用すべきかの推奨を述べてください
- 既存プロファイルに一致しない名前があれば、新規プロファイル候補として挙げてください
- 反映が必要と判断した場合は、提案に留めて指示を待ってください

## 禁止事項

このルーチンは検知・調査・報告と、未帰属クラスタ台帳への追記までです。
次は行わないでください。

- profiles/ 配下の変更（台帳のクラスタをプロファイルへ昇格させる操作を含む）
- レビューキューの承認状態の変更、apply_review_queue.py の --apply 実行
- parse-daily/state.json の更新
- PR作成
- parse-daily/unknown-clusters.json 以外を含む git commit / git push

台帳の追記だけは例外としてコミットとpushを許可します。コンテナは実行後に
回収されるため、コミットしなければ観測が失われ、継続観察が成立しないためです。
その場合も指定ブランチへのpushに留め、PRは作成しないでください。
```

---

## 反映まで任せる場合

上記は意図的に承認・反映を含めていません。保留判定の大半（name-collision、
scope-review-required、attribution-uncertain）が人の判断を要するためです。

数日運用して安全に自動採用できる判定種別が見えてから、`AGENT.md` の実行順序
9〜14（validate_daily.py → apply_review_queue.py --apply → migrate_stix_modeling /
enrich系 → validate_daily.py --check-applied → claim audits / OpenCTI Bundle /
research dossier の再生成 → ui/build_data.py と ui/build_portal_index.py）を
段階的にプロンプトへ加えてください。OpenCTI Bundle は `--actor` と `--prune` を
併用すると他アクターのBundleを削除するため、必ず全件で実行します。
その際も `state.json` はレビュー完了日までしか進めないでください。
