from config import db
from sqlalchemy_serializer import SerializerMixin

class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)

    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=True)

    serialize_rules = ("-team.comments", "-player.comments")