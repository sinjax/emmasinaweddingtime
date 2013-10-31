import os

DEBUG = os.environ.get('DEBUG', False)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',"sqlite:///test.db")

MAIL_DEFAULT_SENDER = 'wedding@emmasinawedding.org'