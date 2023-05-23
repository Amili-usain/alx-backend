#!/usr/bin/env python3
"""
This module defines a Basic Babel setup.
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Config class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)    # Configure Flask app
app.url_map.strict_slashes = False
babel = Babel(app)                # Instantiate Babel object


@app.route('/')
def get_index() -> str:
    """Render the index.html template."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
