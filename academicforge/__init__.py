import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine



# Criando instacia principal do Flask
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

db = MongoEngine(app)

from .views.home import home_blueprint
app.register_blueprint(home_blueprint)



