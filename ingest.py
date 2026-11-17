"""Build the FAISS vector index from documents in data/.

Usage:
    python ingest.py            # index everything in data/
"""

from __future__ import annotations

from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

import config
from embeddings import get_embeddings

SUPPORTED = {".md", ".txt", ".pdf"}


def load_documents(data_dir: Path = config.DATA_DIR) -> list[Document]:
    """Load .md / .txt / .pdf files into LangChain Documents."""
    docs: list[Document] = []
    for path in sorted(data_dir.rglob("*")):
        if path.suffix.lower() not in SUPPORTED or not path.is_file():
            continue
        if path.suffix.lower() == ".pdf":
            from langchain_community.document_loaders import PyPDFLoader

            for page in PyPDFLoader(str(path)).load():
                page.metadata["source"] = path.name
                docs.append(page)
        else:
            text = path.read_text(encoding="utf-8")
            docs.append(Document(page_content=text, metadata={"source": path.name}))
    return docs


def split_documents(docs: list[Document]) -> list[Document]:
    """Split Markdown by headings first (one FAQ = one chunk), then by size."""
    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "h1"), ("##", "section"), ("###", "question")],
        strip_headers=False,
    )
    size_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP
    )

    chunks: list[Document] = []
    for doc in docs:
        if doc.metadata["source"].endswith(".md"):
            parts = md_splitter.split_text(doc.page_content)
            for p in parts:
                p.metadata = {**doc.metadata, **p.metadata}
        else:
            parts = [doc]
        chunks.extend(size_splitter.split_documents(parts))
    return [c for c in chunks if c.page_content.strip()]


def build_index() -> int:
    docs = load_documents()
    if not docs:
        raise SystemExit(f"No documents found in {config.DATA_DIR}")
    chunks = split_documents(docs)
    store = FAISS.from_documents(chunks, get_embeddings())
    store.save_local(str(config.INDEX_DIR))
    return len(chunks)


if __name__ == "__main__":
    n = build_index()
    print(f"Indexed {n} chunks -> {config.INDEX_DIR}")
