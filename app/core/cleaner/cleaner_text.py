import re
from typing import List

from app.core.models.text import TextItem


def clean_items(items: List[TextItem]) -> List[TextItem]:

    return [
        {
            "source_id": item["source_id"],
            "text": clean_text(item["text"]),
            "metadata": item.get("metadata", {}),
        }
        for item in items
    ]


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\x0c", " ", text)
    return text.strip()
