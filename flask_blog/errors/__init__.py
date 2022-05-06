from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog.config import Config
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    print(__name__)
    app = Flask(__name__)
    # Регистрируем бюлпринт main
    from flask_blog.main.routes import main
    app.register_blueprint(main)
    app.config.from_object(Config)

    # Регистрация логин-менеджера
    login_manager.init_app(app)

    # pwd
    bcrypt.init_app(app)

    # Регистируем приложение users
    from flask_blog.users.routes import users
    app.register_blueprint(users)

    db.init_app(app)
    return app
