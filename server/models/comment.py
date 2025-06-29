from config import db

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)

    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=True)

    def __repr__(self):
        return f"<Comment {self.user[:10]}: {self.content[:20]}>"
