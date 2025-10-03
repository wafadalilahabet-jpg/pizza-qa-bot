"""
Pizza Restaurant Q&A Bot
========================

This script:
1. Loads a retriever from vector_db.py.
2. Uses LangChain + Ollama LLM to answer questions.
3. Pulls relevant reviews from the vector store.
4. Provides conversational Q&A about the restaurant.
"""

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from vector_db import retriever  # import retriever from vector_db.py

# -------------------- Model --------------------
model = Ollama(model="llama3.2")

# -------------------- Prompt --------------------
template = """
You are an expert at answering questions about a pizza restaurant.

Here are some relevant reviews:
{reviews}

Here is the question to answer:
{question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Build chain
chain = prompt | model

# -------------------- Chat Loop --------------------
def run_chat():
    """Run interactive Q&A loop."""
    while True:
        print("\n------------------------------------------------")
        question = input("Ask your question (q to quit): ")
        print("------------------------------------------------\n")

        if question.lower() == "q":
            print("Goodbye!")
            break

        # Get relevant reviews
        docs = retriever.invoke(question)
        reviews = "\n".join([doc.page_content for doc in docs])

        # Run chain
        result = chain.invoke({"reviews": reviews, "question": question})
        print("Answer:", result)


if __name__ == "__main__":
    run_chat()
