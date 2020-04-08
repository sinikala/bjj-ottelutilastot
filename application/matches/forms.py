from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, IntegerField, SelectField, RadioField, FormField
from wtforms.validators import InputRequired, NumberRange

class MatchForm(FlaskForm):
    place = StringField("Paikka", [validators.Length(min=3, max=50)])
    fighter1 = SelectField("Ottelija 1", coerce=int)
    fighter2 = SelectField("Ottelija 2", coerce=int)
    winner= RadioField("Voittaja", choices=[('1', '1'), ('2', '2')], 
        validators=[InputRequired(message= "Valitse voittaja")])
    winning_category= SelectField("Voittotyyppi", choices=[
       ('submission', 'Luovutusvoitto'), ('point_win', 'Pistevoitto'),('judge_call', 'Tuomarin päätös') ])
    comment= TextAreaField("Lisätietoja",[validators.Length(max=244)])
    

    class Meta:
        csrf = False

