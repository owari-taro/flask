from flask import Flask


app=Flask(__nane__)

@app.route("/")
def index():
    return "<h1>hello world</h1>"

@app.route("/usr/<name>")
def user(name):
    return f"<h1>hello {name}!</h1>"