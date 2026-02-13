from google import genai
from google.genai import types
from flask import request, jsonify
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

# System instruction for the Career Guru assistant
SYSTEM_INSTRUCTION = (
    "You are Career Guru, a friendly and knowledgeable AI career counselor. "
    "You ONLY answer questions related to careers, jobs, and professional development. "
    "This includes: career advice, resume and cover letter tips, interview preparation, "
    "job search strategies, skill development, salary negotiation, workplace challenges, "
    "professional networking, career transitions, and education/certification guidance. "
    "If a user asks anything unrelated to careers or professional growth, politely decline "
    "and remind them that you are a career-focused assistant. "
    "Keep your responses concise, actionable, and encouraging. "
    "Always respond in plain text only. Do not use any markdown formatting "
    "such as bold, italic, headers, bullet points, or numbered lists."
)

# Store active chat sessions (in-memory, per session_id)
chat_sessions = {}


def _get_or_create_session(session_id):
    """Get an existing chat session or create a new one."""
    if session_id not in chat_sessions:
        chat_sessions[session_id] = client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
            ),
        )
    return chat_sessions[session_id]


def chat():
    """
    POST /api/chat
    Body: { "message": "...", "session_id": "optional-session-id" }
    Returns: { "reply": "...", "session_id": "..." }
    """
    data = request.get_json()

    if not data or not data.get("message"):
        return jsonify({"error": "message is required"}), 400

    user_message = data["message"]
    session_id = data.get("session_id", "default")

    try:
        chat_session = _get_or_create_session(session_id)
        response = chat_session.send_message(user_message)

        return jsonify({
            "reply": response.text,
            "session_id": session_id,
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def clear_chat():
    """
    POST /api/chat/clear
    Body: { "session_id": "optional-session-id" }
    Clears the conversation history for the given session.
    """
    data = request.get_json() or {}
    session_id = data.get("session_id", "default")

    if session_id in chat_sessions:
        del chat_sessions[session_id]

    return jsonify({"message": "Chat history cleared", "session_id": session_id})
