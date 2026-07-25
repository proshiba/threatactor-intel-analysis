# OSINT更新規約

## 情報源の優先順位

1. 政府機関、CERT、法執行機関の勧告・起訴・制裁資料
2. 攻撃を直接観測したセキュリティベンダーの技術報告
3. 公式MITRE ATT&CK、公開マルウェア解析、インシデント報告
4. 二次報道・集約サイト（発見用途のみ。可能な限り原典へ遡る）

検索結果のスニペットだけを証拠として使用しない。原文を開き、アクター名、公開日、
観測期間、主張、IOC/TTPの文脈を確認できたものだけを採用する。

## OSINT Source必須項目

- `source_id`
- `url`
- `title`
- `publisher`
- `published_at`
- `accessed_at`
- `source_type`
- `language`
- `tlp`
- `reliability`
- `actor_scope`
- `claims_supported`
- `archive_url`（存在する場合）
- `analyst_notes`

## 更新判定

- 新aliasは、既存クラスターとのスコープを`exact`と断定せず、
  `overlapping`、`broader`、`narrower`、`unknown`を選ぶ。
- 帰属変更は、単独ベンダーの名称変更と政府帰属を分離する。
- 「公開日」と「攻撃観測日」を分離し、公開日を観測日に流用しない。
- 新キャンペーン、マルウェア、インフラ、TTP、標的は、該当主張のURLを
  `evidence_refs`で参照する。
- IOCとartifactは、原文で同一キャンペーン／マルウェアとの関係を確認できた場合のみ
  その参照を付与する。
- 既存情報と競合する場合は上書きせず、`assessment.uncertainties`と
  `analyst_notes`へ両論を残す。

## 調査状態

各アクターに次の状態を持たせる。

- `not_started`
- `searched`
- `source_verified`
- `integrated`
- `needs_review`

調査クエリ、確認したURL、採用／不採用理由を保存し、同じ検索を繰り返さない。
