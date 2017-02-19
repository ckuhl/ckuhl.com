from flask import Flask
from flask import render_template
from flask_flatpages import FlatPages

# TODO: Set easy way to switch debug state / caching state
DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


@app.route("/")
def main():
    return render_template("pages/home.html")


@app.route("/contact")
def contact():
    return render_template("pages/contact.html")


@app.route("/blog")
def blog():
    latest = sorted(pages, reverse=True,
                    key=lambda p: p.meta['date'])
    return render_template("blog/blog.html", pages=latest)


@app.route("/portfolio")
def portfolio():
    return render_template("pages/portfolio.html")


@app.route("/about")
def about():
    return render_template("pages/about.html")


@app.route('/blog/<path:path>/')
def blog_post(path):
    page = pages.get_or_404(path)
    return render_template('blog/blog_post.html', page=page)


@app.route("/Del")
def danielle():
    return render_template("pages/del.html")


@app.route('/.well-known/acme-challenge/<token_value>')
def letsencrpyt(token_value):
    with open('.well-known/acme-challenge/{}'.format(token_value)) as f:
        answer = f.readline().strip()
    return answer


if __name__ == "__main__":
    app.run(host='0.0.0.0')
