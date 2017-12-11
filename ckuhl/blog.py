import os

from flask import Blueprint, current_app, render_template
from flask_flatpages import FlatPages

from . import tools
from .extensions import Blog


blog = Blueprint('blog', __name__)

@blog.route('/')
def index(blog_n=999):
    """Return a listing of blog posts"""
    return render_template('blog/index.html',
            articles=tools.get_pages(Blog, n=blog_n))

@blog.route('/rss/')
def rss_feed():
    """
    Return the RSS feed
    """
    return tools.generate_rss_feed(tools.get_pages(Blog, n=20))

@blog.route('/<path:path>/')
def post(path):
    """Serve a given blog post (if it exists)"""
    post = Blog.get_or_404(path)

    if post.meta['published'] is False:
        abort(403)

    return render_template('blog/post.html', post=post)

@blog.route('/tag/<string:slug>/')
def tag_page(slug):
    """Serve a listing of all blog posts tagged with a given tag"""
    all_posts = tools.get_pages(Blog)
    tagged = [p for p in all_posts if slug in p.meta['tags']]

    return render_template('blog/tagged.html',
            tag=slug,
            articles=tagged)

