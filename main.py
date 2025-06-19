from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Load FAISS index once at startup
embeddings = OpenAIEmbeddings()
db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Request schema
class QueryRequest(BaseModel):
    question: str
    k: int = 3  # default top K results

# POST endpoint for your RAG
@app.post("/query")
def query_index(request: QueryRequest):
    try:
        docs = db.similarity_search(request.question, k=request.k)
        results = [doc.page_content for doc in docs]
        return {"question": request.question, "answers": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check
@app.get("/")
def read_root():
    return {"message": "OnPrintShop AI Agent is up!"}
