import requests
from flask import Flask,request,render_template



app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    API_KEY_NEWS=
    response_news=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY_NEWS}")
    news=response_news.json()

    datas={}
    if request.method=="POST":
        city_name=request.form.get("city")
        API_key=
        response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
        datas=response.json()
    return render_template("home.html",datas=datas,news=news)

if __name__=="__main__":
    app.run(debug=True)
