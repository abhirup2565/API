from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db=SQLAlchemy(app)



class TodoDB(db.Model,):
    id = db.Column(db.Integer,primary_key=True)
    task=db.Column(db.String(200),nullable=False)

@app.route("/view")
def view():
    data=[]
    todo=TodoDB.query.all()
    for task in todo:
        data.append({
            "ID":task.id,
            "task":task.task
                    })
    return jsonify({"API_Task":data})

@app.route("/post",methods=["POST","GET"])
def set_task():
    data=request.get_json()
    new_task = TodoDB(task=data["task"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"Message":"task has been created"})

@app.route("/delete",methods=["POST","GET"])
def delete_task():
    data=request.get_json()
    task=TodoDB.query.filter_by(id=data["ID"]).first()
    db.session.delete(task)
    db.session.commit()
    return jsonify({"Message":"Task has been delete"})

    
    




if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
