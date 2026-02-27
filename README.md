# 🚀 Chat with Docs

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
Refer to the `Perfect Repo Structure` in the design document for details.
