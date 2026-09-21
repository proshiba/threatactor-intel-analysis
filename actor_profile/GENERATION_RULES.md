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

### 帰属国を標的国へ流用しない（活動記述からの自動構造化）

`enrich_activity_intelligence.py`の`actor_attribution_context()`は、活動記述に現れる
国名のうち実行主体側を指すものを標的候補から除外します。除外する日本語の語形は
次のとおりで、いずれも被害側の表現とは助詞または連結の形が異なります。

| 語形 | 例 | 被害側の形 |
|---|---|---|
| `X系`、`X関連`、`Xの国家支援` + 主体語 | 北朝鮮系ハッカーグループ | 日本の政府機関 |
| `X` + `サイバー攻撃/犯罪/諜報` + 主体語 | 北朝鮮サイバー攻撃グループ | — |
| `Xを背景とする／した` | 北朝鮮を背景とするグループ | — |
| `XIT労働者`（助詞を挟まない連結） | 北朝鮮IT労働者 | 日本のIT労働者 |
| `Xによる攻撃/侵害/諜報` | 中国によるハッキング | 日本への攻撃 |
| `Xからの圧力/制裁/要求` | 米国からの圧力 | 米国の重要インフラ |
| `X人 N人`（国籍付きの人数） | イラン人17人を起訴 | 日本人を標的 |

語形を追加するときは、被害側の表現を巻き込まないことを確認し、
`actor_profile/tests/test_activity_intelligence.py`へ肯定・否定の両方の回帰テストを
同じ変更に含めてください。既存プロファイルへ過去の取込で入った値は自動では
削除されないため、規則を直した後に当該エントリと参照を手動で除去します。

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


### Entity境界の追加ルール

- MITRE ATT&CKでSoftware/Malwareとして管理される名称を、名前一致だけでcanonical Actorにしてはいけない。
  例: GravityRAT(S0237)、Shamoon(S0140)。Operator/clusterは別entityとして追跡する。
- Malware名が歴史的にoperatorの通称として使われる場合も、softwareとactorの両スコープを
  同一profileへ混在させず、legacy profileはdeprecated化し、根拠のあるActor名へ分離する。
- 広域scheme/ecosystemとvendor-specific named adversaryをexact aliasにしない。
  DPRK IT Worker Schemesのような上位ecosystemとFAMOUS CHOLLIMAのようなvendor追跡Actorは
  `related-to` / `overlaps-with`等のrelationshipで結ぶ。
- `actor-census-curation.json`の`exclude`/`override`を使い、次回census materializationで
  software名や誤aliasが再びcanonical Actorへ戻らないようにする。
- ATT&CKの同一Group IDでvendor renameがAssociated Groupとして確認できる場合は、
  rename後の名称を第二のcanonical Actorとして残さず、`merge`で既存のstable profileへ
  統合する。統合元のactor-scoped evidenceは統合先の`source_dirs`へ引き継ぎ、既存profileは
  stable ID互換のため`deprecated` tombstoneとして残す。
- ATT&CK Softwareと同名の候補は、命名元の原典が独立したoperator/groupも同名で追跡して
  いる場合を除きActor化しない。Zebrocyのように原典が明示的にmalware/toolsetとし、別の
  groupが運用すると述べる名称は`exclude`する。
- deprecated profileをSTIXへ出力する場合、`intrusion-set`に`revoked: true`と
  `x_profile_status: deprecated`を付け、active entityとして再利用されないようにする。

## 6. Workbookからのalias抽出

`APT Groups and Operations.xlsx`等のmapping workbookでは、alias候補として扱う列を
**allowlist**する。`Common Name`、`Other Name(s)`、`Alias(es)`のような明示的な
名前列だけを使用し、Country / Origin / Sponsor / Attribution / Comment / Description /
Targets / Operation / Toolset / Malwareなどをaliasへ流用してはいけない。

複数aliasを含む名前セルは`,`、`;`、改行、区切りとしての` / `で分割する。
国名単体、帰属説明文、スポンサー説明文、地域説明などはaliasではない。

元Workbookは本リポジトリに保持しないため、既存profileの補正では
`actor_profile/scripts/migrate_workbook_aliases.py --apply`を使用し、
`actor-mapping-workbook`だけを根拠とするaliasを除去する。MITRE、catalog、
actor-specific source由来のaliasは保持する。元Workbookを利用できる生成環境では、
上記allowlist列だけからaliasを再抽出する。

## 7. Aliasと重複プロファイル

canonical nameとaliasの正規化一致を検出したら、自動統合ではなくレビュー対象にします。

特に次を確認します。

