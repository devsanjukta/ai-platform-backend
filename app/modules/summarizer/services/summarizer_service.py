from app.modules.summarizer.schemas import SummarizeRequest


def summarize_text(request: SummarizeRequest):
    return {
        "message": "processed successfully",
        "data": f"Received text: {request.text}",
    }
