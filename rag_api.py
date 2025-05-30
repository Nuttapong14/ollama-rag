from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import numpy as np
from sentence_transformers import SentenceTransformer
import requests
import json

app = FastAPI()

embedder = SentenceTransformer("BAAI/bge-m3", device="cpu")

conn = psycopg2.connect(
    dbname="vector-db",
    user="admin",
    password="1234",
    host="localhost",
    port="5433"
)

class RAGRequest(BaseModel):
    user_id: str
    message: str

@app.post("/rag")
def rag(req: RAGRequest):
    embedding = embedder.encode(req.message).tolist()

    context = retrieve_similar_context(embedding)

    prompt = f"Context:\n{context}\n\nUser: {req.message}\nAssistant:"

    answer = generate_with_ollama(prompt)

    return {"response": answer.strip()}

def retrieve_similar_context(query_vector, top_k=3) -> str:
    cur = conn.cursor()

    sql_query = """
    SELECT content, embedding <=> %s::vector AS similarity_score from documents
    ORDER BY similarity_score ASC LIMIT %s;
    """

    cur.execute(sql_query, (json.dumps(query_vector), top_k))

    rows = cur.fetchall()
    return "\n---\n".join([row[0] for row in rows])

def generate_with_ollama(prompt: str) -> str:
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )
    return res.json().get("response", "[No response]")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
