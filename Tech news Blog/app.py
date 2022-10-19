from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
import json

with open('config.json', 'r') as j:
    params = json.load(j)["params"]

local_server = True
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-pass']
)

mail = Mail(app)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_num = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(80))
    date = db.Column(db.String(120), nullable=False)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(180), nullable=False)
    date = db.Column(db.String(12), nullable=False)


@app.route("/")
def home():
    post = Posts.query.filter_by().all()
    return render_template('index.html', params=params, posts=post)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, email=email, phone_num=phone, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        # mail.send_message(
        #     'Blog message from' + name,
        #     sender=email,
        #     recipients=[params['gmail-user']],
        #     body=message + "\n" + "phone:- " + phone
        # )
    return render_template('contact.html', params=params)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


app.run(debug=True)
