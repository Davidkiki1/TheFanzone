#!/usr/bin/env python3

from app import app
from config import db
from datetime import datetime, timedelta
from random import choice, randint, uniform
from models import Team, Player, Comment, FanPost, User
from faker import Faker

fake = Faker()

with app.app_context():
    print("🌱 Clearing old data...")
    Comment.query.delete()
    Player.query.delete()
    FanPost.query.delete()
    Team.query.delete()
    User.query.delete()

    print("🌱 Seeding teams and players...")
    positions = ["Goalkeeper", "Defender", "Midfielder", "Winger", "Striker"]
    countries = ["England", "Spain", "Germany", "Italy", "France", "Netherlands", "Portugal"]
    team_names = [
        "Arsenal", "Barcelona", "Bayern Munich", "Juventus", "PSG", "Real Madrid", 
        "Manchester City", "Inter Milan", "Chelsea", "AC Milan", "Atletico Madrid", 
        "Ajax", "Napoli", "Sevilla", "Tottenham", "Dortmund", "RB Leipzig", 
        "Lille", "Roma", "Benfica"
    ]

    teams = []
    players = []

    for team_name in team_names:
        team = Team(
            name=team_name,
            country=choice(countries),
            logo_url=fake.image_url()
        )
        db.session.add(team)
        teams.append(team)

        for _ in range(11):  # 11 players per team
            player = Player(
                name=fake.name(),
                position=choice(positions),
                goals=randint(0, 30),
                assists=randint(0, 20),
                appearances=randint(10, 38),
                rating=round(uniform(6.0, 9.8), 1),
                injured=choice([True, False]),
                minutes_played=randint(500, 3500),
                yellow_cards=randint(0, 10),
                red_cards=randint(0, 3),
                age=randint(18, 36),
                team=team
            )
            players.append(player)
            db.session.add(player)

    db.session.commit()

    print("🌱 Seeding users...")
    users = []
    for i in range(1, 201):
        user = User(username=f"fan{i}")
        user.set_password("password123")
        db.session.add(user)
        users.append(user)
    db.session.commit()

    print("🌱 Seeding fan posts...")
    fan_contents = [
        "Supporting this team is a rollercoaster!",
        "Unbelievable matchday experience!",
        "We need to buy new defenders ASAP.",
        "What a tactical masterclass today!",
        "Emotional win for the lads!",
        "Ref ruined the game.",
        "Our midfield is world class!",
        "Love this club forever.",
        "We’re going to win the league!",
        "Hope the manager signs a new contract."
    ]
    for _ in range(300):
        fan_post = FanPost(
            user=choice(users),
            content=choice(fan_contents),
            timestamp=datetime.utcnow() - timedelta(days=randint(0, 60))
        )
        db.session.add(fan_post)
    db.session.commit()

    print("🌱 Seeding comments...")
    sample_contents = [
        "Great match!", "Terrible ref decision.", "That was a banger goal.",
        "Defending was poor today.", "We deserved the win.", "What a comeback!",
        "Fantastic team chemistry.", "Can't believe that miss.", "Clean sheet again!",
        "Hope the manager stays."
    ]
    for _ in range(150):
        comment = Comment(
            user=choice(users).username,
            content=choice(sample_contents),
            team_id=choice(teams).id,
            player_id=choice(players).id
        )
        db.session.add(comment)
    db.session.commit()

    print("✅ Huge seeding complete!")
