from flask import render_template, request,Flask

from my_app import app

@app.route("/")
@app.route("/hello")
def hello_world():
    user = request.args.get("user", "shalabh")
    return render_template("index.html", user=user)


