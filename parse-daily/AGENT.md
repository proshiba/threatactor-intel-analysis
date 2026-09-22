# 日次脅威インテリジェンス反映手順

この文書は、`proshiba/tech-memo`の以下のデータを毎日取得し、脅威アクター
プロファイルへ安全に反映するエージェント向けの作業規則である。

- `daily-news/news`: 日次ニュース、要約、一次ソース、記事内IOC
- `daily-news/iocs`: 一次ソースを再確認して作成したIOC CSVと収集ログ

`actor_profile/RULES.md`、`actor_profile/GENERATION_RULES.md`、
`actor_profile/OSINT_RULES.md`を上位規則とする。
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
   活動名と説明はtech-memoの記事見出し・要約をそのまま使う。1本の資料が複数の
   クラスターを扱い、見出しが当該アクター以外の作戦を指している場合だけ、
   `review-decisions.json`の`activity_overrides`（`title`、`summary`）で
   差し替える。原文を確認したうえで行い、差し替えた理由を`review_notes`へ残す。
   通常のactivity IDとrecord IDは`activity_reference`から生成するため、表示名の
   差し替えでは作り直されない。日次Activityを根拠精査済みの恒久Activityへ昇格する
   場合だけ、判断へ例えば
   `"activity_id_override": "activity--darkhotel-kctv-lure-2026"`を保存できる。
   overrideは`activity--<actor-slug>-...`の小文字stable IDでなければならず、
   `activity--daily-*`や別actorのnamespaceを使わない。
6. `capability_decisions`は候補ごとに`approved`、`rejected`、
   `related-only`を判断する。`pending`を残したレコードは承認済みにできない。
7. 承認する活動の`stix_object_type`を確認する。日次取込は`activity_type`から
   保守的な既定値（`intrusion`→incident、`reported-activity`等→grouping、
   作戦ラベル→campaign）を設定するが、これは初期値であり判断ではない。
   判断基準は`actor_profile/OPENCTI_INGESTION_RULES.md`を正とする。
   1組織への個別侵害をcampaignにしない。作戦・主体・関係を確定できない
   調査集合はgroupingに留める。既定値と違う判断になった場合は
   `actor_profile/activity-stix-model-curation.json`の`decisions`へ
   `profile_id`・`activity_id`・`stix_object_type`・理由を追加し、反映手順の
   `migrate_stix_modeling.py --apply`で既定値より優先して適用する。
8. artifact候補はレコード承認と別に確認し、値そのものが原文で確認できた項目だけ
   artifact側へ`review_status: approved`を付ける。
9. `validate_daily.py`、`apply_review_queue.py`のdry-run、`--apply`の順に実行する。
10. `python3 actor_profile/scripts/migrate_stix_modeling.py --apply`で
    STIX種別のcuration判断を適用し、続けて
    `python3 actor_profile/scripts/migrate_activity_model.py --apply`、
    `python3 actor_profile/scripts/enrich_activity_intelligence.py --apply
    --report actor_profile/activity-intelligence-report.json`を実行する。これにより、
    レビュー済み活動の標的・被害事例・明示TTPと、公式ATT&CKキャンペーンの
    TTP／マルウェアを活動へ結び付ける。抽出ルール変更時は
    `actor_profile/activity-observation-rules.json`の差分と誤検出監査を行う。
    帰属国を標的候補に流用しない規則は`GENERATION_RULES.md` 2.を参照する。
11. 続けて`python3 actor_profile/scripts/enrich_targeting_scope.py --apply`を実行する。
    活動単位の標的更新後に行うことで、個別国、全世界等の広域表示、複数国から
    導出するUI用地域を再集約できる。日本は被害が確認できる場合に個別国として残す。
    `profiles/targeting-audit.json`の未解決値と地理情報なしのアクターを確認し、
    帰属国やインフラ所在国を標的国へ流用しない。
    最後に`python3 actor_profile/scripts/materialize_activity_diamonds.py --apply`で
    活動別Diamond Modelを再生成する（上記2つのenrichスクリプトからも自動実行される）。
