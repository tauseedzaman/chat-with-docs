from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from app.rag.embeddings import get_embeddings
from app.config import settings
import os

def ingest_document(file_path: str):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path, encoding="utf-8")
    
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap= 150
    )
    splits = text_splitter.split_documents(documents)
    
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=get_embeddings(),
        persist_directory=settings.CHROMA_DB_DIR
    )
    return vectorstore
