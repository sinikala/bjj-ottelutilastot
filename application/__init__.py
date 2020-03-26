from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

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
db.create_all()