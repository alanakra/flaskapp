from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}