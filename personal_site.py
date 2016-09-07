from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Christian Kuhl\'s personal website!'


if __name__ == '__main__':
    app.run()
