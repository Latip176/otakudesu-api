from api.data import Home


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


@app.route("/api/otakudesu/home/")
def home():
    data = Home("https://otakudesu.cam/")
    return jsonify({"author": "Latip176", "data": data.results})


if __name__ == "__main__":
    app.run(debug=True)
