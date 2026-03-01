from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.rag.retriever import get_rag_chain
import os

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        rag_chain = get_rag_chain()
        result = rag_chain.invoke(request.message)
        answer = result.get("answer", "")
        docs = result.get("raw_context", [])
        
        sources_list = []
        seen_sources = set()
        
        for doc in docs:
            source_name = os.path.basename(doc.metadata.get("source", "Unknown"))
            page = doc.metadata.get("page")
            chunk = doc.metadata.get("chunk")
            
            source_label = source_name
            if page is not None:
                source_label += f" (page {page + 1})"
            elif chunk is not None:
                source_label += f" (chunk {chunk})"
            
            if source_label not in seen_sources:
                sources_list.append(source_label)
                seen_sources.add(source_label)
        
        return {
            "answer": answer,
            "sources": sources_list
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
