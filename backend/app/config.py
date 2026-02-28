from pydantic_settings import BaseSettings
from pathlib import Path
from pydantic import model_validator

class Settings(BaseSettings):
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    EMBEDDING_MODEL: str = "nomic-embed-text"
    LLM_MODEL: str = "llama3"
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150
    
    # These can be relative in .env, but we will force them to be absolute
    CHROMA_DB_DIR: str = "data/chroma"
    UPLOAD_DIR: str = "data/uploads"

    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    class Config:
        env_file = str(Path(__file__).resolve().parent.parent.parent / ".env")

    @model_validator(mode='after')
    def force_absolute_paths(self):
        # If the path is relative, make it absolute starting from BASE_DIR
        chroma_path = Path(self.CHROMA_DB_DIR)
        if not chroma_path.is_absolute():
            self.CHROMA_DB_DIR = str(self.BASE_DIR / chroma_path)
            
        upload_path = Path(self.UPLOAD_DIR)
        if not upload_path.is_absolute():
            self.UPLOAD_DIR = str(self.BASE_DIR / upload_path)
            
        return self

settings = Settings()

# Ensure directories exist
Path(settings.CHROMA_DB_DIR).mkdir(parents=True, exist_ok=True)
Path(settings.UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
