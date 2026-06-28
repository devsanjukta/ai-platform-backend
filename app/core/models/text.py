from typing import Any, Dict, TypedDict


class TextItem(TypedDict):
    source_id: str
    text: str
    metadata: Dict[str, Any]
