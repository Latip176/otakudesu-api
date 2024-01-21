from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from api.index import Home
from api.reads import Reads
from api.view import View
from api.search import Search
from api.genre import Genres
from results import Output

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)


# Set header response
@app.after_request
def add_header(response):
    response.headers["Content-Type"] = "application/json"
    return response


# INDEX API
@app.route("/")
def index():
    return Output.results(None, "Welcome to my API", 200)


# INDEX API
@app.route("/api/otakudesu/")
def otakudesu():
    return Output.results(
        None, "Check Documentation on github.com/Latip176/otakudesu-api", 200
    )


# INFO
@app.route("/api/otakudesu/info/")
def info():
    try:
        url = request.args.get("data")
        if url:
            Main = Reads(url="https://otakudesu.cam/anime/" + url)
            return Output.results(Main.results, "success", 200)
        return Output.results(None, "Data is required!", 400)
    except Exception as e:
        return Output.results({"data": None}, f"error {e}", 400)


# STREAM
@app.route("/api/otakudesu/view/")
def view():
    try:
        url = request.args.get("data")
        if url:
            Main = View(url="https://otakudesu.cam/episode/" + url)
            return Output.results(Main.results, "success", 200)
        return Output.results(None, "Data is required!", 400)
    except Exception as e:
        return Output.results({"data": None}, f"error {e}", 400)


# HOME
@app.route("/api/otakudesu/home/")
def home():
    try:
        data = Home("https://otakudesu.media/")
        return Output.results(data.results, "success", 200)
    except Exception as e:
        return Output.results({"data": None}, f"error {e}", 400)


# ONGOING
@app.route("/api/otakudesu/ongoing/")
def ongoing():
    try:
        url = request.args.get("next")
        data = (
            Home(
                "https://otakudesu.media/ongoing-anime/" + url.replace("-", "/"),
                route=True,
            )
            if url
            else Home("https://otakudesu.media/ongoing-anime/", route=True)
        )
        return Output.results(data.results, "success", 200)
    except Exception as e:
        return Output.results({"data": None}, f"error {e}", 400)


# SEARCH
@app.route("/api/otakudesu/search/")
def searchAnime():
    try:
        keyword = request.args.get("keyword")
        if keyword:
            keyword = keyword.replace(" ", "+")
            data = Search(url=f"https://otakudesu.media/?s={keyword}&post_type=anime")
            return Output.results(data.results, "success", 200)
        return Output.results(None, "Keyword is required!", 400)
    except Exception as e:
        return Output.results({"data": None}, f"error {e}", 400)


# GENRES
@app.route("/api/otakudesu/genres/")
def get_all_genres():
    try:
        data = Genres("https://otakudesu.media/genre-list/")
        return Output.results(data.get_genres(), "success", 200)
    except Exception as e:
        return Output.results({"data": None}, f"error {e}", 400)


@app.route("/api/otakudesu/genres/<genre>/")
@app.route("/api/otakudesu/genres/<genre>/<page>")
def get_genres(genre, page=None):
    try:
        data = Genres("https://otakudesu.media/genre-list/")
        if page:
            return Output.results(
                data.get_data(genre + "/page/" + page), "success", 200
            )
        return Output.results(data.get_data(genre), "success", 200)
    except Exception as e:
        return Output.results({"data": None}, f"error {e}", 400)


if __name__ == "__main__":
    app.run()
