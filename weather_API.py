import requests
from flask import Flask,jsonify,request,redirect,url_for,render_template



app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    datas={}
    if request.method=="POST":
        city_name=request.form.get("city")
        API_key=
        response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
        datas=response.json()
    return render_template("home.html",datas=datas)

if __name__=="__main__":
    app.run(debug=True)
