import random

from flask import Flask, render_template, request

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


@app.route('/upload', methods=['GET', 'POST'])
def get_post_upload():
    if request.method == 'GET':
        return """
        <form method=post enctype=multipart/form-data>
        <input type=file name=file /><input type=submit value=upload />
        </form>
        """
    else:
        file = request.files["file"]
        file.save(file.filename)
        file.flush()

    return {"status": "ok"}


if __name__ == "__main__":
    app.run('0.0.0.0', port=80)
