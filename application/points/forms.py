from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SelectField, RadioField, IntegerField
from wtforms.validators import InputRequired, NumberRange

class PointForm(FlaskForm):
    fighter1_points = IntegerField("Pisteet", validators=[NumberRange(min=0, max=100,
        message='Pistesaldo ei voi olla negatiivinen')])
    fighter1_penalties = IntegerField("Rangaistukset", validators=[NumberRange(min= -100, max=0,
        message='Rangaistussaldo ei voi olla nollaa suurempi')])
    fighter1_advantages = IntegerField("Etu", validators=[NumberRange(min=0, max=100,
        message='Etusaldo ei voi olla negatiivinen')])


    fighter2_points = IntegerField("Pisteet", validators=[NumberRange(min=0, max=100,
        message='Pistesaldo ei voi olla negatiivinen')])
    fighter2_penalties = IntegerField("Rangaistukset", validators=[NumberRange(min=-100, max=0,
        message='Rangaistussaldo ei voi olla nollaa suurempi')])
    fighter2_advantages = IntegerField("Etu", validators=[NumberRange(min=0, max=100,
        message='Etusaldo ei voi olla negatiivinen')])


    class Meta:
        csrf = False