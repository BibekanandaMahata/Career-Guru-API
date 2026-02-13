from flask import Flask
from flask_cors import CORS
from controller.chat_controller import chat, clear_chat

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


@app.route("/")
def welcome():
    return "Career Guru API is running successfully."


# Chat routes
app.add_url_rule("/api/chat", view_func=chat, methods=["POST"])
app.add_url_rule("/api/chat/clear", view_func=clear_chat, methods=["POST"])

if __name__ == '__main__':
    app.run(debug=True, port=5000)