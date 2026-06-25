from typing import Optional

from pydantic import BaseModel
from typing_extensions import Literal


class SummarizeRequest(BaseModel):
    type: Literal["text", "file", "url"]
    content: str | None = None
    file: str | None = None


class SummarizeResponse(BaseModel):
    summary: str
