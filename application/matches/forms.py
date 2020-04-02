from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SelectField, RadioField
from wtforms.validators import InputRequired

class MatchForm(FlaskForm):
    place = StringField("Paikka", [validators.Length(min=3)])
    fighter1 = SelectField("Ottelija 1", coerce=int)
    fighter2 = SelectField("Ottelija 2", coerce=int)
    winner= RadioField("Voittaja", choices=[('1', '1'), ('2', '2')], 
        validators=[InputRequired(message= "Valitse voittaja")])
    winning_category= SelectField("Voittotyyppi", choices=[('point_win', 'Pistevoitto'),
       ('submission', 'Luovutusvoitto'), ('judge_call', 'Tuomarin päätös') ])
    comment= TextAreaField("Lisätietoja")
 
    class Meta:
        csrf = False

# winning_category = StringField("Voittotyyppi", [validators.Length(min=5)])
#uovutus-, pistevoitto tai tuomarin päätös