#!/usr/bin/env python3
"""
Route module for the API
"""


from flask import Flask, jsonify, request
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS
from api.v1.auth.auth import Auth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

@app.before_request
def before_request():
    """Method to handler before request"""
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None:
        return jsonify({"error": "Unauthorized"}), 401
    if auth.current_user(request) is None:
        return jsonify({"error": "Forbidden"}), 403
    request.current_user = auth.current_user(request)  # Assigning current user

@app.teardown_appcontext
def teardown_db(exception):
    """ Close storage """
    storage.close()

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

