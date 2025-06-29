from config import db
from datetime import datetime, timezone
from sqlalchemy_serializer import SerializerMixin

class FanPost(db.Model, SerializerMixin):
    __tablename__ = "fan_posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref="fan_posts")

    # Ensures user details (like username) are included.
    serialize_rules = ("-user.fan_posts",)

    def __repr__(self):
        return f"<FanPost by {self.user.username}>"
