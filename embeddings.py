"""Local embedding model shared by ingest.py and rag.py."""

from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings

import config


@lru_cache(maxsize=1)
def get_embeddings() -> HuggingFaceEmbeddings:
    # multilingual-e5 models expect "query: " / "passage: " prefixes.
    is_e5 = "e5" in config.EMBEDDING_MODEL.lower()
    # normalize_embeddings=True makes FAISS L2 distance equivalent to cosine similarity.
    return HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True, **({"prompt": "passage: "} if is_e5 else {})},
        query_encode_kwargs={"normalize_embeddings": True, **({"prompt": "query: "} if is_e5 else {})},
    )
