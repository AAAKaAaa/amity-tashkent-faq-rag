import os

import anthropic
import streamlit as st

import config
import feedback
import rag
import stt
from i18n import LANGUAGES, TEXTS
from ingest import build_index

st.set_page_config(page_title="Amity Tashkent FAQ", page_icon="🎓", layout="centered")

with st.sidebar:
    lang_name = st.selectbox("🌐 Language / Язык / Til", list(LANGUAGES), key="lang_name")
    lang = LANGUAGES[lang_name]
    T = TEXTS[lang]

    st.header(T["kb"])
    files = sorted(p.name for p in config.DATA_DIR.glob("*") if p.suffix in {".md", ".txt", ".pdf"})
    st.caption(T["docs_count"].format(n=len(files)))
    for name in files:
        st.markdown(f"- {name}")

    uploaded = st.file_uploader(T["add_docs"], type=["md", "txt", "pdf"], accept_multiple_files=True)
    if st.button(T["rebuild"], use_container_width=True) or uploaded:
        for f in uploaded or []:
            (config.DATA_DIR / f.name).write_bytes(f.getvalue())
        with st.spinner(T["embedding"]):
            n = build_index()
        rag.load_vectorstore.cache_clear()
        st.success(T["indexed"].format(n=n))

    st.divider()
    top_k = st.slider(T["top_k"], 1, 10, config.TOP_K)
    up, down = feedback.stats()
    st.caption(T["ratings"].format(up=up, down=down))
    if st.button(T["clear"], use_container_width=True):
        st.session_state.messages = []
        for key in [k for k in st.session_state if str(k).startswith("fb_")]:
            del st.session_state[key]
        st.rerun()

    has_key = bool(os.getenv("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_AUTH_TOKEN"))
    if not has_key:
        st.warning(T["no_key"])

st.title(T["title"])
st.caption(T["subtitle"])

if "messages" not in st.session_state:
    st.session_state.messages = []


def on_rate(i: int) -> None:
    rating = st.session_state.get(f"fb_{i}")
    if rating is not None:
        msgs = st.session_state.messages
        feedback.save(msgs[i - 1]["content"], msgs[i]["content"], rating, lang)
        st.toast(T["thanks"])


for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant":
            st.feedback("thumbs", key=f"fb_{i}", on_change=on_rate, args=(i,))

submitted = st.chat_input(T["placeholder"], accept_audio=True, submit_mode="disable")
question = ""
if submitted:
    question = submitted.text.strip()
    if submitted.audio and not question:
        try:
            with st.spinner(T["transcribing"]):
                question = stt.transcribe(submitted.audio.getvalue(), lang)
        except Exception as e:
            st.error(f"{T['stt_error']} {e}")
        if not question:
            st.warning(T["no_speech"])
if not st.session_state.messages and not question:
    cols = st.columns(2)
    for i, s in enumerate(T["suggestions"]):
        if cols[i % 2].button(s, use_container_width=True):
            question = s

if question:
    history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        if not has_key:
            st.error(T["no_key"])
            st.stop()
        try:
            prev_q = next((m["content"] for m in reversed(history) if m["role"] == "user"), "")
            query = f"{prev_q}\n{question}" if len(question.split()) < 6 and prev_q else question
            docs = [d for d, _ in rag.retrieve(query, k=top_k)]
            answer = st.write_stream(
                rag.stream_answer(question, docs, history[-10:], ui_language=lang_name)
            )
            st.session_state.messages += [
                {"role": "user", "content": question},
                {"role": "assistant", "content": answer},
            ]
            st.rerun()
        except rag.IndexNotFoundError as e:
            st.error(f"{e} {T['no_index']}")
        except anthropic.AuthenticationError:
            st.error(T["bad_key"])
        except anthropic.RateLimitError:
            st.error(T["rate_limit"])
        except anthropic.APIConnectionError:
            st.error(T["no_connection"])
        except anthropic.APIStatusError as e:
            st.error(f"{T['api_error']} {e.status_code}: {e.message}")
