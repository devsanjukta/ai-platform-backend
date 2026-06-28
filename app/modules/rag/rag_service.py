import uuid
from pathlib import Path
from typing import Dict, List

from app.core.chunker.text_chunker import chunk_items
from app.core.cleaner.cleaner_text import clean_items
from app.core.constants import ALLOWED_TYPES
from app.core.embedding.embeddings import create_embeddings
from app.core.extractor.extractor_utility import (
    FileObject,
    extract_text_from_files,
)
from app.modules.rag.pipelines.store_embeddings import create_user, save_vectors
from app.modules.rag.rag_schemas import IngestResponse

BASE_DIR = Path(__file__).resolve().parent
RAG_FOLDER = BASE_DIR / "rag_files"


def get_all_files() -> List[FileObject]:
    if not RAG_FOLDER.exists():
        return []

    files: List[FileObject] = []

    for file_path in RAG_FOLDER.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in ALLOWED_TYPES:
            file_id = str(uuid.uuid4())

            files.append(
                FileObject(
                    file_id=file_id,
                    file=file_path.read_bytes(),
                    file_name=file_path.name,
                    file_type=file_path.suffix.lower(),
                )
            )

    return files


async def process_data_ingestion() -> IngestResponse:
    files = get_all_files()
    raw_text = extract_text_from_files(files)
    cleaned = clean_items(raw_text)
    chunks = chunk_items(cleaned)
    vectors = await create_embeddings(chunks)
    await save_vectors(vectors)

    return {
        "total_files": len(files),
    }
