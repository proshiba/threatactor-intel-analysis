# 日次ルーチンの設定

Claude のルーチン（定期実行）として日次チェックを回す場合の設定です。
GitHub Actions の [daily-actor-check.yml](../.github/workflows/daily-actor-check.yml)
と同じ内容を、Claude 側のスケジュールから実行するためのものです。

どちらか一方で足ります。両方動かすと同じ確認を二重に行うため、ルーチンを使う場合は
ワークフローの `review` ジョブを無効化するか、ワークフロー自体を削除してください。

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

---

```text
proshiba/threatactor-intel-analysis で、脅威アクタープロファイルの日次更新チェックを実行してください。

全673アクターを毎日確認するのは現実的でないため、次の2観点に絞ります。

1. 直近に活動があったアクター（過去365日、約75件）に新しい報告がないか
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

tech-memo に載っていない新規公開がないか、次の一次情報源の公開一覧を確認してください。
直近に活動があったアクターに関する新しい一次情報を優先します。

- Microsoft Security Blog https://www.microsoft.com/en-us/security/blog/
- Google Threat Intelligence https://cloud.google.com/blog/topics/threat-intelligence
- Palo Alto Networks Unit 42 https://unit42.paloaltonetworks.com/
- Cisco Talos https://blog.talosintelligence.com/
- ESET Research https://www.welivesecurity.com/en/eset-research/
- SentinelLabs https://www.sentinelone.com/labs/
- Kaspersky Securelist https://securelist.com/

検索結果のスニペットだけを根拠にせず、公開一覧と原文を確認してください
（actor_profile/OSINT_RULES.md）。結果は publisher・URL・最新の関連公開日・判定の
形式で整理してください。parse-daily/state.json の incremental_scans[].external_source_checks
と同じ形式です。

## 3. レビュー

新しいレコードがあれば parse-daily/output/review-queue.json の pending を
主張単位で確認してください。判断規則は parse-daily/AGENT.md に従います。

activity_claim.assessment が strong-subject / attributed-subject でも自動承認の
確定ではありません。evidence_text がアクターを実行主体としていること、同名製品・
別クラスタ・法執行記事・過去言及でないかを原文で確認してください。

## 4. 報告

結果を日本語で簡潔に報告してください。

- 新しい報告が0件なら、その旨を1〜2文で述べるだけで構いません
- 該当があれば、アクター名・記事・判定理由と、採用すべきかの推奨を述べてください
- 既存プロファイルに一致しない名前があれば、新規プロファイル候補として挙げてください
- 反映が必要と判断した場合は、提案に留めて指示を待ってください

## 禁止事項

このルーチンは検知・調査・報告までです。次は行わないでください。

- profiles/ 配下の変更
- レビューキューの承認状態の変更、apply_review_queue.py の --apply 実行
- parse-daily/state.json の更新
- git commit / git push / PR作成
```

---

## 反映まで任せる場合

上記は意図的に承認・反映を含めていません。全履歴監査では1,006件中651件が保留
（name-collision 113件、scope-review-required 155件、attribution-uncertain 72件）で、
大半が判断を要するためです。

数日運用して安全に自動採用できる判定種別が見えてから、`AGENT.md` の手順
（validate_daily.py → apply_review_queue.py --apply → validate_daily.py --check-applied
→ ui/build_data.py → ui/build_portal_index.py）を段階的にプロンプトへ加えてください。
その際も `state.json` はレビュー完了日までしか進めないでください。
