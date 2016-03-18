import os

from flask import Flask
from views.home import home_blueprint
# Criando instacia principal do Flask
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    app.run(debug=True)