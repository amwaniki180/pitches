from . import db


class Pitch(db.Model):
    """
    This is the class which we will use to create the pitches for the app
    """
    __tablename__ = "pitches"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    category = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship("Comment", backref = "pitch", lazy = "dynamic")

def save_pitch(self):
        db.session.add(self)
        db.session.commit()

def get_pitch_comments(self):
        pitch = Pitch.query.filter_by(id = self.id).first()
        comments = Comment.query.filter_by(pitch_id = pitch.id).order_by(Comment.time.desc())
        return comments
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'