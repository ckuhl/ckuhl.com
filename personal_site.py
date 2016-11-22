from flask import Flask
from flask import render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


@app.route("/")
def main():
    return render_template("singletons/home_page.html")


@app.route("/contact")
def contact():
    return render_template("singletons/contact.html")


@app.route("/blog")
def blog():
    return render_template("blog/blog.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio/portfolio.html")


@app.route("/about")
def about():
    return render_template("singletons/about.html")


@app.route('/blog/<path:path>/')
def blog_post(path):
    page = pages.get_or_404(path)
    return render_template('blog/post.html', page=page)


@app.route('/projects/<path:path>/')
def portfolio_project(path):
    page = pages.get_or_404(path)
    return render_template('portfolio/project.html', page=page)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
