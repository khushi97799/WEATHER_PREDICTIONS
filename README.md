# WeatherPulse — Real-Time Weather Intelligence System

> Next-day temperature prediction using XGBoost + real historical weather data + live API integration.

## Live Demo
Run locally with Streamlit — enter any city and get real-time prediction.

## How It Works
1. **Historical Data** — 2 years of real daily weather data (730 samples) from Open-Meteo API for model training
2. **ML Model** — XGBoost regressor trained on temp, humidity, precipitation, wind speed
3. **Live Prediction** — fetches real-time weather via OpenWeather API and predicts next-day temperature
4. **Dashboard** — interactive Streamlit app with live weather display and temperature trend visualization

## Model Performance
- **MAE:** 0.086°C
- **R²:** 0.9988
- **Dataset:** 730 days of real weather data

## Tech Stack
- Python, XGBoost, Scikit-learn, Pandas, NumPy
- Streamlit, Matplotlib
- OpenWeather API, Open-Meteo API

## Quick Start
```bash
pip install -r requirements.txt
python src/create_dataset.py
python src/train_model.py
python -m streamlit run app.py
```

## Project Structure
```
weather-pulse/
├── src/
│   ├── create_dataset.py   # fetches historical data
│   ├── fetch_weather.py    # live weather API
│   ├── preprocess.py       # feature engineering
│   └── train_model.py      # model training
├── data/
│   └── weather.csv
├── app.py                  # Streamlit dashboard
├── model.pkl
└── requirements.txt
```
