from application import app, db
from flask import render_template, request, redirect, url_for

from application.teams.models import Team
from application.teams.forms import TeamForm


@app.route("/teams", methods=["GET"])
def teams_index():
    return render_template("teams/list.html", teams = Team.query.all())

@app.route("/teams/new/")
def teams_form():
    return render_template("teams/new.html", form = TeamForm())

@app.route("/teams/", methods=["POST"])
def teams_create():
    form = TeamForm(request.form)

    if not form.validate():
        return render_template("teams/new.html", form = form)

    t = Team(form.name.data)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))