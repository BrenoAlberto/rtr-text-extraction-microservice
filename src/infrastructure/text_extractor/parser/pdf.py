import PyPDF2
import uuid
import base64

from src.domain.models.text_extraction.text_extractor import TextExtractor
from typing import Optional


class PDFParser(TextExtractor):
    def extract_text(self, file_base_64: str) -> Optional[str]:
        file_path = self._load_base_64_to_temp_file(file_base_64)

        try:
            with open(file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                content = []
                for page in pdf_reader.pages:
                    content.append(page.extract_text())

            return "\n".join(content)
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return None

    def _load_base_64_to_temp_file(self, file_base_64: str) -> str:
        file_path = "/tmp/" + str(uuid.uuid4()) + ".pdf"
        with open(file_path, "wb") as f:
            f.write(base64.b64decode(file_base_64))
        return file_path
