import pandas as pd

def load_logs():
    """Load CSV logs to display to students"""
    return pd.read_csv("../../data/notification_logs.csv")
