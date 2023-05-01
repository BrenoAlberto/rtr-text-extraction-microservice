from src.domain.models.text_extraction.text_extractor import TextExtractor
from .pdf import PDFParser


class TextExtractorFactory:
    @staticmethod
    def create_text_extractor(file_type: str) -> TextExtractor:
        if file_type == "pdf":
            return PDFParser()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
