from flask import render_template
from . import main
from app.models import Pitch
from flask_login import login_required




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


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
