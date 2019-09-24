import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:zuhura18@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/images'


    SECRET_KEY = '12323344ew'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'moharick@gmail.com'


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        debug = os.environ.get("DEBUG")


class TestConfig(Config):
    pass


class DevConfig(Config):
    #SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:zuhura18@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
