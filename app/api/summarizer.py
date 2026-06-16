from fastapi import APIRouter

from app.modules.summarizer.schemas import SummarizeRequest, SummarizeResponse
from app.modules.summarizer.services.summarizer_service import summarize_text

router = APIRouter(prefix="/summarizer", tags=["Summarizer"])


@router.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    resp = summarize_text(request)
    return resp
