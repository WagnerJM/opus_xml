import bcrypt
from app.database import db, BaseMixin
from app.serializer import ma


class User(db, BaseMixin):
    __tablename__ = "users"

    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    _password = db.Column(db.Binary(60))
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username, password):
        self.username = username
        self._password = self._hash_pw(password.encode('utf-8'))

    def _hash_pw(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt(14))

    def check_pw(self, password, hashed_password):
        return bcrypt.checkpw(password, hashed_password)

    

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = (
            "username"
        )