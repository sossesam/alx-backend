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
    return "fr"
    #return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """ this is a documentation """
    us_num = numbers.format_decimal(1.2345, locale="en_US")
    se_num = numbers.format_decimal(1.2345, locale="sv_SE")
    results = {"us_num": us_num, "se_num": se_num}
    return render_template("2-index.html", result = results)


if __name__ == "__main__":
    app.run(debug=True)
