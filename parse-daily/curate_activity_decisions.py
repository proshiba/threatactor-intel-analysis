#!/usr/bin/env python3
"""Create reproducible decisions for explicit actor-operated activity claims."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from daily_common import load_json, write_json_atomic


HERE = Path(__file__).resolve().parent
AUTO_REVIEW_PREFIX = "tech-memo全履歴再監査:"


def decision_for(record: dict[str, Any]) -> dict[str, Any] | None:
    claim = record.get("activity_claim", {})
    assessment = claim.get("assessment")
    if assessment not in {"strong-subject", "attributed-subject"}:
        return None
    if record.get("capability_decisions"):
        # Malware/tool names require an independent primary-source review.
        return None
    location = claim.get("match_location", "unknown")
    evidence = claim.get("evidence_text", "")
    basis = (
        "攻撃活動の実行主体として明記"
        if assessment == "strong-subject"
        else "当該活動への帰属先として明記"
    )
    return {
        "review_status": "approved",
        "confidence": claim.get("suggested_confidence", "medium"),
        "review_notes": (
            "tech-memo全履歴再監査: "
            f"{'記事タイトル' if location == 'title' else '記事要約の同一文'}で"
            f"当該アクターが{basis}されている。"
            "攻撃期間は一次資料中の明示値を別途確認できていないためunknownとし、"
            "記事公開日はreported_atとして分離する。"
            + (f" 根拠: {evidence}" if evidence else "")
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queue", type=Path)
    parser.add_argument(
        "--decisions",
        type=Path,
        default=HERE / "review-decisions.json",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write new decisions; default is an audit-only dry-run",
    )
    parser.add_argument(
        "--replace-auto",
        action="store_true",
        help="discard prior auto-curated decisions before rebuilding them",
    )
    args = parser.parse_args()

    queue = load_json(args.queue)
    decisions = load_json(args.decisions) if args.decisions.exists() else {}
    removed_auto = 0
    if args.replace_auto:
        retained = {
            key: value
            for key, value in decisions.items()
            if not value.get("review_notes", "").startswith(AUTO_REVIEW_PREFIX)
        }
        removed_auto = len(decisions) - len(retained)
        decisions = retained
    proposed: dict[str, dict[str, Any]] = {}
    skipped_existing = 0
    assessments: Counter[str] = Counter()
    for record in queue["records"]:
        claim = record.get("activity_claim", {})
        assessments[claim.get("assessment", "missing")] += 1
        key = f"{record['actor']['slug']}|{record['activity']['activity_reference']}"
        if key in decisions:
            skipped_existing += 1
            continue
        decision = decision_for(record)
        if decision:
            proposed[key] = decision

    summary = {
        "mode": "apply" if args.apply else "dry-run",
        "queue_records": len(queue["records"]),
        "claim_assessments": dict(sorted(assessments.items())),
        "existing_decisions": len(decisions),
        "removed_auto_decisions": removed_auto,
        "skipped_existing": skipped_existing,
        "proposed_decisions": len(proposed),
        "proposed_actors": len({key.split("|", 1)[0] for key in proposed}),
    }
    if args.apply:
        decisions.update(proposed)
        write_json_atomic(args.decisions, dict(sorted(decisions.items())))
        summary["written_decisions"] = len(decisions)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
