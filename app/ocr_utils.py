import tempfile
from surya.predict import Predictor

predictor = Predictor(device="cuda")

def ocr_image(file_path: str):
    """Run OCR on an image file."""
    return predictor.predict_image(file_path)

def ocr_pdf(file_path: str):
    """Placeholder for PDF OCR handling."""
    # TODO: split PDF into images and run ocr_image on each
    return []
