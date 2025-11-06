import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

def predict_best_time(logs_csv):
    """Predict optimal notification time based on past engagement"""
    try:
        df = pd.read_csv(logs_csv)
        df['hour_sent'] = pd.to_datetime(df['timestamp']).dt.hour
        df['opened'] = df['opened'].astype(int)
        X = df[['hour_sent']]
        y = df['opened']
        model = LinearRegression()
        model.fit(X, y)
        best_hour = int(model.predict([[12]])[0])  # Example prediction
        return best_hour
    except:
        return 9  # Default 09:00 AM if no data
