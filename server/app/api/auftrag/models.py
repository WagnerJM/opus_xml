from app.database import BaseMixin, db
from app.serializer import ma

class Autrag(db.Model, BaseMixin):
    __tablename__ = "auftrag"

    auftragID = db.Column(db.Integer, primary_key=True)
    anr = db.Column(db.Integer)
    untersuchungsname = db.Column(db.String)
    stemprop = db.Column(db.String)
    untersuchung_done = db.Column(db.Boolean, default=False)
    listen_id = db.Column(db.Integer, db.ForeignKey("listen.listID"))


    def __init__(self, anr, untersuchungsname, stemprop):
        self.anr = anr
        self.untersuchungsname = untersuchungsname
        self.stemprop = stemprop
    

class AuftragSchema(ma.ModelSchema):
    class Meta:
        model = Auftrag
        fields = (
            "id",
            "untersuchungsname"
            "anr",
            "untersuchung_done",
            ""
        )
