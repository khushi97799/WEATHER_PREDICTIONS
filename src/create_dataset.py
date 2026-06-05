import requests
import pandas as pd
import os

url = (
    "https://archive-api.open-meteo.com/v1/archive?"
    "latitude=26.19&longitude=91.74"
    "&start_date=2023-01-01&end_date=2024-12-31"
    "&daily=temperature_2m_max,temperature_2m_min,"
    "precipitation_sum,windspeed_10m_max,relative_humidity_2m_max"
    "&timezone=Asia/Kolkata"
)

res = requests.get(url).json()
df = pd.DataFrame(res["daily"])
df.columns = ["date", "temp_max", "temp_min", "precipitation", "wind_speed", "humidity"]
df["next_day_temp"] = df["temp_max"].shift(-1)
df = df.dropna()

os.makedirs("data", exist_ok=True)
df.to_csv("data/weather.csv", index=False)
print(f"Dataset created: {len(df)} samples")