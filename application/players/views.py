from application import app, db
from flask import render_template, request, redirect, url_for

from flask_login import current_user, login_required

from application.players.models import Player
from application.players.forms import PlayerForm

@app.route("/players", methods=["GET"])
def players_index():
    return render_template("players/list.html", players = Player.query.all())


@app.route("/teams/<team_id>/players/new")
def players_form(team_id):
    return render_template("players/playerform.html", form = PlayerForm(), team_id = team_id)

@app.route("/teams/<team_id>/players/", methods=["POST"])
def players_create(team_id):
    form = PlayerForm(request.form)

    p = Player(form.name.data, form.number.data)
    p.team_id = team_id
    

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("players_index"))