from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()

def create_app():
    print(__name__)
    app = Flask(__name__)
    app.config.from_object(Config)

    # БД
    db.init_app(app)
    # Регистрация логин-менеджера
    login_manager.init_app(app)
    # pwd
    bcrypt.init_app(app)
    # mail
    mail.init_app(app)

    from flask_blog.main.routes import main
    from flask_blog.users.routes import users
    from flask_blog.posts.routes import posts

    # Регистрируем бюлпринт main
    app.register_blueprint(main)
    app.config.from_object(Config)
    # Регистируем приложение users
    app.register_blueprint(users)
    # Регистрация posts
    app.register_blueprint(posts)

    return app
