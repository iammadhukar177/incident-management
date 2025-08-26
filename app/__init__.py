from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from . import routes, auth
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)

    with app.app_context():
        db.create_all()

    return app
