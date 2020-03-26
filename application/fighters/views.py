from application import app, db
from flask import render_template, request, redirect, url_for
from application.fighters.models import Fighter
from application.fighters.forms import FighterForm


@app.route("/fighters", methods=["GET"])
def fighters_index():
    return render_template("fighters/list.html", fighters= Fighter.query.all())


@app.route("/fighters/new/")
def fighters_form():
    return render_template("fighters/new.html", form= FighterForm())


@app.route("/fighters/", methods=["POST"])
def fighters_create():
    form = FighterForm(request.form)

    if not form.validate():
        return render_template("fighters/new.html", form = form)

    name=form.name.data
    belt = dict(form.belt.choices).get(form.belt.data)
    club= form.club.data
    weight=form.weight.data

    f= Fighter(name, belt, club, weight)
    db.session().add(f)
    db.session().commit()
  
    return redirect(url_for("fighters_index"))



@app.route("/fighters/<fighter_id>", methods=["GET"])
def fighter_info(fighter_id):

    fighter = Fighter.query.get(fighter_id)
  
    return render_template("fighters/fighter.html", fighter=fighter)


@app.route("/fighters/<fighter_id>/", methods=["DELETE", "GET"])
def remove_fighter(fighter_id):

    fighterToDelete = Fighter.query.get(fighter_id)
    db.session().delete(fighterToDelete)
    db.session().commit()
  
    return redirect(url_for("fighters_index"))