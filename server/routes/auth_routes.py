from flask import Blueprint, request, jsonify, session
from config import db
from models import User

auth_bp = Blueprint("auth", __name__)

# ✅ Signup Route
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "username": user.username}), 201

# ✅ Login Route 
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session["user_id"] = user.id  # ✅ store ID not username
        return jsonify({"message": "Login successful", "username": user.username}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# ✅ Check Session 
@auth_bp.route("/check_session", methods=["GET"])
def check_session():
    user_id = session.get("user_id")
    user = User.query.get(user_id) if user_id else None

    if user:
        return jsonify({"username": user.username, "id": user.id}), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401

# ✅ Logout Route
@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.pop("user_id", None)
    return jsonify({"message": "Logged out successfully"}), 200
