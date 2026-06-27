from fastapi import APIRouter

from app.modules.rag.rag_schemas import IngestResponse
from app.modules.rag.rag_service import process_data_ingestion

router = APIRouter(prefix="/rag", tags=["RAG"])


@router.post("/ingest", response_model=IngestResponse)
async def summarize():
    resp = await process_data_ingestion()
    return resp
