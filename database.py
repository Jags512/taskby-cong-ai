from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///sales.db")

def create_data():
    data = {
        "region": ["North", "South", "East", "West"],
        "sales": [1000, 1500, 1200, 1800]
    }
    df = pd.DataFrame(data)
    df.to_sql("sales_data", engine, if_exists="replace", index=False)

create_data()