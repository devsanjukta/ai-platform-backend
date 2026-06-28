import json
import uuid
from typing import List

from app.core.db.executor import execute_query
from app.core.embedding.embeddings import VectorRecord


async def save_vectors(vectors: List[VectorRecord]):
    query = """
    INSERT INTO knowledge_base_rag
    (id, source_id, chunk_index, content, metadata, embedding)
    VALUES ($1, $2, $3, $4, $5, $6)
    """

    for v in vectors:
        await execute_query(
            query,
            v["chunk_id"],
            v["source_id"],
            v["metadata"]["chunk_index"],
            v["text"],
            json.dumps(v["metadata"]),
            str(v["embedding"]),
        )


async def create_user(name: str, email: str):
    query = """
    INSERT INTO users (id, name, email)
    VALUES ($1, $2, $3)
    RETURNING id, name, email, created_at
    """

    user_id = str(uuid.uuid4())
    await execute_query(query, user_id, name, email)
