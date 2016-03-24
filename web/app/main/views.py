from flask import render_template, url_for, redirect
from . import main
from .. import db
from .models import User, Post


@main.route('/')
def index():
    """Default application route."""
    users = User.query.all()
    return render_template('index.html', users=users)
