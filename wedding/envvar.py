import os

DEBUG = os.environ.get('DEBUG', False)
SECRET_KEY = os.environ.get('SECRECT',"notsecret")
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',"sqlite:///test.db")

MAIL_DEFAULT_SENDER = 'wedding@emmasinaweddingtime.info'
MAIL_SERVER = os.environ['MAIL_SERVER']
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
MAIL_PORT = 465
MAIL_USE_SSL = True