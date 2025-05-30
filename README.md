# RAG with Ollama Integration

A Retrieval-Augmented Generation (RAG) system that combines vector similarity search with Ollama's local LLM capabilities. This project uses PostgreSQL with pgvector for document storage and retrieval, FastAPI for the RAG API, and Go for the proxy server.

## 🏗️ Architecture

```
Client Request → Go Proxy Server → FastAPI RAG API → PostgreSQL (pgvector)
                      ↓
               Ollama LLM (llama3.2)
```

## 🚀 Features

   - Vector Database: PostgreSQL with pgvector extension for semantic document search
   - Multilingual Support: Uses BAAI/bge-m3 embeddings model (supports Thai and English)
   - Local LLM: Ollama integration with llama3.2 model
   - API Gateway: Go-based proxy server with API key authentication
   - FastAPI Backend: High-performance Python API for RAG operations
   - Docker Support: Containerized deployment with docker-compose

## 📋 Prerequisites

   - Docker and Docker Compose
   - Ollama installed and running
   - Python 3.12+ (for local development)
   - Go 1.19+ (for local development)

## 🛠️ Installation

## 1. Clone the Repository

```
git clone https://github.com/Nuttapong14/ollama-rag.git
cd ollama-rag
```

## 2. Install Ollama and Pull Model

```
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the required model
ollama pull llama3.2
```

## 3. Start Ollama Service

```
ollama serve
```

## 🗂️ Project Structure

```
ollama-rag/
├── requirements.txt            # Python dependencies
├── rag_api.py                 # FastAPI RAG service
├── main.go                    # Go proxy server
├── insert_document.py         # Document insertion script
├── ollama.ipynb              # Jupyter notebook for testing
└── README.md                 # This file
```

## 🔧 Configuration

## Database Configuration

    - Database: vector-db
    - User: admin
    - Password: 1234
    - Host: localhost
    - Port: 5433

## API Configuration

    - RAG API: http://localhost:8000
    - Proxy Server: http://localhost:8080
    - Ollama: http://localhost:11434
    - API Key: demo

## 📝 Usage

## 1. Initialize Database and Insert Documents

First, run the document insertion script to populate your vector database:

```
python insert_document.py
```

This will insert sample Thai documents into the database with their embeddings.

## 2. Using the RAG API

Direct API Call

```
curl -X POST "http://localhost:8000/rag" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "message": "ตอน 9 โมงเช้าจะมีอะไรเกิดขึ้น"
  }'
```

Through Proxy Server (with API Key)

```
curl -X POST "http://localhost:8080/rag" \
  -H "Authorization: Bearer demo" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "message": "อาหารไทยที่อร่อยที่สุดคืออะไร"
  }'
```