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
def profileform():
    form=UserForm()
    date_joined= datetime.datetime.now()
    date_created= date_joined.strftime('%B %d,%Y')
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
            gender= form.gender.data
            # add data to database
            user=UserProfile(firstname= fname,lastname=lname,email=email, gender= gender,location=location,date_joined= date_created,biography=bio,filename=filename)
            db.session.add(user)
            db.session.commit()

            flash('You have sucessfully created a profile')
            return redirect(url_for('profiles'))
        flash_errors(form)
    return render_template('profileform.html',form=form)

@app.route('/profiles')
def profiles():
    users= UserProfile.query.all()
    return render_template('profiles.html',users=users)


@app.route('/profile/<int:id>')
def userid(id):
    user= UserProfile.query.filter_by(id=id).first()
    return render_template('user.html',user=user)
# show the post with the given id, the id is an integer
#'Post {}'.format(id)




if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port="5432")
