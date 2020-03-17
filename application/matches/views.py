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

@app.route("/matches/", methods=["POST"])
def matches_create():
    place = Match(request.form.get("place"))
    #print(request.form.get("winning_category"))

    db.session().add(place)
    db.session().commit()
  
    return redirect(url_for("matches_index"))