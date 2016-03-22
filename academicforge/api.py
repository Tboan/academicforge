from flask_restful import Resource

from .models import UserModel

class EmailApi(Resource):

    def get(self, email):
        print(email)
        email = UserModel.objects.filter(email=email)
        if email:
            return {'msg': 'Email já existe na base'}, 200
        return {'msg': 'Email disponivel para uso'}, 404