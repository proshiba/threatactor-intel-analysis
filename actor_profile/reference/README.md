# Reference data

`attack-index.json` is the compact MITRE Enterprise ATT&CK reference used to
normalize actor mappings, software, technique IDs, names, and tactics.

To refresh it, temporarily download `enterprise-attack.json` from:

```text
https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json
```

Then run `scripts/build_attack_reference.py` and remove the large downloaded
bundle. The source version is embedded in `attack-index.json`.

## OSINT snapshots

`osint/` contains immutable-at-analysis-time snapshots used by
`scripts/crosscheck_all_actors.py`. `osint/dataset-manifest.json` records the
source URL, upstream version when present, retrieval time, entry count, and
SHA-256 for every dataset.

Aggregation datasets are discovery and cross-check sources. Their aliases,
countries, and `similar` edges are not automatically promoted into canonical
profile assertions without reviewing the linked original reporting.
