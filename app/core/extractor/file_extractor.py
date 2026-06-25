from app.core.extractor.docx_extractor import DocxExtractor
from app.core.extractor.pdf_extractor import PdfExtractor
from app.modules.exceptions.file_exceptions import UnsupportedFileTypeError


class FileExtractor:
    SUPPORTED_FILE_TYPES = {"docx"}

    def __init__(self, content: bytes, filename: str):
        self.content = content
        self.filename = filename

    def __get_file_type(self) -> str:
        return self.filename.split(".")[-1].lower()

    def validate(self, file_type):
        if file_type not in self.SUPPORTED_TYPES:
            raise UnsupportedFileTypeError(f"File type '{file_type}' not supported")

        if not self.content:
            raise ValueError("Empty file content")

    async def extract(self) -> str:
        file_type = self.__get_file_type()
        self.validate(file_type)

        if file_type == "docx":
            return DocxExtractor(self.content).extract()

        elif file_type == "pdf":
            return PdfExtractor(self.content).extract()

        else:
            raise UnsupportedFileTypeError(file_type)
