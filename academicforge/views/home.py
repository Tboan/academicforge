import os

import re
from flask import Blueprint, render_template, url_for, redirect, request
from flask.ext.login import login_user, current_user, login_required, logout_user

from ..forms import SingUp, LoginForm
from ..models import UserModel

# Criando instacia principal do Flask

home_blueprint = Blueprint('home', __name__)


# Rota para pagina inicial (home)
@home_blueprint.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
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
        return redirect(url_for('dashboard.dashboard'))
    try:
        print(form.email.data, form.password.data, form.name.data)
    except Exception as e:
        print(e)
    return render_template('home/singup.html', form=form)


@home_blueprint.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('form valido')
        try:
            user = UserModel.objects.get(email=form.email.data)
            print('user objetido')
        except Exception:
            user = None

        if user is None:
            return render_template('home/login.html', form=form)

        if user.password == form.password.data:
            login_user(user)
            print('redirect')
            # next = request.args.get('next')

            # if not next_is_valid(next):
            #     return abort(400)
            return redirect(url_for('dashboard.dashboard'))

    return render_template('home/login.html', form=form)


@home_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))
