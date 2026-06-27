# from ast import Dict
from typing import Dict

from app.core.constants import ALLOWED_TYPES
from app.core.extractor.docx_extractor import extract_docx_text
from app.core.models.files import FileObject, FileText


def extract_all_text(files: Dict[str, FileObject]) -> Dict[str, FileText]:
    results: Dict[str, FileText] = {}

    for file_id, file_obj in files.items():
        results[file_id] = extract_single_file(file_obj)

    return results


def extract_single_file(file_obj: FileObject) -> FileText:
    file_type = file_obj["file_type"]

    if file_type not in ALLOWED_TYPES:
        return build_file_text(file_obj)

    if file_type == ".docx":
        text = extract_docx_text(file_obj["file"])
        return build_file_text(file_obj, text)

    return build_file_text(file_obj)


def build_file_text(file_obj: FileObject, text: str) -> FileText:
    return {
        "file_id": file_obj["file_id"],
        "file_text": text,
        "file_name": file_obj.get("file_name", ""),
        "file_type": file_obj.get("file_type", ""),
    }
