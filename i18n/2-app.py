#!/usr/bin/env python3
""" Task 2: Get locale from request """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """Class to configure available languages in the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


babel = Babel(app)


@app.route('/')
def index():

    """Returning our html page"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """Getting locale from request.accept_languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
