import pandas as pd

def parse_excel(filepath):
    df = pd.read_excel(filepath, engine="openpyxl")

    # Normalize column headers
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
    
    data = df.to_dict(orient="records")
    return data
