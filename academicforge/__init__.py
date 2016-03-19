import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine

from .views.home import home_blueprint

# Criando instacia principal do Flask
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

db = MongoEngine(app)

app.register_blueprint(home_blueprint)
