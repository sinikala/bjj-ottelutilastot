from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.fighters.models import Fighter
from application.fighters.forms import FighterForm


@app.route("/fighters", methods=["GET"])
def fighters_index():
    return render_template("fighters/list.html", fighters= Fighter.query.all())


@app.route("/fighters/new/")
@login_required
def fighters_form():
    return render_template("fighters/new.html", form= FighterForm())


@app.route("/fighters/", methods=["POST"])
@login_required
def fighters_create():
    form = FighterForm(request.form)

    if not form.validate():
        return render_template("fighters/new.html", form = form)

    name=form.name.data
    belt = dict(form.belt.choices).get(form.belt.data)
    club= form.club.data
    weight=form.weight.data
    creator_id= current_user.id

    f= Fighter(name, belt, club, weight, creator_id)
    db.session().add(f)
    db.session().commit()
  
    return redirect(url_for("fighters_index"))

@app.route("/fighters/<fighter_id>", methods=["GET"])
def fighter_info(fighter_id):

    fighter = Fighter.query.get(fighter_id)
    history= Fighter.get_match_history(fighter_id)
    
    return render_template("fighters/fighter.html", fighter=fighter, history=history)

@app.route("/fighters/edit/<fighter_id>", methods=["GET"])
@login_required
def fighters_editform(fighter_id):
    fighterToEdit = Fighter.query.get(fighter_id)

    form=FighterForm(formdata=request.form, obj=fighterToEdit)
    return render_template("fighters/edit_fighter.html", form= form, fighter_id=fighter_id)

@app.route("/fighters/edit/<fighter_id>/", methods=["POST"])
@login_required
def edit_fighter(fighter_id):

    fighterToEdit = Fighter.query.get(fighter_id)

    form=FighterForm(formdata=request.form, obj=fighterToEdit)
    if form.validate():
        fighterToEdit.name=form.name.data
        fighterToEdit.belt = dict(form.belt.choices).get(form.belt.data)
        fighterToEdit.club= form.club.data
        fighterToEdit.weight=form.weight.data

        db.session().commit()
        return redirect(url_for("fighters_index"))
    else:
        return render_template("fighters/edit_fighter.html", form = form)

@app.route("/fighters/<fighter_id>/", methods=["DELETE", "GET"])
@login_required
def remove_fighter(fighter_id):

    fighterToDelete = Fighter.query.get(fighter_id)
    db.session().delete(fighterToDelete)
    db.session().commit()
  
    return redirect(url_for("fighters_index"))