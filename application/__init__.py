#Flask
from flask import Flask
app = Flask(__name__)

#SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
#Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///futsal.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


from application import views

#teams
from application.teams import models
from application.teams import views

#auth
from application.auth import models
from application.auth import views

#player
from application.players import models
from application.players import views

# Login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#create db tables
db.create_all()