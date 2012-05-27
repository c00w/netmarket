from frontend import app
import flask

app.route("/search", methods=["POST", "GET"])
def search():
    return flask.render_template("search/search.html")
