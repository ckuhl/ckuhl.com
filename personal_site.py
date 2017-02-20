from flask import Flask
from flask import render_template
from flask_flatpages import FlatPages

# App constants
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'static/posts'
FLATPAGES_MARKDOWN_EXTENSIONS = []


# Flask init
app = Flask(__name__)
app.config.from_object(__name__)

# Flask-Flatpages init
pages = FlatPages(app)


@app.route("/")
def main():
    return render_template("pages/home.html")


@app.route("/contact/")
def contact():
    return render_template("pages/contact.html")


@app.route("/blog/")
def blog():
    # Articles are pages with a publication date
    articles = [p for p in pages if 'published' in p.meta
                and p.meta['published'] is True]
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['created'])
    return render_template("blog/blog.html", articles=latest)


@app.route("/portfolio/")
def portfolio():
    return render_template("pages/portfolio.html")


@app.route("/about/")
def about():
    return render_template("pages/about.html")


@app.route('/blog/<path:path>/')
def blog_post(path):
    post = pages.get_or_404(path)
    return render_template('blog/blog_post.html', post=post)


# turns out, you can't use `del` as a function name... Oops!
@app.route("/Del/")
def danielle():
    return render_template("pages/del.html")


# Pass through for Let's Encrypt's certbot to do its thing
@app.route('/.well-known/acme-challenge/<token_value>')
def letsencrpyt(token_value):
    with open('.well-known/acme-challenge/{}'.format(token_value)) as f:
        answer = f.readline().strip()
    return answer


if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0')
