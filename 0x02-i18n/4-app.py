#!/usr/bin/env python3
"""This module detects if the incoming request in the get_locale functio
contains locale argument and if value is a supported locale, returns it."""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Config class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best language match using request.accept_languages.
    If 'locale' parameter is present in the request and is a supported locale,
    use it as the preferred locale"""
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Render index.html template."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
