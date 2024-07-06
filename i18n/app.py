#!/usr/bin/env python3


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Configuration for Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@babel.localeselector
def get_locale():
    # Select the desired locale based on user preferences or browser settings
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
