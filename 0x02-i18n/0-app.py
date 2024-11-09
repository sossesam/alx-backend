#!/usr/bin/env python3
""" this is a documentation """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """ this is a documentation """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
