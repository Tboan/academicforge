import os

from flask import Flask

# Criando instacia principal do Flask
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

# Rota para pagina inicial (home)
@app.route('/')
def home():
    return 'hello world -- Academic forge - {}'.format(os.environ['APP_SETTINGS'])


if __name__ == '__main__':
    app.run(debug=True)