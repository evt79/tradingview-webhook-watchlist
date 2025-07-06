import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Watchlist Live", layout="wide")
st.title("🔔 Señales en Tiempo Real desde TradingView")

try:
    res = requests.get("https://TU-APP-RENDER.onrender.com/watchlist")  # Cambia esta URL tras desplegar
    data = res.json()
    df = pd.DataFrame(data)

    if not df.empty:
        df["time"] = pd.to_datetime(df["time"])
        st.dataframe(df.sort_values(by="time", ascending=False), use_container_width=True)
    else:
        st.info("Esperando señales...")
except Exception as e:
    st.error(f"No se pudo conectar al servidor: {e}")