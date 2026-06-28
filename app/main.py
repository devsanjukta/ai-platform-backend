from fastapi import FastAPI

from app.api.router import api_router
from app.core.db.session import db

app = FastAPI(title="AI Platform Backend", version="1.0.0")

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    print("STARTUP CALLED")  # 👈 add this
    await db.init()


@app.on_event("shutdown")
async def shutdown():
    await db.close()
