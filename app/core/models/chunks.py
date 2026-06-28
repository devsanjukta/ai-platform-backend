from typing import TypedDict


class TextChunk(TypedDict):
    chunk_id: str
    source_id: str
    text: str
    chunk_index: int
