from typing import TypedDict


class FileObject(TypedDict):
    file_id: str
    file: bytes
    file_name: str
    file_type: str


class FileText(TypedDict):
    file_id: str
    file_text: str
    file_name: str
    file_type: str
