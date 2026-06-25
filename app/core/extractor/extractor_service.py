from app.core.extractor.file_extractor import FileExtractor


class ExtractorService:
    async def extract(self, request) -> str:
        match request.type:
            case "text":
                return request.content

            # case "file":
            #     return await self._extract_file(request.file)

            case "url":
                return await self._extract_url(request.content)

            case _:
                raise ValueError("Unsupported type")

    async def _extract_file(self, file):
        extractor = FileExtractor(file)
        return await extractor.extract()
