#!/usr/bin/env python3
""" Authentication Module """

from flask import Flask, request, jsonify, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/", methods=["GET"])
def home():
    """Return a JSON response with a welcome message"""
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def users():
    """Registers a new user"""
    email = request.form.get("email")
    password = request.form.get("password")
    
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route("/sessions", methods=["POST"])
def login():
    """Logs in a user and creates a session"""
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not AUTH.valid_login(email, password):
        abort(401)
    
    session_id = AUTH.create_session(email)
    if session_id is None:
        abort(401)
    
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
