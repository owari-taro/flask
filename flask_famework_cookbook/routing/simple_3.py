from flask.views import View
from flask import Flask



class GetRequest(View):
    methods=["GET","POST"]
    def dispatch_request(self):
        if request.method=="GET":
            bar=request.args.get("foo","bar")
        if request.method=="POST":
            bar=reuqest.form.get("foo","bar")
        #bar=request.args.get("foo","bar")
        return f"a simple flask where is {bar}"


if __name__=="__main__":
    app=Flask()
    app.add_url_rule("tmp",view_func=GetRequest.as_view("get_request"))
    app.run(debug=True)
