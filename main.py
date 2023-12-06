from api.index import Home
from api.reads import Reads
from api.view import View
from api.search import Search
from results import Output

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# set header response
@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Accept"] = "application/json"
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


# index
@app.route("/")
def index():
    return Output.results(None, "Welcome to my API", 200)


# index api
@app.route("/api/otakudesu/")
def otakudesu():
    return Output.results(
        None, "Cek Documentation in github.com/Latip176/otakudesu-api", 200
    )


# get info of anime
@app.route("/api/otakudesu/info/")
def info():
    url = request.args.get("data")
    if url:
        Main = Reads(url="https://otakudesu.cam/anime/" + url)
        return Output.results(Main.results, "success", 200)
    return Output.results(None, "data is required!", 400)


# get strem by anime
@app.route("/api/otakudesu/view/")
def view():
    url = request.args.get("data")
    if url:
        Main = View(url="https://otakudesu.cam/episode/" + url)
        return Output.results(Main.results, "success", 200)
    return Output.results(None, "data is required!", 400)


# get all data by home otakudesu
@app.route("/api/otakudesu/home/")
def home():
    data = Home("https://otakudesu.wiki/")
    return Output.results(data.results, "success", 200)


# get data ongoing anime
@app.route("/api/otakudesu/ongoing/")
def ongoing():
    url = request.args.get("next")
    data = (
        Home("https://otakudesu.cam/ongoing-anime/" + url.replace("-", "/"), route=True)
        if url
        else Home("https://otakudesu.cam/ongoing-anime/", route=True)
    )
    return Output.results(data.results, "success", 200)


# search anime by keyword
@app.route("/api/otakudesu/search/")
def searchAnime():
    keyword = request.args.get("keyword")
    if keyword:
        keyword = keyword.replace(" ", "+")
        data = Search(url=f"https://otakudesu.cam/?s={keyword}&post_type=anime")
        return Output.results(data.results, "success", 200)
    return Output.results(None, "keyword is required!", 400)


if __name__ == "__main__":
    app.run()
