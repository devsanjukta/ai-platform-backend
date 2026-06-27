import uuid
from pathlib import Path
from typing import Dict

from app.core.chunker.text_chunker import chunk_files_text
from app.core.cleaner.cleaner_text import clean_all_text
from app.core.constants import ALLOWED_TYPES
from app.core.extractor.extractor_utility import (
    FileObject,
    extract_all_text,
)

BASE_DIR = Path(__file__).resolve().parent
RAG_FOLDER = BASE_DIR / "rag_files"


def get_all_files() -> Dict[str, FileObject]:
    if not RAG_FOLDER.exists():
        return {}

    files = {}

    for file_path in RAG_FOLDER.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in ALLOWED_TYPES:
            file_id = str(uuid.uuid4())

            files[file_id] = FileObject(
                file_id=file_id,
                file=file_path.read_bytes(),
                file_name=file_path.name,
                file_type=file_path.suffix.lower(),
            )

    return files


async def process_data_ingestion():
    files = get_all_files()
    rawFilesText = extract_all_text(files)
    cleaned_text = clean_all_text(rawFilesText)
    chunked_text = chunk_files_text(cleaned_text)
    return {"total_files": len(files), "chunked": chunked_text}
