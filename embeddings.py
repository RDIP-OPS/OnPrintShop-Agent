from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Create output folder if it doesn't exist
os.makedirs("faiss_index", exist_ok=True)

# Load all .txt files from the scraped documents folder
docs = []
input_dir = "./onprintshop_docs"
if not os.path.exists(input_dir) or not os.listdir(input_dir):
    print(f"Warning: No documents found in '{input_dir}'. Please run scraper.py first.")
else:
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        if filename.endswith(".txt"):
            print(f"Loading: {filename}")
            loader = TextLoader(filepath)
            docs.extend(loader.load())

# Split text into smaller chunks for better search results
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Create embeddings (numerical representations of text)
embeddings = OpenAIEmbeddings()

# Build FAISS index (your searchable knowledge base)
print("Building FAISS index. This might take a moment...")
db = FAISS.from_documents(chunks, embeddings)
db.save_local("faiss_index")
print("✅ Embeddings built! Your search index is ready.")
