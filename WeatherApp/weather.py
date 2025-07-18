from dotenv import load_dotenv
from dataclasses import dataclass
import requests
import os

load_dotenv()

API_KEY=os.getenv('API_KEY')
def get_lat_lon(city_name,state_code,country_code,API_KEY):
    resp=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}").json()
    data=resp[0]
    lat,lon=data.get('lat'),data.get('lon')#lat,lon=data['lat'],data['lon']s
    return lat,lon

def get_current_weather(lat,lon,API_KEY):
    res=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric").json()
    data=WeatherData(
        main=res.get('weather')[0].get('main'),
        description=res.get('weather')[0].get('description'),
        icon=res.get('weather')[0].get('icon'),
        temperature=res.get('main').get('temp')
    )
    return data

@dataclass
class WeatherData:
    main:str
    description:str
    icon:str
    temperature:float

def main(city_name,country_code,API_KEY=API_KEY,state_code=""):
    lat,lon=get_lat_lon("Mumbai","","India",API_KEY)
    weather_data=get_current_weather(lat,lon,API_KEY)
    return weather_data


if __name__=="__main__":
    lat,lon=get_lat_lon("Mumbai","","India",API_KEY)
    print(get_current_weather(lat,lon,API_KEY))