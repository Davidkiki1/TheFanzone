#!/usr/bin/env python3

from app import app
from config import db
from datetime import datetime
from faker import Faker
from random import choice, randint
from models import Team, Player, Comment, FanPost

faker = Faker()

with app.app_context():
    print("🌱 Clearing old data...")
    Comment.query.delete()
    Player.query.delete()
    FanPost.query.delete()
    Team.query.delete()

    print("🌱 Seeding teams...")
    team_names = [
        "Arsenal", "Barcelona", "Bayern Munich", "Juventus", "PSG",
        "Ajax", "Napoli", "Real Madrid", "Manchester City", "Inter Milan"
    ]
    teams = []
    for name in team_names:
        team = Team(name=name, country=faker.country(), logo_url=faker.image_url())
        teams.append(team)
    db.session.add_all(teams)
    db.session.commit()

    print("🌱 Seeding players...")
    positions = ["Goalkeeper", "Defender", "Midfielder", "Winger", "Striker"]
    players = []
    for _ in range(20):
        player = Player(
            name=faker.name(),
            position=choice(positions),
            goals=randint(0, 25),
            assists=randint(0, 15),
            appearances=randint(10, 38),
            team=choice(teams)
        )
        players.append(player)
    db.session.add_all(players)
    db.session.commit()

    print("🌱 Seeding comments...")
    comments = []
    for _ in range(30):
        comment = Comment(
            user=faker.user_name(),
            content=faker.sentence(nb_words=10),
            team_id=choice(teams).id,
            player_id=choice(players).id
        )
        comments.append(comment)
    db.session.add_all(comments)
    db.session.commit()

    print("🌱 Seeding fan posts...")
    fan_posts = []
    for _ in range(15):
        fan_post = FanPost(
            user=faker.user_name(),
            content=faker.paragraph(nb_sentences=3),
            timestamp=datetime.utcnow().isoformat()
        )
        fan_posts.append(fan_post)
    db.session.add_all(fan_posts)
    db.session.commit()

    print("✅Seeding complete!")
