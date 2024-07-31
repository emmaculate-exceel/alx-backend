#!/usr/bin/env python3
""" babel object """
from flask import request, render_template
from flask_babel import Babel
import babel

app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config:
    """ selecting language for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'UTC'


def get_locale():
    """ select language """
    return request.accept_languages.best_match(
        app.config['LANGUAGES'])


app.config.from_object(Config)
