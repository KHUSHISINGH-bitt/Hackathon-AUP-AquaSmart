# --- ml/anomaly_detection.py ---
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(data_path='data/water_usage.csv'):
    df = pd.read_csv(data_path)
    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df[['water_usage']])
    return df[df['anomaly'] == -1]