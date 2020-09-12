from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class PlayerForm(FlaskForm):
    name = StringField("Player name")
    number = IntegerField("Player number")


    class Meta:
        csrf = False