import uuid
from typing import List

from app.core.models.chunks import TextChunk
from app.core.models.text import TextItem


def chunk_text(
    source_id: str, text: str, chunk_size: int = 1000, overlap: int = 150
) -> List[TextChunk]:
    if not text:
        return []

    overlap = min(overlap, chunk_size - 1)

    chunks: List[TextChunk] = []
    start = 0
    chunk_index = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(
            {
                "chunk_id": str(uuid.uuid4()),
                "source_id": source_id,
                "text": chunk,
                "chunk_index": chunk_index,
            }
        )

        chunk_index += 1
        start = end - overlap

    return chunks


def chunk_items(items: List[TextItem]) -> List[TextChunk]:
    all_chunks: List[TextChunk] = []

    for item in items:
        chunks = chunk_text(source_id=item["source_id"], text=item["text"])
        all_chunks.extend(chunks)

    return all_chunks
