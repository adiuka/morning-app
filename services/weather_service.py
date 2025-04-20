import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
from config import WEATHER_API_KEY, LAT, LON


def get_weather():
    """Returns: average temperature (float), will_rain (bool)"""

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url=url)
    weather_data = response.json()
    temp = 0
    for hour in weather_data['list'][:8]:
        hour_temp = float(hour['main']['temp'])
        temp += hour_temp
    average_temp = temp / 8
    
    will_rain = False
    for hour in weather_data['list'][:8]:
        condition_code = hour['weather'][0]['id']
        if int(condition_code) < 700:
            will_rain = True

    return round(average_temp, 1), will_rain
