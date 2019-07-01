from flask import render_template
from app import app





@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    title = "Home - welcome to pitches...Best pitch app"
    return render_template("index.html", pitches = pitches,title = title)
