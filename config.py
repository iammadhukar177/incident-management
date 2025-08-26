import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'devkey')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///incidents.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
