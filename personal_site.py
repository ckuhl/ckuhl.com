from flask import Flask
from flask import abort
from flask import render_template
from flask_flatpages import FlatPages


# App setup
DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'static/posts'
FLATPAGES_MARKDOWN_EXTENSIONS = []

app = Flask(__name__)
app.config.from_object(__name__)

pages = FlatPages(app)


# Helper code

def get_articles(n=999):
    # Articles are pages with a publication date
    articles = [p for p in pages if 'published' in p.meta
                and p.meta['published'] is True]
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['created'])
    return latest[:n]


# Page routing

@app.route('/')
def main():
    latest_posts = get_articles(5)[:5]
    return render_template('pages/home.html', articles=latest_posts)


@app.route('/contact/')
def contact():
    return render_template('pages/contact.html')


@app.route('/blog/')
def blog(n=999):
    return render_template('blog/blog.html', articles=get_articles(n=n)[:n])


@app.route('/portfolio/')
def portfolio():
    return render_template('pages/portfolio.html')


@app.route('/about/')
def about():
    return render_template('pages/about.html')


@app.route('/blog/<path:path>/')
def blog_post(path):
    post = pages.get_or_404(path)

    if post.meta['published'] is False:
        abort(403)

    return render_template('blog/blog_post.html', post=post)


# turns out, you can't use `del` as a function name... Oops!
@app.route('/Del/')
def danielle():
    return render_template('pages/del.html')


# Pass through for Let's Encrypt's certbot to do its thing
@app.route('/.well-known/acme-challenge/<token_value>')
def letsencrpyt(token_value):
    with open('.well-known/acme-challenge/{}'.format(token_value)) as f:
        answer = f.readline().strip()
    return answer


# HTTP error codes

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(403)
def page_forbidden(e):
    return render_template('errors/403.html'), 403


if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)
