from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.matches.models import Match
from application.matches.forms import MatchForm
from application.fighters.models import Fighter

@app.route("/matches", methods=["GET"])
def matches_index():
    return render_template("matches/list.html", matches = Match.query.all())

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
    if (m.winner_id==1):
        m.winner_id=2
    else:
         m.winner_id=1
    db.session().commit()
  
    return redirect(url_for("matches_index"))



@app.route("/matches/<match_id>", methods=["DELETE", "GET"])
@login_required
def match_remove_match(match_id):

    matchToDelete = Match.query.get(match_id)
    db.session().delete(matchToDelete)
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
    place = form.place.data
    fighter1_id = dict(form.fighter1.choices).get(form.fighter1.label)
    fighter2_id = dict(form.fighter2.choices).get(form.fighter2.label)
    comment= form.comment.data
    creator_id= current_user.id
    match = Match(place, winning_category, fighter1_id, fighter2_id, comment, creator_id)

    if fighter1_id==fighter2_id:
        return render_template("matches/new.html", form = form,
                               error = "Valitse kaksi eri ottelijaa")

    db.session().add(match)
    db.session().commit()
  
    return redirect(url_for("matches_index"))