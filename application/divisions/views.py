from application import app, db
from flask import render_template, request, redirect, url_for

from application.divisions.models import Division

@app.route("/divisions", methods=["GET"])
def divisions_index():
    return render_template("divisions/list.html", divisions = Division.query.all())

