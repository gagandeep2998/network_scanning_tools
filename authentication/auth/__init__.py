from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = "network_scanner.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "This is some secret data"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///network_scanner.db"
    db.init_app(app)

    from .auth import auth

    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app


def create_db(app):
    if not path.exists("network_scanner/" + DB_NAME):
        with app.app_context():
            db.create_all()
