from flask import Blueprint, render_template

from .. import utils
from ..ext import Pages


core = Blueprint('core', __name__)


@core.route('/')
def main():
    """List recent blog posts and portfolio projects"""
    NUM_BLOG_POSTS = 3
    NUM_PORTFOLIO_PAGES = 3

    blog_posts = utils.filter_by_category(Pages, 'blog', n=NUM_BLOG_POSTS)

    portfolio_projects = utils.filter_by_category(Pages, 'portfolio', n=NUM_PORTFOLIO_PAGES)

    return render_template('core/index.j2',
                           articles=blog_posts,
                           projects=portfolio_projects)


@core.route('/about/')
def about():
    """Static "About me" page"""
    return render_template('core/about.j2')


@core.route('/contact/')
def contact():
    """Static "Contact" page"""
    return render_template('core/contact.j2')
