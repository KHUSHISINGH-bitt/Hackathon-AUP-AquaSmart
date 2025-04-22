import pandas as pd
import numpy as np
import os
import time
from datetime import datetime, timedelta

def create_hourly_entry(last_timestamp):
    new_time = last_timestamp + timedelta(hours=1)
    base_usage = np.random.normal(loc=100, scale=20)
    return new_time, base_usage

def stream_data():
    # Load existing data to get last timestamp
    if os.path.exists('data/water_usage.csv'):
        df = pd.read_csv('data/water_usage.csv')
        last_time = pd.to_datetime(df['timestamp'].iloc[-1])
    else:
        last_time = pd.to_datetime('2025-04-01 00:00:00')
        
    while True:
        new_time, new_usage = create_hourly_entry(last_time)
        new_row = f"\n{new_time.strftime('%Y-%m-%d %H:%M:%S')},{new_usage}"
        
        with open('data/water_usage.csv', 'a') as f:
            f.write(new_row)
        
        last_time = new_time
        time.sleep(60)  # Wait 1 minute between updates

if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)
    stream_data()