from flask import Blueprint, request, jsonify
from models import Team
from config import db

team_bp = Blueprint('teams', __name__)

@team_bp.route('/', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return jsonify([
        {
            "id": team.id,
            "name": team.name,
            "country": team.country,
            "logo_url": team.logo_url,
            "year_created": team.year_created,
            "trophies": team.trophies,
            "players": [player.id for player in team.players],
            "comments": [comment.id for comment in team.comments],
        } for team in teams
    ]), 200

@team_bp.route('/<int:id>', methods=['GET'])
def get_team(id):
    team = Team.query.get_or_404(id)
    return jsonify({
        "team": {
            "id": team.id,
            "name": team.name,
            "country": team.country,
            "logo_url": team.logo_url,
            "year_created": team.year_created,
            "trophies": team.trophies,
        },
        "players": [
            {
                "id": player.id,
                "name": player.name,
                "position": player.position,
                "goals": player.goals,
                "assists": player.assists,
                "appearances": player.appearances,
            } for player in team.players
        ],
        "comments": [
            {
                "id": comment.id,
                "user": comment.user,
                "content": comment.content,
            } for comment in team.comments
        ]
    }), 200

@team_bp.route('/', methods=['POST'])
def create_team():
    data = request.get_json()
    team = Team(
        name=data['name'],
        country=data.get('country'),
        logo_url=data.get('logo_url'),
        year_created=data.get('year_created'),
        trophies=data.get('trophies')
    )
    db.session.add(team)
    db.session.commit()
    return jsonify({
        "id": team.id,
        "name": team.name,
        "country": team.country,
        "logo_url": team.logo_url,
        "year_created": team.year_created,
        "trophies": team.trophies,
        "players": [],
        "comments": [],
    }), 201
