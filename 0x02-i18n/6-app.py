#!/usr/bin/env python3
"""This determines the best language match using the following priority order:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Config class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Get the user dictionary based on the user ID."""
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """Execute before all other functions"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Determine the best language match using the following priority order """
    # 1. Locale from URL parameters
	locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    # 2. Locale from user settings
	if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    # 3. Locale from request header
	locale = request.headers.get('locale', '')
	if locale in app.config["LANGUAGES"]:
        return locale
   # 4. Default locale
   return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Render 6-index.html template"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
