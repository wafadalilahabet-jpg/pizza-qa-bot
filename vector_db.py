"""
Vector Database Setup
=====================

This module:
1. Loads restaurant reviews from CSV.
2. Embeds them using Ollama embeddings.
3. Stores them in a persistent ChromaDB vector store.
4. Exposes a retriever for semantic search.
"""

import os
import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# -------------------- Load Dataset --------------------
df = pd.read_csv("realistic_restaurant_reviews.csv")

# -------------------- Embedding Model --------------------
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# -------------------- Vector Database --------------------
db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)  # Only add docs if DB is new

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

# -------------------- Add Documents --------------------
if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        doc = Document(
            page_content=f"{row['Title']} {row['Review']}",
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        documents.append(doc)
        ids.append(str(i))

    vector_store.add_documents(documents=documents, ids=ids)
    print(" Vector DB initialized with new documents.")

# -------------------- Export Retriever --------------------
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
