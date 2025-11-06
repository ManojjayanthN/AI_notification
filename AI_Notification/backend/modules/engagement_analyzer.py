import pandas as pd

def calculate_engagement(logs_csv):
    df = pd.read_csv(logs_csv)
    total = len(df)
    opened = df['opened'].sum()
    if total == 0:
        return 0
    return round((opened / total) * 100, 2)
