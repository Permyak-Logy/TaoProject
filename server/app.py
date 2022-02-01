import random

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title="Hello")


@app.errorhandler(404)
def error_404(_):
    return render_template("404.html"), 404


@app.route('/index')
@app.route('/index/<int:id>')
def index2(id=None):
    return render_template("index2.html", title='index2', id=id)


@app.route('/api/people/<name>')
def get_people(name):
    return {"people": {
        "id": random.randrange(7 * 10 ** 8, 7 * 10 ** 8 + 2 * 10 ** 6),
        "name": name
    }}


if __name__ == "__main__":
    app.run('127.0.0.1', port=80)
