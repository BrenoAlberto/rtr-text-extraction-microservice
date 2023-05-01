import json
from src.application.services.text_extraction_service import TextExtractionService
from src.infrastructure.text_extractor.parser.factory import TextExtractorFactory


def extract_text_handler(event, context):
    body = json.loads(event["body"])
    file_base_64 = body.get("fileBase64")
    file_type = body.get("fileType")

    text_extractor = TextExtractorFactory.create_text_extractor(file_type)
    text_extraction_service = TextExtractionService(text_extractor)

    extracted_content = text_extraction_service.extract_text(file_base_64)

    if not extracted_content:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Text extraction failed."}),
        }

    return {"statusCode": 200, "body": json.dumps({"content": extracted_content})}

