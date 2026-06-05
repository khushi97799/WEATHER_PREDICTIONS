import requests

API_KEY = "473f5103d14f43b9970ded76f055e84b"

def get_weather(city="Delhi"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    res = requests.get(url).json()

    weather_data = {
        "temp": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "pressure": res["main"]["pressure"],
        "wind_speed": res["wind"]["speed"]
    }

    return weather_data