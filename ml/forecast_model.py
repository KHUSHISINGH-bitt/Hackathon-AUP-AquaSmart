# --- ml/forecast_model.py ---
import pandas as pd
from prophet import Prophet

def predict_usage(data_path='data/water_usage.csv'):
    df = pd.read_csv(data_path)
    df.rename(columns={'timestamp': 'ds', 'water_usage': 'y'}, inplace=True)
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']]