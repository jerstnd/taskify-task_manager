from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# setting up the database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    '''
    initialize the app
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'awdklbgweojg;sldmfar'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) # initialize database

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    create_database(app)
    
    # where to go if the user do not logged in
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #loading a user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    '''
    if database existed, pass
    if does not exist, create database
    '''
    if not path.exists('taskify/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')