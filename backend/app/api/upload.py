from fastapi import APIRouter, UploadFile, File, HTTPException
from app.rag.ingest import ingest_document
from app.config import settings
import shutil
import os

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".txt")):
        raise HTTPException(status_code=400, detail="Only PDF and TXT files are supported.")
    
    file_path = os.path.join(settings.UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        ingest_document(file_path)
        return {"filename": file.filename, "status": "Injected successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
