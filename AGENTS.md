# Repository Agent Instructions

このリポジトリで自動編集を行うエージェントは、作業開始前に次を読むこと。

1. `actor_profile/RULES.md`
2. `actor_profile/GENERATION_RULES.md`
3. OSINTを変更する場合は`actor_profile/OSINT_RULES.md`
4. 日次取込を変更する場合は`parse-daily/AGENT.md`
5. STIXまたはOpenCTI取込を変更する場合は`actor_profile/OPENCTI_INGESTION_RULES.md`

## Non-negotiable guardrails

- 国・origin・worksheet・IP所在地から国家支援を推定しない。
- `state-sponsored`からespionage等のmotivationを推定しない。
- vendorや製品の使用を、そのvendor自身による攻撃と解釈しない。
- Actor / Organization / Malware / Software / Campaignを同名だけで統合しない。
- Activityを一律にCampaign化せず、Campaign / Incident / Groupingを明示する。
- Groupingの包含から未立証Relationshipを生成しない。
- 出典公開日を観測日時やRelationshipの有効期間へ転用しない。
- alias一致だけでexact identityへ昇格しない。
- `unresolved` / `partially-supported`の主張を追加根拠なしに確定値へ昇格しない。
- 不明な値は推測で埋めず、`unknown`または空配列を使う。

生成ロジックを変更した場合は、同じ誤りを防ぐ回帰テストとルールドキュメントを同じPRに
含めること。
