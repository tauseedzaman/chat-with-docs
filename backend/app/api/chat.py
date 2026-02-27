from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.rag.retriever import get_rag_chain

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        rag_chain = get_rag_chain()
        response = rag_chain.invoke({"input": request.message})
        return {"answer": response["answer"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
