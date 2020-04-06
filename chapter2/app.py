from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>hello world</h1>"


@app.route("/user/<name>")
def user(name):
    return f"<h1>hello {name}</h1>"  # .format(name)


@app.route("/user_agent")
def user_agent():
    user_agent = request.headers.get("User-Agent")
    return f"<p>Your browser is {user_agent}"  # .format(user_agent)


if __name__ == "__main__":
    app.run()
