from fastapi import APIRouter, UploadFile, File, HTTPException
from app.rag.ingest import ingest_document
from app.config import settings
from typing import List
import shutil
import os

router = APIRouter()

@router.post("/upload")
async def upload_documents(files: List[UploadFile] = File(...)):
    results = []
    
    for file in files:
        if not file.filename.endswith((".pdf", ".txt")):
            continue
            
        file_path = os.path.join(settings.UPLOAD_DIR, file.filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        try:
            ingest_document(file_path)
            results.append({"filename": file.filename, "status": "Injected successfully"})
        except Exception as e:
            results.append({"filename": file.filename, "status": f"Error: {str(e)}"})
            
    if not results:
        raise HTTPException(status_code=400, detail="No valid PDF or TXT files were provided.")
        
    return results
