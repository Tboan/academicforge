import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_login import LoginManager
from flask_restful import Api




# Criando instacia principal do Flask
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

lm = LoginManager()
lm.init_app(app)

db = MongoEngine(app)
from .api import EmailApi

api = Api(app)

from .views.home import home_blueprint
app.register_blueprint(home_blueprint)

# Registrandos as APIs

api.add_resource(EmailApi, '/api/email/v0.1/<email>', endpoint='email_api')

from .models import UserModel

@lm.user_loader
def load_user(user_id):

    try:
        user = UserModel.objects.get(email=user_id)
    except Exception as e:
        user = None

    return user


