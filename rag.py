"""Retrieval + generation: FAISS retriever (LangChain) and Claude (Anthropic SDK)."""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Iterator
from functools import lru_cache

import anthropic
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

import config
from embeddings import get_embeddings

SYSTEM_PROMPT = """You are the FAQ assistant for Amity University in Tashkent (AUT), \
Uzbekistan. You help students, applicants and parents with questions about admissions, \
programmes, fees, scholarships, campus life, careers, international students and NTCC.

Answer using ONLY the information inside <context>. Each document there has an id and a \
source file name; FAQ records also carry a Status and a "Source URL / file".
- If the context answers the question, give a concise, friendly answer (short paragraphs \
or bullet points; include exact figures, dates and contacts from the context).
- Respect each record's Status. For historical or time-sensitive fees, say which year or \
page the figure comes from and that the offer letter is binding. For conflicting sources, \
give both versions and recommend confirming with the university — never silently pick one. \
For "needs-live-confirmation" or "not-publicly-confirmed" items, say the information is not \
verified and point to the official channel. Treat NTCC/G-32 records as uploaded guidance to \
confirm with the faculty supervisor.
- Facts about AUT apply only to the Tashkent campus; do not assume rules from other Amity \
campuses.
- If the context does not contain the answer, say you don't have that information and \
direct the student to info@amity.uz or +998 71 207 90 06 (or a more specific contact from \
the context). Never invent fees, dates, deadlines, rules or contacts.
- Never ask for or accept passwords or personal student records.
- At the end, add a line "Sources:" with the Source URL(s) of the records you used \
(or the file name if a record has no URL).
- Reply in the same language the user writes in (e.g. English, Russian or Uzbek). \
For Uzbek, use the Latin script. Keep proper names and abbreviations such as B.Tech, \
NTCC, CGPA and INR unchanged. If the question's language is unclear, reply in the \
interface language given with the question."""


class IndexNotFoundError(RuntimeError):
    pass


@lru_cache(maxsize=1)
def load_vectorstore() -> FAISS:
    if not (config.INDEX_DIR / "index.faiss").exists():
        raise IndexNotFoundError("FAISS index not found. Run `python ingest.py` first.")
    # The index is created locally by ingest.py, so deserialising it is safe.
    return FAISS.load_local(
        str(config.INDEX_DIR), get_embeddings(), allow_dangerous_deserialization=True
    )


_TOKEN = re.compile(r"\w+", re.UNICODE)


def tokenize(text: str) -> list[str]:
    # Uzbek Latin uses several apostrophe variants (o', oʻ, o’) — unify them first.
    text = re.sub(r"[ʻʼ’‘`']", "", text.lower())
    return _TOKEN.findall(text)


class BM25:
    """Okapi BM25 keyword index over the same chunks that FAISS holds."""

    def __init__(self, docs: list[Document], k1: float = 1.5, b: float = 0.75):
        self.docs, self.k1, self.b = docs, k1, b
        self.tfs = [Counter(tokenize(d.page_content)) for d in docs]
        self.lens = [sum(tf.values()) for tf in self.tfs]
        self.avg_len = sum(self.lens) / max(len(docs), 1)
        df = Counter(t for tf in self.tfs for t in tf)
        n = len(docs)
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}

    def search(self, query: str, k: int) -> list[tuple[Document, float]]:
        terms = [t for t in tokenize(query) if t in self.idf]
        scores = []
        for doc, tf, dl in zip(self.docs, self.tfs, self.lens):
            s = 0.0
            for t in terms:
                f = tf.get(t, 0)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (
                        f + self.k1 * (1 - self.b + self.b * dl / self.avg_len)
                    )
            scores.append(s)
        order = sorted(range(len(scores)), key=lambda i: -scores[i])[:k]
        return [(self.docs[i], scores[i]) for i in order if scores[i] > 0]


@lru_cache(maxsize=1)
def load_bm25() -> BM25:
    store = load_vectorstore()
    ids = [store.index_to_docstore_id[i] for i in range(len(store.index_to_docstore_id))]
    return BM25([store.docstore.search(i) for i in ids])


def retrieve(
    question: str, k: int = config.TOP_K, mode: str = config.RETRIEVAL_MODE
) -> list[tuple[Document, float]]:
    """Return the k best chunks with a score.

    mode="faiss":  semantic search, score = L2 distance (lower = closer)
    mode="bm25":   keyword search, score = BM25 (higher = better)
    mode="hybrid": both lists merged with Reciprocal Rank Fusion, score = RRF (higher = better)
    """
    if mode == "faiss":
        return load_vectorstore().similarity_search_with_score(question, k=k)
    if mode == "bm25":
        return load_bm25().search(question, k)
    if mode != "hybrid":
        raise ValueError(f"Unknown retrieval mode: {mode}")

    depth = max(20, 4 * k)  # look deeper in each list before fusing
    fused: dict[str, list] = {}
    rankings = (
        [d for d, _ in load_vectorstore().similarity_search_with_score(question, k=depth)],
        [d for d, _ in load_bm25().search(question, depth)],
    )
    for weight, ranked in zip((1.0, config.BM25_WEIGHT), rankings):
        for rank, doc in enumerate(ranked):
            entry = fused.setdefault(doc.page_content, [doc, 0.0])
            entry[1] += weight / (config.RRF_K + rank + 1)
    best = sorted(fused.values(), key=lambda e: -e[1])[:k]
    return [(doc, score) for doc, score in best]


def format_context(docs: list[Document]) -> str:
    return "\n".join(
        f'<document id="{i}" source="{d.metadata.get("source", "unknown")}">\n'
        f"{d.page_content}\n</document>"
        for i, d in enumerate(docs, 1)
    )


@lru_cache(maxsize=1)
def get_client() -> anthropic.Anthropic:
    return anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env / .env


def build_messages(
    question: str, docs: list[Document], history: list[dict], ui_language: str = "English"
) -> list[dict]:
    """Previous turns as plain text, then the new question with its retrieved context."""
    messages = [{"role": m["role"], "content": m["content"]} for m in history]
    messages.append(
        {
            "role": "user",
            "content": f"<context>\n{format_context(docs)}\n</context>\n\n"
            f"Interface language: {ui_language}\n\nQuestion: {question}",
        }
    )
    return messages


def stream_answer(
    question: str, docs: list[Document], history: list[dict], ui_language: str = "English"
) -> Iterator[str]:
    """Stream the answer text from Claude.

    Server-side refusal fallbacks are on: if the main model declines, the API
    re-runs the request on a fallback model within the same call.
    """
    with get_client().beta.messages.stream(
        model=config.LLM_MODEL,
        max_tokens=config.MAX_TOKENS,
        system=SYSTEM_PROMPT,
        output_config={"effort": config.LLM_EFFORT},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=build_messages(question, docs, history, ui_language),
    ) as stream:
        yield from stream.text_stream
        final = stream.get_final_message()
    if final.stop_reason == "refusal":
        yield "\n\n_Sorry, I can't help with that request._"
    elif final.stop_reason == "max_tokens":
        yield "\n\n_(answer truncated)_"
