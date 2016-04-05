from academicforge import db

class DocumentModel(db.Document):
    project = db.ReferenceField('ProjectModel')

    meta = {'allow_inheritance': True}


class ProjectModel(db.Document):
    theme = db.StringField(required=True)
    owner = db.ReferenceField('UserModel')


class UserModel(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.email)


