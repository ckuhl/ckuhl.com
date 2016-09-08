from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("home_page.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
