import requests
from config import API_KEY

def fetch_weather_data(city_name):
    # Added units=metric to get Celsius automatically
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'City not found'}