# app.py
# strictly answers from retrieved context

import os
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from prompt import RAG_PROMPT

load_dotenv()

DB_PATH = "faiss_index"

def load_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    return db

def main():
    db = load_db()

    # Groq chosen for fast inference and good reasoning
    llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0
    )

    while True:
        query = input("\nAsk a question (or type exit): ")

        if query.lower() == "exit":
            break

        docs = db.similarity_search(query, k=4)

        context = "\n\n".join([d.page_content for d in docs])

        final_prompt = RAG_PROMPT.format(context=context, question=query)

        response = llm.invoke(final_prompt)

        print("\nAnswer:\n", response.content)
        print("\n--- Supporting Context ---\n")
        for d in docs:
            print(d.page_content[:500])
            print("\n----------------------\n")

if __name__ == "__main__":
    main()