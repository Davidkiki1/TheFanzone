from flask import Blueprint
from .team_routes import team_bp
from .player_routes import player_bp
from .fanpost_routes import fanpost_bp
from .auth_routes import auth_bp

all_routes = Blueprint('api', __name__)

all_routes.register_blueprint(team_bp, url_prefix="/teams")
all_routes.register_blueprint(player_bp, url_prefix="/players")
all_routes.register_blueprint(fanpost_bp, url_prefix="/fanposts")
all_routes.register_blueprint(auth_bp, url_prefix="/auth")