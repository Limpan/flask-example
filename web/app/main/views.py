from flask import render_template, url_for, redirect
from . import main
from .. import db
from ..models import Post
from .forms import PostForm


@main.route('/', methods=['GET', 'POST'])
def index():
    """Default application route."""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data)
        db.session.add(post)
        db.session.commit()

    posts = Post.query.all()
    return render_template('index.html', form=form, posts=posts)
