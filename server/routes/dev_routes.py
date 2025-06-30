from flask import Blueprint, jsonify, current_app, request
from config import db
from models.user import User
from models.team import Team
from models.player import Player

dev_bp = Blueprint('dev', __name__)

# --- Info Route ---
@dev_bp.route("/dev/info")
def dev_info():
    return jsonify({
        "debug": current_app.debug,
        "database_uri": current_app.config.get("SQLALCHEMY_DATABASE_URI", "Not Found"),
        "secret_key_set": bool(current_app.secret_key),
        "user_count": User.query.count()
    })

# --- List Users ---
@dev_bp.route("/dev/users")
def dev_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

# --- Add Team ---
@dev_bp.route("/dev/teams", methods=["POST"])
def dev_add_team():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return {"error": "Team name is required."}, 400

    existing = Team.query.filter_by(name=name).first()
    if existing:
        return {"error": "Team already exists."}, 409

    team = Team(name=name)
    db.session.add(team)
    db.session.commit()

    return team.to_dict(), 201

# --- Delete Team ---
@dev_bp.route("/dev/teams/<int:team_id>", methods=["DELETE"])
def dev_delete_team(team_id):
    team = Team.query.get(team_id)
    if not team:
        return {"error": "Team not found."}, 404

    db.session.delete(team)
    db.session.commit()
    return {"message": f"Team '{team.name}' deleted successfully."}, 200

# --- Edit Player Stats ---
@dev_bp.route("/dev/players/<int:player_id>", methods=["PATCH"])
def dev_update_player_stats(player_id):
    player = Player.query.get(player_id)
    if not player:
        return {"error": "Player not found."}, 404

    data = request.get_json()
    
    # Update any matching attributes if they exist on the model
    updatable_fields = ["goals", "assists", "yellow_cards", "red_cards", "appearances"]
    for field in updatable_fields:
        if field in data:
            setattr(player, field, data[field])

    db.session.commit()
    return player.to_dict(), 200

@dev_bp.route("/dev/create-admin", methods=["POST"])
def dev_create_admin():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Username and password required"}, 400

    if User.query.filter_by(username=username).first():
        return {"error": "Username already exists"}, 409

    user = User(username=username, is_admin=True)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user.to_dict(), 201
