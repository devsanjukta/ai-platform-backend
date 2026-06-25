from fastapi import APIRouter, File, Form, UploadFile

from app.modules.summarizer.schemas import SummarizeRequest, SummarizeResponse
from app.modules.summarizer.services.summarizer_service import (
    process_summarization_request,
)

router = APIRouter(prefix="/summarizer", tags=["Summarizer"])


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    resp = await process_summarization_request(request)
    return resp
