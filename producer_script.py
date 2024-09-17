from dotenv import load_dotenv
import os 
import requests
import random
from time import sleep

load_dotenv()
api_key = os.environ.get('WEATHER_API_KEY')


def data_producer():
    latitude = round(random.uniform(-90,90),2)
    longitude = round(random.uniform(-90,90),2)

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

    response_body = requests.get(url=url)

    data = response_body.json()
    timezone = data['timezone']
    region = data['name']
    weather_data = data['weather'][0]

    weather_data['timezone'] = timezone
    weather_data['region'] = region
    weather_data['latitude'] = latitude
    weather_data['longitude'] = longitude

    return weather_data

if __name__=="__main__":
    for _ in range(1,5):
        temp_dict = data_producer()
        print(temp_dict,'/n')
        sleep(2)


