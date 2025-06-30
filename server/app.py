from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_cors import CORS
from dotenv import load_dotenv
import os

# --- Load environment variables ---
load_dotenv()

# --- Init app ---
from config import init_app, db
app = init_app()

# --- Import models before migrations ---
from models import Team, Player, Comment, FanPost, User, fanposts_tags

# --- Migrations & Session setup ---
migrate = Migrate(app, db)
Session(app)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key")

# --- CORS setup ---
CORS(app, origins=["http://localhost:3000"], supports_credentials=True, allow_headers="*")


# --- Register blueprints ---
from routes.team_routes import team_bp
from routes.player_routes import player_bp
from routes.fanpost_routes import fanpost_bp
from routes.auth_routes import auth_bp
from routes.dev_routes import dev_bp

app.register_blueprint(team_bp, url_prefix="/teams")
app.register_blueprint(player_bp, url_prefix="/players")
app.register_blueprint(fanpost_bp, url_prefix="/fanposts")
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(dev_bp)

# --- Root test route ---
@app.route('/')
def index():
    return '<h1>⚽ Fanzone Tracker Server is Running</h1>'

# --- Run app ---
if __name__ == '__main__':
    app.run(port=5555, debug=True)
