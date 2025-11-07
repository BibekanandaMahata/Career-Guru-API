from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route("/")
def welcome():
    return "Career Guru API is running successfully."

@app.route("/bgmi_players")
def test():
    return """Professional BGMI Players
Jonathan Gaming

Goblin

Sc0utOP

Mavi

Omega

AkshaT

ClutchGod

Ninja JOD

Snax

Vexe

Creative BGMI Player Name Ideas
Shadow Hunter

Blaze Phantom

Mystic Warrior

Rogue Titan

Venom Striker

Thunder Ghost

Inferno Slayer

Phantom Reaper

Night Stalker

Silent Predator

Steel Viper

Chaos Bringer

Storm Breaker

Frost Venom

Toxic Sniper

Dark Executioner

Lunar Assassin

Nova Killer

Iron Sentinel

Eclipse Warden"""

if __name__ == '__main__':
    app.run(debug=True, port=5000)