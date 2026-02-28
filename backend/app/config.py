from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    EMBEDDING_MODEL: str = "nomic-embed-text"
    LLM_MODEL: str = "llama3"
    
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    CHROMA_DB_DIR: str = str(BASE_DIR / "data" / "chroma")
    UPLOAD_DIR: str = str(BASE_DIR / "data" / "uploads")

    class Config:
        env_file = str(Path(__file__).resolve().parent.parent.parent / ".env")

settings = Settings()

# Ensure directories exist
Path(settings.CHROMA_DB_DIR).mkdir(parents=True, exist_ok=True)
Path(settings.UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
