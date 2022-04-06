import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very hard to guess'
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "Wzs232619"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = int(3306)
    MYSQL_DATABASE = "flask_test"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.environ['HOME'], '.tdl/tdl.db')






class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
