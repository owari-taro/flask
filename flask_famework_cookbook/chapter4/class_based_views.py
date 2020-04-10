from flask.views import View
from flask.views import MethodView
from flask import Flask

app = Flask(__name__)


class GetRquest(View):
    def dispatch_request(self):
        bar = request.args.get("foo", "bar")
        return f"a simple flask request where foo is {bar} "


class GetPostRequest(MethodView):
    def get(self):
        bar = request.args.get("foo", "bar")
        return f"a simple flask request where foo is {bar}"

    def post(self):
        bar = request.form.get("foo", "bar")
        return f"a simple flask request where foo is {bar}"


app.add_url_rule("/a-get-request", view_func=GetRquest.as_view("get_request"))
