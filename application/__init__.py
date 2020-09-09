#Flask
from flask import Flask
app = Flask(__name__)

#SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
#Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///futsal.db"
app.config["SQLALCHEMY_ECHO"] = True

#db
db = SQLAlchemy(app)

#views
from application import views
from application.teams import views

#models
from application.teams import models

#create dbb tables
db.create_all()

from application import views