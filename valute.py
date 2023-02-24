from pprint import pprint

import requests

from config import API_W
# data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# pprint(data['Valute'])

lat = 42.87
lon = 74.59

API_W = 'd914d456db8a60ca05c7a5f9e28644cd' # зарегаться и взять с опенвезер

weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_W}'

weather_data = requests.get(weather)
pprint(weather_data.text)
