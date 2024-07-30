#!/usr/bin/env python3
# A flask app for a single route

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ route for the default page"""
    return render_template('0-index.html')
