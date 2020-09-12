from application import app, db
from flask import render_template, request, redirect, url_for

from flask_login import current_user, login_required

from application.teams.models import Team
from application.teams.forms import TeamForm


@app.route("/teams", methods=["GET"])
def teams_index():
    return render_template("teams/list.html", teams = Team.query.all())

@app.route("/teams/new/")
@login_required
def teams_form():
    return render_template("teams/new.html", form = TeamForm())

@app.route("/teams/<team_id>")
def teams_getOne(team_id):
    t = Team.query.get(team_id)

    return render_template("teams/team.html", team = t)

@app.route("/teams/", methods=["POST"])
@login_required
def teams_create():
    form = TeamForm(request.form)

    if not form.validate():
        return render_template("teams/new.html", form = form)

    t = Team(form.name.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))