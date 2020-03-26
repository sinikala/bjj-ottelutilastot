from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SelectField, DecimalField



class FighterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3)])
    belt = SelectField("Vyöarvo", choices=[('white', 'valkoinen'),
       ('blue', 'sininen'), ('purple', 'violetti'), ('brown', 'ruskea'), ('black', 'musta')])
    club = StringField("Seura")
    weight = DecimalField("Paino", places=1, rounding=None)

    class Meta:
        csrf = False


