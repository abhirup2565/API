from dotenv import load_dotenv
from flask import Flask
import requests
import os

load_dotenv()

API_KEY=os.getenv('API_KEY')
def get_lat_lon(city_name,state_code,country_code,API_KEY):
    resp=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}").json()
    data=resp[0]
    lat,lon=data.get('lat'),data.get('lon')#lat,lon=data['lat'],data['lon']s
    return lat,lon


print(get_lat_lon("Mumbai","","India",API_KEY))
