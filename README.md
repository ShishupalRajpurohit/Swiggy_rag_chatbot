# RAG Application on Swiggy Annual Report (FY 2023–24)

## Document Source
Swiggy Limited Annual Report FY 2023–24  
Public Source: https://www.swiggy.com/about-us/

---

## Objective
Build a Retrieval-Augmented Generation (RAG) system that answers questions strictly based on the Swiggy Annual Report.

The system only responds from retrieved document context.

---

## Architecture

User Query
   ↓
FAISS Vector Search
   ↓
Top Relevant Chunks
   ↓
LLM (Groq - LLaMA 3.1 70B)
   ↓
Final Answer (Context-Grounded)

---

## Tools Used & Justification

### 1. FAISS
- Required vector database
- Fast similarity search
- Lightweight and local

### 2. HuggingFace Embeddings
- Open-source
- No paid API required
- Good semantic search performance

### 3. Groq (LLaMA 3.1 70B)
- Strong reasoning capability
- Fast inference
- Used only for answer generation

### 4. PyMuPDF
- Handles image-heavy PDFs better than basic PDF loaders

---

## Setup Instructions

1. Install dependencies


pip install -r requirements.txt


2. Create `.env` file


GROQ_API_KEY=your_groq_api_key_here


3. Build vector database


python vector_db.py


4. Run application


python app.py


---

## Functional Coverage

✔ Document Processing  
✔ Chunking  
✔ Embedding Generation  
✔ FAISS Vector Store  
✔ Semantic Retrieval  
✔ Context-Grounded Answering  
✔ CLI Interface  

---

## Limitations

- Answers only from provided PDF
- No UI (CLI only as allowed)

- No additional analytics or summarization
