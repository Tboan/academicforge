from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class SingUp(Form):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class LoginForm(Form):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])