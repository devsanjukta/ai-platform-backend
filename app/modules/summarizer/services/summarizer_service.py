from app.modules.summarizer.llm_adapter import generate_summary
from app.modules.summarizer.schemas import SummarizeRequest


def build_prompt(text: str) -> str:
    return f"""
    Summarize this:

    TEXT:
    {text}

    """


async def summarize_text(request: SummarizeRequest):
    prompt = build_prompt(request.text)
    summary = await generate_summary(prompt)

    return {"summary": summary}
