# --- utils/simulator.py ---
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

DATA_PATH = "data/water_usage.csv"

def simulate_new_entry():
    os.makedirs("data", exist_ok=True)
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
    else:
        df = pd.DataFrame(columns=["timestamp", "water_usage"])

    last_timestamp = pd.to_datetime(df["timestamp"].iloc[-1]) if not df.empty else datetime.now() - timedelta(hours=1)
    new_timestamp = last_timestamp + timedelta(hours=1)
    new_usage = np.random.normal(loc=100, scale=20)

    if np.random.rand() < 0.05:
        new_usage += np.random.randint(50, 150)  # Simulate occasional leak

    new_entry = pd.DataFrame({"timestamp": [new_timestamp], "water_usage": [new_usage]})
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)
