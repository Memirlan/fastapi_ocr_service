import io
from PIL import Image
try:
    import pytesseract
except ImportError:  # pragma: no cover - if pytesseract isn't installed
    pytesseract = None

def perform_ocr(image_bytes: bytes) -> str:
    """Simple OCR using pytesseract.

    Parameters
    ----------
    image_bytes : bytes
        Image data in bytes.
    Returns
    -------
    str
        Recognized text.
    """
    if pytesseract is None:
        return "OCR engine not installed"
    image = Image.open(io.BytesIO(image_bytes))
    return pytesseract.image_to_string(image)
