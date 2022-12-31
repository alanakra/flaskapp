from flask import Flask
from flask import render_template

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