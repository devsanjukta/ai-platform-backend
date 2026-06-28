from app.core.db.session import db


async def execute_query(query: str, *args):
    async with db.acquire() as conn:
        return await conn.fetch(query, *args)
