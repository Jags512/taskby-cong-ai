from fastapi import FastAPI
from sqlalchemy import create_engine, text
from llm import generate_sql

app = FastAPI()

engine = create_engine("sqlite:///sales.db")

@app.get("/")
def home():
    return {"message": "NL2SQL API Running 🚀"}

@app.post("/query")
def query_db(question: str):
    try:
        
        sql = generate_sql(question)

        
        with engine.connect() as conn:
            result = conn.execute(text(sql))
            rows = [dict(row) for row in result]

        return {
            "question": question,
            "sql": sql,
            "result": rows
        }

    except Exception as e:
        return {"error": str(e)}