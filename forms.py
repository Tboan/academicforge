from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class SingUp(Form):
    name = StringField('name')
    email = StringField('email')
    password = PasswordField('password')