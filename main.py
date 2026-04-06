
from fastapi import FastAPI
from pydantic import BaseModel
from vanna_setup import create_agent

app = FastAPI()

agent, memory = create_agent()

class Query(BaseModel):
    question: str

def validate_sql(sql):
    forbidden = ["INSERT","UPDATE","DELETE","DROP","ALTER"]
    return not any(word in sql.upper() for word in forbidden)

@app.post("/chat")
def chat(q: Query):
    response = agent.run(q.question)

    sql = response.get("sql", "")

    if not validate_sql(sql):
        return {"error": "Invalid SQL detected"}

    return response

@app.get("/health")
def health():
    return {"status": "ok"}
