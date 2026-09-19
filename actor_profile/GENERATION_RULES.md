# Actor Profile Generation Rules

この文書は、`actor_profile/`と`profiles/`を自動生成・更新するスクリプトおよび
AIエージェント向けの必須ガードレールです。一般的なデータ規約は
[RULES.md](RULES.md)、OSINT検証は[OSINT_RULES.md](OSINT_RULES.md)を参照してください。

## 1. 最優先原則

自動化は「情報を埋めること」より「誤った断定をしないこと」を優先します。
根拠が足りない場合の正しい値は`unknown`、空配列、またはレビュー待ちです。

## 2. 地理情報と帰属を分離する

次は国家支援の証拠ではありません。

- 国別worksheetへの配置
- actorのorigin / country label
- 使用言語、タイムゾーン、キーボード
- C2・VPN・VPS・WHOISの所在地
- 被害国・標的国
- 開発者や逮捕者の国籍・居住地

これらだけを理由に`state-sponsored`、`state-aligned`、
`sponsor_type: state`を設定してはいけません。

国家支援を構造化するには、政府共同勧告、公式帰属、MITRE ATT&CKのactor-specificな
明示記述、または複数の独立した高品質資料など、スポンサー関係そのものを述べる証拠を
必要とします。

### 禁止例

```text
Russia worksheet
→ Russian actor
→ state-sponsored
→ espionage
```

この連鎖はすべて禁止です。

## 3. 国家支援と動機を分離する

国家支援の有無と、作戦目的・動機は別の主張です。

`state-sponsored`から自動的に`espionage`を生成してはいけません。
国家系アクターでも、諜報、破壊、妨害、影響工作、資金獲得など複数の目的があり得ます。
motivationはactor-specificな本文が明示した範囲だけを記録します。

## 4. Vendor / Product / Operator / Adversaryを分離する

記事中に企業名や製品名が出たことは、その企業が攻撃主体であることを意味しません。

例:

```text
Serbian authority used a Cellebrite exploit/product against a device
```

この場合、攻撃実行主体として検討するのはSerbian authority側です。
Cellebriteはvendor/developerとして関係を記録できますが、同社自身が侵入を実行したと
示す別証拠なしにDiamond ModelのAdversaryへ置いてはいけません。

同じ規則を、RMM、EDR、offensive-security tool、spyware platform、exploit broker、
cloud/CDN、hosting providerにも適用します。

## 5. Entity種別を先に決める

新しいcanonical profileを作る前に、対象が次のどれかを確認します。

- Threat Actor / Intrusion Set / Activity Cluster
- Organization / Government Unit / Company
- Malware / Ransomware / Tool / Software
- Campaign / Operation
- Infrastructure / Service

同じ名称が複数の意味で使われる場合は統合せず、スコープを分けます。

例: REvilは文脈によってransomware/software family、RaaS brand、operatorsを指します。
既存のGOLD SOUTHFIELDのようなoperator profileがある場合、software名とactor名を
機械的に同一化してはいけません。

## 6. Aliasと重複プロファイル

canonical nameとaliasの正規化一致を検出したら、自動統合ではなくレビュー対象にします。

特に次を確認します。

1. 同じ一次資料・同じcampaignを指していないか
2. MITRE IDなど安定IDが同じではないか
3. 一方がbroader/narrower/overlappingなvendor clusterではないか
4. 会社名、malware名、operation名の同名衝突ではないか

先頭の`The`、空白、ハイフン、大小文字だけの差は重複候補として扱います。

## 7. Claim auditからの昇格条件

`unresolved`または`partially-supported`は「誤り」とは限りませんが、
自動生成が確定的なattribution/motivation/exact aliasへ昇格させる根拠にはできません。

重要主張の自動昇格には、少なくとも以下を満たします。

- actor-specificな証拠である
- source scopeが主張のscopeと一致する
- entity種別が一致する
- contradictionが未解消ではない

## 8. Source precedence

自動化の既定優先順位:

1. 政府・法執行機関・CERT等の一次資料
2. MITRE ATT&CK等、原典参照を持つactor-specific knowledge base
3. ベンダーのactor-specific technical report
4. 複数資料を集約したOSINT dataset
5. mapping workbook / naming list / search snippet

4と5は候補生成・cross-checkには使えますが、それ単独で国家支援や動機を確定しません。

## 9. Agent preflight checklist

プロファイルまたは生成コードを変更するエージェントは、commit前に次を確認します。

- [ ] country/originをsponsorshipへ変換していない
- [ ] state-sponsoredをespionageへ変換していない
- [ ] vendor/productをadversaryへ変換していない
- [ ] software/campaign/organizationをactorとして新設していない
- [ ] alias一致だけでexact identityにしていない
- [ ] unresolved/partial claimを確定値へ昇格していない
- [ ] actor-specific evidence_refが重要主張に付いている
- [ ] canonical/alias重複候補を確認した
- [ ] 回帰テストを追加または実行した
- [ ] 生成物と集計を再生成した

## 10. 変更後の推奨実行順

```bash
python3 -m unittest discover -s actor_profile/tests -v
python3 -m unittest discover -s parse-daily/tests -v

python3 actor_profile/scripts/materialize_actor_census.py
python3 actor_profile/scripts/bootstrap_all_profiles.py --scan-report-ttps

python3 actor_profile/scripts/build_claim_audits.py
python3 actor_profile/scripts/enrich_activity_intelligence.py --apply
python3 actor_profile/scripts/enrich_targeting_scope.py --apply
python3 actor_profile/scripts/materialize_activity_diamonds.py --apply
python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest

python3 actor_profile/scripts/render_collection_index.py \
  profiles/processing-summary.json \
  actor_profile/corpus-catalog.json \
  profiles/README.md
```

生成結果に大規模な差分が出る場合は、原因となったルール変更とデータ再生成を別commitまたは
別PRに分け、レビュー可能な状態を保ちます。
