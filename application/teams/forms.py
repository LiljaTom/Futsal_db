from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TeamForm(FlaskForm):
    name = StringField("Team name", [validators.Length(min=3)])

    class Meta:
        csrf = False