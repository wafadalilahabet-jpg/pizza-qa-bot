# Pizza Restaurant Q&A Bot

This project demonstrates how to build a simple LLM-powered Q&A bot for a pizza restaurant.  
It uses LangChain + Ollama for the language model and ChromaDB for vector search.

---

## Features
- Loads realistic restaurant reviews from CSV
- Embeds reviews with Ollama embeddings (`mxbai-embed-large`)
- Stores embeddings in ChromaDB (persistent vector DB)
- Provides a chat loop where users can ask restaurant-related questions
- Retrieves and uses relevant reviews to answer

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/pizza-qa-bot.git
cd pizza-qa-bot
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
# Activate on Linux/Mac
source venv/bin/activate
# Activate on Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pandas langchain langchain-community langchain-ollama langchain-chroma ollama
```

### 4. Run Ollama and pull required models
Make sure [Ollama](https://ollama.com/) is installed and running, then pull the models:
```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

---

## Usage

Run the main script:
```bash
python main.py
```

Inside `main.py`, the program will:
- Load the retriever from `vector_db.py`
- Take your input question
- Retrieve the most relevant reviews from the dataset
- Pass reviews + question into the LLM
- Print the generated answer

### Example Session
```text
------------------------------------------------
Ask your question (q to quit): Do customers like the pizza crust?
------------------------------------------------

Answer: Most reviews mention that the crust is crispy on the outside and soft on the inside, which customers really enjoy.
```

---

## Project Structure
```
pizza-qa-bot/
│── main.py                     # Chat loop with LangChain + Ollama
│── vector_db.py                # Vector DB setup with Chroma
│── realistic_restaurant_reviews.csv  # Dataset of restaurant reviews
│── requirements.txt            # Python dependencies
│── README.md                   # Project documentation
│── .gitignore                  # Ignore env/cache files
│── chroma_langchain_db/        # Vector DB (auto-created)
```

---

## Requirements
- Python 3.10+
- [Ollama](https://ollama.com/) installed locally
- LangChain ecosystem packages
- ChromaDB

---

## Example CSV Format
The `realistic_restaurant_reviews.csv` file should have the following columns:
```csv
Title,Review,Rating,Date
"Great Crust","The pizza crust was crispy and perfect.",5,"2023-07-10"
"Too Salty","The pizza was too salty for my taste.",2,"2023-07-12"
```

---

## Customization
- Replace `realistic_restaurant_reviews.csv` with your own dataset of reviews.
- Change the model names in `vector_db.py` and `main.py` to use different embedding or language models.
- Adjust the retriever parameters in `vector_db.py` to return more or fewer relevant reviews.
