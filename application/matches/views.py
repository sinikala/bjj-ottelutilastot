from application import app, db
from flask import render_template, request, redirect, url_for
from application.matches.models import Match

@app.route("/matches", methods=["GET"])
def matches_index():
    return render_template("matches/list.html", matches = Match.query.all())

@app.route("/matches/new/")
def matches_form():
    return render_template("matches/new.html")

@app.route("/matches/<match_id>/", methods=["POST"])
def match_toggle_winner(match_id):

    m = Match.query.get(match_id)
    if (m.winner_id==1):
        m.winner_id=2
    else:
         m.winner_id=1
    db.session().commit()
  
    return redirect(url_for("matches_index"))

@app.route("/matches/<match_id>", methods=["DELETE", "GET"])
def match_remove_match(match_id):

    matchToDelete = Match.query.get(match_id)
    db.session().delete(matchToDelete)
    db.session().commit()
  
    return redirect(url_for("matches_index"))

@app.route("/matches/", methods=["POST"])
def matches_create():
    winning_category = request.form.get("winning_category")
    place = request.form.get("place")
    fighter1 = request.form.get("fighter1")
    fighter2 = request.form.get("fighter2")
    comment= request.form.get("comment")
    match = Match(place, winning_category, fighter1, fighter2, comment)


    db.session().add(match)
    db.session().commit()
  
    return redirect(url_for("matches_index"))