"""Store 👍/👎 ratings of bot answers in feedback/feedback.jsonl (one JSON object per line)."""

from __future__ import annotations

import json
from datetime import datetime

import config

FEEDBACK_FILE = config.BASE_DIR / "feedback" / "feedback.jsonl"


def save(question: str, answer: str, rating: int, lang: str) -> None:
    """rating: 1 = 👍, 0 = 👎 (Streamlit's st.feedback("thumbs") values)."""
    FEEDBACK_FILE.parent.mkdir(exist_ok=True)
    record = {
        "time": datetime.now().isoformat(timespec="seconds"),
        "lang": lang,
        "rating": "up" if rating == 1 else "down",
        "question": question,
        "answer": answer,
    }
    with FEEDBACK_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def stats() -> tuple[int, int]:
    """(number of 👍, number of 👎) collected so far."""
    if not FEEDBACK_FILE.exists():
        return 0, 0
    ratings = [json.loads(line)["rating"] for line in FEEDBACK_FILE.read_text().splitlines() if line]
    return ratings.count("up"), ratings.count("down")
