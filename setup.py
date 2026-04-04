from vanna.openai import OpenAI_Chat
from vanna.base import VannaBase

class MyVanna(OpenAI_Chat, VannaBase):
    def __init__(self):
        OpenAI_Chat.__init__(self, config={
            "api_key": "YOUR_OPENAI_API_KEY",
            "model": "gpt-4"
        })

vn = MyVanna()

# Train Vanna with schema
vn.train(ddl="""
CREATE TABLE sales_data (
    region TEXT,
    sales INTEGER
);
""")