# --- frontend/app.py ---
import streamlit as st
import pandas as pd
import plotly.express as px
import time
from utils.simulator import simulate_new_entry
from utils.eco_score import calculate_eco_score
from utils.tips_engine import get_water_saving_tips
from ml.forecast_model import predict_usage
from ml.anomaly_detection import detect_anomalies

st.set_page_config(layout="wide")
st.title("💧 Smart Water Usage Monitoring Dashboard")

simulate_new_entry()
df = pd.read_csv("data/water_usage.csv")
forecast = predict_usage()
anomalies = detect_anomalies()
eco_score = calculate_eco_score(df)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Water Usage Over Time")
    st.plotly_chart(px.line(df, x='timestamp', y='water_usage', title='Hourly Water Usage'))

with col2:
    st.subheader("🔮 Forecasted Usage (Next 24h)")
    st.plotly_chart(px.line(forecast.tail(48), x='ds', y='yhat', title='Forecasted Water Usage'))

st.subheader("🚨 Detected Anomalies")
st.dataframe(anomalies)

st.subheader("🌱 Eco-Impact Score")
st.metric(label="Water Efficiency Score", value=f"{eco_score} / 100")

st.subheader("💡 Water Saving Tip")
st.info(get_water_saving_tips())

st.button("🔁 Simulate Leak", on_click=lambda: simulate_new_entry())

st.caption("Dashboard auto-refreshes every 10 seconds.")
time.sleep(10)
st.experimental_rerun()
