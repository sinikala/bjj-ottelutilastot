from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, IntegerField, SelectField, RadioField, FormField
from wtforms.validators import InputRequired, NumberRange
from wtforms.fields.html5 import DateField

class MatchForm(FlaskForm):
    date = DateField("Pvm*", format ='%Y-%m-%d')
    place = StringField("Paikka*", [validators.Length(min=3, max=50)])
    fighter1 = SelectField("Ottelija 1*", coerce=int)
    fighter2 = SelectField("Ottelija 2*", coerce=int)
    winner= RadioField("Voittaja*", choices=[('1', '1'), ('2', '2')], 
        validators=[InputRequired(message= "Valitse voittaja")])
    winning_category= SelectField("Voittotyyppi*", choices=[
       ('submission', 'Luovutusvoitto'), ('point_win', 'Pistevoitto'),('judge_call', 'Tuomarin päätös') ])
    comment= TextAreaField("Lisätietoja",[validators.Length(max=50)])
    

    class Meta:
        csrf = False


class FilterForm(FlaskForm):
    by_club= SelectField("Seura", coerce=int)
    by_winning_category= SelectField("Voittokategoria", choices=[('-1', 'Valitse voittokategoria'),
        ('Pistevoitto', 'Pistevoitto'), ('Luovutusvoitto', 'Luovutusvoitto'), ('Tuomarin päätös', 'Tuomarin päätös')])
    by_belt= SelectField("Vyöarvo", choices=[('-1', 'Valitse vyöarvo'), ('valkoinen', 'valkoinen'),
       ('sininen', 'sininen'), ('violetti', 'violetti'), ('ruskea', 'ruskea'), ('musta', 'musta')])
    
    class Meta:
        csrf=False