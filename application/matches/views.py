from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.matches.models import Match
from application.matches.forms import MatchForm

@app.route("/matches", methods=["GET"])
def matches_index():
    return render_template("matches/list.html", matches = Match.query.all())

@app.route("/matches/new/")
@login_required
def matches_form():
    return render_template("matches/new.html", form= MatchForm())

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



@app.route("/matches/", methods=["POST"])
@login_required
def matches_create():
    form= MatchForm(request.form)

    if not form.validate():
        return render_template("matches/new.html", form = form)


    winning_category = dict(form.winning_category.choices).get(form.winning_category.data)
    place = form.place.data
    fighter1 = form.fighter1.data
    fighter2 = form.fighter2.data
    comment= form.comment.data
    match = Match(place, winning_category, fighter1, fighter2, comment)


    db.session().add(match)
    db.session().commit()
  
    return redirect(url_for("matches_index"))