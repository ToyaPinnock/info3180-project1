
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = './app/static/uploads'
SECRET_KEY = 'ASsdfk@HYR567dgrh'

app.config['SECRET_KEY'] = "LKDER2342MDwedWD"
app.config['DATABASE_URL']="postgres://jzdgystcsdntuw:256ded91e4169b559fab4f3ee9c60106339ea62cb36b4f7e7b33576169968640@ec2-34-235-108-68.compute-1.amazonaws.com:5432/ddoe91t285n21o"
#"postgresql://p1:securepass123@localhost/p1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)

from app import views