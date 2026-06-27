from fastapi import APIRouter

from app.api.rag_router import router as rag_router
from app.api.summarizer_router import router as summarizer_router

api_router = APIRouter()

api_router.include_router(summarizer_router)
api_router.include_router(rag_router)
