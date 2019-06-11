from app.database import db, BaseMixin
from app.serializer import ma
from marshmallow.fields import Nested

class SentosaSetting(db.Model, BaseMixin):
    __tablename__ = "sentosaSettings"

    sentosaID = db.Column(db.Integer, primary_key=True)
    auto_nk_amount = db.Column(db.Integer)
    sentosa_unters = db.relationship('SentosaUntersuchung', backref="SentosaSetting", lazy=False)
    auto_pk_anfang = db.Column(db.Boolean, default=False)
    auto_nk_anfang = db.Column(db.Boolean, default=False)

    def __init__(self, auto_nk_amount):
        self.auto_nk_amount = auto_nk_amount


class SentosaUntersuchung(db.Model, BaseMixin):
    __tablename__ = "sentosaUnters"

    sentosaUntersID = db.Column(db.Integer, primary_key=True)
    bezeichnung = db.Column(db.String)
    host_code = db.Column(db.String)
    sentosaSetting_id = db.Column(db.Integer, db.ForeignKey('sentosaSettings.sentosaID'))

    def __init__(self, bezeichnung, host_code):
        self.bezeichnung = bezeichnung
        self.host_code = host_code

    @classmethod
    def find_by_host_code(cls, host_code):
        return cls.query.filter_by(host_code=host_code).first()


class SentosaUntersuchungSchema(ma.ModelSchema):
    class Meta:
        model = SentosaUntersuchung
        fields = (
            "id",
            "bezeichnung",
            "host_code"
        )

class SentosaSettingSchema(ma.ModelSchema):
    sentosa_unters = Nested(SentosaUntersuchungSchema, many=True)
    class Meta:
        model = SentosaSetting
        fields = (
            "id",
            "auto_nk_amount",
            "auto_pk_anfang",
            "auto_nk_anfang",
            "is_active"
        )


