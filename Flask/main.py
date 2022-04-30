from flask import Flask, render_template, request
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail

local_server = True
with open('config.json') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contact(db.Model):
    """
    S.no,Name,Email,Phone_num,Message,Date
    """
    Sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Posts(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    Content = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(120), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)


@app.route('/')
def home():
    return render_template('index.html', params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params,post=post)
# @app.route("/p")
# def post():
#     render_template('p.html',params=params)


@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        """
           S.no,Name,Email,Phone_num,Message,Date
        """
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contact(name=name, phone=phone, message=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message in blog from ' + name, sender=email, recipients=[params['gmail-user']],
                          body=message + "\n" + phone
                          )

    return render_template('contact.html', params=params)


# @app.route('/post')
# def post():
#     return render_template('post.html', params=params)


app.run(debug=True)
# debug=True can be used to save the changes
