from flask import Blueprint, request, jsonify, session
from models import FanPost, User
from config import db

fanpost_bp = Blueprint('fanposts', __name__)

# 🔍 GET all fan posts (newest first)
@fanpost_bp.route('/', methods=['GET'])
def get_fanposts():
    posts = FanPost.query.order_by(FanPost.timestamp.desc()).all()
    return jsonify([post.to_dict(rules=('-user.password_hash',)) for post in posts]), 200

# 📝 CREATE new fan post (requires login)
@fanpost_bp.route('/', methods=['POST'])
def create_fanpost():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Unauthorized. Please log in."}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found."}), 404

    data = request.get_json()
    content = data.get("content", "").strip()
    if not content:
        return jsonify({"error": "Post content cannot be empty."}), 400

    post = FanPost(user_id=user_id, content=content)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict(rules=('-user.password_hash',))), 201

# ✏️ UPDATE a fan post (only by owner)
@fanpost_bp.route('/<int:id>', methods=['PATCH'])
def update_fanpost(id):
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    post = FanPost.query.get_or_404(id)
    if post.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    data = request.get_json()
    content = data.get("content", "").strip()
    if not content:
        return jsonify({"error": "Post content cannot be empty."}), 400

    post.content = content
    db.session.commit()
    return jsonify(post.to_dict(rules=('-user.password_hash',))), 200

# 🗑 DELETE a fan post (only by owner)
@fanpost_bp.route('/<int:id>', methods=['DELETE'])
def delete_fanpost(id):
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    post = FanPost.query.get_or_404(id)
    if post.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Fan post deleted successfully."}), 200
