from flask import Flask,request
app=Flask(__name__)

def get_request():
    bar=request.args.get("foo","bar")
    return f"a simple flask request where foo is {bar}"

if __name__ == "__main__":
    app.add_url_route("tmp",view_func=get_request())