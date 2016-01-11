#!/usr/bin/env python

from flask import Flask, send_from_directory
app = Flask(__name__)


DEBUG = True # oikeesti konffista


@app.route("/api/v1/hello")
def hello():
    return "Hello World!"


if DEBUG:
    @app.route("/static/<path:path>")
    def static_file(path):
        return send_from_directory('static', path)

    @app.route('/', defaults={'path': ''})
    @app.route("/<path:path>")
    def send_index(path):
        return send_from_directory('static', 'index.html')


if __name__ == "__main__":
    app.run()