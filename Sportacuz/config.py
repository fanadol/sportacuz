import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ['SPORTACUZ_KEY']
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jankenpo@localhost:5432/sportacuz'
    UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig,
    test=TestingConfig
)

key = Config.SECRET_KEY