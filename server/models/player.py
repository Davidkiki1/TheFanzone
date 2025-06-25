from config import db
from sqlalchemy_serializer import SerializerMixin

class Player(db.Model, SerializerMixin):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    appearances = db.Column(db.Integer)

    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    comments = db.relationship("Comment", backref="player", cascade="all, delete")

    serialize_rules = ("-team.players", "-comments.player")