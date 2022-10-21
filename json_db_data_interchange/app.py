from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open('employee-details.json', 'r') as j:
    data = json.load(j)
print(data)

app = Flask(__name__)
app.config['SECRET_KEY'] = "cryptickey-hidden"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/tech_news"
db = SQLAlchemy(app)


class Employee(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)

@app.route("/")
def add_to_db():
    for k, v in data.items():
        print(v)
        entry = Employee(firstname=v['firstName'], lastname=v['lastName'])
        db.session.add(entry)
        db.session.commit()
    return "<p>done</p>"

@app.route("/show")
def show():
    post = Employee.query.all()
    with open('output.txt','a+') as out:
        out.write(str(post))
    return "<p>retrieved</p>"

app.run(debug=True)
