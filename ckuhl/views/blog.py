from flask import abort, Blueprint, render_template, redirect, url_for
from flask_flatpages import FlatPages

from .. import utils
from ..ext import Pages


blog = Blueprint('blog', __name__)


@blog.route('/')
def home(blog_n=8):
    """return a listing of blog posts"""
    posts = utils.get_category(Pages, 'blog', n=blog_n)
    blog_posts = [p for p in posts if p.meta['category'] != 'travel']
    return render_template('blog/home.j2',
            articles=blog_posts)


@blog.route('/archive/')
def index(blog_n=999):
    """return a listing of blog posts"""
    posts = utils.get_category(Pages, 'blog', n=blog_n)
    blog_posts = [p for p in posts if p.meta['category'] != 'travel']
    return render_template('blog/index.j2',
            articles=blog_posts)


@blog.route('/index/')
def old_index():
    """Redirect"""
    return redirect(url_for('blog.index'))


@blog.route('/rss/')
def rss_feed():
    """
    Return the RSS feed
    """
    posts = utils.get_category(Pages, 'blog', n=20)
    blog_posts = [p for p in posts if p.meta['category']]
    return utils.generate_rss_feed(blog_posts)


@blog.route('/<string:path>/')
def post(path):
    """Serve a given blog post (if it exists)"""
    p = Pages.get_or_404(path)

    if p.meta['published'] is False:
        abort(403)

    return render_template('blog/post.j2', post=p)


@blog.route('/tag/<string:slug>/')
def tag_page(slug):
    """Serve a listing of all blog posts tagged with a given tag"""
    posts = utils.get_category(Pages, 'blog')
    tagged_posts = [p for p in posts if slug in p.meta['tags']]

    return render_template('blog/tagged.j2',
            tag=slug,
            articles=tagged_posts)

