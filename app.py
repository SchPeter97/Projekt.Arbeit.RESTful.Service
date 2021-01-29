import flask


app = flask.Flask(__name__)


@app.route("/foo", methods=["GET"])
def check():
    return "test"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
