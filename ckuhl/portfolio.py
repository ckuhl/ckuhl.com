from flask import Blueprint, render_template
from flask_flatpages import FlatPages

from . import tools
from .extensions import Portfolio

portfolio = Blueprint('portfolio', __name__)

@portfolio.route('/')
def index(n=999):
    """Serve a listing of portfolio projects"""
    return render_template('portfolio/index.html',
            projects=tools.get_pages(Portfolio, n=n))


@portfolio.route('/<path:path>/')
def project(path):
    """Serve a specific portfolio project"""
    post = Portfolio.get_or_404(path)

    if post.meta['published'] is False:
        abort(403)

    return render_template('portfolio/project.html', post=post)

