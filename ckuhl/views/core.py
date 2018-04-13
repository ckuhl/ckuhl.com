from flask import Blueprint, render_template

from .. import utils
from ..ext import Pages


core = Blueprint('core', __name__)


@core.route('/')
def main(num_posts=3, num_projects=3):
    """Display a list of recent blog posts and portfolio projects"""
    blog_posts = utils.get_category(Pages, 'blog', n=num_posts)

    portfolio_projects = utils.get_category(Pages, 'portfolio', n=num_projects)

    return render_template('core/index.j2',
                           articles=blog_posts,
                           projects=portfolio_projects)


@core.route('/about/')
def about():
    """About me page"""
    return render_template('core/about.j2')
