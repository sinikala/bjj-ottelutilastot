from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from flask_sqlalchemy import SQLAlchemy

import os


if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
#  Kolme vinoviivaa kertoo, tiedosto sijaitsee tämän 
# sovelluksen tiedostojen kanssa samassa paikassa
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///matches.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Sovelluksen toiminnallisuudet
from application import views

from application.matches import models
from application.matches import views

from application.fighters import models
from application.fighters import views

from application.points import models
from application.points import views

from application.auth import models 
from application.auth import views


#Kirjautuminen

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään käyttääksesi näitä toimintoja"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut
try:
    db.create_all()
except:
    pass