from app import app
from config import db
from models import User

with app.app_context():
    username = "devuser"
    password = "devpassword"

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        print(f"User '{username}' already exists.")
    else:
        user = User(username=username, is_dev=True)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print(f"Developer user '{username}' created successfully.")
