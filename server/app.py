#!/usr/bin/env python3

# 🌐 Core Flask & Extensions
from flask import Flask, request
from flask_migrate import Migrate
from flask_session import Session
from config import app, db, api  # app is assumed to be defined in config.py

# 🧩 Blueprints
from routes.team_routes import team_bp
from routes.player_routes import player_bp 
from routes.fanpost_routes import fanpost_bp  
from routes.auth_routes import auth_bp

# 🔁 Migration + Session Setup
app.secret_key = "supersecretkey"  # Needed for sessions
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

migrate = Migrate(app, db)

# 🔗 Register Blueprints
app.register_blueprint(team_bp, url_prefix="/teams")
app.register_blueprint(player_bp, url_prefix="/players")
app.register_blueprint(fanpost_bp, url_prefix="/fanposts")
app.register_blueprint(auth_bp, url_prefix="/auth")

# 🏠 Root Route
@app.route('/')
def index():
    return '<h1>⚽ Fanzone Tracker Server is Running</h1>'

# 🧠 Ensure models are imported for migrations
from models import Team, Player, Comment, FanPost, User

# 🚀 Run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
