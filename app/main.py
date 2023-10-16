import os

from flask import Flask, render_template, request
import pandas as pd

import logging


logging.basicConfig(filename='application.log', level=logging.DEBUG)

APP = Flask(__name__)


@APP.route('/')
def home():
    return render_template(
        "home.html",
    )


if __name__ == '__main__':
    APP.run(debug=True)
