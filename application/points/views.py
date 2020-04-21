from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.points.models import Points
from application.points.forms import PointForm
from application.fighters.models import Fighter
from application.matches.models import Match



@app.route("/matches/new/points", methods=["GET"])
@login_required
def points_form():
    form=PointForm(request.form)
    fighters=Fighter.query.all()
    fighter1_id=request.args.get('fighter1_id')
    fighter2_id=request.args.get('fighter2_id')

    fighter1= Fighter.find_fighter_names(fighter1_id, fighters)
    fighter2= Fighter.find_fighter_names(fighter2_id, fighters)

    match_id=request.args.get('match_id')
    return render_template("points/points.html", fighter1=fighter1, fighter2=fighter2, 
            fighter1_id=fighter1_id, fighter2_id=fighter2_id ,match_id=match_id, form=form)


@app.route("/matches/new/points/", methods=["POST", "GET"])
@login_required
def add_points():
    form=PointForm(request.form)
    fighter1_id=request.args.get('fighter1_id')
    fighter2_id=request.args.get('fighter2_id')
    match_id=request.args.get('match_id')
   
    fighters=Fighter.query.all()
    fighter1= Fighter.find_fighter_names(fighter1_id, fighters)
    fighter2= Fighter.find_fighter_names(fighter2_id, fighters)

    if not form.validate():
        return render_template("points/points.html", error='Luvut eivät kelpaa',
            form = form, fighter1=fighter1, fighter2=fighter2, 
            fighter1_id=fighter1_id, fighter2_id=fighter2_id, match_id=match_id)

    match=Match.query.get(match_id)

    points=form.fighter1_points.data
    penalties= form.fighter1_penalties.data
    advantage=form.fighter1_advantages.data

    points_fighter1= Points(points, penalties, advantage, fighter1_id)
    db.session().add(points_fighter1)
    db.session().commit()

    points=form.fighter2_points.data
    penalties= form.fighter2_penalties.data
    advantage=form.fighter2_advantages.data

    points_fighter2= Points(points, penalties, advantage, fighter2_id)
    db.session().add(points_fighter2)
    db.session().commit()

    return redirect(url_for("matches_index"))
    #match.points.append(points_fighter1)
    #match.points.append(points_fighter2)

    #db.session().commit()