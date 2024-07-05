#!/usr/bin/env python3

""" Setup a basic Flask app """

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Renders a Basic Template for Babel Implementation"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
