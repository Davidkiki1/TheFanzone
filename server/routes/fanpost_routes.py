from flask import Blueprint, request, jsonify, session
from models import FanPost
from config import db
from datetime import datetime

fanpost_bp = Blueprint('fanposts', __name__)

@fanpost_bp.route('/', methods=['GET'])
def get_fanposts():
    posts = FanPost.query.all()
    return jsonify([post.to_dict() for post in posts])

@fanpost_bp.route('/', methods=['POST'])
def create_fanpost():
    user = session.get("user_id")
    if not user:
        return jsonify({"error": "Unauthorized. Please log in."}), 401

    data = request.get_json()
    post = FanPost(
        user=str(user),  # or you can load the User model and attach username if needed
        content=data['content'],
        timestamp=datetime.utcnow().isoformat()
    )
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201