12. `validate_daily.py --check-applied`と各プロファイルの既存validatorを確認する。
    TTPの期間集計では`reported_at`を観測日として使用していないこと、活動・TTP・
    被害事例の双方向参照が切れていないことも確認する。
13. 変更したアクターの派生データを再生成する。
    - `python3 actor_profile/scripts/build_claim_audits.py --actor <slug>`
      （新しい活動・capabilityはclaim監査台帳の対象。変更アクターごとに実行）
    - `python3 actor_profile/scripts/build_opencti_bundles.py --prune`
      （OpenCTI取込Bundleとmanifest.jsonの再生成。**必ず全件で実行する。**
      `--actor`はmanifestを対象アクターだけへ書き換え、`--prune`併用時は
      他アクターのBundleを削除するため、日次では使わない）
    - `python3 actor_profile/scripts/build_actor_research_dossiers.py`
      （`generated/research-dossier.json`と集計の再生成。全件実行）
14. UIへ公開する場合は`python3 ui/build_data.py`と
    `python3 ui/build_portal_index.py`を実行し、TTP Matrixと
    マルウェア利用履歴のall time／過去3年／過去1年、公開索引の件数を確認する。
15. 変更差分、採用・保留・不採用件数、検証結果を報告する。pushは明示依頼時のみ行う。
16. レビューと反映が完了した日まで`state.json`を更新する。未レビューの新規日を
    `last_scanned_date`より先へ進めない。

## 法執行・制裁記事のルーティング

- 逮捕、起訴、訴追、制裁、差押え、裁判結果は攻撃Activityではない。法執行記事の
  公開日を`first_observed` / `last_observed`へ入れず、`latest_activity`の判定にも使わない。
- 記事が過去の攻撃キャンペーンを一次資料として具体化している場合は、攻撃期間だけを
  Campaign / Incident / Groupingへ反映する。法的措置は、実名の個人を
  `associated_entities[]`の`threat-actor-individual`、会社・機関を`organization`として
  分離し、各entityの`legal_actions[]`へ記録する。旧式の`law-enforcement` Activityを
  作らない。
- 逮捕、国内訴追、別法域の起訴、制裁はそれぞれ別のlegal actionである。対象者と法域を
  一括化せず、各actionへ直接の`evidence_refs`を付ける。起訴・chargeは政府資料であっても
  `status: alleged`、逮捕・実施済み制裁は`status: completed`とする。有罪判決がない限り
  犯罪事実を確定表現にしない。
- `action_date`は逮捕日、起訴状のfiled/returned日、制裁指定日など、資料が明示した行為日
  だけを使う。プレスリリース公開日、起訴状のunseal日、日次ファイル日を代用しない。
  行為日が不明ならunknownのままとし、公開日・unseal日はsource metadataまたは説明へ残す。
- 名前付きentityへ安全に結べない妨害・摘発記事は、レビュー判断と根拠を保持して
  `rejected`（攻撃Activityとして不採用）にする。これは法的情報を捨てる意味ではない。
  schema 1.4のentity/legal_actionsへ反映する別レビュー候補として報告し、主体不明の
  Activityや個人を推測で作らない。

## アクター照合

- IOC CSVの`actor`列は強い候補根拠だが、帰属の確定そのものではない。
- canonical nameまたは`scope: exact`のaliasへ一意に一致した場合だけ自動承認候補に
  できる。`overlapping`、`broader`、`narrower`、複数プロファイル一致は手動確認する。
- `deprecated` profileの旧canonical名が、curationで統合済みのactive profileに
  `scope: exact` aliasとして存在する場合はactive側へ解決する。旧slugへ新規レコードを
  保存せず、過去のreview decisionとdaily observationもcanonical slugへ移行する。
- `low confidence`、`suspected`、`possible`、複合名、`unknown`は自動承認しない。
- ニュース本文の名前一致は発見用途に限り、自動承認しない。同名マルウェア、製品名、
  被害組織名、過去事例への言及でないか原文を確認する。
