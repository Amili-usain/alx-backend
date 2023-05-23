#!/usr/bin/env python3
"""This module creates a get_locale function with the babel.localeselector
decorator and uses request.accept_languages to determine the best match with
our supported languages."""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)     # Configure Flask app
app.url_map.strict_slashes = False
babel = Babel(app)                 # Instantiate Babel object


@babel.localeselector
def get_locale() -> str:
    """Determine the best language match using request.accept_languages. """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Render the index.html template"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
