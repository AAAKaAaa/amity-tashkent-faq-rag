# 🎓 University FAQ — RAG Chatbot

A Retrieval-Augmented Generation chatbot that answers university FAQs
(admissions, fees, scholarships, academics, NTCC, hostel, placements) from your own documents.

**Stack:** Python · Streamlit (UI) · LangChain (loading, splitting, vector store) ·
FAISS (vector search) · Sentence-Transformers (`multilingual-e5-small`, local embeddings for ~100 languages incl. Uzbek) ·
Claude (`claude-opus-5-5`) via the Anthropic SDK (answer generation).

## Architecture

```
            ┌──────────── ingest.py (offline) ─────────────┐
data/*.md   │ load → split by FAQ headings → embed (e5-small)│ → faiss_index/
data/*.pdf  └──────────────────────────────────────────────┘
                                                                │
 user question ─→ embed ─→ FAISS top-k chunks ─────────────────┘
                                   │
                                   ▼
             Claude: system prompt + <context> chunks + chat history
                                   │
                                   ▼
           streamed answer + "Sources" (shown in Streamlit)
```

| File | Role |
|---|---|
| `config.py` | Settings (chunk size, top-k, model names) — overridable via `.env` |
| `ingest.py` | Loads `.md/.txt/.pdf` from `data/`, splits, embeds, saves the FAISS index |
| `embeddings.py` | Local HuggingFace embedding model (no API key, works offline) |
| `rag.py` | Retriever + prompt + streaming call to Claude |
| `app.py` | Streamlit chat UI: streaming answers, sources, document upload, index rebuild |
| `stt.py` | Voice questions: local Whisper (`whisper-large-v3-turbo`) speech-to-text |
| `i18n.py` | UI texts in English, Russian and Uzbek |
| `eval/questions.jsonl`, `eval/run_eval.py` | 60 test questions (EN/RU/UZ) and the retrieval evaluation (Hit@k, MRR) |
| `data/Amity_University_Tashkent_RAG_FAQ_Knowledge_Base_*.md` | Knowledge base: 138 FAQs about Amity University Tashkent with source URLs and status flags |
| `examples/sample_university_faq.md` | Generic sample FAQ (not indexed) |

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then put your Anthropic API key in .env
python ingest.py            # build the FAISS index (first run downloads the embedding model, ~470 MB)
streamlit run app.py
```

Open http://localhost:8501 and ask e.g. *"What is the refund policy?"* or *"Qanday stipendiyalar bor?"*

## Voice input

Click the 🎤 button in the chat box, speak, and send. The recording is transcribed locally by Whisper
(first use downloads ~1.6 GB) in the selected interface language, then answered like a typed question.
Set `STT_MODEL=openai/whisper-small` in `.env` for a smaller, faster (but less accurate) model.

## Evaluating retrieval

```bash
python eval/run_eval.py            # compares faiss, bm25 and hybrid (BM25 + FAISS, Reciprocal Rank Fusion)
```

| Retrieval | Hit@1 | Hit@3 | Hit@5 | MRR |
|---|---|---|---|---|
| FAISS, e5-small (default) | 78% | 93% | 95% | 0.857 |
| BM25 only | 37% | 52% | 60% | 0.452 |
| Hybrid, equal weights | 67% | 92% | 97% | 0.786 |
| FAISS, e5-base | 78% | 92% | 97% | 0.860 |

Semantic search alone is the default: the knowledge base has no Uzbek text, so keyword matching adds noise.
Switch with `RETRIEVAL_MODE=hybrid` in `.env`.

## Adding your own data

Drop `.md`, `.txt` or `.pdf` files into `data/` and run `python ingest.py`,
or upload them from the app sidebar (the index is rebuilt automatically).
For best retrieval, write Markdown FAQs as `### Question` headings followed by the answer —
each Q&A becomes one chunk.

## How hallucinations are limited

- The model is instructed to answer **only** from the retrieved context and to say
  "I don't have that information" otherwise, pointing to the right office.
- Every answer lists its source files, and the UI shows the retrieved chunks with their distances.
- Embeddings are multilingual, so a question in Uzbek, Russian or Hindi still finds English documents,
  and Claude replies in the user's language. The UI itself switches between English, Русский and O'zbekcha (sidebar).
