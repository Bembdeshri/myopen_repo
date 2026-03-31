import pandas as pd
from datetime import datetime

def process_weather_data(raw_data):
    if 'error' in raw_data:
        return raw_data
    
    def format_time(unix):
        return datetime.fromtimestamp(unix).strftime('%H:%M %p')

    # This dictionary defines the "Names" used in the app
    processed_data = {
        'City': raw_data.get('name'),
        'Country': raw_data.get('sys', {}).get('country'),
        'Temperature': f"{raw_data['main']['temp']}°C",
        'Feels Like': f"{raw_data['main']['feels_like']}°C",
        'Humidity': f"{raw_data['main']['humidity']}%",
        'Pressure': f"{raw_data['main']['pressure']} hPa",
        'Wind Speed': f"{raw_data['wind']['speed']} m/s",
        'Sunrise': format_time(raw_data['sys']['sunrise']),
        'Sunset': format_time(raw_data['sys']['sunset']),
        'Description': raw_data['weather'][0]['description'].title(),
        'Icon': raw_data['weather'][0]['icon']
    }
    
    df = pd.DataFrame([processed_data])
    return {"display": processed_data, "df": df}