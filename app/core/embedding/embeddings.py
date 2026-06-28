from typing import Any, Dict, List

from pydantic import BaseModel

from app.core.clients.openai_client import get_embedding
from app.core.models.chunks import TextChunk


class VectorRecord(BaseModel):
    chunk_id: str
    source_id: str
    text: str
    embedding: List[float]
    metadata: Dict[str, Any] = {}


async def create_embeddings(chunks: List[TextChunk]) -> List[VectorRecord]:

    texts = [chunk["text"] for chunk in chunks]

    embeddings = await get_embedding(texts)

    results: List[VectorRecord] = []

    for chunk, emb in zip(chunks, embeddings):
        results.append(
            {
                "chunk_id": chunk["chunk_id"],
                "source_id": chunk["source_id"],
                "embedding": emb.embedding,
                "text": chunk["text"],
                "metadata": {"chunk_index": chunk["chunk_index"]},
            }
        )

    return results
