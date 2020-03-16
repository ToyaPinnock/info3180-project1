import os
from app import app
from app import db
from app.models import UserProfile
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
import datetime

from app.forms import UserForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
    form=UserForm()
    date_joined= datetime.datetime.now()
    #date_created= date_joined.strftime('%B,%Y')
    if request.method== 'POST':
        if form.validate_on_submit():
            #upload image
            image=form.photo.data
            filename= secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #Get form data inputs
            fname= form.firstname.data
            lname= form.lastname.data
            email=form.email.data
            bio=form.biography.data
            location= form.location.data
            # add data to database
            user=UserProfile(firstname= fname,lastname=lname,email=email,location=location,date_joined= date_joined,biography=bio)
            db.session.add(user)
            db.session.commit()

            flash('You have sucessfully created a profile')
            return render_template('profiles.html',filename=filename)
        flash_errors(form)
    return render_template('profile.html',form=form)











def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
