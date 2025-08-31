import streamlit as st
import pandas as pd
import joblib

# Load model & preprocessors
model = joblib.load("best_downtime_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

st.title("🔮 Server Downtime Prediction App")
st.markdown("Enter server stats to predict if downtime is likely.")

# User inputs
cpu_usage = st.slider("CPU Usage (%)", 0, 100, 50)
memory_usage = st.slider("Memory Usage (%)", 0, 100, 50)
disk_usage = st.slider("Disk Usage (%)", 0, 100, 50)
network_latency = st.slider("Network Latency (ms)", 0, 500, 50)
location = st.selectbox("Server Location", le.classes_)

# Convert to DataFrame
input_data = pd.DataFrame({
    "cpu_usage": [cpu_usage],
    "memory_usage": [memory_usage],
    "disk_usage": [disk_usage],
    "network_latency": [network_latency],
    "location": [le.transform([location])[0]]
})

# Scale features
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict Downtime"):
    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    if pred == 1:
        st.error(f"⚠️ Downtime Likely (Probability: {prob:.2f})")
    else:
        st.success(f"✅ No Downtime Expected (Probability: {prob:.2f})")
