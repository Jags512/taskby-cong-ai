from transformers import pipeline

# Load model
generator = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.1",
    max_new_tokens=200
)

def generate_sql(question):
    prompt = f"""
You are an expert SQL generator.

Rules:
- Only return SQL query
- No explanation

Schema:
CREATE TABLE sales_data (
    region TEXT,
    sales INTEGER
);

Question: {question}

SQL:
"""

    response = generator(prompt)[0]["generated_text"]

    # Extract SQL part
    sql = response.split("SQL:")[-1].strip()

    return sql