from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import tempfile
import os

from .database import SessionLocal, engine, Base
from .models import Run, InputFile
from .schemas import RunResponse
from .ocr_utils import ocr_image, ocr_pdf
from .report_pdf import generate_pdf

Base.metadata.create_all(bind=engine)

app = FastAPI(title="OCR Service")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "OCR service is running"}


@app.post("/ocr/text", response_model=RunResponse)
async def ocr_text(file: UploadFile = File(...), db: Session = Depends(get_db)):
    temp = tempfile.NamedTemporaryFile(delete=False)
    try:
        content = await file.read()
        temp.write(content)
        temp.close()
        result = ocr_image(temp.name)
        run = Run(
            client_ip="local",
            filename=file.filename,
            file_size=len(content),
            file_format=file.content_type or "unknown",
            endpoint="/ocr/text",
            status=200,
        )
        db.add(run)
        db.commit()
        db.refresh(run)
        db.add(InputFile(run_id=run.run_id, file_data=content))
        db.commit()
        return RunResponse(run_id=run.run_id, text=result.get("text", ""))
    finally:
        os.unlink(temp.name)


@app.post("/ocr/pdf")
async def ocr_to_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    temp = tempfile.NamedTemporaryFile(delete=False)
    output = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    try:
        content = await file.read()
        temp.write(content)
        temp.close()
        result = ocr_image(temp.name)
        generate_pdf(result.get("boxes", []), output.name)
        run = Run(
            client_ip="local",
            filename=file.filename,
            file_size=len(content),
            file_format=file.content_type or "unknown",
            endpoint="/ocr/pdf",
            status=200,
        )
        db.add(run)
        db.commit()
        db.refresh(run)
        db.add(InputFile(run_id=run.run_id, file_data=content))
        db.commit()
        return FileResponse(output.name, filename="result.pdf")
    finally:
        os.unlink(temp.name)
        os.unlink(output.name)
