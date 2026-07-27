# Daily intelligence ingestion

`proshiba/tech-memo`の`daily-news/news`と`daily-news/iocs`を取得し、既存の脅威
アクタープロファイルへ反映するためのレビュー優先パイプラインです。

```bash
# 1. sparse cloneを作成、またはmainをfast-forward
python3 parse-daily/sync_daily.py

# 2. 前回以降の候補を作成
python3 parse-daily/build_review_queue.py --since 2026-07-25

# 3. 明示的な実行主体の主張を監査（既定はdry-run）
python3 parse-daily/curate_activity_decisions.py \
  parse-daily/output/review-queue.json

# 4. output/review-queue.jsonをレビューし、採用するrecordをapprovedへ変更
#    Capability候補は個別にapproved/rejected/related-onlyを判断
python3 parse-daily/validate_daily.py parse-daily/output/review-queue.json

# 5. dry-run後に反映
python3 parse-daily/apply_review_queue.py parse-daily/output/review-queue.json
python3 parse-daily/apply_review_queue.py parse-daily/output/review-queue.json --apply

# 6. 反映確認
python3 parse-daily/validate_daily.py \
  parse-daily/output/review-queue.json --check-applied
```

レビュー判断は`review-decisions.json`へ、`actor-slug|activity_reference`をキーとして
保存できます。これにより同じ入力から同じ承認状態、帰属確度、活動期間、
Capability採否、artifact採否を再現できます。IOC配布ファイルが記事と別URLでも、
`config.json`の`activity_reference_aliases`で同一活動へまとめ、出典自体は失わずに
個別のSourceとして保持します。

ニュース候補には`activity_claim`を持たせ、名前の一致場所、実行主体を示す同一文、
alias衝突、推測・過去言及・法執行記事等の判定理由を保存します。
`curate_activity_decisions.py`は`scope: exact`で、攻撃活動を主題とし、実行主体が
明記された`strong-subject`、または当該活動への帰属が同一文で明記された
`attributed-subject`だけを決定候補にします。後者は帰属表現に合わせて確度を
独立して保持します。dry-run結果を確認した後に限り、`--apply`で再現可能な判断を
`review-decisions.json`へ追記できます。判定規則の変更後に自動判断だけを
再構築する場合は`--replace-auto`を併用し、既存の個別レビュー判断は保持します。

Activityの攻撃期間と報告日は分離します。一次資料で期間を確認できない場合でも活動は
保存し、`first_observed`/`last_observed`はunknownのままにします。tech-memo日次
ファイルの日付は`reported_at`に保存され、UIでは「活動時期不明（報告: YYYY-MM-DD）」
として表示されます。

`--approve-structured`は、IOC CSVの`actor`列が既存プロファイルの正規名または
`exact` aliasへ一意に一致し、低信頼・suspected・複合名ではないレコードだけを
承認します。ニュース本文の単純な名前一致は承認しません。レコード承認後も
Capability候補が`pending`ならvalidatorはエラーにするため、malware欄の値が
固有マルウェア名か、偽旗・過去比較・ファイル名・一般分類でないか確認してください。

過去の日次反映をレビュー判断から再構築する場合だけ`--rebuild-daily`を使用します。
このオプションは`source--daily-`等の日次生成部分と`tech-memo-*`観測だけを除去して
再反映し、元レポート由来のデータは保持します。履歴を欠落させないよう、
`--since`/`--until`なしで作成した全履歴queueだけを受け付けます。通常の日次運用では
不要です。
`--no-render`を付けるとMarkdown/STIXが古くなり得ることを実行結果へ明示します。

取得キャッシュと作業キューはGit管理外です。採用済みデータは
`profiles/<slug>/daily-observations.json`に監査可能な形で保存され、
`actor-profile.json`、`iocs.json`、`artifacts.csv`へ冪等にマージされます。
内容が変わらない再実行ではJSONの更新日時も生成物も書き換えません。
詳細な判断規則と日次運用は[AGENT.md](AGENT.md)を参照してください。
