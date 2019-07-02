import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SECRET_KEY = os.environ.get("0717006024")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://antony:dee@localhost/pitches'

class ProdConfig(Config):
    
    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}




