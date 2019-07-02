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


@main.route("/<uname>/add/pitch", methods = ["GET","POST"])
@login_required
def add_pitch(uname):
    form = AddPitchForm()
    user = User.query.filter_by(name = uname).first()
    if user is None:
        abort(404)
    title = "Add Pitch"
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data 
        dateOriginal = datetime.datetime.now()
        time = str(dateOriginal.time())
        time = time[0:5]
        date = str(dateOriginal)
        date = date[0:10]
        new_pitch = Pitch(title = title, content = pitch, category = category,user = user, date = date,time = time)
        new_pitch.save_pitch()  
        pitches = Pitch.query.all()
        return redirect(url_for("main.categories",category = category))
    return render_template("add_pitch.html",form = form, title = title)
