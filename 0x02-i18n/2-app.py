#!/usr/bin/env python3
""" this is a documentation """

from flask import Flask, render_template, request
from flask_babel import Babel




class Config:
    """ this is a documentation """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/")
def home():
    """ this is a documentation """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
