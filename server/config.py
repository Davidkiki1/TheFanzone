import os
# 📦 Standard & Remote Library Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from sqlalchemy import MetaData

# ✅ Extensions (global instances)
db = SQLAlchemy()
migrate = Migrate()
api = Api()

# ✅ Naming convention for Alembic migrations
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# ✅ init_app pattern
def init_app():
    app = Flask(__name__)

    # 🛠 App Config (now using environment variables for secrets and DB)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///app.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")
    app.json.compact = False

    # ✅ Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    # ✅ CORS with credentials support
    # For development, allow all origins. For production, restrict this!
    CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

    return app