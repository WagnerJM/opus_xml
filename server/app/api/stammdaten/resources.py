from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.stammdaten.models import SentosaSetting, SentosaUntersuchung, SentosaSettingSchema, SentosaUntersuchungSchema


class SentosaSettingListApi(Resource):
    def get(self):
        response = {}
        sentosaSettings = SentosaSetting.query.get(1)
        if sentosaSettings.is_active:
            schema = SentosaSettingSchema()
            response['status'] = "OK"
            response['sentosaSettings'] =  schema.dump(sentosaSettings).data
            return response, 200

        else:
            response['status'] = "NOT ACTIVE"
            response['message'] = "Keine aktive Einstellung gefunden"

            return response, 404

class SentosaSettingApi(Resource):
    def put(self, sentSett_id):
        pass

class SentosaUntersuchungListApi(Resource):
    def get(self):
        schema = SentosaUntersuchungSchema(many=True)
        sentosaUntersuchungen = SentosaUntersuchung.query.filter_by(
            sentosaSetting_id=1).first()
        return schema.dump(sentosaUntersuchungen).data, 200
        
    
    def post(self):
        pass

class SentosaUntersuchungApi(Resource):
    def put(self, sentUnters_id):
        pass