- `activity_claim`は名前一致より厳しいレビュー補助である。`strong-subject`はexact名、
  攻撃活動を主題とするタイトル、同一文の実行主体表現を満たす候補を表す。ただし、
  「Xのexploit/製品をYが使用」「Xが開発したツールが悪用された」のように、Xが
  vendor/developer/provenanceとして現れるだけの文はoperator根拠ではない。製品・exploitの
  開発元と実際の攻撃実行主体を必ず分離する。
  `attributed-subject`は当該の攻撃・侵害・キャンペーンへの明示的な帰属が同一文に
  ある候補を表す。どちらも帰属確定を意味せず、類似・重複・後継・一般的な関連は
  含めない。`scope-review-required`、`name-collision`、`attribution-uncertain`、
  `historical-reference`、`non-operational`は一括承認しない。
- 既存プロファイルにない名前は無理に近いアクターへ寄せず、
  `unmatched_actor_values`へ残す。新規プロファイル作成は別のレビュー対象とする。
- 照合語彙は検証済みaliasだけに絞られている。alias監査（2026-09）で、mapping
  workbookだけを根拠とするaliasは全プロファイルから除去された。これにより
  `Asia`や国名のような衝突は激減した一方、`UNC1151`(Ghostwriter)、`TA542`、
  `DEV-xxxx`系のような実在するベンダー呼称も未一致になる。**未一致は「新規クラスタ」
  ではなく、まず既存アクターの検証済みでない呼称の可能性を疑う。**
  actor-specificな一次資料（命名元ベンダーの記述、ATT&CKのAssociated Groups等）で
  既存アクターの呼称だと確認できた場合は、unknown-clustersへ入れずに、対象profileの
  `actor.aliases`へ`vendor`・`scope`・`evidence_refs`付きで追加する提案として報告する
  （追加自体はRULES.md 5.とGENERATION_RULES.md 7.の確認を経て行う）。
- `config.json`の`actor_value_aliases`は、IOC CSVの`actor`列に現れる修飾付き・複合の
  表記（`BlueDelta (APT28/...)`等）を正規名へ寄せる日次側の写像である。プロファイルの
  alias管理の代替に使わない。原典が単一のexact対応を明示する表記だけを追加する。
- 同名が複数プロファイルへ一致する場合（例: `Sapphire Sleet`はapt38とta444）は
  自動解決しない。原典がどちらのクラスタ境界で追跡しているかを確認し、決められない
  場合は保留する。
- `unmatched_actor_values`はIOC CSVの`actor`列だけを対象とするため、IOCが公開されて
  いない記事の新規アクター名は現れない。この取りこぼしを補うため、記事本文の実行主体
  表現から抽出した名前を`unmatched_name_candidates`へ別建てで残す。抽出は日本語の
  指示語（「攻撃者は」「脅威アクター」「〜グループ」等）に直接続くラテン文字列に限定し、
  既にレジストリへ登録済みの名前と`config.json`の`ignored_name_candidates`は除外する。
  被害組織名・製品名・ベンダー名が混じるため発見用途に限り、レコードは生成しない。
  原文を確認してから未帰属クラスタ台帳との照合と新規プロファイル要否を判断する。
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
  一次資料の公開日を原文で確認できた場合は、`review-decisions.json`の
  `reported_at`に`basis: source-publication`として保存し、日次ファイル日付より優先する。
  どちらも`first_observed` / `last_observed`には転用しない。
- reviewed `reported_at`は完全なtimePointとし、knownならRFC 3339 UTC値、正しいprecision、
  `basis: source-publication`を必須とする。unknownなら`value: null` / `precision: unknown`とする。
  `year`は1月1日00:00:00Z、`month`は当月1日00:00:00Z、`day`は00:00:00Zへ正規化し、
  precisionと矛盾する値を受理しない。既存のcanonical Sourceに独立確認済み公開日がある場合、
  reviewed値との不一致は上書きせず競合として停止する。ただし`daily-news-file-date`は収集日で
  あって公開日ではないため、この公開日競合判定には使わない。
  queue validatorを通さずapplyしてはならず、apply側もvalidation issueがあれば書込み前に停止する。
