# 🚀 Chat with Docs

<img width="1080" height="601" alt="image" src="https://github.com/user-attachments/assets/1622bf67-69c6-4840-aff8-8a1551776a96" />

A local-first RAG chatbot. Upload documents and ask questions grounded in your data.

## 🛠️ Stack
- **FastAPI** (Backend)
- **LangChain** (RAG Framework)
- **ChromaDB** (Vector Database)
- **Ollama** (Local LLM & Embeddings)
- **Vanilla HTML/CSS/JS** (Frontend)

## ⚙️ Prerequisites
1. **Ollama** installed and running.
2. Pull required models:
   ```bash
   ollama pull llama3
   ollama pull nomic-embed-text
   ```

## 🚀 Getting Started

### 1. Setup Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### 2. Run Frontend
Simply open `frontend/simple-chat-ui.html` in your browser.

## 📂 Project Structure
- `backend/`: FastAPI application.
- `data/`: Local storage for ChromaDB and uploads (Git-ignored).
- `examples/sample_docs/`: Sample documents for testing.
- `frontend/`: Simple web UI.

## 📄 Sample Documents
We've included sample documents to help you test the RAG flow immediately:
- `examples/sample_docs/project-overview.txt`: A summary of this project.
- `examples/sample_docs/tauseed-info.txt`: Information about the creator.

Simply upload these files through the UI to start chatting!
