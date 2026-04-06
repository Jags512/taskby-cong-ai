# 🚀 AI-Powered NL2SQL System (Vanna 2.0 + FastAPI)

## 📌 Project Overview

This project is a **Natural Language to SQL (NL2SQL) system** built using **Vanna AI 2.0** and **FastAPI**.

It allows users to ask questions in plain English and automatically:

* Generate SQL queries
* Execute them on a database
* Return results with summary and visualization

---

## 🎯 Assignment Objective

* Build an end-to-end NL2SQL system
* Use **Vanna 2.0 Agent architecture (NOT Vanna 0.x)**
* Integrate an LLM (Gemini / Groq / Ollama)
* Implement SQL validation and error handling
* Provide API endpoints for interaction

---

## 🏗️ System Architecture

```text
User Question (English)
        ↓
FastAPI Backend
        ↓
Vanna 2.0 Agent
(GeminiLlmService / OpenAILlmService)
        ↓
SQL Validation (SELECT only)
        ↓
SQLite Database (clinic.db)
        ↓
Execution via SqliteRunner
        ↓
Response (Data + Summary + Chart)
```

---

## 🛠️ Tech Stack

| Component     | Technology                |
| ------------- | ------------------------- |
| Backend       | FastAPI                   |
| AI Agent      | Vanna AI 2.0              |
| Database      | SQLite                    |
| LLM Provider  | Google Gemini (Free Tier) |
| Visualization | Plotly                    |
| Language      | Python                    |

---

## 🤖 LLM Provider Used

**Provider:** Google Gemini
**Model:** `gemini-2.5-flash`
**Reason:** Free, fast, and supported by Vanna 2.0

---



---



### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

---

## 🗄️ Step 1: Create Database

```bash
python setup_database.py
```

✔ Creates:

* patients
* doctors
* appointments
* treatments
* invoices

✔ Inserts realistic dummy data

---

## 🧠 Step 2: Seed Agent Memory

```bash
python seed_memory.py
```

✔ Adds 15+ Q&A pairs
✔ Helps model generate better SQL

---

## 🚀 Step 3: Run API Server

```bash
uvicorn main:app --port 8000
```

Open:
👉 http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

### ✅ POST /chat

#### Request:

```json
{
  "question": "Top 5 patients by total spending"
}
```

#### Response:

```json
{
  "message": "Here are the top 5 patients...",
  "sql_query": "SELECT ...",
  "columns": ["name", "spending"],
  "rows": [["John", 5000]],
  "row_count": 5,
  "chart": {},
  "chart_type": "bar"
}
```

---

### ✅ GET /health

```json
{
  "status": "ok",
  "database": "connected",
  "agent_memory_items": 15
}
```

---

## 🔒 SQL Validation

Before execution:

* Only **SELECT queries allowed**
* Blocks:

  * INSERT, UPDATE, DELETE
  * DROP, ALTER
  * System tables (sqlite_master)
  * Dangerous keywords (EXEC, GRANT)

---

## ⚠️ Error Handling

* Invalid SQL → Friendly error message
* DB failure → Exception handled
* No data → "No data found" response

---

## 📊 Features Implemented

✅ NL → SQL conversion
✅ Vanna 2.0 Agent
✅ SQLite execution
✅ Agent memory learning
✅ SQL validation
✅ FastAPI endpoints
✅ Error handling
✅ Plotly chart support

---

## 🧪 Testing (20 Questions)

Tested with 20 queries including:

* Patient count
* Revenue
* Joins
* Aggregations
* Time-based queries

📄 Full results available in `RESULTS.md`

---

## ⚠️ Limitations

* Complex joins may fail sometimes
* Accuracy depends on LLM
* No caching implemented

---

## 🚀 Future Improvements

* Add query caching
* Improve SQL validation
* Add authentication
* Deploy on cloud
* Improve visualization

---

## 💡 Key Learning

* Learned Vanna 2.0 Agent architecture
* Integrated LLM with backend
* Built real-world NL2SQL pipeline
* Handled validation and errors

---



