"""Retrieval + generation: FAISS retriever (LangChain) and Claude (Anthropic SDK)."""

from __future__ import annotations

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


def retrieve(question: str, k: int = config.TOP_K) -> list[tuple[Document, float]]:
    """Return the k most similar chunks with their L2 distance (lower = closer)."""
    return load_vectorstore().similarity_search_with_score(question, k=k)


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
