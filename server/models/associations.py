from config import db

fanposts_tags = db.Table(
    "fanposts_tags",
    db.Column("fanpost_id", db.Integer, db.ForeignKey("fan_posts.id")),
    db.Column("team_id", db.Integer, db.ForeignKey("teams.id")),
)
