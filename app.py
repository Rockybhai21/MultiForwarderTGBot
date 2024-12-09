from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello!</h1>"

def create_app():
   return app
    waitress-serve --port=8080 --call hello:create_app
% curl localhost:8080
<h1>Hello!</h1>%
