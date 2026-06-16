from fastapi import APIRouter

from app.api.summarizer import router as summarizer_router

api_router = APIRouter()

api_router.include_router(summarizer_router)
