from flask import Blueprint, request, jsonify
from models import Player
from config import db

player_bp = Blueprint('players', __name__)

# ✅ GET all players
@player_bp.route('/', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players]), 200

# ✅ GET a single player (with comments)
@player_bp.route('/<int:id>', methods=['GET'])
def get_player(id):
    player = Player.query.get_or_404(id)
    return jsonify({
        "player": player.to_dict(),
        "comments": [c.to_dict() for c in player.comments]
    }), 200

# ✅ POST a new player
@player_bp.route('/', methods=['POST'])
def create_player():
    data = request.get_json()

    player = Player(
        name=data['name'],
        position=data.get('position'),
        goals=data.get('goals', 0),
        assists=data.get('assists', 0),
        appearances=data.get('appearances', 0),
        age=data.get('age'),
        minutes_played=data.get('minutes_played'),
        yellow_cards=data.get('yellow_cards'),
        red_cards=data.get('red_cards'),
        rating=data.get('rating'),
        injured=data.get('injured', False),
        team_id=data['team_id']
    )

    db.session.add(player)
    db.session.commit()
    return jsonify(player.to_dict()), 201
