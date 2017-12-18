from flask import Blueprint, render_template

from .. import utils
from ..ext import Pages


root = Blueprint('root', __name__)

@root.route('/')
def main(num_posts=3, num_projects=3):
    """Display a list of recent blog posts and portfolio projects"""
    blog_posts = utils.get_category(Pages, 'blog', n=num_posts)

    portfolio_projects = utils.get_category(Pages, 'portfolio', n=num_projects)

    return render_template('root/index.html',
                           articles=blog_posts,
                           projects=portfolio_projects)

@root.route('/about/')
def about():
    """About me page"""
    return render_template('root/about.html')

@root.route('/Del/')
def del_page():
    """Easter egg, you could say"""
    return render_template('root/del.html')

