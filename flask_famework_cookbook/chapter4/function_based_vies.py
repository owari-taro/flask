from flask import Flask, request
app = Flask(__name__)


@app.route("/a-get-request")
def get_request():
    bar = request.args.get("foo", "bar")
    return "a simple flask request where foo is {bar}"


@app.route("/a-post-request", methods=["POST"])
def post_request():
    # in post,use form not args!
    bar = request.form.get("foo", "bar")
    return f"a simple flask request whrer foo is {bar}"

# compatible with both GET and POST
@app.route("/a-request", methods=["GET", "POST"])
def some_request():
    if request.method == "GET":
        bar = request.args.get("foo", "bar")
    else:
        bar = request.form.get("foo", "bar")
    return f"a simble flask request where foo is {bar}"


if __name__ == "__main__":
    app.run(debug=True)
