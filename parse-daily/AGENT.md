# 日次脅威インテリジェンス反映手順

この文書は、`proshiba/tech-memo`の以下のデータを毎日取得し、脅威アクター
プロファイルへ安全に反映するエージェント向けの作業規則である。

- `daily-news/news`: 日次ニュース、要約、一次ソース、記事内IOC
- `daily-news/iocs`: 一次ソースを再確認して作成したIOC CSVと収集ログ

`actor_profile/RULES.md`と`actor_profile/OSINT_RULES.md`を上位規則とする。
`actor-profile.json`がプロファイル本文の正規データであり、日次取込の監査台帳は
`daily-observations.json`である。MarkdownとSTIXは生成物である。

## 実行順序

1. 作業開始前に`git status --short`を確認し、利用者の未コミット変更を保護する。
2. `python3 parse-daily/sync_daily.py`を実行する。キャッシュに変更がある場合は
   自動破棄せず停止する。
3. `parse-daily/state.json`の`last_scanned_date`と`last_scanned_commit`を確認し、
   前回走査以降を対象に
   `python3 parse-daily/build_review_queue.py --since YYYY-MM-DD`を実行する。
   初回の履歴走査だけは`--since`を省略できる。
4. `parse-daily/output/review-queue.json`の`pending`を主張単位で確認する。
   `activity_claim.assessment`が`strong-subject`または`attributed-subject`でも
   自動承認の確定ではない。
   `evidence_text`がアクターを実行主体としていること、同名製品・別クラスタ・
   法執行・過去事例でないことを確認する。
5. 採用するレコードだけ`review_status: approved`へ変更し、判断理由を
   `review_notes`へ日本語で記載する。不採用は`rejected`と理由を残す。継続利用する
   判断は`review-decisions.json`にも保存し、再生成可能にする。
6. `capability_decisions`は候補ごとに`approved`、`rejected`、
   `related-only`を判断する。`pending`を残したレコードは承認済みにできない。
7. artifact候補はレコード承認と別に確認し、値そのものが原文で確認できた項目だけ
   artifact側へ`review_status: approved`を付ける。
8. `validate_daily.py`、`apply_review_queue.py`のdry-run、`--apply`の順に実行する。
9. `python3 actor_profile/scripts/migrate_activity_model.py --apply`を実行後、
   `python3 actor_profile/scripts/enrich_activity_intelligence.py --apply
   --report actor_profile/activity-intelligence-report.json`を実行する。これにより、
   レビュー済み活動の標的・被害事例・明示TTPと、公式ATT&CKキャンペーンの
   TTP／マルウェアを活動へ結び付ける。抽出ルール変更時は
   `actor_profile/activity-observation-rules.json`の差分と誤検出監査を行う。
10. 続けて`python3 actor_profile/scripts/enrich_targeting_scope.py --apply`を実行する。
    活動単位の標的更新後に行うことで、個別国、全世界等の広域表示、複数国から
    導出するUI用地域を再集約できる。日本は被害が確認できる場合に個別国として残す。
    `profiles/targeting-audit.json`の未解決値と地理情報なしのアクターを確認し、
    帰属国やインフラ所在国を標的国へ流用しない。
11. `validate_daily.py --check-applied`と各プロファイルの既存validatorを確認する。
    TTPの期間集計では`reported_at`を観測日として使用していないこと、活動・TTP・
    被害事例の双方向参照が切れていないことも確認する。
12. UIへ公開する場合は`python3 ui/build_data.py`を実行し、TTP Matrixと
    マルウェア利用履歴のall time／過去3年／過去1年を確認する。
13. 変更差分、採用・保留・不採用件数、検証結果を報告する。pushは明示依頼時のみ行う。
14. レビューと反映が完了した日まで`state.json`を更新する。未レビューの新規日を
    `last_scanned_date`より先へ進めない。

## アクター照合

- IOC CSVの`actor`列は強い候補根拠だが、帰属の確定そのものではない。
- canonical nameまたは`scope: exact`のaliasへ一意に一致した場合だけ自動承認候補に
  できる。`overlapping`、`broader`、`narrower`、複数プロファイル一致は手動確認する。
- `low confidence`、`suspected`、`possible`、複合名、`unknown`は自動承認しない。
- ニュース本文の名前一致は発見用途に限り、自動承認しない。同名マルウェア、製品名、
  被害組織名、過去事例への言及でないか原文を確認する。
- `activity_claim`は名前一致より厳しいレビュー補助である。`strong-subject`はexact名、
  攻撃活動を主題とするタイトル、同一文の実行主体表現を満たす候補を表す。
  `attributed-subject`は当該の攻撃・侵害・キャンペーンへの明示的な帰属が同一文に
  ある候補を表す。どちらも帰属確定を意味せず、類似・重複・後継・一般的な関連は
  含めない。`scope-review-required`、`name-collision`、`attribution-uncertain`、
  `historical-reference`、`non-operational`は一括承認しない。
- 既存プロファイルにない名前は無理に近いアクターへ寄せず、
  `unmatched_actor_values`へ残す。新規プロファイル作成は別のレビュー対象とする。
