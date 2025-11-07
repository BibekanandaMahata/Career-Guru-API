from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route("/")
def welcome():
    return "Career Guru API is running successfully."

@app.route("/home")
def home():
    return "This is the home page."

from controller.user_controller import *
from controller.product import *

if __name__ == '__main__':
    app.run(debug=True, port=5000)

