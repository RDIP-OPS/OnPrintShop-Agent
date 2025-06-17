from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

import os
from dotenv import load_dotenv

load_dotenv()

db = FAISS.load_local("faiss_index", OpenAIEmbeddings())
query = input("Ask a question: ")
docs = db.similarity_search(query, k=3)
for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---\n{doc.page_content[:500]}...")
