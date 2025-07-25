from fastapi import APIRouter, UploadFile, File
from ..ocr.engine import perform_ocr

router = APIRouter()

@router.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    """Perform OCR on an uploaded image"""
    content = await file.read()
    text = perform_ocr(content)
    return {"text": text}
