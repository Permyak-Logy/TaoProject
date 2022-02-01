from flask import Flask, render_template
app = Flask(__name__)
@app.route('/biba/<name>')
@app.route('/biba/')
def hello (name=None):
    return render_template("index.html",name = name)
@app.errorhandler(404)
def eror404 (e):
    return render_template("404.html"),404
@app.route("/kot")
def json():
    return{
        "id": 10,
        "name": "I",
        "age": 18
    }