# from ast import Dict
from typing import List

from app.core.extractor.docx_extractor import extract_docx_text
from app.core.models.files import FileObject
from app.core.models.text import TextItem


def extract_text_from_files(files: List[FileObject]) -> List[TextItem]:
    results: List[TextItem] = []

    for file_obj in files:
        results.append(extract_single_file(file_obj))

    return results


def extract_single_file(file_obj: FileObject) -> TextItem:
    file_type = file_obj["file_type"]
    source_id = file_obj["file_id"]

    text = ""

    if file_type == ".docx":
        text = extract_docx_text(file_obj["file"])

    return {
        "source_id": source_id,
        "text": text,
        "metadata": {
            "file_name": file_obj["file_name"],
            "file_type": file_obj["file_type"],
        },
    }
