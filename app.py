import os

import re
from flask import Flask, render_template, request
from forms import SingUp
# Criando instacia principal do Flask
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

# Rota para pagina inicial (home)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastro', methods=('GET', 'POST'))
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
    return render_template('singup.html', form=form)

@app.route('/confirma-email')
def confirma_email():
    return 'Confirmar email'

if __name__ == '__main__':
    app.run(debug=True)