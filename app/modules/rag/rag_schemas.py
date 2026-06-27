from openai import BaseModel


class IngestResponse(BaseModel):
    total_files: int
