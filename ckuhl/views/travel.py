from flask import Blueprint, render_template
from flask_flatpages import FlatPages

from .. import utils
from ..ext import Blog


travel = Blueprint('travel', __name__)

@travel.route('/')
def home(blog_n=999):
    """return a listing of blog posts"""
    pages = utils.get_pages(Blog, n=blog_n)
    travel_blog = [p for p in pages if p.meta['category'] == 'travel']
    return render_template('travel/home.html',
            articles=travel_blog)

@travel.route('/<string:path>/')
def post(path):
    """Serve a given blog post (if it exists)"""
    post = Blog.get_or_404(path)

    if post.meta['published'] is False:
        abort(403)

    return render_template('travel/post.html', post=post)

