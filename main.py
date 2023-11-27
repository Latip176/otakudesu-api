from api.index import Home
from api.reads import Reads
from api.view import View
from results import Output

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Accept"] = "application/json"
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


@app.route("/")
def index():
    return Output.results(None, "Welcome to my API", 200)


@app.route("/api/otakudesu/")
def otakudesu():
    return Output.results(
        None, "Cek Documentation in github.com/Latip176/otakudesu-api", 200
    )


@app.route("/api/otakudesu/info/")
def info():
    url = request.args.get("url")
    if url:
        Main = Reads(url=url)
        return Output.results(Main.results, "debug!", 200)
    return Output.results(None, "url is required!", 400)


@app.route("/api/otakudesu/view/")
def view():
    url = request.args.get("url")
    if url:
        Main = View(url=url)
        return Output.results(Main.results, "debug!", 200)
    return Output.results(None, "url is required!", 400)


@app.route("/api/otakudesu/home/")
def home():
    data = Home("https://otakudesu.cam/")
    return Output.results(data.results, "success", 200)


if __name__ == "__main__":
    app.run(debug=True)
