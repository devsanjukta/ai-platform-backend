from io import BytesIO

from docx import Document


class DocxExtractor:
    def __init__(self, content: bytes):
        self.content = content

    def extract(self) -> str:
        """
        Extract text from DOCX file bytes.
        """
        try:
            doc = Document(BytesIO(self.content))

            paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]

            return "\n".join(paragraphs)

        except Exception as e:
            raise ValueError(f"Failed to extract DOCX content: {str(e)}")
