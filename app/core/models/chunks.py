from typing import TypedDict


class TextChunk(TypedDict):
    chunk_id: str
    file_id: str
    text: str
    chunk_index: int
