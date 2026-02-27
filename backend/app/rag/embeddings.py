from langchain_ollama import OllamaEmbeddings
from app.config import settings

def get_embeddings():
    return OllamaEmbeddings(
        model=settings.EMBEDDING_MODEL,
        base_url=settings.OLLAMA_BASE_URL
    )
