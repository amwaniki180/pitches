import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')
    

class DevConfig(Config):
    SECRET_KEY='absc'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://antony:dee@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}




