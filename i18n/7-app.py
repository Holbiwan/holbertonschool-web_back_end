#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext
import pytz

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    config translate
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""config app"""


@babel.localeselector
def get_locale():
    """
    get local lang
    """
    local_lang = request.args.get("locale")
    supp_lang = app.config["LANGUAGES"]
    if local_lang in supp_lang:
        return local_lang
    userID = request.args.get("login_as")
    if userID:
        local_lang = users[int(userID)]["locale"]
        if local_lang in supp_lang:
            return local_lang
    local_lang = request.headers.get('locale')
    if local_lang in supp_lang:
        return local_lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    return user dict
    """
    try:
        userID = request.args.get("login_as")
        return users[int(userID)]
    except Exception:
        return None


@app.before_request
def before_request():
    """
    find user
    """
    g.user = get_user()


@babel.timezoneselector
def get_locale():
    """
    time zone
    """
    userTime = request.args.get("timezone")
    if userTime in pytz.all_timezones:
        return userTime
    else:
        raise pytz.exceptions.UnknownTimeZoneError


@app.route("/")
def hello_world():
    """
    hello world
    """
    return render_template("6-index.html")
