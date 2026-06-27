import uuid
from typing import Dict, List

from app.core.extractor.extractor_utility import FileText
from app.core.models.chunks import TextChunk


def chunk_text(
    file_id: str, text: str, chunk_size: int = 1000, overlap: int = 150
) -> List[TextChunk]:

    chunks: List[TextChunk] = []
    start = 0
    chunk_index = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(
            {
                "chunk_id": str(uuid.uuid4()),
                "file_id": file_id,
                "text": chunk,
                "chunk_index": chunk_index,
            }
        )

        chunk_index += 1
        start = end - overlap  # overlap helps context continuity

    return chunks


def chunk_files_text(cleaned_files: Dict[str, FileText]) -> List[TextChunk]:

    all_chunks: List[TextChunk] = []

    for file_id, file_data in cleaned_files.items():
        chunks = chunk_text(file_id=file_id, text=file_data["file_text"])
        all_chunks.extend(chunks)

    return all_chunks
