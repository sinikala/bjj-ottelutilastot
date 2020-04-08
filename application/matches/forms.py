from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SelectField, RadioField, FormField
from wtforms.validators import InputRequired
from application.points.forms import PointForm


class MatchForm(FlaskForm):
    place = StringField("Paikka", [validators.Length(min=3, max=50)])
    fighter1 = SelectField("Ottelija 1", coerce=int)
    fighter2 = SelectField("Ottelija 2", coerce=int)
    winner= RadioField("Voittaja", choices=[('1', '1'), ('2', '2')], 
        validators=[InputRequired(message= "Valitse voittaja")])
    winning_category= SelectField("Voittotyyppi", choices=[('point_win', 'Pistevoitto'),
       ('submission', 'Luovutusvoitto'), ('judge_call', 'Tuomarin päätös') ])
    comment= TextAreaField("Lisätietoja",[validators.Length(max=244)])
    points = FormField(PointForm)

    class Meta:
        csrf = False

