from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
    firstname= StringField('FirstName',validators=[DataRequired()])
    lastname= StringField('LastName',validators=[DataRequired()])
    email= StringField('Email',validators=[DataRequired(), Email()])
    location= StringField('Location',validators=[DataRequired()])
    biography= TextAreaField('Biography',validators=[DataRequired()])
    photo= FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png','Images Only'])])