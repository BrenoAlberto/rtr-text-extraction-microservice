import pytest
from unittest.mock import Mock
from src.domain.models.text_extraction.text_extractor import TextExtractor
from src.application.services.text_extraction_service import TextExtractionService


@pytest.fixture
def text_extraction_service():
    text_extractor = Mock(spec=TextExtractor)
    return TextExtractionService(text_extractor)


def test_extract_text_returns_extracted_content(text_extraction_service):
    file_base_64 = "some_base_64_encoded_file"
    expected_extracted_content = "Sample extracted content"

    text_extraction_service.text_extractor.extract_text.return_value = (
        expected_extracted_content
    )

    result = text_extraction_service.extract_text(file_base_64)
    text_extraction_service.text_extractor.extract_text.assert_called_with(file_base_64)
    assert result == expected_extracted_content


def test_extract_text_returns_none_when_no_content(text_extraction_service):
    file_base_64 = "some_base_64_encoded_file"

    text_extraction_service.text_extractor.extract_text.return_value = None

    result = text_extraction_service.extract_text(file_base_64)
    text_extraction_service.text_extractor.extract_text.assert_called_with(file_base_64)
    assert result is None
