from dotenv import load_dotenv
from flask import Flask
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
    res=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}").json()
    print(res)

@dataclass
class WeatherData:
    pass

if __name__=="__main__":
    lat,lon=get_lat_lon("Mumbai","","India",API_KEY)
    get_current_weather(lat,lon,API_KEY)