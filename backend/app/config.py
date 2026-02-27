from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    EMBEDDING_MODEL: str = "nomic-embed-text"
    LLM_MODEL: str = "llama3"
    CHROMA_DB_DIR: str = "data/chroma"
    UPLOAD_DIR: str = "data/uploads"

    class Config:
        env_file = ".env"

settings = Settings()

# Ensure directories exist
Path(settings.CHROMA_DB_DIR).mkdir(parents=True, exist_ok=True)
Path(settings.UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
