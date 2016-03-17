from flask import render_template, url_for, redirect
from . import main
from .. import db


@main.route('/')
def index():
    """Default application route."""
    return render_template('index.html')
