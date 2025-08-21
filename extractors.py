from typing import BinaryIO


def extract_text_from_pdf(file: BinaryIO) -> str:
    """Extract text from a PDF file object using PyPDF2 if available."""
    try:
        from PyPDF2 import PdfReader  # type: ignore
    except Exception as exc:  # pragma: no cover - optional
        raise RuntimeError("PyPDF2 is required for PDF extraction") from exc

    reader = PdfReader(file)
    text = "".join(page.extract_text() or "" for page in reader.pages)
    return text.strip()


def extract_text_from_image(file: BinaryIO) -> str:
    """Extract text from an image file object using pytesseract if available."""
    try:
        from PIL import Image  # type: ignore
        import pytesseract  # type: ignore
    except Exception as exc:  # pragma: no cover - optional
        raise RuntimeError("pytesseract and Pillow are required for image OCR") from exc

    img = Image.open(file)
    return pytesseract.image_to_string(img)
