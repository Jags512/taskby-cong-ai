# 🚀 NL2SQL System using FastAPI (No OpenAI / No Groq)

## 📌 Overview
This project is a **Natural Language to SQL (NL2SQL)** system that allows users to query a database using plain English.

Users can ask questions like:
> "Show total sales by region"

And the system will:
1. Convert the question into SQL
2. Execute it on a database
3. Return the result

---

## 🏗️ Architecture

User → FastAPI → Local LLM (HuggingFace) → SQL → Database → Result

---

## 🛠️ Tech Stack

- **Backend:** FastAPI  
- **Database:** SQLite  
- **LLM:** HuggingFace Transformers (Mistral / FLAN-T5)  
- **Language:** Python  
- **ORM:** SQLAlchemy  

---

