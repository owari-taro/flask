from flask import request
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.header.get('User-Agent')
    return f'<p>your browser is {user_agent}</p>'


if __name__ == "__main__":
    app.run(debug=False)
