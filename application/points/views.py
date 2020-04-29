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
            fighter1_id=fighter1_id, fighter2_id=fighter2_id ,match_id=match_id,
                form=form)


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

    default_match_points=Points.get_points(match_id)

    points_to_save= Points.query.get_or_404(default_match_points[0]["id"])
    points_to_save.points=form.fighter1_points.data
    points_to_save.penalties= form.fighter1_penalties.data
    points_to_save.advantage=form.fighter1_advantages.data
    db.session().commit()

    points_to_save= Points.query.get_or_404(default_match_points[1]["id"])
    points_to_save.points=form.fighter2_points.data
    points_to_save.penalties= form.fighter2_penalties.data
    points_to_save.advantage=form.fighter2_advantages.data
    db.session().commit()

    return redirect(url_for("matches_index"))
    


@app.route("/points/edit/<match_id>", methods=["GET"])
@login_required
def points_editform(match_id):
    old_points = Points.get_points(match_id)
    old1= "{:d}|{:d}|{:d}".format(old_points[0]["points"], old_points[0]["penalties"], old_points[0]["advantage"])
    old2= "{:d}|{:d}|{:d}".format(old_points[1]["points"], old_points[1]["penalties"], old_points[1]["advantage"])
    
    fighter1=Fighter.query.get_or_404(old_points[0]["fighter_id"]).name
    fighter2=Fighter.query.get_or_404(old_points[1]["fighter_id"]).name
    
    return render_template("points/edit_points.html",form=PointForm(), old1=old1, old2=old2,
            fighter1=fighter1, fighter2=fighter2, match_id=match_id)
    

@app.route("/points/edit/", methods=["POST"])
@login_required
def edit_points():
  match_id=request.args.get('match_id')
  old_points= Points.get_points(match_id)
  fighter1=request.args.get('fighter1')
  fighter2=request.args.get('fighter2')
  old1=request.args.get('old1')
  old2=request.args.get('old2')
  print('****************', old_points)

  form=PointForm(request.form)
  if not form.validate():
    return render_template("points/edit_points.html",form=form, error='Luvut eivät kelpaa', old=old_points,
            old1=old1, old2=old2, fighter1=fighter1, fighter2=fighter2)

  
  points_to_edit= Points.query.get_or_404(old_points[0]["id"])
  points_to_edit.points=form.fighter1_points.data
  points_to_edit.penalties= form.fighter1_penalties.data
  points_to_edit.advantage=form.fighter1_advantages.data
  db.session().commit()

  points_to_edit= Points.query.get_or_404(old_points[1]["id"])
  points_to_edit.points=form.fighter2_points.data
  points_to_edit.penalties= form.fighter2_penalties.data
  points_to_edit.advantage=form.fighter2_advantages.data
  db.session().commit()

  return redirect(url_for("matches_index"))