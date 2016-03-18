import os

import re
from flask import Blueprint,render_template, request
from forms import SingUp
# Criando instacia principal do Flask

home_blueprint = Blueprint('home', __name__)

print(home_blueprint)

# Rota para pagina inicial (home)
@home_blueprint.route('/')
def home():
    return render_template('home/home.html')


@home_blueprint.route('/cadastro', methods=('GET', 'POST'))
def singup():

    form = SingUp()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        if name is None or len(name) == 0:
            return 'E necessario colocar o nome'

        if re.match('.*@centropaulasouza.com.br', email) is None:
            return 'Email deve ser um valido do centropaulasouza'

        if password is None or len(password) == 0:
            return 'Deve adicionar uma senha'
        return 'Confirmar Email'
    return render_template('home/singup.html', form=form)


@home_blueprint.route('/confirma-email')
def confirma_email():
    return 'Confirmar email'
