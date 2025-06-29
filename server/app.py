#!/usr/bin/env python3

# 🌐 Core Flask & Extensions
from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_cors import CORS
from dotenv import load_dotenv
import os

# 🔄 Load environment variables
load_dotenv()

# ⚙️ App + DB Setup
from config import init_app, db
app = init_app()

# 🔐 Secret Key (used by Flask session)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key")  # ✅ Make sure it's set

# 💾 Configure Server-side Session
Session(app)

# 🔁 Migrate DB
migrate = Migrate(app, db)

# 🔗 Register Blueprints
from routes.team_routes import team_bp
from routes.player_routes import player_bp
from routes.fanpost_routes import fanpost_bp
from routes.auth_routes import auth_bp

app.register_blueprint(team_bp, url_prefix="/teams")
app.register_blueprint(player_bp, url_prefix="/players")
app.register_blueprint(fanpost_bp, url_prefix="/fanposts")
app.register_blueprint(auth_bp, url_prefix="/auth")

# ✅ CORS (Allow React frontend on port 3000 to send cookies)
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

# 🏠 Root Route
@app.route('/')
def index():
    return '<h1>⚽ Fanzone Tracker Server is Running</h1>'

# 📦 Ensure models are imported for migrations
from models import Team, Player, Comment, FanPost, User

# 🚀 Run the App
if __name__ == '__main__':
    app.run(port=5555, debug=True)
