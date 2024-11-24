#!/usr/bin/env python3
""" this is a documentation """



from unittest import result
from flask import Flask, render_template, request
from flask_babel import Babel, numbers, gettext


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
    """ this is a documentation """
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """ this is a documentation """
    home_title = gettext("home_title")
    home_header = gettext("home_header")

    
    return render_template("3-index.html", home_header = home_header, home_title = home_title)


if __name__ == "__main__":
    app.run(debug=True)
