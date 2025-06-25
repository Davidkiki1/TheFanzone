#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource
from config import app, db, api
from flask_migrate import Migrate
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

from models import Team, Player, Comment, FanPost


