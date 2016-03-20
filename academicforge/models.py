from academicforge import db


class UserModel(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)