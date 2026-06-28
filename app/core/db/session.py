import asyncpg

from app.core.config import DATABASE_URL

pool: asyncpg.Pool | None = None


class Database:
    def __init__(self):
        self._pool: asyncpg.Pool | None = None

    async def init(self):
        self._pool = await asyncpg.create_pool(DATABASE_URL)
        print("DB POOL CREATED")

    async def close(self):
        if self._pool:
            await self._pool.close()

    def acquire(self):
        if self._pool is None:
            raise RuntimeError("DB not initialized")
        return self._pool.acquire()


db = Database()
