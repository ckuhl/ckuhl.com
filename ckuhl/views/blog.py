from flask import Blueprint, abort, redirect, render_template, url_for

from .. import utils
from ..ext import Pages


blog = Blueprint('blog', __name__)


@blog.route('/')
def home():
    """Show a listing of recent blog posts"""
    BLOG_PAGES = 8
    posts = utils.filter_by_category(Pages, 'blog', n=BLOG_PAGES)
    blog_posts = [p for p in posts if p.meta['category'] != 'travel']
    return render_template('blog/home.j2',
                           articles=blog_posts)


@blog.route('/archive/')
def index():
    """Show a listing of all blog posts"""
    posts = utils.filter_by_category(Pages, 'blog')
    blog_posts = [p for p in posts if p.meta['category'] != 'travel']
    return render_template('blog/index.j2',
                           articles=blog_posts)


@blog.route('/index/')
def old_index():
    """Redirect URL"""
    return redirect(url_for('blog.index'))


@blog.route('/rss/')
def rss_feed():
    """Generate an RSS feed of blog posts"""
    RSS_FEED_ITEMS = 20
    posts = utils.filter_by_category(Pages, 'blog', n=RSS_FEED_ITEMS)
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
    posts = utils.filter_by_category(Pages, 'blog')
    tagged_posts = [p for p in posts if slug in p.meta['tags']]

    return render_template('blog/tagged.j2',
                           tag=slug,
                           articles=tagged_posts)
