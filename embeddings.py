from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings

import config


@lru_cache(maxsize=1)
def get_embeddings() -> HuggingFaceEmbeddings:
    is_e5 = "e5" in config.EMBEDDING_MODEL.lower()
    return HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True, **({"prompt": "passage: "} if is_e5 else {})},
        query_encode_kwargs={"normalize_embeddings": True, **({"prompt": "query: "} if is_e5 else {})},
    )
