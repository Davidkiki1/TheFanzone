from config import db
from sqlalchemy_serializer import SerializerMixin

class FanPost(db.Model, SerializerMixin):
    __tablename__ = "fan_posts"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.String)

    serialize_rules = ("-teams.fan_posts",)