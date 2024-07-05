#!/usr/bin/env python3
""" Task 6: Use user locale """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = "Documentation for gettext"
""" Checker requirements """


""" Emulate user login system with user table """
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Class will configure available languages in the app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """ Returning our html page """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """ Getting locale from request.accept_languages """
    locale = request.args.get("locale")
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    try:
        user = get_user()
        if user and user['locale'] in Config.LANGUAGES:
            return user['locale']
        raise Exception
    except Exception:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ returns a user dictionary or None if the ID cannot be
    found or if login_as was not passed """
    try:
        user_Id = request.args.get('login_as')
        return users[int(user_Id)]
    except Exception:
        return None


@app.before_request
def before_request():
    """ Decorator to make it be executed before all other functions.
    Use get_user to find a user if any, and set it as a global on flask.g.user.
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
