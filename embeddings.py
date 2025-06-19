from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv

load_dotenv()

# Load all .txt files
docs = []
for filename in os.listdir("./onprintshop_docs"):
    if filename.endswith(".txt"):
        loader = TextLoader(f"./onprintshop_docs/{filename}")
        docs.extend(loader.load())

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Create embeddings & save index
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(chunks, embeddings)
db.save_local("faiss_index")

print("✅ Embeddings built!")
