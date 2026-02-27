from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload, chat
from app.config import settings

app = FastAPI(title="Chat with Docs API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, tags=["Upload"])
app.include_router(chat.router, tags=["Chat"])

@app.get("/")
async def root():
    return {"message": "Welcome to Chat with Docs API"}
