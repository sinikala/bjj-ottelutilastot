from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SelectField

class MatchForm(FlaskForm):
    place = StringField("Paikka", [validators.Length(min=3)])
    fighter1 = StringField("Ottelija 1", [validators.Length(min=3)])
    fighter2 = StringField("Ottelija 2", [validators.Length(min=3)])
    winning_category= SelectField("Voittotyyppi", choices=[('point_win', 'Pistevoitto'),
       ('submission', 'Luovutusvoitto'), ('judge_call', 'Tuomarin päätös') ])
    comment= TextAreaField("Lisätietoja")
 
    class Meta:
        csrf = False

# winning_category = StringField("Voittotyyppi", [validators.Length(min=5)])
#uovutus-, pistevoitto tai tuomarin päätös