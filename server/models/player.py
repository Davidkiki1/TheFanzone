from config import db
from sqlalchemy_serializer import SerializerMixin

class Player(db.Model, SerializerMixin):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String)
    goals = db.Column(db.Integer, default=0)
    assists = db.Column(db.Integer, default=0)
    appearances = db.Column(db.Integer, default=0)

    # Extended stats
    age = db.Column(db.Integer)
    minutes_played = db.Column(db.Integer)
    yellow_cards = db.Column(db.Integer)
    red_cards = db.Column(db.Integer)
    rating = db.Column(db.Float)
    injured = db.Column(db.Boolean)

    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team = db.relationship("Team", back_populates="players")  # ✅ use back_populates

    comments = db.relationship("Comment", backref="player", cascade="all, delete")

    # Prevent circular references
    serialize_rules = ("-comments", "-team.players")

    def __repr__(self):
        return f"<Player {self.id}: {self.name}>"
