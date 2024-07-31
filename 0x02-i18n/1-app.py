#!/usr/bin/env python3
""" babel object """
from flask import request, render_template
from flask_babel import Babel
import babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ selecting language for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    hello world
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
