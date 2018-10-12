from flask import Blueprint, abort, render_template

from .. import utils
from ..ext import Pages


portfolio = Blueprint('portfolio', __name__)


@portfolio.route('/')
def index():
    """Serve a listing of portfolio projects"""
    return render_template('portfolio/home.j2',
                           projects=utils.filter_by_category(Pages,
                                                             'portfolio'))


@portfolio.route('/<path:path>/')
def project(path):
    """Serve a specific portfolio project"""
    post = Pages.get_or_404(path)

    if post.meta['published'] is False:
        abort(403)

    return render_template('portfolio/project.j2', post=post)
