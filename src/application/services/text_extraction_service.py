from typing import Optional
from src.domain.models.text_extraction.text_extractor import TextExtractor


class TextExtractionService:
    def __init__(self, text_extractor: TextExtractor):
        self.text_extractor = text_extractor

    def extract_text(self, file_base_64: str) -> Optional[str]:
        extracted_content = self.text_extractor.extract_text(file_base_64)
        if not extracted_content:
            return None
        return extracted_content
