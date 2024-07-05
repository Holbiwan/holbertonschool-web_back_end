#!/usr/bin/env python3
""" Flask app Module
"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)

# Configuration de Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'en'  # For testing purposes, force to 'en'


@app.route('/')
def index():

    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
