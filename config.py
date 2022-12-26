import os
from dotenv import load_dotenv

load_dotenv('.env.dev')
# load_dotenv('.env.prod')

class Config(object):
    DEBUG = bool(os.environ.get('DEBUG'))
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_HOST=os.environ.get('MYSQL_HOST')
    DB_NAME=os.environ.get('MYSQL_DATABASE')
    DB_USER=os.environ.get('MYSQL_USER')
    DB_PASSWORD=os.environ.get('MYSQL_PASSWORD')
    DB_ROOT_PASSWORD=os.environ.get('MYSQL_ROOT_PASSWORD')
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


