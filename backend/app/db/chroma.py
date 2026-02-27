import chromadb
from app.config import settings

client = chromadb.PersistentClient(path=settings.CHROMA_DB_DIR)

def get_collection(name="documents"):
    return client.get_or_create_collection(name=name)
