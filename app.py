import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.fetch_weather import get_weather

model = joblib.load("model.pkl")

st.title("🌦️ Real-Time Weather Prediction Dashboard")

city = st.text_input("Enter City Name", "Bathinda")

if st.button("Get Live Weather"):
    weather = get_weather(city)

    st.subheader("🌍 Live Weather Data")
    st.write(weather)

    features = np.array([[
        weather["temp"],
        weather["temp"] - 3,
        0,
        weather["wind_speed"],
        weather["humidity"]
    ]])

    prediction = model.predict(features)[0]

    st.subheader("🤖 Predicted Next Day Temperature")
    st.success(f"{prediction:.2f} °C")

st.subheader("📊 Sample Weather Trend")
data = pd.DataFrame({
    "temp": [30, 31, 29, 28, 32, 33, 31],
    "days": list(range(7))
})
fig, ax = plt.subplots()
ax.plot(data["days"], data["temp"], marker="o")
ax.set_title("Temperature Trend")
ax.set_xlabel("Days")
ax.set_ylabel("Temperature")
st.pyplot(fig)