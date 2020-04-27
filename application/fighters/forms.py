from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators, SelectField, DecimalField
from wtforms.validators import NumberRange



class FighterForm(FlaskForm):
    name = StringField("Nimi*", [validators.Length(min=3, max=50)])
    born= IntegerField("Syntymävuosi*", validators=[NumberRange(min=1900, max=2017,
        message='Syötä kelvollinen syntymävuosi')])
    belt = SelectField("Vyöarvo*", choices=[('valkoinen', 'valkoinen'),
       ('blue', 'sininen'), ('purple', 'violetti'), ('brown', 'ruskea'), ('black', 'musta')])
    club = StringField("Seura", [validators.Length(min=0, max=80)])
    weight = DecimalField("Paino (kg) ", places=1, rounding=None, validators=[NumberRange(min=0, max=200,
        message='Paino ei voi olla negatiivinen tai yli 200 kg')])

    class Meta:
        csrf = False





class FilterForm(FlaskForm):
    by_club= SelectField("Seura", coerce=int)
    by_belt= SelectField("Vyöarvo", choices=[('-1', 'Valitse vyöarvo'), ('valkoinen', 'valkoinen'),
       ('sininen', 'sininen'), ('violetti', 'violetti'), ('ruskea', 'ruskea'), ('musta', 'musta')])
    
    class Meta:
        csrf=False



class SearchForm(FlaskForm):
    searchword= StringField("Hae nimellä")


    class Meta:
        csrf=False

