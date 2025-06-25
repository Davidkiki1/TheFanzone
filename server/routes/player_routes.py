from flask import Blueprint, request, jsonify
from models import Player
from config import db

player_bp = Blueprint('players', __name__)

@player_bp.route('/', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

@player_bp.route('/<int:id>', methods=['GET'])
def get_player(id):
    player = Player.query.get_or_404(id)
    return player.to_dict(), 200

@player_bp.route('/', methods=['POST'])
def create_player():
    data = request.get_json()
    player = Player(
        name=data['name'],
        position=data.get('position'),
        goals=data.get('goals', 0),
        assists=data.get('assists', 0),
        appearances=data.get('appearances', 0),
        team_id=data['team_id']
    )
    db.session.add(player)
    db.session.commit()
    return player.to_dict(), 201