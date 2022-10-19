from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)


@app.route("/")
def hello_world():
    todo = Todo(title="todo 1", description="this is a description description")
    db.session.add(todo)
    db.session.commit()

    return render_template('index.html',variable = "Aloha Training")


@app.route("/product")
def products():
    return "<p>this is products</p>"


if __name__ == "__main__":
    app.run(debug=True)
