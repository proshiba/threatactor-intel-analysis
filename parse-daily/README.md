# Daily intelligence ingestion

`proshiba/tech-memo`の`daily-news/news`と`daily-news/iocs`を取得し、既存の脅威
アクタープロファイルへ反映するためのレビュー優先パイプラインです。

```bash
# 1. sparse cloneを作成、またはmainをfast-forward
python3 parse-daily/sync_daily.py

# 2. 前回以降の候補を作成
python3 parse-daily/build_review_queue.py --since 2026-07-25

# 3. output/review-queue.jsonをレビューし、採用するrecordをapprovedへ変更
python3 parse-daily/validate_daily.py parse-daily/output/review-queue.json

# 4. dry-run後に反映
python3 parse-daily/apply_review_queue.py parse-daily/output/review-queue.json
python3 parse-daily/apply_review_queue.py parse-daily/output/review-queue.json --apply

# 5. 反映確認
python3 parse-daily/validate_daily.py \
  parse-daily/output/review-queue.json --check-applied
```

`--approve-structured`は、IOC CSVの`actor`列が既存プロファイルの正規名または
`exact` aliasへ一意に一致し、低信頼・suspected・複合名ではないレコードだけを
承認します。ニュース本文の単純な名前一致は承認しません。

取得キャッシュと作業キューはGit管理外です。採用済みデータは
`profiles/<slug>/daily-observations.json`に監査可能な形で保存され、
`actor-profile.json`、`iocs.json`、`artifacts.csv`へ冪等にマージされます。
詳細な判断規則と日次運用は[AGENT.md](AGENT.md)を参照してください。
