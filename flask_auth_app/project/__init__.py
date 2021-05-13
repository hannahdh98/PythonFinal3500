# import statements
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #this will get rid of the deprecation warnings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    app.config['SECRET_KEY'] = ' secret-key-goes-here '
    # personalized SQLALCHEMY_DATABASE_URI password and url goes here to connect.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Grapes34!@localhost:3306/flask'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


