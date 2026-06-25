from app.core.extractor.extractor_service import ExtractorService
from app.modules.summarizer.llm_adapter import generate_summary
from app.modules.summarizer.schemas import SummarizeRequest


def build_prompt(text: str) -> str:
    return f"""
    Summarize this:

    TEXT:
    {text}

    """


async def process_summarization_request(request: SummarizeRequest):
    extractorService = ExtractorService()
    text = await extractorService.extract(request)

    prompt = build_prompt(text)
    summary = await generate_summary(prompt)

    return {"summary": summary}
