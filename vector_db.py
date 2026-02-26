# vector_db.py
# builds FAISS vector DB from the Swiggy annual report PDF

import os
import fitz  # PyMuPDF (works better with image-heavy PDFs)
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()

PDF_PATH = "Annual-Report-FY-2023-24 (1).pdf"
DB_PATH = "faiss_index"

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text("text")  # simple extraction
    return text

def build_vector_db():
    print("Extracting text...")
    raw_text = extract_text_from_pdf(PDF_PATH)

    print("Chunking text...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(raw_text)

    docs = [Document(page_content=c) for c in chunks]

    # using open-source embedding model (minimal + free)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating FAISS index...")
    db = FAISS.from_documents(docs, embeddings)

    db.save_local(DB_PATH)
    print("FAISS index saved.")

def check_db():
    if os.path.exists(DB_PATH):
        print("Vector DB already exists.")
    else:
        print("Vector DB not found. Creating...")
        build_vector_db()

if __name__ == "__main__":
    check_db()