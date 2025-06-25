from flask import Blueprint, request, jsonify
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
    data = request.get_json()
    post = FanPost(
        user=data['user'],
        content=data['content'],
        timestamp=datetime.utcnow().isoformat()
    )
    db.session.add(post)
    db.session.commit()
    return post.to_dict(), 201
