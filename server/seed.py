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
    db.session.commit()  # Commit deletions

    print("🌱 Seeding teams and players...")
    positions = ["Goalkeeper", "Defender", "Midfielder", "Winger", "Striker"]
    countries = ["England", "Spain", "Germany", "Italy", "France", "Netherlands", "Portugal"]

    team_data = {
        "Arsenal": (1886, 48, "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg"),
        "Barcelona": (1899, 97, "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg"),
        "Bayern Munich": (1900, 80, "https://upload.wikimedia.org/wikipedia/en/1/1f/FC_Bayern_München_logo_%282017%29.svg"),
        "Juventus": (1897, 68, "https://upload.wikimedia.org/wikipedia/en/3/3e/Juventus_Turin.svg"),
        "PSG": (1970, 47, "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg"),
        "Real Madrid": (1902, 101, "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg"),
        "Manchester City": (1880, 35, "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg"),
        "Inter Milan": (1908, 42, "https://upload.wikimedia.org/wikipedia/en/0/05/Inter_Milan.svg"),
        "Chelsea": (1905, 34, "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg"),
        "AC Milan": (1899, 49, "https://upload.wikimedia.org/wikipedia/commons/d/d0/Logo_of_AC_Milan.svg"),
        "Atletico Madrid": (1903, 33, "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg"),
        "Ajax": (1900, 76, "https://upload.wikimedia.org/wikipedia/en/7/79/Ajax_Amsterdam.svg"),
        "Napoli": (1926, 15, "https://upload.wikimedia.org/wikipedia/en/2/2d/SSC_Napoli.svg"),
        "Sevilla": (1890, 18, "https://upload.wikimedia.org/wikipedia/en/5/5f/Sevilla_fc_logo.svg"),
        "Tottenham": (1882, 26, "https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg"),
        "Dortmund": (1909, 34, "https://upload.wikimedia.org/wikipedia/commons/6/67/Borussia_Dortmund_logo.svg"),
        "RB Leipzig": (2009, 2, "https://upload.wikimedia.org/wikipedia/en/0/04/RB_Leipzig_2014_logo.svg"),
        "Lille": (1944, 6, "https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Lille_OSC_2018_logo.svg/1200px-Lille_OSC_2018_logo.svg.png"),
        "Roma": (1927, 15, "https://upload.wikimedia.org/wikipedia/en/f/f7/AS_Roma_logo_%282017%29.svg"),
        "Benfica": (1904, 84, "https://upload.wikimedia.org/wikipedia/en/8/89/SL_Benfica_logo.svg")
    }

    team_ids = []
    player_ids = []

    for name, (year, trophies, logo) in team_data.items():
        team = Team(
            name=name,
            country=choice(countries),
            logo_url=logo,
            year_created=year,
            trophies=trophies
        )
        db.session.add(team)
        db.session.flush()  # flush to get team.id
        team_ids.append(team.id)

        for _ in range(11):
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
                team_id=team.id
            )
            db.session.add(player)
            db.session.flush()
            player_ids.append(player.id)

    db.session.commit()
    print(f"✅ Seeded {len(team_ids)} teams and {len(player_ids)} players.")

    print("🌱 Seeding users...")
    users = []
    for i in range(1, 201):
        user = User(username=f"fan{i}")
        user.set_password("password123")
        db.session.add(user)
        users.append(user)

    # Corrected: use is_dev instead of is_admin
    admin = User(username="admin", is_dev=True)
    admin.set_password("adminpass")
    db.session.add(admin)
    users.append(admin)

    db.session.commit()
    print(f"✅ Seeded {len(users)} users (incl. 1 admin).")

    print("🌱 Seeding fan posts...")
    fan_contents = [
        "Supporting this team is a rollercoaster!", "Unbelievable matchday experience!",
        "We need to buy new defenders ASAP.", "What a tactical masterclass today!",
        "Emotional win for the lads!", "Ref ruined the game.",
        "Our midfield is world class!", "Love this club forever.",
        "We’re going to win the league!", "Hope the manager signs a new contract."
    ]
    for _ in range(300):
        post = FanPost(
            user=choice(users),
            content=choice(fan_contents),
            timestamp=datetime.utcnow() - timedelta(days=randint(0, 60))
        )
        db.session.add(post)
    db.session.commit()
    print("✅ Seeded 300 fan posts.")

    print("🌱 Seeding comments...")
    comment_contents = [
        "Great match!", "Terrible ref decision.", "That was a banger goal.",
        "Defending was poor today.", "We deserved the win.", "What a comeback!",
        "Fantastic team chemistry.", "Can't believe that miss.", "Clean sheet again!",
        "Hope the manager stays."
    ]
    for _ in range(150):
        comment = Comment(
            user=choice(users).username,
            content=choice(comment_contents),
            team_id=choice(team_ids),
            player_id=choice(player_ids)
        )
        db.session.add(comment)
    db.session.commit()

    print("✅ Seeded 150 comments.")
    print("🎉 Database seeding complete!")
