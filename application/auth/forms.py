from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False



class RegisterForm(FlaskForm):
    name= StringField("Nimi", [validators.Length(min=3, max=50)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=3, max=50)])
    password = PasswordField("Salasana",[validators.Length(min=5, max=144),
    validators.EqualTo('confirm', message='Salasanojen tulee täsmätä')])
    confirm = PasswordField("Toista salasana")
    registrationkey=PasswordField("Rekisteröitymisavain", [validators.Regexp('^berimbolo$', message='Väärä avain' )])

    class Meta:
        csrf = False