1. 同じ一次資料・同じcampaignを指していないか
2. MITRE IDなど安定IDが同じではないか
3. 一方がbroader/narrower/overlappingなvendor clusterではないか
4. 会社名、malware名、operation名の同名衝突ではないか

先頭の`The`、空白、ハイフン、大小文字だけの差は重複候補として扱います。
同一プロファイル内で正規化後に同じになるaliasは、先に現れた根拠付き表記を残して
materialization時に重複排除します。

## 8. Claim auditからの昇格条件

`unresolved`または`partially-supported`は「誤り」とは限りませんが、
自動生成が確定的なattribution/motivation/exact aliasへ昇格させる根拠にはできません。

重要主張の自動昇格には、少なくとも以下を満たします。

- actor-specificな証拠である
- source scopeが主張のscopeと一致する
- entity種別が一致する
- contradictionが未解消ではない

`build_claim_audits.py`は、identity/alias/relationshipに加えて、actor type、sponsor type、
帰属組織、motivation、activity、victim case、target、全capability区分、TTP、key judgmentを
監査対象にします。参照がない主張は`unresolved`、集約資料またはrepository内取込だけを
根拠とする主張は原則`partially-supported`です。
deprecated profileの台帳は過去の主張を現行主張として残さず、`superseded`の
lifecycle claim 1件だけを保持し、現行コレクション集計から除外します。

`state-sponsored`の自動支持は次のいずれかに限定します。

- actor-specificな証拠を持つ`attribution.sponsor_type: state`
- actor-specificなMITRE ATT&CK記述が国家支援を明示する
- nation-state区分であることを明示した外部taxonomyにcanonical名または`exact` aliasが一致する

国・originの値だけ、非exact alias、`state-aligned`だけでは`state-sponsored`を
`supported`にしません。

## 9. Source precedence

自動化の既定優先順位:

1. 政府・法執行機関・CERT等の一次資料
2. MITRE ATT&CK等、原典参照を持つactor-specific knowledge base
3. ベンダーのactor-specific technical report
4. 複数資料を集約したOSINT dataset
5. mapping workbook / naming list / search snippet

4と5は候補生成・cross-checkには使えますが、それ単独で国家支援や動機を確定しません。

## 10. Census curation

`actor-census.json`からの自動materializationでentity種別や重複を安全に解決できない場合は、
`actor_profile/actor-census-curation.json`へ人手補正を記録します。

- `exclude`: software/brand等をcanonical Actorとして生成しない
- `merge`: census identityを既存profileへ統合する
- `override`: canonical名、stable slug、alias、actor typeを根拠付きで補正する

各ruleには`reason`と`evidence_urls`を必須とし、再生成時も自動推定よりcurationを優先します。
既存profileのstable IDを維持する必要がある場合は`slug`を明示します。

## 11. Agent preflight checklist

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

## 12. 変更後の推奨実行順

```bash
python3 -m unittest discover -s actor_profile/tests -v
python3 -m unittest discover -s parse-daily/tests -v

python3 actor_profile/scripts/materialize_actor_census.py

# 旧生成ルールで既存profileへ入った地理由来のstate/espionage等だけを安全に移行
python3 actor_profile/scripts/migrate_generated_attribution.py --apply

# 新規profileをbootstrapする場合のみ使用（既存profileの一括overwriteは禁止）
python3 actor_profile/scripts/bootstrap_all_profiles.py --scan-report-ttps

# 新規profileを含むcanonical側へmergeデータを移し、一次情報aliasを反映
python3 actor_profile/scripts/migrate_curated_entity_boundaries.py --apply
python3 actor_profile/scripts/apply_verified_alias_updates.py
python3 actor_profile/scripts/sync_attack_reference.py
python3 actor_profile/scripts/enrich_activity_intelligence.py --apply
python3 actor_profile/scripts/migrate_evidence_boundaries.py --apply
python3 actor_profile/scripts/apply_primary_source_corrections.py
python3 actor_profile/scripts/enrich_targeting_scope.py --apply
python3 actor_profile/scripts/materialize_activity_diamonds.py --apply
python3 actor_profile/scripts/build_claim_audits.py
python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest
python3 actor_profile/scripts/build_tidal_activity_index.py
python3 actor_profile/scripts/build_actor_research_dossiers.py

python3 actor_profile/scripts/render_collection_index.py \
  profiles/processing-summary.json \
  actor_profile/corpus-catalog.json \
  profiles/README.md
```

生成結果に大規模な差分が出る場合は、原因となったルール変更とデータ再生成を別commitまたは
別PRに分け、レビュー可能な状態を保ちます。
