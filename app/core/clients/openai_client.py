from dotenv import load_dotenv
from openai import AsyncOpenAI

from app.core.config import OPENAI_API_KEY

load_dotenv()

client = AsyncOpenAI(api_key=OPENAI_API_KEY)


async def get_embedding(text: list[str]) -> list[list[float]]:
    response = await client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )
    return response.data
