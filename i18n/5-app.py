#!/usr/bin/env python3
"""Basic Babel setup & Parametrize templates"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__, template_folder="templates")
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """config class for babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get_locale method that determine the best match
    with our supported languages for the client's browser"""
    if "locale" in request.args:
        locale = request.args['locale']
        if locale in Config.LANGUAGES:
            return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    """get_user method"""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """before_request method"""
    g.user = get_user()


@app.route('/')
def index():
    """index method to render default template"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
