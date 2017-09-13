import logging
import os

from flask import Flask
from flask import abort
from flask import render_template
from flask_flatpages import FlatPages


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


# App setup
FLATPAGES_AUTO_RELOAD = SETTINGS['DEBUG']
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'static/posts'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']

app = Flask(__name__)
app.config.from_object(__name__)

pages = FlatPages(app)


# Helper code

def get_articles(n=999):
    # Articles are pages with a publication date
    articles = [p for p in pages if 'published' in p.meta and
                p.meta['published'] is True]
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['created'])
    return latest[:n]


# Page routing
## Homepage
@app.route('/')
def main():
    latest_posts = get_articles(5)[:5]
    return render_template('pages/home.html', articles=latest_posts)


## Blog pages
@app.route('/blog/')
def blog(n=999):
    return render_template('blog/blog.html', articles=get_articles(n=n)[:n])


@app.route('/blog/<path:path>/')
def blog_post(path):
    post = pages.get_or_404(path)

    if post.meta['published'] is False:
        abort(403)

    return render_template('blog/blog_post.html', post=post)


@app.route('/blog/tag/<string:slug>/')
def tag_page(slug):
    all_posts = get_articles()
    tagged = [p for p in all_posts if slug in p.meta['tags']]

    return render_template('blog/tagged_posts.html', tag=slug, articles=tagged)


## Portfolio pages
@app.route('/portfolio/')
def portfolio():
    return render_template('pages/portfolio.html')


## About pages
@app.route('/about/')
def about():
    return render_template('pages/about.html')


## Miscellaneous pages
@app.route('/misc/brick-breaker')
def brick_breaker():
    return render_template('misc/brick-breaker.html')


@app.route('/Del/')
def danielle():
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
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(403)
def page_forbidden(e):
    return render_template('errors/403.html'), 403


# Initialization
if __name__ == '__main__':
    app.run(debug=SETTINGS['DEBUG'], host='0.0.0.0', port=5000)

