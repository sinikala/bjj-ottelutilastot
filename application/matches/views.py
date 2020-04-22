from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.matches.models import Match
from application.matches.forms import MatchForm
from application.fighters.models import Fighter
from application.points.models import Points

@app.route("/matches", methods=["GET"])
def matches_index():
    matches = Match.query.all()
    all_fighters=Fighter.query.all()
    

    to_list=[]
    for match in matches:
        fighters= Match.get_fighters(match.id)
        fighter1=fighters[0]["name"]
        fighter2=fighters[1]["name"]
        winner= Fighter.find_fighter_names(match.winner_id,all_fighters)

        if match.winning_category=='Pistevoitto':
            p=Points.get_points(match.id)
            points= "{:d}|{:d}|{:d} - {:d}|{:d}|{:d}".format(p[0]["points"], p[0]["penalties"], p[0]["advantage"], p[1]["points"], p[1]["penalties"], p[1]["advantage"])
            to_list.append({"id": match.id, "date":match.date, "place": match.place, 
            "winner_id":match.winner_id, "winner":winner, "fighter1":fighter1, "fighter2":fighter2, "winning_category": match.winning_category, "comment":match.comment, "points":points})

        else:
            to_list.append({"id": match.id, "place": match.place, "date":match.date, 
            "winner_id":match.winner_id, "winner":winner, "fighter1":fighter1, "fighter2":fighter2, "winning_category": match.winning_category, "comment":match.comment})
        
    return render_template("matches/list.html", matches = to_list)

@app.route("/matches/new/", methods=["GET"])
@login_required
def matches_form():
    fighters=Fighter.query.all()
    names=[(i.id, i.name) for i in fighters]
    form= MatchForm()
    form.fighter1.choices=names
    form.fighter2.choices=names
    return render_template("matches/new.html", form= form)
    

@app.route("/matches/<match_id>/", methods=["POST"])
@login_required
def match_toggle_winner(match_id):

    m = Match.query.get(match_id)
    
    if (m.winner_id==m.fighter1_id):
        m.winner_id=m.fighter2_id
    else:
         m.winner_id=m.fighter1_id
    db.session().commit()
  
    return redirect(url_for("matches_index"))



@app.route("/matches/<match_id>", methods=["DELETE", "GET"])
@login_required
def match_remove_match(match_id):
    match_to_delete = Match.query.get(match_id)
    
    if match_to_delete.points:
        for points in match_to_delete.points:
            match_to_delete.points.remove(points)
            db.session().commit()

    db.session().delete(match_to_delete)
    db.session().commit()
  
    return redirect(url_for("matches_index"))



@app.route("/matches/", methods=["POST", "GET"])
@login_required
def matches_create():
    fighters=Fighter.query.all()
    names=[(i.id, i.name) for i in fighters]
    form= MatchForm(request.form)
    form.fighter1.choices=names
    form.fighter2.choices=names

    if not form.validate():
        return render_template("matches/new.html", form = form)

    winning_category = dict(form.winning_category.choices).get(form.winning_category.data)
    date=form.date.data
    place = form.place.data
    fighter1_id =form.fighter1.data
    fighter2_id =form.fighter2.data

    if fighter1_id==fighter2_id:
        return render_template("matches/new.html", form = form, 
                               error = "Valitse kaksi eri ottelijaa")

    winner=form.winner.data
    if winner==1:
        winner_id=fighter1_id
    else:
        winner_id=fighter2_id

    comment= form.comment.data
    creator_id= current_user.id
       
    match = Match(date, place, winning_category, fighter1_id, fighter2_id, winner_id, comment, creator_id)

    db.session().add(match)
    db.session().commit()

    fighter= Fighter.query.get(fighter1_id)
    match.fighters.append(fighter)
    db.session().commit()

    fighter= Fighter.query.get(fighter2_id)
    match.fighters.append(fighter)
    db.session().commit()

    if winning_category=='Pistevoitto':
        return redirect(url_for('points_form', fighter1_id=fighter1_id, fighter2_id=fighter2_id, match_id=match.id))
    else:
        return redirect(url_for("matches_index"))