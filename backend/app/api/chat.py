from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.rag.retriever import get_rag_components
import os
import json
import asyncio

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        retriever, prompt, llm = get_rag_components()
        
        # 1. Get documents first for sources
        docs = await retriever.ainvoke(request.message)
        
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

        # 2. Prepare context for the prompt
        context_text = "\n\n".join(doc.page_content for doc in docs)
        
        async def event_generator():
            # Send sources first
            yield json.dumps({"sources": sources_list}) + "\n"
            
            # Send answer tokens
            chain = prompt | llm
            async for chunk in chain.astream({"input": request.message, "context": context_text}):
                # Extract text from the chunk (depends on LLM type, but StrOutputParser or direct access work)
                content = chunk.content if hasattr(chunk, 'content') else str(chunk)
                if content:
                    yield json.dumps({"answer": content}) + "\n"

        return StreamingResponse(event_generator(), media_type="application/x-ndjson")
        
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
