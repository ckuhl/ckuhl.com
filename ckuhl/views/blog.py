from flask import Blueprint, render_template
from flask_flatpages import FlatPages

from .. import utils
from ..ext import Blog


blog = Blueprint('blog', __name__)

@blog.route('/')
def home(blog_n=999):
    """return a listing of blog posts"""
    posts = utils.get_pages(Blog, n=blog_n)
    blog_posts = [p for p in posts if p.meta['category'] != 'travel']
    return render_template('blog/home.html',
            articles=blog_posts)


@blog.route('/index/')
def index(blog_n=999):
    """return a listing of blog posts"""
    posts = utils.get_pages(Blog, n=blog_n)
    blog_posts = [p for p in posts if p.meta['category'] != 'travel']
    return render_template('blog/index.html',
            articles=blog_posts)

@blog.route('/rss/')
def rss_feed():
    """
    Return the RSS feed
    """
    posts = utils.get_pages(Blog, n=20)
    blog_posts = [p for p in posts if p.meta['category'] != 'travel']
    return utils.generate_rss_feed(blog_posts)

@blog.route('/category/<string:cat>/rss/')
def category_rss(cat):
    """Generate a specific category blog post"""
    all_posts = utils.get_pages(Blog)
    posts_in_cat = [p for p in all_posts if p.meta['category'] == cat]

    return utils.generate_rss_feed(posts_in_cat)

@blog.route('/category/<string:cat>/')
def category(cat):
    """Serve all blog posts in a given category"""
    all_posts = utils.get_pages(Blog)
    posts_in_cat = [p for p in all_posts if p.meta['category'] == cat]

    return render_template('blog/category.html',
            category=cat,
            articles=posts_in_cat)

@blog.route('/<string:path>/')
def post(path):
    """Serve a given blog post (if it exists)"""
    post = Blog.get_or_404(path)

    if post.meta['published'] is False:
        abort(403)

    return render_template('blog/post.html', post=post)

@blog.route('/tag/<string:slug>/')
def tag_page(slug):
    """Serve a listing of all blog posts tagged with a given tag"""
    all_posts = utils.get_pages(Blog)
    tagged = [p for p in all_posts if slug in p.meta['tags']]

    return render_template('blog/tagged.html',
            tag=slug,
            articles=tagged)

