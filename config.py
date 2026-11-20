import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
INDEX_DIR = BASE_DIR / "faiss_index"

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 800))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 120))

TOP_K = int(os.getenv("TOP_K", 5))
RETRIEVAL_MODE = os.getenv("RETRIEVAL_MODE", "faiss")
RRF_K = int(os.getenv("RRF_K", 60))
BM25_WEIGHT = float(os.getenv("BM25_WEIGHT", 1.0))

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-small")

STT_MODEL = os.getenv("STT_MODEL", "openai/whisper-large-v3-turbo")

LLM_MODEL = os.getenv("LLM_MODEL", "claude-opus-5-5")
LLM_EFFORT = os.getenv("LLM_EFFORT", "low")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 16000))
