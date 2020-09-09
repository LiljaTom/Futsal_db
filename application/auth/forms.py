from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username")
    password = StringField("Password")

    class Meta:
        csrf = False