from flask import render_template
from . import main
from app.models import Pitch
from flask_login import login_required
from .. import db,photos
from .forms import AddPitchForm,AddComment,UpdateProfile



@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    title = "Home - welcome to pitches...Best pitch app"
    return render_template("index.html", pitches = pitches,title = title)

@main.route("/pitches/<category>")
def categories(category):
    pitches = None
    if category == "all":
        pitches = Pitch.query.order_by(Pitch.time.desc())
    else:
        pitches = Pitch.query.filter_by(category = category).order_by(Pitch.time.desc()).all()

    return render_template("pitches.html", pitches = pitches, title = category.upper())


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
