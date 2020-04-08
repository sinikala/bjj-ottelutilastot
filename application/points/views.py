from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.points.models import Point
from application.points.forms import PointForm
from application.fighters.models import Fighter


@app.route("/matches/new/points", methods=["GET"])
@login_required
def points_form():
    form=PointForm(request.form)
    
    fighters=Fighter.query.all()
    fighter1= Fighter.find_fighter_names(request.args.get('fighter1_id'), fighters)
    fighter2= Fighter.find_fighter_names(request.args.get('fighter2_id'), fighters)
    match_id=request.args.get('match_id')
    return render_template("points/points.html", fighter1=fighter1, fighter2=fighter2, form=form)


@app.route("/matches/new/points/", methods=["POST", "GET"])
@login_required
def add_points():
    form=PointForm(request.form)

    