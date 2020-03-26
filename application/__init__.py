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

# Luetaan kansiosta application tiedoston views sisältö
from application import views

from application.matches import models
from application.matches import views
from application.fighters import models
from application.fighters import views
# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()