from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db=SQLAlchemy(app)



class Todo(db.Model,):
    id = db.Column(db.Integer,primary_key=True)
    task=db.Column(db.String(200),nullable=False)

@app.route("/")
def home():
    return "hello world"




if __name__=="__main__":
    with app.app_context():
        db.create_all
    app.run()
