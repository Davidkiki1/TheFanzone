from config import db
from sqlalchemy_serializer import SerializerMixin
from .associations import fanposts_tags

class Team(db.Model, SerializerMixin):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    country = db.Column(db.String)
    logo_url = db.Column(db.String)

    players = db.relationship("Player", backref="team", cascade="all, delete")
    comments = db.relationship("Comment", backref="team", cascade="all, delete")
    fan_posts = db.relationship("FanPost", secondary=fanposts_tags, backref="teams")

    serialize_rules = ("-players.team", "-comments.team", "-fan_posts.teams")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "logo_url": self.logo_url,
            "players": [player.id for player in self.players],
            "comments": [comment.id for comment in self.comments],
        }

    def __repr__(self):
        return f"<Team {self.name}>"
