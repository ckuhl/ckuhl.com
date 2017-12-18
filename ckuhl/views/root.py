from flask import Blueprint, render_template

from .. import utils
from ..ext import Blog, Portfolio


root = Blueprint('root', __name__)

@root.route('/')
def main(num_posts=3, num_projects=3):
    """Display a list of recent blog posts and portfolio projects"""
    posts = utils.get_pages(Blog, n=num_posts)
    blog_posts = [p for p in posts if p.meta['category'] != 'travel']

    return render_template('root/index.html',
                           articles=blog_posts,
                           projects=utils.get_pages(Portfolio, n=num_projects))

@root.route('/about/')
def about():
    """About me page"""
    return render_template('root/about.html')

@root.route('/Del/')
def del_page():
    """Easter egg, you could say"""
    return render_template('root/del.html')

