from flask import Blueprint, render_template

from . import tools
from .extensions import Blog, Portfolio


root = Blueprint('root', __name__)

@root.route('/')
def main(blog_n=5, portfolio_n=4):
    """Display a list of recent blog posts and portfolio projects"""
    return render_template('root/index.html',
                           articles=tools.get_pages(Blog, n=blog_n),
                           projects=tools.get_pages(Portfolio, n=portfolio_n))

@root.route('/about/')
def about():
    """About me page"""
    return render_template('root/about.html')

@root.route('/Del/')
def del_page():
    """Easter egg, you could say"""
    return render_template('root/del.html')

