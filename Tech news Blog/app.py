from flask import Flask, render_template, request, session, redirect
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
    MAIL_PASSWORD=params['gmail-pass'],
)
app.config['SECRET_KEY'] = params['secret_key']

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


@app.route("/login", methods=['GET', 'POST'])
def login():
    print("login")
    if 'user' in session and (session['user'] == params['admin_user']):
        # print("in session")
        posts = Posts.query.all()
        render_template('dashboard.html', params=params, posts=posts)
    if request.method == 'POST':
        print("in post")
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        print(username, userpass)
        if username == params["admin_user"] and userpass == params["admin_password"]:
            session['user'] = username
            # print("returning dashboard")
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
    return render_template('login.html', params=params)


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            title = request.form.get('title')
            slug = request.form.get('slug')
            content = request.form.get('content')
            post = Posts.query.filter_by(sno=sno).first()
            post.title = title
            post.slug = slug
            post.content = content
            post.date = datetime.now()
            db.session.commit()
            return redirect('/edit/' + sno)
    post = Posts.query.filter_by(sno=sno).first()
    return render_template('edit.html', params=params, post=post)


@app.route("/add")
def add():
    return render_template('add.html',params=params)


@app.route("/add_to_db", methods=['GET', 'POST'])
def add_to_db():
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            title = request.form.get('title')
            slug = request.form.get('slug')
            content = request.form.get('content')
            entry = Posts(title=title, slug=slug, content=content,date=datetime.now())
            db.session.add(entry)
            db.session.commit()
    posts = Posts.query.all()
    return render_template('dashboard.html', params=params, posts=posts)
def about():
    return render_template('about.html', params=params)


@app.route("/about")
def about():
    return render_template('about.html', params=params)

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')

@app.route("/delete/<string:sno>",methods=['GET','POST'])
def delete(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)
    return "<p>post not deleted</p>"


app.run(debug=True)
