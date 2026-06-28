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


async def process_data_ingestion():
    files = get_all_files()
    rawFilesText = extract_text_from_files(files)
    cleaned_text = clean_items(rawFilesText)
    chunked_text = chunk_items(cleaned_text)
    embedding = await create_embeddings(chunked_text)
    return {"total_files": len(files), "embeddings": embedding}
