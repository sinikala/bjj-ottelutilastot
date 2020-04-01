from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginForm.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginForm.html", form = form,
                               error = "Kirjautuminen epäonnistui")


    login_user(user, remember=True)
    return redirect(url_for("index"))   


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  


@app.route("/register", methods = ["GET", "POST"])
def auth_register():

    if request.method == "GET":
        return render_template("auth/registerForm.html", form = RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerForm.html", form = form)

    username_in_db = User.query.filter_by(username=form.username.data).first()
    if username_in_db:
        return render_template("auth/registerForm.html", form = form,
                               error = "Käyttäjänimi varattu")
    user = User(form.name.data, form.username.data,
                    form.password.data)

    db.session.add(user)
    db.session().commit()
    flash('Kiitos rekisteröitymisestä')

    return redirect(url_for('auth_login'))

      
