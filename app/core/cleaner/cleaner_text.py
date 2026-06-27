import re
from typing import Dict

from app.core.models.files import FileText


def clean_all_text(extracted_files: Dict[str, FileText]) -> Dict[str, FileText]:
    cleaned: Dict[str, FileText] = {}

    for file_id, file_data in extracted_files.items():
        cleaned[file_id] = clean_single_text(file_id, file_data)

    return cleaned


def clean_single_text(file_id: str, file_data: FileText) -> FileText:
    text = file_data.get("file_text", "")

    if not text:
        return file_data

    # 1. normalize whitespace
    text = re.sub(r"\s+", " ", text)

    # 2. remove excessive spaces
    text = text.strip()

    # 3. remove common junk patterns (MVP level)
    text = re.sub(r"\x0c", " ", text)  # page breaks

    return {
        "file_id": file_id,
        "file_name": file_data.get("file_name"),
        "file_type": file_data.get("file_type"),
        "file_text": text,
    }
