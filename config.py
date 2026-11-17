"""Central settings for the University FAQ RAG chatbot."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
INDEX_DIR = BASE_DIR / "faiss_index"

# Chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 800))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 120))

# Retrieval
TOP_K = int(os.getenv("TOP_K", 5))
# "faiss" won the evaluation (eval/run_eval.py): BM25 adds noise because the KB has
# no Uzbek text and the multilingual embeddings already match paraphrases well.
RETRIEVAL_MODE = os.getenv("RETRIEVAL_MODE", "faiss")  # faiss | bm25 | hybrid
RRF_K = int(os.getenv("RRF_K", 60))  # Reciprocal Rank Fusion constant
BM25_WEIGHT = float(os.getenv("BM25_WEIGHT", 1.0))  # keyword list weight vs semantic (1.0)

# Local embedding model (runs on CPU, no API key needed).
# Multilingual (~100 languages incl. Uzbek, Russian, Hindi), so a question in any of
# them still matches English documents.
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-small")

# Speech-to-text for voice questions (local Whisper; supports English, Russian, Uzbek).
# Smaller/faster alternative: openai/whisper-small (weaker on Uzbek).
STT_MODEL = os.getenv("STT_MODEL", "openai/whisper-large-v3-turbo")

# LLM
LLM_MODEL = os.getenv("LLM_MODEL", "claude-opus-5-5")
LLM_EFFORT = os.getenv("LLM_EFFORT", "low")  # low | medium | high — FAQ answers need little reasoning
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 16000))
