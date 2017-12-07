import logging
import os

from flask import Flask
from flask import abort
from flask import render_template
from flask_flatpages import FlatPages

from ckuhl import tools


logger = logging.getLogger(__name__)

# settings configuration
# Check if a settings file exists, and if not, create it
if not os.path.exists(os.path.join('config', 'settings.py')):
    logger.info('Config not found, creating new config from template')
    from shutil import copyfile
    copyfile(os.path.join('config', 'settings.py.template'),
             os.path.join('config', 'settings.py'))

# Conditional import depending on if we're debugging or not
if __debug__:
    from config.settings import DEBUG as SETTINGS
else:
    from config.settings import PRODUCTION as SETTINGS


# Flatpages config
FLATPAGES_BLOG_ROOT = 'content/blog'
FLATPAGES_BLOG_AUTO_RELOAD = SETTINGS['IS_DEBUG']
FLATPAGES_BLOG_EXTENSION = '.md'
FLATPAGES_BLOG_MARKDOWN_EXTENSIONS = [
        'abbr',
        'codehilite',
        'smarty',
        'footnotes',
]

FLATPAGES_PORTFOLIO_ROOT = 'content/projects'
FLATPAGES_PORTFOLIO_AUTO_RELOAD = SETTINGS['IS_DEBUG']
FLATPAGES_PORTFOLIO_EXTENSION = '.md'
FLATPAGES_PORTFOLIO_MARKDOWN_EXTENSIONS = [
        'abbr',
        'codehilite',
        'smarty',
        'footnotes',
]

app = Flask(__name__)
app.config.from_object(__name__)

blog = FlatPages(app, name='blog')
portfolio = FlatPages(app, name='portfolio')

rss_feed_string = tools.generate_rss_feed(tools.get_pages(blog, n=20))

# Page routing
## Homepage
@app.route('/')
def main(blog_n=5, portfolio_n=4):
    """Display a list of recent blog posts and portfolio projects"""
    return render_template('pages/home.html',
                           articles=tools.get_pages(blog, n=blog_n),
                           projects=tools.get_pages(portfolio, n=portfolio_n))


## Blog pages
@app.route('/blog/')
def blog_home(blog_n=999):
    """Return a listing of blog posts"""
    return render_template('blog/index.html',
            articles=tools.get_pages(blog, n=blog_n))


@app.route('/blog/rss/')
def rss_feed():
    """
    Return the RSS feed
    """
    return rss_feed_string


@app.route('/blog/<path:path>/')
def blog_post(path):
    """Serve a given blog post (if it exists)"""
    post = blog.get_or_404(path)

    if post.meta['published'] is False:
        abort(403)

    return render_template('blog/post.html', post=post)


@app.route('/blog/tag/<string:slug>/')
def tag_page(slug):
    """Serve a listing of all blog posts tagged with a given tag"""
    all_posts = tools.get_pages(blog)
    tagged = [p for p in all_posts if slug in p.meta['tags']]

    return render_template('blog/tagged.html',
            tag=slug,
            articles=tagged)

## Portfolio pages
@app.route('/portfolio/')
def portfolio_home(n=999):
    """Serve a listing of portfolio projects"""
    return render_template('portfolio/index.html',
            projects=tools.get_pages(portfolio, n=n))


@app.route('/portfolio/<path:path>/')
def portfolio_project(path):
    """Serve a specific portfolio project"""
    post = portfolio.get_or_404(path)

    if post.meta['published'] is False:
        abort(403)

    return render_template('portfolio/project.html', post=post)


## About pages
@app.route('/about/')
def about():
    """About me page"""
    return render_template('pages/about.html')


## Miscellaneous pages
@app.route('/misc/brick-breaker')
def brick_breaker():
    """
    TODO: Keep this?
    A JavaScript game of brick breaker
    """
    return render_template('misc/brick-breaker.html')


@app.route('/Del/')
def danielle():
    """Special route"""
    return render_template('pages/del.html')


@app.route('/.well-known/acme-challenge/<token_value>')
def letsencrpyt(token_value):
    """
    Pass through for Let's Encrypt's certbot to do its thing
    """
    with open('.well-known/acme-challenge/{}'.format(token_value)) as f:
        answer = f.readline().strip()
    return answer


## HTTP error codes
@app.errorhandler(404)
def page_404(e):
    """Page not found"""
    return render_template('errors/404.html'), 404


@app.errorhandler(403)
def page_403(e):
    """Forbidden"""
    return render_template('errors/403.html'), 403


# Initialization
if __name__ == '__main__':
    app.run(debug=SETTINGS['IS_DEBUG'],
            host=SETTINGS['HOST'],
            port=SETTINGS['PORT'])

