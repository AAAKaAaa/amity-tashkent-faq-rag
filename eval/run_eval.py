"""Retrieval evaluation: does the right FAQ record come back for each test question?

Usage:  python eval/run_eval.py                 # compares faiss, bm25 and hybrid
        python eval/run_eval.py --modes hybrid --k 5

Metrics (per language and overall):
  Hit@1 / Hit@3 / Hit@5 — share of questions whose expected FAQ is in the top 1 / 3 / 5 chunks
  MRR                   — mean of 1/rank of the first correct chunk (0 if not in top k)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import rag  # noqa: E402

QUESTIONS = Path(__file__).with_name("questions.jsonl")
RESULTS = Path(__file__).with_name("results")
FAQ_ID = re.compile(r"FAQ-\d{3}")


def faq_id(doc) -> str | None:
    m = FAQ_ID.search(doc.metadata.get("question") or "") or FAQ_ID.search(doc.page_content[:80])
    return m.group(0) if m else None


def evaluate(mode: str, k: int, items: list[dict]) -> dict:
    rows = []
    for it in items:
        ids = [faq_id(d) for d, _ in rag.retrieve(it["q"], k=k, mode=mode)]
        rank = next((i + 1 for i, x in enumerate(ids) if x in it["expected"]), None)
        rows.append({**it, "retrieved": ids, "rank": rank})
    return {"mode": mode, "k": k, "rows": rows}


def summarize(rows: list[dict]) -> dict:
    n = len(rows)
    hit = lambda c: sum(1 for r in rows if r["rank"] and r["rank"] <= c) / n  # noqa: E731
    return {
        "n": n,
        "hit@1": hit(1),
        "hit@3": hit(3),
        "hit@5": hit(5),
        "mrr": sum(1 / r["rank"] for r in rows if r["rank"]) / n,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--modes", nargs="+", default=["faiss", "bm25", "hybrid"])
    ap.add_argument("--k", type=int, default=5)
    args = ap.parse_args()

    items = [json.loads(line) for line in QUESTIONS.read_text().splitlines() if line.strip()]
    langs = sorted({it["lang"] for it in items})
    report = {}
    print(f"{len(items)} questions, k={args.k}\n")
    print(f"{'mode':<8}{'lang':<6}{'n':>4}{'Hit@1':>8}{'Hit@3':>8}{'Hit@5':>8}{'MRR':>8}")
    for mode in args.modes:
        res = evaluate(mode, args.k, items)
        groups = {lang: [r for r in res["rows"] if r["lang"] == lang] for lang in langs}
        groups["all"] = res["rows"]
        report[mode] = {"summary": {g: summarize(rs) for g, rs in groups.items()}, "rows": res["rows"]}
        for g, s in report[mode]["summary"].items():
            print(
                f"{mode:<8}{g:<6}{s['n']:>4}{s['hit@1']:>8.0%}{s['hit@3']:>8.0%}"
                f"{s['hit@5']:>8.0%}{s['mrr']:>8.3f}"
            )
        misses = [r for r in res["rows"] if not r["rank"]]
        if misses:
            print(f"  misses ({len(misses)}):")
            for r in misses:
                print(f"    [{r['lang']}] {r['q']}  expected {r['expected']} got {r['retrieved'][:3]}")
        print()

    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / f"eval_{datetime.now():%Y%m%d_%H%M%S}.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"Saved {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
