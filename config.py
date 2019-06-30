import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:antony@tony/pitches'