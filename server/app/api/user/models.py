import bcrypt

from app.database import db, BaseMixin
from app.serializer import ma

class User(BaseMixin, db.Model):
    __tablename__ = "users"
    
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    _password = db.Column(db.LargeBinary(60))
    email = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    
    def __init__(self, username, password, email):
        self.username = username
        self._password = self.hash_pw(password.encode('utf-8'))
        self.email = email
        
    def hash_pw(self, password): 
        return bcrypt.hashpw(password, bcrypt.gensalt(13))
    
    def check_pw(self, password, hashed_pw):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_pw)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "is_active",
            "is_admin",
            
        )
