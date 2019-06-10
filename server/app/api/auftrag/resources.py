from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

class AuftragListApi(Resource):
    @jwt_required
    def get(self):
        pass

    @jwt_required
    def post(self):
        pass

class AufragApi(Resource):
    @jwt_required
    def put(self):
        pass 
