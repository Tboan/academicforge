import os

import re
from flask import Blueprint,render_template, request
from ..forms import SingUp
from ..models import UserModel
# Criando instacia principal do Flask

home_blueprint = Blueprint('home', __name__)

# Rota para pagina inicial (home)
@home_blueprint.route('/')
def home():
    user = UserModel.objects
    print(user)
    return render_template('home/home.html')


@home_blueprint.route('/cadastro', methods=('GET', 'POST'))
def singup():

    form = SingUp()
    if form.validate_on_submit():
        user = UserModel()
        user.name = form.name.data
        user.email = form.email.data
        user.password = form.password.data
        if user.name is None or len(user.name) == 0:
            return 'E necessario colocar o nome'

        if re.match('.*@centropaulasouza.com.br', user.email) is None:
            return 'Email deve ser um valido do centropaulasouza'

        if user.password is None or len(user.password) == 0:
            return 'Deve adicionar uma senha'

        user.save()
        return 'Confirmar Email'
    try:
        print(form.email.data, form.password.data, form.name.data)
    except Exception as e:
        print(e)
    return render_template('home/singup.html', form=form)


@home_blueprint.route('/confirma-email')
def confirma_email():
    return 'Confirmar email', 200
