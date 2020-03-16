
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = './app/static/uploads'
SECRET_KEY = 'ASsdfk@HYR567dgrh'

app.config['SECRET_KEY'] = "LKDER2342MDwedWD"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://flask-p1:passes123@localhost/flask-p1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)

from app import views