- `source--daily-*`と`activity--daily-*`は再構築可能な日次slice専用であり、法的措置、恒久的な
  curated activity、個人・組織等の手動主張の所有IDに使わない。`--rebuild-daily`はこれらを
  削除するため、手動主張には安定したcurated IDを割り当てる。同じcanonical URLにcurated
  Sourceがある場合はそのIDをprofile / IOC / artifactで共用し、旧daily IDと観測を移行・重複排除する。
- Source URLのidentity比較ではHTTP(S)のfragment、末尾`/`、`utm_*`等の既知tracking queryだけを
  除去する。記事版・文書ID等を選択しうる未知または意味のあるqueryは保持し、同一Sourceと推定しない。
- Source identityを移行するときは、profileで得た旧→新IDをIOCとartifactへ明示的に伝播する。
  Observation IDは`tech-memo-*`と`csv-row` / `pdf-text` / `text-line` / `xlsx-row`それぞれの元生成式で
  再計算し、後者のIOCではcertificateの`hash_algorithm`とcanonicalな`source_location` JSONを含める。
  元生成方式を判定できない観測は推測で書き換えず、apply前のpreflightで停止する。移行後に同じ
  Observation IDへ収束した行は、campaign/malware/infrastructure/role refsとcontextを保守的に統合する。
- 再ingestで旧IDを復活させないため、`ioc-sources.json`の明示`source[]`も旧→新IDが完全一致する
  全entryの`source_id`だけを更新する。path、field_map、review metadataを変更せず、同じSource IDを
  共有する複数evidence pathも統合・削除しない。`source_groups[].source_id_prefix`が対象旧IDを生成しうる
  場合はprefixを推測変更せずpreflightで停止し、manifest設計を個別レビューする。
- 複数actorを一括applyするときは、必要ファイル、公開日競合、Source移行可否を全actorについて先に
  preflightする。後続actorの不整合で先行actorだけが書き込まれる部分反映を許可しない。
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
- `activity_id_override`は、日次生成Activityのidentityだけをstable curated IDへ
  移すレビュー判断である。反映前に全actorを監査し、同一stable IDへの複数Activityの
  収束、別actorでの所有、同一actor内の未立証な既存ID衝突があれば全書込み前に停止する。
  検証後は旧IDを`actor-profile.json`、`iocs.json`、`artifacts.csv`、
  `ioc-sources.json`の構造化参照へ伝播する。manifestの動的`campaign_refs`列やglobal
  OSINT/curation入力が旧IDを再生成し得る場合は自動推測せず停止し、入力側を明示移行する。
- override付きActivityを再構築する場合、活動名、種別、期間、`reported_at`、説明、
  confidenceはレビュー判断が所有し、手動追加したtarget/malware/infrastructure/tool/TTP/
  victim/evidence refsとanalyst notesは和集合で保持する。Diamond Modelはmerge後の参照から
  再計算する。公開日は`reported_at`/Source metadataであり、観測期間には転用しない。
- `validate_daily.py --check-applied`では旧日次Activity IDが4 canonical filesに残らないこと、
  stable Activityがprofileに1件だけ存在すること、台帳が同じoverrideを記録したことを確認する。
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
  対象はapproved recordだけでなく、全履歴queueに現れるactorと既存の
  `daily-observations.json`を持つactorの和集合とする。恒久alias、relationship、target、
  hunting pivot等が`source--daily-*` / `activity--daily-*` / `malware--daily-*`を参照して
  いる場合は、1件も書き込む前に全体を拒否する。参照を削って続行せず、根拠とActivityを
  stable curated IDへ移行してから再実行する。
  このdependency監査はapplyだけでなくdry-runでも実行する。IOCでは`tech-memo-*` observationを
  除いた後に0件となるIndicatorは削除対象であって依存違反ではない。daily/non-dailyが混在する
  Indicatorはnon-daily observationだけから集約refs・件数・期間を再計算し、その保持観測自体に
  daily IDが残る場合だけ拒否する。
  `ioc-sources.json`も保持される生成入力として同じ監査対象にし、明示`source--daily-*`や
  `campaign_refs`等の`activity--daily-*`が残る場合は拒否する。事前に検証済みのSource旧→新mapで
  明示entryを移行できる場合だけ、その移行後manifestを監査する。
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
