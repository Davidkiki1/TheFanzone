import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from sqlalchemy import MetaData

db = SQLAlchemy()
migrate = Migrate()
api = Api()

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

def init_app():
    app = Flask(__name__)


    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///app.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")
    app.json.compact = False

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

    return app