#!/usr/bin/env python3

from app import app
from config import db
from datetime import datetime
from random import choice, randint
from models import Team, Player, Comment, FanPost

with app.app_context():
    print("🌱 Clearing old data...")
    Comment.query.delete()
    Player.query.delete()
    FanPost.query.delete()
    Team.query.delete()

    print("🌱 Seeding teams and players...")
    teams_data = [
        {
            "name": "Arsenal", "country": "England",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
            "players": ["Bukayo Saka", "Martin Ødegaard", "Gabriel Jesus", "Declan Rice", "William Saliba"]
        },
        {
            "name": "Barcelona", "country": "Spain",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
            "players": ["Robert Lewandowski", "Pedri", "Gavi", "Frenkie de Jong", "João Cancelo"]
        },
        {
            "name": "Bayern Munich", "country": "Germany",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/1/1f/FC_Bayern_München_logo_%282017%29.svg",
            "players": ["Thomas Müller", "Joshua Kimmich", "Alphonso Davies", "Jamal Musiala", "Harry Kane"]
        },
        {
            "name": "Juventus", "country": "Italy",
            "logo_url": "https://upload.wikimedia.org/wikipedia/commons/1/15/Juventus_FC_2017_logo.svg",
            "players": ["Federico Chiesa", "Dusan Vlahovic", "Manuel Locatelli", "Wojciech Szczęsny", "Adrien Rabiot"]
        },
        {
            "name": "PSG", "country": "France",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg",
            "players": ["Kylian Mbappé", "Gianluigi Donnarumma", "Achraf Hakimi", "Ousmane Dembélé", "Vitinha"]
        },
        {
            "name": "Real Madrid", "country": "Spain",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
            "players": ["Vinícius Jr", "Jude Bellingham", "Luka Modrić", "Toni Kroos", "Thibaut Courtois"]
        },
        {
            "name": "Manchester City", "country": "England",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg",
            "players": ["Erling Haaland", "Kevin De Bruyne", "Phil Foden", "Bernardo Silva", "Rodri"]
        },
        {
            "name": "Inter Milan", "country": "Italy",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/0/05/FC_Internazionale_Milano_2021.svg",
            "players": ["Lautaro Martínez", "Hakan Çalhanoğlu", "Nicolò Barella", "Denzel Dumfries", "Yann Sommer"]
        },
        {
            "name": "Chelsea", "country": "England",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
            "players": ["Enzo Fernández", "Raheem Sterling", "Reece James", "Christopher Nkunku", "Thiago Silva"]
        },
        {
            "name": "AC Milan", "country": "Italy",
            "logo_url": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Logo_of_AC_Milan.svg",
            "players": ["Rafael Leão", "Mike Maignan", "Olivier Giroud", "Theo Hernández", "Ismaël Bennacer"]
        },
        {
            "name": "Atletico Madrid", "country": "Spain",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg",
            "players": ["Antoine Griezmann", "Álvaro Morata", "Jan Oblak", "Rodrigo De Paul", "Koke"]
        },
        {
            "name": "Ajax", "country": "Netherlands",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/7/79/Ajax_Amsterdam.svg",
            "players": ["Steven Bergwijn", "Brian Brobbey", "Dusan Tadić", "Edson Álvarez", "Jurrien Timber"]
        },
        {
            "name": "Napoli", "country": "Italy",
            "logo_url": "https://upload.wikimedia.org/wikipedia/commons/2/2d/SSC_Napoli.svg",
            "players": ["Victor Osimhen", "Khvicha Kvaratskhelia", "Piotr Zieliński", "Stanislav Lobotka", "Giovanni Di Lorenzo"]
        },
        {
            "name": "Sevilla", "country": "Spain",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/5/56/Sevilla_CF_logo.svg",
            "players": ["Ivan Rakitić", "Youssef En-Nesyri", "Jesús Navas", "Suso", "Óliver Torres"]
        },
        {
            "name": "Tottenham", "country": "England",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg",
            "players": ["Son Heung-min", "James Maddison", "Cristian Romero", "Pedro Porro", "Dejan Kulusevski"]
        },
        {
            "name": "Dortmund", "country": "Germany",
            "logo_url": "https://upload.wikimedia.org/wikipedia/commons/6/67/Borussia_Dortmund_logo.svg",
            "players": ["Marco Reus", "Julian Brandt", "Mats Hummels", "Karim Adeyemi", "Gregor Kobel"]
        },
        {
            "name": "RB Leipzig", "country": "Germany",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/0/04/RB_Leipzig_2014_logo.svg",
            "players": ["Dani Olmo", "Timo Werner", "Xaver Schlager", "David Raum", "Yussuf Poulsen"]
        },
        {
            "name": "Lille", "country": "France",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/5/5d/Lille_OSC_2018_logo.svg",
            "players": ["Jonathan David", "Tiago Djaló", "Benjamin André", "Gabriel Gudmundsson", "Rémy Cabella"]
        },
        {
            "name": "Roma", "country": "Italy",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/f/f7/AS_Roma_logo_%282017%29.svg",
            "players": ["Paulo Dybala", "Lorenzo Pellegrini", "Tammy Abraham", "Bryan Cristante", "Chris Smalling"]
        },
        {
            "name": "Benfica", "country": "Portugal",
            "logo_url": "https://upload.wikimedia.org/wikipedia/en/8/89/SL_Benfica_logo.svg",
            "players": ["Ángel Di María", "Rafa Silva", "João Mário", "Otamendi", "Petar Musa"]
        },
    ]

    teams = []
    players = []

    for team_info in teams_data:
        team = Team(
            name=team_info["name"],
            country=team_info["country"],
            logo_url=team_info["logo_url"]
        )
        db.session.add(team)
        teams.append(team)

        for player_name in team_info["players"]:
            player = Player(
                name=player_name,
                position=choice(["Goalkeeper", "Defender", "Midfielder", "Winger", "Striker"]),
                goals=randint(0, 25),
                assists=randint(0, 15),
                appearances=randint(10, 38),
                team=team
            )
            players.append(player)
            db.session.add(player)

    db.session.commit()

    print("🌱 Seeding comments...")
    sample_users = [f"user{i}" for i in range(1, 21)]
    sample_contents = [
        "Great match!", "Terrible ref decision.", "That was a banger goal.",
        "Defending was poor today.", "We deserved the win.", "What a comeback!",
        "Fantastic team chemistry.", "Can't believe that miss.", "Clean sheet again!",
        "Hope the manager stays."
    ]

    comments = []
    for _ in range(80):
        comment = Comment(
            user=choice(sample_users),
            content=choice(sample_contents),
            team_id=choice(teams).id,
            player_id=choice(players).id
        )
        comments.append(comment)
    db.session.add_all(comments)
    db.session.commit()

    print("🌱 Seeding fan posts...")
    fan_contents = [
        "Supporting this team is a rollercoaster!",
        "Unbelievable matchday experience!",
        "We need to buy new defenders ASAP.",
        "What a tactical masterclass today!",
        "Emotional win for the lads!"
    ]
    fan_posts = []
    for i in range(1, 51):
        fan_post = FanPost(
            user=f"fan{i}",
            content=choice(fan_contents),
            timestamp=datetime.utcnow().isoformat()
        )
        fan_posts.append(fan_post)
    db.session.add_all(fan_posts)
    db.session.commit()

    print("✅ Seeding complete!")
