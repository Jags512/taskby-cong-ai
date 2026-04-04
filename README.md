# taskby-cong-ai

# 🚀 NL2SQL System using FastAPI (Fully Open-Source)

## 📌 Overview

This project implements a **Natural Language to SQL (NL2SQL)** system that allows users to interact with a database using plain English queries — without writing SQL manually.

The system converts user input into SQL queries using a **local Large Language Model (LLM)** and executes them on a database to return results.

---

## 🎯 Objective

* Build an end-to-end NL2SQL system
* Convert natural language → SQL
* Execute queries on a database
* Return structured results via API

---

## 🏗️ Architecture

```
User (Postman )
        ↓
FastAPI Backend
        ↓
Local LLM (HuggingFace)
        ↓
SQL Query Generation
        ↓
SQLite Database
        ↓
Query Execution
        ↓
JSON Response
```

---

## 🛠️ Tech Stack

| Component     | Technology               |
| ------------- | ------------------------ |
| Backend API   | FastAPI                  |
| Database      | SQLite                   |
| LLM           | HuggingFace Transformers |
| Language      | Python                   |
| ORM           | SQLAlchemy               |
| Data Handling | Pandas                   |

---


```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/nl2sql-project.git
cd nl2sql-project
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

API will be available at:
👉 http://127.0.0.1:8000/docs

---

## 🧪 API Usage

### Endpoint:

```
POST /query
```

### Example Request:

```
/query?question=Total sales by region
```

### Example Response:

```json
{
  "question": "Total sales by region",
  "sql": "SELECT region, SUM(sales) FROM sales_data GROUP BY region;",
  "result": [
    {"region": "North", "SUM(sales)": 1000},
    {"region": "South", "SUM(sales)": 1500}
  ]
}
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE sales_data (
    region TEXT,
    sales INTEGER
);
```

---

## 🤖 LLM Model Details

This project uses a **local HuggingFace model** for SQL generation.

### Example Models:

* `mistralai/Mistral-7B-Instruct`
* `google/flan-t5-base` (lightweight option)

### Prompt Strategy:

* Provide schema context
* Instruct model to return only SQL
* Use deterministic settings (temperature = 0)

---

## 🔄 Workflow

1. User sends a natural language query
2. Backend sends prompt to LLM
3. LLM generates SQL query
4. SQL is executed using SQLAlchemy
5. Results are returned as JSON

---

#

## ⭐ Key Features

* Fully working NL2SQL system
* No OpenAI / No Groq (100% free)
* FastAPI-based REST API
* Real database execution
* Modular and scalable design

---

## 📦 requirements.txt

```
fastapi
uvicorn
transformers
torch
sqlalchemy
pandas
```

---



---

## 💡 Conclusion

This project demonstrates how Natural Language Processing and Large Language Models can be integrated with backend systems to create intuitive data query interfaces. It eliminates the need for SQL knowledge and enables users to interact with databases seamlessly.

---
