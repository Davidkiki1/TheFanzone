from config import db
from sqlalchemy_serializer import SerializerMixin

class Team(db.Model, SerializerMixin):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    country = db.Column(db.String)
    logo_url = db.Column(db.String)
    year_created = db.Column(db.Integer)
    trophies = db.Column(db.Integer)

    players = db.relationship("Player", back_populates="team", cascade="all, delete")
    comments = db.relationship("Comment", backref="team", cascade="all, delete")
    fan_posts = db.relationship("FanPost", secondary="fanposts_tags", backref="teams")

    serialize_rules = ("-players",)

    def __repr__(self):
        return f"<Team {self.id}: {self.name}>"
