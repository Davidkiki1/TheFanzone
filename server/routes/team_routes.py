from flask import Blueprint, request, jsonify
from models import Team
from config import db

team_bp = Blueprint('teams', __name__)

@team_bp.route('/', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return jsonify([team.to_dict() for team in teams])

@team_bp.route('/<int:id>', methods=['GET'])
def get_team(id):
    team = Team.query.get_or_404(id)
    return team.to_dict(), 200

@team_bp.route('/', methods=['POST'])
def create_team():
    data = request.get_json()
    team = Team(name=data['name'], country=data.get('country'), logo_url=data.get('logo_url'))
    db.session.add(team)
    db.session.commit()
    return team.to_dict(), 201