- 未帰属だが将来いずれかのアクターへつながり得るクラスタは
  `parse-daily/unknown-clusters.json`へ記録する。既存プロファイルに一致しない名前を
  見つけたら、新規プロファイル作成や既存プロファイルへの寄せ付けより先に、
  この台帳を照合する。
  - `clusters`に既出の場合は`observations`へ観測を追加し`last_seen`を更新する。
    同じクラスタに対して重複エントリを作らない。
  - `excluded_name_collisions`に記録済みの名称衝突は再検討しない。除外理由が
    誤っていた場合だけ、理由を書き換えてから扱いを変える。
  - どちらにも無く、原文で実体が確認できたクラスタは`status: tracking`で追加する。
    URL、公開日、活動期間、標的、判定根拠、原文確認の有無を残す。
  - 一次資料が既存プロファイルとの関連を否定している場合は`related_profiles`へ
    `explicitly-refuted`として残す。将来の誤統合を防ぐ記録であり、省略しない。
- 台帳のクラスタは、独立した一次資料が2本以上、または政府・CERT・法執行機関の
  言及が得られた時点でプロファイル昇格を検討する。単一ベンダーの初報だけでは
  昇格しない。既存アクターへの帰属が一次資料で確定した場合は当該プロファイルへ
  統合し、台帳側は削除せず`status: merged`と統合先・統合日を残す。
- 台帳は`profiles/`配下ではないため、`ui/build_data.py`と
  `ui/build_portal_index.py`のどちらからも読まれずUIには出ない。UIへ出すには
  `profiles/<slug>/actor-profile.json`への昇格が必要である。UNC1549、UNC3753、
  UNC4221、UAC-0099、UNC5342等、未帰属クラスタ指定子が一級プロファイルとして
  存在する前例に従い、昇格時の`status`は`draft`から開始する。
- アクター間関係は、同じ記事への登場やIOC共有だけで追加しない。一次資料が
  組織関係・協力・部分重複・ツール共有を明示した場合に、関係種別とスコープを
  分離して追加する。
- Sourceの`reliability`は資料そのものの信頼性、レコードの`confidence`は活動と
  アクターの関連確度として分離する。一方の値をもう一方へコピーしない。

## OSINTと反証確認

- tech-memoの要約だけでなく、`primary_url`の原文を開いて主体、観測期間、標的、
  malware、TTP、IOCの文脈を確認する。
- 政府・CERT・法執行機関、直接観測したベンダー、公式ATT&CKを優先する。
- 公開日を攻撃観測日に流用しない。活動の`first_observed`と`last_observed`は、
  IOC CSVの観測日または一次資料が明示した日だけを使う。
- 互換データに`basis: source-publication`、`publication/ongoing`等があっても
  期間集計へ含めず、一次資料で観測期間を確認できた場合だけ置き換える。
- 攻撃期間が不明でもActivityは作成できる。その場合は期間をunknownとし、資料発行日
  またはtech-memo日次ファイルの日付を`reported_at`へ分離して保存する。
- 既存帰属や関係と競合する情報は上書きしない。`claim-audit.json`の
  `contradicted`、`partially-supported`、`unresolved`等で両論とスコープを残す。
- 「反証が見つからなかった」を「反証なし」と断定しない。検索範囲と未解決点を残す。

## IOCとartifact

- ハッシュ、IP、domain、URL、メール、証明書fingerprintだけをIOCへ入れる。
- 実行コマンド、検体内文字列、PDB、パス、ファイル名、registry、mutex、
  named pipe、task、service、process、User-Agent、URI path、メール件名、lure名は
  `artifacts.csv`へ入れる。
- IOC観測には、観測日、source commit、元ファイルと行番号、一次ソースURL、
  activity、malware、role、confidence、説明を保存する。
- 同じIOCを値だけで捨てず、資料・行・日付が異なる観測は別Observationとして残す。
- 同一活動の記事、IOC一覧、hash一覧は1活動へまとめるが、各Observationの
  `source_id`は実際にそのIOCを掲載したURLごとに保持する。
- 一般サービス、被害組織の正規URL、PoC内のprivate IP、サンプル値は攻撃者IOCとして
  採用しない。判断がつかない値はcandidateとして保留する。
- レコードの承認はartifactの自動承認を意味しない。artifactは値と文脈を個別確認する。

## 保存と冪等性

- `record_id`、source ID、activity ID、Observation IDは入力の安定値から生成し、
  表示名の変更で作り直さない。
- 承認済みレコードは`profiles/<slug>/daily-observations.json`へ保存する。
- 反映スクリプトは既存の`iocs.json`と`artifacts.csv`を保持してマージする。
  元レポートがリポジトリに無い状態で`ingest_observables.py`を全件再実行し、
  既存IOCを上書きしてはならない。
- 再実行は同一IDを重複追加しない。過去レコードの修正・撤回は台帳から黙って削除せず、
  変更理由を残してから対象データを更新する。
- 公開日やIOC CSVの収集日を活動期間へ自動転用しない。活動期間は
  `activity_period`として一次資料確認後に保存する。
- `--rebuild-daily`は日次生成部分だけをレビュー判断から再構築する保守操作である。
  `--since`/`--until`なしの全履歴queueでのみ実行し、通常取込には使わない。
  `--no-render`使用時は派生Markdown/STIXが古くなるため、
  同一作業内で必ず再生成する。

## レビュー完了条件

- queue validatorのerrorが0
- 反映対象のprofile validatorのerrorが0
- 承認済みrecordが各`daily-observations.json`に存在
- source、activity、IOC/artifactの参照切れがない
- activity、TTP、victim caseの双方向参照が一致する
- 過去1年・3年の集計に`reported_at`だけのレコードが入っていない
- 新規情報が日本語で記述され、アクター名・malware名・製品名は原表記を維持
- 未照合、低信頼、競合、取得不能な一次ソースが作業結果に明記されている
