from flask import jsonify
from app import app

@app.route("/user")
def cricket_players():
    players = [
        {"name": "Rohit Sharma", "role": "Batsman (Captain)", "team": "India"},
        {"name": "Virat Kohli", "role": "Batsman", "team": "India"},
        {"name": "Shubman Gill", "role": "Batsman", "team": "India"},
        {"name": "Shreyas Iyer", "role": "Batsman", "team": "India"},
        {"name": "Suryakumar Yadav", "role": "Batsman", "team": "India"},
        {"name": "KL Rahul", "role": "Wicketkeeper-Batsman", "team": "India"},
        {"name": "Rishabh Pant", "role": "Wicketkeeper-Batsman", "team": "India"},
        {"name": "Hardik Pandya", "role": "All-Rounder (Vice-Captain)", "team": "India"},
        {"name": "Ravindra Jadeja", "role": "All-Rounder", "team": "India"},
        {"name": "Axar Patel", "role": "All-Rounder", "team": "India"},
        {"name": "Washington Sundar", "role": "All-Rounder", "team": "India"},
        {"name": "Jasprit Bumrah", "role": "Bowler", "team": "India"},
        {"name": "Mohammed Shami", "role": "Bowler", "team": "India"},
        {"name": "Mohammed Siraj", "role": "Bowler", "team": "India"},
        {"name": "Kuldeep Yadav", "role": "Spinner", "team": "India"},
        {"name": "Yuzvendra Chahal", "role": "Spinner", "team": "India"},
        {"name": "Rinku Singh", "role": "Batsman", "team": "India"},
        {"name": "Sanju Samson", "role": "Wicketkeeper-Batsman", "team": "India"},
        {"name": "Ishan Kishan", "role": "Wicketkeeper-Batsman", "team": "India"},
        {"name": "Arshdeep Singh", "role": "Bowler", "team": "India"}
    ]
    return jsonify({
        "status": "success",
        "count": len(players),
        "players": players
    })
