from . import db


class UserProfile(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email= db.Column(db.String(120), unique=True)
    location= db.Column(db.String(120))
    biography= db.Column(db.String(255))
    date_joined = db.Column(db.String(120))
    filename= db.Column(db.String(120))
    gender= db.Column(db.String(50))

def __init__(self, firstname,lastname,email,gender,location,date_joined,biography,filename):
    self.firstname=firstname
    self.lastname=lastname
    self.email=email
    self.gender=gender
    self.location=location
    self.biography=biography
    self.date_joined=date_joined
    self.filename=filename

def is_authenticated(self):
        return True

def is_active(self):
    return True

def is_anonymous(self):
    return False

def get_id(self):
    try:
        return unicode(self.id)  # python 2 support
    except NameError:
        return str(self.id)  # python 3 support

def __repr__(self):
    return '<User %r>' % (self.firstname) % (self.lastname)