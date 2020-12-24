from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>hello world!</h1>'


@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello,{name}</h1>"


if __name__ == "__main__":
    # you can also invoke debug-mode with flask-command,see readme.md!
    # with debug mode,everytime rewrite any file,appserver is restarted
    app.run(debug=True)
